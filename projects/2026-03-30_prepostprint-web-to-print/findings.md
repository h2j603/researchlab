---
title: "PrePostPrint 심층 리서치 — 웹 기술 기반 인쇄 디자인 운동"
date: 2026-03-30
updated: 2026-03-30
status: in-progress
type: research
tags: [web-to-print, print, creative-coding, analog-digital, tool, typography]
related: ["_index.md", "sources.md", "_critique.md"]
confidence: medium
---

# PrePostPrint 심층 리서치

## 1. PrePostPrint란 무엇인가?

### 정의
PrePostPrint은 **HTML, CSS, JavaScript 등 웹 프로그래밍 언어를 디자인 및 셀프 퍼블리싱 도구로 활용**하는 비공식 커뮤니티이자 운동이다. 스스로를 "대안적 출판 시스템을 위한 실험실(Laboratory for alternative publishing systems)"이라 정의한다.

### 지리적 기반
주로 **프랑스와 벨기에**를 중심으로 활동하며, 미국(샌프란시스코, 뉴욕)에서도 워크숍을 개최한 바 있다.

### 역사 및 주요 연혁
- **2017년 10월 20-21일**: PrePostPrint 에디션 살롱이 파리 Gaîté Lyrique에서 개최. 저널 "Code X" 1호가 이 행사에서 출간됨 — HTML과 CSS로 웹 브라우저에서 전체 디자인됨
- **2018년 4월**: EnsadLab(파리 국립장식미술학교 연구소)이 PrePostPrint을 초청하여 2일간 발표 및 토론 진행. Julie Blanc, Quentin Juhel, Lucile Haute가 조직
- **2018년 11월**: Paged Media × PrePostPrint 워크숍 시리즈 — 브뤼셀 1회, 파리 2회 총 3회 개최. Paged.js의 최초 공개 실험이 이루어진 랜드마크 이벤트
- **2021년 10월 27-29일**: Julie Blanc의 Paged.js 워크숍 (Ésac Cambrai)
- **2024년 1월**: Julie Blanc과 Yann Trividic가 파리에서 워크숍 개최, 메인테이너 교체 시기와 겹침
- **2024년 9월 28-29일**: PPPermapublishing @ HEAR (스트라스부르) — 인쇄물 공유 및 10분 데모/발표 슬롯으로 구성

### 핵심 인물
| 이름 | 역할/배경 |
|------|-----------|
| **Julie Blanc** | 그래픽 디자이너, EnsadLab 학생연구원. Paged.js 핵심 개발팀. 인쇄/디지털 읽기 객체 연구. ERG(브뤼셀) 졸업 |
| **Fred Chasen** | Paged.js 핵심 개발자 |
| **Julien Taquet** | Paged.js 핵심 개발자, 워크숍 리더 |
| **Sarah Garcin** | PrePostPrint 조직 멤버, 디자이너 |
| **Raphaël Bastide** | PrePostPrint 조직 멤버, 아티스트/디자이너 |
| **Antoine Fauchié** | PrePostPrint 조직 멤버 |
| **Alexia Foubert** | PrePostPrint 조직 멤버 |
| **Lucile Haute** | EnsadLab 행사 공동 조직 |
| **Evan Brooks** | Bindery.js 개발자 (RISD) |
| **Quentin Juhel** | EnsadLab 학생연구원 |

## 2. 철학과 접근법

### 핵심 철학: 기술적 해방(Technological Emancipation)
PrePostPrint의 근본 철학은 **독점 소프트웨어(Adobe InDesign 등)로부터의 기술적 해방**이다. 오픈소스, 자유 소프트웨어, 웹 표준 기술을 사용하여 출판 워크플로우를 대안적으로 구축한다.

### 웹과 인쇄의 교차
- **"반응형 디자인의 확장으로서의 책"**: Bindery.js의 철학처럼, 웹 디자이너라면 책을 반응형 디자인의 연장선으로 생각할 수 있다
- **코드와 시각적 조작의 왕복**: 브라우저의 요소 검사기(Inspector)를 통해 코드와 시각적 조작 사이를 자유롭게 오갈 수 있다는 점이 전통적 인쇄 제작과 가장 크게 다른 점
- **협업 가능성**: 디자인이 코드/텍스트로 이루어지기 때문에, Etherpad 같은 협업 텍스트 에디터를 사용하여 여러 사람이 동시에 디자인 작업 가능
- **하이브리드 출판**: 종이와 디지털 사이의 상호작용을 탐구. 하나의 소스(HTML/CSS)에서 인쇄용 PDF와 웹 버전을 동시에 생산

### OSP(Open Source Publishing)의 영향
브뤼셀 기반 디자인 그룹 OSP(Open Source Publishing, osp.kitchen)이 이 운동의 선구자 중 하나. HTML2Print 같은 도구를 개발하여 웹 기술 기반 인쇄 작업의 가능성을 실증했다.

## 3. 주요 도구와 기술

### 핵심 도구 비교

| 도구 | 설명 | 상태 | 특징 |
|------|------|------|------|
| **Paged.js** | CSS Paged Media 표준을 브라우저에서 구현하는 JS 라이브러리 | 활발히 개발 중 | CSS 표준 기반, 폴리필(polyfill) 방식 |
| **Bindery.js** | HTML/CSS로 인쇄 가능한 책을 만드는 JS 라이브러리 | 개발 중단 | 2014년 RISD에서 시작, CSS Regions 기반이었으나 Chrome이 폐기 |
| **HTML2Print** | OSP가 만든 웹-투-프린트 보일러플레이트 | 유지 중 | HTML, Less/CSS, JS/jQuery 기반 최소 시작 템플릿 |
| **WeasyPrint** | Python 기반 HTML/CSS → PDF 변환 | 활발히 개발 중 | 서버사이드, CLI 도구 |
| **PrinceXML** | 상용 HTML/CSS → PDF 변환 | 상용 제품 | 가장 완성도 높은 CSS Paged Media 구현 |
| **Vivliostyle** | 오픈소스 CSS 조판 엔진 | 활발히 개발 중 | 일본 기반, CSS Paged Media 지원 |
| **PJ Machine** | 아케이드 버튼이 달린 박스형 퍼블리싱 장치 | 실험적 | NodeJS 기반 라이브 협업 퍼블리싱 |

### CSS Paged Media 표준의 문제
- 2008년 W3C에서 CSS Paged Media 표준이 제정되었으나, 브라우저 벤더들이 구현에 관심을 두지 않음
- 이 때문에 Paged.js 같은 자바스크립트 폴리필(polyfill)이 필요하게 됨
- Bindery.js는 CSS Regions 초안에 기반했으나, Chrome이 이를 폐기하면서 개발 동력을 잃음

### Paged.js와 PrePostPrint의 관계
Paged.js는 PrePostPrint 커뮤니티와 밀접하게 연결되어 있다. 2018년 Paged Media × PrePostPrint 워크숍이 Paged.js의 첫 공개 실험장이었으며, 핵심 개발진(Fred Chasen, Julie Blanc, Julien Taquet)이 PrePostPrint 커뮤니티의 활발한 멤버다.

### Vivliostyle와의 관계
Vivliostyle는 일본 기반의 별도 프로젝트로, PrePostPrint과 직접적인 조직적 연결은 확인되지 않는다. 다만 같은 CSS Paged Media 생태계에 속하며, 웹 기술로 조판(typesetting)을 수행한다는 동일한 철학을 공유한다.

## 4. 주목할 만한 프로젝트 및 출판물

### Code X 저널
- 2017년 PrePostPrint 에디션 살롱에서 창간
- HTML과 CSS로 웹 브라우저에서 전체 디자인 및 제작
- 웹-투-프린트 철학의 실증적 사례

### Cyberwitches Manifesto
- 독점 소프트웨어로부터의 기술적 해방 과정에서 제작
- 모든 인쇄물이 웹-투-프린트로 제작: 웹 브라우저에서 PDF 출력, HTML/CSS로 그래픽 구성

### Each Page A Function
- 자유 소프트웨어, 오픈소스 폰트, 표준 웹 기술만으로 제작
- 디자인, 개발, PDF 내보내기 과정에서 독점 소프트웨어 일절 사용하지 않음
- HTML/PHP/JavaScript/print CSS 워크플로우

### PageTypeToScreen
- ÉSAD Pyrénées의 논문 및 문서를 위한 web2print 템플릿
- Julien Bidoret 제작

### HTML2Print (OSP)
- Open Source Publishing(osp.kitchen)이 제작
- 웹-투-프린트 프로젝트를 시작하기 위한 최소 보일러플레이트
- HTML, Less/CSS, JavaScript/jQuery 기반

## 5. 행사 및 이벤트

### 최근 및 향후 행사
| 시기 | 행사 | 장소 | 비고 |
|------|------|------|------|
| 2024년 9월 28-29일 | PPPermapublishing @ HEAR | 스트라스부르 | 인쇄물 공유 + 10분 데모 슬롯 |
| 2024년 1월 | Julie Blanc & Yann Trividic 워크숍 | 파리 | 메인테이너 교체 시기 |
| 2025년 4월 (예정) | Césure에서 행사 가능성 언급 | 파리 (추정) | Julie Blanc이 언급, 확정 여부 미확인 |

**참고**: 2025-2026년 구체적 행사 정보는 웹 검색에서 확인되지 않음. PrePostPrint의 활동이 비공식적·비정기적 성격이 강하여, 행사 공지가 위키나 메일링리스트를 통해 이루어질 가능성이 높다.

### 메인테이너 교체 (2023-2024)
PrePostPrint은 2023-2024년에 "Call for maintainers"를 발행하여 새로운 운영진을 모집했다. 이는 커뮤니티의 지속가능성을 위한 세대교체 시도로 볼 수 있다.

## 6. 이 분야의 주요 실천가/디자이너

### PrePostPrint 핵심 그룹
- **Julie Blanc** (julie-blanc.fr) — 인쇄/디지털 하이브리드 출판 연구, Paged.js 개발
- **Sarah Garcin** — 인터랙티브 디자인, 참여형 퍼블리싱 도구
- **Raphaël Bastide** — 아티스트/디자이너, 대안적 디지털 도구 탐구
- **Antoine Fauchié** — 디지털 퍼블리싱 연구

### 관련 기관/그룹
- **Open Source Publishing (OSP)** — 브뤼셀 기반, 자유 소프트웨어만으로 디자인 작업을 수행하는 디자인 그룹
- **EnsadLab** — 파리 국립장식미술학교 연구소, PrePostPrint 초청 행사 주최
- **Gaîté Lyrique** — 파리의 디지털 문화 공간, PrePostPrint 에디션 살롱 개최지
- **RISD (Rhode Island School of Design)** — Bindery.js가 탄생한 "HTML Output" 그래픽 디자인 강좌

### 넓은 의미의 웹-투-프린트 실천가
- **Evan Brooks** — Bindery.js 개발자 (RISD)
- **Fred Chasen** — Paged.js 핵심 개발자
- **Julien Bidoret** — PageTypeToScreen 제작, ÉSAD Pyrénées
- **Lucile Haute** — EnsadLab 연구자, 반응형 디자인과 인쇄의 교차 탐구

## 7. 사용자 맥락에서의 의미

### "최신의 기술로 최고의 아날로그함을 추구"와의 접점
PrePostPrint의 핵심은 바로 이 교차점에 있다:
- **최신 기술**: HTML, CSS, JavaScript — 가장 현대적이고 보편적인 웹 기술
- **아날로그 결과물**: 인쇄된 책, 포스터, 진(zine) — 물리적 종이 위의 디자인
- 하나의 코드베이스에서 스크린과 종이 양쪽 모두를 위한 디자인이 가능하다는 점은 "디지털-아날로그 교차" 탐구의 실질적 방법론을 제공

### 아이폰 환경에서의 가능성
- HTML/CSS 코드 작성은 이론적으로 모바일에서도 가능하나, 실제 레이아웃 확인과 PDF 내보내기는 데스크톱 브라우저가 필요
- 개념적 리서치와 코드 구조 설계는 모바일에서 가능, 실행은 휴가/외출 시 PC에서

## 관련 문서
- [크리에이티브 코딩 도구 리서치](../2026-03-30_creative-coding-tools/_index.md)
- [그리드 시스템 리서치](../2026-03-19_grid-systems/_index.md)
