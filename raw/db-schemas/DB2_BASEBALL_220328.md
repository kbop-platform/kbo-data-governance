# DB2_BASEBALL_220328 스키마

테이블 수: 18개

## 목차
1. [BatTotal](#battotal) (23컬럼, 796행)
2. [DEFEN](#defen) (12컬럼, 28,243행)
3. [ENTRY](#entry) (12컬럼, 28,058행)
4. [GAMECONTAPP](#gamecontapp) (29컬럼, 77,280행)
5. [GAMEINFO](#gameinfo) (27컬럼, 720행)
6. [GAMEINFO_WEATHER](#gameinfo_weather) (12컬럼, 1,680행)
7. [GAME_HR](#game_hr) (15컬럼, 1,280행)
8. [GAME_MEMO](#game_memo) (20컬럼, 23,978행)
9. [GAME_MEMO_PITCHCLOCK](#game_memo_pitchclock) (16컬럼, 237행)
10. [Hitter](#hitter) (26컬럼, 19,946행)
11. [KBO_BATRESULT](#kbo_batresult) (90컬럼, 424,921행)
12. [KBO_ETCGAME](#kbo_etcgame) (5컬럼, 122,762행)
13. [KBO_PITRESULT](#kbo_pitresult) (23컬럼, 134,292행)
14. [PITCHCLOCK](#pitchclock) (19컬럼, 215행)
15. [PitTotal](#pittotal) (22컬럼, 562행)
16. [Pitcher](#pitcher) (36컬럼, 8,466행)
17. [Score](#score) (60컬럼, 720행)
18. [TeamRank](#teamrank) (30컬럼, 10행)

## BatTotal
- 행 수: **796**
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
| PK_battotal_2 (PK) | CLUSTERED | Y | GYEAR, PCODE, SEC |

---

## DEFEN
- 행 수: **28,243**
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
- 행 수: **28,058**
- 컬럼 수: **12**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `GDAY` | char(8) | Y |  |  |  |
| 4 | `TURN` | char(2) | N | PK |  |  |
| 5 | `NAME` | varchar(15) | Y |  |  |  |
| 6 | `PCODE` | varchar(10) | N | PK |  |  |
| 7 | `TEAM` | char(1) | Y |  |  |  |
| 8 | `POSI` | char(2) | N | PK |  |  |
| 9 | `CHIN` | int | Y |  |  |  |
| 10 | `CHTURN` | nvarchar(20) | Y |  |  |  |
| 11 | `CHBCNT` | int | Y |  |  |  |
| 12 | `CHIN2` | nvarchar(20) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_ENTRY (PK) | NONCLUSTERED | Y | GMKEY, GYEAR, TURN, PCODE, POSI |

---

## GAMECONTAPP
- 행 수: **77,280**
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
- 행 수: **720**
- 컬럼 수: **27**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `DBHD` | varchar(10) | N |  |  |  |
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

## GAMEINFO_WEATHER
- 행 수: **1,680**
- 컬럼 수: **12**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `code` | varchar(10) | N | PK |  |  |
| 2 | `area_wide` | nvarchar(10) | Y |  |  |  |
| 3 | `area_city` | nvarchar(10) | Y |  |  |  |
| 4 | `area_dong` | nvarchar(10) | Y |  |  |  |
| 5 | `tm` | varchar(10) | N | PK |  |  |
| 6 | `icon40` | nvarchar(10) | Y |  |  |  |
| 7 | `temp` | nvarchar(10) | Y |  |  |  |
| 8 | `humi` | nvarchar(10) | Y |  |  |  |
| 9 | `rain` | nvarchar(10) | Y |  |  |  |
| 10 | `snow` | nvarchar(10) | Y |  |  |  |
| 11 | `wdirk` | nvarchar(10) | Y |  |  |  |
| 12 | `wspeed` | nvarchar(10) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK__GAMEINFO__865C72FCB5B8C679 (PK) | CLUSTERED | Y | code, tm |

---

## GAME_HR
- 행 수: **1,280**
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
| PK_GAME_HR_2 (PK) | CLUSTERED | Y | LE_ID, SR_ID, G_ID, SEQ_NO |

---

## GAME_MEMO
- 행 수: **23,978**
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
| PK_GAME_MEMO_2 (PK) | CLUSTERED | Y | LE_ID, SR_ID, G_ID, INN_NO, BAT_ORDER_NO, BAT_AROUND_NO, TB_SC, PA_PIT_NO, ORDER_NO |

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
- 행 수: **19,946**
- 컬럼 수: **26**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | varchar(16) | N |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `TURN` | varchar(2) | Y |  |  |  |
| 7 | `ONETURN` | varchar(1) | Y |  |  |  |
| 8 | `PA` | smallint | N |  | ((0)) |  |
| 9 | `AB` | smallint | N |  | ((0)) |  |
| 10 | `RBI` | smallint | N |  | ((0)) |  |
| 11 | `RUN` | smallint | N |  | ((0)) |  |
| 12 | `HIT` | smallint | N |  | ((0)) |  |
| 13 | `H2` | smallint | N |  | ((0)) |  |
| 14 | `H3` | smallint | N |  | ((0)) |  |
| 15 | `HR` | smallint | N |  | ((0)) |  |
| 16 | `SB` | smallint | N |  | ((0)) |  |
| 17 | `CS` | smallint | N |  | ((0)) |  |
| 18 | `SH` | smallint | N |  | ((0)) |  |
| 19 | `SF` | smallint | N |  | ((0)) |  |
| 20 | `BB` | smallint | N |  | ((0)) |  |
| 21 | `IB` | smallint | N |  | ((0)) |  |
| 22 | `HP` | smallint | N |  | ((0)) |  |
| 23 | `KK` | smallint | N |  | ((0)) |  |
| 24 | `GD` | smallint | N |  | ((0)) |  |
| 25 | `ERR` | smallint | N |  | ((0)) |  |
| 26 | `LOB` | smallint | N |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Hitter (PK) | CLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## KBO_BATRESULT
- 행 수: **424,921**
- 컬럼 수: **90**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | varchar(16) | N |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `TURN` | char(2) | N |  | ('') |  |
| 7 | `ONETURN` | char(1) | N |  | ('') |  |
| 8 | `POSITION` | varchar(10) | N |  | ('') |  |
| 9 | `CHANGEINN` | varchar(2) | N |  | ('') |  |
| 10 | `INN1` | varchar(10) | N |  | ('') |  |
| 11 | `IL1` | varchar(10) | N |  | ('') |  |
| 12 | `INN1_3` | varchar(10) | N |  | ('') |  |
| 13 | `INN2` | varchar(10) | N |  | ('') |  |
| 14 | `IL2` | varchar(10) | N |  | ('') |  |
| 15 | `INN2_3` | varchar(10) | N |  | ('') |  |
| 16 | `INN3` | varchar(10) | N |  | ('') |  |
| 17 | `IL3` | varchar(10) | N |  | ('') |  |
| 18 | `INN3_3` | varchar(10) | N |  | ('') |  |
| 19 | `INN4` | varchar(10) | N |  | ('') |  |
| 20 | `IL4` | varchar(10) | N |  | ('') |  |
| 21 | `INN4_3` | varchar(10) | N |  | ('') |  |
| 22 | `INN5` | varchar(10) | N |  | ('') |  |
| 23 | `IL5` | varchar(10) | N |  | ('') |  |
| 24 | `INN5_3` | varchar(10) | N |  | ('') |  |
| 25 | `INN6` | varchar(10) | N |  | ('') |  |
| 26 | `IL6` | varchar(10) | N |  | ('') |  |
| 27 | `INN6_3` | varchar(10) | N |  | ('') |  |
| 28 | `INN7` | varchar(10) | N |  | ('') |  |
| 29 | `IL7` | varchar(10) | N |  | ('') |  |
| 30 | `INN7_3` | varchar(10) | N |  | ('') |  |
| 31 | `INN8` | varchar(10) | N |  | ('') |  |
| 32 | `IL8` | varchar(10) | N |  | ('') |  |
| 33 | `INN8_3` | varchar(10) | N |  | ('') |  |
| 34 | `INN9` | varchar(10) | N |  | ('') |  |
| 35 | `IL9` | varchar(10) | N |  | ('') |  |
| 36 | `INN9_3` | varchar(10) | N |  | ('') |  |
| 37 | `INN10` | varchar(10) | N |  | ('') |  |
| 38 | `IL10` | varchar(10) | N |  | ('') |  |
| 39 | `INN10_3` | varchar(10) | N |  | ('') |  |
| 40 | `INN11` | varchar(10) | N |  | ('') |  |
| 41 | `IL11` | varchar(10) | N |  | ('') |  |
| 42 | `INN11_3` | varchar(10) | N |  | ('') |  |
| 43 | `INN12` | varchar(10) | N |  | ('') |  |
| 44 | `IL12` | varchar(10) | N |  | ('') |  |
| 45 | `INN12_3` | varchar(10) | N |  | ('') |  |
| 46 | `INN13` | varchar(10) | N |  | ('') |  |
| 47 | `IL13` | varchar(10) | N |  | ('') |  |
| 48 | `INN13_3` | varchar(10) | N |  | ('') |  |
| 49 | `INN14` | varchar(10) | N |  | ('') |  |
| 50 | `IL14` | varchar(10) | N |  | ('') |  |
| 51 | `INN14_3` | varchar(10) | N |  | ('') |  |
| 52 | `INN15` | varchar(10) | N |  | ('') |  |
| 53 | `IL15` | varchar(10) | N |  | ('') |  |
| 54 | `INN15_3` | varchar(10) | N |  | ('') |  |
| 55 | `INN16` | varchar(10) | N |  | ('') |  |
| 56 | `IL16` | varchar(10) | N |  | ('') |  |
| 57 | `INN16_3` | varchar(10) | N |  | ('') |  |
| 58 | `INN17` | varchar(10) | N |  | ('') |  |
| 59 | `IL17` | varchar(10) | N |  | ('') |  |
| 60 | `INN17_3` | varchar(10) | N |  | ('') |  |
| 61 | `INN18` | varchar(10) | N |  | ('') |  |
| 62 | `IL18` | varchar(10) | N |  | ('') |  |
| 63 | `INN18_3` | varchar(10) | N |  | ('') |  |
| 64 | `INN19` | varchar(10) | N |  | ('') |  |
| 65 | `IL19` | varchar(10) | N |  | ('') |  |
| 66 | `INN19_3` | varchar(10) | N |  | ('') |  |
| 67 | `INN20` | varchar(10) | N |  | ('') |  |
| 68 | `IL20` | varchar(10) | N |  | ('') |  |
| 69 | `INN20_3` | varchar(10) | N |  | ('') |  |
| 70 | `INN21` | varchar(10) | N |  | ('') |  |
| 71 | `IL21` | varchar(10) | N |  | ('') |  |
| 72 | `INN21_3` | varchar(10) | N |  | ('') |  |
| 73 | `INN22` | varchar(10) | N |  | ('') |  |
| 74 | `IL22` | varchar(10) | N |  | ('') |  |
| 75 | `INN22_3` | varchar(10) | N |  | ('') |  |
| 76 | `INN23` | varchar(10) | N |  | ('') |  |
| 77 | `IL23` | varchar(10) | N |  | ('') |  |
| 78 | `INN23_3` | varchar(10) | N |  | ('') |  |
| 79 | `INN24` | varchar(10) | N |  | ('') |  |
| 80 | `IL24` | varchar(10) | N |  | ('') |  |
| 81 | `INN24_3` | varchar(10) | N |  | ('') |  |
| 82 | `INN25` | varchar(10) | N |  | ('') |  |
| 83 | `IL25` | varchar(10) | N |  | ('') |  |
| 84 | `INN25_3` | varchar(10) | N |  | ('') |  |
| 85 | `AB` | tinyint | N |  |  |  |
| 86 | `RUN` | tinyint | N |  |  |  |
| 87 | `HIT` | tinyint | N |  |  |  |
| 88 | `RBI` | tinyint | N |  |  |  |
| 89 | `AVGS` | varchar(5) | N |  |  |  |
| 90 | `AVG5` | varchar(5) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK__KBO_BatRESULT__008190C9 (PK) | CLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## KBO_ETCGAME
- 행 수: **122,762**
- 컬럼 수: **5**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `SEQ` | tinyint | N | PK |  |  |
| 4 | `HOW` | varchar(16) | N |  |  |  |
| 5 | `RESULT` | varchar(255) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK__KBO_ETCGAME__045221AD (PK) | CLUSTERED | Y | GMKEY, GDAY, SEQ |

---

## KBO_PITRESULT
- 행 수: **134,292**
- 컬럼 수: **23**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | varchar(16) | N |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `POS` | char(2) | N |  |  |  |
| 7 | `WLS` | varchar(1) | N |  |  |  |
| 8 | `CHANGEINN` | varchar(4) | N |  |  |  |
| 9 | `GAME` | tinyint | N |  |  |  |
| 10 | `W` | tinyint | N |  |  |  |
| 11 | `L` | tinyint | N |  |  |  |
| 12 | `S` | tinyint | N |  |  |  |
| 13 | `INN` | varchar(5) | N |  |  |  |
| 14 | `PA` | tinyint | N |  |  |  |
| 15 | `BF` | tinyint | N |  |  |  |
| 16 | `AB` | tinyint | N |  |  |  |
| 17 | `HIT` | tinyint | N |  |  |  |
| 18 | `HR` | tinyint | N |  |  |  |
| 19 | `BBHP` | tinyint | N |  |  |  |
| 20 | `KK` | tinyint | N |  |  |  |
| 21 | `R` | tinyint | N |  |  |  |
| 22 | `ER` | tinyint | N |  |  |  |
| 23 | `ERA` | varchar(6) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK__KBO_PitRESULT__0269D93B (PK) | CLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## PITCHCLOCK
- 행 수: **215**
- 컬럼 수: **19**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `GDAY` | char(8) | N | PK |  |  |
| 4 | `STADIUM` | nvarchar(40) | Y |  |  |  |
| 5 | `VTEAM` | nvarchar(4) | N |  |  |  |
| 6 | `HTEAM` | nvarchar(4) | N |  |  |  |
| 7 | `HITNAME` | varchar(15) | Y |  |  |  |
| 8 | `HITTER` | varchar(15) | Y |  |  |  |
| 9 | `PITNAME` | varchar(15) | Y |  |  |  |
| 10 | `PITCHER` | varchar(15) | Y |  |  |  |
| 11 | `CATNAME` | varchar(15) | Y |  |  |  |
| 12 | `CATCHER` | varchar(15) | Y |  |  |  |
| 13 | `TEAM` | nvarchar(4) | N |  |  |  |
| 14 | `NAME` | varchar(15) | Y |  |  |  |
| 15 | `PCODE` | varchar(15) | Y |  |  |  |
| 16 | `PITCHCLOCK` | varchar(15) | Y |  |  |  |
| 17 | `LIVETEXT` | varchar(200) | N | PK |  |  |
| 18 | `RUNNER` | varchar(10) | Y |  |  |  |
| 19 | `DETAIL` | varchar(20) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PITCHCLOCK (PK) | CLUSTERED | Y | GMKEY, GYEAR, GDAY, LIVETEXT |

---

## PitTotal
- 행 수: **562**
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
| IX_pitTotal | NONCLUSTERED | N | PCODE |
| PK_PitTotal_2 (PK) | CLUSTERED | Y | GYEAR, PCODE, SEC |

---

## Pitcher
- 행 수: **8,466**
- 컬럼 수: **36**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | varchar(16) | N |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `POS` | varchar(2) | Y |  |  |  |
| 7 | `START` | varchar(1) | Y |  |  |  |
| 8 | `QUIT` | varchar(1) | Y |  |  |  |
| 9 | `CG` | smallint | N |  | ((0)) |  |
| 10 | `SHO` | smallint | N |  | ((0)) |  |
| 11 | `WLS` | varchar(1) | N |  |  |  |
| 12 | `HOLD` | smallint | N |  | ((0)) |  |
| 13 | `INN` | varchar(6) | N |  |  |  |
| 14 | `INN2` | smallint | N |  | ((0)) |  |
| 15 | `BF` | smallint | N |  | ((0)) |  |
| 16 | `PA` | smallint | N |  | ((0)) |  |
| 17 | `AB` | smallint | N |  | ((0)) |  |
| 18 | `HIT` | smallint | N |  | ((0)) |  |
| 19 | `H2` | smallint | N |  | ((0)) |  |
| 20 | `H3` | smallint | N |  | ((0)) |  |
| 21 | `HR` | smallint | N |  | ((0)) |  |
| 22 | `SB` | smallint | N |  | ((0)) |  |
| 23 | `CS` | smallint | N |  | ((0)) |  |
| 24 | `SH` | smallint | N |  | ((0)) |  |
| 25 | `SF` | smallint | N |  | ((0)) |  |
| 26 | `BB` | smallint | N |  | ((0)) |  |
| 27 | `IB` | smallint | N |  | ((0)) |  |
| 28 | `HP` | smallint | N |  | ((0)) |  |
| 29 | `KK` | smallint | N |  | ((0)) |  |
| 30 | `GD` | smallint | N |  | ((0)) |  |
| 31 | `WP` | smallint | N |  | ((0)) |  |
| 32 | `BK` | smallint | N |  | ((0)) |  |
| 33 | `ERR` | smallint | N |  | ((0)) |  |
| 34 | `R` | smallint | N |  | ((0)) |  |
| 35 | `ER` | smallint | N |  | ((0)) |  |
| 36 | `BS` | smallint | Y |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Pitcher_1 (PK) | CLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## Score
- 행 수: **720**
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
| 38 | `18B` | smallint | Y |  | ((-1)) |  |
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
| 53 | `TPOINT` | smallint | N |  | (0) |  |
| 54 | `BPOINT` | smallint | N |  | (0) |  |
| 55 | `THIT` | smallint | N |  | (0) |  |
| 56 | `BHIT` | smallint | N |  | (0) |  |
| 57 | `TERR` | smallint | N |  | (0) |  |
| 58 | `BERR` | smallint | N |  | (0) |  |
| 59 | `TBBHP` | smallint | N |  | (0) |  |
| 60 | `BBBHP` | smallint | N |  | (0) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Score (PK) | CLUSTERED | Y | GMKEY, GDAY |

---

## TeamRank
- 행 수: **10**
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
| PK_TeamRank_2 (PK) | CLUSTERED | Y | GYEAR, TEAM, SEC |

---
