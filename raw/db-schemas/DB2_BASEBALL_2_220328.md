# DB2_BASEBALL_2_220328 스키마

테이블 수: 5개

## 목차
1. [SEASON_PLAYER_HITTER](#season_player_hitter) (43컬럼, 16,099행)
2. [SEASON_PLAYER_HITTER_SITUATION](#season_player_hitter_situation) (14컬럼, 228,487행)
3. [SEASON_PLAYER_PITCHER](#season_player_pitcher) (54컬럼, 11,173행)
4. [SEASON_PLAYER_PITCHER_SITUATION](#season_player_pitcher_situation) (14컬럼, 214,288행)
5. [TEAM](#team) (7컬럼, 401행)

## SEASON_PLAYER_HITTER
- 행 수: **16,099**
- 컬럼 수: **43**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 3 | `SEASON_ID` | smallint | N | PK |  |  |
| 4 | `P_ID` | int | N | PK |  |  |
| 5 | `SECTION_CD` | int | N | PK |  |  |
| 6 | `GROUP_IF` | varchar(20) | N | PK |  |  |
| 7 | `HRA_RT` | float | N |  |  |  |
| 8 | `GAME_CN` | int | N |  |  |  |
| 9 | `PA_CN` | int | N |  |  |  |
| 10 | `AB_CN` | int | N |  |  |  |
| 11 | `RUN_CN` | int | N |  |  |  |
| 12 | `HIT_CN` | int | N |  |  |  |
| 13 | `H2_CN` | int | N |  |  |  |
| 14 | `H3_CN` | int | N |  |  |  |
| 15 | `HR_CN` | int | N |  |  |  |
| 16 | `XBH_CN` | int | N |  |  |  |
| 17 | `TB_CN` | int | N |  |  |  |
| 18 | `MH_HITTER_CN` | int | N |  |  |  |
| 19 | `RBI_CN` | int | N |  |  |  |
| 20 | `SB_CN` | int | N |  |  |  |
| 21 | `CS_CN` | int | N |  |  |  |
| 22 | `SB_RT` | float | N |  |  |  |
| 23 | `RO_CN` | int | N |  |  |  |
| 24 | `POFF_CN` | int | N |  |  |  |
| 25 | `SH_CN` | int | N |  |  |  |
| 26 | `SF_CN` | int | N |  |  |  |
| 27 | `BB_CN` | int | N |  |  |  |
| 28 | `IB_CN` | int | N |  |  |  |
| 29 | `HP_CN` | int | N |  |  |  |
| 30 | `BBHP_CN` | int | N |  |  |  |
| 31 | `KK_CN` | int | N |  |  |  |
| 32 | `GD_CN` | int | N |  |  |  |
| 33 | `ERR_CN` | int | N |  |  |  |
| 34 | `WIN_HIT_CN` | int | N |  |  |  |
| 35 | `GO_CN` | int | N |  |  |  |
| 36 | `FO_CN` | int | N |  |  |  |
| 37 | `FOGO_RT` | float | N |  |  |  |
| 38 | `PA_PIT_RT` | float | N |  |  |  |
| 39 | `KK_BB_RT` | float | N |  |  |  |
| 40 | `SP_HRA_RT` | float | N |  |  |  |
| 41 | `PH_HRA_RT` | float | N |  |  |  |
| 42 | `OBP_RT` | float | N |  |  |  |
| 43 | `SLG_RT` | float | N |  |  |  |
| 44 | `ISO_RT` | float | N |  |  |  |
| 45 | `OPS_RT` | float | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_SEASON_PLAYER_HITTER_1 (PK) | CLUSTERED | Y | SEASON_ID, P_ID, SECTION_CD, GROUP_IF |

---

## SEASON_PLAYER_HITTER_SITUATION
- 행 수: **228,487**
- 컬럼 수: **14**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 3 | `SEASON_ID` | smallint | N | PK |  |  |
| 4 | `P_ID` | int | N | PK |  |  |
| 5 | `SECTION_CD` | int | N | PK |  |  |
| 6 | `SITUATION_IF` | varchar(20) | N | PK |  |  |
| 8 | `AB_CN` | int | N |  |  |  |
| 9 | `HIT_CN` | int | N |  |  |  |
| 10 | `H2_CN` | int | N |  |  |  |
| 11 | `H3_CN` | int | N |  |  |  |
| 12 | `HR_CN` | int | N |  |  |  |
| 13 | `RBI_CN` | int | N |  |  |  |
| 14 | `BB_CN` | int | N |  |  |  |
| 15 | `HP_CN` | int | N |  |  |  |
| 16 | `KK_CN` | int | N |  |  |  |
| 17 | `GD_CN` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_SEASON_PLAYER_HITTER_SITUATION_1 (PK) | CLUSTERED | Y | SEASON_ID, P_ID, SECTION_CD, SITUATION_IF |

---

## SEASON_PLAYER_PITCHER
- 행 수: **11,173**
- 컬럼 수: **54**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 3 | `SEASON_ID` | smallint | N | PK |  |  |
| 4 | `P_ID` | int | N | PK |  |  |
| 5 | `SECTION_CD` | int | N | PK |  |  |
| 6 | `GROUP_IF` | varchar(20) | N | PK |  |  |
| 7 | `ERA_RT` | float | N |  |  |  |
| 8 | `GAME_CN` | int | N |  |  |  |
| 9 | `START_CN` | int | N |  |  |  |
| 10 | `QUIT_CN` | int | N |  |  |  |
| 11 | `W_CN` | int | N |  |  |  |
| 12 | `START_W_CN` | int | N |  |  |  |
| 13 | `RELIEF_W_CN` | int | N |  |  |  |
| 14 | `L_CN` | int | N |  |  |  |
| 15 | `D_CN` | int | N |  |  |  |
| 16 | `HOLD_CN` | int | N |  |  |  |
| 17 | `SV_CN` | int | N |  |  |  |
| 18 | `SHO_CN` | int | N |  |  |  |
| 19 | `CG_CN` | int | N |  |  |  |
| 20 | `INN2_CN` | int | N |  |  |  |
| 21 | `WRA_RT` | float | N |  |  |  |
| 22 | `PA_CN` | int | N |  |  |  |
| 23 | `AB_CN` | int | N |  |  |  |
| 24 | `PIT_CN` | int | N |  |  |  |
| 25 | `R_CN` | int | N |  |  |  |
| 26 | `ER_CN` | int | N |  |  |  |
| 27 | `HIT_CN` | int | N |  |  |  |
| 28 | `H2_CN` | int | N |  |  |  |
| 29 | `H3_CN` | int | N |  |  |  |
| 30 | `HR_CN` | int | N |  |  |  |
| 31 | `SH_CN` | int | N |  |  |  |
| 32 | `SF_CN` | int | N |  |  |  |
| 33 | `BB_CN` | int | N |  |  |  |
| 34 | `IB_CN` | int | N |  |  |  |
| 35 | `HP_CN` | int | N |  |  |  |
| 36 | `BBHP_CN` | int | N |  |  |  |
| 37 | `KK_CN` | int | N |  |  |  |
| 38 | `GD_CN` | int | N |  |  |  |
| 39 | `BK_CN` | int | N |  |  |  |
| 40 | `WP_CN` | int | N |  |  |  |
| 41 | `GO_CN` | int | N |  |  |  |
| 42 | `FO_CN` | int | N |  |  |  |
| 43 | `FOGO_RT` | float | N |  |  |  |
| 46 | `BS_CN` | int | N |  |  |  |
| 47 | `QS_CN` | int | N |  |  |  |
| 48 | `WHIP_RT` | float | N |  |  |  |
| 49 | `OAVG_RT` | float | N |  |  |  |
| 50 | `OOBP_RT` | float | N |  |  |  |
| 51 | `OSLG_RT` | float | N |  |  |  |
| 52 | `OOPS_RT` | float | N |  |  |  |
| 53 | `BABIP_RT` | float | N |  |  |  |
| 54 | `GAME_KK_RT` | float | N |  |  |  |
| 55 | `GAME_BB_RT` | float | N |  |  |  |
| 56 | `GAME_PIT_AVG_RT` | float | N |  |  |  |
| 57 | `INN_PIT_AVG_RT` | float | N |  |  |  |
| 58 | `BB_KK_RT` | float | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_SEASON_PLAYER_PITCHER_1 (PK) | CLUSTERED | Y | SEASON_ID, P_ID, SECTION_CD, GROUP_IF |

---

## SEASON_PLAYER_PITCHER_SITUATION
- 행 수: **214,288**
- 컬럼 수: **14**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 3 | `SEASON_ID` | smallint | N | PK |  |  |
| 4 | `P_ID` | int | N | PK |  |  |
| 5 | `SECTION_CD` | int | N | PK |  |  |
| 6 | `SITUATION_IF` | varchar(20) | N | PK |  |  |
| 7 | `AB_CN` | int | N |  |  |  |
| 8 | `HIT_CN` | int | N |  |  |  |
| 9 | `H2_CN` | int | N |  |  |  |
| 10 | `H3_CN` | int | N |  |  |  |
| 11 | `HR_CN` | int | N |  |  |  |
| 12 | `BB_CN` | int | N |  |  |  |
| 13 | `HP_CN` | int | N |  |  |  |
| 14 | `KK_CN` | int | N |  |  |  |
| 15 | `WP_CN` | int | N |  |  |  |
| 16 | `BK_CN` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_SEASON_PLAYER_PITCHER_SITUATION_1 (PK) | CLUSTERED | Y | SEASON_ID, P_ID, SECTION_CD, SITUATION_IF |

---

## TEAM
- 행 수: **401**
- 컬럼 수: **7**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 2 | `SEASON_ID` | smallint | N | PK |  |  |
| 3 | `T_ID` | char(2) | N | PK |  |  |
| 4 | `FIRST_NM` | varchar(50) | N |  |  |  |
| 5 | `LAST_NM` | varchar(50) | Y |  |  |  |
| 6 | `FIRST_ENG_NM` | varchar(50) | Y |  |  |  |
| 7 | `LAST_ENG_NM` | varchar(50) | Y |  |  |  |
| 8 | `GROUP_SC` | varchar(10) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_TEAM_1 (PK) | CLUSTERED | Y | SEASON_ID, T_ID |

---
