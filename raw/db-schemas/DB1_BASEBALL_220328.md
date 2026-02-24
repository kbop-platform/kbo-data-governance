# DB1_BASEBALL_220328 스키마

테이블 수: 13개

## 목차
1. [BatTotal](#battotal) (23컬럼, 13,616행)
2. [DEFEN](#defen) (12컬럼, 846,736행)
3. [ENTRY](#entry) (11컬럼, 854,280행)
4. [GAMECONTAPP](#gamecontapp) (29컬럼, 2,531,702행)
5. [GAMEINFO](#gameinfo) (27컬럼, 23,579행)
6. [GAME_HR](#game_hr) (15컬럼, 7,784행)
7. [GAME_MEMO](#game_memo) (20컬럼, 54,544행)
8. [GAME_MEMO_PITCHCLOCK](#game_memo_pitchclock) (16컬럼, 237행)
9. [Hitter](#hitter) (26컬럼, 648,248행)
10. [PitTotal](#pittotal) (22컬럼, 9,377행)
11. [Pitcher](#pitcher) (36컬럼, 223,624행)
12. [Score](#score) (60컬럼, 23,579행)
13. [TeamRank](#teamrank) (30컬럼, 373행)

## BatTotal
- 행 수: **13,616**
- 컬럼 수: **23**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `SEC` | varchar(4) | N | PK |  |  |
| 4 | `TEAM` | varchar(6) | Y |  |  |  |
| 5 | `HRA` | float | N |  |  |  |
| 6 | `GAMENUM` | int | N |  |  |  |
| 7 | `AB` | int | N |  |  |  |
| 8 | `RUN` | int | N |  |  |  |
| 9 | `HIT` | int | N |  |  |  |
| 10 | `H2` | int | N |  |  |  |
| 11 | `H3` | int | N |  |  |  |
| 12 | `HR` | int | N |  |  |  |
| 13 | `TB` | int | N |  |  |  |
| 14 | `RBI` | int | N |  |  |  |
| 15 | `SB` | int | N |  |  |  |
| 16 | `CS` | int | N |  |  |  |
| 17 | `SH` | int | N |  |  |  |
| 18 | `SF` | int | N |  |  |  |
| 19 | `BB` | int | N |  |  |  |
| 20 | `HP` | int | N |  |  |  |
| 21 | `KK` | int | N |  |  |  |
| 22 | `GD` | int | N |  |  |  |
| 23 | `ERR` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| IX_battotal | NONCLUSTERED | N | PCODE |
| PK_battotal_1 (PK) | CLUSTERED | Y | GYEAR, PCODE, SEC |

---

## DEFEN
- 행 수: **846,736**
- 컬럼 수: **12**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N |  |  |  |
| 2 | `GDAY` | int | N |  |  |  |
| 3 | `TB` | char(1) | Y |  |  |  |
| 4 | `ONETURN` | int | Y |  |  |  |
| 5 | `POSI` | varchar(5) | Y |  |  |  |
| 6 | `PCODE` | varchar(10) | Y |  |  |  |
| 7 | `PO` | smallint | Y |  | ((0)) |  |
| 8 | `ASS` | smallint | Y |  | ((0)) |  |
| 9 | `ERR` | smallint | Y |  | ((0)) |  |
| 10 | `DP` | smallint | Y |  | ((0)) |  |
| 11 | `PB` | smallint | Y |  | ((0)) |  |
| 12 | `INPUTTIME` | datetime | N |  |  |  |

---

## ENTRY
- 행 수: **854,280**
- 컬럼 수: **11**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TURN` | char(2) | N | PK |  |  |
| 4 | `NAME` | varchar(15) | N |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `TEAM` | char(1) | N |  |  |  |
| 7 | `POSI` | char(2) | N | PK |  |  |
| 8 | `CHIN` | varchar(2) | N |  |  |  |
| 9 | `CHTURN` | char(1) | N |  |  |  |
| 10 | `CHBCNT` | varchar(2) | N |  |  |  |
| 11 | `CHIN2` | char(1) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_ENTRY (PK) | NONCLUSTERED | Y | GMKEY, GDAY, TURN, PCODE, POSI |

---

## GAMECONTAPP
- 행 수: **2,531,702**
- 컬럼 수: **29**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `GDAY` | char(8) | N |  |  |  |
| 4 | `SERNO` | smallint | N | PK |  |  |
| 5 | `TURN` | char(2) | N |  |  |  |
| 6 | `INN` | tinyint | N |  |  |  |
| 7 | `TB` | char(1) | N |  |  |  |
| 8 | `INN2` | char(1) | Y |  |  |  |
| 9 | `OCOUNT` | char(1) | Y |  |  |  |
| 10 | `BCOUNT` | varchar(30) | Y |  |  |  |
| 11 | `RTURN` | char(2) | Y |  |  |  |
| 12 | `HOW` | char(2) | Y |  |  |  |
| 13 | `FIELD` | varchar(25) | Y |  |  |  |
| 14 | `PLACE` | char(1) | Y |  |  |  |
| 15 | `HITTER` | varchar(10) | Y |  |  |  |
| 16 | `HITNAME` | varchar(20) | Y |  |  |  |
| 17 | `PITNAME` | varchar(20) | Y |  |  |  |
| 18 | `PITCHER` | varchar(10) | Y |  |  |  |
| 19 | `CATNAME` | varchar(20) | Y |  |  |  |
| 20 | `CATCHER` | varchar(10) | Y |  |  |  |
| 21 | `BCNT` | char(3) | Y |  |  |  |
| 22 | `TSCORE` | smallint | Y |  |  |  |
| 23 | `BSCORE` | smallint | Y |  |  |  |
| 24 | `BASE1B` | char(2) | Y |  |  |  |
| 25 | `BASE2B` | char(2) | Y |  |  |  |
| 26 | `BASE3B` | char(2) | Y |  |  |  |
| 27 | `BASE1A` | char(2) | Y |  |  |  |
| 28 | `BASE2A` | char(2) | Y |  |  |  |
| 29 | `BASE3A` | char(2) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_GAMECONTAPP (PK) | NONCLUSTERED | Y | GMKEY, GYEAR, SERNO |

---

## GAMEINFO
- 행 수: **23,579**
- 컬럼 수: **27**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(15) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `DBHD` | char(10) | N |  |  |  |
| 4 | `STADIUM` | nvarchar(40) | Y |  |  |  |
| 5 | `VTEAM` | nvarchar(4) | N |  |  |  |
| 6 | `HTEAM` | nvarchar(4) | N |  |  |  |
| 7 | `STTM` | char(4) | Y |  |  |  |
| 8 | `ENTM` | nvarchar(8) | Y |  |  |  |
| 9 | `DLTM` | nvarchar(8) | Y |  |  |  |
| 10 | `GMTM` | nvarchar(8) | Y |  |  |  |
| 11 | `STAD` | nvarchar(16) | Y |  |  |  |
| 12 | `UMPC` | nvarchar(16) | Y |  |  |  |
| 13 | `UMP1` | nvarchar(16) | Y |  |  |  |
| 14 | `UMP2` | nvarchar(16) | Y |  |  |  |
| 15 | `UMP3` | nvarchar(16) | Y |  |  |  |
| 16 | `UMPL` | nvarchar(16) | Y |  |  |  |
| 17 | `UMPR` | nvarchar(16) | Y |  |  |  |
| 18 | `SCOA` | nvarchar(16) | Y |  |  |  |
| 19 | `SCOB` | nvarchar(16) | Y |  |  |  |
| 20 | `TEMP` | nvarchar(6) | Y |  |  |  |
| 21 | `MOIS` | nvarchar(6) | Y |  |  |  |
| 22 | `WEATH` | nvarchar(4) | Y |  |  |  |
| 23 | `WIND` | nvarchar(6) | Y |  |  |  |
| 24 | `WINS` | nvarchar(10) | Y |  |  |  |
| 25 | `GWEEK` | varchar(12) | Y |  |  |  |
| 26 | `CROWD` | int | Y |  |  |  |
| 27 | `CHAJUN` | char(10) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_GAMEINFO (PK) | NONCLUSTERED | Y | GMKEY, GDAY |

---

## GAME_HR
- 행 수: **7,784**
- 컬럼 수: **15**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | smallint | N | PK |  |  |
| 2 | `SR_ID` | smallint | N | PK |  |  |
| 3 | `SEASON_ID` | smallint | N |  |  |  |
| 4 | `G_ID` | char(13) | N | PK |  |  |
| 5 | `INN_NO` | tinyint | N |  |  |  |
| 6 | `TB_SC` | char(1) | N |  |  |  |
| 7 | `BAT_P_ID` | int | N |  |  |  |
| 8 | `PIT_P_ID` | int | N |  |  |  |
| 9 | `PLACE_SC` | char(1) | N |  |  |  |
| 10 | `HR_DISTANCE_VA` | smallint | N |  |  |  |
| 11 | `DIREC_SC` | varchar(10) | N |  |  |  |
| 12 | `SCORE_CN` | tinyint | N |  |  |  |
| 13 | `RECORD_DT` | varchar(5) | N |  |  |  |
| 14 | `SEQ_NO` | int | N | PK |  |  |
| 15 | `REG_DT` | datetime | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_GAME_HR_1 (PK) | CLUSTERED | Y | LE_ID, SR_ID, G_ID, SEQ_NO |

---

## GAME_MEMO
- 행 수: **54,544**
- 컬럼 수: **20**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | smallint | N | PK |  |  |
| 2 | `SR_ID` | smallint | N | PK |  |  |
| 3 | `SEASON_ID` | smallint | Y |  |  |  |
| 4 | `G_ID` | char(13) | N | PK |  |  |
| 5 | `INN_NO` | tinyint | N | PK |  |  |
| 6 | `BAT_ORDER_NO` | tinyint | N | PK |  |  |
| 7 | `BAT_AROUND_NO` | tinyint | N | PK |  |  |
| 8 | `TB_SC` | char(1) | N | PK |  |  |
| 9 | `PA_PIT_NO` | smallint | N | PK |  |  |
| 10 | `GAME_PIT_NO` | smallint | Y |  |  |  |
| 11 | `P_ID` | int | Y |  |  |  |
| 12 | `REQ_T_ID` | char(2) | Y |  |  |  |
| 13 | `START_TM` | varchar(5) | Y |  |  |  |
| 14 | `END_TM` | varchar(5) | Y |  |  |  |
| 15 | `USE_TM` | varchar(5) | Y |  |  |  |
| 16 | `FIRST_IF` | varchar(20) | Y |  |  |  |
| 17 | `LAST_IF` | varchar(20) | Y |  |  |  |
| 18 | `ETC_ME` | varchar(400) | Y |  |  |  |
| 19 | `ORDER_NO` | int | N | PK |  |  |
| 20 | `REG_DT` | datetime | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_GAME_MEMO_1 (PK) | CLUSTERED | Y | LE_ID, SR_ID, G_ID, INN_NO, BAT_ORDER_NO, BAT_AROUND_NO, TB_SC, PA_PIT_NO, ORDER_NO |

---

## GAME_MEMO_PITCHCLOCK
- 행 수: **237**
- 컬럼 수: **16**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | smallint | N | PK |  |  |
| 2 | `SR_ID` | smallint | N | PK |  |  |
| 3 | `SEASON_ID` | smallint | N |  |  |  |
| 4 | `G_ID` | char(13) | N | PK |  |  |
| 5 | `INN_NO` | tinyint | N |  |  |  |
| 6 | `BAT_ORDER_NO` | tinyint | N |  |  |  |
| 7 | `BAT_AROUND_NO` | tinyint | N |  |  |  |
| 8 | `TB_SC` | char(1) | N |  |  |  |
| 9 | `PA_PIT_NO` | smallint | N |  |  |  |
| 10 | `GAME_PIT_NO` | smallint | Y |  |  |  |
| 11 | `T_ID` | char(2) | Y |  |  |  |
| 12 | `P_ID` | int | Y |  |  |  |
| 13 | `PIT_RESULT_SC` | varchar(20) | Y |  |  |  |
| 14 | `ETC_ME` | varchar(400) | Y |  |  |  |
| 15 | `SEQ_NO` | int | N | PK |  |  |
| 16 | `REG_DT` | datetime | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_GAME_MEMO_PITCHCLOCK_2 (PK) | CLUSTERED | Y | LE_ID, SR_ID, G_ID, SEQ_NO |

---

## Hitter
- 행 수: **648,248**
- 컬럼 수: **26**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | nvarchar(15) | Y |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `TURN` | char(2) | Y |  |  |  |
| 7 | `ONETURN` | char(1) | Y |  |  |  |
| 8 | `PA` | int | N |  | (0) |  |
| 9 | `AB` | int | N |  | (0) |  |
| 10 | `RBI` | int | N |  | (0) |  |
| 11 | `RUN` | int | N |  | (0) |  |
| 12 | `HIT` | int | N |  | (0) |  |
| 13 | `H2` | int | N |  | (0) |  |
| 14 | `H3` | int | N |  | (0) |  |
| 15 | `HR` | int | N |  | (0) |  |
| 16 | `SB` | int | N |  | (0) |  |
| 17 | `CS` | int | N |  | (0) |  |
| 18 | `SH` | int | N |  | (0) |  |
| 19 | `SF` | int | N |  | (0) |  |
| 20 | `BB` | int | N |  | (0) |  |
| 21 | `IB` | int | N |  | (0) |  |
| 22 | `HP` | int | N |  | (0) |  |
| 23 | `KK` | int | N |  | (0) |  |
| 24 | `GD` | int | N |  | (0) |  |
| 25 | `ERR` | int | N |  | (0) |  |
| 26 | `LOB` | int | N |  | (0) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Hitter (PK) | CLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## PitTotal
- 행 수: **9,377**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `SEC` | varchar(4) | N | PK |  |  |
| 4 | `Team` | varchar(6) | Y |  |  |  |
| 5 | `ERA` | float | Y |  |  |  |
| 6 | `GAMENUM` | smallint | N |  |  |  |
| 7 | `CG` | smallint | N |  |  |  |
| 8 | `SHO` | smallint | N |  |  |  |
| 9 | `W` | smallint | N |  |  |  |
| 10 | `L` | smallint | N |  |  |  |
| 11 | `SV` | smallint | N |  |  |  |
| 12 | `Hold` | smallint | N |  |  |  |
| 13 | `BF` | smallint | N |  |  |  |
| 14 | `INN` | varchar(8) | N |  |  |  |
| 15 | `INN2` | smallint | N |  |  |  |
| 16 | `HIT` | smallint | N |  |  |  |
| 17 | `HR` | smallint | N |  |  |  |
| 18 | `BB` | smallint | N |  |  |  |
| 19 | `HP` | smallint | N |  |  |  |
| 20 | `KK` | smallint | N |  |  |  |
| 21 | `R` | smallint | N |  |  |  |
| 22 | `ER` | smallint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PitTotal (PK) | CLUSTERED | Y | GYEAR, PCODE, SEC |

---

## Pitcher
- 행 수: **223,624**
- 컬럼 수: **36**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | Y |  |  |  |
| 4 | `NAME` | varchar(20) | Y |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `POS` | varchar(10) | Y |  |  |  |
| 7 | `START` | char(1) | Y |  |  |  |
| 8 | `QUIT` | char(1) | Y |  |  |  |
| 9 | `CG` | int | N |  | (0) |  |
| 10 | `SHO` | int | N |  | (0) |  |
| 11 | `WLS` | char(1) | Y |  |  |  |
| 12 | `HOLD` | smallint | N |  | (0) |  |
| 13 | `INN` | varchar(10) | Y |  | (0) |  |
| 14 | `INN2` | int | N |  | (0) |  |
| 15 | `BF` | int | N |  | (0) |  |
| 16 | `PA` | int | N |  | (0) |  |
| 17 | `AB` | int | N |  | (0) |  |
| 18 | `HIT` | int | N |  | (0) |  |
| 19 | `H2` | int | N |  | (0) |  |
| 20 | `H3` | int | N |  | (0) |  |
| 21 | `HR` | int | N |  | (0) |  |
| 22 | `SB` | int | N |  | (0) |  |
| 23 | `CS` | int | N |  | (0) |  |
| 24 | `SH` | int | N |  | (0) |  |
| 25 | `SF` | int | N |  | (0) |  |
| 26 | `BB` | int | N |  | (0) |  |
| 27 | `IB` | int | N |  | (0) |  |
| 28 | `HP` | int | N |  | (0) |  |
| 29 | `KK` | int | N |  | (0) |  |
| 30 | `GD` | int | N |  | (0) |  |
| 31 | `WP` | int | N |  | (0) |  |
| 32 | `BK` | int | N |  | (0) |  |
| 33 | `ERR` | int | N |  | (0) |  |
| 34 | `R` | int | N |  | (0) |  |
| 35 | `ER` | int | N |  | (0) |  |
| 36 | `BS` | int | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Pitcher (PK) | CLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## Score
- 행 수: **23,579**
- 컬럼 수: **60**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `1T` | smallint | N |  | ((-1)) |  |
| 4 | `1B` | smallint | N |  | ((-1)) |  |
| 5 | `2T` | smallint | N |  | ((-1)) |  |
| 6 | `2B` | smallint | N |  | ((-1)) |  |
| 7 | `3T` | smallint | N |  | ((-1)) |  |
| 8 | `3B` | smallint | N |  | ((-1)) |  |
| 9 | `4T` | smallint | N |  | ((-1)) |  |
| 10 | `4B` | smallint | N |  | ((-1)) |  |
| 11 | `5T` | smallint | N |  | ((-1)) |  |
| 12 | `5B` | smallint | N |  | ((-1)) |  |
| 13 | `6T` | smallint | N |  | ((-1)) |  |
| 14 | `6B` | smallint | N |  | ((-1)) |  |
| 15 | `7T` | smallint | N |  | ((-1)) |  |
| 16 | `7B` | smallint | N |  | ((-1)) |  |
| 17 | `8T` | smallint | N |  | ((-1)) |  |
| 18 | `8B` | smallint | N |  | ((-1)) |  |
| 19 | `9T` | smallint | N |  | ((-1)) |  |
| 20 | `9B` | smallint | N |  | ((-1)) |  |
| 21 | `10T` | smallint | N |  | ((-1)) |  |
| 22 | `10B` | smallint | N |  | ((-1)) |  |
| 23 | `11T` | smallint | N |  | ((-1)) |  |
| 24 | `11B` | smallint | N |  | ((-1)) |  |
| 25 | `12T` | smallint | N |  | ((-1)) |  |
| 26 | `12B` | smallint | N |  | ((-1)) |  |
| 27 | `13T` | smallint | N |  | ((-1)) |  |
| 28 | `13B` | smallint | N |  | ((-1)) |  |
| 29 | `14T` | smallint | N |  | ((-1)) |  |
| 30 | `14B` | smallint | N |  | ((-1)) |  |
| 31 | `15T` | smallint | N |  | ((-1)) |  |
| 32 | `15B` | smallint | N |  | ((-1)) |  |
| 33 | `16T` | smallint | Y |  | ((-1)) |  |
| 34 | `16B` | smallint | Y |  | ((-1)) |  |
| 35 | `17T` | smallint | Y |  | ((-1)) |  |
| 36 | `17B` | smallint | Y |  | ((-1)) |  |
| 37 | `18T` | smallint | Y |  | ((-1)) |  |
| 38 | `18B` | smallint | Y |  |  |  |
| 39 | `19T` | smallint | Y |  | ((-1)) |  |
| 40 | `19B` | smallint | Y |  | ((-1)) |  |
| 41 | `20T` | smallint | Y |  | ((-1)) |  |
| 42 | `20B` | smallint | Y |  | ((-1)) |  |
| 43 | `21T` | smallint | Y |  | ((-1)) |  |
| 44 | `21B` | smallint | Y |  | ((-1)) |  |
| 45 | `22T` | smallint | Y |  | ((-1)) |  |
| 46 | `22B` | smallint | Y |  | ((-1)) |  |
| 47 | `23T` | smallint | Y |  | ((-1)) |  |
| 48 | `23B` | smallint | Y |  | ((-1)) |  |
| 49 | `24T` | smallint | Y |  | ((-1)) |  |
| 50 | `24B` | smallint | Y |  | ((-1)) |  |
| 51 | `25T` | smallint | Y |  | ((-1)) |  |
| 52 | `25B` | smallint | Y |  | ((-1)) |  |
| 53 | `TPOINT` | int | N |  | (0) |  |
| 54 | `BPOINT` | int | N |  | (0) |  |
| 55 | `THIT` | int | N |  | (0) |  |
| 56 | `BHIT` | int | N |  | (0) |  |
| 57 | `TERR` | int | N |  | (0) |  |
| 58 | `BERR` | int | N |  | (0) |  |
| 59 | `TBBHP` | int | N |  | (0) |  |
| 60 | `BBBHP` | int | N |  | (0) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Score_1 (PK) | CLUSTERED | Y | GMKEY, GDAY |

---

## TeamRank
- 행 수: **373**
- 컬럼 수: **30**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | nvarchar(4) | N | PK |  |  |
| 2 | `SEC` | varchar(4) | N | PK | ('') |  |
| 3 | `RANK` | int | Y |  |  |  |
| 4 | `LEAGUE` | char(5) | Y |  |  |  |
| 5 | `TEAM` | nvarchar(6) | N | PK |  |  |
| 6 | `GAME` | int | Y |  |  |  |
| 7 | `WIN` | int | Y |  |  |  |
| 8 | `LOSE` | int | Y |  |  |  |
| 9 | `SAME` | int | Y |  |  |  |
| 10 | `WRA` | real | Y |  |  |  |
| 11 | `AB` | int | Y |  |  |  |
| 12 | `HIT` | int | Y |  |  |  |
| 13 | `HR` | int | Y |  |  |  |
| 14 | `SB` | int | Y |  |  |  |
| 15 | `RUN` | int | Y |  |  |  |
| 16 | `INN` | varchar(10) | Y |  |  |  |
| 17 | `INN2` | int | Y |  |  |  |
| 18 | `R` | int | Y |  |  |  |
| 19 | `ER` | int | Y |  |  |  |
| 20 | `ERR` | int | Y |  |  |  |
| 21 | `HRA` | varchar(50) | Y |  |  |  |
| 22 | `LRA` | varchar(50) | Y |  |  |  |
| 23 | `BRA` | varchar(50) | Y |  |  |  |
| 24 | `ERA` | varchar(50) | Y |  |  |  |
| 25 | `continue` | varchar(50) | Y |  |  |  |
| 26 | `H2` | int | Y |  |  |  |
| 27 | `H3` | int | Y |  |  |  |
| 28 | `BB` | int | Y |  |  |  |
| 29 | `HP` | int | Y |  |  |  |
| 30 | `SF` | int | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_TeamRank_1 (PK) | CLUSTERED | Y | GYEAR, TEAM, SEC |

---
