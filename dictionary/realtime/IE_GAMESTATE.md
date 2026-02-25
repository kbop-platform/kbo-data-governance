# IE_GAMESTATE

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 15,237 |
| 컬럼 수 | 5 |
| PK | `GAMEID, GYEAR` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | S2i 운영 (R-06) |
| 갱신 주기 | 실시간 (< 5초) |
| 소비자 | 방송팀, 앱 서비스 |
| 데이터 프로덕트 | [실시간 경기](../products/live-game.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GAMEID` | char | 13 | NN | PK | 경기 ID | `game_id` |
| 2 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `STATUS_ID` | tinyint |  | NN |  | 경기 상태 코드 | `status_id` |
| 4 | `INN_NO` | tinyint |  | NN |  | 이닝 번호 | `inning_no` |
| 5 | `TB_SC` | char | 1 | NN |  | 팀 구분 코드 (T=원정, B=홈) | `top_bottom_sc` |

## 코드값 / 고유값


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `STATUS_ID`

| 값 | 건수 |
|-----|------|
| `3` | 14,029 |
| `4` | 1,019 |
| `1` | 100 |
| `2` | 89 |



### `INN_NO`

→ 고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TB_SC`

| 값 | 건수 |
|-----|------|
| `B` | 7,873 |
| `T` | 7,364 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GAMEID` | `20040313HDHH0`, `20040313LGSS0`, `20040313LTSK0` |
| `GYEAR` | `2004`, `2004`, `2004` |
| `STATUS_ID` | `3`, `3`, `3` |
| `INN_NO` | `9`, `9`, `9` |
| `TB_SC` | `B`, `T`, `T` |
