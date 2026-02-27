# KBO 자체 테이블 설계 가이드

> 최종수정: 2026-02-24 | KBO 데이터 표준 정의서 (RFP DAR-001)
> 📋 문서 성격: 신규 시스템 테이블 설계 가이드(안)

## 1. 개요

본 문서는 S2i 미제공 데이터(pitch-by-pitch, 세이버메트릭스 등)를 위한 **KBO 자체 테이블** 설계 시 따라야 할 표준과 패턴을 정의한다.

**대상**: KBO 데이터팀(R-06)이 자체 구축하는 모든 신규 테이블

**목표**:
- S2i 제공 데이터와의 일관성 확보 (동일 ID·타입 체계)
- 표준 명명 규칙 준수
- 향후 확장을 고려한 설계

→ 참고: [ID 체계 §7](../standards/id-system.md#7-id) - 신규 ID 설계 원칙
→ 참고: [명명 규칙 §3](../standards/naming-rules.md#3-db) - DB 계층 명명 규칙
→ 참고: [도메인 타입 §2](../standards-dict/domains.md) - 표준 타입 정의
→ 참고: [데이터 오너십 §4.1](./data-ownership.md#41) - KBO 자체 오너십

---

## 2. 설계 전 체크리스트

신규 테이블 설계를 시작하기 전에 아래 5항목을 확인한다:

| # | 체크 항목 | 확인 내용 |
|---|----------|----------|
| 1 | **중복 확인** | 기존 39종 테이블에 동일/유사 데이터가 없는가? `dictionary/` 검색 |
| 2 | **데이터 출처** | 원천 데이터(S2i, KBO 자체 산출, 외부 API)가 명확한가? |
| 3 | **FK 관계** | 기존 테이블과의 FK 참조 관계가 정의되었는가? |
| 4 | **갱신 주기** | 실시간, 경기 후, 일간, 시즌 종료 중 어떤 주기로 갱신되는가? |
| 5 | **데이터 규모** | 연간 예상 행 수와 향후 5년 증가량을 산정했는가? |

---

## 3. 테이블 명명 규칙

### 3.1 기본 규칙

`UPPER_SNAKE_CASE`, 접두사로 도메인 구분:

| 접두사 | 용도 | 예시 |
|--------|------|------|
| `PITCH_` | Pitch-by-pitch 관련 | `PITCH_BY_PITCH`, `PITCH_TYPE_MASTER` |
| `SABER_` | 세이버메트릭스 관련 | `SABER_HITTER_SEASON`, `SABER_PITCHER_SEASON` |
| `KBO_OPS_` | KBO 운영 자체 | `KBO_OPS_AUDIT_LOG`, `KBO_OPS_WEIGHT_PARAM` |

### 3.2 명명 금지 사항

| 금지 | 사유 | 대안 |
|------|------|------|
| 한글 테이블명 | MSSQL 호환 문제 | 영문 UPPER_SNAKE |
| 공백 포함 | SQL 구문 오류 위험 | 언더스코어 사용 |
| 예약어 (ORDER, INDEX 등) | SQL 예약어 충돌 | 접두사/접미사 추가 |
| 30자 초과 | 가독성 저하 | 약어 사용 (abbreviations.md 참조) |

→ 참고: [명명 규칙 §3.1](../standards/naming-rules.md#31)
→ 참고: [약어 사전](../standards-dict/abbreviations.md)

---

## 4. PK 및 ID 설계 원칙

### 4.1 자연키 우선

의미 있는 자연키가 존재하면 사용한다. KBO 데이터는 대부분 자연키가 명확하다.

| 예시 | 자연키 | 사유 |
|------|--------|------|
| 시즌 타자 세이버 | `season_yr`, `player_id` | 시즌+선수로 유일 |
| Pitch-by-pitch | `game_id`, `season_yr`, `seq_no` | 경기+순번으로 유일 |
| 구종 마스터 | `pitch_type_cd` | 코드값 자체가 유일 |

### 4.2 대리키 사용 조건

자연 복합키가 **3개를 초과**하면 대리키(`bigint IDENTITY`) 사용을 검토한다.

| 조건 | 대리키 사용 |
|------|-----------|
| 복합키 3개 이하 | 자연키 유지 |
| 복합키 4개 이상 | 대리키 추가 검토 |
| FK로 자주 참조 | 대리키 추가 검토 (조인 성능) |

> **UUID 비권장**: 현 시스템 규모(연간 ~21.6만 투구, ~5.7만 타석)에서 UUID는 불필요. 자연키가 인간 가독성이 높다.

### 4.3 FK 이름 일치

외래키 컬럼명은 참조 테이블의 PK 컬럼명과 **동일**하게 한다.

| FK 컬럼 | 참조 테이블 | PK 컬럼 | 일치 |
|---------|-----------|---------|------|
| `game_id` | GAME_INFO | `game_id` | O |
| `player_id` | PERSON | `player_id` | O |
| `pitcher_id` | PERSON | `player_id` | X → 역할별 alias 허용 |

> **역할별 alias**: 같은 테이블을 여러 번 참조할 때 `pitcher_id`, `batter_id` 등 역할 접미사를 사용한다. 이 경우 FK 제약조건 이름으로 참조 관계를 명시한다.

### 4.4 복합 PK 컬럼 순서

카디널리티가 **낮은 것부터** 나열한다 (인덱스 효율):

```
좋은 예: league_id → series_id → game_id → seq_no
나쁜 예: seq_no → game_id → series_id → league_id
```

→ 참고: [ID 체계 §3](../standards/id-system.md#3-pk) - 복합 PK 기준

---

## 5. 컬럼 설계 표준

### 5.1 필수 감사 컬럼

모든 KBO 자체 신규 테이블에 아래 3개 감사 컬럼을 **필수**로 포함한다:

| 컬럼명 | 타입 | NOT NULL | 기본값 | 설명 |
|--------|------|----------|--------|------|
| `reg_dt` | `datetime2` | 필수 | `DEFAULT GETDATE()` | 행 최초 등록 일시 |
| `upd_dt` | `datetime2` | 필수 | `DEFAULT GETDATE()` | 행 최종 수정 일시 (트리거 갱신) |
| `reg_user_id` | `varchar(50)` | 필수 | - | 등록자 ID |

> 신규 테이블만 적용. 기존 테이블 소급은 본 정의서 범위 외 - DAR-009 마이그레이션 시 판단.

### 5.2 타입 표준

| 데이터 종류 | 표준 MSSQL 타입 | 비고 |
|------------|----------------|------|
| 한글 텍스트 | `nvarchar(N)` | varchar 금지 |
| 영문 코드 | `varchar(N)` 또는 `char(N)` | 고정길이면 char |
| 정수 수량 | `int` | smallint/tinyint 금지 |
| 비율/평균 | `decimal(8,5)` | float/real 금지 |
| 식별자 (숫자) | `int` 또는 `bigint` | |
| 식별자 (문자) | `char(N)` | game_id=char(13), team_id=char(2) |
| 시즌 연도 | `smallint` | |
| 불리언 | `bit` | char(1) T/F 금지 |
| 날짜 | `char(8)` (YYYYMMDD) 또는 `datetime2` | |
| 대용량 텍스트 | `nvarchar(max)` | |

→ 참고: [도메인 타입 §2](../standards-dict/domains.md) - 타입별 상세 정의

### 5.3 NULL 정책

| 도메인 | NOT NULL | 기본값 | 비고 |
|--------|----------|--------|------|
| PK 컬럼 | 필수 | - | |
| count (`_cn`) | 필수 | `0` | 0건과 미집계 구분 불필요 |
| flag (`_if`) | 필수 | `0` | false 기본 |
| rate (`_rt`) | 선택 | NULL | NULL=분모 없음, 0.000=분모 있으나 분자 0 |
| 감사 컬럼 | 필수 | `GETDATE()` / - | |

→ 참고: [도메인 타입 §4](../standards-dict/domains.md) - NULL 정책

### 5.4 금지 사항

| 금지 항목 | 사유 | 대안 |
|----------|------|------|
| `float`, `real` | 부동소수점 정밀도 손실 (0.258865237...) | `decimal(8,5)` |
| `tinyint` | 범위 초과 위험 (0~255) | `int` |
| `smallint` (수량용) | 범위 초과 위험 (-32768~32767) | `int` |
| `varchar` + 한글 | EUC-KR 인코딩 깨짐 | `nvarchar` |
| `char(1)` 불리언 | 'T'/'F' 비표준 | `bit` |
| `text`, `ntext` | 레거시 타입 (MSSQL 권장 안 함) | `nvarchar(max)` |
| `money` | 화폐 연산 부정확 | `decimal` |

→ 참고: [컬럼 매핑](../migration/column-mapping.md) - 현행 타입 분포 및 문제점

---

## 6. 인덱스 설계 가이드

| 원칙 | 설명 |
|------|------|
| **PK 인덱스** | 자동 생성 (클러스터드). 복합 PK는 카디널리티 낮은 순서 |
| **FK 인덱스** | 모든 FK 컬럼에 논클러스터드 인덱스 생성 |
| **조회 패턴** | 빈번한 WHERE 조건에 복합 인덱스 추가 |
| **커버링 인덱스** | 자주 조회하는 소수 컬럼은 INCLUDE로 커버링 |
| **과도한 인덱스 금지** | 테이블당 인덱스 5개 이하 권고 (쓰기 성능 유지) |

**세이버메트릭스 테이블 인덱스 예시**:

```sql
-- PK (클러스터드)
PRIMARY KEY (season_yr, player_id)

-- 팀별 조회 (비클러스터드)
CREATE INDEX IX_SABER_HITTER_SEASON_TEAM ON SABER_HITTER_SEASON (season_yr, team_cd)

-- 지표별 상위 랭킹 조회
CREATE INDEX IX_SABER_HITTER_SEASON_WAR ON SABER_HITTER_SEASON (season_yr, war_va DESC)
```

---

## 7. 세이버메트릭스 테이블 설계 패턴

### 7.1 대상 지표

본 정의서 범위 외 - KBO 분석팀 협의 후 우선순위 확정. 아래는 후보 지표 목록.

| 범주 | 지표 | 약어 | 용도 |
|------|------|------|------|
| **타자 공격** | Weighted On-Base Average | wOBA | 타자 출루 가중 평가 |
| | Weighted Runs Created Plus | wRC+ | 리그 평균 대비 타자 생산력 (100 = 리그 평균) |
| | Isolated Power | ISO | 순수 장타력 (SLG - AVG) |
| | Batting Runs | BatR | 타격 기여 런 |
| **타자 주루** | Base Running Runs | BsR | 주루 기여 런 |
| **수비** | Defensive Runs Saved | DRS | 수비 기여 런 |
| | Ultimate Zone Rating | UZR | 수비 범위 런 |
| **투수** | Fielding Independent Pitching | FIP | 수비 독립 투구 지표 |
| | Expected FIP | xFIP | FIP에서 홈런 정규화 |
| | Skill-Interactive ERA | SIERA | 투구 능력 기반 ERA |
| **종합** | Wins Above Replacement | WAR | 대체 선수 대비 승리 기여 |

### 7.2 타자 시즌 테이블 예시 (SABER_HITTER_SEASON)

```sql
CREATE TABLE SABER_HITTER_SEASON (
    -- PK
    season_yr       smallint    NOT NULL,
    player_id       int         NOT NULL,

    -- FK 참조
    team_cd         char(2)     NOT NULL,   -- FK → TEAM (시즌별 소속팀)

    -- 출루 지표
    woba_rt         decimal(8,5)  NULL,     -- Weighted On-Base Average
    wrc_plus_va     decimal(8,2)  NULL,     -- wRC+ (100 = 리그 평균)
    wraa_va         decimal(8,2)  NULL,     -- Weighted Runs Above Average
    wrc_va          decimal(8,2)  NULL,     -- Weighted Runs Created

    -- 주루 지표
    bsr_va          decimal(8,2)  NULL,     -- Base Running Runs
    spd_va          decimal(8,2)  NULL,     -- Speed Score

    -- 수비 지표
    drs_va          decimal(8,2)  NULL,     -- Defensive Runs Saved
    uzr_va          decimal(8,2)  NULL,     -- Ultimate Zone Rating
    uzr_per150_va   decimal(8,2)  NULL,     -- UZR/150

    -- 종합
    war_va          decimal(8,2)  NULL,     -- Wins Above Replacement (위치선수)
    off_war_va      decimal(8,2)  NULL,     -- Offensive WAR
    def_war_va      decimal(8,2)  NULL,     -- Defensive WAR

    -- 감사 컬럼
    reg_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    upd_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    reg_user_id     varchar(50) NOT NULL,

    CONSTRAINT PK_SABER_HITTER_SEASON
        PRIMARY KEY (season_yr, player_id)
);
```

### 7.3 투수 시즌 테이블 예시 (SABER_PITCHER_SEASON)

```sql
CREATE TABLE SABER_PITCHER_SEASON (
    -- PK
    season_yr       smallint    NOT NULL,
    player_id       int         NOT NULL,

    -- FK 참조
    team_cd         char(2)     NOT NULL,

    -- 독립 투구 지표
    fip_rt          decimal(8,5)  NULL,     -- Fielding Independent Pitching
    xfip_rt         decimal(8,5)  NULL,     -- Expected FIP
    siera_rt        decimal(8,5)  NULL,     -- SIERA
    kwera_rt        decimal(8,5)  NULL,     -- K-W ERA (삼진-볼넷 기반)

    -- 구성 지표
    k_pct_rt        decimal(8,5)  NULL,     -- K% (삼진율)
    bb_pct_rt       decimal(8,5)  NULL,     -- BB% (볼넷율)
    hr_per_9_rt     decimal(8,5)  NULL,     -- HR/9
    k_bb_pct_rt     decimal(8,5)  NULL,     -- K-BB%
    lob_pct_rt      decimal(8,5)  NULL,     -- LOB% (잔루율)
    gb_pct_rt       decimal(8,5)  NULL,     -- GB% (땅볼비율)

    -- 타구 질
    babip_rt        decimal(8,5)  NULL,     -- Opp BABIP

    -- 종합
    war_va          decimal(8,2)  NULL,     -- Wins Above Replacement (투수)
    ra9_war_va      decimal(8,2)  NULL,     -- RA9-WAR

    -- 감사 컬럼
    reg_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    upd_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    reg_user_id     varchar(50) NOT NULL,

    CONSTRAINT PK_SABER_PITCHER_SEASON
        PRIMARY KEY (season_yr, player_id)
);
```

### 7.4 계산 공식 표준화 + 가중치 파라미터 테이블

세이버메트릭스 계산에 필요한 리그 평균·가중치는 시즌별로 변동한다. 하드코딩 대신 **파라미터 테이블**에서 관리한다.

```sql
CREATE TABLE KBO_OPS_WEIGHT_PARAM (
    -- PK
    season_yr       smallint    NOT NULL,
    param_cd        varchar(30) NOT NULL,   -- 파라미터 코드

    -- 값
    param_va        decimal(10,5) NOT NULL, -- 파라미터 값
    description     nvarchar(200) NULL,     -- 설명

    -- 감사
    reg_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    upd_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    reg_user_id     varchar(50) NOT NULL,

    CONSTRAINT PK_KBO_OPS_WEIGHT_PARAM
        PRIMARY KEY (season_yr, param_cd)
);
```

**파라미터 예시** (2025시즌):

| season_yr | param_cd | param_va | description |
|-----------|----------|----------|-------------|
| 2025 | `WOBA_BB_WT` | 0.69200 | wOBA 볼넷 가중치 |
| 2025 | `WOBA_HBP_WT` | 0.72200 | wOBA 사구 가중치 |
| 2025 | `WOBA_1B_WT` | 0.88400 | wOBA 1루타 가중치 |
| 2025 | `WOBA_2B_WT` | 1.26200 | wOBA 2루타 가중치 |
| 2025 | `WOBA_3B_WT` | 1.59400 | wOBA 3루타 가중치 |
| 2025 | `WOBA_HR_WT` | 2.03100 | wOBA 홈런 가중치 |
| 2025 | `WOBA_SCALE` | 1.15000 | wOBA → wRC 변환 계수 |
| 2025 | `LG_R_PA` | 0.11000 | 리그 평균 R/PA |
| 2025 | `FIP_CONST` | 3.10000 | FIP 보정 상수 (cFIP) |
| 2025 | `RPW` | 9.50000 | Runs Per Win (WAR 변환) |

> 가중치는 시즌 종료 후 리그 전체 데이터 기반으로 산출한다. 산출 공식은 FanGraphs/Baseball Reference 방법론을 KBO에 적용.

---

## 8. Pitch-by-Pitch 테이블 설계 패턴

### 8.1 설계 원칙

| 항목 | 수치 |
|------|------|
| 경기당 평균 투구수 | ~300구 (양팀 합산) |
| 연간 경기수 | ~720경기 (정규시즌) |
| **연간 예상 행 수** | **~216,000행** |
| 5년 누적 | ~1,080,000행 |
| 행당 예상 크기 | ~200 bytes |
| 연간 용량 | ~43 MB |

> 데이터 규모가 크지 않으므로 파티셔닝은 불필요. 시즌별 인덱스로 충분.

### 8.2 기준 설계 예시 (PITCH_BY_PITCH)

```sql
CREATE TABLE PITCH_BY_PITCH (
    -- PK
    game_id         char(13)    NOT NULL,   -- FK → GAME_INFO
    season_yr       smallint    NOT NULL,
    seq_no          int         NOT NULL,   -- 투구 순번 (경기 내 전체 순번)

    -- 이닝 정보
    inning_no       int         NOT NULL,   -- 이닝 번호
    top_bottom_cd   char(1)     NOT NULL,   -- T=초, B=말

    -- 대결 정보
    pitcher_id      int         NOT NULL,   -- FK → PERSON (투수)
    batter_id       int         NOT NULL,   -- FK → PERSON (타자)
    bat_order_no    int         NOT NULL,   -- 타순 (1~9)

    -- 투구 정보
    pitch_type_cd   varchar(10) NULL,       -- 구종 코드 (§8.3)
    pitch_speed_va  int         NULL,       -- 구속 (km/h)
    pitch_result_cd varchar(10) NOT NULL,   -- 투구 결과 (STRIKE, BALL, FOUL, IN_PLAY, HBP)

    -- 존 위치 (좌표)
    zone_x_va       decimal(6,3) NULL,      -- 존 X 좌표 (-1.5 ~ 1.5, 단위: 피트)
    zone_y_va       decimal(6,3) NULL,      -- 존 Y 좌표 (0 ~ 5.0, 단위: 피트)

    -- 카운트 (투구 전 상태)
    ball_cn         int         NOT NULL DEFAULT 0,  -- 볼 카운트 (0~3)
    strike_cn       int         NOT NULL DEFAULT 0,  -- 스트라이크 카운트 (0~2)
    out_cn          int         NOT NULL DEFAULT 0,  -- 아웃 카운트 (0~2)

    -- 주자 상태 (투구 전)
    runner_1b_if    bit         NOT NULL DEFAULT 0,  -- 1루 주자 유무
    runner_2b_if    bit         NOT NULL DEFAULT 0,  -- 2루 주자 유무
    runner_3b_if    bit         NOT NULL DEFAULT 0,  -- 3루 주자 유무

    -- 타석 결과 (마지막 투구에만)
    pa_result_cd    varchar(10) NULL,       -- 타석 결과 (how_cd 매핑, 마지막 투구만)

    -- 감사 컬럼
    reg_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    upd_dt          datetime2   NOT NULL DEFAULT GETDATE(),
    reg_user_id     varchar(50) NOT NULL,

    CONSTRAINT PK_PITCH_BY_PITCH
        PRIMARY KEY (game_id, season_yr, seq_no),

    CONSTRAINT FK_PBP_GAME FOREIGN KEY (game_id)
        REFERENCES GAME_INFO (game_id),
    CONSTRAINT FK_PBP_PITCHER FOREIGN KEY (pitcher_id)
        REFERENCES PERSON (player_id),
    CONSTRAINT FK_PBP_BATTER FOREIGN KEY (batter_id)
        REFERENCES PERSON (player_id)
);

-- 인덱스
CREATE INDEX IX_PBP_PITCHER ON PITCH_BY_PITCH (season_yr, pitcher_id);
CREATE INDEX IX_PBP_BATTER ON PITCH_BY_PITCH (season_yr, batter_id);
CREATE INDEX IX_PBP_INNING ON PITCH_BY_PITCH (game_id, inning_no, top_bottom_cd);
```

### 8.3 구종 코드 정의

본 정의서 범위 외 - MLBam 기준 초안이며, 기록위원회 확정 후 최종 적용.

| pitch_type_cd | 한글 | 영문 | 약어 |
|---------------|------|------|------|
| `FF` | 포심 패스트볼 | Four-Seam Fastball | 4S |
| `FT` | 투심 패스트볼 | Two-Seam Fastball | 2S |
| `FC` | 커터 | Cutter | CT |
| `SI` | 싱커 | Sinker | SI |
| `SL` | 슬라이더 | Slider | SL |
| `CU` | 커브 | Curveball | CB |
| `CH` | 체인지업 | Changeup | CH |
| `FS` | 스플리터 | Splitter | SP |
| `KN` | 너클볼 | Knuckleball | KN |
| `EP` | 이팩투스 | Eephus | EP |

> 구종 분류는 MLBam Pitch Classification을 기반으로 하되, KBO 기록위원회 확정 후 최종 적용.

---

## 9. 테이블 설계 승인 절차 (6단계)

| 단계 | 행위자 | 산출물 | 기한 |
|------|--------|--------|------|
| 1. 설계 초안 | R-06 (데이터팀) | DDL 스크립트 + 컬럼 설명서 | - |
| 2. 체크리스트 검증 | R-06 (데이터팀) | §2 체크리스트 + §10 검증 결과 | 2영업일 |
| 3. 영향 분석 | R-06 (데이터팀) | FK 관계도, API 설계(안), 용량 산정 | 3영업일 |
| 4. 리뷰 | R-05 (거버넌스 위원회) | 리뷰 코멘트, 승인/반려/수정요청 | 5영업일 |
| 5. DB 생성 | R-04 (DBA) | 실제 테이블 생성, 인덱스, 권한 설정 | 2영업일 |
| 6. 문서 반영 | R-06 (데이터팀) | `dictionary/` 파일 추가, CLAUDE.md 갱신 | 2영업일 |

→ 참고: [변경 절차 §5](./change-process.md#5) - 스키마 변경 일반 절차

---

## 10. 체크리스트 요약

### 10.1 설계 체크리스트

| # | 항목 | 확인 |
|---|------|------|
| 1 | 테이블명이 `UPPER_SNAKE_CASE`이고 적절한 접두사(`PITCH_`/`SABER_`/`KBO_OPS_`) 사용 | [ ] |
| 2 | 모든 컬럼명이 `lower_snake_case`이고 접미사 규칙 준수 | [ ] |
| 3 | PK가 자연키 우선으로 설계됨 (대리키 사용 시 사유 명시) | [ ] |
| 4 | FK 컬럼명이 참조 PK 컬럼명과 일치 | [ ] |
| 5 | 감사 컬럼 3개(`reg_dt`, `upd_dt`, `reg_user_id`) 포함 | [ ] |
| 6 | `float`/`real`/`tinyint`/`smallint`(수량용)/`varchar`(한글) 사용하지 않음 | [ ] |
| 7 | count 컬럼 NOT NULL DEFAULT 0, flag 컬럼 NOT NULL DEFAULT 0 | [ ] |
| 8 | rate 컬럼은 `decimal(8,5)`, NULL 허용 (분모 없음 구분) | [ ] |
| 9 | 한글 가능 컬럼은 모두 `nvarchar` | [ ] |

### 10.2 검토 체크리스트

| # | 항목 | 확인 |
|---|------|------|
| 1 | 기존 테이블과 중복 데이터 없음 | [ ] |
| 2 | FK 참조 무결성 테스트 통과 | [ ] |
| 3 | 예상 데이터 규모 산정 완료 | [ ] |
| 4 | 주요 조회 패턴에 맞는 인덱스 설계됨 | [ ] |
| 5 | API 필드 변환(camelCase) 시 충돌 없음 | [ ] |

### 10.3 배포 체크리스트

| # | 항목 | 확인 |
|---|------|------|
| 1 | DDL이 dev/staging에서 테스트 완료 | [ ] |
| 2 | `dictionary/{domain}/{table}.md` 파일 생성 | [ ] |
| 3 | `glossary/business-terms.md`에 신규 용어 추가 (필요 시) | [ ] |
| 4 | 변경 요청서(CR) 작성 및 승인 완료 | [ ] |
| 5 | CLAUDE.md 갱신 (테이블 수, 폴더 구조) | [ ] |

---

## Appendix: 레거시 vs KBO 자체 차이점 비교

| 항목 | 레거시 (S2i 테이블) | KBO 자체 (신규) |
|------|-------------------|----------------|
| 데이터 생성 | S2i 운영 시스템 | KBO 자체 산출/수집 |
| 스키마 변경 | S2i 협의 필요 | KBO 자체 관리 (R-05 승인) |
| ID 체계 | 구세대(GMKEY/PCODE) + 신세대(G_ID/P_ID) 혼재 | 표준 ID만 사용 (game_id, player_id 등) |
| 명명 규칙 | 불일치 (PascalCase, UPPER, mixed) | lower_snake_case 엄격 적용 |
| 감사 컬럼 | 대부분 없음 (INPUTTIME 일부) | 필수 3개 (reg_dt, upd_dt, reg_user_id) |
| 타입 표준 | float, tinyint, varchar 한글 등 혼재 | 표준 타입만 사용 (§5.2) |
| NULL 정책 | 비일관 | 도메인 타입별 일관 적용 (§5.3) |
| 인코딩 | EUC-KR 깨짐 (varchar+한글) | nvarchar 의무 |
| 합계행 | T/B 혼재 (§7, data-ownership.md) | 합계행 분리 (별도 집계 테이블/뷰) |
