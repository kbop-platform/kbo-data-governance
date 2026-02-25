# GAME_HR

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 7,784 |
| 컬럼 수 | 15 |
| PK | `LE_ID, SR_ID, G_ID, SEQ_NO` |
| 스키마 세대 | new |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 미디어, 외부 API |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [ID 체계](../../standards/id-system.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `LE_ID` | smallint |  | NN | PK | 리그 ID (1=1군) | `league_id` |
| 2 | `SR_ID` | smallint |  | NN | PK | 시리즈 ID (0=정규시즌) | `series_id` |
| 3 | `SEASON_ID` | smallint |  | NN |  | 시즌 ID (연도) | `season_id` |
| 4 | `G_ID` | char | 13 | NN | PK | 경기 ID (YYYYMMDDVVHH# 형식) | `game_id` |
| 5 | `INN_NO` | tinyint |  | NN |  | 이닝 번호 | `inning_no` |
| 6 | `TB_SC` | char | 1 | NN |  | 팀 구분 코드 (T=원정, B=홈) | `top_bottom_sc` |
| 7 | `BAT_P_ID` | int |  | NN |  | 타자 선수 ID | `bat_player_id` |
| 8 | `PIT_P_ID` | int |  | NN |  | 투수 선수 ID | `pit_player_id` |
| 9 | `PLACE_SC` | char | 1 | NN |  | PLACE 상태코드 | `place_sc` |
| 10 | `HR_DISTANCE_VA` | smallint |  | NN |  | HR_DISTANCE 값 | `hr_distance_va` |
| 11 | `DIREC_SC` | varchar | 10 | NN |  | DIREC 상태코드 | `direc_sc` |
| 12 | `SCORE_CN` | tinyint |  | NN |  | SCORE 건수 | `score_cn` |
| 13 | `RECORD_DT` | varchar | 5 | NN |  | RECORD 일시 | `record_dt` |
| 14 | `SEQ_NO` | int |  | NN | PK | 순번 | `seq_no` |
| 15 | `REG_DT` | datetime |  | NN |  | 등록 일시 | `reg_dt` |

## 코드값 / 고유값


### `LE_ID`

| 값 | 건수 |
|-----|------|
| `1` | 7,784 |



### `SR_ID`

| 값 | 건수 |
|-----|------|
| `0` | 7,172 |
| `1` | 330 |
| `8` | 94 |
| `7` | 51 |
| `5` | 44 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `SEASON_ID`

| 값 | 건수 |
|-----|------|
| `2024` | 1,576 |
| `2020` | 1,422 |
| `2025` | 1,280 |
| `2021` | 1,233 |
| `2022` | 1,184 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `G_ID`

| 값 | 건수 |
|-----|------|
| `20220918OBSK0` | 9 |
| `20250720WOSS0` | 9 |
| `20210622LGSK0` | 8 |
| `20220706LTSK0` | 8 |
| `20200819HHSK0` | 8 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `INN_NO`

| 값 | 건수 |
|-----|------|
| `4` | 959 |
| `3` | 916 |
| `5` | 877 |
| `1` | 875 |
| `8` | 871 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `TB_SC`

| 값 | 건수 |
|-----|------|
| `B` | 3,892 |
| `T` | 3,892 |



### `BAT_P_ID`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PIT_P_ID`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PLACE_SC`

| 값 | 건수 |
|-----|------|
| `E` | 7,666 |
| `R` | 90 |
| `H` | 28 |



### `HR_DISTANCE_VA`

| 값 | 건수 |
|-----|------|
| `115` | 1,866 |
| `120` | 1,642 |
| `110` | 1,498 |
| `125` | 1,439 |
| `130` | 582 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `DIREC_SC`

| 값 | 건수 |
|-----|------|
| `7` | 3,311 |
| `9` | 2,331 |
| `78` | 810 |
| `8` | 720 |
| `89` | 612 |



### `SCORE_CN`

| 값 | 건수 |
|-----|------|
| `1` | 4,173 |
| `2` | 2,280 |
| `3` | 1,083 |
| `4` | 248 |



### `RECORD_DT`

| 값 | 건수 |
|-----|------|
| `19:36` | 48 |
| `19:20` | 47 |
| `19:30` | 46 |
| `18:34` | 45 |
| `18:33` | 45 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `LE_ID` | `1`, `1`, `1` |
| `SR_ID` | `0`, `0`, `0` |
| `SEASON_ID` | `2020`, `2020`, `2020` |
| `G_ID` | `20200505LTKT0`, `20200505LTKT0`, `20200505LTKT0` |
| `INN_NO` | `6`, `7`, `8` |
| `TB_SC` | `B`, `T`, `T` |
| `BAT_P_ID` | `68050`, `50506`, `78513` |
| `PIT_P_ID` | `50558`, `65062`, `77563` |
| `PLACE_SC` | `E`, `E`, `E` |
| `HR_DISTANCE_VA` | `115`, `105`, `110` |
