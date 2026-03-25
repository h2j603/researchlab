---
title: "파라미터 기반 폰트 생성/변형 웹 도구 리서치"
date: 2026-03-25
updated: 2026-03-25
status: inbox
type: research
tags: [typography, tool, font-distribution, analog-digital]
related: ["2026-03-25_ai-font-creation-tools.md", "2026-03-25_open-source-font-fork-benchmarking.md"]
confidence: medium
---

# 파라미터 기반 폰트 생성/변형 웹 도구 리서치

슬라이더/파라미터로 폰트를 실시간 조정하고, OTF/TTF로 내보낼 수 있는 웹 기반 도구를 조사한다.

---

## 1. 파라미터(슬라이더) 기반 웹 폰트 에디터

### Prototypo

- **개요**: 웹 브라우저에서 파라미터 슬라이더로 글리프의 x-height, stem width, serif, letter width 등을 실시간 조정하여 커스텀 폰트를 생성하는 도구
- **특징**: Spectral(최초의 파라미터 기반 Google Font)을 Production Type과 함께 제작한 실적이 있음
- **내보내기**: OTF 내보내기 지원 (웹폰트 및 데스크탑 모두 사용 가능)
- **현재 상태**: **사실상 폐쇄**. 공식 사이트(prototypo.io)가 Notion 페이지로 리다이렉트됨. GitHub 저장소(byte-foundry/prototypo)는 아카이브 상태
- **가격**: 서비스 종료
- **제한사항**: 더 이상 사용 불가. 라틴 문자 전용이었음

### Metapolator

- **개요**: 웹 기반 파라미터 폰트 에디터. UFO 폰트와 Metafont 기술을 결합. 무한 개수의 마스터와 축으로 '슈퍼 인터폴레이션' 가능
- **핵심 개념**: 스트로크 요소 기반 — Metafont에서 재구현한 Hobby Spline으로 스켈레톤 경로를 제어하고, 각 스트로크 포인트에서 좌/우 포인트를 각도와 거리로 설정
- **현재 상태**: **개발 중단/비활성**. GitHub(metapolator/metapolator)의 마지막 의미 있는 커밋이 오래됨. 웹사이트(metapolator.com)는 존재하나 실제 작동하는 에디터는 미완성
- **가격**: 무료/오픈소스 (GPL)
- **제한사항**: 완성된 제품이 아님. 컨셉과 프로토타입 수준에 머물러 있음

### Glyphr Studio (v2)

- **개요**: 웹 브라우저에서 100% 작동하는 오픈소스 폰트 에디터. 초보자/취미 타입 디자이너를 위한 낮은 진입장벽
- **가져오기**: SVG, OTF, TTF, WOFF
- **내보내기**: OTF, SVG Font
- **현재 상태**: **활성**. v2가 안정 버전으로 제공 중
- **가격**: 완전 무료, 회원가입 불필요
- **제한사항**: 파라미터/슬라이더 기반 편집이 **아님** — 전통적인 벡터 에디터 방식. Variable Font 축 편집 미지원. 기능이 제한적이므로 복잡한 폰트 프로젝트에는 부족할 수 있음
- **모바일**: 웹 기반이므로 아이폰 브라우저에서 접근 가능하나, 벡터 편집 UX가 터치에 최적화되어 있지 않음

### FontArk

- **개요**: 브라우저 기반 폰트 에디터. 실시간 다중 글리프 편집이 특징. 자동 힌팅, 커닝 등 지원
- **현재 상태**: **베타/비활성 의심**. 공식 사이트 접근이 불안정. 개발 업데이트가 뜸함
- **가격**: 베타 기간 무료였으나, 현재 상태 불명확
- **제한사항**: Variable Font 지원 없음. 안정성 불확실

### fonteditor (baidu/kity-minder 계열)

- **개요**: 웹 기반 TTF 폰트 에디터. 중국어 글리프 편집에도 활용됨
- **현재 상태**: 오픈소스로 존재하나 활발한 유지보수 불명
- **제한사항**: 파라미터 기반이 아닌 전통적 편집 방식

---

## 2. Variable Font 커스텀 축(Custom Axis) 도구

### 커스텀 축 생성이 가능한 도구

| 도구 | 웹 기반 | 커스텀 축 생성 | 비고 |
|------|---------|---------------|------|
| **Glyphs App** | 아니오 (macOS 전용) | **가능** — Font Info > Axes에서 4자리 태그로 사설 축 추가 (예: SMIL, ROTN) | 업계 표준. 유료 ($299) |
| **FontLab 8** | 아니오 (데스크탑) | **가능** — 다축 Variable Font 편집 | 유료 ($499) |
| **fonttools (Python)** | 아니오 (CLI/서버) | **가능** — designSpaceDocument로 축 정의 후 빌드 | 무료/오픈소스 |
| **fontmake** | 아니오 (CLI) | **가능** — .designspace 파일에서 Variable Font 빌드 | 무료/오픈소스 |

### 웹에서 Variable Font을 테스트/조정하는 도구 (생성은 아님)

| 도구 | URL | 기능 |
|------|-----|------|
| **Axis-Praxis** | axis-praxis.org | 기존 Variable Font의 축을 슬라이더로 실시간 조정. 커스텀 축 포함 |
| **Wakamai Fondue** | wakamaifondue.com | 폰트 파일을 드롭하면 사용 가능한 축/기능을 자동 탐지 |
| **Font Gauntlet** (ABC Dinamo) | fontgauntlet.com | Variable Font 테스트 + 애니메이션 가능 |
| **FontFreeze** | mutsuntsai.github.io/fontfreeze | Variable Font의 특정 축 값을 고정(freeze)하여 정적 폰트로 내보내기 |

> **핵심**: 웹 브라우저만으로 커스텀 축을 **생성**할 수 있는 도구는 현재 없다. 축 생성은 Glyphs, FontLab, fonttools 등 데스크탑/CLI 도구가 필요하다. 웹 도구는 이미 만들어진 Variable Font을 **테스트하고 조정**하는 데 특화되어 있다.

### Variable Font 커스텀 축 명명 규칙

- **등록 축(registered)**: 소문자 4자리 태그 — `wght`(weight), `wdth`(width), `slnt`(slant), `ital`(italic), `opsz`(optical size)
- **사설 축(custom)**: 대문자 4자리 태그 — 디자이너가 자유롭게 정의 (예: `YEST`=Yeast, `GRAV`=Gravity, `TEMP`=Temperature)
- 2026년 트렌드: `GRAD`(Grade) 축이 UI 서체의 표준 요구사항으로 부상 중. COLRv1 포맷으로 컬러 + Variable 결합

---

## 3. 프로그래밍 기반 폰트 생성 (웹)

### opentype.js

- **개요**: JavaScript로 OpenType/TrueType 폰트를 읽고, 쓰고, **새로 생성**할 수 있는 라이브러리
- **생성 가능**: 글리프의 베지에 경로를 정의하여 처음부터 폰트를 만들 수 있음
- **내보내기**: `font.toArrayBuffer()`로 OTF 파일 생성 → 브라우저에서 다운로드 가능
- **지원 포맷**: WOFF, OTF, TTF (TrueType `glyf` + PostScript `cff` 아웃라인 모두)
- **고급 기능**: 커닝(GPOS/kern), 합자(ligature), 합성 글리프, 아랍어, 컬러 글리프(SVG/COLR/CPAL)
- **Variable Font 지원**: **미지원** — 현재 Variable Font 축 생성/편집 기능 없음
- **현재 상태**: **활성**. npm에서 설치 가능, GitHub에서 꾸준히 유지보수 중
- **활용 예시**: 코드로 알고리즘적 글리프를 생성하고 즉시 폰트 파일로 내보내기

```javascript
// opentype.js로 브라우저에서 폰트 생성 후 다운로드
const font = new opentype.Font({
  familyName: 'MyFont',
  styleName: 'Regular',
  unitsPerEm: 1000,
  ascender: 800,
  descender: -200,
  glyphs: [notdefGlyph, aGlyph, bGlyph /* ... */]
});

// 브라우저에서 OTF 다운로드
const blob = new Blob([font.toArrayBuffer()], {type: 'font/opentype'});
const url = window.URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'MyFont.otf';
a.click();
```

### p5.js + opentype.js

- **개요**: p5.js의 `loadFont()`가 내부적으로 opentype.js를 사용. p5.Font 객체에서 opentype.js 폰트 객체에 직접 접근 가능
- **워크플로우**: p5.js로 창의적 코딩 → 글리프 형태 시각화/생성 → opentype.js로 폰트 파일 내보내기
- **활용**: 알고리즘적 타이포그래피, 제너러티브 글리프 디자인
- **참고**: Allison Parrish의 [Computational Approaches to Typography](http://comptypo.decontextualize.com/fonts-as-data/)에서 상세 튜토리얼 제공

### fonttools (Python)

- **개요**: Python 기반 폰트 조작 라이브러리. 업계 표준급
- **기능**: OTF/TTF 읽기/쓰기, Variable Font 빌드, 서브셋팅, 변환
- **Variable Font**: **완전 지원** — designSpaceDocument로 축 정의, fontmake로 빌드
- **웹 사용**: 직접 브라우저에서는 불가. 서버사이드 또는 로컬 Python 환경 필요
- **현재 상태**: **매우 활성**. Google Fonts 등에서 공식 사용

### FontFreeze (웹)

- **개요**: 웹에서 Variable Font의 축 값을 고정하여 정적 인스턴스를 내보내는 도구
- **용도**: 기존 Variable Font에서 원하는 weight/width 조합을 골라 일반 폰트로 변환
- **제한**: 새 축을 만드는 것이 아니라, 기존 축을 "잠금"하는 것

---

## 4. 종합 비교표

| 도구 | 유형 | 웹 기반 | 파라미터/슬라이더 | VF 축 생성 | 내보내기 | 상태 | 가격 |
|------|------|---------|-----------------|-----------|---------|------|------|
| **Prototypo** | 파라미터 에디터 | 웹 | **가능** | 불가 | OTF | **폐쇄** | - |
| **Metapolator** | 파라미터 에디터 | 웹 | **가능** | 계획됨 | UFO | **비활성** | 무료 |
| **Glyphr Studio v2** | 벡터 에디터 | 웹 | 불가 | 불가 | OTF, SVG | **활성** | 무료 |
| **FontArk** | 벡터 에디터 | 웹 | 부분적 | 불가 | OTF/TTF | **불확실** | 무료(베타) |
| **opentype.js** | JS 라이브러리 | 웹 | 코드로 가능 | 불가 | OTF | **활성** | 무료 |
| **p5.js + opentype.js** | 크리에이티브 코딩 | 웹 | 코드로 가능 | 불가 | OTF | **활성** | 무료 |
| **fonttools** | Python 라이브러리 | 서버/로컬 | 코드로 가능 | **가능** | OTF/TTF/VF | **활성** | 무료 |
| **Glyphs App** | 전문 에디터 | 데스크탑 | GUI 가능 | **가능** | OTF/TTF/VF | **활성** | $299 |
| **FontLab 8** | 전문 에디터 | 데스크탑 | GUI 가능 | **가능** | OTF/TTF/VF | **활성** | $499 |
| **Axis-Praxis** | 테스트 도구 | 웹 | 슬라이더 조정 | 불가 | 불가 | **활성** | 무료 |
| **FontFreeze** | 변환 도구 | 웹 | 축 값 고정 | 불가 | 정적 폰트 | **활성** | 무료 |

---

## 5. 현실적 평가

### 웹 브라우저만으로 파라미터 기반 폰트 생성이 가능한가?

**결론: 매우 제한적이다.**

- Prototypo가 가장 가까운 답이었으나 **폐쇄**되었다
- Metapolator는 비전은 훌륭하나 **미완성**이다
- 현재 활성 상태인 웹 도구 중 진정한 의미의 파라미터 기반 폰트 생성기는 **없다**
- **opentype.js**를 활용한 커스텀 코딩이 가장 현실적인 대안이다 — 슬라이더 UI를 직접 만들고, 파라미터에 따라 글리프를 생성하는 웹앱을 구축할 수 있음

### Variable Font 커스텀 축은?

- 웹에서 커스텀 축을 **만드는** 도구는 없다
- **Glyphs App** 또는 **fonttools**가 필수 (둘 다 PC 전용)
- 웹 도구는 만들어진 Variable Font을 테스트/시각화하는 데 사용

### 아이폰 환경에서의 접근

- Axis-Praxis, Wakamai Fondue 등으로 Variable Font **테스트**는 가능
- Glyphr Studio로 간단한 글리프 편집은 가능하나 터치 UX 불편
- 본격적인 파라미터 폰트 작업은 PC 필수

---

## 출처

- [Prototypo - Spectral](https://spectral.prototypo.io/)
- [Metapolator](http://metapolator.com/)
- [Glyphr Studio](https://www.glyphrstudio.com/)
- [opentype.js](https://opentype.js.org/) — [GitHub](https://github.com/opentypejs/opentype.js)
- [p5.js + opentype.js 튜토리얼](http://comptypo.decontextualize.com/fonts-as-data/)
- [Axis-Praxis](https://www.axis-praxis.org/)
- [Glyphs App - Creating a Variable Font](https://glyphsapp.com/learn/creating-a-variable-font)
- [Variable Fonts Explained 2026](https://inkbotdesign.com/variable-fonts/)
- [Variable Fonts and Quirky Custom Axes](https://www.rwt.io/typography-tips/variable-fonts-and-quirky-custom-axes/)
- [awesome-typography (GitHub)](https://github.com/Jolg42/awesome-typography)
- [Eye on Design - Parametric vs Variable Fonts](https://eyeondesign.aiga.org/parametric-and-variable-typeface-systems-shape-shifters-for-letterforms/)
- [MDN - Variable Fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)

---

## 관련 문서

- [AI 폰트 제작 도구 리서치](2026-03-25_ai-font-creation-tools.md)
- [오픈소스 기반 자체 서체 제작 벤치마킹](2026-03-25_open-source-font-fork-benchmarking.md)
