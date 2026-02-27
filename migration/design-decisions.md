# 마이그레이션 설계 결정 사항

> 최종수정: 2026-02-25 | 신규 시스템 마이그레이션 참고용
> 📋 문서 성격: 마이그레이션 설계 결정 (수행사 참고)

본 문서는 표준 정의 문서(`standards/`)에서 분리한 **마이그레이션 전용** 설계 결정 사항을 모은다.
현행 시스템 → 신규 시스템 전환 시 수행사가 참고해야 할 미결정 사항과 전환 규칙을 포함한다.

---

## 1. 타입 전환 가이드

현행 MSSQL 타입에서 표준 타입으로의 전환 규칙.

| 현행 MSSQL 타입 | 현행 용도 | 표준 도메인 | 표준 MSSQL 타입 | 전환 필요 |
|----------------|---------|-----------|---------------|----------|
| varchar (한글) | 이름, 텍스트 | name / text | nvarchar | **Yes** - 인코딩 |
| varchar (코드) | 코드값 | code | varchar | No |
| char(13) | GMKEY | identifier | char(13) | No |
| varchar(10) | PCODE | identifier | int | **Yes** - 타입 변경 |
| smallint | 수량 | count | int | **Yes** - 확장 |
| tinyint | 수량 | count | int | **Yes** - 확장 |
| float | 비율 | rate | decimal(8,5) | **Yes** - 정밀도 |
| real | 비율 | rate | decimal(8,5) | **Yes** - 정밀도 |
| char(1) T/F | 플래그 | flag | bit | **Yes** - 표준화 |
| datetime | 일시 | datetime | datetime2 | Minor |
| int | 수량 | count | int | No |
| nvarchar | 이름 | name | nvarchar | No |

→ 참고: [도메인 타입 정의](../standards-dict/domains.md) - 표준 타입 상세

---

## 2. 인코딩 전환 대상 컬럼

현행 `varchar`에 한글을 저장하여 EUC-KR 인코딩으로 깨지는 컬럼 목록.
마이그레이션 시 `nvarchar`로 전환하고 데이터를 재인코딩해야 한다.

| # | 테이블 | 컬럼 | 현행 타입 | 표준 타입 | 비고 |
|---|--------|------|----------|----------|------|
| 1 | person | NAME | varchar(20) | nvarchar(100) | 선수 이름 |
| 2 | person | CAREER | varchar(255) | nvarchar(500) | 경력 |
| 3 | person | PROMISE | varchar | nvarchar | 포부 |
| 4 | person | MONEY | varchar | nvarchar | 연봉 정보 |
| 5 | GAMEINFO | STADIUM | nvarchar(40) | nvarchar(100) | 구장명 (길이 확장) |
| 6 | GAMEINFO | GWEEK | varchar(12) | nvarchar(10) | 요일 (EUC-KR) |
| 7 | TeamRank | TEAM | varchar | nvarchar | 팀명 |
| 8 | GAMECONTAPP | HITNAME | varchar | nvarchar | 타자명 |
| 9 | GAMECONTAPP | PITNAME | varchar | nvarchar | 투수명 |
| 10 | GAMECONTAPP | CATNAME | varchar | nvarchar | 포수명 |
| 11 | CANCEL_GAME | CANCEL_SC_NM | varchar | nvarchar | 취소 사유 |

**전환 방법**:
```sql
-- EUC-KR varchar → nvarchar 전환 예시
ALTER TABLE person ALTER COLUMN NAME nvarchar(100);
-- 기존 데이터는 COLLATE 변환 또는 ETL에서 재인코딩
```

> 인코딩 정책 상세: [도메인 타입 §3](../standards-dict/domains.md)

---

## 3. 합계행(T/B) 처리 방안

Hitter, Pitcher 테이블에서 `PCODE = 'T'` (원정팀 합계), `PCODE = 'B'` (홈팀 합계) 행의 처리.

### 방안 A (권고) - 합계행 분리

- 합계행을 별도 뷰 또는 집계 테이블(`GAME_TEAM_TOTAL`)로 분리
- 원본 테이블에는 실제 선수 행만 유지 (`player_id NOT NULL`)
- 합계는 쿼리 시 `SUM()` 또는 별도 테이블

**장점**: 집계 시 이중 계산 위험 제거, 데이터 품질 향상
**단점**: 레거시 호환 쿼리 수정 필요

### 방안 B - 예약 player_id 사용 (레거시 호환)

- 예약 ID 할당: `player_id = -1` (원정팀 합계), `player_id = -2` (홈팀 합계)
- 별도 컬럼 `is_team_total` (`bit`, 기본값 0) 추가

| 현행 | player_id | is_team_total | top_bottom_cd | 비고 |
|------|-----------|---------------|---------------|------|
| PCODE='T' | -1 | 1 | T | 원정팀 합계 |
| PCODE='B' | -2 | 1 | B | 홈팀 합계 |
| PCODE='75847' | 75847 | 0 | T 또는 B | 개인 기록 |

> **방안 A 권고 사유**: 합계행이 개인 기록 테이블에 혼재하면 `AVG()`, `COUNT()` 등 집계 시 이중 집계 위험. 분리가 데이터 품질에 유리.

→ 참고: [ID 체계](../standards/id-system.md) - player_id 정의

---

## 4. 기록 상태 코드 (record_status_cd) - 신규 설계

RFP DAR-006 요구사항에 따른 기록 상태 전이 코드.
**현행 시스템에 미존재**, 신규 시스템에서 추가한다.

### 상태 전이

```
DRAFT → REVIEW → CONFIRMED
                      ↓
                   REVISED → CONFIRMED
```

### 코드 정의

| 코드 | 한글 | 영문 | 설명 |
|------|------|------|------|
| `DRAFT` | 입력 | Draft | 기록원이 경기 중 실시간 입력 |
| `REVIEW` | 검증 | Under Review | 기록 위원이 정합성 검증 중 |
| `CONFIRMED` | 확정 | Confirmed | 공식 기록으로 확정 |
| `REVISED` | 정정 | Revised | 확정 후 오류 발견 시 정정 |

### 적용 대상

기록 상태 관리가 필요한 테이블:
- HITTER, PITCHER (경기별 기록)
- SCORE (경기 스코어)
- GAME_CONT_APP (플레이 상세)

> 컬럼명: `record_status_cd` (`varchar(10)`)

→ 참고: [변경 관리 절차](../governance/change-process.md) - 상태 전환 절차

---

## 5. 스키마 세대 정리 (TODO)

현행 시스템은 구세대(GMKEY/PCODE 기반)와 신세대(G_ID/P_ID 기반) 스키마가 공존한다.
마이그레이션 수행사가 테이블별 ID 체계를 파악하고 통합 설계를 진행해야 한다.

- **구세대**: GMKEY(char 13), PCODE(varchar 10) 등 레거시 ID → 24종
- **신세대**: G_ID(int), P_ID(int) 등 정수형 ID → 6종, 2022년~ 추가
- **미분류**: IE_* 실시간 등 양쪽 패턴 혼합 → 9종, S2i 확인 필요

> 세대별 테이블 목록과 전환 우선순위는 마이그레이션 설계 단계에서 수행사와 협의하여 확정한다.

→ 참고: [ID 체계](../standards/id-system.md) - 6종 핵심 ID 정의
→ 참고: [타입 전환 가이드](#1-타입-전환-가이드) - MSSQL 타입 전환 규칙

---

## 6. 미확인 코드 목록 (S2i 확인 필요)

S2i에 확인 요청이 필요한 코드값 목록:

| 코드 분류 | 미확인 항목 | 건수 | 우선순위 |
|----------|-----------|------|---------|
| how_cd | `BH` (기타 안타?) | 14,749 | **높음** |
| how_cd | `IN`, `SD` | 1, 3 | 낮음 |
| place_cd | `R` | 1,192 | 중간 |
| place_cd | `A`~`I` 문자코드 | 각 1~67 | 중간 |
| game_type_cd | 값 4, 7, 8, 9 | 16~240 | 중간 |
| series_id | 값 1~9 각 의미 | 9~330 | 중간 |
| cancel_sc_id | 0 이외 값 목록 | - | 낮음 |
| game_sc_id | 70 이외 값 목록 | - | 낮음 |

### 확인 요청 상태

| # | 항목 | 요청일 | 상태 | 비고 |
|---|------|-------|------|------|
| 1 | +1 컬럼명 (49개 테이블) | - | 미요청 | 수령 후 dictionary/ 반영 |
| 2 | DEFEN +6컬럼, ENTRY -1컬럼 | - | 미요청 | 상세 확인 |
| 3 | BH 코드 의미 | - | 미요청 | 우선 확인 필요 |
| 4 | place_cd 문자코드 | - | 미요청 | |
| 5 | game_flag 4,7,8,9 | - | 미요청 | |
| 6 | series_id 1~9 | - | 미요청 | |

→ 참고: [코드 사전](../standards-dict/codes.md) - 확인된 코드값 정의
→ 참고: [프로젝트 가이드 - 미결 사항](../project-guide.md#_7) - S2i 확인 필요 전체 목록
