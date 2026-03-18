# Research Lab — Claude 협업 가이드

## 이 리포지토리의 목적
이 리포지토리는 사용자의 개인 리서치 랩입니다.
Claude와 함께 다양한 주제를 깊이 있게 조사하고, 결과를 체계적으로 정리하는 공간입니다.

## 작업 원칙

### 리서치 워크플로우
1. 아이디어나 질문이 떠오르면 `inbox/`에 빠르게 캡처한다
2. 본격적인 리서치는 `projects/YYYY-MM-DD_주제명/` 폴더를 만들어 진행한다
3. 각 프로젝트 폴더에는 `_index.md`(MOC/요약)와 `findings.md`(상세 내용)를 포함한다
4. 지속적으로 관심 있는 분야는 `areas/`에서 관리한다
5. 참고 자료, 문헌 노트는 `resources/`에 정리한다
6. 완료된 프로젝트는 `archive/`로 이동한다
7. 주기적으로 `inbox/`를 정리하여 적절한 위치로 이동한다

### YAML 프론트매터 규칙
모든 마크다운 문서에 아래 형식의 프론트매터를 포함한다:
```yaml
---
title: "제목"
date: YYYY-MM-DD
updated: YYYY-MM-DD
status: inbox | in-progress | review | complete | archived
type: research | literature-note | concept | reference | log
tags: [태그1, 태그2]
related: ["파일경로1.md", "파일경로2.md"]
confidence: high | medium | low | speculative
---
```

### 태깅 규칙
- 태그는 반드시 YAML 프론트매터의 `tags` 필드에 배열로 작성한다 (본문 내 `#태그` 사용 금지)
- kebab-case 사용: `machine-learning`, `large-language-model`
- `_tags.md` 파일에 공식 태그 목록을 관리하여 태그 중복/분산을 방지한다

### 링크 규칙
- 표준 마크다운 링크를 사용한다: `[제목](상대경로.md)`
- 항상 상대 경로를 사용한다 (절대 경로 금지)
- 각 노트 하단에 "관련 문서" 섹션을 두어 2~5개의 관련 노트를 링크한다

### 품질 기준
- 출처가 있는 정보는 반드시 출처를 명시한다
- 주장과 사실을 구분하여 기술한다
- 불확실한 정보는 `confidence: low` 또는 `confidence: speculative`로 표시한다
- 한국어로 작성하되, 기술 용어는 영어 병기를 허용한다

### 결과물 형식
- 마크다운(.md)을 기본 형식으로 사용한다
- 코드 예제가 포함될 경우 적절한 언어 태그를 사용한다
- 다이어그램이 필요한 경우 Mermaid 문법을 사용한다
- 이미지/PDF 등 바이너리 파일은 `assets/` 디렉토리에 저장한다

### Maps of Content (MOC)
- 각 주요 폴더에 `_index.md` 파일을 두어 해당 폴더의 네비게이션 허브로 사용한다
- MOC는 단순 목록이 아니라, 맥락과 설명을 포함한 큐레이션된 링크 페이지이다
- 특정 주제에 노트가 5개 이상 쌓이면 해당 주제의 MOC를 생성한다

### Claude 협업 규칙
- Claude는 "생각 모드"(질문하고 토론)와 "작성 모드"(결과물 생성)를 구분한다
- 리서치 시작 시 먼저 핵심 질문을 정리하고 접근 방법을 논의한 후 조사에 들어간다
- Claude는 새 노트 작성 시 관련 기존 노트와의 연결을 제안한다
- 최종 링크/분류 결정은 사용자가 한다

## 디렉토리 구조

```
researchlab/
├── CLAUDE.md              # 이 파일 — Claude 협업 규칙
├── README.md              # 리서치 랩 소개
├── _index.md              # 최상위 MOC (전체 네비게이션)
├── _tags.md               # 공식 태그 목록
├── inbox/                 # 빠른 캡처 (정리 전 메모, 아이디어)
├── projects/              # 진행 중인 리서치 프로젝트
│   └── YYYY-MM-DD_주제명/
│       ├── _index.md      # 프로젝트 MOC
│       ├── findings.md    # 상세 조사 내용
│       └── sources.md     # 출처 정리
├── areas/                 # 지속적 관심 분야 (마감 없음)
├── resources/             # 참고 자료, 문헌 노트
├── archive/               # 완료/비활성 프로젝트
├── templates/             # 노트 템플릿
└── assets/                # 이미지, PDF 등 첨부 파일
    └── images/
```

## 커밋 메시지 규칙
- `research: 주제명 - 내용` — 리서치 관련
- `notes: 내용` — 메모/노트 관련
- `docs: 내용` — MOC, 인덱스 업데이트
- `chore: 내용` — 설정/구조 변경
