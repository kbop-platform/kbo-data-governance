# 데이터 품질 규칙

> 최종수정: 2026-02-24 | KBO 데이터 표준 정의서 (RFP DAR-001)

## 1. 개요

본 문서는 KBO 데이터 시스템의 **수신·저장·집계** 전 단계에서 적용하는 데이터 품질 검증 규칙을 정의한다.
각 규칙에는 심각도를 명시하여 위반 시 처리 우선순위를 결정한다.

### 1.1 적용 시점

| 시점 | 설명 | 적용 규칙 |
|------|------|----------|
| **수신 시** | S2i → DB2 데이터 전송 직후 | §2~5 (필수필드, 형식, 수치, 인코딩) |
| **확정 시** | REVIEW → CONFIRMED 전이 전 | §6 (정합성 검증) |
| **배치 시** | 일간/주간 품질 점검 | §8 (KPI 측정) |
| **마이그레이션 시** | DB2 → DB1, 레거시 → 신규 | §2~7 전체 |

### 1.2 심각도 분류

| 심각도 | 의미 | 처리 |
|--------|------|------|
| **CRITICAL** | 데이터 무결성 파괴, 서비스 장애 가능 | **즉시 차단**: 해당 행 저장 불가, 담당자(R-04 DBA) 즉시 통보 |
| **WARNING** | 의심스러운 값, 추가 확인 필요 | **기록 후 통과**: 저장은 허용하되 품질 로그에 기록, 일간 리포트에 포함 |
| **INFO** | 권고 사항, 개선 대상 | **기록만**: 품질 로그에 기록, 주간/월간 리포트에 포함 |

→ 참고: [데이터 오너십 §3](./data-ownership.md#3) — 역할별 위반 처리 책임
→ 참고: [도메인 타입 정의](../standards/domain-types.md) — 타입별 허용 범위

---

## 2. 필수 필드 검증 (NOT NULL)

### 2.1 PK 필드 — CRITICAL

모든 테이블의 PK 구성 컬럼은 NULL을 허용하지 않는다.

| 테이블 | PK 구성 | 검증 규칙 |
|--------|---------|----------|
| GAME_INFO | `game_id` | NOT NULL, 13자 고정 |
| HITTER | `game_id`, `season_yr`, `player_id` | 모두 NOT NULL |
| PITCHER | `game_id`, `season_yr`, `player_id` | 모두 NOT NULL |
| GAME_CONT_APP | `game_id`, `season_yr`, `seq_no` | 모두 NOT NULL |
| ENTRY | `game_id`, `season_yr`, `turn_no`, `player_id`, `position_cd` | 모두 NOT NULL |
| BAT_TOTAL | `season_yr`, `player_id`, `series_cd` | 모두 NOT NULL |
| PIT_TOTAL | `season_yr`, `player_id`, `series_cd` | 모두 NOT NULL |
| SCORE | `game_id`, `season_yr`, `top_bottom_cd` | 모두 NOT NULL |
| PERSON | `season_yr`, `player_id` | 모두 NOT NULL |

> **위반 시**: 해당 행 저장을 **차단**하고 R-04(DBA)에 즉시 통보.

### 2.2 도메인별 필수 필드 — CRITICAL / WARNING

| 도메인 타입 | NOT NULL 정책 | 기본값 | 심각도 |
|------------|--------------|--------|--------|
| count (`_cn`) | 필수 | `0` | **CRITICAL** (NULL 수량은 집계 오류 유발) |
| flag (`_if`) | 필수 | `0` (false) | **CRITICAL** |
| identifier (`_id`) | PK이면 필수 | — | **CRITICAL** |
| rate (`_rt`) | 선택 | NULL | — (NULL = 분모 없음) |
| name (`_nm`) | 선택 | NULL | — |
| code (`_cd`, `_sc`) | 선택 | NULL | — (NULL = 해당없음) |

→ 참고: [도메인 타입 §6](../standards/domain-types.md#6-null) — NULL 처리 정책

---

## 3. 형식 검증

### 3.1 game_id 형식 — CRITICAL

| 항목 | 규칙 |
|------|------|
| 길이 | 정확히 13자 |
| 형식 | `YYYYMMDDVVHH#` |
| YYYY | 1982~현재 연도 또는 `9999` (특별 경기) |
| MMDD | 01~12, 01~31 (유효 날짜) |
| VV | 원정팀 코드 — 유효 team_id (`HH`,`HT`,`KT`,`LG`,`LT`,`NC`,`OB`,`SK`,`SS`,`WO` + 역사팀 + 국제팀) |
| HH | 홈팀 코드 — 동일 |
| # | 더블헤더 번호 — `0`, `1`, `2` |

```
유효 예시: 20250322HHKT0, 99900725EAWE0
무효 예시: 2025032HHKT0 (12자), 20251322HHKT0 (월 13)
```

### 3.2 player_id 형식 — CRITICAL

| 항목 | 규칙 |
|------|------|
| 타입 | 정수 (표준: int) |
| 범위 | 10005 ~ 99999 (정상 선수) |
| 특수값 | `'T'`, `'B'` (레거시 합계행) → 마이그레이션 시 -1, -2로 전환 |
| 검증 | `player_id > 0 OR player_id IN (-1, -2)` |

### 3.3 날짜/시각 형식 — WARNING

| 컬럼 유형 | 저장 형식 | 검증 |
|----------|----------|------|
| `_dt` (날짜) | `char(8)` YYYYMMDD | 유효 날짜 파싱 가능 여부 |
| `_dt` (일시) | `datetime2` | MSSQL 유효 범위 내 |
| `_tm` (시각) | `char(4)` HHMM | HH: 00~23, MM: 00~59 |
| `_tm` (시간량) | `int` (분) | 0 이상 |

### 3.4 코드값 허용 범위 — CRITICAL / WARNING

| 코드 | 허용값 | 심각도 | 비고 |
|------|--------|--------|------|
| `top_bottom_cd` | `T`, `B` | **CRITICAL** | 2값만 허용 |
| `how_cd` | §2.2에 정의된 49종 | **CRITICAL** (미등록 값) | BH 제외 (§9) |
| `place_cd` | `0`~`9`, `78`, `89`, `F`, `S` | **WARNING** (미확인 문자코드) | R, A~I 한시적 수용 (§9) |
| `wls_cd` | `W`, `L`, `S`, `''`(빈값) | **CRITICAL** | |
| `out_count` | `0`, `1`, `2`, `4` | **CRITICAL** | 3은 무효 |
| `weather_cd` | `F`,`C`,`R`,`CR`,`FC`,`CF`,`RC`,`FR`,`W`,`SE`,`S` | **WARNING** | |
| `position_cd` | `X` + `Y` — X: 1~9, Y: 1~9/D/H/R | **CRITICAL** | 2자리 형식 |
| `game_type_cd` | `0`,`1`,`3`,`5` | **WARNING** (4,7,8,9 미확인) | §9 참조 |
| `record_status_cd` | `DRAFT`,`REVIEW`,`CONFIRMED`,`REVISED` | **CRITICAL** | 신규 시스템 |

→ 참고: [코드 사전](../standards/code-dictionary.md) — 전체 코드값 정의

---

## 4. 수치 범위 검증

### 4.1 count 컬럼 범위

| 컬럼 (표준명) | 최소값 | 최대값 | 심각도 | 비고 |
|-------------|--------|--------|--------|------|
| `pa` (타석) | 0 | 15 (경기), 900 (시즌) | **WARNING** | 경기 단위 15 초과 = 이상치 |
| `ab` (타수) | 0 | 15 (경기), 700 (시즌) | **WARNING** | |
| `hit` (안타) | 0 | 10 (경기), 250 (시즌) | **WARNING** | |
| `hr` (홈런) | 0 | 5 (경기), 80 (시즌) | **WARNING** | |
| `rbi` (타점) | 0 | 15 (경기), 200 (시즌) | **WARNING** | |
| `bb` (볼넷) | 0 | 6 (경기), 200 (시즌) | **WARNING** | |
| `so` (삼진) | 0 | 6 (경기 타자), 27 (경기 투수) | **WARNING** | |
| `ip` (이닝) | 0 | 15 (경기), 250 (시즌) | **WARNING** | |
| `pitch_cn` (투구수) | 0 | 200 (경기) | **WARNING** | 170 이상 = 이상치 |
| `crowd_cn` (관중) | 0 | 70,000 | **WARNING** | 최대 수용 인원 |
| `out_count` | 0 | 4 | **CRITICAL** | 0, 1, 2, 4만 허용 |
| 이닝 점수 (`inn_*`) | -1 | 99 | **WARNING** | -1=미진행, 0~99=정상 |
| `seq_no` (순번) | 1 | 999 | **WARNING** | 경기당 최대 이벤트 수 |

### 4.2 rate 컬럼 범위

| 컬럼 (표준명) | 최소값 | 최대값 | 정밀도 | 심각도 |
|-------------|--------|--------|--------|--------|
| `avg_rt` (타율) | 0.00000 | 1.00000 | decimal(8,5) | **CRITICAL** (범위 초과) |
| `obp_rt` (출루율) | 0.00000 | 1.00000 | decimal(8,5) | **CRITICAL** |
| `slg_rt` (장타율) | 0.00000 | 5.00000 | decimal(8,5) | **WARNING** (이론 최대) |
| `ops_rt` (OPS) | 0.00000 | 6.00000 | decimal(8,5) | **WARNING** |
| `era_rt` (ERA) | 0.00000 | 99.99000 | decimal(8,5) | **WARNING** (54.00 이상 = 이상치) |
| `whip_rt` (WHIP) | 0.00000 | 20.00000 | decimal(8,5) | **WARNING** |

**float 노이즈 검출** — WARNING:
현행 시스템에서 `float` 타입으로 저장된 비율값은 부동소수점 노이즈가 발생한다.
- 예: `0.25886523723602295` → 유효 자릿수 17자리 = float 노이즈
- 검증: `ABS(value - ROUND(value, 5)) > 0.000001` 이면 **WARNING**
- 조치: 마이그레이션 시 `decimal(8,5)`로 전환, `ROUND(value, 5)` 적용

→ 참고: [도메인 타입 §3.5](../standards/domain-types.md#35-rate-_rt) — rate 타입 정의

---

## 5. 인코딩 검증

### 5.1 한글 컬럼 nvarchar 의무

| 검증 대상 | 현행 타입 | 표준 타입 | 심각도 |
|----------|----------|----------|--------|
| `person.NAME` | varchar(20) | nvarchar(100) | **CRITICAL** (마이그레이션) / WARNING (운영) |
| `person.CAREER` | varchar(255) | nvarchar(500) | **CRITICAL** / WARNING |
| `GAMEINFO.STADIUM` | varchar(20) | nvarchar(100) | **CRITICAL** / WARNING |
| `GAMECONTAPP.HITNAME` | varchar | nvarchar(100) | **CRITICAL** / WARNING |
| `GAMECONTAPP.PITNAME` | varchar | nvarchar(100) | **CRITICAL** / WARNING |
| `GAMECONTAPP.CATNAME` | varchar | nvarchar(100) | **CRITICAL** / WARNING |
| `CANCEL_GAME.CANCEL_SC_NM` | varchar | nvarchar(200) | **CRITICAL** / WARNING |
| `TeamRank.TEAM` | varchar | nvarchar(100) | **CRITICAL** / WARNING |

> **마이그레이션 시**: varchar→nvarchar 전환은 CRITICAL (필수).
> **현행 운영 시**: 기존 varchar 컬럼의 EUC-KR 깨짐은 WARNING (기록 후 통과).

→ 참고: [도메인 타입 §5](../standards/domain-types.md#5) — 인코딩 정책

### 5.2 코드 컬럼 ASCII 검증 — WARNING

코드 컬럼(`_cd`, `_sc`)에 비ASCII 문자(한글 등) 포함 여부 검증:

| 검증 대상 | 기대값 | 위반 예시 |
|----------|--------|----------|
| `team_id` | 영문 대문자 2자 | 한글 팀명 저장 |
| `how_cd` | 영문 대문자 2자 | 한글 코드 |
| `bat_throw_cd` | 영문 2자 (RR,LL 등) | 한글 "우투우타" (레거시) |

> 레거시 `bat_throw_cd`(HITTYPE)는 현재 한글 값 저장. 마이그레이션 시 영문 코드로 전환.

---

## 6. 정합성 검증 (Cross-table)

### 6.1 FK 참조 무결성 — CRITICAL

| 자식 테이블 | FK 컬럼 | 부모 테이블 | PK 컬럼 | 검증 |
|-----------|---------|-----------|---------|------|
| HITTER | `game_id` | GAME_INFO | `game_id` | 존재 여부 |
| HITTER | `player_id` | PERSON | `player_id` | 존재 여부 (합계행 제외) |
| PITCHER | `game_id` | GAME_INFO | `game_id` | 존재 여부 |
| PITCHER | `player_id` | PERSON | `player_id` | 존재 여부 (합계행 제외) |
| SCORE | `game_id` | GAME_INFO | `game_id` | 존재 여부 |
| ENTRY | `game_id` | GAME_INFO | `game_id` | 존재 여부 |
| ENTRY | `player_id` | PERSON | `player_id` | 존재 여부 |
| GAME_CONT_APP | `game_id` | GAME_INFO | `game_id` | 존재 여부 |
| GAME_HR | `game_id` | GAME_INFO | `game_id` | 존재 여부 |
| BAT_TOTAL | `player_id` | PERSON | `player_id` | 존재 여부 |

> **합계행 예외**: HITTER/PITCHER에서 `player_id IN (-1, -2)` (레거시: PCODE='T','B')는 FK 검증 제외.

### 6.2 집계 정합성 — WARNING

팀 합계행과 개인 기록 합산의 일치 여부:

| 검증 | 수식 | 대상 테이블 |
|------|------|-----------|
| 타자 팀 합계 | `SUM(hit) WHERE player_id > 0 AND top_bottom_cd = 'T'` = `hit WHERE player_id = -1` | HITTER |
| 투수 팀 합계 | `SUM(er) WHERE player_id > 0 AND top_bottom_cd = 'T'` = `er WHERE player_id = -1` | PITCHER |
| 시즌 통산 | `SUM(hit_cn) WHERE season_yr != 9999` ≈ `hit_cn WHERE season_yr = 9999` | BAT_TOTAL |
| 팀 순위 합계 | `SUM(win) 전체 팀` = `SUM(loss) 전체 팀` (무승부 제외) | TEAM_RANK |

> 부동소수점 비율 컬럼(`_rt`)은 반올림 차이 허용: `ABS(차이) < 0.001`

### 6.3 이닝 연속성 — WARNING

GAMECONTAPP 테이블의 이벤트 순서 검증:

| 검증 | 규칙 |
|------|------|
| seq_no 연속 | 동일 game_id 내에서 seq_no가 1부터 순차 증가 |
| 이닝 순서 | inning_no는 비감소 (같은 이닝 내 여러 이벤트 가능) |
| out_count 순서 | 동일 이닝 내에서 out_count는 비감소, 4(이닝종료) 후 0으로 복귀 |
| T/B 교대 | 이닝 내 T(초) → B(말) 순서 |

### 6.4 통산 기록 정합성 — WARNING

BAT_TOTAL, PIT_TOTAL에서 `season_yr = 9999` (통산) 행의 검증:

| 검증 | 규칙 |
|------|------|
| 통산 합산 | 통산 수량 = 각 시즌 수량의 합 |
| 통산 비율 | 통산 비율 = 통산 합산 기준 재계산값 (반올림 차이 허용) |
| 통산 존재 | 시즌 기록이 있는 선수는 통산 행도 존재해야 함 |

---

## 7. 특수값 처리 규칙

### 7.1 -1 센티널 (이닝 미진행) — INFO

Score 테이블의 이닝 점수 컬럼에서 `-1`은 **해당 이닝 미진행**을 의미한다.

| 항목 | 규칙 |
|------|------|
| 적용 대상 | `inn_1_top` ~ `inn_25_bot` (이닝 피벗 컬럼) |
| -1 의미 | 해당 이닝이 진행되지 않음 (9회말 홈팀 리드 시 등) |
| 검증 | `-1` 이후 이닝에 `0 이상` 값이 있으면 **WARNING** (이닝 건너뛰기는 비정상) |
| 집계 시 | `-1`은 합산에서 제외. `WHERE inn_N_top >= 0` |

### 7.2 9999 예약값 (통산) — INFO

| 항목 | 규칙 |
|------|------|
| 적용 대상 | `season_yr`, `series_cd` |
| 9999 의미 | 통산(Career Total) 기록 |
| 검증 | `season_yr = 9999` 행에서 개별 경기 ID 존재 시 **CRITICAL** (통산행에 경기 단위 데이터 혼재) |
| 유의 | `9999`는 삭제하지 않는다 — 유효한 예약값 |

### 7.3 합계행 필터링 (T/B) — WARNING

| 항목 | 규칙 |
|------|------|
| 적용 대상 | HITTER, PITCHER 테이블 |
| 식별 | 레거시: `PCODE IN ('T','B')` / 표준: `player_id IN (-1, -2)` |
| 집계 시 | 합계행을 반드시 제외하지 않으면 이중 집계 발생 |
| 검증 | 집계 쿼리에 합계행 필터가 없으면 **WARNING** |

→ 참고: [ID 체계 §5.1](../standards/id-system.md#51-pcode-t-b) — 합계행 표준 처리

---

## 8. 품질 측정 지표 (KPI)

5개 핵심 KPI를 정의하여 일간/주간/월간 모니터링한다.

| # | KPI | 산식 | 목표 | 측정 주기 | 담당 |
|---|-----|------|------|----------|------|
| 1 | **완결성** (Completeness) | `1 - (NULL PK행 수 / 전체 행 수)` | 100% | 일간 | R-04 (DBA) |
| 2 | **오류율** (Error Rate) | `CRITICAL 위반 건수 / 전체 행 수` | < 0.01% | 일간 | R-04 (DBA) |
| 3 | **인코딩 정상률** | `nvarchar 한글 정상 행 수 / 한글 컬럼 전체 행 수` | > 99.9% | 주간 | R-06 (데이터팀) |
| 4 | **FK 불일치율** | `FK 참조 실패 행 수 / 자식 테이블 전체 행 수` | < 0.1% | 주간 | R-06 (데이터팀) |
| 5 | **미확정 경기 수** | `record_status_cd != 'CONFIRMED'` 경기 수 (당일 경기 제외) | 0건 (전일 이전) | 일간 | R-03 (기록위원회) |

**리포트 경로**:
- 일간: R-04 → R-06 (자동 배치)
- 주간: R-06 → R-05(거버넌스 위원회) 요약 리포트
- 월간: R-05 → KBO 경영진 대시보드 (KPI 추이)

---

## 9. 미확인 코드 한시적 처리

S2i 확인 전까지 다음 미확인 코드값은 **WARNING** 수준으로 수용한다.

| 코드 분류 | 미확인 값 | 건수 | 한시적 처리 | 확정 후 조치 |
|----------|----------|------|-----------|------------|
| `how_cd` | `BH` | 14,749 | **WARNING** 수용 (저장 허용) | 의미 확정 시 코드 사전 반영, WARNING 해제 |
| `how_cd` | `IN`, `SD` | 1, 3 | **WARNING** 수용 | 확정 또는 무효 처리 |
| `place_cd` | `R` | 1,192 | **WARNING** 수용 | 의미 확정 시 반영 |
| `place_cd` | `A`~`I` | 각 1~67 | **WARNING** 수용 | 의미 확정 시 반영 |
| `game_type_cd` | `4`, `7`, `8`, `9` | 16~240 | **WARNING** 수용 | 의미 확정 시 코드 사전 반영 |
| `series_id` | `1`~`9` (0, 15 제외) | 각 9~330 | **WARNING** 수용 | S2i 확인 후 반영 |
| `cancel_sc_id` | 0 이외 값 | — | **WARNING** 수용 | 목록 확보 후 반영 |
| `game_sc_id` | 70 이외 값 | — | **WARNING** 수용 | 목록 확보 후 반영 |

> S2i 회신 시: R-05(거버넌스 위원회) 승인 → 코드 사전 반영 → 해당 코드 WARNING 해제.

→ 참고: [코드 사전 부록C](../standards/code-dictionary.md#c) — 미확인 코드 전체 목록
→ 참고: [변경 절차 §4.2](./change-process.md#42-c3) — 미확인 코드 확정 절차
