# DB2_MINOR_SO_BASEBALL 스키마

테이블 수: 15개

## 목차
1. [BATTOTAL](#battotal) (22컬럼, 144행)
2. [ENTRY](#entry) (12컬럼, 346행)
3. [GAMECONTAPP](#gamecontapp) (29컬럼, 954행)
4. [GAMEINFO](#gameinfo) (27컬럼, 9행)
5. [HITTER](#hitter) (26컬럼, 246행)
6. [KBO_BATRESULT](#kbo_batresult) (65컬럼, 3,303행)
7. [KBO_ETCGAME](#kbo_etcgame) (5컬럼, 1,119행)
8. [KBO_PITRESULT](#kbo_pitresult) (23컬럼, 1,099행)
9. [KBO_SCHEDULE](#kbo_schedule) (15컬럼, 146행)
10. [PERSON](#person) (16컬럼, 8,249행)
11. [PITCHER](#pitcher) (36컬럼, 103행)
12. [PITTOTAL](#pittotal) (21컬럼, 116행)
13. [SCORE](#score) (60컬럼, 9행)
14. [TEAM](#team) (7컬럼, 178행)
15. [TEAMRANK](#teamrank) (29컬럼, 4행)

## BATTOTAL
- 행 수: **144**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `TEAM` | varchar(6) | Y |  |  |  |
| 4 | `HRA` | float | Y |  |  |  |
| 5 | `GAMENUM` | smallint | N |  |  |  |
| 6 | `AB` | smallint | N |  |  |  |
| 7 | `RUN` | smallint | N |  |  |  |
| 8 | `HIT` | smallint | N |  |  |  |
| 9 | `H2` | smallint | N |  |  |  |
| 10 | `H3` | smallint | N |  |  |  |
| 11 | `HR` | smallint | N |  |  |  |
| 12 | `TB` | smallint | N |  |  |  |
| 13 | `RBI` | smallint | N |  |  |  |
| 14 | `SB` | smallint | N |  |  |  |
| 15 | `CS` | smallint | N |  |  |  |
| 16 | `SH` | smallint | N |  |  |  |
| 17 | `SF` | smallint | N |  |  |  |
| 18 | `BB` | smallint | N |  |  |  |
| 19 | `HP` | smallint | N |  |  |  |
| 20 | `KK` | smallint | N |  |  |  |
| 21 | `GD` | smallint | N |  |  |  |
| 22 | `ERR` | smallint | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_BATTOTAL (PK) | NONCLUSTERED | Y | PCODE, GYEAR |

---

## ENTRY
- 행 수: **346**
- 컬럼 수: **12**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `GDAY` | char(8) | Y |  |  |  |
| 4 | `TURN` | char(2) | N | PK |  |  |
| 5 | `NAME` | varchar(15) | Y |  |  |  |
| 6 | `PCODE` | varchar(5) | N | PK |  |  |
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
- 행 수: **954**
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
- 행 수: **9**
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
| 22 | `WEATH` | nvarchar(8) | Y |  |  |  |
| 23 | `WIND` | nvarchar(6) | Y |  |  |  |
| 24 | `WINS` | nvarchar(10) | Y |  |  |  |
| 25 | `GWEEK` | varchar(12) | Y |  |  |  |
| 26 | `CROWD` | int | Y |  |  |  |
| 27 | `CHAJUN` | varchar(10) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_GAMEINFO (PK) | NONCLUSTERED | Y | GMKEY, GDAY |

---

## HITTER
- 행 수: **246**
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
| 8 | `PA` | smallint | N |  |  |  |
| 9 | `AB` | smallint | N |  |  |  |
| 10 | `RBI` | smallint | N |  |  |  |
| 11 | `RUN` | smallint | N |  |  |  |
| 12 | `HIT` | smallint | N |  |  |  |
| 13 | `H2` | smallint | N |  |  |  |
| 14 | `H3` | smallint | N |  |  |  |
| 15 | `HR` | smallint | N |  |  |  |
| 16 | `SB` | smallint | N |  |  |  |
| 17 | `CS` | smallint | N |  |  |  |
| 18 | `SH` | smallint | N |  |  |  |
| 19 | `SF` | smallint | N |  |  |  |
| 20 | `BB` | smallint | N |  |  |  |
| 21 | `IB` | smallint | N |  |  |  |
| 22 | `HP` | smallint | N |  |  |  |
| 23 | `KK` | smallint | N |  |  |  |
| 24 | `GD` | smallint | N |  |  |  |
| 25 | `ERR` | smallint | N |  |  |  |
| 26 | `LOB` | smallint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_HITTER (PK) | NONCLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## KBO_BATRESULT
- 행 수: **3,303**
- 컬럼 수: **65**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | varchar(16) | N |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `TURN` | char(2) | N |  |  |  |
| 7 | `ONETURN` | char(1) | N |  |  |  |
| 8 | `POSITION` | varchar(10) | N |  |  |  |
| 9 | `CHANGEINN` | char(2) | N |  |  |  |
| 10 | `INN1` | varchar(10) | N |  |  |  |
| 11 | `IL1` | varchar(10) | N |  |  |  |
| 12 | `INN2` | varchar(10) | N |  |  |  |
| 13 | `IL2` | varchar(10) | N |  |  |  |
| 14 | `INN3` | varchar(10) | N |  |  |  |
| 15 | `IL3` | varchar(10) | N |  |  |  |
| 16 | `INN4` | varchar(10) | N |  |  |  |
| 17 | `IL4` | varchar(10) | N |  |  |  |
| 18 | `INN5` | varchar(10) | N |  |  |  |
| 19 | `IL5` | varchar(10) | N |  |  |  |
| 20 | `INN6` | varchar(10) | N |  |  |  |
| 21 | `IL6` | varchar(10) | N |  |  |  |
| 22 | `INN7` | varchar(10) | N |  |  |  |
| 23 | `IL7` | varchar(10) | N |  |  |  |
| 24 | `INN8` | varchar(10) | N |  |  |  |
| 25 | `IL8` | varchar(10) | N |  |  |  |
| 26 | `INN9` | varchar(10) | N |  |  |  |
| 27 | `IL9` | varchar(10) | N |  |  |  |
| 28 | `INN10` | varchar(10) | N |  |  |  |
| 29 | `IL10` | varchar(10) | N |  |  |  |
| 30 | `INN11` | varchar(10) | N |  |  |  |
| 31 | `IL11` | varchar(10) | N |  |  |  |
| 32 | `INN12` | varchar(10) | N |  |  |  |
| 33 | `IL12` | varchar(10) | N |  |  |  |
| 34 | `INN13` | varchar(10) | N |  |  |  |
| 35 | `IL13` | varchar(10) | N |  |  |  |
| 36 | `INN14` | varchar(10) | N |  |  |  |
| 37 | `IL14` | varchar(10) | N |  |  |  |
| 38 | `INN15` | varchar(10) | N |  |  |  |
| 39 | `IL15` | varchar(10) | N |  |  |  |
| 40 | `INN16` | varchar(10) | N |  |  |  |
| 41 | `IL16` | varchar(10) | N |  |  |  |
| 42 | `INN17` | varchar(10) | N |  |  |  |
| 43 | `IL17` | varchar(10) | N |  |  |  |
| 44 | `INN18` | varchar(10) | N |  |  |  |
| 45 | `IL18` | varchar(10) | N |  |  |  |
| 46 | `INN19` | varchar(10) | N |  |  |  |
| 47 | `IL19` | varchar(10) | N |  |  |  |
| 48 | `INN20` | varchar(10) | N |  |  |  |
| 49 | `IL20` | varchar(10) | N |  |  |  |
| 50 | `INN21` | varchar(10) | N |  |  |  |
| 51 | `IL21` | varchar(10) | N |  |  |  |
| 52 | `INN22` | varchar(10) | N |  |  |  |
| 53 | `IL22` | varchar(10) | N |  |  |  |
| 54 | `INN23` | varchar(10) | N |  |  |  |
| 55 | `IL23` | varchar(10) | N |  |  |  |
| 56 | `INN24` | varchar(10) | N |  |  |  |
| 57 | `IL24` | varchar(10) | N |  |  |  |
| 58 | `INN25` | varchar(10) | N |  |  |  |
| 59 | `IL25` | varchar(10) | N |  |  |  |
| 60 | `AB` | tinyint | N |  |  |  |
| 61 | `RUN` | tinyint | N |  |  |  |
| 62 | `HIT` | tinyint | N |  |  |  |
| 63 | `RBI` | tinyint | N |  |  |  |
| 64 | `AVGS` | varchar(5) | N |  |  |  |
| 65 | `AVG5` | varchar(5) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_KBO_BATRESULT (PK) | NONCLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## KBO_ETCGAME
- 행 수: **1,119**
- 컬럼 수: **5**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `SEQ` | tinyint | N | PK | ((0)) |  |
| 4 | `HOW` | varchar(16) | N |  |  |  |
| 5 | `RESULT` | varchar(255) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_KBO_ETCGAME (PK) | NONCLUSTERED | Y | GMKEY, GDAY, SEQ |

---

## KBO_PITRESULT
- 행 수: **1,099**
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
| PK_KBO_PITRESULT (PK) | NONCLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## KBO_SCHEDULE
- 행 수: **146**
- 컬럼 수: **15**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GAME_FLAG` | char(1) | N |  |  |  |
| 4 | `GAMEDATE` | varchar(8) | N | PK |  |  |
| 5 | `GYEAR` | char(4) | N |  |  |  |
| 6 | `GMONTH` | char(2) | N |  |  |  |
| 7 | `GDAY` | char(2) | N |  |  |  |
| 8 | `GWEEK` | varchar(2) | N |  |  |  |
| 9 | `HOME` | varchar(10) | N |  |  |  |
| 10 | `HOME_KEY` | char(2) | N |  |  |  |
| 11 | `VISIT` | varchar(10) | N |  |  |  |
| 12 | `VISIT_KEY` | char(2) | N |  |  |  |
| 13 | `STADIUM` | varchar(10) | N |  |  |  |
| 15 | `DHEADER` | char(1) | N |  |  |  |
| 18 | `GTIME` | char(5) | N |  |  |  |
| 21 | `CANCEL_FLAG` | bit | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_KBO_SCHEDULE (PK) | NONCLUSTERED | Y | GMKEY, GAMEDATE |

---

## PERSON
- 행 수: **8,249**
- 컬럼 수: **16**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | smallint | N | PK |  |  |
| 2 | `PCODE` | varchar(10) | N | PK |  |  |
| 3 | `NAME` | varchar(20) | N |  |  |  |
| 4 | `TEAM` | varchar(8) | N |  |  |  |
| 5 | `POS` | char(1) | Y |  |  |  |
| 6 | `POSITION` | varchar(4) | Y |  |  |  |
| 7 | `BACKNUM` | varchar(50) | Y |  |  |  |
| 8 | `CNAME` | varchar(30) | Y |  |  |  |
| 9 | `HITTYPE` | varchar(8) | Y |  |  |  |
| 10 | `BIRTH` | varchar(8) | Y |  |  |  |
| 11 | `HEIGHT` | varchar(3) | Y |  |  |  |
| 12 | `WEIGHT` | varchar(3) | Y |  |  |  |
| 13 | `INDATE` | varchar(8) | Y |  |  |  |
| 14 | `PROMISE` | varchar(12) | Y |  |  |  |
| 15 | `MONEY` | varchar(12) | Y |  |  |  |
| 16 | `CAREER` | varchar(255) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PERSON (PK) | NONCLUSTERED | Y | GYEAR, PCODE |

---

## PITCHER
- 행 수: **103**
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
| 9 | `CG` | smallint | N |  |  |  |
| 10 | `SHO` | smallint | N |  |  |  |
| 11 | `WLS` | varchar(1) | N |  |  |  |
| 12 | `HOLD` | smallint | N |  |  |  |
| 13 | `INN` | varchar(6) | N |  |  |  |
| 14 | `INN2` | smallint | N |  |  |  |
| 15 | `BF` | smallint | N |  |  |  |
| 16 | `PA` | smallint | N |  |  |  |
| 17 | `AB` | smallint | N |  |  |  |
| 18 | `HIT` | smallint | N |  |  |  |
| 19 | `H2` | smallint | N |  |  |  |
| 20 | `H3` | smallint | N |  |  |  |
| 21 | `HR` | smallint | N |  |  |  |
| 22 | `SB` | smallint | N |  |  |  |
| 23 | `CS` | smallint | N |  |  |  |
| 24 | `SH` | smallint | N |  |  |  |
| 25 | `SF` | smallint | N |  |  |  |
| 26 | `BB` | smallint | N |  |  |  |
| 27 | `IB` | smallint | N |  |  |  |
| 28 | `HP` | smallint | N |  |  |  |
| 29 | `KK` | smallint | N |  |  |  |
| 30 | `GD` | smallint | N |  |  |  |
| 31 | `WP` | smallint | N |  |  |  |
| 32 | `BK` | smallint | N |  |  |  |
| 33 | `ERR` | smallint | N |  |  |  |
| 34 | `R` | smallint | N |  |  |  |
| 35 | `ER` | smallint | N |  |  |  |
| 36 | `BS` | smallint | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PITCHER (PK) | NONCLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## PITTOTAL
- 행 수: **116**
- 컬럼 수: **21**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `TEAM` | varchar(6) | Y |  |  |  |
| 4 | `ERA` | float | N |  |  |  |
| 5 | `GAMENUM` | smallint | N |  |  |  |
| 6 | `CG` | smallint | N |  |  |  |
| 7 | `SHO` | smallint | N |  |  |  |
| 8 | `W` | smallint | N |  |  |  |
| 9 | `L` | smallint | N |  |  |  |
| 10 | `SV` | smallint | N |  |  |  |
| 11 | `HOLD` | smallint | N |  |  |  |
| 12 | `BF` | smallint | N |  |  |  |
| 13 | `INN` | varchar(8) | N |  |  |  |
| 14 | `INN2` | smallint | N |  |  |  |
| 15 | `HIT` | smallint | N |  |  |  |
| 16 | `HR` | smallint | N |  |  |  |
| 17 | `BB` | smallint | N |  |  |  |
| 18 | `HP` | smallint | N |  |  |  |
| 19 | `KK` | smallint | N |  |  |  |
| 20 | `R` | smallint | N |  |  |  |
| 21 | `ER` | smallint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PITTOTAL (PK) | NONCLUSTERED | Y | PCODE, GYEAR |

---

## SCORE
- 행 수: **9**
- 컬럼 수: **60**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `1T` | smallint | N |  |  |  |
| 4 | `1B` | smallint | N |  |  |  |
| 5 | `2T` | smallint | N |  |  |  |
| 6 | `2B` | smallint | N |  |  |  |
| 7 | `3T` | smallint | N |  |  |  |
| 8 | `3B` | smallint | N |  |  |  |
| 9 | `4T` | smallint | N |  |  |  |
| 10 | `4B` | smallint | N |  |  |  |
| 11 | `5T` | smallint | N |  |  |  |
| 12 | `5B` | smallint | N |  |  |  |
| 13 | `6T` | smallint | N |  |  |  |
| 14 | `6B` | smallint | N |  |  |  |
| 15 | `7T` | smallint | N |  |  |  |
| 16 | `7B` | smallint | N |  |  |  |
| 17 | `8T` | smallint | N |  |  |  |
| 18 | `8B` | smallint | N |  |  |  |
| 19 | `9T` | smallint | N |  |  |  |
| 20 | `9B` | smallint | N |  |  |  |
| 21 | `10T` | smallint | N |  |  |  |
| 22 | `10B` | smallint | N |  |  |  |
| 23 | `11T` | smallint | N |  |  |  |
| 24 | `11B` | smallint | N |  |  |  |
| 25 | `12T` | smallint | N |  |  |  |
| 26 | `12B` | smallint | N |  |  |  |
| 27 | `13T` | smallint | N |  |  |  |
| 28 | `13B` | smallint | N |  |  |  |
| 29 | `14T` | smallint | N |  |  |  |
| 30 | `14B` | smallint | N |  |  |  |
| 31 | `15T` | smallint | N |  |  |  |
| 32 | `15B` | smallint | N |  |  |  |
| 33 | `16T` | smallint | Y |  |  |  |
| 34 | `16B` | smallint | Y |  |  |  |
| 35 | `17T` | smallint | Y |  |  |  |
| 36 | `17B` | smallint | Y |  |  |  |
| 37 | `18T` | smallint | Y |  |  |  |
| 38 | `18B` | smallint | Y |  |  |  |
| 39 | `19T` | smallint | Y |  |  |  |
| 40 | `19B` | smallint | Y |  |  |  |
| 41 | `20T` | smallint | Y |  |  |  |
| 42 | `20B` | smallint | Y |  |  |  |
| 43 | `21T` | smallint | Y |  |  |  |
| 44 | `21B` | smallint | Y |  |  |  |
| 45 | `22T` | smallint | Y |  |  |  |
| 46 | `22B` | smallint | Y |  |  |  |
| 47 | `23T` | smallint | Y |  |  |  |
| 48 | `23B` | smallint | Y |  |  |  |
| 49 | `24T` | smallint | Y |  |  |  |
| 50 | `24B` | smallint | Y |  |  |  |
| 51 | `25T` | smallint | Y |  |  |  |
| 52 | `25B` | smallint | Y |  |  |  |
| 53 | `TPOINT` | smallint | N |  |  |  |
| 54 | `BPOINT` | smallint | N |  |  |  |
| 55 | `THIT` | smallint | N |  |  |  |
| 56 | `BHIT` | smallint | N |  |  |  |
| 57 | `TERR` | smallint | N |  |  |  |
| 58 | `BERR` | smallint | N |  |  |  |
| 59 | `TBBHP` | smallint | N |  |  |  |
| 60 | `BBBHP` | smallint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_SCORE (PK) | NONCLUSTERED | Y | GMKEY, GDAY |

---

## TEAM
- 행 수: **178**
- 컬럼 수: **7**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `SEASON_ID` | smallint | N | PK |  |  |
| 2 | `T_ID` | char(2) | N | PK |  |  |
| 3 | `FIRST_NM` | varchar(50) | N |  |  |  |
| 4 | `LAST_NM` | varchar(50) | Y |  |  |  |
| 5 | `FIRST_ENG_NM` | varchar(50) | Y |  |  |  |
| 6 | `LAST_ENG_NM` | varchar(50) | Y |  |  |  |
| 7 | `GROUP_SC` | varchar(10) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_TEAM (PK) | NONCLUSTERED | Y | SEASON_ID, T_ID |

---

## TEAMRANK
- 행 수: **4**
- 컬럼 수: **29**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | char(4) | N | PK |  |  |
| 2 | `RANK` | tinyint | N |  |  |  |
| 3 | `LEAGUE` | varchar(5) | Y |  |  |  |
| 4 | `TEAM` | nvarchar(12) | N | PK |  |  |
| 5 | `GAME` | tinyint | N |  |  |  |
| 6 | `WIN` | smallint | N |  |  |  |
| 7 | `LOSE` | smallint | N |  |  |  |
| 8 | `SAME` | tinyint | N |  |  |  |
| 9 | `WRA` | decimal(4,3) | N |  |  |  |
| 10 | `AB` | smallint | N |  |  |  |
| 11 | `HIT` | smallint | N |  |  |  |
| 12 | `HR` | smallint | N |  |  |  |
| 13 | `SB` | smallint | N |  |  |  |
| 14 | `RUN` | smallint | N |  |  |  |
| 15 | `INN` | varchar(8) | N |  |  |  |
| 16 | `INN2` | smallint | N |  |  |  |
| 17 | `R` | smallint | N |  |  |  |
| 18 | `ER` | smallint | N |  |  |  |
| 19 | `ERR` | smallint | N |  |  |  |
| 20 | `HRA` | varchar(5) | N |  |  |  |
| 21 | `LRA` | varchar(5) | N |  |  |  |
| 22 | `BRA` | varchar(5) | N |  |  |  |
| 23 | `ERA` | varchar(5) | N |  |  |  |
| 24 | `CONTINUE` | varchar(4) | Y |  |  |  |
| 25 | `H2` | smallint | N |  |  |  |
| 26 | `H3` | smallint | N |  |  |  |
| 27 | `BB` | smallint | N |  |  |  |
| 28 | `HP` | smallint | N |  |  |  |
| 29 | `SF` | smallint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_TEAMRANK (PK) | NONCLUSTERED | Y | GYEAR, TEAM |

---
