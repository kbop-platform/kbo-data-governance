# SEASON_PLAYER_PITCHER_SITUATION

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_2_220328` |
| 행 수 | 301,375 |
| 컬럼 수 | 14 |
| PK | `SEASON_ID, P_ID, SECTION_CD, SITUATION_IF` |
| 스키마 세대 | new |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 통계분석팀 (R-04) |
| 갱신 주기 | D+1 (시즌 중) |
| 소비자 | 분석팀 |
| 데이터 프로덕트 | [시즌 통계](../products/season-stats.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 3 | `SEASON_ID` | smallint |  | NN | PK | 시즌 ID (연도) | `season_id` |
| 4 | `P_ID` | int |  | NN | PK | 선수 ID (정수) | `player_id` |
| 5 | `SECTION_CD` | int |  | NN | PK | 구간 코드 | `section_cd` |
| 6 | `SITUATION_IF` | varchar | 20 | NN | PK | 상황 구분 | `situation_if` |
| 7 | `AB_CN` | int |  | NN |  | AB 건수 | `ab_cn` |
| 8 | `HIT_CN` | int |  | NN |  | HIT 건수 | `hit_cn` |
| 9 | `H2_CN` | int |  | NN |  | H2 건수 | `h2b_cn` |
| 10 | `H3_CN` | int |  | NN |  | H3 건수 | `h3b_cn` |
| 11 | `HR_CN` | int |  | NN |  | HR 건수 | `hr_cn` |
| 12 | `BB_CN` | int |  | NN |  | BB 건수 | `bb_cn` |
| 13 | `HP_CN` | int |  | NN |  | HP 건수 | `hbp_cn` |
| 14 | `KK_CN` | int |  | NN |  | KK 건수 | `so_cn` |
| 15 | `WP_CN` | int |  | NN |  | WP 건수 | `wp_cn` |
| 16 | `BK_CN` | int |  | NN |  | BK 건수 | `bk_cn` |

## 코드값 / 고유값


### `SEASON_ID`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `P_ID`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `SECTION_CD`

| 값 | 건수 |
|-----|------|
| `4` | 84,574 |
| `7` | 66,666 |
| `6` | 56,395 |
| `3` | 55,687 |
| `5` | 22,801 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `SITUATION_IF`

| 값 | 건수 |
|-----|------|
| `1` | 26,865 |
| `2` | 26,761 |
| `3` | 18,872 |
| `0` | 15,226 |
| `8` | 14,124 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `SEASON_ID` | `1982`, `1982`, `1982` |
| `P_ID` | `10082`, `10082`, `10082` |
| `SECTION_CD` | `2`, `2`, `3` |
| `SITUATION_IF` | `L`, `R`, `0` |
| `AB_CN` | `43`, `262`, `182` |
| `HIT_CN` | `8`, `68`, `45` |
| `H2_CN` | `0`, `14`, `7` |
| `H3_CN` | `0`, `2`, `2` |
| `HR_CN` | `1`, `11`, `8` |
| `BB_CN` | `2`, `35`, `18` |
