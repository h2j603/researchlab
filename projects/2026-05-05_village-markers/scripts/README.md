# 마을표석 자동화 파이프라인

`projects/2026-05-05_village-markers/findings.md` §11에서 정의한 4계층 발견 파이프라인을 실행하는 스크립트.

## 두 갈래

1. **`match_heritage.py`** — L1 백본. 공공데이터포털의 ‘전국향토문화유적표준데이터’ CSV를 받아 경기도 + ‘표석/비/유래비’ 키워드로 필터링하고 67개 후보와 매칭.
2. **`detect_markers.py`** — L4 자동화. 카카오 로컬 API로 후보 주소를 좌표로 변환 → Google Static Street View로 4방향 이미지 수집 → Claude Vision으로 §10 변수(돌·크기·각자) 추출.

각각 독립 실행 가능. 둘 다 돌리면 데이터셋 + 거리뷰가 결합된다.

## 설치

```bash
pip install -r requirements.txt
```

## API 키 발급 (한 번만)

| 키 | 발급처 | 무료 한도 | 환경변수 |
|----|--------|----------|---------|
| Kakao REST API | https://developers.kakao.com → 내 애플리케이션 → 앱 키 | 30,000 호출/일 (지오코딩) | `KAKAO_REST_API_KEY` |
| Google Maps Platform | https://console.cloud.google.com → API 사용 설정 → ‘Street View Static API’ + ‘Geocoding API’ | $200/월 무료 (~28,500 거리뷰) | `GOOGLE_MAPS_API_KEY` |
| Anthropic | https://console.anthropic.com → API Keys | 결제 등록 필요 | `ANTHROPIC_API_KEY` |

`.env` 파일을 만들어 한 번에 로드:

```bash
cat > .env <<'EOF'
KAKAO_REST_API_KEY=발급받은_키
GOOGLE_MAPS_API_KEY=발급받은_키
ANTHROPIC_API_KEY=sk-ant-...
EOF

set -a && source .env && set +a
```

## 사용법

### 1. L1 데이터셋 매칭

```bash
# (1) data.go.kr/15021147 페이지에서 CSV 직접 다운로드 (브라우저)
# (2) 받은 파일을 인자로 넘김
python match_heritage.py \
  --csv ~/Downloads/전국향토문화유적표준데이터.csv \
  --candidates candidates.yaml \
  --output matches.md
```

매칭 결과는 마크다운 표로 `matches.md`에 저장. 미매칭 후보는 별도 섹션으로 분리되어 거리뷰 단계로 넘어간다.

### 2. 거리뷰 + Vision 분류

```bash
# 시범: 처음 3개만
python detect_markers.py --candidates candidates.yaml --limit 3 --output detections.json

# 본격: 전체 67개
python detect_markers.py --candidates candidates.yaml --output detections.json
```

각 후보당:
- 카카오 로컬로 주소 → (위도, 경도)
- Google Street View Static API로 4방향 (heading 0/90/180/270) 캡처
- 각 이미지를 Claude Vision으로 분류 — `marker_present` / `stone_type` (S1~S5) / `size` (Z1~Z4) / 각자 5변수
- 결과 JSON + 다운로드된 이미지를 `out/` 디렉토리에 저장

### 옵션

- `--model` — 기본 `claude-opus-4-7`. 비용 압박 시 `claude-sonnet-4-6`도 가능. 정확도-비용 트레이드오프.
- `--limit N` — 처음 N개만 실행 (시범용)
- `--cache-dir` — 다운로드된 거리뷰 이미지 캐시 디렉토리 (기본 `out/streetview/`). 동일 좌표 재실행 시 fetch 생략.

## 출력

기본적으로 모든 산출물이 `out/` 디렉토리에 모인다.

```
out/
├── streetview/
│   ├── G15_백마마을_h0.jpg     # 좌표에서 동쪽
│   ├── G15_백마마을_h90.jpg    # 남쪽
│   ├── G15_백마마을_h180.jpg   # 서쪽
│   ├── G15_백마마을_h270.jpg   # 북쪽
│   ├── G16_밤가시마을_h0.jpg
│   ├── ...
└── detections.json               # 후보 × 4방향 × §10 변수
```

각 이미지는 `{후보ID}_{마을이름}_h{heading}.jpg` 형식으로 저장. 캐시 적중 (재실행 시 동일 좌표는 fetch 생략) 가능. `detections.json`의 각 항목에 `image` 필드로 경로가 기록되어 있어, 분류 결과와 이미지를 시각적으로 대조하기 쉽다.

`detections.json`을 `gyeonggi-cases.md` 표에 수동으로 옮기거나, 후속 스크립트로 자동 병합 가능.

## 한계와 비평

- **Google Street View 커버리지**: 한국 도시 도로는 대체로 잘 잡히지만, 단지 입구가 좁은 골목이거나 사유지 안쪽이면 누락된다. `marker_present: false`가 모두 ‘없다’를 의미하지 않는다 — ‘로드뷰에 안 잡혔다’일 수 있다.
- **카메라 방향의 한계**: 4방향 캡처로도 표석을 정면에서 못 잡을 수 있다. 표석은 보통 정문 옆 화단에 있어 도로뷰의 측면에 잡힌다 — 각자가 식별 안 되는 경우 다수.
- **Claude Vision의 한계**: 돌 종류 (S1)/(S2)/(S3) 구분은 사진 해상도·조명에 따라 오차. (S4)/(S5)는 더 어려움. 각자 식별은 정면 클로즈업이 있을 때만 신뢰 가능.
- **자동화의 함정**: 본 리서치의 핵심이 ‘현장 검증’이라는 점에서, 자동화는 **1차 후보 추출용**으로만 쓴다. §10 변수의 최종 측정은 사람이 직접 확인.

## 비용 추정

67개 후보 × 4 방향 = 268 이미지

- Google Street View: 268 × $0.007 = **$1.88** (월 $200 무료 한도 내)
- Kakao 지오코딩: 67 호출 (무료)
- Claude Opus 4.7 Vision (with prompt caching): 268 이미지 × ~1500 입력 토큰 + 200 출력 토큰. 캐시 적중 시 입력은 ~10% 비용. 추정 **$3~5**.
- Sonnet 4.6 사용 시 약 60% 절감 — **$1.5~2.5**.

총 약 **$5~10**으로 67개 후보를 1차 자동 분류. 완벽하지는 않지만 현장 답사 일정의 우선순위를 잡는 데 충분하다.
