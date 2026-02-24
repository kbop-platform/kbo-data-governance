# FALL_LEAGUE_BASEBALL 스키마

테이블 수: 11개

## 목차
1. [FALL_LEAGUE_RECORD](#fall_league_record) (20컬럼, 103행)
2. [GAME_KBO](#game_kbo) (24컬럼, 70행)
3. [GAME_PLAYER_HITTER](#game_player_hitter) (31컬럼, 1,426행)
4. [GAME_PLAYER_PITCHER](#game_player_pitcher) (38컬럼, 646행)
5. [GAME_TEAM_HITTER](#game_team_hitter) (24컬럼, 58행)
6. [GAME_TEAM_PITCHER](#game_team_pitcher) (24컬럼, 58행)
7. [PERSON_BASE](#person_base) (6컬럼, 5,184행)
8. [SEASON_PLAYER_HITTER](#season_player_hitter) (46컬럼, 354행)
9. [SEASON_PLAYER_PITCHER](#season_player_pitcher) (59컬럼, 306행)
10. [SEASON_TEAM_HITTER](#season_team_hitter) (37컬럼, 27행)
11. [SEASON_TEAM_PITCHER](#season_team_pitcher) (38컬럼, 25행)

## FALL_LEAGUE_RECORD
- 행 수: **103**
- 컬럼 수: **20**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `선수` | nvarchar(50) | N | PK |  |  |
| 2 | `팀` | nvarchar(10) | N | PK |  |  |
| 3 | `타율` | real | Y |  |  |  |
| 4 | `경기` | int | Y |  |  |  |
| 5 | `타석` | int | Y |  |  |  |
| 6 | `타수` | int | Y |  |  |  |
| 7 | `득점` | int | Y |  |  |  |
| 8 | `안타` | int | Y |  |  |  |
| 9 | `2루타` | int | Y |  |  |  |
| 10 | `3루타` | int | Y |  |  |  |
| 11 | `홈런` | int | Y |  |  |  |
| 12 | `루타` | int | Y |  |  |  |
| 13 | `타점` | int | Y |  |  |  |
| 14 | `도루` | int | Y |  |  |  |
| 15 | `희비` | int | Y |  |  |  |
| 16 | `볼넷` | int | Y |  |  |  |
| 17 | `사구` | int | Y |  |  |  |
| 18 | `삼진` | int | Y |  |  |  |
| 19 | `출루율` | real | Y |  |  |  |
| 20 | `장타율` | real | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| FALL_LEAGUE_RECORD_PK (PK) | CLUSTERED | Y | 선수, 팀 |

---

## GAME_KBO
- 행 수: **70**
- 컬럼 수: **24**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `SR_ID` | int | Y |  |  |  |
| 3 | `G_ID` | varchar(50) | N | PK |  |  |
| 4 | `SEASON_ID` | int | Y |  |  |  |
| 5 | `G_DT` | varchar(50) | Y |  |  |  |
| 6 | `HEADER_NO` | int | Y |  |  |  |
| 7 | `AWAY_ID` | varchar(50) | Y |  |  |  |
| 8 | `AWAY_NM` | nvarchar(50) | Y |  |  |  |
| 9 | `HOME_ID` | varchar(50) | Y |  |  |  |
| 10 | `HOME_NM` | nvarchar(50) | Y |  |  |  |
| 11 | `S_NM` | nvarchar(50) | Y |  |  |  |
| 12 | `G_TM` | varchar(50) | Y |  |  |  |
| 13 | `T_PIT_P_ID` | int | Y |  |  |  |
| 14 | `T_PIT_P_NM` | varchar(50) | Y |  |  |  |
| 15 | `B_PIT_P_ID` | int | Y |  |  |  |
| 16 | `B_PIT_P_NM` | varchar(50) | Y |  |  |  |
| 17 | `T_SCORE_CN` | int | Y |  |  |  |
| 18 | `B_SCORE_CN` | int | Y |  |  |  |
| 19 | `T_RECORDPAGE_IF` | varchar(50) | Y |  |  |  |
| 20 | `B_RECORDPAGE_IF` | varchar(50) | Y |  |  |  |
| 21 | `CROWD_CN` | varchar(50) | Y |  |  |  |
| 22 | `GAME_SC_ID` | int | Y |  |  |  |
| 23 | `CANCEL_SC_ID` | int | Y |  |  |  |
| 24 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| GAME_KBO_PK (PK) | CLUSTERED | Y | G_ID |

---

## GAME_PLAYER_HITTER
- 행 수: **1,426**
- 컬럼 수: **31**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `Column1` | int | Y |  |  |  |
| 2 | `LE_ID` | int | Y |  |  |  |
| 3 | `SR_ID` | int | Y |  |  |  |
| 4 | `G_ID` | varchar(50) | N |  |  |  |
| 5 | `P_NM` | nvarchar(50) | N |  |  |  |
| 6 | `P_ID` | int | Y |  |  |  |
| 7 | `SEASON_ID` | int | Y |  |  |  |
| 8 | `TB_SC` | varchar(50) | Y |  |  |  |
| 9 | `BAT_TURN_NO` | int | Y |  |  |  |
| 10 | `BAT_ORDER_NO` | int | Y |  |  |  |
| 11 | `HRA_RT` | int | Y |  |  |  |
| 12 | `PA_CN` | int | Y |  |  |  |
| 13 | `AB_CN` | int | Y |  |  |  |
| 14 | `RUN_CN` | int | Y |  |  |  |
| 15 | `HIT_CN` | int | Y |  |  |  |
| 16 | `H2_CN` | int | Y |  |  |  |
| 17 | `H3_CN` | int | Y |  |  |  |
| 18 | `HR_CN` | int | Y |  |  |  |
| 19 | `RBI_CN` | int | Y |  |  |  |
| 20 | `SB_CN` | int | Y |  |  |  |
| 21 | `CS_CN` | int | Y |  |  |  |
| 22 | `RO_CN` | int | Y |  |  |  |
| 23 | `POFF_CN` | int | Y |  |  |  |
| 24 | `SH_CN` | int | Y |  |  |  |
| 25 | `SF_CN` | int | Y |  |  |  |
| 26 | `BB_CN` | int | Y |  |  |  |
| 27 | `IB_CN` | int | Y |  |  |  |
| 28 | `HP_CN` | int | Y |  |  |  |
| 29 | `KK_CN` | int | Y |  |  |  |
| 30 | `GD_CN` | int | Y |  |  |  |
| 31 | `REG_DT` | varchar(50) | Y |  |  |  |

---

## GAME_PLAYER_PITCHER
- 행 수: **646**
- 컬럼 수: **38**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `Column1` | int | Y |  |  |  |
| 2 | `LE_ID` | int | Y |  |  |  |
| 3 | `SR_ID` | int | Y |  |  |  |
| 4 | `G_ID` | varchar(50) | Y |  |  |  |
| 5 | `P_NM` | nvarchar(50) | Y |  |  |  |
| 6 | `P_ID` | int | Y |  |  |  |
| 7 | `SEASON_ID` | int | Y |  |  |  |
| 8 | `TB_SC` | varchar(50) | Y |  |  |  |
| 9 | `TURN_NO` | int | Y |  |  |  |
| 10 | `ERA_RT` | int | Y |  |  |  |
| 11 | `RESULT_SC` | varchar(50) | Y |  |  |  |
| 12 | `START_CK` | int | Y |  |  |  |
| 13 | `QUIT_CK` | int | Y |  |  |  |
| 14 | `SHO_CK` | int | Y |  |  |  |
| 15 | `CG_CK` | int | Y |  |  |  |
| 16 | `INN2_CN` | int | Y |  |  |  |
| 17 | `PA_CN` | int | Y |  |  |  |
| 18 | `AB_CN` | int | Y |  |  |  |
| 19 | `PIT_CN` | int | Y |  |  |  |
| 20 | `R_CN` | int | Y |  |  |  |
| 21 | `ER_CN` | int | Y |  |  |  |
| 22 | `HIT_CN` | int | Y |  |  |  |
| 23 | `H2_CN` | int | Y |  |  |  |
| 24 | `H3_CN` | int | Y |  |  |  |
| 25 | `HR_CN` | int | Y |  |  |  |
| 26 | `SH_CN` | int | Y |  |  |  |
| 27 | `SF_CN` | int | Y |  |  |  |
| 28 | `BB_CN` | int | Y |  |  |  |
| 29 | `HP_CN` | int | Y |  |  |  |
| 30 | `IB_CN` | int | Y |  |  |  |
| 31 | `BBHP_CN` | int | Y |  |  |  |
| 32 | `KK_CN` | int | Y |  |  |  |
| 33 | `BK_CN` | int | Y |  |  |  |
| 34 | `WP_CN` | int | Y |  |  |  |
| 35 | `BS_CK` | int | Y |  |  |  |
| 36 | `QS_CK` | int | Y |  |  |  |
| 37 | `OAVG_RT` | int | Y |  |  |  |
| 38 | `REG_DT` | varchar(50) | Y |  |  |  |

---

## GAME_TEAM_HITTER
- 행 수: **58**
- 컬럼 수: **24**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `SR_ID` | int | Y |  |  |  |
| 3 | `G_ID` | varchar(50) | N | PK |  |  |
| 4 | `T_ID` | varchar(50) | N | PK |  |  |
| 5 | `SEASON_ID` | int | Y |  |  |  |
| 6 | `TB_SC` | varchar(50) | Y |  |  |  |
| 7 | `HRA_RT` | int | Y |  |  |  |
| 8 | `AB_CN` | int | Y |  |  |  |
| 9 | `RUN_CN` | int | Y |  |  |  |
| 10 | `HIT_CN` | int | Y |  |  |  |
| 11 | `H2_CN` | int | Y |  |  |  |
| 12 | `H3_CN` | int | Y |  |  |  |
| 13 | `HR_CN` | int | Y |  |  |  |
| 14 | `SB_CN` | int | Y |  |  |  |
| 15 | `CS_CN` | int | Y |  |  |  |
| 16 | `RO_CN` | int | Y |  |  |  |
| 17 | `POFF_CN` | int | Y |  |  |  |
| 18 | `SH_CN` | int | Y |  |  |  |
| 19 | `SF_CN` | int | Y |  |  |  |
| 20 | `BB_CN` | int | Y |  |  |  |
| 21 | `HP_CN` | int | Y |  |  |  |
| 22 | `KK_CN` | int | Y |  |  |  |
| 23 | `ERR_CN` | int | Y |  |  |  |
| 24 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| GAME_TEAM_HITTER_PK (PK) | CLUSTERED | Y | G_ID, T_ID |

---

## GAME_TEAM_PITCHER
- 행 수: **58**
- 컬럼 수: **24**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `SR_ID` | int | Y |  |  |  |
| 3 | `G_ID` | varchar(50) | N | PK |  |  |
| 4 | `T_ID` | varchar(50) | N | PK |  |  |
| 5 | `SEASON_ID` | int | Y |  |  |  |
| 6 | `TB_SC` | varchar(50) | Y |  |  |  |
| 7 | `ERA_RT` | int | Y |  |  |  |
| 8 | `RESULT_SC` | varchar(50) | Y |  |  |  |
| 9 | `INN2_CN` | int | Y |  |  |  |
| 10 | `AB_CN` | int | Y |  |  |  |
| 11 | `R_CN` | int | Y |  |  |  |
| 12 | `ER_CN` | int | Y |  |  |  |
| 13 | `HIT_CN` | int | Y |  |  |  |
| 14 | `H2_CN` | int | Y |  |  |  |
| 15 | `H3_CN` | int | Y |  |  |  |
| 16 | `HR_CN` | int | Y |  |  |  |
| 17 | `SH_CN` | int | Y |  |  |  |
| 18 | `SF_CN` | int | Y |  |  |  |
| 19 | `BB_CN` | int | Y |  |  |  |
| 20 | `HP_CN` | int | Y |  |  |  |
| 21 | `KK_CN` | int | Y |  |  |  |
| 22 | `ERR_CN` | int | Y |  |  |  |
| 23 | `QS_CK` | int | Y |  |  |  |
| 24 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| GAME_TEAM_PITCHER_PK (PK) | CLUSTERED | Y | G_ID, T_ID |

---

## PERSON_BASE
- 행 수: **5,184**
- 컬럼 수: **6**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `P_ID` | varchar(50) | N | PK |  |  |
| 2 | `P_NM` | nvarchar(50) | Y |  |  |  |
| 3 | `minor_T_NM` | nvarchar(50) | Y |  |  |  |
| 4 | `minor_T_ID` | varchar(50) | Y |  |  |  |
| 5 | `POS_NM` | nvarchar(50) | Y |  |  |  |
| 6 | `BIRTH_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PERSON_BASE_PK (PK) | CLUSTERED | Y | P_ID |

---

## SEASON_PLAYER_HITTER
- 행 수: **354**
- 컬럼 수: **46**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `NAME` | varchar(100) | Y |  |  |  |
| 3 | `SEASON_ID` | int | N | PK |  |  |
| 4 | `P_ID` | varchar(10) | N | PK |  |  |
| 5 | `SECTION_CD` | varchar(10) | N | PK |  |  |
| 6 | `GROUP_IF` | varchar(50) | N | PK |  |  |
| 7 | `HRA_RT` | real | Y |  |  |  |
| 8 | `GAME_CN` | int | Y |  |  |  |
| 9 | `PA_CN` | int | Y |  |  |  |
| 10 | `AB_CN` | int | Y |  |  |  |
| 11 | `RUN_CN` | int | Y |  |  |  |
| 12 | `HIT_CN` | int | Y |  |  |  |
| 13 | `H2_CN` | int | Y |  |  |  |
| 14 | `H3_CN` | int | Y |  |  |  |
| 15 | `HR_CN` | int | Y |  |  |  |
| 16 | `XBH_CN` | int | Y |  |  |  |
| 17 | `TB_CN` | int | Y |  |  |  |
| 18 | `MH_HITTER_CN` | int | Y |  |  |  |
| 19 | `RBI_CN` | int | Y |  |  |  |
| 20 | `SB_CN` | int | Y |  |  |  |
| 21 | `CS_CN` | int | Y |  |  |  |
| 22 | `SB_RT` | int | Y |  |  |  |
| 23 | `RO_CN` | int | Y |  |  |  |
| 24 | `POFF_CN` | int | Y |  |  |  |
| 25 | `SH_CN` | int | Y |  |  |  |
| 26 | `SF_CN` | int | Y |  |  |  |
| 27 | `BB_CN` | int | Y |  |  |  |
| 28 | `IB_CN` | int | Y |  |  |  |
| 29 | `HP_CN` | int | Y |  |  |  |
| 30 | `KK_CN` | int | Y |  |  |  |
| 31 | `GD_CN` | int | Y |  |  |  |
| 32 | `ERR_CN` | int | Y |  |  |  |
| 33 | `WIN_HIT_CN` | int | Y |  |  |  |
| 34 | `GO_CN` | int | Y |  |  |  |
| 35 | `FO_CN` | int | Y |  |  |  |
| 36 | `FOGO_RT` | int | Y |  |  |  |
| 37 | `KK_BB_RT` | int | Y |  |  |  |
| 38 | `SP_HRA_RT` | int | Y |  |  |  |
| 39 | `PH_HRA_RT` | int | Y |  |  |  |
| 40 | `OBP_RT` | real | Y |  |  |  |
| 41 | `SLG_RT` | real | Y |  |  |  |
| 42 | `ISO_RT` | int | Y |  |  |  |
| 43 | `OPS_RT` | int | Y |  |  |  |
| 44 | `XR_RT` | int | Y |  |  |  |
| 45 | `GPA_RT` | int | Y |  |  |  |
| 46 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| SEASON_PLAYER_HITTER_PK (PK) | CLUSTERED | Y | SEASON_ID, P_ID, SECTION_CD, GROUP_IF |

---

## SEASON_PLAYER_PITCHER
- 행 수: **306**
- 컬럼 수: **59**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `NAME` | varchar(100) | Y |  |  |  |
| 3 | `SEASON_ID` | int | N | PK |  |  |
| 4 | `P_ID` | varchar(10) | N | PK |  |  |
| 5 | `SECTION_CD` | varchar(10) | N | PK |  |  |
| 6 | `GROUP_IF` | varchar(50) | N | PK |  |  |
| 7 | `ERA_RT` | real | Y |  |  |  |
| 8 | `GAME_CN` | int | Y |  |  |  |
| 9 | `START_CN` | int | Y |  |  |  |
| 10 | `QUIT_CN` | int | Y |  |  |  |
| 11 | `W_CN` | int | Y |  |  |  |
| 12 | `START_W_CN` | int | Y |  |  |  |
| 13 | `RELIEF_W_CN` | int | Y |  |  |  |
| 14 | `L_CN` | int | Y |  |  |  |
| 15 | `D_CN` | int | Y |  |  |  |
| 16 | `HOLD_CN` | int | Y |  |  |  |
| 17 | `SV_CN` | int | Y |  |  |  |
| 18 | `SHO_CN` | int | Y |  |  |  |
| 19 | `CG_CN` | int | Y |  |  |  |
| 20 | `INN2_CN` | int | Y |  |  |  |
| 21 | `WRA_RT` | real | Y |  |  |  |
| 22 | `PA_CN` | int | Y |  |  |  |
| 23 | `AB_CN` | int | Y |  |  |  |
| 24 | `PIT_CN` | int | Y |  |  |  |
| 25 | `R_CN` | int | Y |  |  |  |
| 26 | `ER_CN` | int | Y |  |  |  |
| 27 | `HIT_CN` | int | Y |  |  |  |
| 28 | `H2_CN` | int | Y |  |  |  |
| 29 | `H3_CN` | int | Y |  |  |  |
| 30 | `HR_CN` | int | Y |  |  |  |
| 31 | `SH_CN` | int | Y |  |  |  |
| 32 | `SF_CN` | int | Y |  |  |  |
| 33 | `BB_CN` | int | Y |  |  |  |
| 34 | `IB_CN` | int | Y |  |  |  |
| 35 | `HP_CN` | int | Y |  |  |  |
| 36 | `BBHP_CN` | int | Y |  |  |  |
| 37 | `KK_CN` | int | Y |  |  |  |
| 38 | `GD_CN` | int | Y |  |  |  |
| 39 | `BK_CN` | int | Y |  |  |  |
| 40 | `WP_CN` | int | Y |  |  |  |
| 41 | `GO_CN` | int | Y |  |  |  |
| 42 | `FO_CN` | int | Y |  |  |  |
| 43 | `FOGO_RT` | int | Y |  |  |  |
| 44 | `SVO_CN` | int | Y |  |  |  |
| 45 | `TS_CN` | int | Y |  |  |  |
| 46 | `BS_CN` | int | Y |  |  |  |
| 47 | `QS_CN` | int | Y |  |  |  |
| 48 | `WHIP_RT` | int | Y |  |  |  |
| 49 | `OAVG_RT` | int | Y |  |  |  |
| 50 | `OOBP_RT` | int | Y |  |  |  |
| 51 | `OSLG_RT` | int | Y |  |  |  |
| 52 | `OOPS_RT` | int | Y |  |  |  |
| 53 | `BABIP_RT` | int | Y |  |  |  |
| 54 | `GAME_KK_RT` | int | Y |  |  |  |
| 55 | `GAME_BB_RT` | int | Y |  |  |  |
| 56 | `GAME_PIT_AVG_RT` | int | Y |  |  |  |
| 57 | `INN_PIT_AVG_RT` | int | Y |  |  |  |
| 58 | `BB_KK_RT` | int | Y |  |  |  |
| 59 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| SEASON_PLAYER_PITCHER_PK (PK) | CLUSTERED | Y | SEASON_ID, P_ID, SECTION_CD, GROUP_IF |

---

## SEASON_TEAM_HITTER
- 행 수: **27**
- 컬럼 수: **37**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `SR_ID` | int | Y |  |  |  |
| 3 | `SEASON_ID` | int | N | PK |  |  |
| 4 | `T_ID` | varchar(50) | N | PK |  |  |
| 5 | `SECTION_CD` | varchar(10) | N | PK |  |  |
| 6 | `GROUP_IF` | int | N | PK |  |  |
| 7 | `HRA_RT` | real | Y |  |  |  |
| 8 | `GAME_CN` | int | Y |  |  |  |
| 9 | `PA_CN` | int | Y |  |  |  |
| 10 | `AB_CN` | int | Y |  |  |  |
| 11 | `RUN_CN` | int | Y |  |  |  |
| 12 | `HIT_CN` | int | Y |  |  |  |
| 13 | `H2_CN` | int | Y |  |  |  |
| 14 | `H3_CN` | int | Y |  |  |  |
| 15 | `HR_CN` | int | Y |  |  |  |
| 16 | `TB_CN` | int | Y |  |  |  |
| 17 | `MH_HITTER_CN` | int | Y |  |  |  |
| 18 | `RBI_CN` | int | Y |  |  |  |
| 19 | `SB_CN` | int | Y |  |  |  |
| 20 | `CS_CN` | int | Y |  |  |  |
| 21 | `SB_RT` | int | Y |  |  |  |
| 22 | `RO_CN` | int | Y |  |  |  |
| 23 | `POFF_CN` | int | Y |  |  |  |
| 24 | `SH_CN` | int | Y |  |  |  |
| 25 | `SF_CN` | int | Y |  |  |  |
| 26 | `BB_CN` | int | Y |  |  |  |
| 27 | `IB_CN` | int | Y |  |  |  |
| 28 | `HP_CN` | int | Y |  |  |  |
| 29 | `KK_CN` | int | Y |  |  |  |
| 30 | `GD_CN` | int | Y |  |  |  |
| 31 | `ERR_CN` | int | Y |  |  |  |
| 32 | `SP_HRA_RT` | int | Y |  |  |  |
| 33 | `PH_HRA_RT` | int | Y |  |  |  |
| 34 | `OBP_RT` | real | Y |  |  |  |
| 35 | `SLG_RT` | real | Y |  |  |  |
| 36 | `OPS_RT` | int | Y |  |  |  |
| 37 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| SEASON_TEAM_HITTER_PK (PK) | CLUSTERED | Y | SEASON_ID, T_ID, SECTION_CD, GROUP_IF |

---

## SEASON_TEAM_PITCHER
- 행 수: **25**
- 컬럼 수: **38**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | int | Y |  |  |  |
| 2 | `SR_ID` | int | Y |  |  |  |
| 3 | `SEASON_ID` | int | N | PK |  |  |
| 4 | `T_ID` | varchar(50) | N | PK |  |  |
| 5 | `SECTION_CD` | varchar(10) | N | PK |  |  |
| 6 | `GROUP_IF` | int | N | PK |  |  |
| 7 | `ERA_RT` | real | Y |  |  |  |
| 8 | `GAME_CN` | int | Y |  |  |  |
| 9 | `W_CN` | int | Y |  |  |  |
| 10 | `L_CN` | int | Y |  |  |  |
| 11 | `HOLD_CN` | int | Y |  |  |  |
| 12 | `SV_CN` | int | Y |  |  |  |
| 13 | `SHO_CN` | int | Y |  |  |  |
| 14 | `CG_CN` | int | Y |  |  |  |
| 15 | `INN2_CN` | int | Y |  |  |  |
| 16 | `WRA_RT` | real | Y |  |  |  |
| 17 | `PA_CN` | int | Y |  |  |  |
| 18 | `AB_CN` | int | Y |  |  |  |
| 19 | `PIT_CN` | int | Y |  |  |  |
| 20 | `R_CN` | int | Y |  |  |  |
| 21 | `ER_CN` | int | Y |  |  |  |
| 22 | `HIT_CN` | int | Y |  |  |  |
| 23 | `H2_CN` | int | Y |  |  |  |
| 24 | `H3_CN` | int | Y |  |  |  |
| 25 | `HR_CN` | int | Y |  |  |  |
| 26 | `SH_CN` | int | Y |  |  |  |
| 27 | `SF_CN` | int | Y |  |  |  |
| 28 | `BB_CN` | int | Y |  |  |  |
| 29 | `IB_CN` | int | Y |  |  |  |
| 30 | `HP_CN` | int | Y |  |  |  |
| 31 | `KK_CN` | int | Y |  |  |  |
| 32 | `BK_CN` | int | Y |  |  |  |
| 33 | `WP_CN` | int | Y |  |  |  |
| 34 | `BS_CN` | int | Y |  |  |  |
| 35 | `QS_CN` | int | Y |  |  |  |
| 36 | `WHIP_RT` | int | Y |  |  |  |
| 37 | `OAVG_RT` | int | Y |  |  |  |
| 38 | `REG_DT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| SEASON_TEAM_PITCHER_PK (PK) | CLUSTERED | Y | SEASON_ID, T_ID, SECTION_CD, GROUP_IF |

---
