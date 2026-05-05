#!/usr/bin/env python3
"""거리뷰 + Vision 자동화 — 후보 주소 → 좌표 → Street View 4방향 → Claude Vision 분류.

사용:
    python detect_markers.py --candidates candidates.yaml --output detections.json
    python detect_markers.py --candidates candidates.yaml --limit 3   # 시범

환경변수:
    KAKAO_REST_API_KEY    카카오 로컬 API 지오코딩
    GOOGLE_MAPS_API_KEY   Google Static Street View API
    ANTHROPIC_API_KEY     Claude API
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
from enum import Enum
from pathlib import Path

import requests
import yaml
from anthropic import Anthropic
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# §10 변수 — Pydantic 스키마 (Claude Vision 구조화 출력용)
# ---------------------------------------------------------------------------


class StoneType(str, Enum):
    S1 = "S1"  # 오석/검은돌
    S2 = "S2"  # 다듬은 화강암
    S3 = "S3"  # 자연석
    S4 = "S4"  # 대리석
    S5 = "S5"  # 콘크리트/인조석
    UNKNOWN = "unknown"


class SizeClass(str, Enum):
    Z1 = "Z1"  # 소형 < 1m
    Z2 = "Z2"  # 중형 1~1.8m
    Z3 = "Z3"  # 대형 1.8~3m
    Z4 = "Z4"  # 초대형 > 3m
    UNKNOWN = "unknown"


class Engraving(BaseModel):
    language: str = Field(description="한자 / 한자+한글 / 한글 / 한글+영문 / unknown")
    script: str = Field(description="해서/행서/예서/전서/초서/명조/고딕/캘리그래피/민체/unknown")
    depth: str = Field(description="얕음 / 중간 / 깊음 / unknown")
    gilding: str = Field(description="무 / 백색충전 / 금박 / 채색 / unknown")
    intaglio: str = Field(description="음각 / 양각 / 평각 / unknown")


class MarkerAnalysis(BaseModel):
    marker_present: bool = Field(description="이미지에 마을 표석/돌비석이 보이는가")
    stone_type: StoneType
    size: SizeClass
    engraving: Engraving
    text_content: str = Field(description="표석에 새겨진 글자 (식별 가능한 만큼)")
    confidence: str = Field(description="high / medium / low")
    notes: str = Field(description="기타 관찰 (단지 풍경 / 식물에 가림 / 측면 등)")


# ---------------------------------------------------------------------------
# 시스템 프롬프트 — 캐시 대상
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """당신은 한국 마을표석을 분류하는 시각 분석 도구입니다.
이미지에 마을 입구의 돌비석/유래비/명패가 보이는지 식별하고, 보인다면 다음 변수를 분류합니다.

## 돌 종류 (stone_type)
- S1 = 오석(검은돌) — 검은 광택, 흰 글자 음각으로 강한 대비. 묘비·신도비의 격식
- S2 = 다듬은 화강암 — 회백~연분홍 입자가 보이는 매끈한 표면. 가장 보편적
- S3 = 자연석(원석) — 다듬지 않은 자연 형상, 이끼·풍화 흔적. 토속적
- S4 = 대리석/무늬돌 — 화려한 결무늬, 강한 광택
- S5 = 콘크리트/인조석 — 시멘트·미장·복합재. 신도시 후기 단지
- unknown — 사진에서 판별 불가

## 크기 (size) — 인접 인물·차·가로등 기준 추정
- Z1 = 소형 (< 1m) — 화단 안에 들어가는 안내석
- Z2 = 중형 (1~1.8m) — 인간 시선 높이. 가장 보편적
- Z3 = 대형 (1.8~3m) — 위압감. 기념비
- Z4 = 초대형 (> 3m) — 단독 랜드마크
- unknown

## 각자 (engraving)
- language: 한자 / 한자+한글 / 한글 / 한글+영문 / unknown
- script: 해서·행서·예서·전서·초서 (한자) / 명조·고딕·캘리그래피·민체 (한글) / unknown
- depth: 얕음 / 중간 / 깊음 / unknown
- gilding: 무도금 / 백색충전 / 금박 / 채색 / unknown
- intaglio: 음각 / 양각 / 평각 / unknown

## 신뢰도 (confidence)
- high — 표석 정면 클로즈업, 모든 변수 식별 가능
- medium — 표석은 보이나 일부 변수만 식별 (각자 흐릿함 등)
- low — 표석으로 추정되나 사진 해상도·각도 불충분

## 중요한 원칙
- 표석이 명확하지 않으면 marker_present=false, 다른 모든 필드 unknown
- 사진에 단지명 간판이 보여도 그것이 '돌비석' 형태가 아니면 marker_present=false
- 한국어로 답변. 글자 식별이 가능하면 text_content에 그대로 옮겨 적기
"""

# ---------------------------------------------------------------------------
# 외부 API
# ---------------------------------------------------------------------------


def geocode_kakao(address: str, api_key: str) -> tuple[float, float] | None:
    """카카오 로컬 API → (위도, 경도). 실패 시 None."""
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {"Authorization": f"KakaoAK {api_key}"}
    try:
        resp = requests.get(url, params={"query": address}, headers=headers, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  geocode 실패: {e}", file=sys.stderr)
        return None

    docs = resp.json().get("documents", [])
    if not docs:
        # 키워드 검색으로 fallback
        url2 = "https://dapi.kakao.com/v2/local/search/keyword.json"
        try:
            resp2 = requests.get(url2, params={"query": address}, headers=headers, timeout=10)
            resp2.raise_for_status()
            docs = resp2.json().get("documents", [])
        except requests.RequestException:
            return None
    if not docs:
        return None
    d = docs[0]
    return (float(d["y"]), float(d["x"]))  # (lat, lng)


def fetch_streetview(lat: float, lng: float, heading: int, api_key: str,
                     out_path: Path) -> bool:
    """Google Static Street View → JPEG 저장. 캐시 적중 시 fetch 생략."""
    if out_path.exists() and out_path.stat().st_size > 1000:
        return True
    url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "size": "640x640",
        "location": f"{lat},{lng}",
        "heading": str(heading),
        "fov": "90",
        "pitch": "0",
        "key": api_key,
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  streetview 실패: {e}", file=sys.stderr)
        return False

    # Google은 커버리지 없으면 회색 placeholder를 200으로 반환 — 크기로 거름
    if len(resp.content) < 5000:
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(resp.content)
    return True


# ---------------------------------------------------------------------------
# Claude Vision
# ---------------------------------------------------------------------------


def classify_image(client: Anthropic, image_path: Path, model: str) -> MarkerAnalysis | None:
    """Claude Vision로 이미지 분류. 실패 시 None."""
    image_data = base64.standard_b64encode(image_path.read_bytes()).decode("utf-8")

    try:
        response = client.messages.parse(
            model=model,
            max_tokens=1024,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "이 거리뷰 이미지에 마을표석이 보이는지 분류하세요.",
                        },
                    ],
                }
            ],
            output_format=MarkerAnalysis,
        )
    except Exception as e:
        print(f"  vision 실패: {e}", file=sys.stderr)
        return None

    return response.parsed_output


# ---------------------------------------------------------------------------
# 파이프라인
# ---------------------------------------------------------------------------


def process_candidate(client: Anthropic, candidate: dict, out_dir: Path,
                      kakao_key: str, google_key: str, model: str) -> dict:
    name = candidate["name"]
    cid = candidate["id"]
    print(f"\n[{cid}] {name} — {candidate['address']}", file=sys.stderr)

    coord = geocode_kakao(candidate["address"], kakao_key)
    if coord is None:
        return {**candidate, "status": "geocode_failed"}
    lat, lng = coord
    print(f"  좌표: {lat:.6f}, {lng:.6f}", file=sys.stderr)

    detections = []
    for heading in (0, 90, 180, 270):
        img_path = out_dir / "streetview" / f"{cid}_{name}_h{heading}.jpg"
        if not fetch_streetview(lat, lng, heading, google_key, img_path):
            print(f"  h{heading}: 거리뷰 없음", file=sys.stderr)
            continue

        analysis = classify_image(client, img_path, model)
        if analysis is None:
            continue
        print(
            f"  h{heading}: marker={analysis.marker_present} "
            f"stone={analysis.stone_type.value} size={analysis.size.value} "
            f"conf={analysis.confidence}",
            file=sys.stderr,
        )
        detections.append({
            "heading": heading,
            "image": str(img_path.relative_to(out_dir.parent)),
            "analysis": analysis.model_dump(),
        })

        time.sleep(0.5)  # rate limit

    # 가장 자신 있는 분석 선택
    best = None
    if detections:
        ranked = sorted(
            detections,
            key=lambda d: (
                d["analysis"]["marker_present"],
                {"high": 3, "medium": 2, "low": 1}.get(d["analysis"]["confidence"], 0),
            ),
            reverse=True,
        )
        best = ranked[0]

    return {
        **candidate,
        "lat": lat,
        "lng": lng,
        "detections": detections,
        "best": best,
        "status": "ok",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", default=Path("candidates.yaml"), type=Path)
    parser.add_argument("--output", default=Path("detections.json"), type=Path)
    parser.add_argument("--out-dir", default=Path("out"), type=Path,
                        help="이미지·캐시 저장 디렉토리")
    parser.add_argument("--limit", type=int, default=None,
                        help="처음 N개만 처리 (시범용)")
    parser.add_argument("--model", default="claude-opus-4-7",
                        help="Claude 모델. 비용 절감 시 claude-sonnet-4-6")
    args = parser.parse_args()

    kakao_key = os.environ.get("KAKAO_REST_API_KEY")
    google_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not kakao_key or not google_key:
        print("KAKAO_REST_API_KEY와 GOOGLE_MAPS_API_KEY 환경변수가 필요합니다.",
              file=sys.stderr)
        return 1

    with args.candidates.open(encoding="utf-8") as f:
        candidates = yaml.safe_load(f)["candidates"]
    if args.limit:
        candidates = candidates[: args.limit]

    client = Anthropic()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for c in candidates:
        try:
            results.append(process_candidate(
                client, c, args.out_dir, kakao_key, google_key, args.model
            ))
        except Exception as e:
            print(f"  처리 실패: {e}", file=sys.stderr)
            results.append({**c, "status": "error", "error": str(e)})

    args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2),
                           encoding="utf-8")
    print(f"\n결과: {args.output}", file=sys.stderr)
    print(f"  처리: {len(results)}건", file=sys.stderr)
    print(f"  marker_present=true: "
          f"{sum(1 for r in results if r.get('best', {}).get('analysis', {}).get('marker_present'))}건",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
