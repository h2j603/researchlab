---
title: "한국 마을표석 — 출처 정리"
date: 2026-05-05
updated: 2026-05-05
status: in-progress
type: reference
tags: [social-phenomenon, urban, material-culture, monument]
related: ["_index.md", "findings.md", "_critique.md"]
confidence: medium
---

# 출처 정리

> 출처는 (a) 직접 확인 / (b) 서지정보만 확보 / (c) 추가 검증 필요로 구분한다. 추가 발견 시 갱신.

## G. 발견 파이프라인 — 공공 데이터셋 (findings.md §11)

마을표석 ‘좌표·이미지·메타데이터’ 백본 후보. 하이브리드 4계층 전략의 데이터 소스.

| 우선 | 데이터셋 | URL | 포맷 | 좌표 | 사진 | 비고 |
|------|---------|-----|------|------|------|------|
| **L1 백본** | 전국향토문화유적표준데이터 | https://www.data.go.kr/data/15021147/standard.do | CSV/JSON | O | O | 위도·경도·이미지정보·조성시대 표준 스키마. ‘표석·비·유래비’ 키워드 필터 |
| **L2 텍스트 보강** | 한국학중앙연구원 한국향토문화전자대전 공간정보 (20200929) | https://www.data.go.kr/data/15052766/fileData.do | 파일 | O | X | 백과 항목 본문 링크 + 좌표 |
| **L3 좌표 검증** | 국가유산청 문화재 공간정보 (OpenAPI) | https://www.data.go.kr/data/3070426/openapi.do | OpenAPI(XML), SHP | O | O | GIS 기반, 지정유산 위주 |
| 보조 | 국가유산청 지정유산 지도다운로드 (20250831) | https://www.data.go.kr/data/15148507/fileData.do | 파일 | O | △ | 지정유산 한정 |
| 보조 | 국가유산청 문화유산 데이터 지도 (20211130) | https://www.data.go.kr/data/15094713/fileData.do | 파일 | O | △ | #2/#3의 시각화 파생 |
| 보조 | 모바일국가유산공간정보서비스 | https://gis-heritage.go.kr/ | 웹 | O | O | 좌표 검증용 인터페이스 |
| 한정 | 서울 열린데이터광장 | https://data.seoul.go.kr/ | CSV/JSON/API | △ | △ | 서울 표석 한정. 경기 67개와 무관 |
| 보조 | 한국향토문화전자대전 (HTML) | http://www.grandculture.net/korea | HTML | △ | O | 항목 단위 풍부, 정형 아님 |

**핵심 결론**: ‘마을표석’만 별도로 묶은 데이터셋은 **존재하지 않음**. L1을 백본으로 잡고 L2·L3로 보강하는 하이브리드가 최선. 매칭 못 잡힌 마을은 시·군지 PDF + 거리뷰 + 휴가 답사로 잔여 보강.

자세한 활용 시나리오는 [findings.md §11](findings.md) 참조.

-----

## A. 마을 공동체와 ‘마을 만들기’ 정책 비판

### 정헌목 (한국학중앙연구원, 인류학)
한국 아파트 공동체 인류학 연구의 대표 학자. 신도시·브랜드 단지에서의 ‘공동체’ 형성을 비판적으로 분석.

- 정헌목, 「가치 있는 아파트 만들기: 수도권 브랜드 단지에서의 공동체 형성의 조건과 실천」, 비교문화연구. (b)
- 정헌목, 「행동하는 소수, 침묵하는 다수: 브랜드 단지 내 어린이 사망사건으로 본 아파트 공동체성의 의미」, 한국문화인류학 49-2 (2016). (b)
- 정헌목, 「마을 기업가처럼 보기: 도시개발의 공동체적 전환과 공동체의 자본화」, 한국문화인류학. (b) — 서울시 마을 만들기 사업의 ‘마을’ 자본화를 비판적으로 분석.

### 기타
- 권봉관, 「도시의 ‘마을 만들기’에 따른 공동체의 형성과 메티스의 기능」, 민속연구 27 (2013). (b)
- 김기홍, 『마을의 재발견』, 울림 (2014). (b)

## B. 자연부락·동제·마을 경계의 민속학

- 한국민족문화대백과사전 ‘장승’, ‘솟대’ 항목. (a) — 학술적 출발점. 장승의 세 기능 ① 마을 수문신·수호신, ② 사찰·지역 간 경계표, ③ 이정표.
- 이필영(한남대), 마을신앙·동제 연구. (b)
- 주강현, 마을 공동체와 민속 연구. (b)
- 한국역사민속학회·한국민속학회 학술지 — 자연부락 단위 마을신앙 연구 다수. (c)

## C. 신도시 단지명·지명 부여 연구

- 김기빈, 『땅이름 뿌리찾기: 토지개발지역 지명유래』, 한국건설기술연구원 (2000). (b)
- 한국토지공사, 『일산신도시 개발사업 기본계획』 (1990). (b)
- 한국토지공사, 『일산신도시 사인시스템 및 가로시설물 설계 종합보고서』 (1995). (b) — **표지석 포함 사인시스템의 직접 1차 자료. 우선순위 높음.**
- 한국토지개발공사, 『수도권 신도시 건설사업』 (1991). (b)

## D. 비석·금석문·물질문화

- 한국금석학회, 『금석문 연구』. (b)
- Susan Stewart, *On Longing: Narratives of the Miniature, the Gigantic, the Souvenir, the Collection*, Duke University Press (1993). (b) — 비석·기념물의 영속성·기억 연구.
- (추가 후보) 르페브르(Henri Lefebvre), *La production de l’espace* (1974) — ‘체험된 공간(lived space)’ 개념 직접 인용 시 필요. (c)

## E. 해외 비교 — 1차 자료 후보

- (일본) 道祖神·村名碑 관련 일본 민속학 자료. (c)
- (중국) 牌坊·石敢當 관련 중국 민속학·풍수학 자료. (c)
- (영국) Norfolk village signs — 1920년대 이후의 정교한 전통. 자료 확인 필요. (c)

## F. 연구 공백 메모

- “마을표석”을 단일 연구 대상으로 삼은 본격 학위논문·단행본은 검색 범위에서 발견되지 않음.
- 농촌 표석 → 신도시 아파트 단지 표석으로 이어지는 형식의 이동·재료의 의미론·공동체 호명 장치를 통합적으로 다룬 연구는 드물어 보임.
- 직접 다룰 경우 새로운 기여 가능성. 단, 가설 단계의 주장은 [_critique.md](_critique.md)에서 통제.

## 추천 출발점

**정헌목의 아파트 공동체 연구 + 한국문화인류학회의 마을 만들기 비판 연구 + 김기빈의 신도시 지명 자료** — 이 세 축을 함께 읽으면 학술적 토대를 잡을 수 있다.

-----

## H. 디자인 출판물 레퍼런스 (NL/DE 권 + 책+웹 하이브리드)

본 프로젝트의 결과물 형식 — **zine 또는 book+web 동시 퍼블리싱, Cyber Feminism Index(Mindy Seu, Inventory Press 2022) 수준의 큐레이팅된 아카이브** — 을 위한 참고 작업.

### 12개 핵심 레퍼런스

| # | 제목 / 작가 | 출판사 / 연도 | 포맷 | 다루는 대상 | 본 프로젝트와의 연결점 |
|---|------------|-------------|------|-----------|---------------------|
| H1 | **Library of the Printed Web** — Paul Soulellis | 자가출판 → MoMA Library | 책+웹+POD 진 시리즈 | 웹-투-프린트 아티스트 출판물 아카이브 | **‘공식 등록 외부 매체’를 큐레이팅+책+웹 하이브리드**로 묶는 가장 가까운 사례. CFI와 거의 동일한 DNA |
| H2 | **Caps Lock** — Ruben Pater | Valiz, 2021 | 책 (research essay+카탈로그) | 자본주의 도구로서의 그래픽 디자인 | 6 챕터 사례 카탈로그, 캡션이 본문만큼 중요. 표지·내지 ‘공식 매뉴얼’ 톤 차용. **NL 맥락에서 가장 가까운 톤** |
| H3 | **The Politics of Design** — Ruben Pater | BIS Publishers, 2016 | 시각 문화 핸드북 | 색·기호·문자·이미지의 문화적 정치학 | 좌우 페이지 = 사례+해설 견본첩. 그리드 기반 메타데이터 처리 — 표석 도상·서체·색 비교 카탈로그의 페이지 구조 모델 |
| H4 | **The New Alphabet (시리즈)** — HKW + 편집팀 | Spector Books, 2020~ | 책 시리즈 25권 + 행사 + 웹 | ‘새 알파벳’ 키워드 25개 사전 | 일관된 표지 시스템·번호. **시리즈 자체가 메타데이터**. 책+웹+이벤트 다층 퍼블리싱 |
| H5 | **FORENSIS: The Architecture of Public Truth** — Forensic Architecture (eds. Weizman·Franke) | Sternberg Press, 2014 | 다중 저자 리서치 문집 | 국가폭력 증거를 건축·공간 데이터로 재구성 | 표석을 단순 기록물이 아닌 **‘공식 진술의 인공물’**로 다루는 방법론 |
| H6 | **Atlas of the Conflict: Israel-Palestine** — Malkit Shoshan | 010 Publishers, 2010 | 지도책+데이터 아카이브 | 100년간 영토·행정·인구 변화 500여 지도 | 지도의 일관된 시각 시스템 + 카테고리 색인 + 연표·범례 모듈화. **표석을 지리·행정 데이터로 매핑할 때의 시각 표준화 모델** |
| H7 | **In Alphabetical Order: File Under Werkplaats Typografie** — eds. Stuart Bailey 외 | WT/Roma·Veenman, 2003 | 학교 아카이브 책 | WT 학생·교사 작업의 ABC 색인 | 알파벳 색인이 책 전체 구조. **‘분류 도식 자체가 디자인’이라는 사고** — 표석 항목 분류·색인의 모델 |
| H8 | **Roma Publications #1–425 at Sitterwerk** — Roger Willems / Hans Gremmen 사진 | Roma Publications, 2022 | 출판사 자기 아카이브 | 25년간 425권 출판물 사진 카탈로그 | 책을 오브제로 촬영, 인덱스+이미지 단순 페어링. **오브제(표석)를 일관된 촬영 규약으로 카탈로그화**하는 견본첩 모델 |
| H9 | **Space for Visual Research (1·2)** — Markus Weisbeck 외 | Spector Books, 2018·2023 | 책 시리즈 (Bauhaus Uni Weimar) | 추상·시각 실험의 학생 리서치 아카이브 | 그리드·플레이트 번호·작가 인덱스. **각자(刻字) 견본첩 + 인덱스 시스템** — 표석 유형별 매뉴얼 |
| H10 | **Set Margins'** (출판 카탈로그) — Freek Lommé | Set Margins', Eindhoven, 2022~ | 책+meetups 플랫폼 | ‘주변부에서 오는 충동’ 큐레이팅 — 디자인·액티비즘·비공식 출판 | **‘공식 외부’를 출판으로 정당화하는 편집 POV** — 마을표석의 핵심 정서와 일치 |
| H11 | **Onomatopee Research Projects** (시리즈) | Onomatopee, 2006~ | 책+전시 짝 (15~25권/년) | 자가발의 리서치 — 도시·생태·디자인·아카이브 | 전시-책 1:1 매칭. **‘전시+책’ 더블 퍼블리싱** — 본 프로젝트 결과물 형식의 직접 모델 |
| H12 | **Fw:Books 사진+리서치 시리즈** — Hans Gremmen | Fw:Books, 2008~ | 책 (사진+리서치) | 사진가 장기 아카이브 — 지형·인공물·기록사진 | 단일 디자이너 일관된 손맛, 사진 시퀀스+캡션 절제. **표석을 사진 아카이브로 다룰 때의 시퀀싱·여백 운용** |

### 추천 우선순위 (CFI 질감 가까운 순)

1. **H1 Library of the Printed Web** — 책+웹+POD 하이브리드, 큐레이팅 + 강한 편집 POV. CFI와 같은 DNA
2. **H2 Caps Lock** — 단일 저자 POV + 사례 카탈로그 + 그래픽 디자이너 주도. NL 톤
3. **H4 The New Alphabet** — 시리즈 자체가 큐레이팅 사전, 다층 퍼블리싱

### 본 프로젝트에 직접 적용 가능한 형식 요소

- **모듈러 표석 카드 (CFI식 entry card)**: 항목당 고정 메타데이터 슬롯 — 위치(좌표·행정구역) / 설치 주체(관·주민·기업) / 재질(S1~S5) / 서체 분류 / 설치 연도 / 문안 유형 / 사진. H1·H6 entry 모델 참고
- **분류 도식 자체를 표지·인덱스로**: H7 *In Alphabetical Order*처럼 G1·G2·G3 분류와 a/b/c/d 명명 4계열이 책의 구조이자 시각 시스템이 되도록 설계
- **각자 견본첩(specimen book) 구조**: H9·H2처럼 좌=실물 사진(통일 촬영 규약), 우=메타데이터+비평 캡션. 표석 서체를 디지털화한 견본 페이지 별도 챕터
- **책+웹 페어링** (H1 직접 모델): 책=큐레이팅 셀렉션 + 편집 에세이 / 웹=확장 가능 데이터셋(필터·지도·태그). 아이폰만으로 운영 가능한 정적 사이트(Are.na / Cargo / Tumblr) 기반
- **‘공식 외부’를 정당화하는 편집 POV** (H10·H2): 도입부에 **‘왜 비공식 표석을 다루는가’**의 선언적 에세이. 단순 도록과 차별화하는 핵심 — `findings.md` §11의 ‘메타 발견’(표석은 비등록·비지정이 본질)이 그 에세이의 1차 자료
- **연도·지역 시퀀스 그리드** (H6): 시간축 매핑 — 표석 설치 연도·지역 분포를 시각 시스템화한 인덱스 페이지

### 출처

- [Library of the Printed Web — Soulellis](https://soulellis.com/entries/lotpw.html)
- [Caps Lock — Valiz](https://valiz.nl/en/publications/caps-lock.html)
- [The New Alphabet — Spector / HKW](https://www.itsnicethat.com/articles/the-new-alphabet-spector-books-graphic-design-publication-260221)
- [FORENSIS — Sternberg Press](https://www.sternberg-press.com/product/the-architecture-of-public-truth/)
- [Forensic Architecture — Publications](https://forensic-architecture.org/programme/publications)
- [Onomatopee Publications](https://www.onomatopee.net/publications/)
- [Spector Books — Space for Visual Research](https://spectorbooks.com/space-for-visual-research)
- [Roma Publications #1–425 at Sitterwerk](https://www.perimeterbooks.com/products/roma-publications-1-425-at-sitterwerk-st-gallen-1)
- [Hans Gremmen / Fw:Books](https://fw-books.nl/author/hans/)
- [Werkplaats Typografie](https://werkplaatstypografie.org/)
- [Set Margins'](https://www.setmargins.press/)
- [The Politics of Design — BIS Publishers](https://www.bispublishers.com/the-politics-of-design.html)

-----

## 관련 문서
- [findings.md](findings.md)
- [_index.md](_index.md)
- [_critique.md](_critique.md)
