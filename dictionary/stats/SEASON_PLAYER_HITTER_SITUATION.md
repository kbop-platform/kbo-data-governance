# SEASON_PLAYER_HITTER_SITUATION

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_2_220328` |
| 행 수 | 360,625 |
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
| 8 | `AB_CN` | int |  | NN |  | AB 건수 | `ab_cn` |
| 9 | `HIT_CN` | int |  | NN |  | HIT 건수 | `hit_cn` |
| 10 | `H2_CN` | int |  | NN |  | H2 건수 | `h2b_cn` |
| 11 | `H3_CN` | int |  | NN |  | H3 건수 | `h3b_cn` |
| 12 | `HR_CN` | int |  | NN |  | HR 건수 | `hr_cn` |
| 13 | `RBI_CN` | int |  | NN |  | RBI 건수 | `rbi_cn` |
| 14 | `BB_CN` | int |  | NN |  | BB 건수 | `bb_cn` |
| 15 | `HP_CN` | int |  | NN |  | HP 건수 | `hbp_cn` |
| 16 | `KK_CN` | int |  | NN |  | KK 건수 | `so_cn` |
| 17 | `GD_CN` | int |  | NN |  | GD 건수 | `gidp_cn` |

## 코드값 / 고유값


### `SEASON_ID`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `P_ID`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `SECTION_CD`

| 값 | 건수 |
|-----|------|
| `4` | 96,664 |
| `6` | 89,827 |
| `3` | 64,106 |
| `7` | 55,507 |
| `5` | 27,871 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `SITUATION_IF`

| 값 | 건수 |
|-----|------|
| `2` | 32,102 |
| `1` | 30,109 |
| `3` | 20,217 |
| `0` | 18,639 |
| `9` | 16,424 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `SEASON_ID` | `1982`, `1982`, `1982` |
| `P_ID` | `10005`, `10005`, `10005` |
| `SECTION_CD` | `1`, `1`, `3` |
| `SITUATION_IF` | `LO`, `RO`, `0` |
| `AB_CN` | `55`, `227`, `192` |
| `HIT_CN` | `11`, `62`, `53` |
| `H2_CN` | `1`, `8`, `7` |
| `H3_CN` | `1`, `0`, `1` |
| `HR_CN` | `0`, `1`, `1` |
| `RBI_CN` | `0`, `12`, `1` |
