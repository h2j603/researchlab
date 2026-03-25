---
title: "출처 — CK Font 제작 전략"
date: 2026-03-25
updated: 2026-03-25
status: in-progress
type: reference
tags: [typography, ai, font-distribution]
related: ["_index.md", "findings.md"]
confidence: medium
---

# 출처 — CK Font 제작 전략

## AI 폰트 생성 도구

- [Creative Fabrica - AI Font Generator](https://www.creativefabrica.com/tools/ai-font-generator/) — 글자 드로잉 → AI 정제 → TTF 다운로드. 웹 기반, 무료 계정 가능
- [GLIPH](https://gliph.us/) — 이미지를 TTF 폰트로 변환. 무료, 웹 기반
- [Font AI](https://www.font-ai.com/) — 텍스트 프롬프트 기반 폰트 생성, OFL 준수
- [Calligraphr](https://www.calligraphr.com/) — 손글씨 템플릿 → 폰트 변환. 20~30분 소요
- [Fontself](https://www.fontself.com/) — Illustrator/Photoshop 플러그인. 아트워크를 폰트로 변환
- [Bylo.ai](https://bylo.ai/features/ai-font-generator/) — 다국어(중국어, 아랍어) 지원 AI 폰트 생성

## 폰트 에디터

- [Glyphr Studio](https://www.glyphrstudio.com/) — 웹 기반 오픈소스 폰트 에디터
- [FontForge](https://fontforge.org/) — 오픈소스 전문 폰트 편집기
- [Glyphs](https://glyphsapp.com/) — 맥용 전문 폰트 디자인 도구

## AI 폰트 생성 연구

- [Positional Component-Guided Hangul Font Generation (2025)](https://www.mdpi.com/2079-9292/14/13/2699) — 한글 폰트 AI 생성 최신 연구 (SSIM 0.9798)
- [SKFont (2021)](https://link.springer.com/article/10.1007/s10032-021-00374-4) — 114자 샘플로 전체 한글 글리프 생성
- [GitHub - ai-typography](https://github.com/mansgreback/ai-typography) — ML 기반 타입페이스 생성 프로젝트

## 리뷰/가이드

- [Lummi - Best AI Font Generators 2025](https://www.lummi.ai/blog/best-font-generators)
- [NeoSpark - Best AI Font Generators 2025](https://useneospark.com/blog/best-ai-font-generators-2025/)
- [Grovers - Best AI Font Generators 2026](https://grovers.io/best-ai-font-generators/)
- [I Love Typography - Fonts and AI](https://trust.ilovetypography.com/fonts-and-ai/)

## 베이스 서체 후보 (포크용)

- [Iosevka GitHub](https://github.com/be5invis/Iosevka) — 코드 기반 빌드, Condensed + Mono + Geometric. 21.9k stars. SIL OFL
- [Iosevka 공식 사이트](https://typeof.net/Iosevka/) — 커스터마이저, 문서
- [Martian Mono GitHub](https://github.com/evilmartians/mono) — Variable Font (wdth + wght), 기하학적 모노스페이스. SIL OFL
- [JetBrains Mono](https://www.jetbrains.com/lp/mono/) — 기하학적 모노스페이스, 좁은 폭. SIL OFL
- [Space Mono](https://github.com/googlefonts/spacemono) — 60년대 기하학 스타일. Apache 2.0
- [IBM Plex GitHub](https://github.com/IBM/plex) — 체계적 패밀리, 8웨이트. SIL OFL
- [Monaspace GitHub](https://github.com/githubnext/monaspace) — GitHub 공식, 5개 하위 패밀리. SIL OFL

## CK 레퍼런스 서체

- **Druk** (Commercial Type) — 극단적 컨덴스드/와이드, 강렬한 헤드라인
- **Dharma Gothic** — 무료 컨덴스드 서체, 다양한 웨이트
- **GT America Compressed** — 기하학적 컨덴스드 산세리프
- **Space Grotesk** (오픈소스) — 기하학적 산세리프, 모노스페이스 느낌
- **IBM Plex Sans Condensed** (오픈소스) — 기하학적 컨덴스드, Variable Font 지원
- **Monument Extended** — 와이드/컨덴스드 대비가 강한 디스플레이 서체

## 관련 문서
- [findings.md](findings.md)
- [_index.md](_index.md)
