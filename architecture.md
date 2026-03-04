# 시스템 아키텍처

이 문서는 KBO DataHub의 전체 시스템 구성, 데이터 흐름, 프론트엔드 구조를 상세히 기술한다.
프로젝트 개요는 [README.md](README.md) 참조.

---

## 목차

1. [전체 시스템 구성](#전체-시스템-구성)
2. [데이터베이스 아키텍처](#데이터베이스-아키텍처)
3. [스키마 세대 구분](#스키마-세대-구분)
4. [데이터 흐름](#데이터-흐름)
5. [프론트엔드 아키텍처](#프론트엔드-아키텍처)
6. [인증 구조](#인증-구조)
7. [빌드 및 배포 구조](#빌드-및-배포-구조)
8. [데이터 프로덕트 구조](#데이터-프로덕트-구조)
9. [티어 및 오너십 체계](#티어-및-오너십-체계)

---

## 전체 시스템 구성

```
                      ┌──────────────────┐
                      │   데이터 소스     │
                      ├──────────────────┤
                      │ S2i (경기기록)    │
                      │ KMA (기상청)      │
                      │ KBO 자체 (OPS)    │
                      └────────┬─────────┘
                               │
                               v
┌──────────────────────────────────────────────────────┐
│              MSSQL Server (49.50.172.83:1433)         │
│                                                      │
│  ┌─────────────┐  ┌──────────────────────────────┐   │
│  │ DB1 (4개)    │  │ DB2 (13개)                    │   │
│  │ 누적형       │  │ 리그별 시즌형                  │   │
│  │ 정규시즌     │  │ 포스트/올스타/시범/국제/마이너  │   │
│  └─────────────┘  └──────────────────────────────┘   │
│  ┌───────────────────────────────────────────────┐   │
│  │ 기타: BROADCAST_BASEBALL, FALL_LEAGUE_BASEBALL │   │
│  └───────────────────────────────────────────────┘   │
└──────────────────────────┬───────────────────────────┘
                           │
                           │ Python 스크립트 (pymssql)
                           v
┌──────────────────────────────────────────────────────┐
│                kbo-data-governance 저장소              │
│                                                      │
│  raw/*.json (추출 원본)                                │
│       │                                               │
│       v                                               │
│  scripts/*.py (13종 파이프라인)                         │
│       │                                               │
│       ├──→ dictionary/*.md (39개 테이블 사전)           │
│       ├──→ migration/*.md (매핑 산출물)                 │
│       ├──→ assets/data/*.json (AG Grid 데이터)         │
│       └──→ exports/데이터사전.xlsx                      │
│                                                      │
│  + standards/ standards-dict/ governance/ catalog/     │
│    glossary/ (수동 작성 문서)                           │
└──────────────────────────┬───────────────────────────┘
                           │
                           │ MkDocs Material + GitHub Actions
                           v
┌──────────────────────────────────────────────────────┐
│                GitHub Pages (정적 사이트)               │
│                                                      │
│  auth.js 인증 게이트                                   │
│       │                                               │
│       v                                               │
│  ┌─────────┐  ┌───────────┐  ┌───────────┐          │
│  │ Catalog  │  │ Dictionary │  │ Governance│          │
│  │ (AG Grid)│  │ (AG Grid)  │  │           │          │
│  └─────────┘  └───────────┘  └───────────┘          │
└──────────────────────────────────────────────────────┘
```

---

## 데이터베이스 아키텍처

### DB 분류 체계

MSSQL 서버에 19개 데이터베이스가 존재하며, 크게 2가지 유형으로 나뉜다.

**DB1 (누적형, 4개)**

| DB명 | 대상 | 비고 |
|------|------|------|
| DB1_BASEBALL_220328 | 1군 정규시즌 | 13테이블, 5.2M행 |
| DB1_BASEBALL_2_220328 | 1군 정규시즌 (확장) | 4테이블, 695K행. 신세대 스키마 |
| DB1_MINOR_BASEBALL_220328 | 2군 정규시즌 | 9테이블, 1.7M행 |
| DB1_MINOR_SO_BASEBALL | 소셜 야구 | 9테이블, 26K행 |

- 연도별 데이터가 같은 DB에 누적됨 (`GYEAR` 컬럼으로 구분)
- 행 수가 많고 서비스 운영에 직접 사용

**DB2 (리그별 시즌형, 13개)**

| DB명 | 대상 |
|------|------|
| DB2_BASEBALL_220328 | 1군 시즌 (구세대) |
| DB2_BASEBALL_2_220328 | 1군 시즌 (확장) |
| DB2_BASEBALL_NEW_220328 | 1군 시즌 (신세대) |
| DB2_POSTSEASON | 포스트시즌 |
| DB2_ALLSTAR | 올스타전 |
| DB2_EXHIBITION | 시범경기 |
| DB2_INTERNATIONAL | 국제대회 |
| DB2_OTHER_GAME | 기타 경기 |
| DB2_MINOR_* (4개) | 마이너 리그 변형 |
| BROADCAST_BASEBALL | 방송 데이터 |
| FALL_LEAGUE_BASEBALL | 가을야구 |

- 동일 테이블 구조가 리그별로 복제됨
- 예: `Hitter` 테이블이 12개 DB에 존재 → 12개 인스턴스

### 인스턴스 분포

전체 252개 테이블 인스턴스 중 39개 고유 테이블 구조(테이블 타입)가 존재한다.
같은 테이블 타입이 여러 DB에 걸쳐 반복되는 구조이며,
DB마다 컬럼 수가 미세하게 다른 경우가 있다(특히 신세대 DB에서 컬럼 추가).

---

## 스키마 세대 구분

현행 시스템에는 두 세대의 스키마가 공존한다.

| 구분 | 구세대 (legacy) | 신세대 (new) |
|------|----------------|-------------|
| PK 식별자 | GMKEY (char 15), PCODE (varchar) | G_ID (char 13), P_ID (int) |
| 명명 스타일 | PascalCase, 약어 중심 (HRA, KK, HP) | lower_snake_case + suffix (_id, _cd, _nm) |
| 도입 시기 | 1982년~ | 2020년대~ |
| 대표 테이블 | GAMEINFO, Hitter, Pitcher, BatTotal | SEASON_PLAYER_HITTER, SEASON_PLAYER_PITCHER |
| 해당 DB | DB1_BASEBALL, DB2_BASEBALL 등 | DB1_BASEBALL_2, DB2_BASEBALL_NEW 등 |

`realtime/` 도메인의 IE_* 테이블은 스키마 세대가 명확하지 않아 `unknown`으로 분류한다.

표준화 방향:
- 모든 컬럼을 `lower_snake_case` + 도메인 suffix 규칙으로 통일
- GMKEY → game_id, PCODE → player_id (varchar → int 타입 변환 포함)
- 전체 매핑은 [migration/column-mapping.md](migration/column-mapping.md) 참조

---

## 데이터 흐름

### 시스템 수준

```
S2i (벤더)
  │
  ├──→ DB2 (리그별 원본 수신)
  │       │
  │       └──→ DB1 (누적 집계)
  │
  └──→ 실시간 중계 데이터 (IE_* 테이블)

KMA (기상청) ──→ GAMEINFO_WEATHER (DB2 경유)

KBO 자체
  ├──→ OPS (운영통합관리) 테이블
  └──→ 세이버메트릭스 지표 (향후)
```

### 데이터 생명주기

```
DRAFT (경기 중) → REVIEW (경기 종료 후 기록원 검토) → CONFIRMED (익일 17:00 확정)
    → REVISED (시즌 중 수정 발생 시) → ARCHIVED (시즌 종료 후)
```

### 갱신 주기별 테이블

| 주기 | 테이블 수 | 예시 |
|------|:---------:|------|
| 실시간 | 9 | IE_LiveText, IE_BallCount, IE_GAMESTATE |
| 경기당일 | 12 | GAMEINFO, Hitter, Pitcher, Score |
| D+1 | 5 | BatTotal, PitTotal, TeamRank |
| 시즌 | 4 | SEASON_PLAYER_HITTER, SEASON_PLAYER_PITCHER |
| 연 1회 | 9 | person, TEAM, STADIUM, KBO_schedule |

---

## 프론트엔드 아키텍처

### 기술 구성

MkDocs Material이 정적 사이트를 생성하고, AG Grid가 인터랙티브 기능을 담당한다.

```
MkDocs Material (정적 사이트 생성기)
│
├── Markdown → HTML 변환
│     dictionary/*.md → 테이블 사전 페이지
│     standards/*.md → 표준 문서 페이지
│     governance/*.md → 거버넌스 문서 페이지
│     migration/*.md → 마이그레이션 페이지
│
├── AG Grid Community (인터랙티브 그리드)
│     catalog/instances.md ← ag-grid-instances.js ← catalog-instances.json
│     catalog/columns.md ← ag-grid-catalog.js ← catalog-columns.json
│     standards-dict/glossary.md ← ag-grid-glossary.js ← glossary-terms.json
│     standards-dict/domains.md ← ag-grid-domain.js ← domain-types.json
│     standards-dict/codes.md ← ag-grid-codes.js ← code-dictionary.json
│     standards-dict/abbreviations.md ← ag-grid-abbreviations.js
│
└── home-dashboard.js
      홈 대시보드 통계 카드 동적 렌더링
```

### AG Grid 공통 패턴

AG Grid 뷰들은 `ag-grid-common.js`에 정의된 공통 유틸리티를 사용하며 동일한 패턴을 따른다:

1. JSON 데이터 fetch (`assets/data/*.json`)
2. 통계 카드 렌더링 (상단 수치 요약)
3. 캐스케이딩 드롭다운 필터 (선택하면 다른 필터 옵션이 연동)
4. 텍스트 검색 (debounce 적용)
5. 필터 칩 표시 (활성 필터를 태그로 표현)
6. CSV 내보내기
7. 반응형 컬럼 숨김 (좁은 화면)

**인스턴스 뷰의 사이드 패널**: 테이블 행을 클릭하면 520px 슬라이드 패널이 열리며,
해당 테이블의 메타데이터(DB, 티어, 오너, PK 등)와 컬럼 목록을 표시한다.

### CSS 구조

| 파일 | 역할 |
|------|------|
| `custom.css` | 전역 테마. KBO 네이비(#1B2A5B) 기반, 다크모드 포함 |
| `ag-grid-kbo.css` | AG Grid 커스텀 테마 `ag-theme-kbo`. 뱃지, 필터, 카드 스타일 |
| `home.css` | 홈 대시보드 히어로 + 카드 그리드 |
| `section-landing.css` | 섹션 랜딩 페이지 (Dictionary, Governance, Migration 등) |
| `dict-detail.css` | 데이터 사전 개별 테이블 페이지 |
| `product-detail.css` | 데이터 프로덕트 + 리니지 페이지 |
| `side-panel.css` | 인스턴스 뷰 슬라이드 패널 |

모든 CSS 파일이 다크모드(`[data-md-color-scheme="slate"]`)를 지원한다.

### 페이지 유형별 HTML 구조

**사전 상세 페이지** (`dict-detail-page` 클래스):
- 히어로 섹션: 테이블명, 도메인/티어/세대/접근수준 뱃지
- 퀵 스탯: 행 수, 컬럼 수, 갱신 주기, 오너
- 정보 그리드: 대표 DB, PK, 소비자, 프로덕트, 관련 표준
- 컬럼 테이블: ordinal, 현행명, 타입, 길이, PK/NN, 설명, 표준명(안)
- 코드값: `<details>` 접이식, 분포 건수 포함
- 샘플 데이터: 상위 3행

**데이터 프로덕트 페이지** (`product-page` 클래스):
- 히어로 + 퀵 스탯
- 포함 테이블 목록 (역할 설명 포함)
- JOIN 관계 (ASCII 트리 다이어그램)
- 소비자 그리드
- 품질 SLA 카드
- 데이터 흐름 Mermaid 다이어그램

---

## 인증 구조

클라이언트 사이드 인증 게이트를 사용한다. 서버 없이 동작.

- `auth.js`가 페이지 로드 시 `document.documentElement`를 숨김
- 사용자가 `아이디:비밀번호` 형식으로 입력
- SHA-256 해시 비교 후 `sessionStorage`에 인증 토큰 저장
- 인증 성공 시 페이지 표시 + MkDocs 헤더에 로그아웃 버튼 추가
- 탭/브라우저를 닫으면 세션 만료

이 방식은 정적 사이트의 간이 접근 제어 용도이며, 보안이 중요한 경우
서버 사이드 인증이나 GitHub 프라이빗 저장소 접근 제어로 대체해야 한다.

---

## 빌드 및 배포 구조

### MkDocs 심볼릭 링크 구조

MkDocs는 `docs/` 디렉토리를 소스로 사용하지만,
이 프로젝트에서는 콘텐츠를 루트에 배치하고 `serve.sh`가 심볼릭 링크를 생성한다.

```
docs/ (gitignored, 빌드 시 생성)
├── index.md → ../home.md
├── project-guide.md → ../project-guide.md
├── architecture.md → ../architecture.md
├── development-guide.md → ../development-guide.md
├── dictionary/ → ../dictionary/
├── catalog/ → ../catalog/
├── standards/ → ../standards/
├── standards-dict/ → ../standards-dict/
├── governance/ → ../governance/
├── migration/ → ../migration/
├── glossary/ → ../glossary/
└── assets/ → ../assets/
```

이 구조를 사용하는 이유:
- 루트에서 직접 Markdown 파일을 편집 가능
- GitHub에서 Markdown 미리보기가 바로 동작
- `docs/` 디렉토리 충돌 없이 MkDocs 빌드 가능

### GitHub Actions 배포

`.github/workflows/deploy-docs.yml`이 `main` push 시 자동 실행:
1. Python + mkdocs-material 설치
2. 심볼릭 링크 생성 (serve.sh와 동일)
3. `mkdocs build` → `site/` 생성
4. GitHub Pages에 업로드

---

## 데이터 프로덕트 구조

6개 데이터 프로덕트가 비즈니스 단위로 테이블을 그룹핑한다.

| 프로덕트 | 테이블 수 | 컬럼 수 | 갱신 주기 | 주요 소비자 |
|----------|:---------:|:-------:|----------|-----------|
| 경기 요약 (Game Summary) | 8 | 216 | 경기당일 | 방송팀, 기록팀, 외부 API |
| 실시간 경기 (Live Game) | 9 | 96 | 실시간 | 중계 시스템, 앱 |
| 선수 프로필 (Player Profile) | 4 | 43 | 연 1회 | 기록팀, 외부 API |
| 시즌 통계 (Season Stats) | 6 | 274 | D+1~시즌 | 통계분석팀, 외부 API |
| 일정 관리 (Schedule) | 2 | 22 | 시즌 | 운영팀, 외부 API |
| 기준 데이터 (Master Codes) | 3 | 21 | 연 1회 | 전체 시스템 |

각 프로덕트 문서는 `dictionary/products/` 에 위치하며,
포함 테이블, JOIN 관계, 소비자, 품질 SLA를 정의한다.

---

## 티어 및 오너십 체계

### 데이터 티어

| 티어 | 테이블 수 | 기준 | 예시 |
|------|:---------:|------|------|
| Tier 1 (Critical) | 12 | 서비스 핵심. 유실 시 장애 | GAMEINFO, Hitter, Pitcher, person |
| Tier 2 (Standard) | 17 | 일상 운영. 지연 시 영향 | BatTotal, DEFEN, SEASON_PLAYER_* |
| Tier 3 (Reference) | 10 | 참조용. 지연 허용 | IE_log, STADIUM, CANCEL_GAME |

### 역할 (RBAC)

| 역할 ID | 역할 | 주요 책임 |
|---------|------|----------|
| R-01 | S2i (벤더) | 경기 데이터 수집, DB2 적재 |
| R-02 | KBO 기록위원회 | 데이터 검증, 확정 |
| R-03 | KBO 운영팀 | 일정/구장/팀 마스터 관리 |
| R-04 | 통계분석팀 | 시즌 통계, 세이버메트릭스 |
| R-05 | 외부 수행사 | 시스템 개발, 읽기 전용 |
| R-06 | 데이터팀 | 표준 관리, 품질 모니터링 |

상세 권한 매트릭스는 [governance/data-ownership.md](governance/data-ownership.md) 참조.

---

관련 문서:
- [README.md](README.md) — 프로젝트 개요
- [development-guide.md](development-guide.md) — 개발 및 운영 가이드
- [project-guide.md](project-guide.md) — 수행사/운영팀 읽기 가이드
