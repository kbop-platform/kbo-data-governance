# TeamRank

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 373 |
| 컬럼 수 | 30 |
| PK | `GYEAR, SEC, TEAM` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 통계분석팀 (R-04) |
| 갱신 주기 | D+1 (전일 경기 반영) |
| 소비자 | 미디어, 외부 API |
| 데이터 프로덕트 | [시즌 통계](../products/season-stats.md) |
| 접근 수준 | Internal |
| 관련 표준 | [ID 체계](../../standards/id-system.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GYEAR` | nvarchar | 4 | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 2 | `SEC` | varchar | 4 | NN | PK | 구간 (시즌연도 또는 "9999"=통산) | `series_cd` |
| 3 | `RANK` | int |  |  |  | 순위 | `rank_no` |
| 4 | `LEAGUE` | char | 5 |  |  | 리그 | `league_cd` |
| 5 | `TEAM` | nvarchar | 6 | NN | PK | 팀 코드 (2자리, HH=키움, HT=KIA 등) | `team_cd` |
| 6 | `GAME` | int |  |  |  | 경기 수 | `game_cn` |
| 7 | `WIN` | int |  |  |  | 승 | `win` |
| 8 | `LOSE` | int |  |  |  | 패 | `loss` |
| 9 | `SAME` | int |  |  |  | 무승부 | `same_rank_if` |
| 10 | `WRA` | real |  |  |  | 승률 | `wrc` |
| 11 | `AB` | int |  |  |  | 타수 (At Bat) | `ab` |
| 12 | `HIT` | int |  |  |  | 안타 | `hit` |
| 13 | `HR` | int |  |  |  | 홈런 | `hr` |
| 14 | `SB` | int |  |  |  | 도루 | `sb` |
| 15 | `RUN` | int |  |  |  | 득점 | `run` |
| 16 | `INN` | varchar | 10 |  |  | 이닝 번호 | `ip` |
| 17 | `INN2` | int |  |  |  | 이닝 세부 (아웃수 환산 또는 연장 구분) | `inn_2_score` |
| 18 | `R` | int |  |  |  | 실점 | `runs_cn` |
| 19 | `ER` | int |  |  |  | 자책점 | `er` |
| 20 | `ERR` | int |  |  |  | 실책 | `err` |
| 21 | `HRA` | varchar | 50 |  |  | 타율 | `avg` |
| 22 | `LRA` | varchar | 50 |  |  | 좌타자 대 타율 | `left_avg` |
| 23 | `BRA` | varchar | 50 |  |  | 대타율 (Batting Avg Against) | `bat_avg` |
| 24 | `ERA` | varchar | 50 |  |  | 평균자책점 | `era` |
| 25 | `continue` | varchar | 50 |  |  | 연속 기록 | `continue_if` |
| 26 | `H2` | int |  |  |  | 2루타 | `h2b` |
| 27 | `H3` | int |  |  |  | 3루타 | `h3b` |
| 28 | `BB` | int |  |  |  | 볼넷 | `bb` |
| 29 | `HP` | int |  |  |  | 사구 (Hit by Pitch) | `hbp` |
| 30 | `SF` | int |  |  |  | 희생플라이 | `sf` |

## 코드값 / 고유값


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SEC`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `LEAGUE`

| 값 | 건수 |
|-----|------|
| `` | 154 |
| `magic` | 8 |
| `dream` | 8 |
| `0` | 8 |



### `TEAM`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `INN`

| 값 | 건수 |
|-----|------|
| `0` | 10 |
| `1108 1/3` | 3 |
| `1115 2/3` | 3 |
| `1119` | 3 |
| `1120 2/3` | 3 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GYEAR` | `1982`, `1982`, `1982` |
| `SEC` | `1982`, `1982`, `1982` |
| `RANK` | `5`, `6`, `2` |
| `LEAGUE` | `dream`, `dream`, `magic` |
| `TEAM` | `롯데`, `삼미`, `삼성` |
| `GAME` | `80`, `80`, `80` |
| `WIN` | `31`, `15`, `54` |
| `LOSE` | `49`, `65`, `26` |
| `SAME` | `0`, `0`, `0` |
| `WRA` | `0.3880000114440918`, `0.18799999356269836`, `0.675000011920929` |
