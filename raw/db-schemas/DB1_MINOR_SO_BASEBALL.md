# DB1_MINOR_SO_BASEBALL 스키마

테이블 수: 9개

## 목차
1. [BATTOTAL](#battotal) (22컬럼, 1,946행)
2. [ENTRY](#entry) (12컬럼, 4,516행)
3. [GAMECONTAPP](#gamecontapp) (29컬럼, 13,309행)
4. [GAMEINFO](#gameinfo) (27컬럼, 124행)
5. [HITTER](#hitter) (26컬럼, 3,303행)
6. [PITCHER](#pitcher) (36컬럼, 1,265행)
7. [PITTOTAL](#pittotal) (21컬럼, 1,142행)
8. [SCORE](#score) (60컬럼, 124행)
9. [TEAMRANK](#teamrank) (29컬럼, 67행)

## BATTOTAL
- 행 수: **1,946**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `TEAM` | varchar(6) | Y |  |  |  |
| 4 | `HRA` | float | N |  |  |  |
| 5 | `GAMENUM` | int | N |  |  |  |
| 6 | `AB` | int | N |  |  |  |
| 7 | `RUN` | int | N |  |  |  |
| 8 | `HIT` | int | N |  |  |  |
| 9 | `H2` | int | N |  |  |  |
| 10 | `H3` | int | N |  |  |  |
| 11 | `HR` | int | N |  |  |  |
| 12 | `TB` | int | N |  |  |  |
| 13 | `RBI` | int | N |  |  |  |
| 14 | `SB` | int | N |  |  |  |
| 15 | `CS` | int | N |  |  |  |
| 16 | `SH` | int | N |  |  |  |
| 17 | `SF` | int | N |  |  |  |
| 18 | `BB` | int | N |  |  |  |
| 19 | `HP` | int | N |  |  |  |
| 20 | `KK` | int | N |  |  |  |
| 21 | `GD` | int | N |  |  |  |
| 22 | `ERR` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_BATTOTAL (PK) | NONCLUSTERED | Y | PCODE, GYEAR |

---

## ENTRY
- 행 수: **4,516**
- 컬럼 수: **12**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `GDAY` | char(8) | N |  |  |  |
| 4 | `TURN` | char(2) | N | PK |  |  |
| 5 | `NAME` | varchar(15) | N |  |  |  |
| 6 | `PCODE` | char(5) | N | PK |  |  |
| 7 | `TEAM` | char(1) | N |  |  |  |
| 8 | `POSI` | char(2) | N | PK |  |  |
| 9 | `CHIN` | varchar(2) | N |  |  |  |
| 10 | `CHTURN` | char(1) | N |  |  |  |
| 11 | `CHBCNT` | varchar(2) | N |  |  |  |
| 12 | `CHIN2` | char(1) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_ENTRY (PK) | NONCLUSTERED | Y | GMKEY, GYEAR, TURN, PCODE, POSI |

---

## GAMECONTAPP
- 행 수: **13,309**
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
- 행 수: **124**
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

## HITTER
- 행 수: **3,303**
- 컬럼 수: **26**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GMKEY` | char(13) | N | PK |  |  |
| 2 | `GDAY` | char(8) | N | PK |  |  |
| 3 | `TB` | char(1) | N |  |  |  |
| 4 | `NAME` | nvarchar(30) | Y |  |  |  |
| 5 | `PCODE` | varchar(10) | N | PK |  |  |
| 6 | `TURN` | char(2) | Y |  |  |  |
| 7 | `ONETURN` | char(1) | Y |  |  |  |
| 8 | `PA` | int | N |  |  |  |
| 9 | `AB` | int | N |  |  |  |
| 10 | `RBI` | int | N |  |  |  |
| 11 | `RUN` | int | N |  |  |  |
| 12 | `HIT` | int | N |  |  |  |
| 13 | `H2` | int | N |  |  |  |
| 14 | `H3` | int | N |  |  |  |
| 15 | `HR` | int | N |  |  |  |
| 16 | `SB` | int | N |  |  |  |
| 17 | `CS` | int | N |  |  |  |
| 18 | `SH` | int | N |  |  |  |
| 19 | `SF` | int | N |  |  |  |
| 20 | `BB` | int | N |  |  |  |
| 21 | `IB` | int | N |  |  |  |
| 22 | `HP` | int | N |  |  |  |
| 23 | `KK` | int | N |  |  |  |
| 24 | `GD` | int | N |  |  |  |
| 25 | `ERR` | int | N |  |  |  |
| 26 | `LOB` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_HITTER (PK) | NONCLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## PITCHER
- 행 수: **1,265**
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
| 9 | `CG` | int | N |  |  |  |
| 10 | `SHO` | int | N |  |  |  |
| 11 | `WLS` | char(1) | Y |  |  |  |
| 12 | `HOLD` | smallint | N |  |  |  |
| 13 | `INN` | varchar(10) | Y |  |  |  |
| 14 | `INN2` | int | N |  |  |  |
| 15 | `BF` | int | N |  |  |  |
| 16 | `PA` | int | N |  |  |  |
| 17 | `AB` | int | N |  |  |  |
| 18 | `HIT` | int | N |  |  |  |
| 19 | `H2` | int | N |  |  |  |
| 20 | `H3` | int | N |  |  |  |
| 21 | `HR` | int | N |  |  |  |
| 22 | `SB` | int | N |  |  |  |
| 23 | `CS` | int | N |  |  |  |
| 24 | `SH` | int | N |  |  |  |
| 25 | `SF` | int | N |  |  |  |
| 26 | `BB` | int | N |  |  |  |
| 27 | `IB` | int | N |  |  |  |
| 28 | `HP` | int | N |  |  |  |
| 29 | `KK` | int | N |  |  |  |
| 30 | `GD` | int | N |  |  |  |
| 31 | `WP` | int | N |  |  |  |
| 32 | `BK` | int | N |  |  |  |
| 33 | `ERR` | int | N |  |  |  |
| 34 | `R` | int | N |  |  |  |
| 35 | `ER` | int | N |  |  |  |
| 36 | `BS` | int | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PITCHER (PK) | NONCLUSTERED | Y | GMKEY, GDAY, PCODE |

---

## PITTOTAL
- 행 수: **1,142**
- 컬럼 수: **21**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `TEAM` | varchar(6) | Y |  |  |  |
| 4 | `ERA` | char(53) | Y |  |  |  |
| 5 | `GAMENUM` | int | N |  |  |  |
| 6 | `CG` | int | N |  |  |  |
| 7 | `SHO` | int | N |  |  |  |
| 8 | `W` | int | N |  |  |  |
| 9 | `L` | int | N |  |  |  |
| 10 | `SV` | int | N |  |  |  |
| 11 | `HOLD` | int | Y |  |  |  |
| 12 | `BF` | int | N |  |  |  |
| 13 | `INN` | varchar(15) | N |  |  |  |
| 14 | `INN2` | int | N |  |  |  |
| 15 | `HIT` | int | N |  |  |  |
| 16 | `HR` | int | N |  |  |  |
| 17 | `BB` | int | N |  |  |  |
| 18 | `HP` | int | N |  |  |  |
| 19 | `KK` | int | N |  |  |  |
| 20 | `R` | int | N |  |  |  |
| 21 | `ER` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PITTOTAL (PK) | NONCLUSTERED | Y | PCODE, GYEAR |

---

## SCORE
- 행 수: **124**
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
| 53 | `TPOINT` | int | N |  |  |  |
| 54 | `BPOINT` | int | N |  |  |  |
| 55 | `THIT` | int | N |  |  |  |
| 56 | `BHIT` | int | N |  |  |  |
| 57 | `TERR` | int | N |  |  |  |
| 58 | `BERR` | int | N |  |  |  |
| 59 | `TBBHP` | int | N |  |  |  |
| 60 | `BBBHP` | int | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_SCORE (PK) | NONCLUSTERED | Y | GMKEY, GDAY |

---

## TEAMRANK
- 행 수: **67**
- 컬럼 수: **29**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | nvarchar(8) | N | PK |  |  |
| 2 | `RANK` | int | Y |  |  |  |
| 3 | `LEAGUE` | char(5) | Y |  |  |  |
| 4 | `TEAM` | nvarchar(12) | N | PK |  |  |
| 5 | `GAME` | int | Y |  |  |  |
| 6 | `WIN` | int | Y |  |  |  |
| 7 | `LOSE` | int | Y |  |  |  |
| 8 | `SAME` | int | Y |  |  |  |
| 9 | `WRA` | real | Y |  |  |  |
| 10 | `AB` | int | Y |  |  |  |
| 11 | `HIT` | int | Y |  |  |  |
| 12 | `HR` | int | Y |  |  |  |
| 13 | `SB` | int | Y |  |  |  |
| 14 | `RUN` | int | Y |  |  |  |
| 15 | `INN` | varchar(10) | Y |  |  |  |
| 16 | `INN2` | int | Y |  |  |  |
| 17 | `R` | int | Y |  |  |  |
| 18 | `ER` | int | Y |  |  |  |
| 19 | `ERR` | int | Y |  |  |  |
| 20 | `HRA` | varchar(50) | Y |  |  |  |
| 21 | `LRA` | varchar(50) | Y |  |  |  |
| 22 | `BRA` | varchar(50) | Y |  |  |  |
| 23 | `ERA` | varchar(50) | Y |  |  |  |
| 24 | `CONTINUE` | varchar(50) | Y |  |  |  |
| 25 | `H2` | int | Y |  |  |  |
| 26 | `H3` | int | Y |  |  |  |
| 27 | `BB` | int | Y |  |  |  |
| 28 | `HP` | int | Y |  |  |  |
| 29 | `SF` | int | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_TEAMRANK (PK) | NONCLUSTERED | Y | GYEAR, TEAM |

---
