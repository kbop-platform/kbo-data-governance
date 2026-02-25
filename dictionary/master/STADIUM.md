# STADIUM

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 487 |
| 컬럼 수 | 3 |
| PK | `gyear, stadium` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 3 — Reference |
| 데이터 오너 | 데이터 관리자 (R-01) |
| 갱신 주기 | 연 1회 (시즌 전) |
| 소비자 | 전 시스템 |
| 데이터 프로덕트 | [기준 데이터](../products/master-codes.md) |
| 접근 수준 | Public |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `gyear` | char | 4 | NN | PK | 연도 | `season_yr` |
| 2 | `stadium` | varchar | 10 | NN | PK | 구장 코드 | `stadium_nm` |
| 3 | `stadium_key` | char | 2 | NN |  | 구장 코드 | `stadium_id` |

## 코드값 / 고유값


### `gyear`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `stadium`

| 값 | 건수 |
|-----|------|
| `Àá½Ç` | 45 |
| `ÇÑ¹ç` | 43 |
| `»çÁ÷` | 41 |
| `Ã»ÁÖ` | 39 |
| `½Ã¹Î` | 34 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `stadium_key`

| 값 | 건수 |
|-----|------|
| `JS` | 45 |
| `DJ` | 43 |
| `SJ` | 41 |
| `CJ` | 39 |
| `DG` | 34 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gyear` | `1982`, `1982`, `1982` |
| `stadium` | `±¸´ö`, `µ¿´ë¹®`, `¸¶»ê` |
| `stadium_key` | `KD`, `DM`, `MS` |
