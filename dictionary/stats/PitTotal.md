# PitTotal

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 9,377 |
| 컬럼 수 | 22 |
| PK | `PCODE, GYEAR, SEC` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 통계분석팀 (R-04) |
| 갱신 주기 | D+1 (전일 경기 반영) |
| 소비자 | 통계팀, 외부 API |
| 데이터 프로덕트 | [시즌 통계](../products/season-stats.md) |
| 접근 수준 | Internal |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 2 | `GYEAR` | char | 4 | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `SEC` | varchar | 4 | NN | PK | 구간 (시즌연도 또는 "9999"=통산) | `series_cd` |
| 4 | `Team` | varchar | 6 |  |  | 팀 코드 | `team_cd` |
| 5 | `ERA` | float |  |  |  | 평균자책점 | `era` |
| 6 | `GAMENUM` | smallint |  | NN |  | 경기 수 | `game_cn` |
| 7 | `CG` | smallint |  | NN |  | 완투 | `cg` |
| 8 | `SHO` | smallint |  | NN |  | 완봉 | `sho` |
| 9 | `W` | smallint |  | NN |  | 승 | `win` |
| 10 | `L` | smallint |  | NN |  | 패 | `loss` |
| 11 | `SV` | smallint |  | NN |  | 세이브 | `sv` |
| 12 | `Hold` | smallint |  | NN |  | 홀드 | `hld` |
| 13 | `BF` | smallint |  | NN |  | 상대타자수 | `bf` |
| 14 | `INN` | varchar | 8 | NN |  | 이닝 번호 | `ip` |
| 15 | `INN2` | smallint |  | NN |  | 이닝 세부 (아웃수 환산 또는 연장 구분) | `inn_2_score` |
| 16 | `HIT` | smallint |  | NN |  | 안타 | `hit` |
| 17 | `HR` | smallint |  | NN |  | 홈런 | `hr` |
| 18 | `BB` | smallint |  | NN |  | 볼넷 | `bb` |
| 19 | `HP` | smallint |  | NN |  | 사구 (Hit by Pitch) | `hbp` |
| 20 | `KK` | smallint |  | NN |  | 삼진 | `so` |
| 21 | `R` | smallint |  | NN |  | 실점 | `runs_cn` |
| 22 | `ER` | smallint |  | NN |  | 자책점 | `er` |

## 코드값 / 고유값

> **EUC-KR 참고**: `Team` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨 (예: `·Ôµ¥`=롯데, `»ï¼º`=삼성). nvarchar 전환은 마이그레이션 시 처리.


### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SEC`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Team`

| 값 | 건수 |
|-----|------|
| `·Ôµ¥` | 897 |
| `»ï¼º` | 876 |
| `LG` | 857 |
| `ÇÑÈ­` | 760 |
| `µÎ»ê` | 643 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `GAMENUM`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `CG`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SHO`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `W`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `L`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SV`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Hold`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BF`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `INN`

| 값 | 건수 |
|-----|------|
| `1` | 212 |
| `2` | 170 |
| `3` | 123 |
| `4` | 101 |
| `0 1/3` | 92 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `INN2`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HIT`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BB`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HP`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `KK`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `R`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `ER`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `PCODE` | `10082`, `80620`, `82003` |
| `GYEAR` | `1982`, `1982`, `1982` |
| `SEC` | `1982`, `1982`, `1982` |
| `Team` | `OB`, `»ï¼º`, `OB` |
| `ERA` | `3.86`, `2.47`, `3.39` |
| `GAMENUM` | `27`, `48`, `27` |
| `CG` | `2`, `8`, `6` |
| `SHO` | `0`, `2`, `1` |
| `W` | `6`, `15`, `7` |
| `L` | `5`, `11`, `6` |
