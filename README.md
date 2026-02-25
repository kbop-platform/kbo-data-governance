# 데이터 카탈로그

KBO 신규 시스템(RFP DAR-001) 구축을 위한 데이터 카탈로그입니다. 표준, 코드 체계, 거버넌스, 마이그레이션 정책을 포함합니다.

---

## 현황

| 데이터베이스 | 테이블 | 컬럼 | 총 행 수 | 스키마 세대 |
|:---:|:---:|:---:|:---:|:---:|
| 17개 | 39종 | 787개 | 25.7M | 구세대 + 신세대 공존 |

---

## 문서 구성

| 영역 | 설명 | 바로가기 |
|------|------|---------|
| **데이터 프로덕트** | 6개 비즈니스 단위 (경기 요약, 실시간, 선수, 시즌 통계, 일정, 기준) | [경기 요약](dictionary/products/game-summary.md) |
| **데이터 사전** | 39종 테이블, 787개 컬럼 상세. 리니지·티어·오너 포함 | [테이블 조감도](dictionary/index.md) |
| **표준 정의** | 명명 규칙(4계층), ID 체계(6종), 코드 사전, 도메인 타입(12종), 약어 사전 | [명명 규칙](standards/naming-rules.md) |
| **용어 사전** | ~165개 업무 용어, 7개 도메인 | [업무 용어](glossary/business-terms.md) |
| **거버넌스** | 오너십, 품질 규칙, 변경 절차, 설계 가이드, 보안, 재해 복구 | [데이터 오너십](governance/data-ownership.md) |
| **마이그레이션** | 컬럼 매핑, 설계 결정, 테이블 매핑 | [컬럼 매핑](migration/column-mapping.md) |

---

## 빠른 참조

### 4계층 명명 규칙

| 계층 | 컨벤션 | 예시 |
|------|--------|------|
| **DB** | `lower_snake_case` | `game_id`, `avg_rt` |
| **API** | camelCase | `gameId`, `avgRt` |
| **Kafka** | `dot.separated` | `kbo.game.play` |
| **WebSocket** | camelCase | `gameId` |

### 6종 핵심 ID

| ID | 형식 | 예시 |
|----|------|------|
| `game_id` | char(13) | `20250322HHKT0` |
| `player_id` | int | `75847` |
| `team_id` | char(2) | `HH` |
| `stadium_id` | char(2) | `JS` |
| `season_id` | smallint | `2025` |
| `series_id` | smallint | `0` (정규) |

### 12종 도메인 타입

| 접미사 | 용도 | MSSQL 타입 |
|--------|------|-----------|
| `_id` | 식별자 | char / int |
| `_nm` | 이름 | nvarchar |
| `_cd` / `_sc` | 코드 / 상태 | varchar / char |
| `_cn` | 수량 | int |
| `_rt` | 비율 | decimal(8,5) |
| `_dt` | 날짜 | char(8) / datetime2 |
| `_tm` | 시각 | char(4) / int |
| `_if` | 불리언 | bit |
| `_va` | 측정값 | int / decimal |
| `_no` | 순번 | int |

---

## 관련 문서

- [프로젝트 가이드](project-guide.md) — 프로젝트 구조, 스크립트 파이프라인, 수행사 참고, 레거시 주의사항
- Excel 산출물: `exports/데이터사전.xlsx` (9시트)
