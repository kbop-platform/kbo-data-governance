# ID 체계 표준

> 최종수정: 2026-02-25 | 출처: analysis/id-analysis.md, raw/column-metadata.json
> 📋 문서 성격: 신규 시스템 ID 표준(안) · 현행 레거시 매핑 포함

## 1. 개요

KBO 데이터 시스템의 식별자(ID) 체계를 정의한다.
현행 시스템은 **구세대**(GMKEY/PCODE)와 **신세대**(G_ID/P_ID) 두 체계가 공존하며, 본 표준은 신세대 명명으로 통일한다.

- 모든 ID는 **부여 후 변경 불가**(immutable).
- 1982년부터의 과거 데이터에 대한 레거시 매핑 규칙을 포함한다 (DAR-009 마이그레이션용).

→ 참고: [명명 규칙](./naming-rules.md) - ID 네이밍 컨벤션
→ 참고: [도메인 사전](../standards-dict/domains.md) - ID 타입 정의

---

## 2. 핵심 ID 정의

### 2.1 game_id (경기 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `game_id` |
| 레거시명 | `GMKEY`, `G_ID`, `gmkey`, `gameID`, `GAMEID` |
| 타입 | `char(13)` |
| 형식 | `YYYYMMDDVVHH#` (13자리 고정) |
| 데이터 범위 | `19820327SSLG0` ~ 현재 |

**형식 분해**:
```
YYYYMMDDVVHH#
│       ││  └─ 더블헤더 번호 (0=단일, 1=1차전, 2=2차전)
│       │└──── 홈팀 코드 (2자)
│       └───── 원정팀 코드 (2자)
└────────────── 경기 일자 (8자리)
```

예시: `20250322HHKT0` = 2025-03-22 키움(원정) vs KT(홈) 단일경기. game_id 내부의 팀코드는 역사적 코드 고정 (SK=SSG, OB=두산 등 변경하지 않음). 특수값: `9999MMDDVVHH0` = 올스타전 등 특별 경기, DH번호 `1`/`2` = 더블헤더.

### 2.2 player_id (선수 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `player_id` |
| 레거시명 | `PCODE`, `P_ID`, `PlayerID` |
| 타입 | `int` (표준), `varchar(10)` (레거시) |
| 형식 | 5자리 숫자 (`NNNNN`) |
| 데이터 범위 | 10005 ~ 99999+ |

번호 대역: 1xxxx=코칭스태프, 5xxxx=현역, 6xxxx~9xxxx=과거 선수. 레거시 PCODE(`varchar(10)`)는 `int`로 전환한다.

### 2.3 team_id (팀 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `team_id` |
| 레거시명 | `T_ID`, `TEAM`, `HTEAM`, `VTEAM` |
| 타입 | `char(2)` |
| 형식 | 영문 대문자 2자리 |

현행 10개 팀: `HH`, `HT`, `KT`, `LG`, `LT`, `NC`, `OB`, `SK`, `SS`, `WO`. team_id는 역사적 코드를 유지한다 (OB=두산, SK=SSG 등 팀명이 바뀌어도 코드 불변).

→ 참고: [코드 사전](../standards-dict/codes.md) - 전체 팀 코드 목록

### 2.4 stadium_id (구장 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `stadium_id` |
| 레거시명 | `stadium_key`, `STAD` |
| 타입 | `char(2)` |
| 형식 | 영문 대문자 2자리 |

`GAMEINFO.STADIUM`은 한글 구장명(`nvarchar`)이며 ID가 아니다. 코드 참조에는 `stadium_id`를 사용한다.

→ 참고: [코드 사전](../standards-dict/codes.md) - 전체 구장 코드

### 2.5 season_id (시즌 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `season_id` (FK로 사용 시) / `season_yr` (속성으로 사용 시) |
| 레거시명 | `GYEAR`, `SEASON_ID`, `gyear` |
| 타입 | `smallint` |
| 형식 | 4자리 연도 (YYYY) |
| 데이터 범위 | 1982 ~ 현재 |
| 예약값 | `9999` = 통산(Career Total) |

### 2.6 league_id / series_id (리그/시리즈 ID)

| ID | 표준명 | 타입 | 값 |
|----|--------|------|-----|
| 리그 | `league_id` | `smallint` | 1=1군 정규, 2=가을리그/기타 |
| 시리즈 | `series_id` | `smallint` | 0=정규시즌, 1=포스트시즌, 15=가을리그 |

---

## 3. 복합 PK 표준

주요 테이블의 복합 PK 구성. 현행(레거시) PK와 표준 PK를 대비한다.

| 테이블 (표준) | 현행 PK (레거시) | 표준 PK | 설명 |
|-------------|----------------|---------|------|
| GAME_INFO | `GMKEY`, `GDAY` | `game_id` | 경기 1건=1행. GDAY는 GMKEY에 포함되어 중복 제거 |
| HITTER | `GMKEY`, `GYEAR`, `PCODE` | `game_id`, `season_yr`, `player_id` | 경기별 타자 기록 |
| PITCHER | `GMKEY`, `GYEAR`, `PCODE` | `game_id`, `season_yr`, `player_id` | 경기별 투수 기록 |
| GAME_CONT_APP | `GMKEY`, `GYEAR`, `SEQ_NO` | `game_id`, `season_yr`, `seq_no` | 경기 이벤트 상세 |
| ENTRY | `GMKEY`, `GYEAR`, `TURN`, `PCODE`, `POS` | `game_id`, `season_yr`, `turn_no`, `player_id`, `position_cd` | 출전 엔트리 |
| BAT_TOTAL | `PCODE`, `GYEAR`, `SEC` | `season_yr`, `player_id`, `series_cd` | 타격 시즌/통산 합산 |
| PIT_TOTAL | `PCODE`, `GYEAR`, `SEC` | `season_yr`, `player_id`, `series_cd` | 투구 시즌/통산 합산 |
| SEASON_PLAYER_HITTER | 신세대 PK | `season_id`, `player_id`, `section_cd`, `group_if` | 시즌 타자 통계 |
| SCORE | `GMKEY`, `GDAY` (2컬럼) | `game_id`, `season_yr`, `top_bottom_cd` (3컬럼) | 팀별 경기 스코어 (*) |
| GAME_HR | 신세대 PK | `league_id`, `series_id`, `game_id`, `seq_no` | 홈런 기록 |
| PERSON | `SEASON_ID`, `PCODE` | `season_yr`, `player_id` | 시즌별 선수 정보 |

> (*) **SCORE PK 전환 설명**: 현행은 경기당 1행으로 이닝별 점수를 피벗 컬럼(1T, 1B, 2T, 2B...)에 저장하므로 `GMKEY, GDAY` 2컬럼 PK. 표준은 팀별 1행(정규화)으로 전환하며 `top_bottom_cd`(T=원정, B=홈)를 PK에 추가하여 경기당 2행 구조로 변경한다. `season_yr`는 시즌별 파티셔닝 및 조인 효율을 위해 추가.

---

## 4. 레거시 ID 매핑

### 4.1 GMKEY → game_id

| 항목 | 레거시 | 표준 |
|------|--------|------|
| 컬럼명 | GMKEY / G_ID / gmkey / gameID | game_id |
| 타입 | char(13) | char(13) |
| 값 형식 | 동일 (YYYYMMDDVVHH#) | 동일 |

**매핑 규칙**: 이름만 변경. 값과 형식은 동일하므로 `RENAME` 또는 `VIEW ALIAS`로 처리.

### 4.2 PCODE → player_id

| 항목 | 레거시 | 표준 |
|------|--------|------|
| 컬럼명 | PCODE / P_ID / PlayerID | player_id |
| 타입 | varchar(10) / int | int |
| 값 형식 | 5자리 숫자 문자열 | 정수 |

**매핑 규칙**: `CAST(PCODE AS int)`. 단, 특수값 처리 필요 (Section 5 참고).

### 4.3 기타 매핑

| 레거시 | 표준 | 변환 |
|--------|------|------|
| TEAM / HTEAM / VTEAM | team_cd / home_team_cd / away_team_cd | 값 정리 필요 (한글→코드) |
| STADIUM (한글) | stadium_nm | 이름 변경 |
| STAD / stadium_key | stadium_id | 이름 변경 |
| GYEAR (char/smallint) | season_yr / season_id | 타입 통일 (smallint) |

---

## 5. 특수값 처리

| 특수값 | 테이블 | 의미 | 표준 처리 |
|--------|--------|------|----------|
| PCODE = `'T'` / `'B'` | Hitter, Pitcher | 팀 합계행 (원정/홈) | 마이그레이션 시 분리 방안 결정 필요 |
| GYEAR = `9999` / SEC = `9999` | BatTotal, PitTotal | 전 시즌 통산 합계 | `season_yr = 9999` 통산 예약값으로 유지 |
| game_id `9999*` | GAME_INFO 등 | 올스타전/시범경기 등 특별 경기 | 유효한 game_id로 인정 |
| SEC = 팀명(한글) | BatTotal | 비정상 데이터 | 정리 필요 |

> → 참고: [마이그레이션 설계 결정 §3](../migration/design-decisions.md) - 합계행 처리 방안 A/B 상세

---

## 6. 팀 코드 이력 관리

team_id는 불변이지만 팀명은 변경된다. TEAM 마스터 테이블(401행, PK: `season_id + team_id`)에서 `first_nm`(구단명), `last_nm`(팀명), 영문명, `group_sc` 등으로 연도별 이력을 관리한다.

**팀 코드 변천**:
| team_id | 구단 변천 | 기간 |
|---------|----------|------|
| `OB` | OB 베어스 → 두산 베어스 | 1982~ |
| `SK` | 쌍방울 레이더스 → SK 와이번스 → SSG 랜더스 | 1990~ |
| `HH` | 현대 유니콘스 → 서울 히어로즈 → 넥센 → 키움 | 2008~ |
| `HT` | 해태 타이거즈 → KIA 타이거즈 | 1982~ |
| `WO` | 빙그레 이글스 → 한화 이글스 | 1986~ |
| `HD` | 삼미 → 청보 → 태평양 → 현대 | 1982~2007 (해체) |
| `SB` | 쌍방울 | 1991~1999 (해체) |

> game_id 내부 팀코드와 이 테이블을 조인하면 해당 시점의 팀명을 조회할 수 있다.

→ 참고: [코드 사전](../standards-dict/codes.md) - 전체 팀 코드 목록

---

## 7. 신규 시스템 ID 가이드

KBO가 자체 구축하는 새 테이블(세이버메트릭스, pitch-by-pitch 등)의 ID 설계 원칙:

| 원칙 | 설명 |
|------|------|
| 자연키 우선 | 의미 있는 자연키가 있으면 사용 (game_id, player_id 등) |
| 대리키 사용 조건 | 자연키가 없거나 복합키가 3개 이상일 때 `bigint IDENTITY` |
| UUID 비권장 | 현 시스템 규모에서 UUID는 불필요. 자연키가 이미 인간 가독성 높음 |
| FK 이름 일치 | 외래키 컬럼명은 참조 테이블의 PK 컬럼명과 동일하게 |
| 복합키 순서 | 카디널리티가 낮은 것부터 (league_id → series_id → game_id → seq_no) |

**예시: pitch-by-pitch 테이블 (향후 신규)**:
```sql
CREATE TABLE PITCH_BY_PITCH (
    game_id      char(13)   NOT NULL,  -- FK → GAME_INFO
    season_yr    smallint   NOT NULL,
    inning_no    int        NOT NULL,
    seq_no       int        NOT NULL,  -- 투구 순번
    pitcher_id   int        NOT NULL,  -- FK → PERSON
    batter_id    int        NOT NULL,  -- FK → PERSON
    pitch_type_cd varchar(10),
    pitch_speed_va int,
    pitch_result_cd varchar(10),
    CONSTRAINT PK_PITCH PRIMARY KEY (game_id, season_yr, seq_no)
);
```
