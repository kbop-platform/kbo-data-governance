# GAME_MEMO_PITCHCLOCK

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 237 |
| 컬럼 수 | 16 |
| PK | `LE_ID, SR_ID, G_ID, SEQ_NO` |
| 스키마 세대 | new |
| 데이터 티어 | Tier 3 — Reference |
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
| 3 | `SEASON_ID` | smallint |  | NN |  | 시즌 ID (연도) | `season_id` |
| 4 | `G_ID` | char | 13 | NN | PK | 경기 ID (YYYYMMDDVVHH# 형식) | `game_id` |
| 5 | `INN_NO` | tinyint |  | NN |  | 이닝 번호 | `inning_no` |
| 6 | `BAT_ORDER_NO` | tinyint |  | NN |  | BAT_ORDER 번호 | `bat_order_no` |
| 7 | `BAT_AROUND_NO` | tinyint |  | NN |  | BAT_AROUND 번호 | `bat_around_no` |
| 8 | `TB_SC` | char | 1 | NN |  | 팀 구분 코드 (T=원정, B=홈) | `top_bottom_sc` |
| 9 | `PA_PIT_NO` | smallint |  | NN |  | PA_PIT 번호 | `pa_pitch_no` |
| 10 | `GAME_PIT_NO` | smallint |  |  |  | GAME_PIT 번호 | `game_pitch_no` |
| 11 | `T_ID` | char | 2 |  |  | 팀 코드 (2자리) | `team_id` |
| 12 | `P_ID` | int |  |  |  | 선수 ID (정수) | `player_id` |
| 13 | `PIT_RESULT_SC` | varchar | 20 |  |  | PIT_RESULT 상태코드 | `pit_result_sc` |
| 14 | `ETC_ME` | varchar | 400 |  |  | ETC 메모 | `etc_memo` |
| 15 | `SEQ_NO` | int |  | NN | PK | 순번 | `seq_no` |
| 16 | `REG_DT` | datetime |  | NN |  | 등록 일시 | `reg_dt` |

## 코드값 / 고유값

> **EUC-KR 참고**: `PIT_RESULT_SC` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `LE_ID`

| 값 | 건수 |
|-----|------|
| `1` | 237 |



### `SR_ID`

| 값 | 건수 |
|-----|------|
| `0` | 215 |
| `1` | 17 |
| `8` | 3 |
| `5` | 1 |
| `3` | 1 |



### `SEASON_ID`

| 값 | 건수 |
|-----|------|
| `2025` | 237 |



### `G_ID`

| 값 | 건수 |
|-----|------|
| `20250328HTHH0` | 3 |
| `20250317LTWO0` | 2 |
| `20250310HHSK0` | 2 |
| `20250325LTSK0` | 2 |
| `20250323WOSS0` | 2 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `INN_NO`

| 값 | 건수 |
|-----|------|
| `7` | 37 |
| `3` | 29 |
| `8` | 29 |
| `1` | 27 |
| `5` | 26 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BAT_ORDER_NO`

| 값 | 건수 |
|-----|------|
| `3` | 39 |
| `6` | 34 |
| `1` | 30 |
| `7` | 29 |
| `5` | 23 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BAT_AROUND_NO`

| 값 | 건수 |
|-----|------|
| `0` | 237 |



### `TB_SC`

| 값 | 건수 |
|-----|------|
| `B` | 123 |
| `T` | 114 |



### `PA_PIT_NO`

| 값 | 건수 |
|-----|------|
| `1` | 177 |
| `4` | 23 |
| `3` | 15 |
| `5` | 10 |
| `2` | 4 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `GAME_PIT_NO`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `T_ID`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `P_ID`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `PIT_RESULT_SC`

| 값 | 건수 |
|-----|------|
| `C` | 170 |
| `P` | 66 |
| `Q` | 1 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `LE_ID` | `1`, `1`, `1` |
| `SR_ID` | `0`, `0`, `0` |
| `SEASON_ID` | `2025`, `2025`, `2025` |
| `G_ID` | `20250322HHKT0`, `20250323WOSS0`, `20250323WOSS0` |
| `INN_NO` | `3`, `1`, `7` |
| `BAT_ORDER_NO` | `6`, `1`, `8` |
| `BAT_AROUND_NO` | `0`, `0`, `0` |
| `TB_SC` | `B`, `B`, `B` |
| `PA_PIT_NO` | `1`, `3`, `4` |
| `GAME_PIT_NO` | `109`, `22`, `266` |
