# KBO DataHub

KBO 데이터 자산의 표준, 사전, 품질, 거버넌스를 한 곳에서 관리하는 문서 포털.

39개 테이블 / 787개 컬럼 / 19개 데이터베이스 / 25.7M 행을 대상으로
AS-IS 현황 정리, 표준화 설계, 마이그레이션 매핑까지 포함한다.

---

## 목차

1. [프로젝트 배경과 목적](#프로젝트-배경과-목적)
2. [기술 스택](#기술-스택)
3. [시스템 아키텍처](#시스템-아키텍처)
4. [디렉토리 구조](#디렉토리-구조)
5. [로컬 개발 환경 구축](#로컬-개발-환경-구축)
6. [데이터 파이프라인](#데이터-파이프라인)
7. [문서 사이트 배포](#문서-사이트-배포)
8. [주요 문서 안내](#주요-문서-안내)
9. [데이터 도메인 요약](#데이터-도메인-요약)
10. [레거시 주의사항](#레거시-주의사항)
11. [미결 사항](#미결-사항)
12. [기여 규칙](#기여-규칙)

---

## 프로젝트 배경과 목적

KBO는 1982년부터 축적된 경기 기록 데이터를 MSSQL 기반으로 운영하고 있다.
현행 시스템은 레거시 명명(PascalCase, 약어 중심), EUC-KR 인코딩, float 정밀도 손실 등의 기술 부채를 안고 있으며,
신규 시스템 전환을 앞두고 **데이터 자산 전수 조사와 표준화**가 필요한 상황이다.

이 프로젝트의 목적:

- 현행 39개 테이블, 787개 컬럼의 **데이터 사전** 구축
- AS-IS → TO-BE **컬럼 매핑**(577건 이름 변경, 210건 타입 전환) 정의
- **명명 규칙, 도메인 타입, 코드 사전, ID 체계** 등 데이터 표준 수립
- **거버넌스 정책**(오너십, 품질 규칙, 변경 관리, 보안, DR) 문서화
- 위 모든 산출물을 검색 가능한 **MkDocs Material 사이트**로 배포

대상 독자:
- **수행사 개발자** — 신규 시스템 설계 시 현행 구조, 표준, 매핑 참조
- **KBO 운영팀** — 거버넌스 정책 수립과 데이터 품질 관리
- **데이터팀** — 일상적인 데이터 사전 조회 및 유지보수

---

## 기술 스택

| 구분 | 기술 | 용도 |
|------|------|------|
| 원천 DB | Microsoft SQL Server | 19개 DB, 252개 테이블 인스턴스 |
| 문서 사이트 | MkDocs Material (Python) | 정적 사이트 생성, 한국어 검색 |
| 인터랙티브 그리드 | AG Grid Community 32.x | Catalog, Dictionary 등 그리드 뷰 |
| 자동화 스크립트 | Python 3.12+ (pymssql, openpyxl) | DB 추출, 사전 생성, Excel 산출물 |
| 인증 | 클라이언트 SHA-256 해시 | 사이트 접근 제어 (서버 불필요) |
| CI/CD | GitHub Actions | main push 시 GitHub Pages 자동 배포 |
| 폰트 | Noto Sans KR / JetBrains Mono | 본문 / 코드 |

---

## 시스템 아키텍처

아키텍처 상세는 [architecture.md](architecture.md) 참조.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        데이터 소스                                   │
│  S2i (경기기록 벤더)    KMA (기상청)    KBO 자체 (운영/세이버)          │
└────────┬──────────────────┬──────────────────┬──────────────────────┘
         │                  │                  │
         v                  v                  v
┌─────────────────────────────────────────────────────────────────────┐
│                    MSSQL Server (49.50.172.83)                       │
│                                                                     │
│  DB1 (4개, 누적형)              DB2 (13개, 리그별 시즌형)              │
│  ├ DB1_BASEBALL_220328          ├ DB2_BASEBALL_220328                │
│  ├ DB1_BASEBALL_2_220328        ├ DB2_BASEBALL_NEW_220328            │
│  ├ DB1_MINOR_BASEBALL_220328    ├ DB2_POSTSEASON, DB2_ALLSTAR ...    │
│  └ DB1_MINOR_SO_BASEBALL        └ BROADCAST_BASEBALL, FALL_LEAGUE   │
└────────┬────────────────────────────────────────────────────────────┘
         │
         │  Python 스크립트 (13종)
         v
┌─────────────────────────────────────────────────────────────────────┐
│                    kbo-data-governance 저장소                         │
│                                                                     │
│  raw/*.json ─→ scripts/ ─→ dictionary/*.md + assets/data/*.json     │
│                              standards/*.md                          │
│                              governance/*.md                         │
│                              migration/*.md                          │
│                              standards-dict/*.md                     │
│                              catalog/*.md (AG Grid 페이지)            │
└────────┬────────────────────────────────────────────────────────────┘
         │
         │  MkDocs build + GitHub Actions
         v
┌─────────────────────────────────────────────────────────────────────┐
│                    GitHub Pages (정적 사이트)                         │
│  인증 게이트 → 홈 대시보드 → Catalog / Dictionary / Governance / ...   │
└─────────────────────────────────────────────────────────────────────┘
```

**핵심 구조**:
- **DB1** — 누적형 영구 DB. 1군/2군 정규시즌 데이터가 연도별로 쌓임
- **DB2** — 리그별 시즌 DB. 포스트시즌, 올스타, 시범경기, 국제대회 등 별도 DB로 분리
- 동일 테이블 구조(예: Hitter, GAMEINFO)가 최대 12개 DB에 인스턴스로 존재 → 총 248개 인스턴스
- 스키마 세대가 혼재: **구세대**(GMKEY/PCODE, PascalCase)와 **신세대**(G_ID/P_ID, suffix 규칙) 공존

---

## 디렉토리 구조

```
kbo-data-governance/
│
├── README.md                    ← 이 파일 (프로젝트 소개)
├── home.md                      ← MkDocs 홈 페이지 (사이트 대시보드)
├── project-guide.md             ← 수행사/운영팀 읽기 가이드
├── architecture.md              ← 시스템 아키텍처 상세
├── development-guide.md         ← 개발/운영 가이드 (파이프라인, 유지보수)
├── mkdocs.yml                   ← MkDocs 설정 (네비게이션, 플러그인, CSS/JS)
├── serve.sh                     ← 로컬 서버 실행 (심볼릭 링크 + mkdocs serve)
│
├── dictionary/                  # 데이터 사전 — 39개 테이블, 테이블당 1파일
│   ├── index.md                 #   사전 메인 페이지 (도메인별 요약, 통계)
│   ├── lineage.md               #   데이터 리니지 (시스템/테이블/컬럼 수준)
│   ├── products/                #   데이터 프로덕트 6종 정의
│   │   ├── game-summary.md      #     경기 요약 (8테이블, 216컬럼)
│   │   ├── live-game.md         #     실시간 경기
│   │   ├── player-profile.md    #     선수 프로필
│   │   ├── season-stats.md      #     시즌 통계
│   │   ├── schedule.md          #     일정 관리
│   │   └── master-codes.md      #     기준 데이터
│   ├── game/                    #   경기 기록 도메인 (12테이블)
│   │   ├── README.md            #     도메인 인덱스
│   │   ├── GAMEINFO.md          #     경기 정보 (27컬럼, 23,579행)
│   │   ├── Hitter.md            #     타자 기록
│   │   ├── Pitcher.md           #     투수 기록
│   │   └── ...                  #     외 8개
│   ├── stats/                   #   통계 도메인 (10테이블)
│   ├── realtime/                #   실시간 도메인 (9테이블, IE_* 접두사)
│   └── master/                  #   마스터 도메인 (8테이블)
│
├── catalog/                     # AG Grid 카탈로그 페이지
│   ├── instances.md             #   테이블 인스턴스 매트릭스 (248건)
│   └── columns.md               #   컬럼 검색 (787건)
│
├── standards-dict/              # 4대 사전 (AG Grid 기반)
│   ├── index.md                 #   사전 랜딩 페이지
│   ├── glossary.md              #   용어 사전 (134건)
│   ├── abbreviations.md         #   약어 사전
│   ├── domains.md               #   도메인 타입 사전 (93건)
│   └── codes.md                 #   코드 사전 (168건, 18그룹)
│
├── standards/                   # 데이터 표준 정의
│   ├── index.md                 #   표준/거버넌스 랜딩 페이지
│   ├── naming-rules.md          #   4계층 명명 규칙 (DB/API/Kafka/WS)
│   └── id-system.md             #   6종 식별자 체계 + 복합 PK 표준
│
├── governance/                  # 거버넌스 정책 6종
│   ├── data-ownership.md        #   6개 역할, RBAC 접근 권한 매트릭스
│   ├── quality-rules.md         #   품질 규칙, 5개 KPI, SLA
│   ├── change-process.md        #   변경 관리 절차 (C1~C3, S1~S4, D1~D3)
│   ├── table-design-guide.md    #   신규 테이블 설계 가이드 + DDL 예시
│   ├── data-security.md         #   3등급 보안 분류, PII 처리
│   └── disaster-recovery.md     #   백업 정책, RTO/RPO, DR 절차
│
├── migration/                   # 마이그레이션 산출물
│   ├── index.md                 #   마이그레이션 랜딩 페이지
│   ├── column-mapping.md        #   787컬럼 AS-IS→TO-BE 전수 매핑
│   ├── table-mapping.md         #   19DB, 252인스턴스 테이블 매핑
│   ├── design-decisions.md      #   타입 전환 설계 결정
│   └── column-diff.md           #   백업DB ↔ S2i 컬럼 차이 분석
│
├── glossary/
│   └── business-terms.md        # 업무 용어 원본 (134건, 7개 카테고리)
│
├── assets/                      # 정적 자원
│   ├── css/                     #   스타일시트 7종
│   │   ├── custom.css           #     전역 테마 (KBO 네이비 컬러, 다크모드)
│   │   ├── ag-grid-kbo.css      #     AG Grid 커스텀 테마 (ag-theme-kbo)
│   │   ├── home.css             #     홈 대시보드 레이아웃
│   │   ├── dict-detail.css      #     데이터 사전 상세 페이지
│   │   ├── product-detail.css   #     데이터 프로덕트 페이지
│   │   ├── section-landing.css  #     섹션 랜딩 페이지
│   │   └── side-panel.css       #     인스턴스 슬라이드 패널
│   ├── js/                      #   JavaScript 10종
│   │   ├── auth.js              #     SHA-256 인증 게이트
│   │   ├── home-dashboard.js    #     홈 대시보드 통계 렌더링
│   │   ├── ag-grid-common.js    #     AG Grid 공통 유틸리티
│   │   ├── ag-grid-catalog.js   #     컬럼 카탈로그 그리드
│   │   ├── ag-grid-instances.js #     인스턴스 매트릭스 그리드
│   │   ├── ag-grid-glossary.js  #     용어 사전 그리드
│   │   ├── ag-grid-domain.js    #     도메인 타입 그리드
│   │   ├── ag-grid-codes.js     #     코드 사전 그리드
│   │   ├── ag-grid-abbreviations.js # 약어 사전 그리드
│   │   └── datatables-init.js   #     DataTables 자동 초기화
│   ├── data/                    #   AG Grid 데이터 소스 (JSON, 빌드 생성물)
│   │   ├── catalog-columns.json #     787 컬럼 메타데이터
│   │   ├── catalog-instances.json#    248 인스턴스 메타데이터
│   │   ├── glossary-terms.json  #     134 용어
│   │   ├── domain-types.json    #     93 도메인 타입 분석
│   │   └── code-dictionary.json #     168 코드값
│   └── images/
│       └── kbo-logo.png         #   사이트 로고
│
├── scripts/                     # Python 자동화 스크립트 13종
│   ├── requirements.txt         #   의존성 (pymssql, openpyxl)
│   ├── inventory-mssql.py       #   [1] MSSQL 스키마 추출
│   ├── inventory-excel.py       #   [2] S2i Excel 파싱
│   ├── column-diff.py           #   [3] 백업DB ↔ S2i 비교
│   ├── extract-columns.py       #   [4] 컬럼 메타+샘플+코드값 추출
│   ├── generate-dictionary.py   #   [5] Markdown 사전 초기 생성
│   ├── upgrade-dictionary.py    #   [6] 표준명 + 버전태그 추가
│   ├── fill-descriptions.py     #   [7] 빈 설명 일괄 채움
│   ├── export-excel.py          #   [8] Excel 산출물 생성
│   ├── enrich-metadata.py       #   [9] 운영 메타데이터(티어/오너/주기) 추가
│   ├── extract-mapping.py       #   [10] 컬럼 매핑 생성
│   ├── build-grid-data.py       #   [11] AG Grid용 JSON 빌드
│   ├── cleanup-dictionary.py    #   유틸: 사전 파일 정리
│   └── redesign-dictionary.py   #   유틸: 사전 페이지 디자인 리뉴얼
│
├── raw/                         # 기계 추출 원본 (수정 금지)
│   ├── mssql-inventory.json     #   MSSQL 스키마 전체 인벤토리
│   ├── excel-inventory.json     #   S2i Excel 파싱 결과
│   ├── column-metadata.json     #   컬럼 상세 메타데이터
│   ├── column-diff.json         #   스키마 차이 분석 결과
│   └── db-schemas/              #   DB별 스키마 덤프 (19개 DB)
│       ├── _SCHEMA_SUMMARY.md   #     전체 요약
│       └── *.json / *.md        #     DB별 상세
│
├── references/                  # 원본 참고 자료 (수정 금지)
│   ├── KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf
│   ├── S2i_KBOP DB 보유 국제대회 목록_260220.xlsx
│   ├── S2i_KBOP 백업 DB 테이블별 데이터 확인_260220.xlsx
│   └── rfp_데이터요구사항.pdf
│
├── exports/
│   └── 데이터사전.xlsx           # Excel 산출물 (납품용)
│
├── .github/workflows/
│   └── deploy-docs.yml          # GitHub Pages 자동 배포
│
└── .gitignore
```

---

## 로컬 개발 환경 구축

### 사전 조건

- Python 3.12 이상
- Git

### 문서 사이트 실행

```bash
git clone git@github.com:kbop-platform/kbo-data-governance.git
cd kbo-data-governance

# MkDocs 설치
pip install mkdocs-material

# 로컬 서버 실행 (심볼릭 링크 자동 생성 + 서버 시작)
./serve.sh
```

브라우저에서 `http://127.0.0.1:8000` 접속.
`serve.sh`가 `docs/` 디렉토리에 심볼릭 링크를 생성하여 MkDocs가 각 디렉토리를 인식하도록 처리한다.

### 스크립트 실행 (DB 접속 필요 시)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt

# .env 파일 생성
cat > .env << 'EOF'
MSSQL_SERVER=49.50.172.83
MSSQL_PORT=1433
MSSQL_USER=<사용자>
MSSQL_PASSWORD=<비밀번호>
EOF
```

상세한 스크립트 실행 가이드는 [development-guide.md](development-guide.md) 참조.

---

## 데이터 파이프라인

13개 Python 스크립트가 순차 의존성을 가진 파이프라인을 구성한다.

```
[MSSQL] ──→ [1] inventory-mssql.py ──→ raw/mssql-inventory.json
[Excel] ──→ [2] inventory-excel.py ──→ raw/excel-inventory.json
              [3] column-diff.py ──→ raw/column-diff.json
[MSSQL] ──→ [4] extract-columns.py ──→ raw/column-metadata.json
                                          │
              [5] generate-dictionary.py ←─┘──→ dictionary/*.md (초기)
              [6] upgrade-dictionary.py ──→ dictionary/*.md (표준명 추가)
              [7] fill-descriptions.py ──→ dictionary/*.md (설명 추가)
              [8] export-excel.py ──→ exports/데이터사전.xlsx
              [9] enrich-metadata.py ──→ dictionary/*.md (티어/오너 추가)
              [10] extract-mapping.py ──→ migration/column-mapping.md
              [11] build-grid-data.py ──→ assets/data/*.json
```

- 1~4번은 **MSSQL 접속 필요** (VPN 또는 내부망)
- 5~11번은 `raw/*.json`과 `dictionary/*.md`만 참조하므로 **오프라인 실행 가능**
- 일반 유지보수 시에는 5~11번만 실행하면 된다

---

## 문서 사이트 배포

`main` 브랜치에 push하면 GitHub Actions가 자동으로 빌드 및 배포한다.

**배포 흐름**:
1. `.github/workflows/deploy-docs.yml` 트리거
2. `mkdocs build`로 정적 사이트 생성 (`site/`)
3. GitHub Pages에 업로드

수동 빌드:
```bash
./serve.sh  # 심볼릭 링크 생성 필요
python3 -m mkdocs build
# site/ 디렉토리에 결과물 생성
```

---

## 주요 문서 안내

### 신규 시스템 수행사 (권장 읽기 순서)

| 순서 | 문서 | 내용 |
|:---:|------|------|
| 1 | [데이터 프로덕트](dictionary/products/game-summary.md) | 비즈니스 단위별 데이터 구조 |
| 2 | [명명 규칙](standards/naming-rules.md) | DB/API/Kafka/WS 4계층 네이밍 |
| 3 | [ID 체계](standards/id-system.md) | 식별자 6종, 복합 PK 표준 |
| 4 | [도메인 사전](standards-dict/domains.md) | 11종 도메인 타입, 인코딩 정책 |
| 5 | [코드 사전](standards-dict/codes.md) | 코드값 전체 정의 |
| 6 | [컬럼 매핑](migration/column-mapping.md) | 787컬럼 AS-IS → TO-BE 매핑 |
| 7 | [데이터 사전](dictionary/index.md) | 필요한 테이블만 참조 |
| 8 | [용어 사전](standards-dict/glossary.md) | 용어 불명확 시 참조 |

### KBO 운영팀

| 순서 | 문서 | 내용 |
|:---:|------|------|
| 1 | [데이터 오너십](governance/data-ownership.md) | 역할, 권한, RBAC |
| 2 | [품질 규칙](governance/quality-rules.md) | 품질 기준, KPI, SLA |
| 3 | [변경 관리 절차](governance/change-process.md) | 코드/스키마 변경 프로세스 |
| 4 | [테이블 설계 가이드](governance/table-design-guide.md) | 신규 테이블 설계 시 참조 |
| 5 | [데이터 보안](governance/data-security.md) | 보안 등급, PII 처리 |
| 6 | [재해 복구](governance/disaster-recovery.md) | 백업, RTO/RPO |

### 개발자 유지보수

| 문서 | 내용 |
|------|------|
| [아키텍처 상세](architecture.md) | 시스템 구성, 프론트엔드 구조, 데이터 흐름 |
| [개발 가이드](development-guide.md) | 파이프라인 상세, 테이블 추가/수정 절차, 트러블슈팅 |
| [프로젝트 가이드](project-guide.md) | 수행사 참조용 전체 개요 |

---

## 데이터 도메인 요약

39개 테이블은 4개 도메인으로 분류되며, 3단계 티어로 중요도를 구분한다.

| 도메인 | 테이블 수 | 컬럼 수 | 주요 테이블 | 설명 |
|--------|:---------:|:-------:|------------|------|
| 경기 기록 (game) | 12 | 284 | GAMEINFO, Hitter, Pitcher, Score | 이닝별 경기 진행 데이터 |
| 통계 (stats) | 10 | 318 | BatTotal, PitTotal, SEASON_PLAYER_HITTER | 합산/시즌 집계 데이터 |
| 실시간 (realtime) | 9 | 96 | IE_LiveText, IE_BallCount, IE_GAMESTATE | 문자중계, 볼카운트 등 실시간 수신 |
| 마스터 (master) | 8 | 95 | person, TEAM, STADIUM, KBO_schedule | 선수/팀/구장/일정 기준 데이터 |

**티어 분류**:
- **Tier 1 (Critical)** — 12개. 경기 정보, 타자/투수 기록, 선수 등 핵심 테이블. 데이터 유실 시 서비스 장애.
- **Tier 2 (Standard)** — 17개. 시즌 통계, 수비 기록 등 일상 운영 테이블.
- **Tier 3 (Reference)** — 10개. 시스템 로그, 구장 정보 등 참조용 테이블.

---

## 레거시 주의사항

현행 시스템을 참조하는 개발자가 반드시 인지해야 할 사항.

| 항목 | 설명 | 상세 문서 |
|------|------|----------|
| EUC-KR 깨짐 | `varchar`에 저장된 한글은 EUC-KR 인코딩. nvarchar 전환 필요 | [도메인 사전](standards-dict/domains.md) |
| float 노이즈 | 타율 등 비율이 `float`로 저장되어 정밀도 손실 | [도메인 사전](standards-dict/domains.md) |
| 합계행 혼재 | `PCODE='T'/'B'`인 팀 합계행이 개인 기록과 같은 테이블에 존재 | [ID 체계](standards/id-system.md) |
| 9999 예약값 | `GYEAR=9999`는 연도가 아닌 통산 기록 | [ID 체계](standards/id-system.md) |
| -1 센티널 | Score 이닝 점수에서 `-1`은 미진행 이닝 | [품질 규칙](governance/quality-rules.md) |
| ID 체계 혼재 | 구세대(`GMKEY`/`PCODE`)와 신세대(`G_ID`/`P_ID`)가 공존 | [컬럼 차이](migration/column-diff.md) |
| 팀코드 불변 | OB=두산, SK=SSG. 구단명이 변경되어도 코드는 유지 | [ID 체계](standards/id-system.md) |

---

## 미결 사항

### S2i 확인 필요

| # | 항목 | 우선순위 |
|---|------|---------|
| 1 | +1 컬럼명 확인 (49개 테이블에서 S2i가 1개 컬럼 더 보유) | 높음 |
| 2 | DEFEN +6컬럼, ENTRY -1컬럼 상세 확인 | 높음 |
| 3 | BH 코드 의미 (14,749건 사용) | 높음 |
| 4 | place_cd 문자코드 (R, A~I) 의미 | 중간 |
| 5 | game_flag 4,7,8,9 의미 | 중간 |
| 6 | series_id 1~9 의미 | 중간 |

### 거버넌스 결정 보류

| # | 항목 | 확인 대상 |
|---|------|----------|
| 1 | S2i 데이터 수신 SLA 수치 | S2i 계약서 |
| 2 | 기록위원회 검토 기한 | KBO 운영규정 |
| 3 | 감사 컬럼 소급 적용 범위 | 마이그레이션 시 판단 |
| 4 | 세이버메트릭스 지표 우선순위 | KBO 분석팀 |
| 5 | 구종 코드 확정 | 기록위원회 |

---

## 기여 규칙

### 브랜치 전략

- `main` — 배포 브랜치. 직접 push 금지, PR 필수.
- `feature/*` — 기능 추가
- `fix/*` — 수정

### 커밋 메시지

```
<타입>: <간단 설명>

- 타입: feat, fix, docs, refactor, chore, data
- 예시: docs: GAMEINFO 컬럼 설명 보완
- 예시: data: column-metadata.json 2026시즌 갱신
```

### 데이터 사전 수정 시

1. `dictionary/` 하위 .md 파일 직접 수정
2. `build-grid-data.py` 실행하여 `assets/data/*.json` 갱신
3. 로컬에서 `./serve.sh`로 사이트 확인
4. PR 생성

상세 절차는 [development-guide.md](development-guide.md) 참조.

---

(c) 2026 KBOP Data Biz Team. Confidential.
