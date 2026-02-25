# GAMECONTAPP

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 2,531,702 |
| 컬럼 수 | 29 |
| PK | `GMKEY, GYEAR, SERNO` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 기록팀, 분석팀 |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GMKEY` | char | 13 | NN | PK | 경기 고유키 (YYYYMMDDVVHH#, 13자리) | `game_id` |
| 2 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `GDAY` | char | 8 | NN |  | 경기 일자 (YYYYMMDD) | `game_dt` |
| 4 | `SERNO` | smallint |  | NN | PK | 일련번호 | `seq_no` |
| 5 | `TURN` | char | 2 | NN |  | 타순 | `turn_no` |
| 6 | `INN` | tinyint |  | NN |  | 이닝 번호 | `ip` |
| 7 | `TB` | char | 1 | NN |  | 팀 구분 (T=원정/Top, B=홈/Bottom) | `top_bottom_cd` |
| 8 | `INN2` | char | 1 |  |  | 이닝 세부 (아웃수 환산 또는 연장 구분) | `inn_2_score` |
| 9 | `OCOUNT` | char | 1 |  |  | 아웃 카운트 (0,1,2,4=이닝종료) | `opp_count` |
| 10 | `BCOUNT` | varchar | 30 |  |  | 투구 시퀀스 상세 (S/B/T/F/H 등) | `ball_count_cd` |
| 11 | `RTURN` | char | 2 |  |  | 실제 타순 (교체 포함) | `real_turn_no` |
| 12 | `HOW` | char | 2 |  |  | 플레이 결과 코드 (H1=안타, HR=홈런, KK=삼진 등 49종) | `how_cd` |
| 13 | `FIELD` | varchar | 25 |  |  | 수비 배치 코드 | `field_cd` |
| 14 | `PLACE` | char | 1 |  |  | 타구 방향 (0~9=포지션번호, S=삼진 등) | `place_cd` |
| 15 | `HITTER` | varchar | 10 |  |  | 타자 선수 코드 | `hitter_nm` |
| 16 | `HITNAME` | varchar | 20 |  |  | 타자 이름 (EUC-KR) | `hitter_nm` |
| 17 | `PITNAME` | varchar | 20 |  |  | 투수 이름 (EUC-KR) | `pitcher_nm` |
| 18 | `PITCHER` | varchar | 10 |  |  | 투수 선수 코드 | `pitcher_nm` |
| 19 | `CATNAME` | varchar | 20 |  |  | 포수 이름 (EUC-KR) | `catcher_nm` |
| 20 | `CATCHER` | varchar | 10 |  |  | 포수 선수 코드 | `catcher_id` |
| 21 | `BCNT` | char | 3 |  |  | 볼카운트 (S-B 형식) | `ball_count_cd` |
| 22 | `TSCORE` | smallint |  |  |  | 원정팀 누적 득점 | `total_score` |
| 23 | `BSCORE` | smallint |  |  |  | 홈팀 누적 득점 | `bat_score` |
| 24 | `BASE1B` | char | 2 |  |  | 1루 주자 타순 (플레이 전) | `base_1b_before_id` |
| 25 | `BASE2B` | char | 2 |  |  | 2루 주자 타순 (플레이 전) | `base_2b_before_id` |
| 26 | `BASE3B` | char | 2 |  |  | 3루 주자 타순 (플레이 전) | `base_3b_before_id` |
| 27 | `BASE1A` | char | 2 |  |  | 1루 주자 타순 (플레이 후) | `base_1b_after_id` |
| 28 | `BASE2A` | char | 2 |  |  | 2루 주자 타순 (플레이 후) | `base_2b_after_id` |
| 29 | `BASE3A` | char | 2 |  |  | 3루 주자 타순 (플레이 후) | `base_3b_after_id` |

## 코드값 / 고유값


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `GDAY`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SERNO`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TURN`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `INN`

→ 고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TB`

| 값 | 건수 |
|-----|------|
| `T` | 1,287,178 |
| `B` | 1,244,524 |



### `INN2`

| 값 | 건수 |
|-----|------|
| `` | 2,521,429 |
| `2` | 10,269 |
| `3` | 4 |



### `OCOUNT`

| 값 | 건수 |
|-----|------|
| `1` | 873,921 |
| `2` | 873,911 |
| `0` | 745,166 |
| `4` | 38,704 |



### `RTURN`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HOW`

| 값 | 건수 |
|-----|------|
| `BH` | 484,156 |
| `GR` | 414,454 |
| `FL` | 342,069 |
| `KK` | 269,138 |
| `H1` | 268,791 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `PLACE`

| 값 | 건수 |
|-----|------|
| `A` | 566,292 |
| `1` | 420,424 |
| `2` | 419,622 |
| `3` | 418,858 |
| `B` | 316,534 |

> 외 10건 — 전체 목록은 `raw/column-metadata.json` 참조



### `HITTER`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `PITCHER`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `CATCHER`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `BCNT`

| 값 | 건수 |
|-----|------|
| `0-0` | 341,395 |
| `2-2` | 320,514 |
| `2-1` | 318,415 |
| `2-3` | 314,463 |
| `1-1` | 241,431 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `TSCORE`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BSCORE`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BASE1B`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BASE2B`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BASE3B`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BASE1A`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BASE2A`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BASE3A`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `19820327SSLG0`, `19820327SSLG0`, `19820327SSLG0` |
| `GYEAR` | `1982`, `1982`, `1982` |
| `GDAY` | `20250325`, `20250325`, `20250325` |
| `SERNO` | `10`, `20`, `30` |
| `TURN` | `14`, `14`, `16` |
| `INN` | `4`, `4`, `5` |
| `TB` | `B`, `B`, `T` |
| `INN2` | ``, ``, `` |
| `OCOUNT` | `1`, `2`, `0` |
| `BCOUNT` | `SBT`, `BH`, `BBBTFT` |
