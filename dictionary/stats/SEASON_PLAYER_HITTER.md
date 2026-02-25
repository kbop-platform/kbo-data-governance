# SEASON_PLAYER_HITTER

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_2_220328` |
| 행 수 | 19,747 |
| 컬럼 수 | 43 |
| PK | `SEASON_ID, P_ID, SECTION_CD, GROUP_IF` |
| 스키마 세대 | new |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 통계분석팀 (R-04) |
| 갱신 주기 | D+1 (시즌 중) |
| 소비자 | 통계팀, 외부 API |
| 데이터 프로덕트 | [시즌 통계](../products/season-stats.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 3 | `SEASON_ID` | smallint |  | NN | PK | 시즌 ID (연도) | `season_id` |
| 4 | `P_ID` | int |  | NN | PK | 선수 ID (정수) | `player_id` |
| 5 | `SECTION_CD` | int |  | NN | PK | 구간 코드 | `section_cd` |
| 6 | `GROUP_IF` | varchar | 20 | NN | PK | 그룹 여부 | `group_if` |
| 7 | `HRA_RT` | float |  | NN |  | HRA 비율 | `avg_rt` |
| 8 | `GAME_CN` | int |  | NN |  | GAME 건수 | `game_cn` |
| 9 | `PA_CN` | int |  | NN |  | PA 건수 | `pa_cn` |
| 10 | `AB_CN` | int |  | NN |  | AB 건수 | `ab_cn` |
| 11 | `RUN_CN` | int |  | NN |  | RUN 건수 | `run_cn` |
| 12 | `HIT_CN` | int |  | NN |  | HIT 건수 | `hit_cn` |
| 13 | `H2_CN` | int |  | NN |  | H2 건수 | `h2b_cn` |
| 14 | `H3_CN` | int |  | NN |  | H3 건수 | `h3b_cn` |
| 15 | `HR_CN` | int |  | NN |  | HR 건수 | `hr_cn` |
| 16 | `XBH_CN` | int |  | NN |  | XBH 건수 | `xbh_cn` |
| 17 | `TB_CN` | int |  | NN |  | TB 건수 | `tb_cn` |
| 18 | `MH_HITTER_CN` | int |  | NN |  | MH_HITTER 건수 | `mh_hitter_cn` |
| 19 | `RBI_CN` | int |  | NN |  | RBI 건수 | `rbi_cn` |
| 20 | `SB_CN` | int |  | NN |  | SB 건수 | `sb_cn` |
| 21 | `CS_CN` | int |  | NN |  | CS 건수 | `cs_cn` |
| 22 | `SB_RT` | float |  | NN |  | SB 비율 | `sb_rt` |
| 23 | `RO_CN` | int |  | NN |  | RO 건수 | `ro_cn` |
| 24 | `POFF_CN` | int |  | NN |  | POFF 건수 | `poff_cn` |
| 25 | `SH_CN` | int |  | NN |  | SH 건수 | `sh_cn` |
| 26 | `SF_CN` | int |  | NN |  | SF 건수 | `sf_cn` |
| 27 | `BB_CN` | int |  | NN |  | BB 건수 | `bb_cn` |
| 28 | `IB_CN` | int |  | NN |  | IB 건수 | `ibb_cn` |
| 29 | `HP_CN` | int |  | NN |  | HP 건수 | `hbp_cn` |
| 30 | `BBHP_CN` | int |  | NN |  | BBHP 건수 | `bb_hbp_cn` |
| 31 | `KK_CN` | int |  | NN |  | KK 건수 | `so_cn` |
| 32 | `GD_CN` | int |  | NN |  | GD 건수 | `gidp_cn` |
| 33 | `ERR_CN` | int |  | NN |  | ERR 건수 | `err_cn` |
| 34 | `WIN_HIT_CN` | int |  | NN |  | WIN_HIT 건수 | `win_hit_cn` |
| 35 | `GO_CN` | int |  | NN |  | GO 건수 | `go_cn` |
| 36 | `FO_CN` | int |  | NN |  | FO 건수 | `fo_cn` |
| 37 | `FOGO_RT` | float |  | NN |  | FOGO 비율 | `fo_go_rt` |
| 38 | `PA_PIT_RT` | float |  | NN |  | PA_PIT 비율 | `pa_pitch_rt` |
| 39 | `KK_BB_RT` | float |  | NN |  | KK_BB 비율 | `so_bb_rt` |
| 40 | `SP_HRA_RT` | float |  | NN |  | SP_HRA 비율 | `vs_sp_avg_rt` |
| 41 | `PH_HRA_RT` | float |  | NN |  | PH_HRA 비율 | `pinch_avg_rt` |
| 42 | `OBP_RT` | float |  | NN |  | OBP 비율 | `obp_rt` |
| 43 | `SLG_RT` | float |  | NN |  | SLG 비율 | `slg_rt` |
| 44 | `ISO_RT` | float |  | NN |  | ISO 비율 | `iso_rt` |
| 45 | `OPS_RT` | float |  | NN |  | OPS 비율 | `ops_rt` |

## 코드값 / 고유값


### `SEASON_ID`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `P_ID`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `SECTION_CD`

| 값 | 건수 |
|-----|------|
| `1` | 11,632 |
| `2` | 8,115 |



### `GROUP_IF`

| 값 | 건수 |
|-----|------|
| `LG` | 950 |
| `HH` | 935 |
| `SK` | 911 |
| `HT` | 897 |
| `LT` | 885 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `SEASON_ID` | `1982`, `1982`, `1982` |
| `P_ID` | `10005`, `30003`, `30004` |
| `SECTION_CD` | `1`, `1`, `1` |
| `GROUP_IF` | `1982`, `1982`, `1982` |
| `HRA_RT` | `0.25886523723602295`, `0.21052631735801697`, `0.25182482600212097` |
| `GAME_CN` | `76`, `12`, `80` |
| `PA_CN` | `323`, `22`, `299` |
| `AB_CN` | `282`, `19`, `274` |
| `RUN_CN` | `46`, `1`, `29` |
| `HIT_CN` | `73`, `4`, `69` |
