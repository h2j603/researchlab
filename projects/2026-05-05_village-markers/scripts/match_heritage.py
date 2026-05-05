#!/usr/bin/env python3
"""L1 백본 매칭 — 전국향토문화유적표준데이터(data.go.kr/15021147)에서
경기도 + '표석/비/유래비' 키워드 행을 골라 후보 마을과 매칭.

사용:
    python match_heritage.py --csv ~/Downloads/heritage.csv \
        --candidates candidates.yaml --output matches.md
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

MARKER_KEYWORDS = ("표석", "비석", "유래비", "기념비", "마을표지", "지명비")


def load_candidates(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["candidates"]


def iter_gyeonggi_markers(csv_path: Path):
    """경기도 + 표석 키워드 행만 yield."""
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            address = (
                row.get("소재지지번주소")
                or row.get("소재지도로명주소")
                or row.get("주소")
                or ""
            )
            kind_blob = " ".join(
                str(row.get(k, ""))
                for k in ("향토문화유적종류", "유적분류", "소개", "내용", "명칭")
            )
            if "경기" not in address:
                continue
            if not any(kw in kind_blob for kw in MARKER_KEYWORDS):
                continue
            yield row


def match(markers: list[dict], candidates: list[dict]) -> dict[str, list[dict]]:
    """후보 → 매칭된 표석 리스트. 미매칭 후보는 빈 리스트."""
    by_candidate: dict[str, list[dict]] = {c["id"]: [] for c in candidates}

    # 각 표석 행마다 모든 후보와 비교
    for marker in markers:
        m_name = marker.get("명칭", "")
        m_addr = (
            marker.get("소재지지번주소")
            or marker.get("소재지도로명주소")
            or marker.get("주소")
            or ""
        )
        for c in candidates:
            # 1순위: 마을 이름이 표석 명칭에 포함
            if c["name"] in m_name:
                by_candidate[c["id"]].append({**marker, "_reason": "name"})
                continue
            # 2순위: 주소의 시·구·동 일부가 일치
            # 후보 주소를 단어로 분리해서 마지막 1~2개가 표석 주소에 등장하는지 확인
            tokens = c["address"].split()
            if len(tokens) >= 3:
                tail = " ".join(tokens[-2:])  # 예: "정발산동", "마두1동"
                if tail in m_addr:
                    by_candidate[c["id"]].append({**marker, "_reason": "address"})

    return by_candidate


def write_markdown(
    candidates: list[dict],
    matches: dict[str, list[dict]],
    output_path: Path,
) -> None:
    matched = [c for c in candidates if matches[c["id"]]]
    unmatched = [c for c in candidates if not matches[c["id"]]]

    lines: list[str] = []
    lines.append("# L1 데이터셋 매칭 결과")
    lines.append("")
    lines.append(
        f"전국향토문화유적표준데이터 → 경기도 + 표석 키워드 필터 → 후보 매칭. "
        f"매칭률: {len(matched)}/{len(candidates)} "
        f"({len(matched) / len(candidates) * 100:.1f}%)."
    )
    lines.append("")

    lines.append("## 매칭된 후보")
    lines.append("")
    if matched:
        lines.append("| 후보 ID | 마을 | 표석 명칭 | 표석 주소 | 좌표 | 매칭 근거 |")
        lines.append("|---|---|---|---|---|---|")
        for c in matched:
            for m in matches[c["id"]]:
                lat = m.get("위도") or m.get("Y좌표") or ""
                lng = m.get("경도") or m.get("X좌표") or ""
                addr = (
                    m.get("소재지지번주소")
                    or m.get("소재지도로명주소")
                    or m.get("주소")
                    or ""
                )
                lines.append(
                    f"| {c['id']} | {c['name']} | {m.get('명칭', '')} | "
                    f"{addr} | {lat},{lng} | {m['_reason']} |"
                )
    else:
        lines.append("(없음)")
    lines.append("")

    lines.append("## 미매칭 후보 (L4 거리뷰로 넘어갈 대상)")
    lines.append("")
    if unmatched:
        lines.append("| 후보 ID | 그룹 | 마을 | 주소 | 비고 |")
        lines.append("|---|---|---|---|---|")
        for c in unmatched:
            lines.append(
                f"| {c['id']} | {c['group']} | {c['name']} | "
                f"{c['address']} | {c.get('note', '')} |"
            )
    else:
        lines.append("(없음 — L1으로 모두 커버됨)")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=Path,
                        help="data.go.kr/15021147에서 받은 CSV 경로")
    parser.add_argument("--candidates", default=Path("candidates.yaml"),
                        type=Path, help="후보 YAML")
    parser.add_argument("--output", default=Path("matches.md"),
                        type=Path, help="결과 마크다운")
    args = parser.parse_args()

    if not args.csv.exists():
        print(f"CSV 파일이 없습니다: {args.csv}", file=sys.stderr)
        return 1

    candidates = load_candidates(args.candidates)
    markers = list(iter_gyeonggi_markers(args.csv))
    print(f"경기도 표석 후보 행: {len(markers)}건", file=sys.stderr)

    matches = match(markers, candidates)
    n_matched = sum(1 for v in matches.values() if v)
    print(f"매칭: {n_matched}/{len(candidates)}", file=sys.stderr)

    write_markdown(candidates, matches, args.output)
    print(f"결과: {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
