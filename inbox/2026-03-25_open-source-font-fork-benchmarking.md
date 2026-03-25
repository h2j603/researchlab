---
title: "오픈소스 기반 자체 서체 제작 벤치마킹"
date: 2026-03-25
updated: 2026-03-25
status: inbox
type: research
tags: [typography, font-distribution, case-study, tool]
related: ["2026-03-25_ai-font-creation-tools.md"]
confidence: medium
---

# 오픈소스 기반 자체 서체 제작 벤치마킹

오픈소스 폰트를 포크/변형하여 새 서체를 만든 사례와, 소규모 팀/개인이 오픈소스 도구로 처음부터 서체를 만든 사례를 조사한다.

---

## 1. 오픈소스 폰트 포크/변형으로 새 서체를 만든 사례

### 1-1. 대표적 포크 계보 (글로벌)

#### Bitstream Vera → DejaVu → Menlo / Hack

가장 유명한 오픈소스 폰트 포크 체인이다.

| 단계 | 서체 | 설명 |
|------|------|------|
| 원본 | **Bitstream Vera** | Bitstream이 자유 라이선스로 공개한 원본 서체 |
| 1차 포크 | **DejaVu** | Vera 기반, 유니코드 커버리지를 대폭 확장하는 것이 목표. 커뮤니티 프로젝트 |
| 2차 파생 | **Menlo** | Apple이 DejaVu Sans Mono를 변형하여 macOS 10.6에 기본 탑재 |
| 2차 파생 | **Hack** | DejaVu Sans Mono를 프로그래밍 환경에 최적화. 글리프 형태 재설계, 글리프셋 확장 |

- **시사점**: 하나의 좋은 원본에서 목적에 따라 여러 갈래로 분화하는 전형적 패턴. 각 포크마다 "유니코드 확장", "특정 용도 최적화" 등 명확한 목표가 있음.

#### Libre Franklin → Public Sans

| 항목 | 내용 |
|------|------|
| 원본 | **Libre Franklin** (SIL OFL) |
| 파생 | **Public Sans** — 미국 정부(USWDS)가 공식 서체로 사용하기 위해 포크 |
| 변경점 | 높이를 약 2% 줄임, 행간을 약간 넓힘, 소문자 `l`에 꼬리(hook) 추가하여 `1`과 구분 |
| 도구 | 오픈소스 도구 기반 수정 |

- **시사점**: 기관/정부도 기존 오픈소스를 포크하여 "약간의 수정"만으로 자체 서체를 만들 수 있다. 2%의 높이 차이, 한 글자의 형태 변경만으로도 "구별되는 서체"를 만든 사례.

#### IBM Plex → iA Writer 서체

| 항목 | 내용 |
|------|------|
| 원본 | **IBM Plex** (OFL) |
| 파생 | **iA Writer** 전용 서체 — IBM Plex를 "heavy modification"하여 제작 |
| 목적 | iA Writer 앱의 가독성 최적화 |

- **시사점**: 상업 앱이 오픈소스 폰트를 기반으로 자사 전용 서체를 만든 사례. "무에서 유"가 아니라 "기존 서체의 깊은 수정"으로 브랜드 아이덴티티를 확보.

### 1-2. 한국 사례 — 오픈소스 폰트 합성/포크

#### Sarasa Gothic (更紗ゴシック)

| 항목 | 내용 |
|------|------|
| 제작자 | Belleve Invis (개인 개발자) |
| 원본 | **본고딕/Source Han Sans** (한글·한자) + **Iosevka** (영문) |
| 방식 | 두 오픈소스 폰트를 합성(merge) |
| 특징 | TTF 형식, 힌팅 재작업으로 작은 글씨 가독성 향상, CJK 광범위 지원 |
| 유지보수 | 꾸준히 업데이트 중 |

- **시사점**: 개인 1인이 "기존 폰트 합성 + 힌팅 개선"이라는 방식으로 고품질 결과를 달성. 한글 폰트를 처음부터 만드는 것은 비현실적이지만, 합성은 개인도 가능.

#### Monoplex KR

| 항목 | 내용 |
|------|------|
| 원본 | **IBM Plex Mono** (영문) + **IBM Plex Sans KR** (한글) |
| 방식 | 영문 전용 코딩 폰트에 한글 글리프를 합성 |
| 목적 | IBM Plex Mono의 한글 미지원 문제 해결 |

#### JetBrainsMonoHangul

| 항목 | 내용 |
|------|------|
| 원본 | **JetBrains Mono** (영문) + **D2 Coding** (한글, 네이버) |
| 방식 | D2 Coding에서 한글 글리프를 추출하여 JetBrains Mono에 결합 |
| 문제점 | JetBrains Mono는 계속 업데이트되지만, 합성 버전은 업데이트 중단 |

- **시사점**: 합성 폰트의 고질적 문제 — 원본이 업데이트되면 합성본도 따라가야 하는데 개인이 유지보수하기 어려움.

#### Neo 둥근모 Code

| 항목 | 내용 |
|------|------|
| 원본 | **둥근모꼴** (1990년대 비트맵 폰트) |
| 방식 | 과거 비트맵 폰트를 TTF로 재제작, ligature 기능 추가 |
| 의의 | 레트로 폰트의 현대적 포맷 복원 |

#### D2 Coding (네이버)

| 항목 | 내용 |
|------|------|
| 원본 | **나눔바른고딕** (한글 베이스) |
| 방식 | 나눔바른고딕의 한글 + 새로 제작한 영문 코딩 글리프 결합 |
| 라이선스 | OFL — 재배포, 상용 프로그램 포함 허용 |
| 특징 | 한글이 부드러우면서 영문 코드와 자연스럽게 조화 |

### 1-3. 기타 글로벌 포크 사례

| 파생 서체 | 원본 | 변경 내용 |
|-----------|------|-----------|
| **Libertinus Serif** | Linux Libertine | 버그 수정 + 키릴 볼드 이탤릭 추가 |
| **Khartiya** | Bitstream Charter | 키릴 문자, 스몰캡, 올드스타일 숫자 추가 |
| **Fork Awesome** | Font Awesome | 아이콘 폰트의 커뮤니티 포크 |
| **Nerd Fonts** | 50+ 오픈소스 폰트 | 기존 폰트에 개발용 아이콘 글리프를 패치하여 합성 (3600+ 아이콘) |

---

## 2. 소규모 팀/개인이 오픈소스 도구로 처음부터 만든 서체 사례

### 2-1. 오픈소스 폰트 에디터 비교

| 도구 | 특징 | 적합 대상 | 환경 |
|------|------|-----------|------|
| **FontForge** | 가장 오래된 오픈소스 폰트 에디터. OTF/TTF/UFO 등 모든 형식 지원. 스크립팅(Python) 가능 | 중급 이상, 자동화 필요 시 | 데스크탑 (Win/Mac/Linux) |
| **Glyphr Studio v2** | 웹 기반, 초보/취미 타입 디자이너 최적화. SVG/OTF/TTF/WOFF 가져오기 지원 | 입문자, 취미 | 브라우저 (모바일 포함) |
| **Fontra** | 웹 기반, Variable Font 편집에 특화 | Variable Font 제작 | 브라우저 |
| **BirdFont** | 벡터 에디터와 폰트 에디터의 중간 형태 | 입문~중급 | 데스크탑 |

### 2-2. Glyphr Studio 탄생 사례 (1인 개발)

Glyphr Studio 자체가 "개인이 폰트를 만들고 싶었는데 도구가 없어서 도구부터 만든" 사례다.

| 항목 | 내용 |
|------|------|
| 시작 | 2010년, 제작자가 자체 폰트를 만들고 싶었으나 Windows용 무료 폰트 에디터가 없었음 |
| 결정 | HTML5 Canvas로 웹 기반 폰트 에디터를 직접 개발 |
| 현재 | Glyphr Studio v2로 진화, 오픈소스로 공개 |
| 철학 | "처음으로 서체를 만드는 사람이나 취미로 만드는 사람이 쉽게 폰트 파일을 만들 수 있도록" |

### 2-3. 전문가 혼합 워크플로우 (무료 도구 조합)

TypeDrawers 커뮤니티에서 공유된 실무 워크플로우:

1. **Fontra**에서 Variable Font 기본 설계
2. **FontForge**에서 OpenType 테이블 추가
3. **fonttools**, **nanoemoji** 등 Python 라이브러리로 컬러 테이블, 미세 조정
4. 최종 바이너리 빌드

- **시사점**: 무료 도구만으로도 전문 수준의 폰트 제작이 가능하지만, 여러 도구를 조합해야 하며 학습 곡선이 존재.

### 2-4. Velvetyne — 오픈소스 폰트 커뮤니티의 모범 사례

프랑스의 **Velvetyne Type Foundry**는 오픈소스 폰트만을 제작·배포하는 독립 파운드리다.

| 항목 | 내용 |
|------|------|
| 형태 | 소규모 디자이너 커뮤니티/파운드리 |
| 철학 | 모든 서체를 무료·오픈소스로 공개 |
| 워크숍 | "Font Fonk Fork" 워크숍 — Cooper Hewitt 서체를 참가자들이 각자 포크하여 변형본을 만드는 실습 |
| 도구 | 다양한 오픈소스 도구 활용 |
| 결과물 | 실험적이면서도 높은 퀄리티의 디스플레이 서체 다수 |

- **시사점**: 소규모 커뮤니티가 오픈소스 도구와 라이선스를 활용하여 지속적으로 고퀄리티 서체를 생산할 수 있음을 증명.

### 2-5. 제작 기간 참고

| 범위 | 예상 기간 |
|------|-----------|
| 영문 기본 글리프 (A-z, 0-9, 기호) | 수 주 (초보 기준) |
| 영문 완성 세트 + 다이어크리틱 | 1~3개월 |
| 멀티 웨이트/스타일 패밀리 | 6개월~1년 |
| CJK(한중일) 포함 전체 유니코드 | 수 년 (팀 필요) |
| 기존 폰트 포크 + 부분 수정 | 수 일~수 주 |
| 기존 폰트 합성 (merge) | 수 일 (스크립팅 활용 시) |

---

## 3. 라이선스 핵심 정리

오픈소스 폰트 포크/변형의 법적 근거:

### SIL Open Font License (OFL)
- 사용, 연구, 수정, 재배포 자유
- **Reserved Font Name(예약 이름)** 제도: 원본 이름이 예약되어 있으면 포크 시 반드시 이름을 변경해야 함
- 폰트 단독 판매는 불가 (다른 소프트웨어에 번들은 가능)

### Apache 2.0
- OFL보다 더 유연한 상업적 활용
- Roboto 등 Google 계열 폰트에 주로 사용

---

## 4. 핵심 시사점 요약

1. **"무에서 유" 보다 "포크 + 수정"이 현실적**: Public Sans(Libre Franklin 포크, 2% 높이 차이만으로 별도 서체), iA Writer(IBM Plex 기반 깊은 수정) 등 증명
2. **한글은 합성(merge) 전략이 유효**: Sarasa Gothic, Monoplex KR 등 — 영문 오픈소스 + 한글 오픈소스를 합성하는 패턴이 반복적으로 성공
3. **개인도 가능하지만 유지보수가 관건**: JetBrainsMonoHangul처럼 원본 업데이트를 따라가지 못하면 폐기되는 문제
4. **아이폰 환경에서 가능한 것**: Glyphr Studio(브라우저 기반)로 글리프 스케치/편집은 가능. FontForge 세밀 작업은 PC 필수
5. **Velvetyne 모델**: 소규모 커뮤니티가 오픈소스 도구만으로 지속적으로 퀄리티 높은 서체를 생산하는 것이 가능함을 증명

---

## 출처

### 포크/파생 사례
- [DejaVu fonts — Wikipedia](https://en.wikipedia.org/wiki/DejaVu_fonts) — Bitstream Vera → DejaVu 포크 계보
- [Hack Typeface — GitHub](https://github.com/font-forks/chrissimpkins.Hack) — DejaVu Sans Mono 기반 프로그래밍 폰트
- [Open-source Unicode typefaces — Wikipedia](https://en.wikipedia.org/wiki/Open-source_Unicode_typefaces) — 오픈소스 유니코드 서체 전체 목록
- [Velvetyne — Font Fonk Fork Workshop](https://velvetyne.fr/news/font-fonk-fork/) — 오픈소스 폰트 포크 워크숍
- [네이버 D2 Coding — GitHub](https://github.com/naver/d2codingfont) — 나눔바른고딕 기반 코딩 서체
- [프로그래밍 글꼴 — 나무위키](https://namu.wiki/w/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EA%B8%80%EA%BC%B4) — Sarasa Gothic, Monoplex KR 등 한국어 합성 폰트 사례

### 도구/워크플로우
- [FontForge](https://fontforge.org/en-US/) — 오픈소스 폰트 에디터
- [Glyphr Studio](https://www.glyphrstudio.com/) — 웹 기반 무료 폰트 에디터
- [Which is the best free font editor? — TypeDrawers](https://typedrawers.com/discussion/5400/which-is-the-best-free-font-editor) — 무료 폰트 에디터 비교 논의

### 라이선스
- [Open Source Font Licenses Guide](https://font-converters.com/licensing/open-source-fonts) — OFL, Apache 2.0 등 라이선스 해설
- [SIL Open Font License — 오픈소스SW 라이선스 종합정보시스템](https://www.olis.or.kr/license/Detailselect.do?lId=1086&mapcode=010068) — OFL 한국어 설명

---

## 관련 문서

- [AI 폰트 제작 도구 및 워크플로우 리서치](2026-03-25_ai-font-creation-tools.md)
