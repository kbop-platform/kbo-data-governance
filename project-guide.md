# 프로젝트 가이드

프로젝트 구조, 빌드 방법, 수행사 참고사항을 정리한 문서입니다.

---

## 수행사 참고 (DAR-002~009)

신규 시스템 수행사가 본 정의서를 참조할 때 권장하는 읽기 순서:

| 순서 | 문서 | 핵심 내용 |
|:---:|------|----------|
| 1 | [명명 규칙](standards/naming-rules.md) | DB/API/Kafka/WS 4계층 명명 |
| 2 | [ID 체계](standards/id-system.md) | 식별자 6종, 복합 PK 표준 |
| 3 | [도메인 타입](standards/domain-types.md) | 타입 표준, NULL/인코딩 정책 |
| 4 | [코드 사전](standards/code-dictionary.md) | 코드값 전체 정의 |
| 5 | [데이터 사전](dictionary/index.md) | 필요한 테이블만 참조 |
| 6 | [업무 용어](glossary/business-terms.md) | 용어 불명확 시 참조 |

### 레거시 주의사항

현행 시스템을 참조하는 개발자를 위한 핵심 주의사항:

| 주의사항 | 설명 | 참조 |
|----------|------|------|
| **EUC-KR 깨짐** | `varchar`에 저장된 한글은 EUC-KR 인코딩 | [도메인 타입 §5](standards/domain-types.md#5) |
| **float 노이즈** | 타율 등 비율이 `float`로 저장 | [도메인 타입 §3.5](standards/domain-types.md#35-rate-_rt) |
| **합계행 혼재** | `PCODE='T'/'B'` 팀 합계행이 개인 기록과 혼재 | [ID 체계 §5](standards/id-system.md#5) |
| **9999 예약값** | `GYEAR=9999`는 통산 기록 (연도 아님) | [ID 체계 §5](standards/id-system.md#5) |
| **-1 센티널** | Score 이닝 점수에서 `-1`은 미진행 이닝 | [품질 규칙 §7](governance/quality-rules.md#7) |
| **ID 체계 혼재** | 구세대(`GMKEY`/`PCODE`) + 신세대(`G_ID`/`P_ID`) 공존 | [컬럼 차이](analysis/column-diff.md) |
| **팀코드 불변** | OB=두산, SK=SSG — 구단명 변경에도 코드 유지 | [ID 체계 §6](standards/id-system.md#6) |

---

## KBO 내부 운영팀 참고

| 순서 | 문서 | 핵심 내용 |
|:---:|------|----------|
| 1 | [데이터 오너십](governance/data-ownership.md) | 역할과 권한 |
| 2 | [품질 규칙](governance/quality-rules.md) | 품질 기준과 KPI |
| 3 | [변경 관리 절차](governance/change-process.md) | 코드/스키마 변경 절차 |
| 4 | [테이블 설계 가이드](governance/table-design-guide.md) | 자체 테이블 설계 시 |

---

## 프로젝트 구조

```
data-dict/
├── dictionary/              # 데이터 사전 — 39종 테이블 × 1파일
│   ├── game/                #   경기 기록 (12)
│   ├── stats/               #   통계 (10)
│   ├── realtime/            #   실시간 (9)
│   └── master/              #   마스터 (8)
├── standards/               # 표준 정의 — 5개 문서
├── glossary/                # 업무 용어 사전
├── governance/              # 거버넌스 정책 — 4개 문서
├── analysis/                # 현행 시스템 분석 — 7개 문서
├── raw/                     # 기계 추출 원본 데이터
├── references/              # 원본 참고 자료 (수정 금지)
├── exports/                 # Excel 산출물
├── scripts/                 # 데이터 파이프라인 (Python)
└── assets/                  # 이미지, CSS 등 정적 자원
```

---

## 스크립트 파이프라인

### 사전 조건

```bash
pip install -r scripts/requirements.txt   # pymssql, openpyxl
cp .env.example .env                       # DB 접속 정보 설정
```

### 실행 순서

파이프라인은 순차 의존성이 있으므로 번호 순서대로 실행한다.

| # | 스크립트 | 역할 | 출력 |
|---|---------|------|------|
| 1 | `inventory-mssql.py` | MSSQL 스키마 추출 | `raw/mssql-inventory.json` |
| 2 | `inventory-excel.py` | S2i Excel 파싱 | `raw/excel-inventory.json` |
| 3 | `column-diff.py` | 백업DB ↔ S2i 비교 | `raw/column-diff.json` |
| 4 | `extract-columns.py` | 컬럼 메타+샘플+코드값 | `raw/column-metadata.json` |
| 5 | `generate-dictionary.py` | Markdown 사전 생성 | `dictionary/` |
| 6 | `upgrade-dictionary.py` | 버전태그 + 표준명 추가 | `dictionary/` 갱신 |
| 7 | `fill-descriptions.py` | 빈 설명 일괄 채움 | `dictionary/` 갱신 |
| 8 | `export-excel.py` | Excel 산출물 생성 | `exports/데이터사전.xlsx` |

> 1~4는 MSSQL 접속 필요. 5~8은 `raw/*.json`만 참조하므로 오프라인 실행 가능.

---

## MkDocs 문서 사이트

전체 문서를 검색 가능한 HTML 사이트로 빌드한다.

```bash
git clone git@github.com:kbop-platform/kbo-data-governance.git
cd kbo-data-governance
pip install mkdocs-material
./serve.sh
```

`serve.sh`가 심볼릭 링크 생성 + 서버 실행을 자동으로 처리한다. 브라우저에서 `http://127.0.0.1:8000` 접속.

> `site/`와 `docs/`는 `.gitignore`에 포함.

---

## 미결 사항

### S2i 확인 필요

| # | 항목 | 영향 문서 | 우선순위 |
|---|------|----------|---------|
| 1 | +1 컬럼명 확인 (49개 테이블) | `dictionary/`, `analysis/column-diff.md` | 높음 |
| 2 | DEFEN +6컬럼, ENTRY -1컬럼 상세 | `dictionary/game/DEFEN.md`, `ENTRY.md` | 높음 |
| 3 | BH 코드 의미 (14,749건) | `standards/code-dictionary.md` §2.2 | 높음 |
| 4 | place_cd 문자코드 (R, A~I) | `standards/code-dictionary.md` §2.3 | 중간 |
| 5 | game_flag 4,7,8,9 의미 | `standards/code-dictionary.md` §8.3 | 중간 |
| 6 | series_id 1~9 의미 | `standards/code-dictionary.md` §10 | 중간 |

### 거버넌스 결정 보류

| # | 항목 | 위치 | 확인 대상 |
|---|------|------|----------|
| 1 | S2i 데이터 수신 SLA 수치 | `governance/data-ownership.md` §5.1 | S2i 계약서 |
| 2 | 기록위원회 검토 기한 | `governance/change-process.md` §3.2 | KBO 운영규정 |
| 3 | 감사 컬럼 소급 적용 범위 | `governance/table-design-guide.md` §5.1 | 마이그레이션 시 판단 |
| 4 | 세이버메트릭스 지표 우선순위 | `governance/table-design-guide.md` §7.1 | KBO 분석팀 |
| 5 | 구종 코드 확정 | `governance/table-design-guide.md` §8.3 | 기록위원회 |

---

## 기술 스택

| 구분 | 기술 |
|------|------|
| 원천 DB | Microsoft SQL Server (MSSQL) |
| 스크립트 | Python 3 (pymssql, openpyxl) |
| 문서 형식 | Markdown (GitHub Flavored) |
| 산출물 형식 | Excel (.xlsx) |
| 문서 사이트 | MkDocs Material |
