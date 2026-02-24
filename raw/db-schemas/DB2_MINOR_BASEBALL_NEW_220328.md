# DB2_MINOR_BASEBALL_NEW_220328 스키마

테이블 수: 8개

## 목차
1. [IE_BALLCOUNT](#ie_ballcount) (11컬럼, 8,651행)
2. [IE_BATTERRECORD](#ie_batterrecord) (25컬럼, 263,107행)
3. [IE_GAMELIST](#ie_gamelist) (6컬럼, 8,362행)
4. [IE_GAMESTATE](#ie_gamestate) (5컬럼, 6,978행)
5. [IE_LIVETEXT](#ie_livetext) (7컬럼, 4,506,413행)
6. [IE_PITCHERRECORD](#ie_pitcherrecord) (22컬럼, 75,646행)
7. [IE_SCOREINNING](#ie_scoreinning) (5컬럼, 147,846행)
8. [IE_SCORERHEB](#ie_scorerheb) (7컬럼, 17,302행)

## IE_BALLCOUNT
- 행 수: **8,651**
- 컬럼 수: **11**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `STRIKE` | tinyint | Y |  |  |  |
| 4 | `BALL` | tinyint | Y |  |  |  |
| 5 | `OUT` | tinyint | Y |  |  |  |
| 6 | `BASE1` | tinyint | Y |  |  |  |
| 7 | `BASE2` | tinyint | Y |  |  |  |
| 8 | `BASE3` | tinyint | Y |  |  |  |
| 9 | `PITCHER` | varchar(10) | Y |  |  |  |
| 10 | `BATTER` | varchar(10) | Y |  |  |  |
| 11 | `BATRESULT` | varchar(50) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_BALLCOUNT (PK) | NONCLUSTERED | Y | GAMEID, GYEAR |

---

## IE_BATTERRECORD
- 행 수: **263,107**
- 컬럼 수: **25**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `BATORDER` | tinyint | N | PK | ((0)) |  |
| 4 | `POSITION` | tinyint | N |  |  |  |
| 5 | `POSITIONNAME` | varchar(20) | N |  |  |  |
| 6 | `PLAYERNAME` | varchar(15) | N |  |  |  |
| 7 | `PLAYERID` | varchar(10) | N | PK |  |  |
| 8 | `SEQNO` | tinyint | N | PK | ((0)) |  |
| 9 | `OAB` | tinyint | N |  |  |  |
| 10 | `RUN` | tinyint | N |  |  |  |
| 11 | `H1` | tinyint | N |  |  |  |
| 12 | `H2` | tinyint | N |  |  |  |
| 13 | `H3` | tinyint | N |  |  |  |
| 14 | `HR` | tinyint | N |  |  |  |
| 15 | `RBI` | tinyint | N |  |  |  |
| 16 | `STEAL` | tinyint | N |  |  |  |
| 17 | `CS` | tinyint | N |  |  |  |
| 18 | `SH` | tinyint | N |  |  |  |
| 19 | `SF` | tinyint | N |  |  |  |
| 20 | `BB` | tinyint | N |  |  |  |
| 21 | `HBP` | tinyint | N |  |  |  |
| 22 | `SO` | tinyint | N |  |  |  |
| 23 | `DP` | tinyint | N |  |  |  |
| 24 | `TP` | tinyint | N |  |  |  |
| 25 | `BHOME` | tinyint | N |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_BATTERRECORD (PK) | NONCLUSTERED | Y | GAMEID, GYEAR, BATORDER, PLAYERID, SEQNO |

---

## IE_GAMELIST
- 행 수: **8,362**
- 컬럼 수: **6**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `HOMENAME` | varchar(8) | N |  |  |  |
| 4 | `HOMEMASCOT` | varchar(20) | N |  |  |  |
| 5 | `VISITNAME` | varchar(8) | N |  |  |  |
| 6 | `VISITMASCOT` | varchar(20) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_GAMELIST (PK) | NONCLUSTERED | Y | GAMEID, GYEAR |

---

## IE_GAMESTATE
- 행 수: **6,978**
- 컬럼 수: **5**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `STATUS_ID` | tinyint | N |  |  |  |
| 4 | `INN_NO` | tinyint | N |  |  |  |
| 5 | `TB_SC` | char(1) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_GAMESTATE (PK) | NONCLUSTERED | Y | GAMEID, GYEAR |

---

## IE_LIVETEXT
- 행 수: **4,506,413**
- 컬럼 수: **7**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `LIVETEXT` | varchar(200) | Y |  |  |  |
| 4 | `SEQNO` | smallint | N | PK | ((0)) |  |
| 5 | `INNING` | tinyint | Y |  |  |  |
| 6 | `BTOP` | tinyint | Y |  |  |  |
| 7 | `TEXTSTYLE` | tinyint | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_LIVETEXT (PK) | NONCLUSTERED | Y | GAMEID, GYEAR, SEQNO |

---

## IE_PITCHERRECORD
- 행 수: **75,646**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `PLAYERNAME` | varchar(15) | N |  |  |  |
| 4 | `PLAYERID` | varchar(10) | N | PK |  |  |
| 5 | `SEQNO` | tinyint | N |  |  |  |
| 6 | `INNING` | varchar(5) | N |  |  |  |
| 7 | `PA` | tinyint | N |  |  |  |
| 8 | `PITCHBALLCNT` | tinyint | N |  |  |  |
| 9 | `PITCHSTRIKECNT` | tinyint | N |  |  |  |
| 10 | `OAB` | tinyint | N |  |  |  |
| 11 | `RUN` | tinyint | N |  |  |  |
| 12 | `HIT` | tinyint | N |  |  |  |
| 13 | `HR` | tinyint | N |  |  |  |
| 14 | `SH` | tinyint | N |  |  |  |
| 15 | `SF` | tinyint | N |  |  |  |
| 16 | `BB` | tinyint | N |  |  |  |
| 17 | `HBP` | tinyint | N |  |  |  |
| 18 | `SO` | tinyint | N |  |  |  |
| 19 | `BK` | tinyint | N |  |  |  |
| 20 | `WP` | tinyint | N |  |  |  |
| 21 | `ER` | tinyint | N |  |  |  |
| 22 | `BHOME` | tinyint | N |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_PITCHERRECORD (PK) | NONCLUSTERED | Y | GAMEID, GYEAR, PLAYERID |

---

## IE_SCOREINNING
- 행 수: **147,846**
- 컬럼 수: **5**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `INNING` | tinyint | N | PK |  |  |
| 4 | `SCORE` | tinyint | N |  |  |  |
| 5 | `BHOME` | tinyint | N | PK |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_SCOREINNING (PK) | NONCLUSTERED | Y | GAMEID, GYEAR, INNING, BHOME |

---

## IE_SCORERHEB
- 행 수: **17,302**
- 컬럼 수: **7**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GAMEID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `RUN` | tinyint | N |  |  |  |
| 4 | `HIT` | tinyint | N |  |  |  |
| 5 | `ERROR` | tinyint | N |  |  |  |
| 6 | `BALLFOUR` | tinyint | N |  |  |  |
| 7 | `BHOME` | tinyint | N | PK | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_SCORERHEB (PK) | NONCLUSTERED | Y | GAMEID, GYEAR, BHOME |

---
