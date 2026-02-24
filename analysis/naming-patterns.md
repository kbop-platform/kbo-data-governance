# 네이밍 패턴 분석

> 분석 일시: 2026-02-23
> 대상: 19개 DB, 52종 테이블, 약 5,600개 컬럼

## 1. 테이블명 네이밍 패턴

### 1.1 대소문자 규칙 (불일치 존재)

| 패턴 | 테이블 예시 | 사용 DB |
|------|------------|---------|
| **PascalCase** | `BatTotal`, `Hitter`, `Pitcher`, `PitTotal`, `Score`, `TeamRank` | DB1/DB2 1군 정규시즌 |
| **UPPER_CASE** | `BATTOTAL`, `HITTER`, `PITCHER`, `PITTOTAL`, `SCORE`, `TEAMRANK` | DB1/DB2 2군(Minor) |
| **UPPER_SNAKE** | `GAME_HR`, `GAME_MEMO`, `CANCEL_GAME`, `GAME_MEMO_PITCHCLOCK` | 1군 공통 |
| **PascalCase+접두** | `IE_BallCount`, `IE_BatterRecord`, `IE_LiveText` | DB2 1군 NEW |
| **UPPER_SNAKE+접두** | `IE_BALLCOUNT`, `IE_BATTERRECORD`, `IE_LIVETEXT` | DB2 2군 NEW |
| **소문자_snake** | `person`, `person2` | DB2_BASEBALL_NEW |
| **혼합** | `KBO_BATRESULT`, `KBO_schedule`, `BROADCASTING_schedule` | 각종 |

**주요 문제:**
- **동일 테이블이 DB마다 대소문자가 다름** (`Hitter` vs `HITTER`, `BatTotal` vs `BATTOTAL`)
- **같은 DB 내에서도 혼용** (`KBO_schedule` 소문자 vs `CANCEL_GAME` 대문자)
- 1군은 PascalCase 경향, 2군은 UPPER_CASE 경향

### 1.2 테이블 접두사 체계

| 접두사 | 의미 | 테이블 수 |
|--------|------|----------|
| `IE_` | 기록입력(Input/Entry) 시스템 | 8종 |
| `KBO_` | KBO 공식 데이터 | 4종 |
| `GAME_` | 경기 관련 | 5종 |
| `SEASON_` | 시즌 통계 | 6종 |
| `BROADCASTING_` | 중계 관련 | 4종 |
| `FALL_LEAGUE_` | 가을리그 | 1종 |
| (없음) | 핵심 테이블 | ~24종 |

### 1.3 테이블 명명 스키마: 2개 세대 공존

#### 구세대 스키마 (Sports2i 원본)
- 식별자: `GMKEY` (경기키), `PCODE` (선수코드)
- 네이밍: 짧은 약어 (`GAMECONTAPP`, `BatTotal`, `DEFEN`, `ENTRY`)
- 특징: 접두사 없음, 약어 중심

#### 신세대 스키마 (KBO 표준)
- 식별자: `LE_ID`, `SR_ID`, `SEASON_ID`, `G_ID`, `P_ID`
- 네이밍: `{도메인}_{의미}_{접미사}` 패턴
- 접미사 규칙: `_NM`(이름), `_CD`(코드), `_CN`(카운트), `_SC`(구분코드), `_IF`(플래그), `_RT`(비율), `_DT`(일시), `_TM`(시간), `_VA`(값)
- 테이블: `GAME_HR`, `GAME_MEMO`, `CANCEL_GAME`, `FALL_LEAGUE_*`

---

## 2. 컬럼명 네이밍 패턴

### 2.1 대소문자 규칙

| 패턴 | 비율 (추정) | 예시 |
|------|------------|------|
| **UPPER_CASE** | ~70% | `GMKEY`, `PCODE`, `GYEAR`, `GDAY`, `STADIUM` |
| **camelCase / 소문자** | ~15% | `gmkey`, `gyear`, `gamedate`, `stadium_key` |
| **PascalCase+접미** | ~15% | `SEASON_ID`, `CANCEL_SC_NM`, `HR_DISTANCE_VA` |

**주요 불일치:**
- `KBO_schedule` 테이블의 컬럼은 **소문자** (`gmkey`, `gamedate`, `stadium_key`)
- 나머지 대부분은 **UPPER_CASE** (`GMKEY`, `GDAY`, `STADIUM`)
- 신세대 테이블(`GAME_HR` 등)은 **UPPER+접미사** (`LE_ID`, `PLACE_SC`)

### 2.2 공통 약어 패턴

#### 식별자 약어
| 약어 | 의미 | 사용 컬럼 |
|------|------|----------|
| `GM` | Game (경기) | `GMKEY` |
| `G` | Game | `G_ID`, `GDAY`, `GYEAR` |
| `P` | Player (선수) / Pitcher | `PCODE`, `P_ID`, `POS` |
| `T` | Team (팀) | `T_ID`, `TB` |
| `S` | Stadium / Season / Series | `S_NM`, `SEASON_ID`, `SR_ID` |
| `LE` | League (리그) | `LE_ID` |

#### 기록 약어 (야구 통계)
| 약어 | 의미 (영문) | 의미 (한글) |
|------|------------|------------|
| `AB` | At Bat | 타수 |
| `HIT` | Hit | 안타 |
| `H2` | Double | 2루타 |
| `H3` | Triple | 3루타 |
| `HR` | Home Run | 홈런 |
| `RBI` | Runs Batted In | 타점 |
| `RUN` | Run | 득점 |
| `BB` | Base on Balls | 볼넷 |
| `HP` | Hit by Pitch | 사구 |
| `KK` | Strikeout | 삼진 |
| `SB` | Stolen Base | 도루 |
| `CS` | Caught Stealing | 도루실패 |
| `SH` | Sacrifice Hit | 희생번트 |
| `SF` | Sacrifice Fly | 희생플라이 |
| `GD` | Grounded into DP | 병살타 |
| `ERR` | Error | 실책 |
| `IB` | Intentional Base on Balls | 고의사구 |
| `PA` | Plate Appearance | 타석 |
| `TB` | Total Base / Top/Bottom | 루타/팀구분 |
| `INN` | Inning | 이닝 |
| `BF` | Batters Faced | 상대타자수 |
| `CG` | Complete Game | 완투 |
| `SHO` | Shutout | 완봉 |
| `WLS` | Win/Loss/Save | 승패세 |
| `ER` | Earned Run | 자책점 |
| `ERA` | Earned Run Average | 평균자책점 |
| `HRA` | Batting Average (타율) | 타율 |
| `WP` | Wild Pitch | 폭투 |
| `BK` | Balk | 보크 |
| `PB` | Passed Ball | 포일 |
| `PO` | Put Out | 자살 |
| `ASS` | Assist | 보살 |
| `DP` | Double Play | 병살 |
| `LOB` | Left on Base | 잔루 |

#### 경기 정보 약어
| 약어 | 의미 |
|------|------|
| `STTM` | Start Time (시작시간) |
| `ENTM` | End Time (종료시간) |
| `DLTM` | Delay Time (지연시간) |
| `GMTM` | Game Time (경기시간, 분) |
| `STAD` | Stadium Code (구장 약어코드) |
| `UMPC` | Umpire Chief (주심) |
| `UMP1~3` | Umpire 1~3 (루심) |
| `SCOA/SCOB` | Scorer A/B (기록원) |
| `TEMP` | Temperature (기온, ×10) |
| `MOIS` | Moisture (습도) |
| `WEATH` | Weather (날씨 코드) |
| `WIND` | Wind Direction (풍향) |
| `WINS` | Wind Speed (풍속) |
| `CROWD` | Crowd (관중수) |
| `DBHD` | Doubleheader (더블헤더) |
| `CHAJUN` | 차전(라운드) |

### 2.3 신세대 컬럼 접미사 규칙

| 접미사 | 의미 | 예시 |
|--------|------|------|
| `_ID` | 식별자 | `LE_ID`, `SR_ID`, `G_ID`, `P_ID`, `T_ID` |
| `_NM` | 이름 | `AWAY_NM`, `HOME_NM`, `S_NM`, `CANCEL_SC_NM` |
| `_CD` | 코드 | `BROAD_CD`, `SECTION_CD` |
| `_SC` | 구분코드(Sub Code) | `TB_SC`, `PLACE_SC`, `DIREC_SC`, `GAME_SC_ID`, `CANCEL_SC_ID`, `GROUP_SC` |
| `_CN` | 수량(Count) | `SCORE_CN`, `GAME_CN`, `PA_CN`, `AB_CN`, `CROWD_CN` |
| `_RT` | 비율(Rate) | `HRA_RT`, `SB_RT`, `OBP_RT`, `SLG_RT`, `OPS_RT` |
| `_IF` | 플래그(If/Boolean) | `GROUP_IF`, `FIRST_IF`, `LAST_IF`, `T_RECORDPAGE_IF` |
| `_DT` | 일시(DateTime) | `REG_DT`, `RECORD_DT`, `G_DT` |
| `_TM` | 시간(Time) | `G_TM`, `START_TM`, `END_TM`, `USE_TM` |
| `_VA` | 값(Value) | `HR_DISTANCE_VA` |
| `_NO` | 번호(Number) | `INN_NO`, `BAT_ORDER_NO`, `SEQ_NO`, `HEADER_NO` |

---

## 3. DB간 네이밍 불일치 요약

### 3.1 테이블명 불일치
| 논리명 | 1군 DB | 2군 DB | 비고 |
|--------|--------|--------|------|
| 타자기록 | `Hitter` | `HITTER` | 대소문자 |
| 투수기록 | `Pitcher` | `PITCHER` | 대소문자 |
| 타격합산 | `BatTotal` | `BATTOTAL` | 대소문자 |
| 투구합산 | `PitTotal` | `PITTOTAL` | 대소문자 |
| 스코어 | `Score` | `SCORE` | 대소문자 |
| 팀순위 | `TeamRank` | `TEAMRANK` | 대소문자 |
| 타격결과 | `KBO_BATRESULT` (90col) | `KBO_BATRESULT` (65col) | 컬럼수 차이 |
| 일정 | `KBO_schedule` (소문자) | `KBO_SCHEDULE` (대문자) | 대소문자+컬럼수 |

### 3.2 컬럼명 불일치
| 논리명 | 구세대 | 신세대 |
|--------|--------|--------|
| 경기 식별자 | `GMKEY` | `G_ID` |
| 선수 식별자 | `PCODE` | `P_ID` |
| 팀 식별자 | `TEAM`, `HTEAM`, `VTEAM` | `T_ID`, `HOME_ID`, `AWAY_ID` |
| 구장명 | `STADIUM` | `S_NM` |
| 시즌 | `GYEAR` | `SEASON_ID` |

---

## 4. 네이밍 패턴 통계

### 데이터 타입 분포 (DB2_BASEBALL_220328 기준)
| 타입 | 사용 수 | 비율 |
|------|---------|------|
| varchar | 152 | 31.4% |
| smallint | 144 | 29.8% |
| char | 60 | 12.4% |
| int | 51 | 10.5% |
| nvarchar | 38 | 7.9% |
| tinyint | 27 | 5.6% |
| datetime | 4 | 0.8% |
| bigint | 4 | 0.8% |
| float | 2 | 0.4% |
| real | 1 | 0.2% |

### 문자열 타입 혼용 문제
- `varchar` vs `nvarchar` 혼용 (한글 데이터에 varchar 사용 → EUC-KR 인코딩)
- `char` (고정길이) vs `varchar` (가변길이) 혼용
- 동일 의미 컬럼이 테이블마다 다른 타입 사용

---

## 5. 표준화 권고사항

1. **테이블명**: `UPPER_SNAKE_CASE` 통일 권장 (MSSQL 관례)
2. **컬럼명**: `UPPER_SNAKE_CASE` 통일 (구세대 약어 유지하되 신세대 접미사 규칙 적용)
3. **문자열**: 한글 포함 컬럼은 `nvarchar` 사용, 코드성은 `varchar` 유지
4. **식별자**: 신세대 `_ID` 체계로 통일 (`G_ID`, `P_ID`, `T_ID`)
5. **약어 사전**: 야구 통계 약어는 국제 표준 유지 (AB, HR, ERA 등)
