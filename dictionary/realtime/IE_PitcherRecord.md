# IE_PitcherRecord

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 134,388 |
| 컬럼 수 | 22 |
| PK | `gameID, GYEAR, PlayerID` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | S2i 운영 (R-06) |
| 갱신 주기 | 실시간 (< 5초) |
| 소비자 | 방송팀 |
| 데이터 프로덕트 | [실시간 경기](../products/live-game.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `gameID` | char | 13 | NN | PK | 경기 ID (GMKEY와 동일 형식) | `game_id` |
| 2 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `PlayerName` | varchar | 15 | NN |  | 선수명 (EUC-KR) | `player_nm` |
| 4 | `PlayerID` | varchar | 10 | NN | PK | 선수 코드 | `player_id` |
| 5 | `SeqNO` | tinyint |  | NN |  | 순번 | `seq_no` |
| 6 | `Inning` | varchar | 5 | NN |  | 이닝 | `inning_no` |
| 7 | `PA` | tinyint |  | NN |  | 타석 (Plate Appearance) | `pa` |
| 8 | `PitchBallCnt` | tinyint |  | NN |  | 볼 투구 수 | `pitch_ball_cn` |
| 9 | `PitchStrikeCnt` | tinyint |  | NN |  | 스트라이크 투구 수 | `pitch_strike_cn` |
| 10 | `OAB` | tinyint |  | NN |  | 상대 타수 | `opp_ab` |
| 11 | `Run` | tinyint |  | NN |  | 득점 | `run` |
| 12 | `Hit` | tinyint |  | NN |  | 안타 | `hit` |
| 13 | `HR` | tinyint |  | NN |  | 홈런 | `hr` |
| 14 | `SH` | tinyint |  | NN |  | 희생번트 | `sh` |
| 15 | `SF` | tinyint |  | NN |  | 희생플라이 | `sf` |
| 16 | `BB` | tinyint |  | NN |  | 볼넷 | `bb` |
| 17 | `HBP` | tinyint |  | NN |  | 사구 (Hit by Pitch) | `hbp` |
| 18 | `SO` | tinyint |  | NN |  | 삼진 | `so` |
| 19 | `BK` | tinyint |  | NN |  | 보크 | `bk` |
| 20 | `WP` | tinyint |  | NN |  | 폭투 | `wp` |
| 21 | `ER` | tinyint |  | NN |  | 자책점 | `er` |
| 22 | `bHome` | tinyint |  | NN |  | 홈팀 여부 | `home_if` |

## 코드값 / 고유값


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PlayerID`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `SeqNO`

| 값 | 건수 |
|-----|------|
| `1` | 30,718 |
| `2` | 29,501 |
| `3` | 27,774 |
| `4` | 22,354 |
| `5` | 13,968 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `Inning`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PA`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PitchBallCnt`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PitchStrikeCnt`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `OAB`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Run`

→ 고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Hit`

→ 고유값 19종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HR`

| 값 | 건수 |
|-----|------|
| `0` | 113,070 |
| `1` | 17,681 |
| `2` | 3,065 |
| `3` | 492 |
| `4` | 71 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `SH`

| 값 | 건수 |
|-----|------|
| `0` | 121,355 |
| `1` | 11,686 |
| `2` | 1,204 |
| `3` | 131 |
| `4` | 12 |



### `SF`

| 값 | 건수 |
|-----|------|
| `0` | 125,452 |
| `1` | 8,516 |
| `2` | 393 |
| `3` | 26 |
| `4` | 1 |



### `BB`

| 값 | 건수 |
|-----|------|
| `0` | 71,472 |
| `1` | 36,458 |
| `2` | 15,289 |
| `3` | 6,688 |
| `4` | 2,921 |

> 외 5건 — 전체 목록은 `raw/column-metadata.json` 참조



### `HBP`

| 값 | 건수 |
|-----|------|
| `0` | 119,672 |
| `1` | 13,069 |
| `2` | 1,489 |
| `3` | 145 |
| `4` | 13 |



### `SO`

→ 고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BK`

| 값 | 건수 |
|-----|------|
| `0` | 133,517 |
| `1` | 857 |
| `2` | 14 |



### `WP`

| 값 | 건수 |
|-----|------|
| `0` | 122,628 |
| `1` | 10,595 |
| `2` | 1,056 |
| `3` | 93 |
| `4` | 15 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `ER`

→ 고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `bHome`

| 값 | 건수 |
|-----|------|
| `1` | 68,683 |
| `0` | 65,705 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gameID` | `20040309LTSS0`, `20040309LTSS0`, `20040309LTSS0` |
| `GYEAR` | `2004`, `2004`, `2004` |
| `PlayerName` | `°­¹Î¿µ`, `°­¿µ½Ä`, `°¡µæ¿°` |
| `PlayerID` | `70531`, `70615`, `92501` |
| `SeqNO` | `3`, `1`, `1` |
| `Inning` | `1.0`, `5.0`, `0.2` |
| `PA` | `3`, `22`, `5` |
| `PitchBallCnt` | `0`, `9`, `3` |
| `PitchStrikeCnt` | `6`, `37`, `9` |
| `OAB` | `3`, `20`, `4` |
