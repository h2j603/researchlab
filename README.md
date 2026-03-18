# Research Lab

Claude와 함께 운영하는 개인 리서치 랩입니다.

## 시스템 개요

**PARA + Zettelkasten 하이브리드** 구조를 채택합니다:
- **PARA**(Projects/Areas/Resources/Archive)로 실행 가능성 기반 분류
- **Zettelkasten** 스타일 링크로 노트 간 유기적 연결
- **MOC**(Maps of Content)로 주제별 네비게이션

## 워크플로우

```
아이디어 → inbox/ → 정리 → projects/ or areas/ or resources/
                                    ↓ (완료 시)
                                archive/
```

1. 아이디어/질문이 생기면 `inbox/`에 빠르게 캡처
2. 본격 리서치는 `projects/YYYY-MM-DD_주제명/`에서 진행
3. 지속 관심 분야는 `areas/`에서 관리
4. 참고 자료/문헌 노트는 `resources/`에 정리
5. 완료된 프로젝트는 `archive/`로 이동
6. 주기적으로 `inbox/` 정리

## 디렉토리 구조

| 디렉토리 | 용도 | 예시 |
|-----------|------|------|
| `inbox/` | 빠른 캡처, 미정리 메모 | 떠오른 아이디어, 질문 |
| `projects/` | 진행 중인 리서치 프로젝트 | `2026-03-18_llm-scaling-laws/` |
| `areas/` | 지속적 관심 분야 | `ai-research/`, `systems-thinking/` |
| `resources/` | 참고 자료, 문헌 노트 | 논문 요약, 개념 정리 |
| `archive/` | 완료/비활성 프로젝트 | 끝난 리서치 |
| `templates/` | 노트 템플릿 | 리서치, 문헌 노트, 컨셉 노트 |
| `assets/` | 이미지, PDF 등 | 다이어그램, 스크린샷 |

## 주요 파일

- `CLAUDE.md` — Claude 협업 규칙 및 작업 원칙
- `_index.md` — 전체 네비게이션 (MOC)
- `_tags.md` — 공식 태그 목록
