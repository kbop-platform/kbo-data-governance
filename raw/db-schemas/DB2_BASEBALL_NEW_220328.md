# DB2_BASEBALL_NEW_220328 스키마

테이블 수: 15개

## 목차
1. [CANCEL_GAME](#cancel_game) (6컬럼, 1,290행)
2. [IE_BallCount](#ie_ballcount) (11컬럼, 15,482행)
3. [IE_BatterRecord](#ie_batterrecord) (25컬럼, 451,166행)
4. [IE_GAMESTATE](#ie_gamestate) (5컬럼, 15,237행)
5. [IE_GameList](#ie_gamelist) (6컬럼, 15,908행)
6. [IE_LiveText](#ie_livetext) (7컬럼, 8,005,079행)
7. [IE_PitcherRecord](#ie_pitcherrecord) (22컬럼, 134,388행)
8. [IE_ScoreRHEB](#ie_scorerheb) (7컬럼, 30,860행)
9. [IE_Scoreinning](#ie_scoreinning) (5컬럼, 267,166행)
10. [IE_log](#ie_log) (3컬럼, 785,406행)
11. [KBO_schedule](#kbo_schedule) (22컬럼, 27,340행)
12. [PERSON_FA](#person_fa) (4컬럼, 228행)
13. [STADIUM](#stadium) (3컬럼, 487행)
14. [person](#person) (20컬럼, 100,812행)
15. [person2](#person2) (17컬럼, 91,891행)

## CANCEL_GAME
- 행 수: **1,290**
- 컬럼 수: **6**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `LE_ID` | smallint | N | PK |  |  |
| 2 | `SR_ID` | smallint | N | PK |  |  |
| 3 | `SEASON_ID` | smallint | N |  |  |  |
| 4 | `G_ID` | char(13) | N | PK |  |  |
| 5 | `CANCEL_SC_NM` | varchar(20) | Y |  |  |  |
| 6 | `REG_DT` | datetime | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_CANCEL_GAME_1 (PK) | CLUSTERED | Y | LE_ID, SR_ID, G_ID |

---

## IE_BallCount
- 행 수: **15,482**
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
- 행 수: **451,166**
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
- 행 수: **15,237**
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
- 행 수: **15,908**
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
- 행 수: **8,005,079**
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
- 행 수: **134,388**
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
- 행 수: **30,860**
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
- 행 수: **267,166**
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

## IE_log
- 행 수: **785,406**
- 컬럼 수: **3**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gameID` | char(13) | Y |  |  |  |
| 2 | `SeqNO` | smallint | Y |  |  |  |
| 3 | `InsertedTime` | datetime | Y |  |  |  |

---

## KBO_schedule
- 행 수: **27,340**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gmkey` | char(13) | N | PK |  |  |
| 2 | `game_flag` | char(1) | Y |  |  |  |
| 3 | `end_flag` | char(1) | N |  |  |  |
| 4 | `gamedate` | varchar(8) | N | PK |  |  |
| 5 | `gyear` | char(4) | N |  |  |  |
| 6 | `gmonth` | char(2) | N |  |  |  |
| 7 | `gday` | char(2) | N |  |  |  |
| 8 | `gweek` | varchar(2) | N |  |  |  |
| 9 | `home` | varchar(10) | N |  |  |  |
| 10 | `home_key` | char(2) | N |  |  |  |
| 11 | `visit` | varchar(10) | N |  |  |  |
| 12 | `visit_key` | char(2) | N |  |  |  |
| 13 | `stadium` | varchar(10) | N |  |  |  |
| 14 | `stadium_key` | char(2) | N |  |  |  |
| 15 | `dheader` | char(1) | N |  |  |  |
| 16 | `hpcode` | char(5) | N |  |  |  |
| 17 | `vpcode` | char(5) | N |  |  |  |
| 18 | `gtime` | char(5) | N |  |  |  |
| 19 | `hscore` | tinyint | N |  |  |  |
| 20 | `vscore` | tinyint | N |  |  |  |
| 21 | `cancel_flag` | bit | N |  | ((0)) |  |
| 22 | `suspended_flag` | bit | N |  | ((0)) |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_KBO_schedule (PK) | CLUSTERED | Y | gmkey, gamedate |

---

## PERSON_FA
- 행 수: **228**
- 컬럼 수: **4**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | smallint | N |  |  |  |
| 2 | `PCODE` | varchar(10) | N |  |  |  |
| 3 | `MONEY` | varchar(12) | Y |  |  |  |
| 4 | `OPTION` | varchar(12) | Y |  |  |  |

---

## STADIUM
- 행 수: **487**
- 컬럼 수: **3**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gyear` | char(4) | N | PK |  |  |
| 2 | `stadium` | varchar(10) | N | PK |  |  |
| 3 | `stadium_key` | char(2) | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_STADIUM (PK) | CLUSTERED | Y | gyear, stadium |

---

## person
- 행 수: **100,812**
- 컬럼 수: **20**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | smallint | N | PK |  |  |
| 2 | `PCODE` | varchar(10) | N | PK |  |  |
| 3 | `NAME` | varchar(20) | N |  |  |  |
| 4 | `TEAM` | varchar(20) | N |  |  |  |
| 5 | `T_ID` | char(2) | Y |  |  |  |
| 6 | `POS` | char(1) | Y |  |  |  |
| 7 | `POSITION` | varchar(4) | Y |  |  |  |
| 8 | `BACKNUM` | varchar(50) | Y |  |  |  |
| 9 | `ENGNAME` | nvarchar(50) | Y |  |  |  |
| 10 | `CNAME` | nvarchar(30) | Y |  |  |  |
| 11 | `HITTYPE` | varchar(8) | Y |  |  |  |
| 12 | `BIRTH` | varchar(8) | Y |  |  |  |
| 13 | `HEIGHT` | varchar(3) | Y |  |  |  |
| 14 | `WEIGHT` | varchar(3) | Y |  |  |  |
| 15 | `INDATE` | varchar(8) | Y |  |  |  |
| 16 | `PROMISE` | varchar(12) | Y |  |  |  |
| 17 | `MONEY` | varchar(12) | Y |  |  |  |
| 18 | `CAREER` | varchar(255) | Y |  |  |  |
| 19 | `DRAFT` | varchar(70) | Y |  |  |  |
| 20 | `REG_DT` | datetime | N |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_person_2 (PK) | CLUSTERED | Y | GYEAR, PCODE |

---

## person2
- 행 수: **91,891**
- 컬럼 수: **17**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `GYEAR` | smallint | N | PK |  |  |
| 2 | `PCODE` | varchar(10) | N | PK |  |  |
| 3 | `NAME` | varchar(20) | N | PK |  |  |
| 4 | `TEAM` | varchar(8) | N |  |  |  |
| 5 | `T_ID` | char(2) | Y |  |  |  |
| 6 | `POS` | char(1) | Y |  |  |  |
| 7 | `POSITION` | varchar(4) | Y |  |  |  |
| 8 | `BACKNUM` | varchar(50) | Y |  |  |  |
| 9 | `CNAME` | varchar(30) | Y |  |  |  |
| 10 | `HITTYPE` | varchar(8) | Y |  |  |  |
| 11 | `BIRTH` | varchar(8) | Y |  |  |  |
| 12 | `HEIGHT` | varchar(3) | Y |  |  |  |
| 13 | `WEIGHT` | varchar(3) | Y |  |  |  |
| 14 | `INDATE` | varchar(8) | Y |  |  |  |
| 15 | `PROMISE` | varchar(12) | Y |  |  |  |
| 16 | `MONEY` | varchar(12) | Y |  |  |  |
| 17 | `CAREER` | varchar(70) | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_person2_GYEAR_PCODE_NAME (PK) | CLUSTERED | Y | GYEAR, PCODE, NAME |

---
