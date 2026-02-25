# IE_ScoreRHEB

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 30,860 |
| 컬럼 수 | 7 |
| PK | `gameID, GYEAR, bHome` |
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
| 1 | `gameID` | char | 13 | NN | PK | 경기 ID (GMKEY와 동일 형식) | `game_id` |
| 2 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `Run` | tinyint |  | NN |  | 득점 | `run` |
| 4 | `Hit` | tinyint |  | NN |  | 안타 | `hit` |
| 5 | `Error` | tinyint |  | NN |  | 실책 | `err` |
| 6 | `BallFour` | tinyint |  | NN |  | 볼넷 여부 | `ball_four_if` |
| 7 | `bHome` | tinyint |  | NN | PK | 홈팀 여부 | `home_if` |

## 코드값 / 고유값


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Run`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Hit`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Error`

| 값 | 건수 |
|-----|------|
| `0` | 15,978 |
| `1` | 10,087 |
| `2` | 3,584 |
| `3` | 939 |
| `4` | 225 |

> 외 3건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BallFour`

→ 고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `bHome`

| 값 | 건수 |
|-----|------|
| `1` | 15,430 |
| `0` | 15,430 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gameID` | `20040313HDHH0`, `20040313HDHH0`, `20040313LGSS0` |
| `GYEAR` | `2004`, `2004`, `2004` |
| `Run` | `6`, `4`, `7` |
| `Hit` | `10`, `6`, `13` |
| `Error` | `0`, `2`, `0` |
| `BallFour` | `10`, `4`, `5` |
| `bHome` | `0`, `1`, `0` |
