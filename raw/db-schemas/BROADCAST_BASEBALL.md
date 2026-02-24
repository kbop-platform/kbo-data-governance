# BROADCAST_BASEBALL 스키마

테이블 수: 5개

## 목차
1. [BROADCASTING_CD](#broadcasting_cd) (2컬럼, 12행)
2. [BROADCASTING_RATE](#broadcasting_rate) (23컬럼, 1,589행)
3. [BROADCASTING_RATE_MINOR](#broadcasting_rate_minor) (21컬럼, 93행)
4. [BROADCASTING_schedule](#broadcasting_schedule) (22컬럼, 823행)
5. [BROADCASTING_schedule_minor ](#broadcasting_schedule_minor ) (20컬럼, 678행)

## BROADCASTING_CD
- 행 수: **12**
- 컬럼 수: **2**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `BROAD_NM` | char(20) | N |  |  |  |
| 2 | `BROAD_CD` | varchar(2) | N | PK |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_BROADCASTING_CD (PK) | CLUSTERED | Y | BROAD_CD |

---

## BROADCASTING_RATE
- 행 수: **1,589**
- 컬럼 수: **23**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gmkey` | char(13) | N | PK |  |  |
| 2 | `game_flag` | char(1) | Y |  |  |  |
| 3 | `end_flag` | char(1) | N |  |  |  |
| 4 | `cancel_flag` | bit | N |  | ((0)) |  |
| 5 | `suspended_flag` | bit | N |  | ((0)) |  |
| 6 | `gamedate` | varchar(8) | N | PK |  |  |
| 7 | `gyear` | char(4) | N |  |  |  |
| 8 | `gmonth` | char(2) | N |  |  |  |
| 9 | `gday` | char(2) | N |  |  |  |
| 10 | `gweek` | varchar(2) | N |  |  |  |
| 11 | `home` | varchar(10) | N |  |  |  |
| 12 | `home_key` | char(2) | N |  |  |  |
| 13 | `visit` | varchar(10) | N |  |  |  |
| 14 | `visit_key` | char(2) | N |  |  |  |
| 15 | `stadium` | varchar(10) | N |  |  |  |
| 16 | `stadium_key` | char(2) | N |  |  |  |
| 17 | `dheader` | char(1) | N |  |  |  |
| 18 | `gtime` | char(5) | N |  |  |  |
| 19 | `BROAD_CD` | varchar(2) | N | PK |  |  |
| 20 | `BROAD_RATE` | float | N |  |  |  |
| 21 | `BROAD_VIEWER` | float | N | PK |  |  |
| 22 | `BROAD_TOTAL_RATE` | float | Y |  |  |  |
| 23 | `BROAD_TOTAL_VIEWER` | float | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_BROADCASTING_RATE (PK) | CLUSTERED | Y | gmkey, gamedate, BROAD_CD, BROAD_VIEWER |

---

## BROADCASTING_RATE_MINOR
- 행 수: **93**
- 컬럼 수: **21**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gmkey` | char(13) | N | PK |  |  |
| 2 | `game_flag` | char(1) | Y |  |  |  |
| 3 | `cancel_flag` | bit | N |  | ((0)) |  |
| 4 | `suspended_flag` | bit | N |  | ((0)) |  |
| 5 | `gamedate` | varchar(8) | N | PK |  |  |
| 6 | `gyear` | char(4) | N |  |  |  |
| 7 | `gmonth` | char(2) | N |  |  |  |
| 8 | `gday` | char(2) | N |  |  |  |
| 9 | `gweek` | varchar(2) | N |  |  |  |
| 10 | `home` | varchar(10) | N |  |  |  |
| 11 | `home_key` | char(2) | N |  |  |  |
| 12 | `visit` | varchar(10) | N |  |  |  |
| 13 | `visit_key` | char(2) | N |  |  |  |
| 14 | `stadium` | varchar(10) | N |  |  |  |
| 15 | `dheader` | char(1) | N |  |  |  |
| 16 | `gtime` | char(5) | N |  |  |  |
| 17 | `BROAD_CD` | varchar(2) | N | PK |  |  |
| 18 | `BROAD_RATE` | float | N |  |  |  |
| 19 | `BROAD_VIEWER` | float | N | PK |  |  |
| 20 | `BROAD_TOTAL_RATE` | float | Y |  |  |  |
| 21 | `BROAD_TOTAL_VIEWER` | float | Y |  |  |  |

**인덱스:**
| 인덱스명 | 유형 | 고유 | 컬럼 |
|---------|------|------|------|
| PK_BROADCASTING_RATE_MINOR (PK) | CLUSTERED | Y | gmkey, gamedate, BROAD_CD, BROAD_VIEWER |

---

## BROADCASTING_schedule
- 행 수: **823**
- 컬럼 수: **22**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gmkey` | char(13) | N |  |  |  |
| 2 | `game_flag` | char(1) | Y |  |  |  |
| 3 | `end_flag` | char(1) | N |  |  |  |
| 4 | `cancel_flag` | bit | N |  | ((0)) |  |
| 5 | `suspended_flag` | bit | N |  | ((0)) |  |
| 6 | `gamedate` | varchar(8) | N |  |  |  |
| 7 | `gyear` | char(4) | N |  |  |  |
| 8 | `gmonth` | char(2) | N |  |  |  |
| 9 | `gday` | char(2) | N |  |  |  |
| 10 | `gweek` | varchar(2) | N |  |  |  |
| 11 | `home` | varchar(10) | N |  |  |  |
| 12 | `home_key` | char(2) | N |  |  |  |
| 13 | `visit` | varchar(10) | N |  |  |  |
| 14 | `visit_key` | char(2) | N |  |  |  |
| 15 | `stadium` | varchar(10) | N |  |  |  |
| 16 | `stadium_key` | char(2) | N |  |  |  |
| 17 | `dheader` | char(1) | N |  |  |  |
| 18 | `gtime` | char(5) | N |  |  |  |
| 19 | `TSM` | char(1) | N |  | ((0)) |  |
| 20 | `REFFER_CAM_TVING` | char(1) | N |  | ((0)) |  |
| 21 | `REFFER_CAM_MBC` | char(1) | N |  | ((0)) |  |
| 22 | `CGV` | char(1) | N |  | ((0)) |  |

---

## BROADCASTING_schedule_minor 
- 행 수: **678**
- 컬럼 수: **20**

| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |
|---|--------|------------|------|----|----|------|
| 1 | `gmkey` | char(13) | N |  |  |  |
| 2 | `game_flag` | char(1) | Y |  |  |  |
| 3 | `end_flag` | char(1) | N |  |  |  |
| 4 | `cancel_flag` | bit | N |  | ((0)) |  |
| 5 | `suspended_flag` | bit | N |  | ((0)) |  |
| 6 | `gamedate` | varchar(8) | N |  |  |  |
| 7 | `gyear` | char(4) | N |  |  |  |
| 8 | `gmonth` | char(2) | N |  |  |  |
| 9 | `gday` | char(2) | N |  |  |  |
| 10 | `gweek` | varchar(2) | N |  |  |  |
| 11 | `home` | varchar(10) | N |  |  |  |
| 12 | `home_key` | char(2) | N |  |  |  |
| 13 | `visit` | varchar(10) | N |  |  |  |
| 14 | `visit_key` | char(2) | N |  |  |  |
| 15 | `stadium` | varchar(10) | N |  |  |  |
| 16 | `stadium_key` | char(2) | N |  |  |  |
| 17 | `dheader` | char(1) | N |  |  |  |
| 18 | `gtime` | char(5) | N |  |  |  |
| 19 | `REFFER_CAM` | char(1) | N |  | ((0)) |  |
| 20 | `TVN` | char(1) | N |  | ((0)) |  |

---
