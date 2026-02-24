# Data Dictionary & Governance Project

## 프로젝트
KBO 데이터 표준 정의서 및 거버넌스 체계 수립. (RFP DAR-001)
Sports2i(외주) 운영 시스템의 백업DB를 분석하여 신규 시스템용 데이터 표준 정의.

## RFP 요구사항 (DAR-001~009)
- **DAR-001**: 데이터 표준 및 코드 체계 수립 ← **우리 핵심 산출물**
  - 산출물: 데이터 표준 정의서 (데이터 사전, 식별자 체계, 코드 체계, 명명 규칙 포함)
  - 적용 대상: DB 컬럼, API 필드, Kafka/WebSocket 메시지 필드
- **DAR-002~009**: 데이터 모델 설계/마이그레이션 등 → 신규 시스템 수행사 과업 (우리 범위 밖, DAR-001이 입력물)
- 참고: `references/rfp_데이터요구사항.pdf`

## DB 접속
- 접속 정보: `.env` 파일 참조 (MSSQL_SERVER, MSSQL_PORT, MSSQL_USER, MSSQL_PASSWORD)
- `.env`는 `.gitignore`에 포함되어 git 추적 제외
- **DB1** (4개): 영구/누적. DB2 확정 → DB1 반영
- **DB2** (13개): 시즌 데이터. 경기 당일 S2i가 전송
- `_220328` = 최초 백업일. 데이터는 지속 갱신 중

## 참고 자료 (`references/`)
| 파일 | 역할 |
|------|------|
| `S2i_KBOP 백업 DB 테이블별 데이터 확인_260220.xlsx` | **공식 테이블 목록** (248개 인스턴스) |
| `S2i_KBOP DB 보유 국제대회 목록_260220.xlsx` | 국제대회 38개 대회 |
| `KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf` | 2022년 문서, **오래됨 참고만** |

## 현황
- 17개 DB, 39종 테이블, 252개 인스턴스, 25.7M행
- 구세대(GMKEY/PCODE) + 신세대(G_ID/P_ID) 공존
- S2i 대비 49개 테이블에서 +1컬럼 (컬럼명 미확인)
- S2i 미제공: pitch-to-pitch, 세이버메트릭스 → KBO 자체 구축

## 폴더 구조
```
data-dict/
├── references/          # 원본 참고 자료 (PDF, Excel)
├── raw/                 # 기계 추출 원본 데이터
│   ├── *.json           # 파이프라인 핵심 출력 (5개)
│   └── db-schemas/      # DB별 스키마 json+md (17DB)
├── analysis/            # Phase 1 분석 결과 문서
├── dictionary/          # Phase 2 데이터 사전 (핵심 산출물)
│   ├── game/            # 경기 기록 (12)
│   ├── stats/           # 통계 (10)
│   ├── realtime/        # 실시간 (9)
│   └── master/          # 마스터 (8)
├── standards/           # Phase 3 표준 정의 (5개 문서)
│   ├── abbreviations.md # 표준 약어 사전
│   ├── naming-rules.md  # 명명 규칙 (DB/API/Kafka/WS 4계층)
│   ├── domain-types.md  # 도메인 타입 정의 (12종)
│   ├── id-system.md     # ID 체계 (6종 핵심 ID)
│   └── code-dictionary.md # 코드 사전 (이벤트/팀/구장/상태)
├── glossary/            # Phase 4 업무 용어 사전
│   └── business-terms.md # ~165개 용어, 7개 도메인
├── governance/          # Phase 5 거버넌스 정책 (4개 문서)
│   ├── data-ownership.md    # 데이터 오너십 (역할 R-01~R-06, 접근 권한)
│   ├── quality-rules.md     # 품질 규칙 (검증 규칙, 심각도, KPI 5개)
│   ├── change-process.md    # 변경 관리 절차 (코드/스키마/문서 변경)
│   └── table-design-guide.md # KBO 자체 테이블 설계 가이드 (세이버/P-b-P)
├── exports/             # Excel 산출물
│   └── 데이터사전.xlsx   # Excel 출력 9시트 (export-excel.py로 생성)
├── docs/                # MkDocs 심볼릭 링크 (.gitignore)
├── mkdocs.yml           # MkDocs Material 설정
└── scripts/             # 데이터 파이프라인
    ├── 핵심 스크립트 (8개)
    ├── requirements.txt
    └── archive/         # 탐색용 스크립트 보관
```

---

## 완료

### Phase 1: 현황 파악 [완료]
- MSSQL 스키마 추출 → `raw/mssql-inventory.json`
- Excel 파싱 → `raw/excel-inventory.json`
- 백업DB ↔ S2i 비교 → `analysis/table-mapping.md`
- 컬럼 차이 75개 분석 → `analysis/column-diff.md`, `raw/column-diff.json`
- 코드값 분석 (HOW/PLACE/POSI/TB 등) → `analysis/code-analysis.md`
- ID 체계 분석 → `analysis/id-analysis.md`
- 네이밍 패턴 분석 → `analysis/naming-patterns.md`

### Phase 2: 테이블별 컬럼 상세 [완료]
- 39종 테이블 MSSQL 직접 조회 (컬럼 메타+샘플+코드값) → `raw/column-metadata.json`
- 도메인별 사전 43파일 생성 → `dictionary/`
  - `game/` 12개: GAMEINFO, GAMECONTAPP, ENTRY, Hitter, Pitcher, Score, DEFEN 등
  - `stats/` 10개: BatTotal, PitTotal, TeamRank, KBO_BATRESULT(90col), SEASON_PLAYER_* 등
  - `realtime/` 9개: IE_LiveText, IE_BatterRecord, IE_PitcherRecord 등
  - `master/` 8개: person, TEAM, STADIUM, KBO_schedule 등

### Phase 2.5: dictionary/ 보강 [완료]
- dictionary/ 39파일에 버전 태그 추가 (`> 최종수정: YYYY-MM-DD | 출처: ...`)
- dictionary/ 39파일에 `표준명(안)` 컬럼 추가 (462개 레거시→snake_case 매핑)
- Excel 출력 생성 → `exports/데이터사전.xlsx` (목차/컬럼사전/코드값/문서정보 4시트)
- 프로젝트 폴더 구조 정리 (references/, raw/db-schemas/, scripts/archive/)
- 상호참조 규칙 정의 (작업 규칙에 반영)

### Phase 3: 표준 정의 [완료]
- 표준 약어 사전 → `standards/abbreviations.md`
  - 식별자/야구기록(타격25+투수20+수비6)/경기정보/시스템 약어, 접미사 11종, KBO 비표준 약어 10개
- 명명 규칙 확정 → `standards/naming-rules.md`
  - DB(snake_case) / API(camelCase) / Kafka(dot.lower) / WebSocket 4계층
  - 레거시→표준 변환 5원칙, Do/Don't 예시
- 도메인 타입 정의 → `standards/domain-types.md`
  - 12종 표준 타입 (identifier~inning_score), 현행→표준 전환 가이드
  - 인코딩 정책 (한글=nvarchar), NULL 처리 정책
- ID 체계 확정 → `standards/id-system.md`
  - 6종 핵심 ID (game_id, player_id, team_id, stadium_id, season_id, league/series_id)
  - 복합 PK 표준, 레거시 매핑, 특수값 처리 (T/B 합계, 9999 통산)
  - 팀 코드 이력 관리, 신규 테이블 ID 가이드
- 코드 사전 → `standards/code-dictionary.md`
  - 경기 이벤트 (how_cd 49종, place_cd 13+종, wls_cd, out_count)
  - 포지션/라인업, 팀 코드 (현행10+역사+국제), 구장 18+종
  - 날씨/방송/경기상태 코드, **기록 상태 코드 신규 정의** (DRAFT→REVIEW→CONFIRMED→REVISED)

---

## TODO

### Phase 2.5 잔여
- [ ] S2i 추가 컬럼 정보 수령 시 해당 테이블 md 파일에 반영

### Phase 4: 용어 사전 + 컬럼 설명 채움 [완료]
- 업무 용어 사전 → `glossary/business-terms.md` (~165개 용어, 7개 도메인)
- 컬럼 설명 일괄 채움 → `scripts/fill-descriptions.py` → dictionary/ 28파일 252개 빈 설명 채움 (100% 커버리지)
- `export-excel.py` COL_DESC 확장 (~80개 → ~350개)
- `exports/데이터사전.xlsx` 재생성 (787개 컬럼, 설명 완비)

### Phase 5: 거버넌스 정책 [완료]
- 데이터 오너십 → `governance/data-ownership.md`
  - 역할 6종 (R-01~R-06), DB 접근 권한 매트릭스, 도메인별 오너십
  - S2i 계약 관리 원칙, ID 불변 원칙, 합계행 오너십, 감사 로그
- 품질 규칙 → `governance/quality-rules.md`
  - 심각도 3단계 (CRITICAL/WARNING/INFO), 검증 규칙 (필수필드/형식/수치/인코딩/정합성)
  - 특수값 처리 (-1 센티널, 9999 예약, T/B 합계행), KPI 5개, 미확인 코드 한시적 처리
- 변경 관리 절차 → `governance/change-process.md`
  - 변경 유형 10종 (C1~C3, S1~S4, D1~D3), record_status_cd 상태 전이도
  - 코드/스키마/문서 개정 절차, 긴급 Fast-Track, 변경 요청서 양식
- KBO 자체 테이블 설계 가이드 → `governance/table-design-guide.md`
  - 테이블 명명 (접두사: PITCH_/SABER_/KBO_OPS_), PK/ID 설계 원칙
  - 컬럼 표준 (감사 3컬럼 필수, 금지 타입), 인덱스 가이드
  - 세이버메트릭스 테이블 패턴 (타자/투수/가중치 파라미터)
  - Pitch-by-Pitch 설계 패턴 (구종 10종), 설계 승인 6단계, 체크리스트

### Phase 6: 통합 강화 (Excel 확장 + MkDocs HTML) [완료]
- Excel 5시트 추가 → `exports/데이터사전.xlsx` (4시트 → 9시트)
  - 시트 5 표준 요약: 4계층 명명, 12종 도메인 타입, 접미사→MSSQL 매핑, 변환 5원칙 (28항목)
  - 시트 6 ID 체계: 7종 핵심 ID + 복합 PK 표준 11건 (20항목)
  - 시트 7 코드 사전: how_cd 49종, place_cd, 팀 12종, 구장 18종, 날씨/방송/상태/포지션 (128항목)
  - 시트 8 용어 사전: 타격/투수/수비/세이버/경기운영/선수팀/품질 (61항목)
  - 시트 9 거버넌스 요약: 역할 R-01~R-06, 오너십, KPI 5개, 변경 유형 10종 (29항목)
- 테이블 목록 조감도 신규 → `dictionary/index.md`
  - 39종 테이블 도메인별 목록 (컬럼수/행수/PK/세대/설명), FK 관계도, 세대 분포
- MkDocs Material 사이트 → `mkdocs.yml` + `docs/` (심볼릭 링크)
  - 한글/영문 전문 검색, 라이트/다크 모드, 탭 내비게이션
  - `docs/` 심볼릭 링크로 원본 파일 이중 관리 방지
  - `mkdocs serve` → localhost:8000, `mkdocs build` → `site/`

### 미결 사항
- [ ] S2i에 +1 컬럼명 확인 요청 (49개 테이블) → 수령 후 dictionary/ 반영
- [ ] DEFEN +6컬럼, ENTRY -1컬럼 상세 확인
- [ ] varchar 한글 인코딩(EUC-KR) 처리 방안 → `standards/domain-types.md` Section 5에 정책 정의 완료, 실제 전환은 마이그레이션 시
- [ ] 코드 사전 미확인 항목 S2i 확인: BH 코드(14,749건), PLACE 문자코드(A~S), game_flag(4,7,8,9), series_id(1~9)

---

## 작업 규칙
- 문서: 한글 (기술 용어 영문 유지)
- 코드값: 영문 대문자
- 사전: `dictionary/도메인/테이블.md` (1테이블 1파일)
- 기술스택: Python 3 (pymssql, openpyxl), Markdown
- 버전 태그: dictionary/ 파일 상단에 `> 최종수정: YYYY-MM-DD | 출처: ...` 유지
- 상호참조: 문서 간 참조 시 상대경로 링크 사용
  - 형식: `→ 참고: [문서명](상대경로)`
  - 예시: `→ 참고: [표준 약어 사전](../standards/abbreviations.md)`
  - 참조 관계:
    - `standards/naming-rules.md` ↔ `standards/abbreviations.md` (약어 기반 명명)
    - `standards/code-dictionary.md` ↔ `standards/id-system.md` (코드값에 ID 참조)
    - `standards/id-system.md` ↔ `dictionary/` (레거시↔표준 매핑)
    - `standards/domain-types.md` ↔ `dictionary/` (타입 정의 적용)
    - `governance/change-process.md` ↔ `standards/code-dictionary.md` (코드 변경 절차)
    - `governance/data-ownership.md` ↔ `governance/change-process.md` (역할→승인 주체)
    - `governance/quality-rules.md` ↔ `standards/domain-types.md` (타입별 검증 규칙)
    - `governance/table-design-guide.md` ↔ `standards/naming-rules.md` (신규 테이블 명명)
    - `governance/table-design-guide.md` ↔ `standards/id-system.md` (신규 ID 설계)

## 스크립트 파이프라인 (`scripts/`)
```
1. inventory-mssql.py      → raw/mssql-inventory.json
2. inventory-excel.py      → raw/excel-inventory.json
3. column-diff.py          → raw/column-diff.json
4. extract-columns.py      → raw/column-metadata.json
5. generate-dictionary.py  → dictionary/{domain}/{table}.md
6. upgrade-dictionary.py   → dictionary/ 버전태그+표준명 추가
7. export-excel.py         → exports/데이터사전.xlsx
8. fill-descriptions.py    → dictionary/ 빈 설명 일괄 채움
```
