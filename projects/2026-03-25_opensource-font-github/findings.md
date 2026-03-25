---
title: "오픈소스 폰트 GitHub 프로젝트 — 상세 조사"
date: 2026-03-25
updated: 2026-03-25
status: in-progress
type: research
tags: [typography, font-distribution, tool, case-study, ai]
related: ["_index.md", "../../inbox/2026-03-25_ai-font-creation-tools.md"]
confidence: medium
---

# 오픈소스 폰트 GitHub 프로젝트 — 상세 조사

---

## 1. 소규모 팀/개인이 만든 오픈소스 서체 프로젝트

### 주요 프로젝트 목록

| 프로젝트 | 제작자 | Stars | 특징 | 제작 도구 |
|----------|--------|-------|------|-----------|
| [Iosevka](https://github.com/be5invis/Iosevka) | be5invis (개인) | 21.9k | 코드용 가변 서체. 빌드 시스템으로 수천 가지 변형 자동 생성 | JavaScript 기반 자체 빌드 시스템 |
| [Maple Font](https://github.com/subframe7536/maple-font) | subframe7536 (개인) | 24.7k | 라운드 코너 모노스페이스. 중영문 2:1 완벽 비율. 리거처 지원 | Python, OpenType |
| [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic) | be5invis (개인) | 12k | Iosevka + Source Han Sans 합성 CJK 서체. 한/중/일 지원 | Iosevka 빌드 + JavaScript |
| [Playfair](https://github.com/clauseggers/Playfair) | Claus Eggers (개인) | 590 | 범용 세리프 서체. 라틴/키릴 지원 | Glyphs App |
| [Plus Jakarta Sans](https://github.com/tokotype/PlusJakartaSans) | Tokotype (소규모 스튜디오) | 1k | 자카르타시 공식 서체. "협업의 도시" 프로그램용 | Python (fontmake) |
| [jf open 粉圓](https://github.com/justfont/open-huninn-font) | justfont (소규모 팀) | 1.3k | 대만 전통 중국어 라운드 서체. 보포모포/타이기 기호 포함 | OpenType |
| [undefined medium](https://github.com/andirueckel/undefined-medium) | andirueckel (개인) | 580 | 픽셀 그리드 기반 모노스페이스. 500+ 글자 | 직접 디자인 |
| [Hauora Sans](https://github.com/WCYS-Co/Hauora-Sans) | WCYS Co (소규모 팀) | 173 | 네오 그로테스크 산세리프. 건강 연구 프로젝트에서 시작 | Glyphs App |

### 워크플로우 패턴 분석

**패턴 A: 코드 기반 생성 (Iosevka, Sarasa Gothic)**
- 글리프를 코드로 정의하고, 빌드 시스템이 폰트 파일을 자동 생성
- 사용자가 설정 파일로 수천 가지 변형을 커스터마이즈 가능
- GitHub Actions로 자동 빌드 및 릴리즈
- 장점: 재현 가능, 변형 무한, 협업 용이
- 단점: 진입 장벽 높음, 코딩 필수

**패턴 B: 전통 도구 + GitHub (Playfair, Hauora Sans)**
- Glyphs App 또는 FontForge에서 디자인
- .glyphs / .ufo 소스 파일을 GitHub에 커밋
- fontmake/gftools로 빌드 자동화
- Google Fonts 파이프라인과 호환

**패턴 C: 합성/패칭 (Nerd Fonts, Sarasa Gothic)**
- 기존 폰트들을 스크립트로 결합/패칭
- FontForge Python 스크립팅 활용
- 자동화된 CI/CD 파이프라인

### 제작 도구 생태계

| 도구 | 유형 | 가격 | GitHub 연동 |
|------|------|------|-------------|
| **FontForge** | 오픈소스 에디터 | 무료 | Python 스크립팅으로 CI 연동 |
| **Glyphs App** | 상용 에디터 (Mac) | 유료 | .glyphs 파일 커밋 |
| **RoboFont** | 상용 에디터 (Mac) | 유료 | UFO 형식으로 Git 친화적 |
| **Glyphr Studio** | 웹 기반 오픈소스 | 무료 | [GitHub 리포](https://github.com/glyphr-studio/Glyphr-Studio-2) (278 stars) |
| **fontmake** | 빌드 도구 | 무료 | Google Fonts 표준 빌드 |
| **gftools** | 후처리 도구 | 무료 | Google Fonts QA |

---

## 2. AI/ML 기반 폰트 생성 GitHub 프로젝트

### Few-shot 폰트 생성 (소수 샘플 → 전체 글자)

이 분야의 핵심 흐름은 **NAVER/Clova AI** 팀이 주도하고 있다.

| 프로젝트 | Stars | 학회 | 접근법 | 특징 |
|----------|-------|------|--------|------|
| [MC-GAN](https://github.com/azadis/MC-GAN) | 447 | CVPR 2018 | Multi-Content GAN | Few-shot 폰트 스타일 전이의 초기 연구 |
| [fewshot-font-generation](https://github.com/clovaai/fewshot-font-generation) | 261 | 통합 리포 | FUNIT/DM-Font/LF-Font/MX-Font | **Clova AI의 통합 리포**. 4개 모델 비교 가능 |
| [LF-Font](https://github.com/clovaai/lffont) | 185 | AAAI 2021 | 로컬 스타일 표현 + 분해 | 글자의 부분별 스타일을 분리 학습 |
| [MX-Font](https://github.com/clovaai/mxfont) | 177 | ICCV 2021 | Multiple Localized Experts | 여러 전문가 네트워크로 세밀한 스타일 포착 |
| [VQ-Font (ICCV)](https://github.com/awei669/VQ-Font) | 152 | ICCV 2023 | VQ-VAE + 대조 학습 | 구조 보존 + 양자화된 스타일 전이 |
| [DM-Font](https://github.com/clovaai/dmfont) | 145 | ECCV 2020 | 분해 기반 생성 | 글자를 컴포넌트로 분해하여 생성 |
| [CF-Font](https://github.com/wangchi95/CF-Font) | 141 | - | Content Fusion | 콘텐츠 융합 기반 few-shot 생성 |
| [AGIS-Net](https://github.com/ueoo/AGIS-Net) | 129 | SIGGRAPH Asia 2019 | One-Stage Few-Shot | 예술적 글리프 이미지 합성 |
| [FsFont](https://github.com/tlc121/FsFont) | 84 | CVPR 2022 | Fine-Grained Local Styles | PaddlePaddle 구현 |
| [VQ-Font (AAAI)](https://github.com/Yaomingshuai/VQ-Font) | 56 | AAAI 2024 | 구조 인식 + 양자화 | 구조적 강화 버전 |
| [DA-Font](https://github.com/wrchen2001/DA-Font) | 46 | ACM MM 2025 | Dual-Attention | **2025년 최신**. 이중 어텐션 하이브리드 |
| [DeepCalliFont](https://github.com/lsflyt-pku/DeepCalliFont) | 31 | AAAI 2024 | Dual-modality GAN | 중국 서예체 특화. 이중 모달리티 |
| [GC-Font](https://github.com/wrchen2001/GC-Font) | 27 | BMVC 2025 | Global Context | **2025년 최신**. 전역 문맥 특징 모델링 |

### 핵심 관찰

- **Clova AI (NAVER)가 이 분야의 허브**: `clovaai/fewshot-font-generation` 리포 하나로 4개 모델을 통합 제공. 비교 실험에 가장 유용
- **대부분 PyTorch 기반**: Python + PyTorch가 사실상 표준. PaddlePaddle은 FsFont 정도
- **CJK 폰트에 특히 유용**: 한중일 글자 수가 방대하므로 few-shot 접근이 실질적 가치를 가짐
- **2025년에도 활발**: DA-Font(ACM MM 2025), GC-Font(BMVC 2025)가 최근 공개
- **실제 사용 가능한 폰트 파일 출력은 제한적**: 대부분 이미지(PNG) 생성까지만. OTF/TTF 변환은 별도 파이프라인 필요

### 실행 환경 요구사항

| 요구사항 | 상세 |
|----------|------|
| GPU | NVIDIA GPU 필수 (CUDA). 대부분 V100/A100 기준 |
| Python | 3.7~3.10 |
| 프레임워크 | PyTorch 1.x~2.x |
| 데이터셋 | 폰트 이미지 데이터셋 필요 (직접 렌더링하거나 제공된 것 사용) |

---

## 3. 오픈소스 폰트를 포크해서 새 서체를 만든 프로젝트

### 대표적 포크/파생 프로젝트

| 프로젝트 | Stars | 베이스 폰트 | 변형 내용 |
|----------|-------|-------------|-----------|
| [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic) | 12k | **Iosevka** + **Source Han Sans** | 두 폰트를 합성하여 CJK 코딩 폰트 생성. 한/중/일/라틴 통합 |
| [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) | 62.2k | **Hack, Source Code Pro** 등 50+ 폰트 | 기존 폰트에 3,600+ 아이콘 글리프를 패칭(추가) |
| [Maple Font](https://github.com/subframe7536/maple-font) | 24.7k | 독자 디자인이지만 Nerd Font 아이콘 통합 | 라운드 코너 + 리거처 + CJK 2:1 비율 |
| **중국어 산세리프** (IPAex 파생) | 2.4k | **IPAex Gothic** | 일본어 폰트를 중국어 간체용으로 변형 |
| **중국어 손글씨** (SetoFont 파생) | 2.1k | **SetoFont (濑户字体)** | 일본 손글씨 폰트를 중국어로 확장 |
| [Libertinus Serif](https://github.com/alerque/libertinus) | ~700 | **Linux Libertine** | 버그 수정 + 키릴 볼드 이탤릭 추가 (Khaled Hosny → Stefan Peev) |
| [jf open 粉圓](https://github.com/justfont/open-huninn-font) | 1.3k | **Kosugi Maru** (小杉丸ゴシック) | 일본어 라운드 고딕을 대만 전통 중국어로 확장. 보포모포/타이기 추가 |
| **GitHub Mona Sans / Hubot Sans** | - | GitHub 자체 개발 | 가변 축 3개(weight, width, slant). OFL 라이선스 |

### 포크 패턴 분석

**패턴 1: CJK 언어 확장**
- 가장 흔한 패턴. 일본어 폰트 → 중국어/한국어 확장
- 예: IPAex Gothic → 중국어 산세리프, Kosugi Maru → jf open 粉圓
- 이유: CJK 폰트는 글자 수가 방대하여 처음부터 만들기 어려움

**패턴 2: 기능 추가/패칭**
- 기존 폰트에 아이콘, 리거처, 특수 문자 등을 추가
- 예: Nerd Fonts (아이콘 패칭), Sarasa Gothic (Iosevka + Source Han Sans 합성)
- 자동화 스크립트로 업스트림 업데이트 추적

**패턴 3: 버그 수정/품질 개선**
- 원본 폰트의 문제를 고치고 별도 프로젝트로 유지
- 예: Libertinus (Linux Libertine 버그 수정), Inconsolata Sugar (공백 문제 수정)

**패턴 4: 스타일 변형**
- 기존 서체의 디자인 방향을 변경
- 예: 모노스페이스화(Robotization Mono), 라운드 처리, 웨이트 확장

### 라이선스 참고

대부분의 포크/파생 프로젝트는 **SIL Open Font License (OFL)**을 사용한다. OFL은:
- 자유로운 수정/재배포 허용
- 파생 폰트는 다른 이름을 사용해야 함 (Reserved Font Name 조항)
- 폰트 단독 판매는 불가 (소프트웨어 번들은 가능)

---

## 출처

### 소규모 팀/개인 프로젝트
- [Iosevka](https://github.com/be5invis/Iosevka) — 코드 기반 가변 서체
- [Maple Font](https://github.com/subframe7536/maple-font) — 라운드 모노스페이스
- [Playfair](https://github.com/clauseggers/Playfair) — 범용 세리프
- [Plus Jakarta Sans](https://github.com/tokotype/PlusJakartaSans) — 도시 공식 서체
- [Glyphr Studio 2](https://github.com/glyphr-studio/Glyphr-Studio-2) — 웹 기반 폰트 에디터
- [GitHub - Collaborative Open Source Type Design](https://fonts.github.io/typographic-collaboration/) — 협업 워크플로우

### AI/ML 프로젝트
- [Clova AI fewshot-font-generation](https://github.com/clovaai/fewshot-font-generation) — 4개 모델 통합
- [MC-GAN](https://github.com/azadis/MC-GAN) — CVPR 2018 Few-shot
- [VQ-Font](https://github.com/awei669/VQ-Font) — ICCV 2023
- [DA-Font](https://github.com/wrchen2001/DA-Font) — ACM MM 2025 최신
- [GC-Font](https://github.com/wrchen2001/GC-Font) — BMVC 2025 최신

### 포크/파생 프로젝트
- [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic) — Iosevka + Source Han Sans 합성
- [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) — 아이콘 패칭
- [jf open 粉圓](https://github.com/justfont/open-huninn-font) — Kosugi Maru 파생
- [Mona Sans & Hubot Sans](https://github.com/mona-sans) — GitHub 공식 폰트
- [FontForge](https://github.com/fontforge/fontforge) — 오픈소스 에디터
- [The Ultimate Font Design Tools 2025](https://joliciatype.com/the-ultimate-font-design-tools-in-2025-fontlab-glyphs-more/) — 도구 비교

---

## 관련 문서

- [AI 폰트 제작 도구 리서치](../../inbox/2026-03-25_ai-font-creation-tools.md)
- [AI 폰트 사례 연구](../../projects/2026-03-25_ai-font-case-studies/_index.md)
- [프로젝트 인덱스](_index.md)
