# Literature — 문헌/레퍼런스 노트 작성

논문, 아티클, 책, 영상 등 참고 자료를 문헌 노트로 정리한다.

## 실행 절차

1. 사용자의 입력(`$ARGUMENTS`)에서 자료 정보를 파악한다 (제목, URL, 저자 등)
2. `resources/` 디렉토리에 `YYYY-MM-DD_자료명.md` 파일을 생성한다 (자료명은 kebab-case 영문)
3. `templates/literature-note-template.md` 템플릿을 따른다
4. 사용자가 제공한 정보를 바탕으로 가능한 항목을 채운다:
   - 한 줄 요약
   - 요약 (3~5문단)
   - 핵심 주장/발견
   - 나의 생각/비판 (사용자의 관점을 반영하여 질문 형태로 제시)
   - 내 리서치와의 연결
5. 기존 프로젝트나 노트와 관련이 있으면 `related` 필드와 "관련 문서" 섹션에 링크한다
6. `_tags.md`에서 적절한 태그를 선택한다

## 입력 예시

- `/literature "Nostalgia and Consumer Behavior" — 복고 마케팅 관련 논문`
- `/literature https://example.com/article 아날로그 회귀 트렌드 기사`

## 주의사항

- URL이 제공되면 웹에서 내용을 가져와 정리한다
- 출처를 정확히 기재한다
- 사용자의 작업 관점(시각 문화, 물성, 아날로그-디지털 교차)에서 연결점을 제안한다
