# GAME_MEMO

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 54,544 |
| 컬럼 수 | 20 |
| PK | `LE_ID, SR_ID, G_ID, INN_NO, BAT_ORDER_NO, BAT_AROUND_NO, TB_SC, PA_PIT_NO, ORDER_NO` |
| 스키마 세대 | new |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 기록팀 |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `LE_ID` | smallint |  | NN | PK | 리그 ID (1=1군) | `league_id` |
| 2 | `SR_ID` | smallint |  | NN | PK | 시리즈 ID (0=정규시즌) | `series_id` |
| 3 | `SEASON_ID` | smallint |  |  |  | 시즌 ID (연도) | `season_id` |
| 4 | `G_ID` | char | 13 | NN | PK | 경기 ID (YYYYMMDDVVHH# 형식) | `game_id` |
| 5 | `INN_NO` | tinyint |  | NN | PK | 이닝 번호 | `inning_no` |
| 6 | `BAT_ORDER_NO` | tinyint |  | NN | PK | BAT_ORDER 번호 | `bat_order_no` |
| 7 | `BAT_AROUND_NO` | tinyint |  | NN | PK | BAT_AROUND 번호 | `bat_around_no` |
| 8 | `TB_SC` | char | 1 | NN | PK | 팀 구분 코드 (T=원정, B=홈) | `top_bottom_sc` |
| 9 | `PA_PIT_NO` | smallint |  | NN | PK | PA_PIT 번호 | `pa_pitch_no` |
| 10 | `GAME_PIT_NO` | smallint |  |  |  | GAME_PIT 번호 | `game_pitch_no` |
| 11 | `P_ID` | int |  |  |  | 선수 ID (정수) | `player_id` |
| 12 | `REQ_T_ID` | char | 2 |  |  | 요청 팀 코드 | `req_team_id` |
| 13 | `START_TM` | varchar | 5 |  |  | START 시각 | `start_tm` |
| 14 | `END_TM` | varchar | 5 |  |  | END 시각 | `end_tm` |
| 15 | `USE_TM` | varchar | 5 |  |  | USE 시각 | `use_tm` |
| 16 | `FIRST_IF` | varchar | 20 |  |  | 첫 여부 플래그 | `first_if` |
| 17 | `LAST_IF` | varchar | 20 |  |  | 마지막 여부 플래그 | `last_if` |
| 18 | `ETC_ME` | varchar | 400 |  |  | ETC 메모 | `etc_memo` |
| 19 | `ORDER_NO` | int |  | NN | PK | ORDER 번호 | `order_no` |
| 20 | `REG_DT` | datetime |  | NN |  | 등록 일시 | `reg_dt` |

## 코드값 / 고유값


### `LE_ID`

| 값 | 건수 |
|-----|------|
| `1` | 54,544 |



### `SR_ID`

| 값 | 건수 |
|-----|------|
| `0` | 51,456 |
| `1` | 1,486 |
| `7` | 439 |
| `5` | 353 |
| `6` | 327 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `SEASON_ID`

| 값 | 건수 |
|-----|------|
| `2025` | 23,978 |
| `2024` | 13,364 |
| `2023` | 4,719 |
| `2022` | 4,377 |
| `2020` | 4,054 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `G_ID`

| 값 | 건수 |
|-----|------|
| `20250827HTSK0` | 69 |
| `20250730OBHT0` | 67 |
| `20250815HTOB0` | 66 |
| `20250703NCHH0` | 66 |
| `20250709OBLT0` | 65 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `INN_NO`

| 값 | 건수 |
|-----|------|
| `7` | 6,546 |
| `5` | 6,481 |
| `8` | 6,453 |
| `6` | 6,398 |
| `3` | 6,300 |

> 외 8건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BAT_ORDER_NO`

| 값 | 건수 |
|-----|------|
| `3` | 7,095 |
| `2` | 6,918 |
| `4` | 6,797 |
| `1` | 6,533 |
| `5` | 5,929 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BAT_AROUND_NO`

| 값 | 건수 |
|-----|------|
| `0` | 54,384 |
| `1` | 158 |
| `3` | 2 |



### `TB_SC`

| 값 | 건수 |
|-----|------|
| `B` | 27,295 |
| `T` | 27,249 |



### `PA_PIT_NO`

| 값 | 건수 |
|-----|------|
| `0` | 25,987 |
| `1` | 8,387 |
| `2` | 6,556 |
| `3` | 4,939 |
| `4` | 3,755 |

> 외 9건 — 전체 목록은 `raw/column-metadata.json` 참조



### `GAME_PIT_NO`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `P_ID`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `REQ_T_ID`

| 값 | 건수 |
|-----|------|
| `` | 48,830 |
| `LT` | 603 |
| `SK` | 600 |
| `HT` | 598 |
| `SS` | 590 |

> 외 9건 — 전체 목록은 `raw/column-metadata.json` 참조



### `START_TM`

| 값 | 건수 |
|-----|------|
| `00:00` | 48,363 |
| `18:30` | 59 |
| `18:34` | 38 |
| `19:15` | 36 |
| `19:22` | 36 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `END_TM`

| 값 | 건수 |
|-----|------|
| `00:00` | 48,473 |
| `19:16` | 35 |
| `18:35` | 34 |
| `20:09` | 33 |
| `19:27` | 33 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `USE_TM`

| 값 | 건수 |
|-----|------|
| `00:00` | 50,830 |
| `00:01` | 2,398 |
| `00:02` | 763 |
| `00:03` | 290 |
| `00:04` | 18 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `FIRST_IF`

| 값 | 건수 |
|-----|------|
| `4` | 10,683 |
| `` | 9,693 |
| `Æ÷¼ö` | 8,867 |
| `ÄÚÄª½ºÅÂÇÁ` | 8,672 |
| `C` | 4,623 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `LAST_IF`

| 값 | 건수 |
|-----|------|
| `` | 47,528 |
| `¾Æ¿ô` | 2,392 |
| `¼¼ÀÌÇÁ` | 2,081 |
| `1,2·ç°£` | 711 |
| `ÆÄ¿ï` | 366 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `LE_ID` | `1`, `1`, `1` |
| `SR_ID` | `0`, `0`, `0` |
| `SEASON_ID` | `2020`, `2020`, `2020` |
| `G_ID` | `20200505HHSK0`, `20200505HHSK0`, `20200505LTKT0` |
| `INN_NO` | `7`, `9`, `1` |
| `BAT_ORDER_NO` | `5`, `3`, `1` |
| `BAT_AROUND_NO` | `0`, `0`, `0` |
| `TB_SC` | `B`, `B`, `T` |
| `PA_PIT_NO` | `0`, `0`, `0` |
| `GAME_PIT_NO` | `170`, `213`, `0` |
