# 개발 및 운영 가이드

KBO DataHub의 유지보수 절차를 기술한다.
스크립트 파이프라인 개요는 [project-guide.md](project-guide.md)의 "스크립트 파이프라인" 섹션 참조.

---

## 개발 환경 설정

```bash
git clone git@github.com:kbop-platform/kbo-data-governance.git
cd kbo-data-governance

python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs-material
pip install -r scripts/requirements.txt

# DB 접속이 필요한 경우
cat > .env << 'EOF'
MSSQL_SERVER=49.50.172.83
MSSQL_PORT=1433
MSSQL_USER=<사용자>
MSSQL_PASSWORD=<비밀번호>
EOF

bash serve.sh
# http://127.0.0.1:8000
```

---

## 일상 유지보수

### 사전 파일 내용 수정

1. `dictionary/<도메인>/<테이블>.md` 직접 편집
2. `python scripts/build-grid-data.py` 실행 (JSON 동기화)
3. 로컬 `bash serve.sh`로 확인 → PR

### 용어/코드 사전 수정

1. `glossary/business-terms.md` 또는 해당 원본 편집
2. `python scripts/build-grid-data.py` 실행
3. PR

### 시즌 데이터 갱신

1. `python scripts/extract-columns.py` (DB 접속 필요)
2. `python scripts/fill-descriptions.py`
3. `python scripts/enrich-metadata.py`
4. `python scripts/build-grid-data.py`
5. 로컬 확인 → PR

---

## 테이블 추가 절차

### 1. 분류 결정

- 도메인: game / stats / realtime / master
- 스키마 세대: legacy (GMKEY/PCODE) / new (G_ID/P_ID)
- 티어: Tier 1 / 2 / 3

### 2. 파일 생성

`dictionary/<도메인>/<테이블명>.md` 생성.
기존 파일(예: `dictionary/game/GAMEINFO.md`)을 복사해서 수정하는 것을 권장.

### 3. 인덱스 및 설정 갱신

- `dictionary/<도메인>/README.md`에 테이블 행 추가
- `mkdocs.yml`의 `nav`에 항목 추가

### 4. 스크립트 매핑 갱신 (해당 시)

| 스크립트 | 수정 위치 |
|---------|----------|
| `extract-columns.py` | `TABLE_DB_MAP` |
| `generate-dictionary.py` | `DOMAINS` |
| `enrich-metadata.py` | `TIER`, `OWNER`, `REFRESH` 등 7개 매핑 |
| `upgrade-dictionary.py` | `STANDARD_MAP` |
| `fill-descriptions.py` | `COLUMN_DESC` 또는 `TABLE_OVERRIDES` |

### 5. 데이터 갱신 및 확인

```bash
python scripts/build-grid-data.py
bash serve.sh
```

---

## 테이블 수정 절차

기존 테이블에 컬럼 추가/삭제/변경 시:

1. `dictionary/<도메인>/<테이블>.md` 컬럼 테이블 수정
2. 표준명 필요 시 `upgrade-dictionary.py`의 `STANDARD_MAP`에 추가
3. 설명 필요 시 `fill-descriptions.py`의 `COLUMN_DESC`에 추가
4. `python scripts/build-grid-data.py`
5. migration 문서 갱신 필요 여부 확인
6. PR

---

## AG Grid 데이터

`assets/data/` 하위 JSON은 **수동 편집 금지**. `build-grid-data.py`가 생성한다.

```bash
python scripts/build-grid-data.py
```

| 파일 | 소스 | 건수 |
|------|------|:----:|
| `catalog-columns.json` | `dictionary/*.md` 파싱 | 787 |
| `catalog-instances.json` | `raw/mssql-inventory.json` + dictionary 메타 | 248 |
| `glossary-terms.json` | `glossary/business-terms.md` 파싱 | 134 |
| `domain-types.json` | catalog-columns.json 분석 | 93 |
| `code-dictionary.json` | `standards/code-dictionary.md` 파싱 | 168 |

---

## MkDocs 변경

### 새 디렉토리 추가

1. `serve.sh`에 `ln -sfn ../<디렉토리> docs/<디렉토리>` 추가
2. `.github/workflows/deploy-docs.yml`에도 동일 추가
3. `mkdocs.yml` nav에 경로 추가

### CSS/JS 추가

`mkdocs.yml`의 `extra_css` 또는 `extra_javascript`에 경로 추가.
파일은 `assets/css/` 또는 `assets/js/`에 배치.

---

## 트러블슈팅

### MkDocs 서버가 파일을 못 찾음

심볼릭 링크가 깨진 경우.

```bash
rm -rf docs/
bash serve.sh
```

### AG Grid에 데이터가 안 나옴

1. `assets/data/*.json` 존재 여부 확인
2. `python -m json.tool assets/data/catalog-columns.json > /dev/null` (JSON 유효성)
3. 브라우저 콘솔에서 fetch 오류 확인
4. `build-grid-data.py` 재실행

### DB 접속 실패

- `.env` 접속 정보 확인
- VPN 연결 확인 (내부망)
- `pip install pymssql` 확인
- 1433 포트 방화벽 확인

### 인증 통과 불가

- 입력 형식: `아이디:비밀번호` (콜론 구분)
- 브라우저 Session Storage 클리어
- 해시 변경: `assets/js/auth.js`의 `HASH` 상수

---

## 수정 금지 파일

| 경로 | 이유 |
|------|------|
| `raw/*.json` | 스크립트 생성물 |
| `references/*` | 원본 참고 자료 |
| `assets/data/*.json` | `build-grid-data.py` 생성물 |
| `exports/데이터사전.xlsx` | `export-excel.py` 생성물 |
| `docs/` | gitignored, 심볼릭 링크 자동 생성 |
