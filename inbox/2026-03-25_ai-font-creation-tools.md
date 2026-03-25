---
title: "AI 폰트 제작 도구 및 워크플로우 리서치"
date: 2026-03-25
updated: 2026-03-25
status: inbox
type: research
tags: [typography, ai, tool, font-distribution, analog-digital]
related: []
confidence: medium
---

# AI 폰트 제작 도구 및 워크플로우 리서치

Noto Sans 수정이 너무 어려웠던 경험에서 출발. 다국어 고품질 폰트를 AI 보조로 제작할 수 있는 현실적인 방법을 탐색한다.

## 핵심 발견

### 1. 실제 설치 가능한 폰트(OTF/TTF)를 만들어주는 도구

| 도구 | 특징 | 가격 | 모바일 가능 |
|------|------|------|-------------|
| **[Creative Fabrica Font Generator](https://www.creativefabrica.com/tools/ai-font-generator/)** | 직접 글자를 그리면 AI가 정제하여 설치 가능한 폰트 파일로 변환. 간격/정렬 자동 조정 | 무료 계정으로 사용 가능 | 웹 기반 (모바일 브라우저 가능) |
| **[GLIPH](https://gliph.us/)** | 이미지(손글씨, 드로잉, AI 생성 텍스트)를 TTF 폰트로 변환. 디자인 경험 불필요 | 무료 | 웹 기반 |
| **[Calligraphr](https://www.calligraphr.com/)** | 손글씨 템플릿 작성 후 업로드하면 폰트로 변환. 20~30분 소요 | 무료/유료 | 템플릿 작성은 아이폰 가능 |
| **[Font AI](https://www.font-ai.com/)** | 텍스트 프롬프트로 폰트 생성. 이미지에서 폰트 식별 후 유사 폰트 생성 가능. Open Font License 준수 | - | 웹 기반 |
| **[Fontself](https://www.fontself.com/)** | Illustrator/Photoshop 플러그인. 아트워크를 폰트로 변환. 완전한 디자인 컨트롤 | 유료 | PC 전용 (데스크탑 앱 필요) |

### 2. AI 이미지 생성 + 벡터화 워크플로우

**Skywork AI, NeoSpark 등**은 고해상도 글자 이미지를 생성하지만, 설치 가능한 폰트 파일은 별도 도구로 벡터화해야 한다.

워크플로우:
1. AI로 글자 이미지 생성 (프롬프트 기반)
2. 이미지를 벡터화 (Illustrator 또는 오픈소스 도구)
3. FontForge / Glyphr Studio에서 폰트 파일로 조립

### 3. 다국어/CJK 폰트 제작

- CJK(한중일) 폰트는 글자 수가 방대하여 AI 보조가 특히 유용
- **Bylo.ai**: 중국어, 아랍어 등 다국어 지원 명시
- ML 접근법 두 가지:
  - (A) 가능한 많은 글자를 학습 데이터에 포함
  - (B) 핵심 글자만 선별 학습 후 나머지를 수동 제작
- AI를 "가이드 스케치" 또는 "대체 글자 생성기"로 활용하는 것이 현실적

#### 한글 전용 AI 폰트 생성 연구 (2025 최신)

한글은 11,172자의 방대한 글자 수와 초성·중성·종성의 조합 구조 때문에 특수한 접근이 필요하다.

**Few-shot 방식 (소수 샘플로 전체 생성):**
- **SKFont**: 조건부 GAN 기반. **114개 샘플**만으로 나머지 11,172자를 동일 스타일로 자동 생성. 골격(skeleton) 기반 접근
- **CKFont**: 초성/중성/종성 컴포넌트 기반. **28개 글자**만으로 모든 한글을 생성하는 GAN 모델
- **Patch-Font (2025.02)**: 패치 기반 어텐션 + 멀티태스크 인코딩. 기존 few-shot 방법(VQ-Font 등)이 한글에서 일반화에 실패한 문제를 해결 시도

**컴포넌트 인식 방식 (2025 최신):**
- **Positional Component-Guided (2025.07)**: YOLOv8-Seg로 한글을 자모 컴포넌트로 분해한 뒤, 조건부 GAN으로 스타일 전이. 자모의 위치적 의미를 활용하여 SSIM 0.9798 달성 (기존 MX-Font, CKFont 능가)
- **HFH-Font**: 디퓨전 모델 기반 고해상도 few-shot 합성. 벡터 글리프 변환까지 지원

**핵심 시사점:**
- Noto Sans 직접 수정보다, **소수 스타일 샘플 → AI 자동 확장**이 훨씬 현실적
- CKFont 접근(28자 → 전체)이 개인 작업자에게 가장 매력적이나, 아직 상용 서비스는 아님
- 학술 연구 수준이므로 직접 사용하려면 Python/ML 환경 필요 (PC 필수)

### 4. 전문가 워크플로우 (2025-2026)

- **Glyphs App + AI 어시스턴트**: Claude/ChatGPT를 활용해 플러그인 제작, 디자인 로직 자동화
- **Glyphr Studio**: 웹 기반 오픈소스 폰트 에디터. 협업 기능 + AI 보조 벡터 편집
- **FontForge**: 무료 오픈소스. 스크립팅으로 AI 생성 결과물 일괄 처리 가능

### 5. 아이폰 환경에서의 현실적 워크플로우

**가능한 것:**
- 웹 기반 도구(Creative Fabrica, GLIPH, Font AI, Glyphr Studio)로 기본 작업
- Calligraphr 템플릿을 아이폰에서 작성 (Apple Pencil 없이도 손가락으로 가능)
- 프롬프트 기반 AI 도구로 컨셉/스타일 탐색

**PC 필요한 것:**
- Fontself (Illustrator/Photoshop 플러그인)
- FontForge 세밀한 편집
- 벡터화 작업 (Illustrator)
- 최종 폰트 파일 테스트 및 미세 조정

**제안 워크플로우:**
1. 평소(아이폰): 웹 기반 도구로 글자 스타일 실험, 프롬프트 테스트, 참고 자료 수집
2. 휴가/외출(PC): FontForge/Glyphs에서 정밀 편집, 벡터화, 최종 빌드

## 주요 iOS 앱

- **Font Generator - AI Text Art** (App Store): AI 텍스트 아트 생성 (폰트 파일 생성은 아님, 스타일 탐색용)

## 참고: Noto Sans 수정 대안

Noto Sans를 직접 수정하는 대신 고려할 접근:
- AI 도구로 Noto Sans "스타일"을 참조한 새 폰트 생성
- 소수 글자만 커스터마이즈가 목표라면 Fontself나 Glyphr Studio가 적합
- 전체 다국어 폰트가 목표라면 ML 기반 글자 확장(접근법 B)이 가장 현실적

## 출처

- [Lummi - Best AI Font Generators 2025](https://www.lummi.ai/blog/best-font-generators)
- [Skywork AI - 2026 Guide to AI Font Generation](https://skywork.ai/skypage/en/ai-font-generation-guide/2019016119495294976)
- [Creative Fabrica - AI Font Generator](https://www.creativefabrica.com/tools/ai-font-generator/)
- [Font AI](https://www.font-ai.com/)
- [GLIPH - AI-Powered Font Generator](https://gliph.us/)
- [Bylo.ai - AI Font Generator](https://bylo.ai/features/ai-font-generator)
- [GitHub - ai-typography (ML typeface creation)](https://github.com/mansgreback/ai-typography)
- [NeoSpark - Best AI Font Generators 2025](https://useneospark.com/blog/best-ai-font-generators-2025/)
- [Grovers - Best AI Font Generators 2026](https://grovers.io/best-ai-font-generators/)
- [I Love Typography - Fonts and AI](https://trust.ilovetypography.com/fonts-and-ai/)

### 한글/CJK AI 폰트 연구 출처
- [Positional Component-Guided Hangul Font Generation (2025)](https://www.mdpi.com/2079-9292/14/13/2699) — YOLOv8 + GAN 기반 한글 폰트 생성
- [Patch-Font: Few-Shot Font Generation (2025)](https://www.mdpi.com/2076-3417/15/3/1654) — 패치 기반 어텐션 few-shot 접근
- [SKFont: Skeleton-Driven Korean Font Generator](https://link.springer.com/article/10.1007/s10032-021-00374-4) — 114개 샘플로 전체 한글 생성
- [HFH-Font: Few-Shot Chinese Font Synthesis (ACM TOG)](https://dl.acm.org/doi/10.1145/3687994) — 디퓨전 모델 기반 고해상도 합성
- [Few-Shot Korean Font Generation based on Hangul Composability](https://koreascience.or.kr/article/JAKO202106153177641.page) — 한글 조합성 활용

---

## 관련 문서

- [오픈소스 기반 자체 서체 제작 벤치마킹](2026-03-25_open-source-font-fork-benchmarking.md)
- [CK Font 제작 전략](../condensed-kiwi/projects/2026-03-25_ck-font-creation/_index.md)
- [CK 브랜딩 프로젝트](../condensed-kiwi/projects/2026-04-01_ck-branding/_index.md)
