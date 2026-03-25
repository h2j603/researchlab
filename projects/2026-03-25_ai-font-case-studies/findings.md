---
title: "AI 서체 완성·배포 사례 — 상세 조사"
date: 2026-03-25
updated: 2026-03-25
status: in-progress
type: research
tags: [typography, ai, font-generation, case-study, open-source]
related: ["../../inbox/2026-03-25_ai-font-creation-tools.md"]
confidence: medium
---

# AI 서체 완성·배포 사례 — 상세 조사

## 1. 실제 완성·배포된 AI 서체 사례

### 1-1. AIfont — Process Studio (2019~)

- **제작자**: Process Studio (비엔나 기반 아트 & 디자인 스튜디오)
- **기술**: 커스텀 DCGAN(Deep Convolutional GAN)을 텍스트 포함 이미지 대량 학습
- **결과물**: **500개의 AI 생성 폰트 파일 + 1개의 가변(Variable) 폰트**로 구성된 패키지. 실제 구매·설치 가능
- **맥락**: 2019년 비엔나 비엔날레 "UNCANNY VALUES" 전시(MAK 미술관)의 비주얼 아이덴티티로 사용. 전시 전반의 사이니지, 인쇄물, 설치 작품에 적용
- **특이사항**: 프로모션 텍스트 자체도 AI가 생성 — "거의 완전히 거짓"이라고 명시. 의도적으로 AI의 불완전성을 작품의 일부로 수용
- **현재 상태**: [aifont.process.studio](https://aifont.process.studio/)에서 판매 중. 트라이얼 폰트 제공
- **AI/인간 비율**: AI ~80% / 인간 ~20%. 글리프 생성 자체는 GAN이 전담. 인간은 학습 데이터 큐레이션, 모델 설계, 최종 폰트 파일 패키징 담당

### 1-2. Monotype × Blaze Type "Human Types" 프로젝트 (2025)

- **제작자**: Monotype 리서치팀 + Blaze Type (프랑스 파운드리)의 Matthieu Salvaggio
- **기술**: Monotype 자체 개발 생성형 AI 도구 (베타). 소수의 베지에 곡선 글리프를 입력하면 나머지 알파벳을 외삽(extrapolation)
- **결과물**: **6개의 한정 서체(limited fonts)** 공동 제작
- **맥락**: 2025년 6월 런던 Brand Talks에서 공개. Monotype의 Re:Vision 2025 타입 트렌드 보고서의 일부
- **핵심 발견**: 타입 디자이너가 AI를 "공동 창작 도구"로 사용한 공식 사례. Salvaggio는 AI의 가능성과 한계를 모두 보고
- **AI/인간 비율**: AI ~40% / 인간 ~60%. 초기 글리프 디자인, 스타일 방향, 최종 품질 검수는 전적으로 인간. AI는 글리프 확장(소수 → 전체 알파벳) 담당. 인간의 창작 판단이 주도적

### 1-3. Vondy AI Font Generator (2024~)

- **제작자**: Vondy (AI 도구 플랫폼)
- **기술**: 프롬프트 기반 서체 생성. 스타일 선택 후 간격, 획 두께, 대체 글리프, 리가처까지 조정 가능
- **결과물**: OTF/TTF 형식으로 내보내기 가능. Adobe, Canva, Figma에서 사용 가능
- **특징**: "실험"이 아니라 실용적 폰트 제작을 목표로 한 상용 서비스
- **AI/인간 비율**: AI ~70% / 인간 ~30%. 기본 생성은 AI, 세부 조정(간격, 두께, 스타일 변형)은 사용자가 수행

### 1-4. Font AI (font-ai.com) (2024~)

- **제작자**: Font AI
- **기술**: 기존 폰트 + 텍스트 프롬프트로 커스텀 변형 생성. Open Font License / Apache 라이선스 소스만 사용
- **결과물**: 사용 가능한 폰트 파일 생성. 폰트 식별(이미지에서 서체 인식) 기능도 포함
- **라이선스**: 원본 소스의 라이선스를 존중하며, 원작자 크레딧 명시
- **AI/인간 비율**: AI ~60% / 인간 ~40%. 사용자가 방향(프롬프트, 기반 폰트)을 설정하고, AI가 변형을 실행

### 1-5. Creative Fabrica AI Font Generator

- **기술**: 사용자가 직접 글자를 그리면 AI가 정제·정렬·간격 자동 조정 후 설치 가능한 폰트 파일로 변환
- **특징**: 무료 계정 사용 가능. 웹 기반(모바일 브라우저 가능)
- **AI/인간 비율**: AI ~50% / 인간 ~50%. 글자의 기본 형태는 인간이 그리고, AI는 정제·최적화 담당

---

## 2. 오픈소스 AI 폰트 생성 프로젝트 (GitHub)

### 2-1. FontDiffuser (AAAI 2024)

- **리포지토리**: [yeungchenwa/FontDiffuser](https://github.com/yeungchenwa/FontDiffuser)
- **기술**: 디노이징 디퓨전 + 멀티스케일 콘텐츠 어그리게이션 + 스타일 대비 학습
- **특징**: **원샷(One-Shot)** 폰트 생성 — 스타일 참조 이미지 1장으로 전체 글리프 세트 생성
- **학술 배경**: AAAI 2024 논문
- **실용성**: 연구 코드 공개. PyTorch 기반. 직접 폰트 파일 생성까지는 추가 파이프라인 필요
- **AI/인간 비율**: AI ~90% / 인간 ~10%. 인간은 스타일 참조 이미지 1장 제공 + 환경 설정만

### 2-2. Naver CLOVA AI — Few-Shot Font Generation 시리즈

- **리포지토리**: [clovaai/fewshot-font-generation](https://github.com/clovaai/fewshot-font-generation)
- **포함 모델**: FUNIT (ICCV'19), DM-Font (ECCV'20), LF-Font (AAAI'21), MX-Font (ICCV'21)
- **기술**: 소수 글리프 샘플에서 전체 폰트를 생성하는 GAN 기반 접근법들의 통합 저장소
- **특징**: 특히 **CJK(한중일) 폰트 생성**에 강점. 수천~수만 자의 글리프를 소수 샘플로 확장
- **AI/인간 비율**: AI ~85% / 인간 ~15%. 인간은 소수 참조 글리프 디자인 + 품질 검수

### 2-3. ai-typography — Stable Diffusion 기반

- **리포지토리**: [mansgreback/ai-typography](https://github.com/mansgreback/ai-typography)
- **기술**: 이미지 프롬프트 + 인페인팅을 통한 서체 생성. Stable Diffusion/Dreambooth 기반
- **기능**: 카테고리 결합, 보완, 새 서체 생성, 입력 서체 스타일화
- **실용성**: 누락 글자 추가, 새 서체의 출발점으로 활용 가능
- **AI/인간 비율**: AI ~70% / 인간 ~30%. 인간이 참조 이미지와 프롬프트로 방향 설정

### 2-4. deep-fonts

- **리포지토리**: [erikbern/deep-fonts](https://github.com/erikbern/deep-fonts)
- **기술**: 딥러닝 기반 폰트 생성 (초기 프로젝트)
- **특징**: 폰트의 잠재 공간(latent space)을 학습하여 서체 간 보간(interpolation) 가능
- **AI/인간 비율**: AI ~90% / 인간 ~10%

### 2-5. 한글 특화 프로젝트들

| 프로젝트 | 접근법 | 필요 샘플 수 | 특징 |
|----------|--------|-------------|------|
| **SKFont** | 골격 기반 조건부 GAN | 114자 | 골격(skeleton)에서 전체 11,172자 생성 |
| **CKFont** | 자모 컴포넌트 GAN | **28자** | 초·중·종성 분리 후 조합으로 전체 생성 |
| **Patch-Font** (2025) | 패치 어텐션 + 멀티태스크 | 소수 | VQ-Font의 한글 일반화 실패 문제 해결 시도 |
| **Positional Component-Guided** (2025) | YOLOv8-Seg + GAN | 소수 | SSIM 0.9798 달성. MX-Font, CKFont 능가 |

---

## 3. AI vs 인간 역할 요약

### AI가 잘하는 것
- **글리프 확장**: 소수 샘플 → 전체 글자 세트 (특히 CJK처럼 글자 수가 방대한 체계)
- **스타일 일관성 유지**: 수백~수천 글리프에 걸쳐 동일 스타일 적용
- **간격·정렬 자동화**: 메트릭스, 커닝 등 반복적 기술 작업
- **변형 생성**: 기존 서체에서 웨이트, 스타일 변형을 빠르게 생성

### 인간이 여전히 필수인 것
- **초기 디자인 방향 설정**: 어떤 느낌의 서체를 만들 것인가
- **핵심 글리프 디자인**: 참조 글리프의 품질이 최종 결과를 결정
- **품질 검수 및 미세 조정**: AI 생성 글리프의 오류 수정, 광학적 보정
- **베지에 곡선 최적화**: AI 생성 아웃라인은 종종 불필요하게 복잡
- **라이선스·윤리적 판단**: 학습 데이터의 출처, 원작자 권리 문제

### 역할 비율 스펙트럼

```
완전 AI ←──────────────────────────────→ 완전 인간

AIfont(Process)  FontDiffuser  Vondy  Monotype×Blaze  Creative Fabrica  전통 폰트 디자인
  AI 80%           AI 90%     AI 70%    AI 40%           AI 50%           AI 0%
```

---

## 4. 업계 반응: "AI 서체 역풍(Backlash)"

2026년 타이포그래피 트렌드에서 주목할 만한 역방향 움직임이 있다.

- 2023~2024년의 AI 생성 서체의 "무균적 균일성"에 대한 반발
- **"Imperfect by Design"** — 의도적 불완전성, 서사, 인간 흔적을 가진 타이포그래피를 추구
- **"AI가 만든 것처럼 보이는 폰트를 쓴다면, 이미 뒤처진 것"** 이라는 인식 확산
- AI가 모방할 수 없는 것에 가치를 두는 방향: 역사적 뉘앙스, 의도적 불완전성, 키네틱 움직임

이는 "최신의 기술로 최고의 아날로그함을 추구"하는 방향과 직접적으로 맞닿아 있다.

---

## 출처

### 실제 배포 사례
- [Process Studio — AIfont](https://process.studio/works/aifont-ai-generated-typeface/) — AI 생성 서체 500개 패키지
- [AIfont 판매 페이지](https://aifont.process.studio/)
- [Monotype — Human Types and AI Project](https://www.monotype.com/company/press-release/monotype-unveils-human-types-and-ai-project) — Blaze Type 협업 6개 한정 서체
- [Blaze Type — Designing Fonts with AI](https://blazetype.eu/blog/designing-fonts-with-ai/) — Monotype AI 도구 체험기
- [Font AI](https://www.font-ai.com/) — 프롬프트 기반 폰트 변형 생성
- [Creative Fabrica AI Font Generator](https://www.creativefabrica.com/tools/ai-font-generator/)

### 오픈소스 프로젝트
- [FontDiffuser (AAAI 2024)](https://github.com/yeungchenwa/FontDiffuser) — 원샷 디퓨전 폰트 생성
- [CLOVA AI Few-Shot Font Generation](https://github.com/clovaai/fewshot-font-generation) — DM-Font, LF-Font, MX-Font 통합
- [ai-typography](https://github.com/mansgreback/ai-typography) — Stable Diffusion 기반 서체 생성
- [deep-fonts](https://github.com/erikbern/deep-fonts) — 딥러닝 폰트 생성 초기 프로젝트

### 트렌드 및 분석
- [Lummi — Best AI Font Generators 2025](https://www.lummi.ai/blog/best-font-generators)
- [IK Agency — Typography Trends 2026](https://www.ikagency.com/graphic-design-typography/typography-trends-2026/)
- [Groteskly Yours — AI Fonts: The Future Is Here?](https://groteskly.xyz/blog/ai-fonts)
- [I Love Typography — Fonts and AI](https://trust.ilovetypography.com/fonts-and-ai/) — AI 폰트 전문 컨퍼런스

---

## 관련 문서

- [AI 폰트 제작 도구 및 워크플로우 리서치](../../inbox/2026-03-25_ai-font-creation-tools.md)
