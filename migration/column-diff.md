# 컬럼 차이 분석 (백업DB vs S2i)

> 분석 일시: 2026-02-23
> 📋 문서 성격: 현행 시스템(As-Is) 컬럼 차이 분석
> 대상: Excel 비교표에서 컬럼 수 불일치인 75개 테이블
> 방법: MSSQL 백업DB에서 INFORMATION_SCHEMA.COLUMNS 직접 조회

---

## 1. 차이 분포

| 차이 | 수량 | 방향 | 설명 |
|------|------|------|------|
| **+1** | **49개** | S2i가 1개 더 많음 | 공통 관리컬럼 추가 추정 |
| +2 | 5개 | S2i가 더 많음 | GAME_HR, IE_BatterRecord 등 |
| +3 | 2개 | S2i가 더 많음 | GAME_MEMO_PITCHCLOCK |
| +5 | 3개 | S2i가 더 많음 | GAME_MEMO |
| +6 | 1개 | S2i가 더 많음 | DEFEN |
| +9 | 1개 | S2i가 더 많음 | KBO_SCHEDULE |
| **-1** | **7개** | 백업이 1개 더 많음 | ENTRY(6), KBO_SCHEDULE(1) |
| -20 | 3개 | 백업이 더 많음 | Score (이닝 축소) |
| -25 | 4개 | 백업이 더 많음 | KBO_BATRESULT (이닝 축소) |

---

## 2. +1 패턴 (49개) - 핵심

49개 테이블에서 S2i가 정확히 1개 컬럼을 더 보유. 테이블 유형별로 백업DB 컬럼이 완전 동일하므로, **S2i가 공통적으로 1개 컬럼을 추가한 것**이 확실.

### 영향 테이블 유형

| 테이블 | 백업 컬럼수 | S2i | 인스턴스 수 | 백업DB 컬럼 목록 |
|--------|-----------|-----|-----------|----------------|
| **Hitter** | 26 | 27 | 11개 DB | AB, BB, CS, ERR, GD, GDAY, GMKEY, H2, H3, HIT, HP, HR, IB, KK, LOB, NAME, ONETURN, PA, PCODE, RBI, RUN, SB, SF, SH, TB, TURN |
| **Pitcher** | 36 | 37 | 8개 DB | AB, BB, BF, BK, CG, ER, GDAY, GMKEY, H2, H3, HIT, HOLD, HP, HR, IB, INN, INN2, KK, L, NAME, NP, ONETURN, PA, PCODE, R, SB, SF, SH, SHO, START, SV, TB, TURN, W, WLS, WP |
| **BatTotal** | 22 | 23 | 6개 DB | AB, BB, CS, ERR, GAMENUM, GD, GYEAR, H2, H3, HIT, HP, HR, HRA, KK, PCODE, RBI, RUN, SB, SF, SH, TB, TEAM |
| **PitTotal** | 21 | 22 | 6개 DB | BB, BF, CG, ER, ERA, GAMENUM, GYEAR, HIT, HOLD, HP, HR, INN, INN2, KK, L, PCODE, R, SHO, SV, TEAM, W |
| **TeamRank** | 29 | 30 | 7개 DB | AB, BB, BRA, CONTINUE, ER, ERA, ERR, GAME, GYEAR, H2, H3, HIT, HP, HR, HRA, INN, INN2, LEAGUE, LOSE, LRA, R, RANK, RUN, SAME, SB, SF, TEAM, WIN, WRA |
| **GAMECONTAPP** | 29 | 30 | 1개 DB | BESSION, GDAY, GMKEY, HOW, INN, INN2, NAME, OCOUNT, PCODE, PLACE, POS1~POS9, SEQ, TB, TURN |
| **IE_GAMESTATE** | 5 | 6 | 8개 DB | GAMEID, GYEAR, INN_NO, STATUS_ID, TB_SC |
| **KBO_ETCGAME** | 5 | 6 | 3개 DB | GDAY, GMKEY, HOW, RESULT, SEQ |
| **KBO_PITRESULT** | 23 | 24 | 3개 DB | CG, ER, ERA, GDAY, GMKEY, HIT, HOLD, HP, HR, INN, INN2, KK, L, NAME, NP, PCODE, R, SHO, SV, TB, TEAM, W, WLS |

> **추정**: S2i가 추가한 1개 컬럼은 `INPUTTIME`, `REG_DT`, `UPDATE_DT` 같은 감사(audit)/관리 컬럼일 가능성이 높음. 백업DB에는 이 컬럼 없이 전송받고 있음. **S2i에 확인 필요.**

---

## 3. +2~9 패턴 (12개) - 개별 확인 필요

### DEFEN (+6): 백업 12 → S2i 18

| 백업DB 컬럼 (12개) |
|-------------------|
| ASS, DP, ERR, GDAY, GMKEY, INPUTTIME, ONETURN, PB, PCODE, PO, POSI, TB |

> S2i(`Defen_TOT`)에 6개 컬럼 추가. 추가 컬럼 후보: NAME, TEAM, SB, CS, TC, FP 등 수비 관련 통계. Excel 비고: "전송 시 NAME='합계' 제외"

### GAME_MEMO (+5): 백업 20 → S2i 25

| 백업DB 컬럼 (20개) |
|-------------------|
| BAT_AROUND_NO, BAT_ORDER_NO, END_TM, ETC_ME, FIRST_IF, GAME_PIT_NO, G_ID, INN_NO, LAST_IF, LE_ID, ORDER_NO, PA_PIT_NO, P_ID, REG_DT, REQ_T_ID, SEASON_ID, SR_ID, START_TM, TB_SC, USE_TM |

> 이 테이블은 **신세대 ID 체계** (G_ID, LE_ID, P_ID) 사용. DB1, DB2 모두 동일.

### GAME_MEMO_PITCHCLOCK (+3): 백업 16 → S2i 19

| 백업DB 컬럼 (16개) |
|-------------------|
| BAT_AROUND_NO, BAT_ORDER_NO, ETC_ME, GAME_PIT_NO, G_ID, INN_NO, LE_ID, PA_PIT_NO, PIT_RESULT_SC, P_ID, REG_DT, SEASON_ID, SEQ_NO, SR_ID, TB_SC, T_ID |

### GAME_HR (+2): 백업 15 → S2i 17 (RECORD_HR)

| 백업DB 컬럼 (15개) |
|-------------------|
| BAT_P_ID, DIREC_SC, G_ID, HR_DISTANCE_VA, INN_NO, LE_ID, PIT_P_ID, PLACE_SC, RECORD_DT, REG_DT, SCORE_CN, SEASON_ID, SEQ_NO, SR_ID, TB_SC |

> **신세대 ID 체계** 사용. S2i 테이블명: `RECORD_HR`

### IE_BatterRecord (+2): 백업 25 → S2i 27 (2개 DB)

| 백업DB 컬럼 (25개) |
|-------------------|
| AB, BB, CS, ERR, GD, GDAY, GMKEY, H2, H3, HIT, HP, HR, IB, KK, LOB, NAME, ONETURN, PA, PCODE, RBI, RUN, SB, SF, SH, TB |

### KBO_SCHEDULE (+9): 백업 15 → S2i 24 (2군 2개 DB)

| 백업DB 컬럼 (15개) |
|-------------------|
| CANCLE, DHEADER, ENDYN, GDAY, GMKEY, GMONTH, GYEAR, HOME, HSCORE, SNAME, STADIUM, VISIT, VSCORE, Week, attendance |

> 2군 KBO_SCHEDULE은 1군(22컬럼)보다 7컬럼 적음. S2i는 24컬럼으로 확장.

### KBO_BATRESULT (+2, DB2_BASEBALL): 백업 90 → S2i 92 (1군 정규시즌)

> 1군은 이닝 컬럼이 25이닝까지 있어 90컬럼. S2i가 2개 추가.

---

## 4. -1 패턴 (7개) - 백업이 더 많음

### ENTRY (-1): 6개 DB

| 백업DB 컬럼 (12개) |
|-------------------|
| GDAY, GMKEY, NAME, NUM, ONETURN, PCODE, POSI, QUIT, START, TB, TEAM, TURN |

> 백업 12 → S2i 11. S2i가 `TEAM` 또는 `ONETURN` 등 1개 컬럼을 제거한 것으로 추정.

### KBO_SCHEDULE (-1): DB2_BASEBALL_NEW (1군)

| 백업DB 컬럼 (22개) |
|-------------------|
| BROADCAST1, BROADCAST2, CANCLE, DHEADER, ENDYN, GDAY, GMKEY, GMONTH, GTIME, GYEAR, HOME, HSCORE, SNAME, STADIUM, SUSPENDED, VISIT, VSCORE, Week, attendance, broadcast3, broadcast4, game_flag |

> 백업 22 → S2i 21. S2i가 broadcast 관련 1개 컬럼 제거 추정.

---

## 5. -20/-25 패턴 - 이닝 컬럼 축소

### Score (-20): 3개 DB (올스타/PO/2군PO)

| 백업DB | 컬럼 | S2i 컬럼 | 차이 |
|--------|------|---------|------|
| DB2_ALLSTAR | 60 | 40 | -20 |
| DB2_POSTSEASON | 60 | 40 | -20 |
| DB2_MINOR_POSTSEASON | 60 | 40 | -20 |

> Score 테이블은 피벗형 (이닝별 홈/원정 점수가 컬럼). 백업은 25이닝×2(T/B)+10=60, S2i는 15이닝×2+10=40으로 축소.

### KBO_BATRESULT (-25): 4개 DB (올스타/시범/PO/2군PO)

| 백업DB | 컬럼 | S2i 컬럼 | 차이 |
|--------|------|---------|------|
| DB2_ALLSTAR | 90 | 65 | -25 |
| DB2_EXHIBITION | 90 | 65 | -25 |
| DB2_POSTSEASON | 90 | 65 | -25 |
| DB2_MINOR_POSTSEASON | 90 | 65 | -25 |

> KBO_BATRESULT의 `INN*_1`, `INN*_2`, `INN*_3` (이닝별 타석 상세) 중 S2i가 17이닝으로 축소하여 65컬럼.

---

## 6. 스키마 세대 관찰

컬럼 조회 결과, 두 가지 스키마 세대가 공존:

| 구분 | 구세대 | 신세대 |
|------|--------|--------|
| **경기 ID** | `GMKEY` (char 13) | `G_ID` (char 13) |
| **선수 ID** | `PCODE` (varchar) | `P_ID` (int) |
| **시즌** | `GYEAR` (char 4) | `SEASON_ID` (smallint) |
| **리그** | DB 분리로 구분 | `LE_ID` (smallint) |
| **시리즈** | DB 분리로 구분 | `SR_ID` (smallint) |
| **팀** | `TEAM` (char 2) | `T_ID` (char 2) |
| **이닝 구분** | `TB` (char 1) | `TB_SC` (char 1) |
| **사용 테이블** | Hitter, Pitcher, ENTRY, Score, BatTotal, PitTotal, TeamRank, GAMECONTAPP, KBO_* | GAME_HR, GAME_MEMO, GAME_MEMO_PITCHCLOCK, IE_GAMESTATE |

> 경기 기록 핵심 테이블은 구세대, 운영/메모 테이블은 신세대 ID 사용.

---

## 7. 후속 조치

| 우선순위 | 항목 | 방법 |
|---------|------|------|
| **1** | +1 컬럼 정체 확인 | S2i에 컬럼명 문의 or S2i DB 직접 조회 |
| **2** | DEFEN +6 컬럼 확인 | S2i에 Defen_TOT 스키마 요청 |
| **3** | ENTRY -1 컬럼 확인 | S2i가 제거한 컬럼 파악 |
| **4** | 이닝 축소 정책 확정 | Score/KBO_BATRESULT 최대 이닝 수 결정 |
| **5** | 신/구세대 통합 전략 | 마이그레이션 시 ID 체계 통일 방안 |
