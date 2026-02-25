# SEASON_PLAYER_PITCHER

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_2_220328` |
| 행 수 | 13,306 |
| 컬럼 수 | 54 |
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
| 7 | `ERA_RT` | float |  | NN |  | ERA 비율 | `era_rt` |
| 8 | `GAME_CN` | int |  | NN |  | GAME 건수 | `game_cn` |
| 9 | `START_CN` | int |  | NN |  | START 건수 | `start_cn` |
| 10 | `QUIT_CN` | int |  | NN |  | QUIT 건수 | `quit_cn` |
| 11 | `W_CN` | int |  | NN |  | W 건수 | `win_cn` |
| 12 | `START_W_CN` | int |  | NN |  | START_W 건수 | `start_win_cn` |
| 13 | `RELIEF_W_CN` | int |  | NN |  | RELIEF_W 건수 | `relief_win_cn` |
| 14 | `L_CN` | int |  | NN |  | L 건수 | `loss_cn` |
| 15 | `D_CN` | int |  | NN |  | D 건수 | `double_cn` |
| 16 | `HOLD_CN` | int |  | NN |  | HOLD 건수 | `hld_cn` |
| 17 | `SV_CN` | int |  | NN |  | SV 건수 | `sv_cn` |
| 18 | `SHO_CN` | int |  | NN |  | SHO 건수 | `sho_cn` |
| 19 | `CG_CN` | int |  | NN |  | CG 건수 | `cg_cn` |
| 20 | `INN2_CN` | int |  | NN |  | 이닝 점수 컬럼 | `ip_cn` |
| 21 | `WRA_RT` | float |  | NN |  | WRA 비율 | `wrc_rt` |
| 22 | `PA_CN` | int |  | NN |  | PA 건수 | `pa_cn` |
| 23 | `AB_CN` | int |  | NN |  | AB 건수 | `ab_cn` |
| 24 | `PIT_CN` | int |  | NN |  | PIT 건수 | `pitch_cn` |
| 25 | `R_CN` | int |  | NN |  | R 건수 | `runs_cn` |
| 26 | `ER_CN` | int |  | NN |  | ER 건수 | `er_cn` |
| 27 | `HIT_CN` | int |  | NN |  | HIT 건수 | `hit_cn` |
| 28 | `H2_CN` | int |  | NN |  | H2 건수 | `h2b_cn` |
| 29 | `H3_CN` | int |  | NN |  | H3 건수 | `h3b_cn` |
| 30 | `HR_CN` | int |  | NN |  | HR 건수 | `hr_cn` |
| 31 | `SH_CN` | int |  | NN |  | SH 건수 | `sh_cn` |
| 32 | `SF_CN` | int |  | NN |  | SF 건수 | `sf_cn` |
| 33 | `BB_CN` | int |  | NN |  | BB 건수 | `bb_cn` |
| 34 | `IB_CN` | int |  | NN |  | IB 건수 | `ibb_cn` |
| 35 | `HP_CN` | int |  | NN |  | HP 건수 | `hbp_cn` |
| 36 | `BBHP_CN` | int |  | NN |  | BBHP 건수 | `bb_hbp_cn` |
| 37 | `KK_CN` | int |  | NN |  | KK 건수 | `so_cn` |
| 38 | `GD_CN` | int |  | NN |  | GD 건수 | `gidp_cn` |
| 39 | `BK_CN` | int |  | NN |  | BK 건수 | `bk_cn` |
| 40 | `WP_CN` | int |  | NN |  | WP 건수 | `wp_cn` |
| 41 | `GO_CN` | int |  | NN |  | GO 건수 | `go_cn` |
| 42 | `FO_CN` | int |  | NN |  | FO 건수 | `fo_cn` |
| 43 | `FOGO_RT` | float |  | NN |  | FOGO 비율 | `fo_go_rt` |
| 46 | `BS_CN` | int |  | NN |  | BS 건수 | `bs_cn` |
| 47 | `QS_CN` | int |  | NN |  | QS 건수 | `qs_cn` |
| 48 | `WHIP_RT` | float |  | NN |  | WHIP 비율 | `whip_rt` |
| 49 | `OAVG_RT` | float |  | NN |  | OAVG 비율 | `opp_avg_rt` |
| 50 | `OOBP_RT` | float |  | NN |  | OOBP 비율 | `opp_obp_rt` |
| 51 | `OSLG_RT` | float |  | NN |  | OSLG 비율 | `opp_slg_rt` |
| 52 | `OOPS_RT` | float |  | NN |  | OOPS 비율 | `opp_ops_rt` |
| 53 | `BABIP_RT` | float |  | NN |  | BABIP 비율 | `babip_rt` |
| 54 | `GAME_KK_RT` | float |  | NN |  | GAME_KK 비율 | `game_so_rt` |
| 55 | `GAME_BB_RT` | float |  | NN |  | GAME_BB 비율 | `game_bb_rt` |
| 56 | `GAME_PIT_AVG_RT` | float |  | NN |  | GAME_PIT_AVG 비율 | `game_pitch_avg_rt` |
| 57 | `INN_PIT_AVG_RT` | float |  | NN |  | 이닝 점수 컬럼 | `inn_pitch_avg_rt` |
| 58 | `BB_KK_RT` | float |  | NN |  | BB_KK 비율 | `bb_so_rt` |

## 코드값 / 고유값

### `SEASON_ID`

| 값 | 건수 |
|-----|------|
| `2021` | 620 |
| `2024` | 584 |
| `2023` | 576 |
| `2020` | 571 |
| `2022` | 565 |
| `2025` | 565 |
| `2018` | 522 |
| `2019` | 517 |
| `2016` | 506 |
| `2015` | 497 |
| `2017` | 483 |
| `2014` | 420 |
| `2013` | 391 |
| `2010` | 388 |
| `2009` | 386 |
| `2011` | 378 |
| `2012` | 377 |
| `2008` | 376 |
| `2004` | 359 |
| `2001` | 354 |

### `P_ID`

| 값 | 건수 |
|-----|------|
| `73801` | 48 |
| `72523` | 43 |
| `73211` | 41 |
| `73117` | 40 |
| `74857` | 38 |
| `73738` | 37 |
| `74513` | 36 |
| `99314` | 36 |
| `97336` | 36 |
| `72447` | 36 |
| `76650` | 36 |
| `77637` | 36 |
| `77446` | 36 |
| `70425` | 35 |
| `77318` | 35 |
| `70615` | 35 |
| `97541` | 34 |
| `99445` | 34 |
| `99563` | 34 |
| `77211` | 34 |

### `SECTION_CD`

| 값 | 건수 |
|-----|------|
| `1` | 7,675 |
| `2` | 5,631 |

### `GROUP_IF`

| 값 | 건수 |
|-----|------|
| `LG` | 657 |
| `HH` | 652 |
| `HT` | 639 |
| `SK` | 617 |
| `LT` | 616 |
| `OB` | 616 |
| `SS` | 587 |
| `WO` | 461 |
| `NC` | 351 |
| `2021` | 308 |
| `2024` | 291 |
| `KT` | 289 |
| `2023` | 285 |
| `2020` | 283 |
| `2025` | 281 |
| `2022` | 281 |
| `2018` | 260 |
| `2019` | 257 |
| `2016` | 250 |
| `2015` | 244 |

## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `SEASON_ID` | `1982`, `1982`, `1982` |
| `P_ID` | `10082`, `80620`, `82003` |
| `SECTION_CD` | `1`, `1`, `1` |
| `GROUP_IF` | `1982`, `1982`, `1982` |
| `ERA_RT` | `3.85714`, `2.46927`, `3.3913` |
| `GAME_CN` | `27`, `48`, `27` |
| `START_CN` | `0`, `0`, `0` |
| `QUIT_CN` | `0`, `0`, `0` |
| `W_CN` | `6`, `15`, `7` |
| `START_W_CN` | `0`, `0`, `0` |
| `RELIEF_W_CN` | `0`, `0`, `0` |
| `L_CN` | `5`, `11`, `6` |
| `D_CN` | `0`, `0`, `0` |
| `HOLD_CN` | `0`, `0`, `0` |
| `SV_CN` | `3`, `11`, `0` |
| `SHO_CN` | `0`, `2`, `1` |
| `CG_CN` | `2`, `8`, `6` |
| `INN2_CN` | `259`, `667`, `414` |
| `WRA_RT` | `0.5454545454545454`, `0.5769230769230769`, `0.5384615384615384` |
| `PA_CN` | `365`, `864`, `566` |
| `AB_CN` | `0`, `0`, `0` |
| `PIT_CN` | `0`, `0`, `0` |
| `R_CN` | `43`, `78`, `64` |
| `ER_CN` | `37`, `61`, `52` |
| `HIT_CN` | `76`, `189`, `139` |
| `H2_CN` | `0`, `0`, `0` |
| `H3_CN` | `0`, `0`, `0` |
| `HR_CN` | `12`, `11`, `8` |
| `SH_CN` | `0`, `0`, `0` |
| `SF_CN` | `0`, `0`, `0` |
| `BB_CN` | `37`, `34`, `31` |
| `IB_CN` | `0`, `0`, `0` |
| `HP_CN` | `11`, `6`, `4` |
| `BBHP_CN` | `48`, `40`, `35` |
| `KK_CN` | `42`, `99`, `65` |
| `GD_CN` | `0`, `0`, `0` |
| `BK_CN` | `0`, `0`, `0` |
| `WP_CN` | `0`, `0`, `0` |
| `GO_CN` | `0`, `0`, `0` |
| `FO_CN` | `0`, `0`, `0` |
| `FOGO_RT` | `0.0`, `0.0`, `0.0` |
| `BS_CN` | `0`, `0`, `0` |
| `QS_CN` | `0`, `0`, `0` |
| `WHIP_RT` | `0.0`, `0.0`, `0.0` |
| `OAVG_RT` | `0.0`, `0.0`, `0.0` |
| `OOBP_RT` | `0.0`, `0.0`, `0.0` |
| `OSLG_RT` | `0.0`, `0.0`, `0.0` |
| `OOPS_RT` | `0.0`, `0.0`, `0.0` |
| `BABIP_RT` | `0.0`, `0.0`, `0.0` |
| `GAME_KK_RT` | `0.0`, `0.0`, `0.0` |
| `GAME_BB_RT` | `0.0`, `0.0`, `0.0` |
| `GAME_PIT_AVG_RT` | `0.0`, `0.0`, `0.0` |
| `INN_PIT_AVG_RT` | `0.0`, `0.0`, `0.0` |
| `BB_KK_RT` | `0.0`, `0.0`, `0.0` |
