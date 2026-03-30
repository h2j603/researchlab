---
title: "크리에이티브 코딩 도구 리서치 — 상세 조사"
date: 2026-03-30
updated: 2026-03-30
status: in-progress
type: research
tags: [creative-coding, tool, analog-digital, typography, emerging]
related: ["_index.md", "../2026-03-25_ai-font-case-studies/_index.md"]
confidence: medium
---

# 크리에이티브 코딩 도구 리서치 (2025-2026) — 상세 조사

## 1. 크리에이티브 코딩 라이브러리 — p5.js/three.js 대안 및 신흥 도구

### 핵심 발견
- **p5.js 2.x** — 여전히 제너러티브 아트 입문의 표준. 2.x 라인에서 모듈 구조와 렌더링이 개선됨. 브라우저에서 즉시 실행 가능하므로 아이폰에서도 에디터(OpenProcessing 등)를 통해 접근 가능
- **c2.js** — 컴퓨터 기하학, 물리 시뮬레이션, 진화 알고리즘 기반의 크리에이티브 코딩 라이브러리. p5.js보다 수학적/알고리즘적 접근에 강점
- **Two.js** — SVG, Canvas, WebGL을 렌더러로 선택할 수 있는 2D 드로잉 API. 벡터 기반 제너러티브 그래픽에 적합하며 출력물(인쇄)과의 호환성이 좋음
- **Paper.js** — 벡터 그래픽 스크립팅 프레임워크. 패스 기반 제너러티브 드로잉, 모핑 효과에 강점. SVG 출력 가능
- **PixiJS** — 고성능 2D WebGL 렌더러. 스프라이트, 필터, 셰이더 지원. 유체적인 비주얼 경험에 최적화
- **React Three Fiber** — Three.js의 React 래퍼. 선언적이고 조합 가능한 3D 씬 구축. 웹 인터페이스와 자연스럽게 통합
- **Nannou** — Rust 기반 크리에이티브 코딩 프레임워크. 퍼포먼스 크리티컬한 제너러티브 아트에 적합하나, 프로그래밍 배경 필요
- **Spline** — 3D 디자인 도구로, 인터랙티브 씬을 웹으로 직접 내보낼 수 있음. 코드 없이 3D 작업 가능

### 출처
- [Top Creative Coding Tools in 2025](https://blog.vibecoding.vip/creative-coding-tools/) — 2025년 주요 크리에이티브 코딩 도구 종합 비교
- [10 Creative Coding Examples & Project Ideas (2026)](https://lovable.dev/guides/creative-coding-examples-project-ideas) — 프로젝트 아이디어 포함 가이드
- [awesome-creative-coding-js-libraries](https://github.com/rasagy/awesome-creative-coding-js-libraries) — JS 기반 크리에이티브 코딩 라이브러리 큐레이션
- [Best p5.js alternatives (2026)](https://www.producthunt.com/products/p5-js/alternatives) — Product Hunt의 p5.js 대안 목록

---

## 2. 제너러티브 아트 / 크리에이티브 코딩 도구 — 모바일/웹 중심

### 핵심 발견
- **Hydra** — 브라우저에서 라이브 코딩으로 비디오 신시사이저를 구현. GLSL 스타일 연산자를 체이닝하여 반응형 비주얼 생성. 아이폰 브라우저에서도 접근 가능 (hydra.ojack.xyz)
- **Juno** — 노코드 제너러티브 아트 스튜디오. 인터랙티브, 시간 기반, 오디오 리액티브 작품을 코드 없이 제작 가능
- **Cødeart** — 아이폰용 크리에이티브 코딩 앱. p5.js 기반 기법을 모바일에서 사용 가능. 수학적 공식을 시각적 결과물로 전환. **아이폰 사용 환경에 직접 부합**
- **ml5.js** — 브라우저에서 포즈 감지, 이미지 분류, 스타일 트랜스퍼 등 머신러닝 기능을 몇 줄의 코드로 사용 가능
- **Strudel** — 브라우저에서 리듬 패턴과 제너러티브 음악을 라이브 코딩. 시각 작업과 사운드를 연결하는 데 유용
- **TouchDesigner / Cables.gl** — 노드 기반 비주얼 프로그래밍 도구. Cables.gl은 웹 기반이라 모바일 접근 가능성 있음

### 아이폰 접근성 평가
| 도구 | 아이폰 접근성 | 비고 |
|------|-------------|------|
| Cødeart | **직접 사용 가능** | App Store에서 설치 |
| Hydra | **웹에서 사용 가능** | hydra.ojack.xyz |
| OpenProcessing | **웹에서 사용 가능** | p5.js 스케치 실행/편집 |
| Juno | **웹에서 사용 가능** | 노코드 인터페이스 |
| Cables.gl | 부분적 가능 | 웹 기반이나 터치 최적화 미흡 |
| TouchDesigner | 불가능 | 데스크톱 전용 |

### 출처
- [CodeArt - App Store](https://apps.apple.com/us/app/codeart-processinng-ide/id6747937898) — 아이폰용 크리에이티브 코딩 IDE
- [10 Experimental Art Apps on the iPhone](https://todayinart.com/experimental-art-apps-on-the-iphone/) — 아이폰 실험적 아트 앱 목록
- [Best AI Creative Coding Tools for Artists in 2025](https://medium.com/@TransientLabs/best-ai-creative-coding-tools-for-artists-in-2025-40c9f810a193) — AI 통합 크리에이티브 코딩 도구

---

## 3. 타이포그래피 중심 라이브러리 / 도구

### 핵심 발견
- **가변 폰트(Variable Fonts)** — 2025년 기준 웹 표준으로 정착. 하나의 폰트 파일에서 weight, width, slant 등 다축 보간이 가능하여 스크롤, 호버, 음성 명령 등에 반응하는 키네틱 타이포그래피 구현 가능
- **GSAP + 가변 폰트 조합** — 가변 폰트 축(axis)을 GSAP 타임라인으로 애니메이션하면 유체적인 타이포그래피 모션 구현 가능. 스크롤 드리븐 타이포그래피에 특히 유용
- **Rive** — 인터랙티브 모션 디자인 도구. 키네틱 타이포그래피를 시각적 인터페이스로 제작하고 웹/앱에 내보내기 가능
- **키네틱 타이포그래피 트렌드** — 2025-2026년 유체적 형태, 모듈 폰트, 리퀴드 텍스트 이펙트가 주류. 주의력 저하 시대에 애니메이션 텍스트의 인게이지먼트가 정적 텍스트 대비 최대 40% 증가
- **추천 가변 폰트** — Inter, Roboto Flex (weight/width 애니메이션), Monument Extended, Aeonik, Sohne (기하학적 구조로 모션에 적합)

### 키네틱 타이포그래피 구현 방법
1. **CSS만으로** — `@font-variation-settings`, `transition`, `@keyframes`를 활용한 가변 폰트 애니메이션
2. **GSAP + ScrollTrigger** — 스크롤 위치에 따른 폰트 축 변화
3. **p5.js / Canvas** — 글리프를 직접 렌더링하여 물리 시뮬레이션 적용
4. **Rive** — 비주얼 에디터에서 타이포 모션 제작 후 내보내기

### 출처
- [Typography Trends 2026 – Variable Fonts, Kinetic Text & Storytelling with Type](https://www.theinkorporated.com/insights/future-of-typography/) — 2026년 타이포그래피 트렌드 종합
- [7 Kinetic Typography Trends 2025](https://www.upskillist.com/blog/top-7-kinetic-typography-trends-2025/) — 키네틱 타이포그래피 7대 트렌드
- [Kinetic Typography: The Complete Guide (2026)](https://www.ikagency.com/graphic-design-typography/kinetic-typography/) — 키네틱 타이포그래피 완전 가이드
- [Creative Bloq — Typography Trends 2025](https://www.creativebloq.com/design/fonts-typography/from-variable-fonts-to-kinetic-type-these-typography-trends-could-be-big-in-2025) — 가변 폰트와 키네틱 타입 트렌드

---

## 4. 아날로그 미감 + 디지털 기술 교차 도구

### 핵심 발견
- **리소그래프 이펙트 부활** — 2026년 리소그래프 미학이 대규모로 재부상 중. AI 생성 이미지의 "완벽함"에 대한 반작용으로 인간 손맛과 불완전함을 의도적으로 추구하는 디자인 트렌드
- **RizzCraft (True Grit Texture Supply)** — Photoshop, Procreate, Clip Studio, Affinity Photo에서 리소그래프 인쇄의 촉감적 불완전함을 재현. 최대 4색, 10-100% 톤 밸류, 종이 텍스처, 오버프린트, 판 어긋남 등 제어 가능
- **Super Riso 2** — 리소그래프 기계의 기술적 논리(스팟 컬러 분판 동작)를 이해하고 재현하는 접근. 그레인, 디더링, 미스프린트, 멀티컬러 잉크 겹침
- **Glitch Art Studio (모바일)** — 이미지 왜곡, 픽셀 벤딩, 텍스처 생성을 모바일에서 실행 가능. 날것의 미래주의적 텍스처 제작
- **Adobe Fresco (무료화)** — 2024년 말 완전 무료화. 유화/수채화를 시뮬레이션하는 라이브 브러시 포함. 아이폰에서 사용 가능

### "기술로 아날로그함을 추구"하는 도구 분류
| 카테고리 | 도구 | 아이폰 가능 |
|---------|------|-----------|
| 리소그래프 시뮬레이션 | RizzCraft, Super Riso 2 | Procreate Pocket으로 부분 가능 |
| 글리치/디스토션 | Glitch Art Studio | 가능 |
| 아날로그 페인팅 | Adobe Fresco | 가능 (무료) |
| 그레인/텍스처 | Vintage Camera, The Grainverse | 가능 |
| 크리에이티브 코딩 + 노이즈 | p5.js noise(), GLSL grain shader | 웹에서 가능 |

### 출처
- [Best Risograph Effect Plugins and Tools (2026)](https://www.illustration.app/blog/best-risograph-effect-plugins-and-tools-for-digital-design-in-2026) — 2026년 리소그래프 이펙트 도구 종합
- [RizzCraft — True Grit Texture Supply](https://www.truegrittexturesupply.com/products/rizzcraft) — 리소그래프 시뮬레이션 도구
- [Analog Aesthetic — Envato](https://author.envato.com/hub/analog-aesthetic/) — 아날로그 미학 트렌드 분석
- [6 Art Apps Every Digital Artist Should Try in 2025](https://salaisbrew.com/blogs/brew-blog/6-art-apps-every-digital-artist-should-try-in-2025) — 2025 디지털 아트 앱

---

## 5. 비주류이지만 강력한 시각 작업 라이브러리

### 핵심 발견
- **c2.js** — 컴퓨터 기하학 기반 크리에이티브 코딩. 보로노이, 들로네 삼각분할, 컨벡스 헐 등 기하학적 연산을 시각화에 바로 적용 가능. p5.js 생태계보다 알려져 있지 않지만 독특한 결과물 생산 가능
- **Hydra** — 라이브 코딩 비디오 신시사이저. 한 줄의 코드로 복잡한 비주얼 패턴 생성. VJ 퍼포먼스와 인스톨레이션에 특화. 아이폰 브라우저에서 접근 가능
- **lil-gui** — 어떤 스케치에든 즉시 슬라이더, 컬러 피커, 드롭다운을 추가. 제너러티브 파라미터를 실시간으로 조작할 수 있게 해주는 유틸리티
- **Strudel** — 알고리즘 음악 라이브 코딩. 시각 작업에 사운드 레이어를 추가하려는 디자이너에게 진입 장벽이 낮음
- **Tone.js** — 브라우저에서 인터랙티브 음악/사운드 제작. 신시사이저, 시퀀스, 이펙트 체인을 코드로 구성

### 출처
- [Top 15 Algorithmic Art Tools](https://stevezafeiriou.com/algorithmic-art-tools/) — 알고리즘 아트 도구 종합
- [12 Best JS Animation Libraries 2025](https://www.devkit.best/blog/mdx/javascript-animation-libraries-physics-engines-2025) — JS 애니메이션 라이브러리 비교

---

## 종합 추천 — 아이폰 + 그래픽 디자이너 환경

### 즉시 시작 가능한 도구 (아이폰에서 바로)
1. **Cødeart** — App Store 설치 후 p5.js 기반 크리에이티브 코딩
2. **Hydra** (hydra.ojack.xyz) — 브라우저에서 라이브 코딩 비주얼
3. **OpenProcessing** — 브라우저에서 p5.js 스케치 편집/실행
4. **Adobe Fresco** — 아날로그 페인팅 시뮬레이션 (무료)
5. **Glitch Art Studio** — 글리치/아날로그 텍스처 생성

### 휴가/외출 시 PC에서 탐색할 것
1. **GSAP + 가변 폰트** — 키네틱 타이포그래피 프로토타이핑
2. **RizzCraft** — 리소그래프 이펙트 심화 작업
3. **React Three Fiber** — 3D 웹 비주얼
4. **c2.js** — 기하학 기반 제너러티브 아트

---

## 관련 문서
- [크리에이티브 코딩 도구 리서치 MOC](_index.md)
- [AI 폰트 사례 연구](../2026-03-25_ai-font-case-studies/_index.md)
- [오픈소스 폰트 GitHub](../2026-03-25_opensource-font-github/_index.md)
