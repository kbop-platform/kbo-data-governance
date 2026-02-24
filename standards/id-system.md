# ID 체계 표준

> 최종수정: 2026-02-24 | 출처: analysis/id-analysis.md, raw/column-metadata.json

## 1. 개요

KBO 데이터 시스템의 식별자(ID) 체계를 정의한다.
현행 시스템은 **구세대**(GMKEY/PCODE)와 **신세대**(G_ID/P_ID) 두 체계가 공존하며, 본 표준은 신세대 명명으로 통일한다.

- 모든 ID는 **부여 후 변경 불가**(immutable).
- 1982년부터의 과거 데이터에 대한 레거시 매핑 규칙을 포함한다 (DAR-009 마이그레이션용).

→ 참고: [명명 규칙](./naming-rules.md) — ID 네이밍 컨벤션
→ 참고: [도메인 타입 정의](./domain-types.md#31-identifier-_id) — ID 타입 정의

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

**예시**:
| game_id | 일자 | 원정 | 홈 | DH |
|---------|------|------|-----|-----|
| `20250322HHKT0` | 2025-03-22 | HH(키움) | KT(KT) | 단일 |
| `20250322LTLG0` | 2025-03-22 | LT(롯데) | LG(LG) | 단일 |
| `19820327SSLG0` | 1982-03-27 | SS(삼성) | LG(MBC) | 단일 |

> **주의**: game_id 내부의 팀코드는 **역사적 코드 고정**. SK(현 SSG), OB(현 두산) 등 팀명이 바뀌어도 game_id는 변경하지 않는다.

**특수 game_id**:
| 패턴 | 의미 |
|------|------|
| `9999MMDDVVHH0` | 올스타전 등 특별 경기 |
| DH번호 `1`, `2` | 더블헤더 1차전, 2차전 |

### 2.2 player_id (선수 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `player_id` |
| 레거시명 | `PCODE`, `P_ID`, `PlayerID` |
| 타입 | `int` (표준), `varchar(10)` (레거시) |
| 형식 | 5자리 숫자 (`NNNNN`) |
| 데이터 범위 | 10005 ~ 99999+ |

**번호 대역**:
| 대역 | 추정 의미 |
|------|----------|
| 1xxxx | 코칭스태프/감독 (초기 등록) |
| 5xxxx | 현역 선수 (최근 등록) |
| 6xxxx~9xxxx | 과거 선수 (1982년~) |

> 레거시 PCODE는 `varchar(10)`이나 실제 값은 5자리 숫자. 표준 `int`로 전환한다.

### 2.3 team_id (팀 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `team_id` |
| 레거시명 | `T_ID`, `TEAM`, `HTEAM`, `VTEAM` |
| 타입 | `char(2)` |
| 형식 | 영문 대문자 2자리 |

**현행 10개 팀**:
| team_id | 구단명 | 팀명 | 연고지 | 홈 구장 |
|---------|--------|------|--------|---------|
| `HH` | 키움 | 히어로즈 | 서울(고척) | KC |
| `HT` | KIA | 타이거즈 | 광주 | GJ |
| `KT` | KT | 위즈 | 수원 | SW |
| `LG` | LG | 트윈스 | 서울(잠실) | JS |
| `LT` | 롯데 | 자이언츠 | 부산(사직) | SJ |
| `NC` | NC | 다이노스 | 창원 | CW |
| `OB` | 두산 | 베어스 | 서울(잠실) | JS |
| `SK` | SSG | 랜더스 | 인천(문학) | IC |
| `SS` | 삼성 | 라이온즈 | 대구 | DG |
| `WO` | 한화 | 이글스 | 대전 | DJ |

> team_id는 역사적 코드를 유지한다. OB=두산, SK=SSG로 팀명이 바뀌어도 코드는 변경하지 않는다.

→ 참고: [코드 사전 Section 4](./code-dictionary.md#4) — 역사적 팀 코드 전체

### 2.4 stadium_id (구장 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `stadium_id` |
| 레거시명 | `stadium_key`, `STAD` |
| 타입 | `char(2)` |
| 형식 | 영문 대문자 2자리 |

**주요 구장**:
| stadium_id | 구장명 | 도시 | 상태 |
|------------|--------|------|------|
| `JS` | 잠실 | 서울 | 운영 |
| `KC` | 고척 | 서울 | 운영 |
| `GJ` | 광주(무등/챔피언스필드) | 광주 | 운영 |
| `SW` | 수원 | 수원 | 운영 |
| `DG` | 대구(시민/라이온즈파크) | 대구 | 운영 |
| `DJ` | 대전(한밭) | 대전 | 운영 |
| `IC` | 인천(문학) | 인천 | 운영 |
| `SJ` | 사직 | 부산 | 운영 |
| `CW` | 창원(NC파크) | 창원 | 운영 |
| `DM` | 동대문 | 서울 | **폐장** |
| `KD` | 구덕 | 부산 | **폐장** |

→ 참고: [코드 사전 Section 5](./code-dictionary.md#5) — 전체 구장 코드

> **주의**: `GAMEINFO.STADIUM`은 한글 구장명(`nvarchar`)이며 ID가 아니다. 코드 참조에는 `stadium_id`를 사용한다.

### 2.5 season_id (시즌 ID)

| 항목 | 값 |
|------|-----|
| 표준명 | `season_id` (FK로 사용 시) / `season_yr` (속성으로 사용 시) |
| 레거시명 | `GYEAR`, `SEASON_ID`, `gyear` |
| 타입 | `smallint` |
| 형식 | 4자리 연도 (YYYY) |
| 데이터 범위 | 1982 ~ 현재 |
| 예약값 | `9999` = 통산(Career Total) |

**사용 구분**:
| 용도 | 표준명 | 예시 테이블 |
|------|--------|-----------|
| 테이블 PK / FK | `season_id` | TEAM, SEASON_PLAYER_* |
| 필터 속성 | `season_yr` | BAT_TOTAL, PIT_TOTAL, PERSON |

### 2.6 league_id / series_id (리그/시리즈 ID)

| ID | 표준명 | 타입 | 값 |
|----|--------|------|-----|
| 리그 | `league_id` | `smallint` | 1=1군 정규, 2=가을리그/기타 |
| 시리즈 | `series_id` | `smallint` | 0=정규시즌, 1=포스트시즌, 15=가을리그 |

> 값 목록은 현행 데이터에서 확인된 것만 기재. 전체 값은 S2i 확인 필요.

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

### 5.1 합계행 (PCODE = 'T' / 'B')

Hitter, Pitcher 테이블에서 팀 합계행:
- `PCODE = 'T'`: 원정팀(Top) 합계
- `PCODE = 'B'`: 홈팀(Bottom) 합계

**표준 처리 방안**:

방안 A (**권고**) — 합계행 분리:
- 합계행을 별도 뷰 또는 집계 테이블로 분리
- 원본 테이블에는 실제 선수 행만 유지 (player_id NOT NULL)
- 합계는 쿼리 시 `SUM()` 또는 별도 `GAME_TEAM_TOTAL` 테이블

방안 B — 예약 player_id 사용 (레거시 호환):
- `player_id`가 PK 구성요소이므로 NULL 불가
- 예약 ID 할당: `player_id = -1` (원정팀 합계), `player_id = -2` (홈팀 합계)
- 별도 컬럼 `is_team_total` (`bit`, 기본값 0) 추가
- 원정/홈 구분은 기존 `top_bottom_cd` 컬럼 활용

| 현행 | player_id | is_team_total | top_bottom_cd | 비고 |
|------|-----------|---------------|---------------|------|
| PCODE='T' | -1 | 1 | T | 원정팀 합계 |
| PCODE='B' | -2 | 1 | B | 홈팀 합계 |
| PCODE='75847' | 75847 | 0 | T 또는 B | 개인 기록 |

> **방안 A 권고 사유**: 합계행이 개인 기록 테이블에 혼재하면 `AVG()`, `COUNT()` 등 집계 시 이중 집계 위험. 분리가 데이터 품질에 유리.

### 5.2 통산 (GYEAR = 9999)

BatTotal, PitTotal 테이블에서 선수 통산 기록:
- `GYEAR = 9999` / `SEC = 9999`: 전 시즌 통산 합계

**표준**: `season_yr = 9999`는 **통산 예약값**으로 문서화. 삭제하지 않는다.

### 5.3 특별 경기 (game_id 9999*)

`99990725EAWE0` 같은 `9999` 시작 game_id:
- 올스타전, 시범경기 등 특별 이벤트

**표준**: 유효한 game_id로 인정. `9999`는 연도가 아닌 특별 경기 표시자.

### 5.4 BatTotal.SEC 값

| 현행 SEC 값 | 의미 | 표준 series_cd |
|------------|------|---------------|
| 연도 (2025 등) | 해당 시즌 | 연도값 유지 |
| `9999` | 통산 | `9999` |
| `1` | 전체 (추정) | 확인 필요 |
| 팀명 (한글) | — | **비정상 데이터** — 정리 필요 |

---

## 6. 팀 코드 이력 관리

team_id는 불변이지만 팀명(구단명, 팀명)은 변경된다. TEAM 마스터 테이블로 이력을 관리한다.

**TEAM 테이블 구조** (현행, 401행):
| 컬럼 | 용도 |
|------|------|
| season_id | 시즌 연도 |
| team_id | 팀 코드 (2자) |
| first_nm | 구단명 (예: "키움") |
| last_nm | 팀명 (예: "히어로즈") |
| first_eng_nm | 구단 영문명 |
| last_eng_nm | 팀 영문명 |
| group_sc | 그룹 구분 (ALLSTAR, MAGIC, DREAM) |

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

→ 참고: [코드 사전 Section 4](./code-dictionary.md#4) — 전체 팀 코드 목록

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
