# 개발 및 운영 가이드

이 문서는 KBO DataHub의 일상적인 유지보수, 스크립트 파이프라인 상세, 테이블 추가/수정 절차를 기술한다.
프로젝트 개요는 [README.md](README.md), 아키텍처는 [architecture.md](architecture.md) 참조.

---

## 목차

1. [개발 환경 설정](#개발-환경-설정)
2. [스크립트 파이프라인 상세](#스크립트-파이프라인-상세)
3. [일상 유지보수 작업](#일상-유지보수-작업)
4. [테이블 추가 절차](#테이블-추가-절차)
5. [테이블 수정 절차](#테이블-수정-절차)
6. [AG Grid 데이터 갱신](#ag-grid-데이터-갱신)
7. [MkDocs 설정 변경](#mkdocs-설정-변경)
8. [트러블슈팅](#트러블슈팅)
9. [파일별 역할 요약](#파일별-역할-요약)

---

## 개발 환경 설정

### 필수 도구

| 도구 | 버전 | 용도 |
|------|------|------|
| Python | 3.12+ | 스크립트 실행, MkDocs |
| Git | 2.x | 버전 관리 |
| pip | 최신 | 패키지 관리 |

### 초기 설정

```bash
# 1. 저장소 클론
git clone git@github.com:kbop-platform/kbo-data-governance.git
cd kbo-data-governance

# 2. 가상 환경 생성
python3 -m venv .venv
source .venv/bin/activate

# 3. 의존성 설치
pip install mkdocs-material
pip install -r scripts/requirements.txt

# 4. (DB 접속이 필요한 경우) 환경 변수 설정
cat > .env << 'EOF'
MSSQL_SERVER=49.50.172.83
MSSQL_PORT=1433
MSSQL_USER=<사용자>
MSSQL_PASSWORD=<비밀번호>
EOF

# 5. 로컬 서버 실행
./serve.sh
# http://127.0.0.1:8000 에서 확인
```

---

## 스크립트 파이프라인 상세

### 전체 흐름

```
Phase 1: 데이터 추출 (DB 접속 필요)
  [1] inventory-mssql.py → raw/mssql-inventory.json
  [2] inventory-excel.py → raw/excel-inventory.json
  [3] column-diff.py → raw/column-diff.json
  [4] extract-columns.py → raw/column-metadata.json

Phase 2: 문서 생성 (오프라인)
  [5] generate-dictionary.py → dictionary/*.md 초기 생성
  [6] upgrade-dictionary.py → 표준명(안) 컬럼 추가
  [7] fill-descriptions.py → 빈 설명 필드 채움

Phase 3: 산출물 생성 (오프라인)
  [8] export-excel.py → exports/데이터사전.xlsx
  [9] enrich-metadata.py → 티어/오너/갱신주기 메타데이터
  [10] extract-mapping.py → migration/column-mapping.md

Phase 4: 프론트엔드 데이터 (오프라인)
  [11] build-grid-data.py → assets/data/*.json

유틸리티 (필요 시):
  cleanup-dictionary.py → 사전 파일 용량 정리
  redesign-dictionary.py → 사전 페이지 HTML 디자인 갱신
```

### 스크립트별 상세

#### [1] inventory-mssql.py

MSSQL 서버에 접속하여 전체 DB/테이블/컬럼 인벤토리를 추출한다.

- 입력: `.env` (DB 접속 정보)
- 출력: `raw/mssql-inventory.json`
- 동작: `DB1_*`, `DB2_*` 패턴의 DB를 탐색, `sys.dm_db_partition_stats`에서 행 수 추출
- 실행: `python scripts/inventory-mssql.py`

#### [2] inventory-excel.py

S2i에서 제공받은 Excel 파일을 파싱한다.

- 입력: `references/S2i_KBOP 백업 DB 테이블별 데이터 확인_260220.xlsx`, `references/S2i_KBOP DB 보유 국제대회 목록_260220.xlsx`
- 출력: `raw/excel-inventory.json`
- 동작: 3개 시트 파싱 (병합 셀 처리 포함), 백업DB vs S2i 비교 데이터 추출
- 실행: `python scripts/inventory-excel.py`

#### [3] column-diff.py

백업 DB와 S2i 간 컬럼 수 불일치 테이블을 분석한다.

- 입력: `raw/excel-inventory.json`, MSSQL 접속
- 출력: `raw/column-diff.json`
- 동작: 불일치 테이블의 실제 컬럼 목록을 가져와 diff 수행, +1 패턴 분석
- 실행: `python scripts/column-diff.py`

#### [4] extract-columns.py

각 테이블의 컬럼 메타데이터, 샘플 데이터, 코드값을 추출한다.

- 입력: `.env`, 내부 `TABLE_DB_MAP` (40개 테이블 → 대표 DB 매핑)
- 출력: `raw/column-metadata.json`
- 동작: 컬럼 정보(`INFORMATION_SCHEMA.COLUMNS`) + TOP 3 샘플 + 코드 컬럼 distinct 값
- 코드 컬럼 판별: 이름 suffix (`_SC`, `_CD`, `_ID` 등) 또는 타입/길이 기준
- 스키마 세대 판별: `G_ID`/`P_ID` 존재 → new, `GMKEY`/`PCODE` → legacy
- 실행: `python scripts/extract-columns.py`

#### [5] generate-dictionary.py

추출된 메타데이터로 Markdown 사전 파일을 초기 생성한다.

- 입력: `raw/column-metadata.json`
- 출력: `dictionary/game/*.md`, `dictionary/stats/*.md`, `dictionary/realtime/*.md`, `dictionary/master/*.md`, 각 도메인 `README.md`
- 동작: 140개 컬럼 설명 사전 + 4개 도메인 분류를 기반으로 테이블당 1파일 생성
- 실행: `python scripts/generate-dictionary.py`
- 주의: 기존 파일을 덮어쓴다. 이미 생성된 사전이 있으면 주의.

#### [6] upgrade-dictionary.py

사전 파일에 `표준명(안)` 컬럼을 추가한다.

- 입력: `dictionary/*.md` (기존 사전 파일)
- 출력: `dictionary/*.md` (갱신)
- 동작: 462개 항목의 STANDARD_MAP으로 현행 컬럼명 → 표준 컬럼명 매핑
- 실행: `python scripts/upgrade-dictionary.py`

#### [7] fill-descriptions.py

빈 설명 필드를 일괄 채운다.

- 입력: `dictionary/*.md`
- 출력: `dictionary/*.md` (갱신)
- 동작: 350개 컬럼 설명 사전 + 테이블별 오버라이드 + 이닝 패턴 자동 생성
- 옵션: `--dry-run` 으로 변경 없이 미리보기 가능
- 실행: `python scripts/fill-descriptions.py` 또는 `python scripts/fill-descriptions.py --dry-run`

#### [8] export-excel.py

사전 내용을 Excel 산출물로 변환한다.

- 입력: `dictionary/*.md`
- 출력: `exports/데이터사전.xlsx`
- 실행: `python scripts/export-excel.py`

#### [9] enrich-metadata.py

각 사전 파일에 운영 메타데이터(티어, 오너, 갱신주기, 소비자, 프로덕트, 접근수준, 관련표준)를 추가한다.

- 입력: `dictionary/*.md`, 내부 매핑 테이블
- 출력: `dictionary/*.md` (갱신)
- 동작: 39개 테이블 각각에 7개 필드 주입
- 실행: `python scripts/enrich-metadata.py`

#### [10] extract-mapping.py

사전 파일의 표준명 정보를 읽어 마이그레이션 매핑 문서를 생성한다.

- 입력: `dictionary/*.md`
- 출력: `migration/column-mapping.md`
- 동작: suffix 패턴으로 표준 타입 추론, 전환 규칙 분류 (직접매핑/이름변경/타입변환/인코딩변환 등)
- 실행: `python scripts/extract-mapping.py`

#### [11] build-grid-data.py

AG Grid에 사용할 JSON 데이터를 빌드한다.

- 입력: `dictionary/*.md`, `raw/mssql-inventory.json`, `glossary/business-terms.md`, `standards/code-dictionary.md`
- 출력: `assets/data/catalog-columns.json`, `catalog-instances.json`, `glossary-terms.json`, `domain-types.json`, `code-dictionary.json`, `dictionary-tables.json`
- 실행: `python scripts/build-grid-data.py`

---

## 일상 유지보수 작업

### 시즌 데이터 갱신

매 시즌 시작 시:

1. MSSQL에 새 시즌 데이터가 반영되었는지 확인
2. `python scripts/extract-columns.py` 실행 (raw 데이터 갱신)
3. `python scripts/generate-dictionary.py` — 새 테이블이 추가된 경우만
4. `python scripts/fill-descriptions.py` — 빈 설명 채움
5. `python scripts/enrich-metadata.py` — 메타데이터 갱신
6. `python scripts/build-grid-data.py` — AG Grid JSON 갱신
7. `./serve.sh` 로 로컬 확인
8. PR 생성 및 리뷰

### 사전 파일 내용 수정

컬럼 설명이나 메타데이터를 수정할 때:

1. `dictionary/<도메인>/<테이블>.md` 직접 편집
2. `python scripts/build-grid-data.py` 실행 (JSON 동기화)
3. 로컬 확인 후 PR

### 용어/코드/도메인 사전 수정

1. `glossary/business-terms.md` 또는 해당 원본 문서 편집
2. `python scripts/build-grid-data.py` 실행
3. PR

---

## 테이블 추가 절차

새 테이블을 데이터 사전에 추가하는 절차:

### 1. 테이블 분류

- 도메인 결정: game / stats / realtime / master
- 스키마 세대 확인: legacy (GMKEY/PCODE) / new (G_ID/P_ID)
- 티어 결정: Tier 1 (Critical) / Tier 2 (Standard) / Tier 3 (Reference)

### 2. 사전 파일 생성

`dictionary/<도메인>/<테이블명>.md` 파일을 생성한다.
기존 파일(예: `dictionary/game/GAMEINFO.md`)을 템플릿으로 복사하여 수정하는 것을 권장한다.

필수 섹션:
- 히어로 (테이블명, 도메인, 티어, 세대, 접근수준)
- 퀵 스탯 (행 수, 컬럼 수, 갱신주기, 오너)
- 정보 그리드 (대표 DB, PK, 소비자, 프로덕트 등)
- 컬럼 상세 테이블

### 3. 도메인 인덱스 갱신

`dictionary/<도메인>/README.md`에 새 테이블 행 추가.

### 4. mkdocs.yml 갱신

`mkdocs.yml`의 `nav` 섹션에 새 테이블 항목 추가.

### 5. 스크립트 매핑 갱신 (해당 시)

새 테이블의 메타데이터를 스크립트에 반영해야 하는 경우:

| 스크립트 | 수정 위치 |
|---------|----------|
| `extract-columns.py` | `TABLE_DB_MAP` 딕셔너리 |
| `generate-dictionary.py` | `DOMAINS` 딕셔너리 |
| `enrich-metadata.py` | `TIER`, `OWNER`, `REFRESH` 등 7개 매핑 |
| `upgrade-dictionary.py` | `STANDARD_MAP` (해당 컬럼의 표준명) |
| `fill-descriptions.py` | `COLUMN_DESC` 또는 `TABLE_OVERRIDES` |

### 6. 데이터 갱신

```bash
python scripts/build-grid-data.py   # AG Grid JSON
./serve.sh                          # 로컬 확인
```

### 7. PR 생성

변경된 파일 목록:
- `dictionary/<도메인>/<테이블>.md` (신규)
- `dictionary/<도메인>/README.md` (수정)
- `mkdocs.yml` (수정)
- `assets/data/*.json` (재생성)
- 해당 스크립트 (수정 시)

---

## 테이블 수정 절차

기존 테이블에 컬럼이 추가/삭제/변경된 경우:

1. `dictionary/<도메인>/<테이블>.md` 의 컬럼 테이블 수정
2. 표준명(안)이 필요하면 `scripts/upgrade-dictionary.py`의 `STANDARD_MAP`에 추가
3. 컬럼 설명이 필요하면 `scripts/fill-descriptions.py`의 `COLUMN_DESC`에 추가
4. `python scripts/build-grid-data.py` 실행
5. 관련 migration 문서 갱신 필요 여부 확인
6. PR

---

## AG Grid 데이터 갱신

`assets/data/` 하위 JSON 파일은 `build-grid-data.py`가 생성한다.
이 파일들을 수동 편집하지 않는다.

```bash
# 전체 재빌드
python scripts/build-grid-data.py
```

생성되는 파일:

| 파일 | 소스 | 행 수 |
|------|------|:-----:|
| `catalog-columns.json` | `dictionary/*.md` 파싱 | 787 |
| `catalog-instances.json` | `raw/mssql-inventory.json` + dictionary 메타 | 248 |
| `glossary-terms.json` | `glossary/business-terms.md` 파싱 | 134 |
| `domain-types.json` | `catalog-columns.json` 분석 | 93 |
| `code-dictionary.json` | `standards/code-dictionary.md` 파싱 | 168 |
| `dictionary-tables.json` | dictionary 요약 | 39 |

---

## MkDocs 설정 변경

### 네비게이션 추가

`mkdocs.yml`의 `nav` 섹션을 수정한다.
중첩 구조는 MkDocs의 네스트 네비게이션 문법을 따른다.

```yaml
nav:
  - 상위 메뉴:
    - 하위 항목: path/to/file.md
```

### CSS/JS 추가

`mkdocs.yml`의 `extra_css` 또는 `extra_javascript`에 경로를 추가한다.
파일은 `assets/css/` 또는 `assets/js/`에 배치한다.

### 심볼릭 링크 추가

새 최상위 디렉토리를 MkDocs에 포함하려면:
1. `serve.sh`에 `ln -sfn ../<디렉토리> docs/<디렉토리>` 추가
2. `.github/workflows/deploy-docs.yml`에도 동일하게 추가
3. `mkdocs.yml` nav에 해당 경로 추가

---

## 트러블슈팅

### MkDocs 서버가 파일을 못 찾는 경우

`docs/` 디렉토리의 심볼릭 링크가 깨졌을 수 있다.

```bash
rm -rf docs/
./serve.sh   # 심볼릭 링크 재생성
```

### AG Grid에 데이터가 안 나오는 경우

1. `assets/data/*.json` 파일이 존재하는지 확인
2. JSON 형식이 올바른지 확인 (`python -m json.tool assets/data/catalog-columns.json > /dev/null`)
3. 브라우저 개발자 도구 콘솔에서 fetch 오류 확인
4. `build-grid-data.py` 재실행

### 인증 게이트를 통과할 수 없는 경우

- 인증 형식: `아이디:비밀번호` (콜론으로 구분)
- `sessionStorage`를 수동으로 클리어하려면: 브라우저 개발자 도구 → Application → Session Storage → 삭제
- 인증 해시 변경: `assets/js/auth.js`의 `HASH` 상수를 수정

### Python 스크립트 DB 접속 실패

- `.env` 파일의 접속 정보 확인
- VPN 연결 확인 (내부망 필요)
- pymssql 설치 확인: `pip install pymssql`
- 방화벽에서 1433 포트가 열려 있는지 확인

### EUC-KR 인코딩 관련

사전 파일에서 한글이 깨져 보이는 컬럼(`GWEEK` 등):
- 이는 원천 DB에서 `varchar`(EUC-KR)에 한글을 저장한 레거시 문제
- 마이그레이션 시 `nvarchar`(UTF-8)로 전환 예정
- 해당 컬럼에는 `dict-encoding-warn` 경고가 표시됨

---

## 파일별 역할 요약

### 루트 파일

| 파일 | 역할 | 수정 빈도 |
|------|------|----------|
| `README.md` | 프로젝트 소개 (GitHub 표시용) | 프로젝트 변경 시 |
| `home.md` | MkDocs 홈 대시보드 | 통계 수치 변경 시 |
| `project-guide.md` | 수행사/운영팀 가이드 | 미결사항 해소 시 |
| `architecture.md` | 시스템 아키텍처 상세 | 구조 변경 시 |
| `development-guide.md` | 이 파일. 개발/운영 가이드 | 절차 변경 시 |
| `mkdocs.yml` | MkDocs 설정 | 페이지 추가/삭제 시 |
| `serve.sh` | 로컬 서버 실행 | 디렉토리 추가 시 |

### 자주 수정되는 파일

| 작업 | 수정 대상 |
|------|----------|
| 컬럼 설명 보완 | `dictionary/<도메인>/<테이블>.md` |
| 용어 추가 | `glossary/business-terms.md` |
| 테이블 추가 | `dictionary/`, `mkdocs.yml`, 관련 스크립트 |
| 거버넌스 정책 변경 | `governance/*.md` |
| AG Grid 데이터 동기화 | `python scripts/build-grid-data.py` 실행 |

### 수정하면 안 되는 파일

| 디렉토리/파일 | 이유 |
|-------------|------|
| `raw/*.json` | 스크립트가 생성하는 원본 데이터. 수동 수정 금지 |
| `references/*` | 원본 참고 자료. 수정 금지 |
| `assets/data/*.json` | `build-grid-data.py`가 생성. 직접 수정 금지 |
| `exports/데이터사전.xlsx` | `export-excel.py`가 생성. 직접 수정 금지 |
| `docs/` | gitignored. 심볼릭 링크로 자동 생성 |

---

관련 문서:
- [README.md](README.md) — 프로젝트 개요
- [architecture.md](architecture.md) — 시스템 아키텍처 상세
- [project-guide.md](project-guide.md) — 수행사/운영팀 읽기 가이드
