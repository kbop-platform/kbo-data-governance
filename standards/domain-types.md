# 도메인 타입 정의

> 최종수정: 2026-02-25 | 출처: raw/column-metadata.json, analysis/naming-patterns.md

## 1. 개요

컬럼 접미사에 따른 표준 데이터 타입을 정의한다.
각 도메인 타입은 MSSQL 물리 타입, API 논리 타입, 허용 범위를 포함한다.

→ 참고: [약어 사전 Section 6](./abbreviations.md#6) — 접미사 의미 정의
→ 참고: [명명 규칙](./naming-rules.md) — 접미사 적용 규칙

→ 현행 타입 분포는 [컬럼 매핑](../migration/column-mapping.md) 참조

---

## 2. 표준 도메인 타입 정의

### 2.1 identifier (`_id`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_id` |
| 용도 | 엔티티 고유 식별자 |
| MSSQL 타입 | `char(13)` — game_id (고정 형식) |
| | `int` — player_id, league_id, series_id |
| | `char(2)` — team_id, stadium_id (고정 2자) |
| | `smallint` — season_id |
| API 타입 | `string` (숫자 ID도 문자열 직렬화) |
| NOT NULL | 필수 (PK 구성요소) |

**현행 → 표준 전환**:
| 현행 | 컬럼 | 표준 |
|------|------|------|
| varchar(10) | PCODE | int |
| char(13) | GMKEY | char(13) — 유지 |

→ 참고: [ID 체계](./id-system.md) — ID별 형식 상세 정의

### 2.2 name (`_nm`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_nm` |
| 용도 | 사람/팀/장소 등 이름 |
| MSSQL 타입 | `nvarchar(100)` — 일반 이름 |
| | `nvarchar(500)` — 경력(CAREER) 등 긴 텍스트 |
| API 타입 | `string` |
| NOT NULL | 선택 (빈 이름 허용) |

> **핵심**: 한글 포함 가능성이 있는 모든 이름 컬럼은 반드시 `nvarchar`. `varchar` 사용 금지.

**현행 → 표준 전환**:
| 현행 | 컬럼 | 표준 |
|------|------|------|
| varchar(20) | person.NAME | nvarchar(100) |
| varchar(255) | person.CAREER | nvarchar(500) |

### 2.3 code (`_cd`, `_sc`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_cd` (일반 코드), `_sc` (구분코드/상태코드) |
| 용도 | 코드 테이블 참조값, 상태 구분 |
| MSSQL 타입 | `char(2)` — 고정길이 코드 (team_cd, stadium_cd) |
| | `varchar(10)` — 가변길이 코드 (how_cd, weather_cd) |
| API 타입 | `string` |
| NOT NULL | 선택 (빈 코드 = 해당없음) |

→ 참고: [코드 사전](./code-dictionary.md) — 코드값 정의

### 2.4 count (`_cn`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_cn` |
| 용도 | 수량, 건수, 횟수 |
| MSSQL 타입 | `int` |
| API 타입 | `number` (integer) |
| NOT NULL | 필수, 기본값 `0` |

> **통일**: 현행 `smallint`, `tinyint` 모두 `int`로 표준화. 야구 통계에서 `tinyint`(0~255) 초과 가능성 존재 (관중수, 투구수 등).

**현행 → 표준 전환**:
| 현행 | 컬럼 예시 | 표준 |
|------|----------|------|
| smallint | HR, RBI, BB 등 | int |
| tinyint | SCORE_CN, INN_NO 등 | int |

> **이닝 점수 특수 케이스**: `inn_{N}_top`, `inn_{N}_bot`, `inn_{N}_score` 패턴의 피벗 컬럼(Score/KBO_BATRESULT, 이닝 1~25, 최대 50개)은 `smallint`, 범위 0~99, 미진행 이닝 = NULL.

### 2.5 rate (`_rt`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_rt` |
| 용도 | 비율, 평균, 승률 |
| MSSQL 타입 | `decimal(8,5)` |
| API 타입 | `number` (float) |
| NOT NULL | 선택 (타석 없으면 NULL — 0.000과 구분) |

> **핵심**: `float` → `decimal(8,5)` 전환. 야구 통계 정밀도 보장.
> - 타율: 0.00000 ~ 1.00000 (예: 0.34200)
> - ERA: 0.00000 ~ 99.99000 (예: 3.52000)
> - OPS: 0.00000 ~ 5.00000 (이론 최대)

**현행 → 표준 전환**:
| 현행 | 컬럼 예시 | 표준 |
|------|----------|------|
| float | HRA (타율) | decimal(8,5) |
| real | — | decimal(8,5) |

### 2.6 datetime (`_dt`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_dt` |
| 용도 | 날짜 또는 일시 |
| MSSQL 타입 | `char(8)` — 날짜만 (YYYYMMDD 형식, game_dt, birth_dt) |
| | `datetime2` — 타임스탬프 (reg_dt) |
| API 타입 | `string` (ISO 8601) |
| | 날짜: `"2025-03-22"` |
| | 일시: `"2025-03-22T18:30:00+09:00"` |
| NOT NULL | 선택 |

**현행 → 표준 전환**:
| 현행 | 컬럼 예시 | 표준 |
|------|----------|------|
| varchar(8) | GDAY, BIRTH | char(8) |
| datetime | REG_DT | datetime2 |

### 2.7 time (`_tm`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_tm` |
| 용도 | 시각 또는 시간량 |
| MSSQL 타입 | `char(4)` — 시각 (HHMM, 예: `1830`) |
| | `int` — 시간량/분 (예: `257` = 4시간 17분) |
| API 타입 | `string` — 시각 (`"18:30"` 변환) |
| | `number` — 시간량 (분 단위) |
| NOT NULL | 선택 |

### 2.8 flag (`_if`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_if` |
| 용도 | 불리언 (예/아니오) |
| MSSQL 타입 | `bit` |
| API 타입 | `boolean` |
| NOT NULL | 필수, 기본값 `0` (false) |

**현행 → 표준 전환**:
| 현행 | 컬럼 예시 | 표준 |
|------|----------|------|
| char(1) 'T'/'F' | GROUP_IF | bit (0/1) |
| varchar 'True'/'False' | cancel_flag | bit (0/1) |

> **주의**: `KBO_schedule.game_flag`는 불리언이 아님 (값: 0~9). 명칭을 `game_type_cd`로 변경 권고.

### 2.9 value (`_va`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_va` |
| 용도 | 측정값, 수치 데이터 |
| MSSQL 타입 | `int` — 정수 측정값 (기온×10, 키, 몸무게) |
| | `decimal(10,2)` — 소수점 측정값 (거리 등) |
| API 타입 | `number` |
| NOT NULL | 선택 |

**현행 컬럼 예시**:
| 컬럼 | 현행 값 | 단위 | 비고 |
|------|---------|------|------|
| temperature_va | 245 | ×10 (24.5°C) | 정수 저장, API에서 /10 변환 |
| hr_distance_va | 120 | 미터 | 홈런 비거리 |

### 2.10 number (`_no`)

| 항목 | 값 |
|------|-----|
| 접미사 | `_no` |
| 용도 | 순번, 순서, 번호 |
| MSSQL 타입 | `int` |
| API 타입 | `number` (integer) |
| NOT NULL | 필수 (PK 구성요소인 경우), 선택 (일반) |

**예시**: `seq_no`, `inning_no`, `bat_order_no`, `doubleheader_no`

### 2.11 text (접미사 없음)

| 항목 | 값 |
|------|-----|
| 접미사 | 없음 (또는 자유) |
| 용도 | 자유 텍스트, 메모 |
| MSSQL 타입 | `nvarchar(500)` — 일반 텍스트 |
| | `nvarchar(max)` — 대용량 텍스트 (LiveText 등) |
| API 타입 | `string` |
| NOT NULL | 선택 |

> 모든 텍스트 컬럼은 `nvarchar`. `varchar` 사용 금지.

---

## 3. 인코딩 정책

| 구분 | 표준 | 사유 |
|------|------|------|
| 한글 포함 컬럼 | `nvarchar` (UTF-16) | EUC-KR 깨짐 방지 |
| 코드/ID 컬럼 | `varchar` (ASCII) | 영문/숫자만 사용 |
| DB Collation | `Korean_Wansung_CI_AS` 또는 `Latin1_General_CI_AS` | MSSQL 기본 |

> 현행 → 표준 타입 전환 가이드 및 인코딩 전환 대상 컬럼 상세는 마이그레이션 문서 참고.
> → 참고: [마이그레이션 설계 결정 §1, §2](../migration/design-decisions.md)

---

## 4. NULL 처리 정책

| 도메인 타입 | NOT NULL | 기본값 | 사유 |
|------------|----------|--------|------|
| identifier (_id) | PK이면 필수 | — | PK는 NULL 불가 |
| name (_nm) | 선택 | NULL | 빈 이름 허용 |
| code (_cd, _sc) | 선택 | NULL | NULL = 해당없음 |
| count (_cn) | 필수 | `0` | 0건과 미집계 구분 불필요 |
| rate (_rt) | 선택 | NULL | NULL = 분모 없음 (타석 0) vs 0.000 (타석 있으나 안타 0) |
| datetime (_dt) | 선택 | NULL | |
| time (_tm) | 선택 | NULL | |
| flag (_if) | 필수 | `0` | false 기본 |
| value (_va) | 선택 | NULL | |
| number (_no) | PK이면 필수 | — | |
| text | 선택 | NULL | |

> **rate NULL vs 0 구분 예시**:
> - 타율 `NULL`: 시즌 중 타석 없음 (투수, 미출장)
> - 타율 `0.000`: 타석 있으나 안타 0개 (개막전 첫 경기)
