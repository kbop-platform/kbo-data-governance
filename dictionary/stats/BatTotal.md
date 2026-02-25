# BatTotal

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 13,616 |
| 컬럼 수 | 23 |
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
| 4 | `TEAM` | varchar | 6 |  |  | 팀 코드 (2자리, HH=키움, HT=KIA 등) | `team_cd` |
| 5 | `HRA` | float |  | NN |  | 타율 | `avg` |
| 6 | `GAMENUM` | int |  | NN |  | 경기 수 | `game_cn` |
| 7 | `AB` | int |  | NN |  | 타수 (At Bat) | `ab` |
| 8 | `RUN` | int |  | NN |  | 득점 | `run` |
| 9 | `HIT` | int |  | NN |  | 안타 | `hit` |
| 10 | `H2` | int |  | NN |  | 2루타 | `h2b` |
| 11 | `H3` | int |  | NN |  | 3루타 | `h3b` |
| 12 | `HR` | int |  | NN |  | 홈런 | `hr` |
| 13 | `TB` | int |  | NN |  | 루타 (Total Bases) — 안타로 획득한 총 루수 | `tb_cn` |
| 14 | `RBI` | int |  | NN |  | 타점 | `rbi` |
| 15 | `SB` | int |  | NN |  | 도루 | `sb` |
| 16 | `CS` | int |  | NN |  | 도루실패 | `cs` |
| 17 | `SH` | int |  | NN |  | 희생번트 | `sh` |
| 18 | `SF` | int |  | NN |  | 희생플라이 | `sf` |
| 19 | `BB` | int |  | NN |  | 볼넷 | `bb` |
| 20 | `HP` | int |  | NN |  | 사구 (Hit by Pitch) | `hbp` |
| 21 | `KK` | int |  | NN |  | 삼진 | `so` |
| 22 | `GD` | int |  | NN |  | 병살타 | `gidp` |
| 23 | `ERR` | int |  | NN |  | 실책 | `err` |

## 코드값 / 고유값

> **EUC-KR 참고**: `TEAM` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨 (예: `·Ôµ¥`=롯데, `»ï¼º`=삼성). nvarchar 전환은 마이그레이션 시 처리.


### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SEC`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TEAM`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `TB`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `PCODE` | `10005`, `10005`, `10005` |
| `GYEAR` | `1982`, `1983`, `1984` |
| `SEC` | `1982`, `1983`, `1984` |
| `TEAM` | `ÇØÅÂ`, `»ï¼º`, `OB` |
| `HRA` | `0.259`, `0.211`, `0.252` |
| `GAMENUM` | `76`, `12`, `80` |
| `AB` | `282`, `19`, `274` |
| `RUN` | `46`, `1`, `29` |
| `HIT` | `73`, `4`, `69` |
| `H2` | `9`, `0`, `14` |
