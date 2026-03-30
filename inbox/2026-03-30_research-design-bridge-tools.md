---
title: "리서치-디자인 브릿지 도구 탐색 (2025-2026)"
date: 2026-03-30
updated: 2026-03-30
status: inbox
type: research
tags: [tool, emerging, analog-digital, technology, print]
related: ["projects/2026-03-30_creative-coding-tools/_index.md"]
confidence: medium
---

# 리서치-디자인 브릿지 도구 탐색 (2025-2026)

사회 현상 리서치와 디자인 아웃풋을 연결하는 니치/신흥 기술 및 라이브러리 조사.
5개 교차 영역: 데이터 시각화, 웹-투-프린트, 실험적 AI 디자인, 아카이빙/리서치 도구, 실험적 웹 기술.

---

## 1. 사회 현상 데이터 시각화 (D3.js 대안 및 신흥 도구)

### 핵심 발견
- **Observable Plot** — D3 팀이 만든 고수준 API. D3의 저수준 복잡도 없이 빠르게 차트를 만들 수 있다. 사회 데이터의 빠른 탐색에 적합
- **Vega / Vega-Lite** — "grammar of graphics" 기반. 선언적 JSON으로 시각화를 정의. Python 바인딩(Altair)으로 데이터 사이언스 워크플로와 연결. v6.0.0 (2025년 3월) 출시
- **Apache ECharts 6.0** (2025년 7월) — 관계 시각화를 위한 chord series, matrix 좌표계 추가. 사회 네트워크/관계 데이터에 유용
- **Flourish** — 스토리텔링과 시각적 내러티브에 특화. 언론, 연구자, 미디어 조직이 사회 현상을 대중에게 전달할 때 사용. 무료 티어 존재
- **Nivo** (React) — D3 기반 React 컴포넌트. SVG/Canvas/HTML 3가지 렌더링 지원. 테마 커스터마이징이 강력하여 브랜딩 적용에 유리

### 출처
- [JavaScript Chart Libraries In 2026 — Luzmo](https://www.luzmo.com/blog/javascript-chart-libraries) — 2026 JS 차트 라이브러리 비교
- [Observable Plot](https://observablehq.com/plot/) — D3 팀의 고수준 시각화 API
- [Apache ECharts](https://echarts.apache.org/) — 대규모 데이터셋 처리에 강한 오픈소스 시각화
- [Flourish](https://flourish.studio/) — 스토리텔링 중심 데이터 시각화 플랫폼

---

## 2. 웹-투-프린트 도구 및 라이브러리

### 핵심 발견
- **Paged.js** — CSS Paged Media 폴리필의 사실상 표준. Chromium 위에 CSS Paged Media 스펙을 구현. 책, 문학 작품, 타이포그래피 출판물 등 실제 인쇄 프로젝트에 활발히 사용 중
- **Vivliostyle** — Paged.js와 함께 CSS Paged Media 3대 도구 중 하나. 일본 커뮤니티에서 특히 활발. CSS 조판 엔진으로 다국어 타이포그래피에 강점
- **WeasyPrint** — Python 기반 CSS 레이아웃 엔진. BSD 라이선스. HTML/CSS를 PDF로 변환. 통계 리포트, 인보이스 등에 활용. CourtBouillon이 유지보수
- **Typst** — LaTeX의 현대적 대안. 마크업 기반 조판 시스템. LaTeX만큼 강력하면서 학습 곡선이 훨씬 완만. 리서치 문서 출판에 유망
- **Bindery.js는 개발 중단됨** — 대안으로 Paged.js 또는 WeasyPrint 권장
- **PrePostPrint** — 웹 프로그래밍 언어를 디자인/자가출판 도구로 활용하는 워크숍/커뮤니티. 2026년 4월, 6월 컨퍼런스 예정

### 출처
- [Paged.js](https://pagedjs.org/) — CSS Paged Media 폴리필
- [Vivliostyle](https://vivliostyle.org/) — CSS 기반 조판 엔진
- [WeasyPrint](https://weasyprint.org/) — Python CSS 레이아웃 엔진
- [Typst](https://typst.app/) — 현대적 마크업 조판 시스템
- [PrePostPrint](https://prepostprint.org/resources/) — 웹-투-프린트 커뮤니티 및 리소스
- [print-css.rocks](https://print-css.rocks/) — CSS Paged Media 튜토리얼 (2026년 7월 종료 예정)

---

## 3. 비주류 실험적 AI 디자인 도구

### 핵심 발견
- **Hydra** — 라이브 코딩 비디오 신스. 브라우저에서 실시간으로 비주얼을 생성/조작. 실험적 시각 퍼포먼스에 적합. Midjourney/DALL-E와 완전히 다른 접근
- **Juno** — 노코드 제너러티브 아트 스튜디오. 인터랙티브, 시간 기반, 오디오 리액티브 작품을 코드 없이 제작. 레시피 또는 빈 캔버스에서 시작하여 즉시 공유 가능
- **TouchDesigner** — 노드 기반 실시간 엔진. VJ, 설치 미술, 프로젝션 매핑에 특화. 학습 곡선 높지만 라이브 인풋/하드웨어 통합이 압도적
- **Strudel** — 브라우저에서 제너러티브 음악 스케치를 만드는 JS 라이브러리. 사운드+비주얼 교차 작업에 유용
- **Google Stitch** (구 Galileo AI) — AI 네이티브 디자인 캔버스. Experimental Mode에서 Gemini 3.0 활용. 이미지 인풋 지원. 주류 AI 이미지 생성과 다른, 디자인 시스템 중심 접근

### 출처
- [Hydra](https://hydra.ojack.xyz/) — 라이브 코딩 비디오 신스
- [Juno](https://juno.art/) — 노코드 제너러티브 아트 플랫폼
- [TouchDesigner](https://derivative.ca/) — 노드 기반 실시간 비주얼 엔진
- [Strudel](https://strudel.cc/) — 브라우저 기반 제너러티브 음악
- [Google Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/) — AI 네이티브 UI 디자인 도구

---

## 4. 아카이빙/리서치 정리 도구 (Knowledge Graph, Zettelkasten)

### 핵심 발견
- **Zettlr** — 학술 연구자/작가 특화. Zotero 연동으로 인용 관리 내장. Zettelkasten 방법론 기본 지원. 완전 무료 오픈소스. 사회 현상 리서치의 문헌 관리에 특히 적합
- **AFFiNE** — 2025-2026년 가장 주목받는 신흥 도구. 로컬 퍼스트 + 비주얼 캔버스 + 협업 DB를 통합. 오픈소스. Obsidian과 Notion의 장점을 결합하려는 시도
- **Logseq** — 아웃라이너 기반 지식 관리. 로컬 데이터 저장. 오픈소스. 블록 단위 링크가 강점
- **Obsidian + AI 에이전트** — Obsidian CEO가 "Obsidian Skills"를 공개하여 AI 에이전트(Claude Code 등)가 볼트 내에서 직접 작업 가능. NER + Graph LLM으로 지식 그래프를 자동 구축하는 실험도 진행 중
- **AI 증강 지식 그래프** — NER(개체명 인식)과 LLM을 Zettelkasten 위에 레이어로 올려 자동 엔티티 링킹, 추론, 링크 예측을 하는 접근이 부상 중

### 출처
- [Zettlr](https://www.zettlr.com/) — 연구자를 위한 마크다운 에디터
- [AFFiNE](https://affine.pro/) — 오픈소스 올인원 지식 관리 도구
- [Logseq](https://logseq.com/) — 아웃라이너 기반 로컬 지식 관리
- [AI Zettelkasten — Obsidian Forum](https://forum.obsidian.md/t/ai-empowered-zettelkasten-with-ner-and-graph-llm/79112) — NER + Graph LLM 실험
- [Obsidian Alternatives — AlternativeTo](https://alternativeto.net/software/obsidian/) — 2026 대안 목록

---

## 5. 실험적 웹 기술

### 핵심 발견
- **View Transitions API** — 2025년 10월 Baseline Newly Available 달성. Chrome, Edge, Firefox, Safari 모두 지원. Cross-document 전환도 Chrome 126+, Safari 18.2+ 지원. React 코어에도 통합 진행 중. **2026년 신규 프로젝트의 기본 선택지**
- **Scroll-Driven Animations** — CSS만으로 스크롤 기반 애니메이션 구현. 메인 스레드 밖에서 실행 가능. Chrome 115+, Firefox(플래그 필요). Safari 미지원이지만 폴리필 존재. JS 라이브러리(GSAP 등) 의존 대폭 감소 가능
- **CSS Houdini `@property`** — 커스텀 프로퍼티에 타입 지정 가능. 브라우저가 커스텀 프로퍼티를 애니메이션할 수 있게 됨. 다만 Paint API, Font Metrics API 등은 아직 제안 단계
- **Interop 2025** — 브라우저 간 호환성 개선 프로젝트. View Transitions, Anchor Positioning, Navigation API 등이 중점 영역
- **Ladybird** — 완전히 새로운 브라우저 엔진. 2026년 퍼블릭 알파 예정. Blink/WebKit/Gecko 외의 독립 엔진이라는 점에서 웹 생태계에 의미

### 출처
- [View Transitions in 2025 — Chrome Developers](https://developer.chrome.com/blog/view-transitions-in-2025) — View Transitions 최신 동향
- [Scroll-Driven Animations — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) — CSS 스크롤 기반 애니메이션 가이드
- [CSS Houdini — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini) — Houdini API 개요
- [Interop 2025 — WebKit](https://webkit.org/blog/16458/announcing-interop-2025/) — 브라우저 호환성 프로젝트
- [Ladybird Browser Engine](https://www.makeuseof.com/ladybird-new-browser-engine-coming-2026/) — 2026 새 브라우저 엔진

---

## 종합: 리서치-디자인 브릿지에 유망한 조합

| 워크플로 단계 | 추천 도구 | 이유 |
|---|---|---|
| 리서치 정리 | Zettlr + Zotero | 문헌 관리 내장, 무료, 로컬 |
| 데이터 탐색 | Observable Plot / Vega-Lite | 빠른 프로토타이핑, 선언적 |
| 시각 내러티브 | Flourish + View Transitions | 스토리텔링 + 브라우저 네이티브 전환 |
| 인쇄 출력 | Paged.js + Typst | 웹→프린트 변환의 현재 최선 |
| 실험적 비주얼 | Hydra / Juno | 코드 기반 실시간 비주얼 생성 |
| 지식 그래프 | Obsidian + NER/LLM 레이어 | AI 자동 링킹으로 리서치 연결 강화 |

### 아이폰 접근성 참고
- Observable Plot, Flourish, Hydra, Juno, Strudel은 **브라우저 기반**이므로 아이폰에서도 접근 가능
- Zettlr, AFFiNE는 모바일 앱 또는 모바일 웹 지원이 제한적
- Paged.js, Typst는 PC 환경 필요 (휴가/외출 시 작업)

---

## 관련 문서
- [크리에이티브 코딩 도구 리서치](../projects/2026-03-30_creative-coding-tools/_index.md)
