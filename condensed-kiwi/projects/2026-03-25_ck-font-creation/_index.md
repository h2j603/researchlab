---
title: "CK Font 제작 전략 — AI 활용 영문 서체"
date: 2026-03-25
updated: 2026-03-25
status: in-progress
type: research
tags: [typography, ai, font-distribution, condensed-kiwi, analog-digital, tool]
related: ["../2026-04-01_ck-branding/_index.md", "../2026-04-01_ck-branding/findings.md"]
confidence: medium
---

# CK Font 제작 전략 — AI 활용 영문 서체

## 개요
- **배경**: NotoSans 포크를 통한 다국어 서체 제작이 난이도·범위 면에서 비현실적이라는 판단
- **전환**: 영문(라틴) 서체만 제작 → 글리프 수 ~230개로 범위 축소
- **목표**: AI 보조 워크플로우로 CK 정체성을 담은 완성도 높은 영문 서체 제작
- **제약**: 군복무 중 아이폰 위주 작업, 휴가 시에만 PC 가능

## 핵심 질문
1. AI로 "쓸 만한" 수준이 아니라 **전문 서체 수준**의 퀄리티를 만들 수 있는가?
2. 아이폰 환경에서 어디까지 진행할 수 있는가?
3. NotoSans 포크 대신 처음부터 만드는 것과, 기존 오픈소스를 변형하는 것 중 어느 쪽이 유리한가?
4. CK의 비주얼 아이덴티티(컨덴스드, 볼드, 산세리프)를 서체에 어떻게 녹이는가?

## 문서
- [리서치 및 전략](findings.md) — AI 폰트 제작 방법론, 도구, 실행 전략
- [비평](_critique.md) — Red Team 검증
- [출처](sources.md) — 참고 자료

## NotoSans 포크와의 차이

| | NotoSans 포크 (기존 방향) | AI 활용 영문 서체 (새 방향) |
|---|---|---|
| 범위 | 150개 문자 체계, 수만 글리프 | 라틴 알파벳 ~230 글리프 |
| 난이도 | 극히 높음 (타입 디자인 전문성 필요) | 중간 (AI 보조로 접근 가능) |
| 차별화 | 파라미터 조정으로는 NotoSans 그림자 벗어나기 어려움 | 처음부터 CK 성격을 설계 가능 |
| 라이선스 | OFL — 폰트 단독 판매 불가 | 자체 제작 시 라이선스 자유 |
| 다국어 | 기본 내장 | 추후 확장 가능 (영문 완성 후) |
| 실행 가능성 | 휴가 시 PC 필수, 장기 프로젝트 | 아이폰에서도 일부 진행 가능 |

## 관련 문서
- [CK 브랜딩 프로젝트](../2026-04-01_ck-branding/_index.md) — 원래 NotoSans 포크 논의가 있었던 프로젝트
- [AI 폰트 도구 리서치](../../../inbox/2026-03-25_ai-font-creation-tools.md) — 초기 도구 탐색
