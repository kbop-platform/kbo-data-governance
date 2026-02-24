# OPS Schema Summary (ops-schema.json)

> 분석 일시: 2026-02-23
> 출처: KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf (2022년 문서, 참고용)

## Overview

| Category | Tables | Description |
|----------|--------|-------------|
| MASTER | 23 | 마스터 데이터 (코드, 선수, 팀, 구장, 경기 등) |
| RECORD | 9 | 기록 데이터 (경기 결과, 선수/팀 성적) |
| LIVE | 3 | 실시간 경기 데이터 (문자중계, 매트릭스, 라인업) |
| ALARM | 1 | 알람 수신 관리 |
| APPROVAL | 11 | 승인 요청/처리 (선수 등록, 트레이드, FA 등) |
| MONITORING | 24 | 모니터링 (경기영상, 행동강령, 코로나, 부정행위 등) |
| OFFICAL | 8 | 공시업무 (주소록, 서명, 알람 등) |
| 업무관련 | 5 | 업무 관련 (구단 문의, 자료실, 일반요청) |
| UNKNOWN | 27 | 미분류 (원본에 category 없음) |
| **TOTAL** | **111** | **총 1062개 컬럼** |

---

## MASTER (23 tables)

### AREA_SECTION
- **논리명**: 지역 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | TINYINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### BOARD_PLAYER_STATE
- **논리명**: 선수 이동 현황
- **PK**: `BD_SE`
- **컬럼 수**: 12

| Column | Type |
|--------|------|
| BD_SE | INT |
| BD_DT | DATE |
| BD_SC | TINYINT |
| TEAM_NM | VARCHAR |
| BEFORE_TEAM_NM | VARCHAR |
| PLAYER_NM | VARCHAR |
| POS_IF | VARCHAR |
| ETC_IF | VARCHAR |
| MAIN_YN | CHAR |
| ORDER_NO | INT |
| GROUP_NO | TINYINT |
| REG_DT | DATETIME |

### BOARD_PLAYER_STATE_SECTION
- **논리명**: 선수 이동 현황 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | TINYINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### CODE
- **논리명**: 코드
- **PK**: `COLUMN_NM, CODE_ID`
- **컬럼 수**: 8

| Column | Type |
|--------|------|
| COLUMN_NM | VARCHAR |
| CODE_ID | INT |
| CODE_NM | VARCHAR |
| ORDER_NO | INT |
| DEL_CK | BIT `NN` |
| UPDATE_DT | DATETIME |
| DEL_DT | DATETIME |
| REG_DT | DATETIME |

### COMPETITION_NATION
- **논리명**: 대회 국가
- **PK**: `COMP_ID`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| COMP_ID | SMALLINT |
| COMP_YR | SMALLINT |
| COMP_CD | VARCHAR |
| COMP_NM | VARCHAR |
| REG_DT | DATETIME |

### COMPETITION_RESULT_SECTION
- **논리명**: 대회 결과 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### GAME
- **논리명**: 경기
- **PK**: `LE_ID, SR_ID, G_ID`
- **비고**: 2. SR_ID : 1 – 시범경기, 0 – 정규경기, 6 – 순위결정전, 4 – 와일드카드결정전, 3 – 준플레이오프, 5 – 플레이
오프, 7 – 한국시리즈, 9 – 올스타전, 8 - 국제전
- **컬럼 수**: 16

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEASON_ID | SMALLINT |
| G_DT | VARCHAR |
| G_TM | VARCHAR |
| H_T_ID | CHAR |
| A_T_ID | CHAR |
| S_ID | VARCHAR |
| S_NM | VARCHAR |
| END_CK | BIT |
| CANCEL_CK | BIT |
| CANCEL_SC_ID | SMALLINT |
| SUSPENDED_CK | BIT |
| UPDATE_DT | DATETIME |
| REG_DT | DATETIME |

### GAME_ASSIGN
- **논리명**: 경기 인원 배정
- **PK**: `LE_ID, SR_ID, G_ID`
- **비고**: 2. SR_ID : 1 – 시범경기, 0 – 정규경기, 6 – 순위결정전, 4 – 와일드카드결정전, 3 – 준플레이오프, 5 – 플레이
오프, 7 – 한국시리즈, 9 – 올스타전, 8 - 국제전
- **컬럼 수**: 19

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEASON_ID | SMALLINT |
| AWAY_ID | CHAR |
| HOME_ID | CHAR |
| S_ID | CHAR |
| HEADER_NO | TINYINT |
| OPT_U_ID | VARCHAR |
| UMPC_P_ID | INT |
| UMP1_P_ID | INT |
| UMP2_P_ID | INT |
| UMP3_P_ID | INT |
| UMPL_P_ID | INT |
| UMPR_P_ID | INT |
| UMPS_P_ID | INT |
| SCOA_P_ID | INT |
| SCOB_P_ID | INT |
| REG_DT | DATETIME |

### GAME_CANCEL_MEMO
- **논리명**: 경기 취소 메모
- **PK**: `LE_ID, SR_ID, G_ID`
- **비고**: 2. SR_ID : 1 – 시범경기, 0 – 정규경기, 6 – 순위결정전, 4 – 와일드카드결정전, 3 – 준플레이오프, 5 – 플레이
오프, 7 – 한국시리즈, 9 – 올스타전, 8 - 국제전
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEASON_ID | SMALLINT |
| CANCEL_ME | VARCHAR |
| REG_DT | DATETIME |

### GAME_SECTION
- **논리명**: 경기 구분
- **PK**: `SC_SC, SC_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| SC_SC | VARCHAR |
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### GAME_START_PITCHER
- **논리명**: 경기 선발 투수
- **PK**: `LE_ID, SR_ID, G_ID`
- **컬럼 수**: 8

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEASON_ID | SMALLINT |
| T_PIT_P_ID | INT |
| B_PIT_P_ID | INT |
| APPR_CK | CHAR |
| REG_DT | DATETIME |

### PLAYER
- **논리명**: 선수 명단
- **PK**: `LE_ID, SEASON_ID, P_ID`
- **컬럼 수**: 21

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| T_ID | CHAR |
| P_NM | VARCHAR |
| P_CHN_NM | VARCHAR |
| P_ENG_NM | VARCHAR |
| P_FULL_NM | VARCHAR |
| BACK_NO | VARCHAR |
| POS_CD | INT |
| BIRTH_DT | VARCHAR |
| PIT_DIREC_CD | INT |
| PIT_FORM_CD | INT |
| HIT_DIREC_CD | INT |
| ACTIVE_CD | INT |
| JOIN_DT | DATE |
| SALARY_IF | VARCHAR |
| CAREER_IF | VARCHAR |
| FINAL_CAREER_IF | VARCHAR |
| FOREIGNER_CK | BIT `NN` |
| REG_DT | DATETIME |

### PLAYER_CAREER
- **논리명**: 선수 경력
- **PK**: `CA_RE`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| CA_RE | INT |
| P_ID | INT |
| START_DS | DATE |
| END_DS | DATE |
| CA_SC | SMALLINT |
| T_ID | CHAR |
| BAFORE_T_ID | CHAR |
| ETC_ME | VARCHAR |
| REG_DT | DATETIME |

### PLAYER_CAREER_SECTION
- **논리명**: 선수 경력 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### PLAYER_DRAFT
- **논리명**: 선수 신인지명
- **PK**: `P_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| P_ID | INT |
| DRAFT_YR | SMALLINT |
| REG_DT | DATETIME |

### PLAYER_FA
- **논리명**: 선수 FA
- **PK**: `LE_ID, SEASON_ID, P_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| REG_DT | DATETIME |

### PLAYER_SALARY
- **논리명**: 선수 연봉
- **PK**: `LE_ID, SEASON_ID, P_ID`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| T_ID | CHAR |
| PAYMENT_VA | INT |
| CONTRACT_CN | SMALLINT |
| SALARY_VA | INT |
| OPTION_VA | INT |
| REG_DT | DATETIME |

### SALARY_CAP
- **논리명**: 샐리러 캡
- **PK**: `LE_ID, SEASON_ID`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| MAX_VA | INT |
| MIN_VA | INT |
| REG_DT | DATETIME |

### SCHOOL
- **논리명**: 학교 정보
- **PK**: `AREA_SC, SCH_SC, SCH_NM`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| AREA_SC | TINYINT |
| SCH_SC | TINYINT |
| SCH_NM | VARCHAR |
| REG_DT | DATETIME |

### SCHOOL_SECTION
- **논리명**: 학교 정보 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | TINYINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### STADIUM
- **논리명**: 구장 정보
- **PK**: `SEASON_ID, S_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| SEASON_ID | SMALLINT |
| S_ID | VARCHAR |
| S_NM | VARCHAR |
| REG_DT | DATETIME |

### TEAM
- **논리명**: 팀 정보
- **PK**: `LE_ID, SEASON_ID, T_ID`
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| T_NM | VARCHAR |
| T_FULL_NM | VARCHAR |
| REG_DT | DATETIME |

### UMPIRE_EVALUATION_GROUP
- **논리명**: 심판 행동강령 평가표 그룹
- **PK**: `LE_ID, SEASON_ID, P_ID`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| EVALUATION_CD | INT |
| USER_ID | VARCHAR |
| CHAIRMAN_USER_ID | VARCHAR |
| TEAMLEADER_USER_ID | VARCHAR |
| GROUP_NO | SMALLINT |
| FIRST_SECOND_CK | BIT |

---

## RECORD (9 tables)

### GAME_INFO
- **논리명**: 경기 정보
- **PK**: `LE_ID, SR_ID, G_ID`
- **컬럼 수**: 19

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEASON_ID | SMALLINT |
| AWAY_ID | CHAR |
| HOME_ID | CHAR |
| START_DT | DATETIME |
| END_DT | DATETIME |
| USE_DT | TIME |
| DELAY_TM | VARCHAR |
| EX_INN9_USE_DT | TIME |
| HALF_SC | CHAR |
| UMPC_P_ID | INT |
| UMP1_P_ID | INT |
| UMP2_P_ID | INT |
| UMP3_P_ID | INT |
| UMPL_P_ID | INT |
| UMPR_P_ID | INT |
| REG_DT | DATETIME |

### GAME_INN_SCORE
- **논리명**: 경기 이닝별 점수
- **PK**: `LE_ID, SR_ID, G_ID, INN_NO, TB_SC`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| INN_NO | TINYINT |
| TB_SC | CHAR |
| SCORE_CN | SMALLINT |
| REG_DT | DATETIME |

### GAME_PLAYER_HITTER
- **논리명**: 경기별 선수 타자
- **PK**: `LE_ID, SR_ID, G_ID, P_ID`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| P_ID | INT |
| SEASON_ID | SMALLINT |
| TB_SC | CHAR |
| BAT_TURN_NO | TINYINT |
| BAT_ORDER_NO | TINYINT |
| HRA_RT | FLOAT |
| PA_CN | SMALLINT |
| AB_CN | SMALLINT |
| RUN_CN | SMALLINT |
| HIT_CN | SMALLINT |
| H2_CN | SMALLINT |
| H3_CN | SMALLINT |
| HR_CN | SMALLINT |
| RBI_CN | SMALLINT |
| SB_CN | SMALLINT |
| CS_CN | SMALLINT |
| RO_CN | SMALLINT |
| POFF_CN | SMALLINT |
| SH_CN | SMALLINT |
| SF_CN | SMALLINT |
| BB_CN | SMALLINT |
| IB_CN | SMALLINT |
| HP_CN | SMALLINT |
| KK_CN | SMALLINT |

### GAME_PLAYER_PITCHER
- **논리명**: 경기별 선수 투수
- **PK**: `LE_ID, SR_ID, G_ID, P_ID`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| P_ID | INT |
| SEASON_ID | SMALLINT |
| TB_SC | CHAR |
| TURN_NO | TINYINT |
| ERA_RT | FLOAT |
| RESULT_SC | CHAR |
| START_CK | BIT `NN` |
| QUIT_CK | BIT `NN` |
| SHO_CK | BIT `NN` |
| CG_CK | BIT `NN` |
| INN2_CN | SMALLINT |
| PA_CN | SMALLINT |
| AB_CN | SMALLINT |
| PIT_CN | SMALLINT |
| R_CN | SMALLINT |
| ER_CN | SMALLINT |
| ERR_CN | SMALLINT |
| HIT_CN | SMALLINT |
| H2_CN | SMALLINT |
| H3_CN | SMALLINT |
| HR_CN | SMALLINT |
| SH_CN | SMALLINT |
| SF_CN | SMALLINT |
| BB_CN | SMALLINT |

### GAME_RESULT
- **논리명**: 경기 결과
- **PK**: `LE_ID, SR_ID, G_ID`
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| T_SCORE_CN | SMALLINT |
| B_SCORE_CN | SMALLINT |
| REG_DT | DATETIME |

### GAME_TEAM_HITTER
- **논리명**: 경기별 팀 타자
- **PK**: `LE_ID, SR_ID, G_ID, T_ID`
- **컬럼 수**: 23

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| T_ID | CHAR |
| SEASON_ID | SMALLINT |
| TB_SC | CHAR |
| HRA_RT | FLOAT |
| AB_CN | SMALLINT |
| RUN_CN | SMALLINT |
| HIT_CN | SMALLINT |
| H2_CN | SMALLINT |
| H3_CN | SMALLINT |
| HR_CN | SMALLINT |
| SB_CN | SMALLINT |
| CS_CN | SMALLINT |
| RO_CN | SMALLINT |
| POFF_CN | SMALLINT |
| SH_CN | SMALLINT |
| SF_CN | SMALLINT |
| BB_CN | SMALLINT |
| HP_CN | SMALLINT |
| ERR_CN | SMALLINT |
| REG_DT | DATETIME |

### GAME_TEAM_PITCHER
- **논리명**: 경기별 팀 투수
- **PK**: `LE_ID, SR_ID, G_ID, T_ID`
- **컬럼 수**: 24

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| T_ID | CHAR |
| SEASON_ID | SMALLINT |
| TB_SC | CHAR |
| ERA_RT | FLOAT |
| RESULT_SC | CHAR |
| INN2_CN | SMALLINT |
| AB_CN | SMALLINT |
| R_CN | SMALLINT |
| ER_CN | SMALLINT |
| HIT_CN | SMALLINT |
| H2_CN | SMALLINT |
| H3_CN | SMALLINT |
| HR_CN | SMALLINT |
| SH_CN | SMALLINT |
| SF_CN | SMALLINT |
| BB_CN | SMALLINT |
| HP_CN | SMALLINT |
| KK_CN | SMALLINT |
| ERR_CN | SMALLINT |
| QS_CK | BIT `NN` |
| REG_DT | DATETIME |

### SEASON_PLAYER_ENTRY
- **논리명**: 시즌별 선수 엔트리
- **PK**: `LE_ID, SEASON_ID, P_ID`
- **컬럼 수**: 10

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| T_ID | CHAR |
| REGDAY_CN | SMALLINT |
| PITHIT_SC | CHAR |
| RECORD_CN | SMALLINT |
| FA_REGDAY_CK | BIT `NN` |
| FA_RECORD_CK | BIT `NN` |
| REG_DT | DATETIME |

### SEASON_PLAYER_ENTRY_INTNL
- **논리명**: 시즌별 선수 엔트리 국제전
- **PK**: `LE_ID, SEASON_ID, P_ID, INTNL_SC`
- **컬럼 수**: 8

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| INTNL_SC | VARCHAR |
| REGDAY_CN | SMALLINT |
| FA_USE_CK | BIT `NN` |
| MILITARY_CK | BIT `NN` |
| REG_DT | DATETIME |

---

## LIVE (3 tables)

### IE_GAME_LIVETEXT
- **논리명**: 실시간 경기 문자중계
- **PK**: `LE_ID, SR_ID, G_ID, SEQ_NO`
- **컬럼 수**: 16

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEQ_NO | SMALLINT |
| SEASON_ID | SMALLINT |
| INN_NO | TINYINT |
| BAT_AROUND_NO | TINYINT |
| TB_SC | CHAR |
| LIVETEXT_IF | VARCHAR |
| TEXTSTYLE_SC | TINYINT |
| BAT_P_ID | INT |
| BAT_ORDER_NO | TINYINT |
| PA_PIT_NO | SMALLINT |
| PIT_P_ID | INT |
| PIT_RESULT_SC | CHAR |
| REG_DT | DATETIME |

### IE_GAME_MATRIX_MIX
- **논리명**: 실시간 경기 매트릭스 MIX
- **PK**: `LE_ID, SR_ID, G_ID, SEQ_NO`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEQ_NO | SMALLINT |
| SEASON_ID | SMALLINT |
| INN_NO | TINYINT |
| BAT_AROUND_NO | TINYINT |
| TB_SC | CHAR |
| BEFORE_OUT_CN | TINYINT |
| BEFORE_AWAY_SCORE_CN | SMALLINT |
| BEFORE_HOME_SCORE_CN | SMALLINT |
| BEFORE_SCORE_GAP_CN | SMALLINT |
| BEFORE_RUNNER_SC | TINYINT |
| AFTER_OUT_CN | TINYINT |
| AFTER_AWAY_SCORE_CN | SMALLINT |
| AFTER_HOME_SCORE_CN | SMALLINT |
| AFTER_SCORE_GAP_CN | SMALLINT |
| AFTER_RUNNER_SC | TINYINT |
| BAT_P_ID | INT |
| PIT_P_ID | INT |
| RUN_P_ID | INT |
| HOW_ID | CHAR |
| LIVETEXT_IF | VARCHAR |
| BEFORE_WE_RT | FLOAT |
| AFTER_WE_RT | FLOAT |
| WPA_RT | FLOAT |
| LI_RT | FLOAT |

### LINEUP
- **논리명**: 실시간 경기 엔트리
- **PK**: `LE_ID, SR_ID, G_ID, P_ID, BAT_ORDER_NO, POS_TURN_NO, POS_SC`
- **컬럼 수**: 16

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| P_ID | INT |
| BAT_ORDER_NO | TINYINT |
| POS_TURN_NO | TINYINT |
| POS_SC | CHAR |
| BAT_TURN_NO | TINYINT |
| SEASON_ID | SMALLINT |
| TB_SC | CHAR |
| CH_INN_NO | TINYINT |
| CH_BAT_AROUND_NO | TINYINT |
| CH_BAT_ORDER_NO | TINYINT |
| CH_PIT_BALL_CN | SMALLINT |
| PLAY_NO | TINYINT |
| REG_DT | DATETIME |

---

## ALARM (1 tables)

### ALARM_RCV_USER
- **논리명**: 알람 수신 사용자
- **PK**: `ALARM_ID, USER_ID`
- **컬럼 수**: 12

| Column | Type |
|--------|------|
| ALARM_ID | BIGINT |
| USER_ID | VARCHAR |
| READ_CK | BIT `NN` |
| READ_DT | DATETIME |
| DEL_CK | BIT `NN` |
| DEL_ID | VARCHAR |
| DEL_IP_IF | VARCHAR |
| DEL_DT | DATETIME |
| TEXT_SEND_CK | BIT `NN` |
| TEXT_SEND_SUCC_CK | BIT `NN` |
| TEXT_SEND_DT | DATETIME |
| REG_DT | DATETIME |

---

## APPROVAL (11 tables)

### APPROVAL_ITEM_NOTE
- **논리명**: 승인 신청 항목 판독 구분 노트
- **PK**: `ITEM_SC, NOTE_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| ITEM_SC | SMALLINT |
| NOTE_ID | TINYINT |
| NOTE_IF | VARCHAR |
| REG_DT | DATETIME |

### APPROVAL_ITEM_SECTION
- **논리명**: 승인 신청 항목 판독 구분
- **PK**: `SC_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| DEL_CK | BIT `NN` |
| REG_DT | DATETIME |

### APPROVAL_MASTER
- **논리명**: 승인 마스터
- **PK**: `APPROVAL_SE`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| APPROVAL_SE | INT |
| REQ_TABLE_ID | TINYINT |
| SEASON_ID | SMALLINT |
| REQ_T_ID | CHAR `NN` |
| ITEM_SC | SMALLINT |
| REQ_DT | DATE |
| FILE_NM | VARCHAR |
| APPROVAL_CK | BIT `NN` |
| RETURN_CK | BIT `NN` |
| UPDATE_DT | DATETIME |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_ETC
- **논리명**: 승인 요청 기타 사항
- **PK**: `REQ_SE`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_GAME
- **논리명**: 승인 요청 경기
- **PK**: `REQ_SE`
- **컬럼 수**: 12

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| BF_G_TM | VARCHAR |
| AF_G_TM | VARCHAR |
| BF_S_ID | VARCHAR |
| AF_S_ID | VARCHAR |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_OBJECTION
- **논리명**: 승인 요청 반대
- **PK**: `REQ_SE`
- **컬럼 수**: 12

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| P_ID | INT |
| INN_NO | TINYINT |
| BAT_ORDER_NO | TINYINT |
| RECORD_CD | TINYINT |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_PLAYER_CHANGE
- **논리명**: 승인 요청 선수 교체
- **PK**: `REQ_SE`
- **컬럼 수**: 18

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| BF_P_NM | VARCHAR |
| AF_P_NM | VARCHAR |
| BF_P_CHN_NM | VARCHAR |
| AF_P_CHN_NM | VARCHAR |
| BF_BACK_NO | VARCHAR |
| AF_BACK_NO | VARCHAR |
| BF_POS_CD | INT |
| AF_POS_CD | INT |
| BF_ACTIVE_CD | INT |
| AF_ACTIVE_CD | INT |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_PLAYER_FA_CONTRACT
- **논리명**: 승인 요청 FA 선수 계약
- **PK**: `REQ_SE`
- **컬럼 수**: 16

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| T_ID | CHAR |
| P_NM | VARCHAR |
| POS_CD | INT |
| QUALIFY_YEARS_CN | TINYINT |
| QUALIFY_SC | INT |
| PAYMENT_IF | VARCHAR |
| SALARY_IF | VARCHAR |
| CONTRACT_DT | DATE |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_PLAYER_FA_INOUT
- **논리명**: 승인 요청 선수 FA 트레이드
- **PK**: `REQ_SE`
- **컬럼 수**: 13

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| IN_T_ID | CHAR |
| IN_P_ID | INT |
| IN_P_NM | VARCHAR |
| IN_POS_CD | INT |
| OUT_T_ID | CHAR |
| OUT_P_ID | INT |
| INOUT_DT | DATE |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_PLAYER_INOUT
- **논리명**: 승인 요청 선수 트레이드
- **PK**: `REQ_SE`
- **컬럼 수**: 16

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| P_NM | VARCHAR |
| POS_CD | INT |
| INOUT_SC | VARCHAR |
| OUT_T_ID | CHAR |
| IN_T_ID | CHAR |
| INOUT_DT | DATE |
| BF_BACK_NO | VARCHAR |
| AF_BACK_NO | VARCHAR |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_PLAYER_NEW
- **논리명**: 승인 요청 선수 신규
- **PK**: `REQ_SE`
- **컬럼 수**: 16

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_NM | VARCHAR |
| P_FULL_NM | VARCHAR |
| P_ENG_NM | VARCHAR |
| BIRTH_DT | DATE |
| BACK_NO | VARCHAR |
| POS_CD | INT |
| PIT_DIREC_CD | INT |
| PIT_FORM_CD | INT |
| HIT_DIREC_CD | INT |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| REG_DT | DATETIME |

---

## MONITORING (24 tables)

### MONITORING_COVID_BASIC
- **논리명**: 코로나 19 주요 점검 사항
- **PK**: `COVID_SE, QUESTION_SC, QUESTION_NO`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| COVID_SE | INT |
| QUESTION_SC | CHAR |
| QUESTION_NO | INT |
| ANSWER_YN | CHAR |
| REG_DT | DATETIME |

### MONITORING_COVID_MASTER
- **논리명**: 코로나 19 주요사항 마스터
- **PK**: `MASTER_SE, COVID_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| COVID_SE | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_COVID_SPECIAL
- **논리명**: 코로나 19 주요 특이 사항
- **PK**: `COVID_SE`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| COVID_SE | INT |
| SPECIAL_CT | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_DISPUTE_REPORT
- **논리명**: 분쟁 및 사고 보고서
- **PK**: `MASTER_SE, DISPUTE_SE`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| DISPUTE_SE | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| REPORT_CT | VARCHAR |
| ADD_CT | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_EVALUATION_BASIC
- **논리명**: 행동강령 평가표 일반
- **PK**: `EVALUATION_SE, QUESTION_SC, QUESTION_NO`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| EVALUATION_SE | INT |
| QUESTION_SC | CHAR |
| QUESTION_NO | INT |
| POINT_VA | SMALLINT |
| REG_DT | DATETIME |

### MONITORING_EVALUATION_CONTENT
- **논리명**: 행동강령 평가표 내용
- **PK**: `EVALUATION_SE`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| EVALUATION_SE | INT |
| VAR_CT | VARCHAR |
| OPINION_CT | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_EVALUATION_MASTER
- **논리명**: 행동강령 평가표 마스터
- **PK**: `EVALUATION_SE`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| EVALUATION_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| EVALUATION_SC | CHAR |
| MONTH | SMALLINT |
| UMP_P_ID | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_EVALUATION_ROUNDUP
- **논리명**: 행동강령 평가표 모음
- **PK**: `EVALUATION_SE`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| EVALUATION_SE | SMALLINT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| MONTH | SMALLINT |
| UMP_P_ID | INT |
| USER_ID | VARCHAR |
| MANAGE_SCORE | FLOAT |
| RULE_SCORE | FLOAT |
| REG_DT | DATETIME |

### MONITORING_GAME_BASIC
- **논리명**: 경기 영상 모니터링 기본
- **PK**: `GAME_SE, TYPE_SC, QUESTION_NO`
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| GAME_SE | INT |
| TYPE_SC | CHAR |
| QUESTION_NO | INT |
| ANSWER_YN | CHAR |
| P_ID | INT |
| REG_DT | DATETIME |

### MONITORING_GAME_DETAIL
- **논리명**: 경기 영상 세부 모니터링 사항
- **PK**: `INN_NO, TB_SC, GAME_SE`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| GAME_SE | INT |
| INN_NO | SMALLINT |
| TB_SC | CHAR |
| DETAIL_CT | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_GAME_MASTER
- **논리명**: 경기 영상 모니터링 마스터
- **PK**: `GAME_SE, MASTER_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| GAME_SE | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_ILLEGAL_CHECKLIST
- **논리명**: 부정행위방지 모니터링 체크리스트
- **PK**: `ILLEGAL_SE, ILLEGAL_SC, QUESTION_NO`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| ILLEGAL_SE | INT |
| ILLEGAL_SC | CHAR |
| QUESTION_NO | INT |
| ANSWER_YN | CHAR |
| REG_DT | DATETIME |

### MONITORING_ILLEGAL_CONTENT
- **논리명**: 부정행위 모니터링 내용 및 조치사항
- **PK**: `ILLEGAL_SE, CONTENT_SE`
- **컬럼 수**: 10

| Column | Type |
|--------|------|
| ILLEGAL_SE | INT |
| CONTENT_SE | INT |
| WORK_CT | VARCHAR |
| PERSONAL_IF | VARCHAR |
| DATE_IF | VARCHAR |
| PLACE_IF | VARCHAR |
| CONTENT_IF | VARCHAR |
| PHONE_IF | VARCHAR |
| ACTION_IF | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_ILLEGAL_FILE
- **논리명**: 부정행위방지 모니터링 첨부파일
- **PK**: `CONTENT_SE, FILE_NO`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| CONTENT_SE | INT |
| FILE_NO | INT |
| FILE_LK | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_ILLEGAL_MASTER
- **논리명**: 부정행위방지 모니터링 마스터
- **PK**: `MASTER_SE, ILLEGAL_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| ILLEGAL_SE | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_MASTER
- **논리명**: 경기 모니터링 평가 마스터
- **PK**: `MASTER_SE, LE_ID, SR_ID, G_ID`
- **컬럼 수**: 19

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| G_ID | CHAR |
| SEASON_ID | SMALLINT |
| GAME_CK | BIT |
| OPERATION_CK | BIT |
| COVID_CK | BIT |
| DISPUTE_CK | BIT |
| SPEED_CK | BIT |
| ILLEGAL_CK | BIT |
| EVALUATION_A_CK | BIT |
| EVALUATION_B_CK | BIT |
| EVALUATION_C_CK | BIT |
| UMPIRE_A_CK | BIT |
| UMPIRE_B_CK | BIT |
| UMPIRE_C_CK | BIT |
| EDUCATION_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_OPERATION_GAME
- **논리명**: 경기 모니터링 사항
- **PK**: `OPERATION_SE, QUESTION_SC, QUESTION_NO`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| OPERATION_SE | INT |
| QUESTION_SC | CHAR |
| QUESTION_NO | INT |
| ANSWER_YN | CHAR |
| REG_DT | DATETIME |

### MONITORING_OPERATION_MASTER
- **논리명**: 경기 모니터링 마스터
- **PK**: `OPERATION_SE, MASTER_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| OPERATION_SE | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_OPERATION_SPECIAL
- **논리명**: 경기 모니터링 특이 사항
- **PK**: `OPERATION_SE`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| OPERATION_SE | INT |
| SPECIAL_CT | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_OPERATION_UMPIRE
- **논리명**: 운영, 심판육성위원 모니터링 심판평가
- **PK**: `OPERATION_SE, UMPIRE_POS_CD, UMPIRE_EVALUATION_CD`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| OPERATION_SE | INT |
| UMPIRE_POS_CD | INT |
| UMPIRE_EVALUATION_CD | INT |
| EVALUATION_NO | INT |
| P_ID | INT |
| POINT_VA | SMALLINT |
| REG_DT | DATETIME |

### MONITORING_SPEED_BASIC
- **논리명**: 경기 스피드업 위반
- **PK**: `SPEED_SE, VIOLATION_SC, VIOLATION_NO, T_ID`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| SPEED_SE | INT |
| VIOLATION_SC | SMALLINT |
| VIOLATION_NO | INT |
| T_ID | CHAR |
| INN_NO | SMALLINT |
| P_ID | INT |
| VIOLATION_TM | TIME |
| VIOLATION_CT | VARCHAR |
| REG_DT | DATETIME |

### MONITORING_SPEED_MASTER
- **논리명**: 경기 스피드업 위반 마스터
- **PK**: `MASTER_SE, SPEED_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| SPEED_SE | INT |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| USER_ID | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

### MONITORING_SPEED_UNIFORM
- **논리명**: 경기 스피드업 위반 유니폼
- **PK**: `SPEED_SE, VIOLATION_SC, VIOLATION_NO, T_ID`
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| SPEED_SE | INT |
| VIOLATION_SC | SMALLINT |
| VIOLATION_NO | INT |
| T_ID | CHAR |
| P_ID | INT |
| REG_DT | DATETIME |

### MONITORING_UMPIRE_REPORT
- **논리명**: 심판 위원 보고서
- **PK**: `MASTER_SE, UMPIRE_SE, UMPIRE_SC`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| UMPIRE_SE | INT |
| UMPIRE_SC | CHAR |
| SUBMIT_CK | BIT |
| TEMP_CK | BIT |
| UMP_P_ID | INT |
| USER_ID | VARCHAR |
| REPORT_CT | VARCHAR |
| ADD_CT | VARCHAR |
| DEL_CK | BIT |
| REG_DT | DATETIME |

---

## OFFICAL (8 tables)

### OFFICIAL_ADDRESS_GROUP
- **논리명**: 주소록 관리
- **PK**: `GROUP_SE`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| GROUP_SE | INT |
| GROUP_NM | VARCHAR |
| REG_DT | DATETIME |

### OFFICIAL_ADDRESS_USER
- **논리명**: 주소록 사용자
- **PK**: `GROUP_SE, USER_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| GROUP_SE | INT |
| USER_ID | VARCHAR |
| REG_DT | DATETIME |

### OFFICIAL_ALARM
- **논리명**: 승인 공시업무 알람
- **PK**: `OFFICIAL_SE, ALARM_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| OFFICIAL_SE | INT |
| ALARM_ID | BIGINT |
| REG_DT | DATETIME |

### OFFICIAL_APPROVAL_GROUP
- **논리명**: 승인 공시업무 그룹 관리
- **PK**: `OFFICIAL_SE, APPROVAL_SE`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| OFFICIAL_SE | INT |
| APPROVAL_SE | INT |
| REG_DT | DATETIME |

### OFFICIAL_ITEM_TEXT
- **논리명**: 텍스트 기존 값 관리
- **PK**: `ITEM_SC`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| ITEM_SC | SMALLINT |
| OFFICIAL_TT | VARCHAR |
| OFFICIAL_CT | VARCHAR |
| REG_DT | DATETIME |

### OFFICIAL_MASTER
- **논리명**: 승인 공시업무 마스터
- **PK**: `OFFICIAL_SE`
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| OFFICIAL_SE | INT |
| OFFICIAL_TT | VARCHAR |
| OFFICIAL_CT | VARCHAR |
| SIGN_CT | VARCHAR |
| OFFICIAL_DT | DATE |
| REG_DT | DATETIME |

### OFFICIAL_RCV_USER
- **논리명**: 승인 공시업무 수신 사용자
- **PK**: `OFFICIAL_SE, RCV_SC, USER_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| OFFICIAL_SE | INT |
| RCV_SC | INT |
| USER_ID | VARCHAR |
| REG_DT | DATETIME |

### OFFICIAL_SIGNATURE
- **논리명**: 서명 관리
- **PK**: `SIGN_SE`
- **컬럼 수**: 8

| Column | Type |
|--------|------|
| SIGN_SE | INT |
| DEPARTMENT_IF | VARCHAR |
| POSITION_IF | VARCHAR |
| SIGNER_NM | VARCHAR |
| SIGN1_CT | VARCHAR |
| SIGN2_CT | VARCHAR |
| SIGN3_CT | VARCHAR |
| REG_DT | DATETIME |

---

## 업무관련 (5 tables)

### CLUB_REQUEST
- **논리명**: 구단 문의
- **PK**: `REQ_SE`
- **컬럼 수**: 13

| Column | Type |
|--------|------|
| REQ_SE | INT |
| LE_ID | SMALLINT |
| T_ID | CHAR |
| REQ_SC | SMALLINT |
| REQ_DT | DATETIME |
| REQ_TT | VARCHAR |
| REQ_CT | VARCHAR |
| FILE_NM | VARCHAR |
| FILE_LK | VARCHAR |
| REPLY_CT | VARCHAR |
| REPLY_CK | CHAR |
| REPLY_DT | DATETIME |
| REG_DT | DATETIME |

### CLUB_REQUEST_SECTION
- **논리명**: 구단 문의 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### FILE_CENTER
- **논리명**: 자료실
- **PK**: `FILE_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| FILE_SE | INT |
| FILE_SC | SMALLINT |
| FILE_NM | VARCHAR |
| FILE_LK | VARCHAR |
| UPLOAD_DT | DATE |
| REG_T_ID | CHAR |
| REG_DT | DATETIME |

### FILE_CENTER_SECTION
- **논리명**: 자료실 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### GENERAL_REQUEST
- **논리명**: 일반 업무 요청
- **PK**: `REQ_SE`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| REQ_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| REQ_T_ID | CHAR |
| ITEM_SC | SMALLINT |
| REQ_DT | DATE |
| FILE_NM | VARCHAR |
| APPROVAL_DT | DATE |
| APPROVAL_CK | BIT `NN` |
| RETURN_CK | BIT `NN` |
| REG_DT | DATETIME |

---

## UNKNOWN (27 tables)

### ALARM
- **논리명**: 알람
- **PK**: `ALARM_ID`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| ALARM_ID | BIGINT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| ALARM_CD | INT |
| ALARM_VA | VARCHAR |
| ALARM_DT | DATETIME |
| REG_ID | VARCHAR |
| REG_COMPANY_CD | INT |
| REG_T_ID | CHAR |
| REG_IP_IF | VARCHAR |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_PLAYER_REG
- **논리명**: 승인 요청 선수 등록
- **PK**: `REQ_SE`
- **컬럼 수**: 15

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| P_ID | INT |
| BIRTH_DT | DATE |
| POS_CD | INT |
| START_DT | DATE |
| PERIOD_CN | INT |
| APPLICANT_NM | VARCHAR |
| NOTE_IF | VARCHAR |
| ORDER_NO | TINYINT |
| PLAYER_REQ_DT | DATETIME |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_TABLE_LIST
- **논리명**: 승인 요청 테이블 목록
- **PK**: `TABLE_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| TABLE_ID | TINYINT |
| TABLE_NM | VARCHAR |
| REG_DT | DATETIME |

### APPROVAL_REQUEST_TEAM_REGISTER
- **논리명**: 승인 요청 팀 등록
- **PK**: `REQ_SE`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| REQ_SE | INT |
| APPROVAL_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| RECORD_DT | DATE |
| REG_DT | DATETIME |

### APPROVAL_SECTION
- **논리명**: 승인 구분
- **PK**: `SC_ID`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| SC_ID | TINYINT |
| SC_NM | VARCHAR |
| REG_DT | DATETIME |

### COMPETITION_RESULT
- **논리명**: 대회 결과
- **PK**: `COMP_ID, RESULT_SC`
- **컬럼 수**: 3

| Column | Type |
|--------|------|
| COMP_ID | SMALLINT |
| RESULT_SC | SMALLINT |
| REG_DT | DATETIME |

### ENTRY_REG
- **논리명**: 엔트리 입력
- **PK**: `LE_ID, SEASON_ID, ENTRY_DT, T_ID, P_ID`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| ENTRY_DT | VARCHAR |
| T_ID | CHAR |
| P_ID | INT |
| P_NM | VARCHAR |
| BACK_NO | VARCHAR |
| POS_CD | INT |
| REG_YN | CHAR |
| CHANGE_CK | BIT `NN` |
| REG_DT | DATETIME |

### ENTRY_REG_ETC
- **논리명**: 엔트리 등록 기타사항
- **PK**: `LE_ID, SEASON_ID, ENTRY_DT, T_ID, P_ID`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| ENTRY_DT | VARCHAR |
| T_ID | CHAR |
| P_ID | INT |
| MASTER_SE | INT |
| GROUP_ID | SMALLINT |
| REG_REASON_CD | INT |
| REG_DT | DATETIME |

### ENTRY_REG_ETC_MASTER
- **논리명**: 엔트리 입력 기타사항 마스터
- **PK**: `MASTER_SE`
- **컬럼 수**: 10

| Column | Type |
|--------|------|
| MASTER_SE | INT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| P_ID | INT |
| START_DT | VARCHAR |
| END_DT | VARCHAR |
| GROUP_ID | SMALLINT |
| REG_REASON_CD | INT |
| REG_DT | DATETIME |

### ENTRY_REG_LOG
- **논리명**: 엔트리 입력 로그
- **PK**: `ALARM_ID, LE_ID, SEASON_ID, ENTRY_DT, T_ID, P_ID`
- **컬럼 수**: 12

| Column | Type |
|--------|------|
| ALARM_ID | BIGINT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| ENTRY_DT | VARCHAR |
| T_ID | CHAR |
| P_ID | INT |
| P_NM | VARCHAR |
| BACK_NO | VARCHAR |
| POS_CD | INT |
| REG_YN | CHAR |
| CHANGE_CK | BIT `NN` |
| REG_DT | DATETIME |

### ENTRY_REG_MASTER
- **논리명**: 엔트리 입력 마스터
- **PK**: `LE_ID, SEASON_ID, ENTRY_DT, T_ID`
- **컬럼 수**: 11

| Column | Type |
|--------|------|
| LE_ID | INT |
| SEASON_ID | SMALLINT |
| ENTRY_DT | VARCHAR |
| T_ID | CHAR |
| APPROVE_CK | BIT `NN` |
| APPROVE_ID_VA | VARCHAR |
| APPROVE_IP_VA | VARCHAR |
| APPROVE_DT | DATETIME |
| REG_ID_VA | VARCHAR |
| REG_IP_VA | VARCHAR |
| REG_DT | DATETIME |

### ENTRY_REG_MASTER_LOG
- **논리명**: 엔트리 입력 마스터 로그
- **PK**: `ALARM_ID`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| ALARM_ID | BIGINT |
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| ENTRY_DT | VARCHAR |
| T_ID | CHAR |
| IP_VA | VARCHAR |
| ID_VA | VARCHAR |
| ACT_CD | INT |
| REG_DT | DATETIME |

### ENTRY_SETUP
- **논리명**: 엔트리 인원 관리
- **PK**: `S_DT, E_DT, LE_ID`
- **컬럼 수**: 9

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| S_DT | VARCHAR |
| E_DT | VARCHAR |
| SEASON_ID | SMALLINT |
| P_ENTRY_CN | SMALLINT |
| DH_P_ENTRY_CN | SMALLINT |
| C_ENTRY_CN | SMALLINT |
| QC_ENTRY_CN | SMALLINT |
| REG_DT | DATETIME |

### PLAYER_BASE
- **논리명**: 선수 승인 확인
- **PK**: `SEASON_ID, P_NM, BIRTH_DT`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| SEASON_ID | SMALLINT |
| P_NM | VARCHAR |
| BIRTH_DT | VARCHAR |
| P_ID | INT |
| T_ID | CHAR |
| P_CHN_NM | VARCHAR |
| P_ENG_NM | VARCHAR |
| P_FULL_NM | VARCHAR |
| BACK_NO | VARCHAR |
| POS_CD | INT |
| HEIGHT_VA | FLOAT |
| WEIGHT_VA | FLOAT |
| PIT_DIREC_CD | INT |
| PIT_FORM_CD | INT |
| HIT_DIREC_CD | INT |
| REG_CD | INT |
| ACTIVE_CD | INT |
| JOIN_DT | DATE |
| JOIN_TEAM_IF | VARCHAR |
| PAYMENT_VA | INT |
| PAYMENT_MONEY_CD | INT |
| SALARY_VA | INT |
| SALARY_MONEY_CD | INT |
| BLOOD_SC | VARCHAR |
| SCH_LITTLE_NM | VARCHAR |
| SCH_ELE_AREA_SC | TINYINT |
| SCH_ELE_NM | VARCHAR |

### PLAYER_PENALTY
- **논리명**: 선수 징계 관리
- **PK**: `PENALTY_SE`
- **컬럼 수**: 8

| Column | Type |
|--------|------|
| PENALTY_SE | INT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| P_ID | INT |
| PENALTY_CD | INT |
| PENALTY_START_DT | DATE |
| PENALTY_GAME_CN | SMALLINT |
| REG_DT | DATETIME |

### SEASON_PLAYER_HITTER
- **논리명**: 시즌별 선수 타자
- **PK**: `LE_ID, SR_ID, SEASON_ID, P_ID, SECTION_CD, GROUP_IF`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| SECTION_CD | INT |
| GROUP_IF | VARCHAR |
| HRA_RT | FLOAT |
| GAME_CN | INT |
| PA_CN | INT |
| AB_CN | INT |
| RUN_CN | INT |
| HIT_CN | INT |
| H2_CN | INT |
| H3_CN | INT |
| HR_CN | INT |
| XBH_CN | INT |
| TB_CN | INT |
| MH_HITTER_CN | INT |
| RBI_CN | INT |
| SB_CN | INT |
| CS_CN | INT |
| SB_RT | FLOAT |
| RO_CN | INT |
| POFF_CN | INT |
| SH_CN | INT |
| SF_CN | INT |
| BB_CN | INT |

### SEASON_PLAYER_PITCHER
- **논리명**: 시즌별 선수 투수
- **PK**: `LE_ID, SR_ID, SEASON_ID, P_ID, SECTION_SC, GROUP_IF`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| P_ID | INT |
| SECTION_CD | INT |
| GROUP_IF | VARCHAR |
| ERA_RT | FLOAT |
| GAME_CN | INT |
| START_CN | INT |
| QUIT_CN | INT |
| W_CN | INT |
| START_W_CN | INT |
| RELIEF_W_CN | INT |
| L_CN | INT |
| D_CN | INT |
| HOLD_CN | INT |
| SV_CN | INT |
| SHO_CN | INT |
| CG_CN | INT |
| INN2_CN | INT |
| WRA_RT | FLOAT |
| PA_CN | INT |
| AB_CN | INT |
| PIT_CN | INT |
| R_CN | INT |
| ER_CN | INT |
| HIT_CN | INT |

### SEASON_TEAM_ENTRY
- **논리명**: 시즌별 팀 엔트리
- **PK**: `LE_ID, SEASON_ID, T_ID`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| REGDAY_CN | SMALLINT |
| REG_DT | DATETIME |

### SEASON_TEAM_HITTER
- **논리명**: 시즌 그룹별 팀 타자
- **PK**: `LE_ID, SR_ID, SEASON_ID, T_ID, SECTION_ID, GROUP_IF`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| SECTION_CD | INT |
| GROUP_IF | VARCHAR |
| HRA_RT | FLOAT |
| GAME_CN | INT |
| PA_CN | INT |
| AB_CN | INT |
| RUN_CN | INT |
| HIT_CN | INT |
| H2_CN | INT |
| H3_CN | INT |
| HR_CN | INT |
| TB_CN | INT |
| MH_HITTER_CN | INT |
| RBI_CN | INT |
| SB_CN | INT |
| CS_CN | INT |
| SB_RT | FLOAT |
| RO_CN | INT |
| POFF_CN | INT |
| SH_CN | INT |
| SF_CN | INT |
| BB_CN | INT |
| IB_CN | INT |

### SEASON_TEAM_PITCHER
- **논리명**: 시즌 그룹별 팀 투수
- **PK**: `LE_ID, SR_ID, SEASON_ID, T_ID, SECTION_CD, GROUP_IF`
- **컬럼 수**: 27

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| SECTION_CD | INT |
| GROUP_IF | VARCHAR |
| ERA_RT | FLOAT |
| GAME_CN | INT |
| W_CN | INT |
| L_CN | INT |
| HOLD_CN | INT |
| SV_CN | INT |
| SHO_CN | INT |
| CG_CN | INT |
| INN2_CN | INT |
| WRA_RT | FLOAT |
| PA_CN | INT |
| AB_CN | INT |
| PIT_CN | INT |
| R_CN | INT |
| ER_CN | INT |
| HIT_CN | INT |
| H2_CN | INT |
| H3_CN | INT |
| HR_CN | INT |
| SH_CN | INT |
| SF_CN | INT |

### TEAMRANK
- **논리명**: 팀 순위
- **PK**: `LE_ID, SR_ID, SEASON_ID, T_ID`
- **컬럼 수**: 7

| Column | Type |
|--------|------|
| LE_ID | SMALLINT |
| SR_ID | SMALLINT |
| SEASON_ID | SMALLINT |
| T_ID | CHAR |
| GROUP_SC | VARCHAR |
| RANK_NO | TINYINT |
| REG_DT | DATETIME |

### USER
- **논리명**: 사용자 정보
- **PK**: `USER_ID`
- **컬럼 수**: 14

| Column | Type |
|--------|------|
| USER_ID | VARCHAR |
| AUTH_CD | INT |
| EVALUATION_CD | INT |
| COMPANY_CD | INT |
| T_ID | CHAR |
| USER_PW | VARCHAR |
| USER_NM | VARCHAR |
| EMAIL_VA | VARCHAR |
| PHONE_VA | VARCHAR |
| HAND_PHONE_VA | VARCHAR |
| DEL_CK | BIT `NN` |
| UPDATE_DT | DATETIME |
| DEL_DT | DATETIME |
| REG_DT | DATETIME |

### USER_ALARM_CK
- **논리명**: 사용자 알람 체크
- **PK**: `USER_ID, ALARM_CD`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| USER_ID | VARCHAR |
| ALARM_CD | INT |
| RCV_CK | BIT `NN` |
| REG_DT | DATETIME |

### USER_BLOCK_LOG
- **논리명**: 사용자 차단 로그
- **PK**: `LOG_SE`
- **컬럼 수**: 6

| Column | Type |
|--------|------|
| LOG_SE | INT |
| LOG_DT | DATE |
| IP_IF | VARCHAR |
| SC_ID | SMALLINT |
| UNBLOCK_CK | BIT `NN` |
| REG_DT | DATETIME |

### USER_LOG_SECTION
- **논리명**: 사용자 로그 구분
- **PK**: `SC_ID`
- **컬럼 수**: 4

| Column | Type |
|--------|------|
| SC_ID | SMALLINT |
| SC_NM | VARCHAR |
| GROUP_SC | VARCHAR |
| REG_DT | DATETIME |

### USER_LOGIN_LOG
- **논리명**: 사용자 로그인 로그
- **PK**: `LOG_SE`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| LOG_SE | BIGINT |
| LOG_DT | DATE |
| USER_ID | VARCHAR |
| ACCESS_SC | VARCHAR |
| REG_DT | DATETIME |

### USER_LOGIN_TRY_LOG
- **논리명**: 사용자 로그인 시도 로그
- **PK**: `LOG_SE`
- **컬럼 수**: 5

| Column | Type |
|--------|------|
| LOG_SE | BIGINT |
| LOG_DT | DATE |
| IP_IF | VARCHAR |
| SC_ID | SMALLINT |
| REG_DT | DATETIME |
