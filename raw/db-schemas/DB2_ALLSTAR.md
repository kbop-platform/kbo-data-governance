# DB2_ALLSTAR 스키마

테이블 수: 20개

## 목차
1. [BatTotal](#battotal) (22컬럼, 0행)
2. [ENTRY](#entry) (12컬럼, 2,560행)
3. [GAMECONTAPP](#gamecontapp) (29컬럼, 5,683행)
4. [GAMEINFO](#gameinfo) (27컬럼, 56행)
5. [Hitter](#hitter) (26컬럼, 1,713행)
6. [IE_BallCount](#ie_ballcount) (11컬럼, 25행)
7. [IE_BatterRecord](#ie_batterrecord) (25컬럼, 858행)
8. [IE_GAMESTATE](#ie_gamestate) (5컬럼, 25행)
9. [IE_GameList](#ie_gamelist) (6컬럼, 21행)
10. [IE_LiveText](#ie_livetext) (7컬럼, 11,461행)
11. [IE_PitcherRecord](#ie_pitcherrecord) (22컬럼, 379행)
12. [IE_ScoreRHEB](#ie_scorerheb) (7컬럼, 48행)
13. [IE_Scoreinning](#ie_scoreinning) (5컬럼, 418행)
14. [KBO_BATRESULT](#kbo_batresult) (90컬럼, 548행)
15. [KBO_ETCGAME](#kbo_etcgame) (5컬럼, 135행)
16. [KBO_PITRESULT](#kbo_pitresult) (23컬럼, 300행)
17. [PitTotal](#pittotal) (21컬럼, 0행)
18. [Pitcher](#pitcher) (36컬럼, 833행)
19. [Score](#score) (60컬럼, 56행)
20. [TeamRank](#teamrank) (29컬럼, 0행)

## BatTotal
- 행 수: **0**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  | b'\xec\x84\xa0\xec\x88\x98 ID' |
| 2 | `GYEAR` | char(4) | N | PK |  | b'\xec\x97\xb0\xeb\x8f\x84' |
| 3 | `TEAM` | varchar(6) | Y |  |  | b'\xed\x8c\x80' |
| 4 | `HRA` | float | Y |  | ((0)) | b'\xed\x83\x80\xec\x9c\xa8' |
| 5 | `GAMENUM` | smallint | N |  | ((0)) | b'\xea\xb2\xbd\xea\xb8\xb0\xec\x88\x98' |
| 6 | `AB` | smallint | N |  | ((0)) | b'\xed\x83\x80\xec\x88\x98' |
| 7 | `RUN` | smallint | N |  | ((0)) | b'\xeb\x93\x9d\xec\xa0\x90' |
| 8 | `HIT` | smallint | N |  | ((0)) | b'\xec\x95\x88\xed\x83\x80' |
| 9 | `H2` | smallint | N |  | ((0)) | b'2\xeb\xa3\xa8\xed\x83\x80' |
| 10 | `H3` | smallint | N |  | ((0)) | b'3\xeb\xa3\xa8\xed\x83\x80' |
| 11 | `HR` | smallint | N |  | ((0)) | b'\xed\x99\x88\xeb\x9f\xb0' |
| 12 | `TB` | smallint | N |  | ((0)) | b'\xeb\xa3\xa8\xed\x83\x80' |
| 13 | `RBI` | smallint | N |  | ((0)) | b'\xed\x83\x80\xec\xa0\x90' |
| 14 | `SB` | smallint | N |  | ((0)) | b'\xeb\x8f\x84\xeb\xa3\xa8' |
| 15 | `CS` | smallint | N |  | ((0)) | b'\xeb\x8f\x84\xeb\xa3\xa8\xec\x9e\x90' |
| 16 | `SH` | smallint | N |  | ((0)) | b'\xed\x9d\xac\xed\x83\x80' |
| 17 | `SF` | smallint | N |  | ((0)) | b'\xed\x9d\xac\xeb\xb9\x84' |
| 18 | `BB` | smallint | N |  | ((0)) | b'4\xea\xb5\xac' |
| 19 | `HP` | smallint | N |  | ((0)) | b'\xec\x82\xac\xea\xb5\xac' |
| 20 | `KK` | smallint | N |  | ((0)) | b'\xec\x82\xbc\xec\xa7\x84' |
| 21 | `GD` | smallint | N |  | ((0)) | b'\xeb\xb3\x91\xec\x82\xb4\xed\x83\x80' |
| 22 | `ERR` | smallint | N |  | ((0)) | b'\xec\x8b\xa4\xec\xb1\x85' |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_battotal (PK) | CLUSTERED | Y | GYEAR, PCODE |

---

## ENTRY
- 행 수: **2,560**
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
- 행 수: **5,683**
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
- 행 수: **56**
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

## Hitter
- 행 수: **1,713**
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

## IE_BallCount
- 행 수: **25**
- 컬럼 수: **11**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  | b'\xea\xb2\x8c\xec\x9e\x84\xec\xbd\x94\xeb\x93\x9c' |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `strike` | tinyint | N |  |  | b'\xed\x98\x84\xec\x9e\xac \xec\x8a\xa4\xed\x8a\xb8\xeb\x9d\xbc\xec\x9d\xb4\xed\x81\xac' |
| 4 | `ball` | tinyint | N |  |  | b'\xed\x98\x84\xec\x9e\xac \xeb\xb3\xbc' |
| 5 | `out` | tinyint | N |  |  | b'\xed\x98\x84\xec\x9e\xac \xec\x95\x84\xec\x9b\x83\xec\xb9\xb4\xec\x9a\xb4\xed\x8a\xb8' |
| 6 | `base1` | tinyint | N |  |  | b'\xed\x98\x84\xec\x9e\xac 1\xeb\xa3\xa8\xec\xa3\xbc\xec\x9e\x90 \xed\x83\x80\xec\x88\x9c' |
| 7 | `base2` | tinyint | N |  |  | b'\xed\x98\x84\xec\x9e\xac 2\xeb\xa3\xa8\xec\xa3\xbc\xec\x9e\x90 \xed\x83\x80\xec\x88\x9c' |
| 8 | `base3` | tinyint | N |  |  | b'\xed\x98\x84\xec\x9e\xac 3\xeb\xa3\xa8\xec\xa3\xbc\xec\x9e\x90 \xed\x83\x80\xec\x88\x9c' |
| 9 | `pitcher` | varchar(10) | N |  |  | b'\xed\x98\x84\xec\x9e\xac \xed\x88\xac\xec\x88\x98' |
| 10 | `batter` | varchar(10) | N |  |  | b'\xed\x98\x84\xec\x9e\xac \xed\x83\x80\xec\x9e\x90' |
| 11 | `batResult` | varchar(50) | N |  | ('-') | b'\xed\x98\x84\xec\x9e\xac\xed\x83\x80\xec\x9e\x90 \xec\x98\xa4\xeb\x8a\x98\xec\x9d\x98 \xec\x84\xb1\xec\xa0\x81' |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_BallCount (PK) | CLUSTERED | Y | gameID, GYEAR |

---

## IE_BatterRecord
- 행 수: **858**
- 컬럼 수: **25**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `BatOrder` | tinyint | N | PK |  |  |
| 4 | `Position` | tinyint | N |  |  |  |
| 5 | `PositionName` | varchar(20) | N |  |  |  |
| 6 | `PlayerName` | varchar(15) | N |  |  |  |
| 7 | `PlayerID` | varchar(10) | N | PK |  |  |
| 8 | `SeqNO` | tinyint | N | PK |  |  |
| 9 | `OAB` | tinyint | N |  |  |  |
| 10 | `Run` | tinyint | N |  |  |  |
| 11 | `H1` | tinyint | N |  |  |  |
| 12 | `H2` | tinyint | N |  |  |  |
| 13 | `H3` | tinyint | N |  |  |  |
| 14 | `HR` | tinyint | N |  |  |  |
| 15 | `RBI` | tinyint | N |  |  |  |
| 16 | `Steal` | tinyint | N |  |  |  |
| 17 | `CS` | tinyint | N |  |  |  |
| 18 | `SH` | tinyint | N |  |  |  |
| 19 | `SF` | tinyint | N |  |  |  |
| 20 | `BB` | tinyint | N |  |  |  |
| 21 | `HBP` | tinyint | N |  |  |  |
| 22 | `SO` | tinyint | N |  |  |  |
| 23 | `DP` | tinyint | N |  |  |  |
| 24 | `TP` | tinyint | N |  |  |  |
| 25 | `bHome` | tinyint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_BatterRecord (PK) | CLUSTERED | Y | gameID, GYEAR, BatOrder, PlayerID, SeqNO |

---

## IE_GAMESTATE
- 행 수: **25**
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
| PK_IE_GAMESTATE (PK) | CLUSTERED | Y | GAMEID, GYEAR |

---

## IE_GameList
- 행 수: **21**
- 컬럼 수: **6**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `HomeName` | varchar(8) | N |  |  |  |
| 4 | `HomeMascot` | varchar(20) | N |  |  |  |
| 5 | `VisitName` | varchar(8) | N |  |  |  |
| 6 | `VisitMascot` | varchar(20) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_GameList (PK) | CLUSTERED | Y | gameID, GYEAR |

---

## IE_LiveText
- 행 수: **11,461**
- 컬럼 수: **7**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `LiveText` | varchar(200) | N |  |  |  |
| 4 | `SeqNO` | smallint | N | PK |  |  |
| 5 | `Inning` | tinyint | N |  |  |  |
| 6 | `bTop` | tinyint | N |  |  |  |
| 7 | `textStyle` | tinyint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_LiveText (PK) | CLUSTERED | Y | gameID, GYEAR, SeqNO |

---

## IE_PitcherRecord
- 행 수: **379**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `PlayerName` | varchar(15) | N |  |  |  |
| 4 | `PlayerID` | varchar(10) | N | PK |  |  |
| 5 | `SeqNO` | tinyint | N |  |  |  |
| 6 | `Inning` | varchar(5) | N |  |  |  |
| 7 | `PA` | tinyint | N |  |  |  |
| 8 | `PitchBallCnt` | tinyint | N |  |  |  |
| 9 | `PitchStrikeCnt` | tinyint | N |  |  |  |
| 10 | `OAB` | tinyint | N |  |  |  |
| 11 | `Run` | tinyint | N |  |  |  |
| 12 | `Hit` | tinyint | N |  |  |  |
| 13 | `HR` | tinyint | N |  |  |  |
| 14 | `SH` | tinyint | N |  |  |  |
| 15 | `SF` | tinyint | N |  |  |  |
| 16 | `BB` | tinyint | N |  |  |  |
| 17 | `HBP` | tinyint | N |  |  |  |
| 18 | `SO` | tinyint | N |  |  |  |
| 19 | `BK` | tinyint | N |  |  |  |
| 20 | `WP` | tinyint | N |  |  |  |
| 21 | `ER` | tinyint | N |  |  |  |
| 22 | `bHome` | tinyint | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_PitcherRecord (PK) | CLUSTERED | Y | gameID, GYEAR, PlayerID |

---

## IE_ScoreRHEB
- 행 수: **48**
- 컬럼 수: **7**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `Run` | tinyint | N |  |  |  |
| 4 | `Hit` | tinyint | N |  |  |  |
| 5 | `Error` | tinyint | N |  |  |  |
| 6 | `BallFour` | tinyint | N |  |  |  |
| 7 | `bHome` | tinyint | N | PK |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_ScoreRHEB (PK) | CLUSTERED | Y | gameID, GYEAR, bHome |

---

## IE_Scoreinning
- 행 수: **418**
- 컬럼 수: **5**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | N | PK |  |  |
| 2 | `GYEAR` | smallint | N | PK |  |  |
| 3 | `inning` | tinyint | N | PK |  |  |
| 4 | `Score` | tinyint | N |  |  |  |
| 5 | `bHome` | tinyint | N | PK |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_IE_Scoreinning (PK) | CLUSTERED | Y | gameID, GYEAR, inning, bHome |

---

## KBO_BATRESULT
- 행 수: **548**
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
- 행 수: **135**
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
- 행 수: **300**
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

## PitTotal
- 행 수: **0**
- 컬럼 수: **21**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `PCODE` | varchar(10) | N | PK |  |  |
| 2 | `GYEAR` | char(4) | N | PK |  |  |
| 3 | `Team` | varchar(6) | Y |  |  |  |
| 4 | `ERA` | float | Y |  | ((0)) |  |
| 5 | `GAMENUM` | smallint | N |  | ((0)) |  |
| 6 | `CG` | smallint | N |  | ((0)) |  |
| 7 | `SHO` | smallint | N |  | ((0)) |  |
| 8 | `W` | smallint | N |  | ((0)) |  |
| 9 | `L` | smallint | N |  | ((0)) |  |
| 10 | `SV` | smallint | N |  | ((0)) |  |
| 11 | `Hold` | smallint | N |  | ((0)) |  |
| 12 | `BF` | smallint | N |  | ((0)) |  |
| 13 | `INN` | varchar(8) | N |  | ((0)) |  |
| 14 | `INN2` | smallint | N |  | ((0)) |  |
| 15 | `HIT` | smallint | N |  | ((0)) |  |
| 16 | `HR` | smallint | N |  | ((0)) |  |
| 17 | `BB` | smallint | N |  | ((0)) |  |
| 18 | `HP` | smallint | N |  | ((0)) |  |
| 19 | `KK` | smallint | N |  | ((0)) |  |
| 20 | `R` | smallint | N |  | ((0)) |  |
| 21 | `ER` | smallint | N |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_PitTotal (PK) | CLUSTERED | Y | GYEAR, PCODE |

---

## Pitcher
- 행 수: **833**
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
- 행 수: **56**
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
| 53 | `TPOINT` | smallint | N |  | ((0)) |  |
| 54 | `BPOINT` | smallint | N |  | ((0)) |  |
| 55 | `THIT` | smallint | N |  | ((0)) |  |
| 56 | `BHIT` | smallint | N |  | ((0)) |  |
| 57 | `TERR` | smallint | N |  | ((0)) |  |
| 58 | `BERR` | smallint | N |  | ((0)) |  |
| 59 | `TBBHP` | smallint | Y |  | ((0)) |  |
| 60 | `BBBHP` | smallint | Y |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_Score (PK) | CLUSTERED | Y | GMKEY, GDAY |

---

## TeamRank
- 행 수: **0**
- 컬럼 수: **29**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | char(4) | N | PK |  | b'\xec\x97\xb0\xeb\x8f\x84' |
| 2 | `RANK` | tinyint | N |  | ((0)) | b'\xec\x88\x9c\xec\x9c\x84' |
| 3 | `LEAGUE` | varchar(5) | Y |  |  | b'\xeb\xa6\xac\xea\xb7\xb8' |
| 4 | `TEAM` | nvarchar(6) | N | PK |  | b'\xed\x8c\x80' |
| 5 | `GAME` | tinyint | N |  | ((0)) | b'\xea\xb2\xbd\xea\xb8\xb0\xec\x88\x98' |
| 6 | `WIN` | smallint | N |  | ((0)) | b'\xec\x8a\xb9\xeb\xa6\xac' |
| 7 | `LOSE` | smallint | N |  | ((0)) | b'\xed\x8c\xa8\xec\xa0\x84' |
| 8 | `SAME` | tinyint | N |  | ((0)) | b'\xeb\xac\xb4\xec\x8a\xb9\xeb\xb6\x80' |
| 9 | `WRA` | decimal(4,3) | N |  | ((0)) | b'\xec\x8a\xb9\xeb\xa5\xa0' |
| 10 | `AB` | smallint | N |  | ((0)) | b'\xed\x83\x80\xec\x88\x98' |
| 11 | `HIT` | smallint | N |  | ((0)) | b'\xec\x95\x88\xed\x83\x80' |
| 12 | `HR` | smallint | N |  | ((0)) | b'\xed\x99\x88\xeb\x9f\xb0' |
| 13 | `SB` | smallint | N |  | ((0)) | b'\xeb\x8f\x84\xeb\xa3\xa8' |
| 14 | `RUN` | smallint | N |  | ((0)) | b'\xeb\x93\x9d\xec\xa0\x90' |
| 15 | `INN` | varchar(8) | N |  | ('0') | b'\xec\x9d\xb4\xeb\x8b\x9d' |
| 16 | `INN2` | smallint | N |  | ((0)) | b'\xec\x9d\xb4\xeb\x8b\x9d*3' |
| 17 | `R` | smallint | N |  | ((0)) | b'\xec\x8b\xa4\xec\xa0\x90' |
| 18 | `ER` | smallint | N |  | ((0)) | b'\xec\x9e\x90\xec\xb1\x85\xec\xa0\x90' |
| 19 | `ERR` | smallint | N |  | ((0)) | b'\xec\x8b\xa4\xec\xb1\x85' |
| 20 | `HRA` | varchar(5) | N |  | ('0') | b'\xed\x83\x80\xec\x9c\xa8' |
| 21 | `LRA` | varchar(5) | N |  | ('0') | b'\xec\x9e\xa5\xed\x83\x80\xec\x9c\xa8' |
| 22 | `BRA` | varchar(5) | N |  | ('0') | b'\xec\xb6\x9c\xeb\xa3\xa8\xec\x9c\xa8' |
| 23 | `ERA` | varchar(5) | N |  | ('0') | b'\xeb\xb0\xa9\xec\x96\xb4\xec\x9c\xa8' |
| 24 | `continue` | varchar(4) | Y |  |  | b'\xec\x97\xb0\xec\x86\x8d' |
| 25 | `H2` | smallint | N |  | ((0)) | b'2\xeb\xa3\xa8\xed\x83\x80' |
| 26 | `H3` | smallint | N |  | ((0)) | b'3\xeb\xa3\xa8\xed\x83\x80' |
| 27 | `BB` | smallint | N |  | ((0)) | b'4\xea\xb5\xac' |
| 28 | `HP` | smallint | N |  | ((0)) | b'\xec\x82\xac\xea\xb5\xac' |
| 29 | `SF` | smallint | N |  | ((0)) | b'\xed\x9d\xac\xec\x83\x9d\xed\x94\x8c\xeb\x9d\xbc\xec\x9d\xb4' |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_TeamRank (PK) | CLUSTERED | Y | GYEAR, TEAM |

---
