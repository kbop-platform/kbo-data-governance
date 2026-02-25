# CANCEL_GAME

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 1,290 |
| 컬럼 수 | 6 |
| PK | `LE_ID, SR_ID, G_ID` |
| 스키마 세대 | new |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 경기운영팀 (R-05) |
| 갱신 주기 | 발생 즉시 |
| 소비자 | 운영팀, 방송팀 |
| 데이터 프로덕트 | [일정 관리](../products/schedule.md) |
| 접근 수준 | Public |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `LE_ID` | smallint |  | NN | PK | 리그 ID (1=1군) | `league_id` |
| 2 | `SR_ID` | smallint |  | NN | PK | 시리즈 ID (0=정규시즌) | `series_id` |
| 3 | `SEASON_ID` | smallint |  | NN |  | 시즌 ID (연도) | `season_id` |
| 4 | `G_ID` | char | 13 | NN | PK | 경기 ID (YYYYMMDDVVHH# 형식) | `game_id` |
| 5 | `CANCEL_SC_NM` | varchar | 20 |  |  | CANCEL_SC 명칭 | `cancel_sc_nm` |
| 6 | `REG_DT` | datetime |  | NN |  | 등록 일시 | `reg_dt` |

## 코드값 / 고유값


### `LE_ID`

| 값 | 건수 |
|-----|------|
| `1` | 1,290 |



### `SR_ID`

| 값 | 건수 |
|-----|------|
| `0` | 1,120 |
| `1` | 157 |
| `5` | 4 |
| `3` | 4 |
| `7` | 3 |

> 외 2건 — 전체 목록은 `raw/column-metadata.json` 참조



### `SEASON_ID`

→ 고유값 16종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `G_ID`

| 값 | 건수 |
|-----|------|
| `20100427SSLG0` | 1 |
| `20100421SKOB0` | 1 |
| `20100421LGWO0` | 1 |
| `20100418LGHT0` | 1 |
| `20100414OBHT0` | 1 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `LE_ID` | `1`, `1`, `1` |
| `SR_ID` | `0`, `0`, `0` |
| `SEASON_ID` | `2010`, `2010`, `2010` |
| `G_ID` | `20100331LTHH0`, `20100331OBWO0`, `20100331SKLG0` |
| `CANCEL_SC_NM` | `¿ìÃµÃë¼Ò`, `¿ìÃµÃë¼Ò`, `¿ìÃµÃë¼Ò` |
| `REG_DT` | `2025-09-01 14:04:52.060000`, `2025-09-01 14:04:52.060000`, `2025-09-01 14:04:52.060000` |
