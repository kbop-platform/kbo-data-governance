# OPS 테이블 명세서 (Sports2i)

출처: KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf
테이블 수: 111개
총 컬럼 수: 1821개

## 카테고리별 목차

### MASTER (23개)
- [CODE](#code) - 코드 (12컬럼)
- [GAME](#game) - 경기 (24컬럼)
- [GAME_SECTION](#game_section) - 경기 구분 (7컬럼)
- [GAME_ASSIGN](#game_assign) - 경기 인원 배정 (28컬럼)
- [GAME_CANCEL_MEMO](#game_cancel_memo) - 경기 취소 메모 (11컬럼)
- [GAME_START_PITCHER](#game_start_pitcher) - 경기 선발 투수 (15컬럼)
- [STADIUM](#stadium) - 구장 정보 (8컬럼)
- [TEAM](#team) - 팀 정보 (11컬럼)
- [PLAYER](#player) - 선수 명단 (27컬럼)
- [PLAYER_DRAFT](#player_draft) - 선수 신인지명 (6컬럼)
- [PLAYER_FA](#player_fa) - 선수 FA (8컬럼)
- [PLAYER_CAREER](#player_career) - 선수 경력 (16컬럼)
- [PLAYER_CAREER_SECTION](#player_career_section) - 선수 경력 구분 (6컬럼)
- [PLAYER_SALARY](#player_salary) - 선수 연봉 (13컬럼)
- [SALARY_CAP](#salary_cap) - 샐리러 캡 (8컬럼)
- [AREA_SECTION](#area_section) - 지역 구분 (6컬럼)
- [COMPETITION_NATION](#competition_nation) - 대회 국가 (10컬럼)
- [COMPETITION_RESULT_SECTION](#competition_result_section) - 대회 결과 구분 (6컬럼)
- [SCHOOL](#school) - 학교 정보 (8컬럼)
- [SCHOOL_SECTION](#school_section) - 학교 정보 구분 (6컬럼)
- [UMPIRE_EVALUATION_GROUP](#umpire_evaluation_group) - 심판 행동강령 평가표 그룹 (12컬럼)
- [BOARD_PLAYER_STATE](#board_player_state) - 선수 이동 현황 (19컬럼)
- [BOARD_PLAYER_STATE_SECTION](#board_player_state_section) - 선수 이동 현황 구분 (6컬럼)

### RECORD (9개)
- [GAME_INFO](#game_info) - 경기 정보 (30컬럼)
- [GAME_INN_SCORE](#game_inn_score) - 경기 이닝별 점수 (14컬럼)
- [GAME_RESULT](#game_result) - 경기 결과 (12컬럼)
- [GAME_PLAYER_PITCHER](#game_player_pitcher) - 경기별 선수 투수 (49컬럼)
- [GAME_PLAYER_HITTER](#game_player_hitter) - 경기별 선수 타자 (54컬럼)
- [GAME_TEAM_PITCHER](#game_team_pitcher) - 경기별 팀 투수 (47컬럼)
- [GAME_TEAM_HITTER](#game_team_hitter) - 경기별 팀 타자 (46컬럼)
- [SEASON_PLAYER_ENTRY](#season_player_entry) - 시즌별 선수 엔트리 (18컬럼)
- [SEASON_PLAYER_ENTRY_INTNL](#season_player_entry_intnl) - 시즌별 선수 엔트리 국제전 (13컬럼)

###  (27개)
- [SEASON_PLAYER_HITTER](#season_player_hitter) - 시즌별 선수 타자 (54컬럼)
- [SEASON_PLAYER_PITCHER](#season_player_pitcher) - 시즌별 선수 투수 (54컬럼)
- [SEASON_TEAM_ENTRY](#season_team_entry) - 시즌별 팀 엔트리 (10컬럼)
- [SEASON_TEAM_PITCHER](#season_team_pitcher) - 시즌 그룹별 팀 투수 (54컬럼)
- [SEASON_TEAM_HITTER](#season_team_hitter) - 시즌 그룹별 팀 타자 (54컬럼)
- [TEAMRANK](#teamrank) - 팀 순위 (13컬럼)
- [PLAYER_BASE](#player_base) - 선수 승인 확인 (31컬럼)
- [PLAYER_PENALTY](#player_penalty) - 선수 징계 관리 (14컬럼)
- [COMPETITION_RESULT](#competition_result) - 대회 결과 (6컬럼)
- [ENTRY_REG](#entry_reg) - 엔트리 입력 (20컬럼)
- [ENTRY_REG_ETC](#entry_reg_etc) - 엔트리 등록 기타사항 (17컬럼)
- [ENTRY_REG_ETC_MASTER](#entry_reg_etc_master) - 엔트리 입력 기타사항 마스터 (19컬럼)
- [ENTRY_REG_LOG](#entry_reg_log) - 엔트리 입력 로그 (22컬럼)
- [ENTRY_REG_MASTER](#entry_reg_master) - 엔트리 입력 마스터 (18컬럼)
- [ENTRY_REG_MASTER_LOG](#entry_reg_master_log) - 엔트리 입력 마스터 로그 (18컬럼)
- [ENTRY_SETUP](#entry_setup) - 엔트리 인원 관리 (16컬럼)
- [ALARM](#alarm) - 알람 (20컬럼)
- [APPROVAL_REQUEST_PLAYER_REG](#approval_request_player_reg) - 승인 요청 선수 등록 (22컬럼)
- [APPROVAL_REQUEST_TABLE_LIST](#approval_request_table_list) - 승인 요청 테이블 목록 (6컬럼)
- [APPROVAL_REQUEST_TEAM_REGISTER](#approval_request_team_register) - 승인 요청 팀 등록 (13컬럼)
- [APPROVAL_SECTION](#approval_section) - 승인 구분 (6컬럼)
- [USER](#user) - 사용자 정보 (19컬럼)
- [USER_ALARM_CK](#user_alarm_ck) - 사용자 알람 체크 (7컬럼)
- [USER_BLOCK_LOG](#user_block_log) - 사용자 차단 로그 (11컬럼)
- [USER_LOG_SECTION](#user_log_section) - 사용자 로그 구분 (8컬럼)
- [USER_LOGIN_LOG](#user_login_log) - 사용자 로그인 로그 (10컬럼)
- [USER_LOGIN_TRY_LOG](#user_login_try_log) - 사용자 로그인 시도 로그 (10컬럼)

### LIVE (3개)
- [LINEUP](#lineup) - 실시간 경기 엔트리 (32컬럼)
- [IE_GAME_MATRIX_MIX](#ie_game_matrix_mix) - 실시간 경기 매트릭스 MIX (49컬럼)
- [IE_GAME_LIVETEXT](#ie_game_livetext) - 실시간 경기 문자중계 (27컬럼)

### ALARM (1개)
- [ALARM_RCV_USER](#alarm_rcv_user) - 알람 수신 사용자 (15컬럼)

### 업무관련 (5개)
- [FILE_CENTER](#file_center) - 자료실 (13컬럼)
- [FILE_CENTER_SECTION](#file_center_section) - 자료실 구분 (6컬럼)
- [CLUB_REQUEST](#club_request) - 구단 문의 (19컬럼)
- [CLUB_REQUEST_SECTION](#club_request_section) - 구단 문의 구분 (6컬럼)
- [GENERAL_REQUEST](#general_request) - 일반 업무 요청 (17컬럼)

### APPROVAL (11개)
- [APPROVAL_ITEM_NOTE](#approval_item_note) - 승인 신청 항목 판독 구분 노트 (8컬럼)
- [APPROVAL_ITEM_SECTION](#approval_item_section) - 승인 신청 항목 판독 구분 (9컬럼)
- [APPROVAL_MASTER](#approval_master) - 승인 마스터 (20컬럼)
- [APPROVAL_REQUEST_ETC](#approval_request_etc) - 승인 요청 기타 사항 (6컬럼)
- [APPROVAL_REQUEST_GAME](#approval_request_game) - 승인 요청 경기 (19컬럼)
- [APPROVAL_REQUEST_OBJECTION](#approval_request_objection) - 승인 요청 반대 (18컬럼)
- [APPROVAL_REQUEST_PLAYER_CHANGE](#approval_request_player_change) - 승인 요청 선수 교체 (25컬럼)
- [APPROVAL_REQUEST_PLAYER_FA_CONTRACT](#approval_request_player_fa_contract) - 승인 요청 FA 선수 계약 (22컬럼)
- [APPROVAL_REQUEST_PLAYER_FA_INOUT](#approval_request_player_fa_inout) - 승인 요청 선수 FA 트레이드 (25컬럼)
- [APPROVAL_REQUEST_PLAYER_INOUT](#approval_request_player_inout) - 승인 요청 선수 트레이드 (29컬럼)
- [APPROVAL_REQUEST_PLAYER_NEW](#approval_request_player_new) - 승인 요청 선수 신규 (26컬럼)

### MONITORING (24개)
- [MONITORING_COVID_BASIC](#monitoring_covid_basic) - 코로나 19 주요 점검 사항 (9컬럼)
- [MONITORING_COVID_MASTER](#monitoring_covid_master) - 코로나 19 주요사항 마스터 (10컬럼)
- [MONITORING_COVID_SPECIAL](#monitoring_covid_special) - 코로나 19 주요 특이 사항 (5컬럼)
- [MONITORING_DISPUTE_REPORT](#monitoring_dispute_report) - 분쟁 및 사고 보고서 (12컬럼)
- [MONITORING_EVALUATION_BASIC](#monitoring_evaluation_basic) - 행동강령 평가표 일반 (9컬럼)
- [MONITORING_EVALUATION_CONTENT](#monitoring_evaluation_content) - 행동강령 평가표 내용 (6컬럼)
- [MONITORING_EVALUATION_MASTER](#monitoring_evaluation_master) - 행동강령 평가표 마스터 (18컬럼)
- [MONITORING_EVALUATION_ROUNDUP](#monitoring_evaluation_roundup) - 행동강령 평가표 모음 (16컬럼)
- [MONITORING_GAME_BASIC](#monitoring_game_basic) - 경기 영상 모니터링 기본 (10컬럼)
- [MONITORING_GAME_DETAIL](#monitoring_game_detail) - 경기 영상 세부 모니터링 사항 (9컬럼)
- [MONITORING_GAME_MASTER](#monitoring_game_master) - 경기 영상 모니터링 마스터 (10컬럼)
- [MONITORING_ILLEGAL_CHECKLIST](#monitoring_illegal_checklist) - 부정행위방지 모니터링 체크리스트 (9컬럼)
- [MONITORING_ILLEGAL_CONTENT](#monitoring_illegal_content) - 부정행위 모니터링 내용 및 조치사항 (13컬럼)
- [MONITORING_ILLEGAL_FILE](#monitoring_illegal_file) - 부정행위방지 모니터링 첨부파일 (7컬럼)
- [MONITORING_ILLEGAL_MASTER](#monitoring_illegal_master) - 부정행위방지 모니터링 마스터 (10컬럼)
- [MONITORING_MASTER](#monitoring_master) - 경기 모니터링 평가 마스터 (25컬럼)
- [MONITORING_OPERATION_GAME](#monitoring_operation_game) - 경기 모니터링 사항 (9컬럼)
- [MONITORING_OPERATION_MASTER](#monitoring_operation_master) - 경기 모니터링 마스터 (10컬럼)
- [MONITORING_OPERATION_SPECIAL](#monitoring_operation_special) - 경기 모니터링 특이 사항 (5컬럼)
- [MONITORING_OPERATION_UMPIRE](#monitoring_operation_umpire) - 운영, 심판육성위원 모니터링 심판평가 (12컬럼)
- [MONITORING_SPEED_BASIC](#monitoring_speed_basic) - 경기 스피드업 위반 (14컬럼)
- [MONITORING_SPEED_MASTER](#monitoring_speed_master) - 경기 스피드업 위반 마스터 (10컬럼)
- [MONITORING_SPEED_UNIFORM](#monitoring_speed_uniform) - 경기 스피드업 위반 유니폼 (11컬럼)
- [MONITORING_UMPIRE_REPORT](#monitoring_umpire_report) - 심판 위원 보고서 (15컬럼)

### OFFICAL (8개)
- [OFFICIAL_ADDRESS_GROUP](#official_address_group) - 주소록 관리 (6컬럼)
- [OFFICIAL_ADDRESS_USER](#official_address_user) - 주소록 사용자 (6컬럼)
- [OFFICIAL_ALARM](#official_alarm) - 승인 공시업무 알람 (6컬럼)
- [OFFICIAL_APPROVAL_GROUP](#official_approval_group) - 승인 공시업무 그룹 관리 (6컬럼)
- [OFFICIAL_ITEM_TEXT](#official_item_text) - 텍스트 기존 값 관리 (6컬럼)
- [OFFICIAL_MASTER](#official_master) - 승인 공시업무 마스터 (9컬럼)
- [OFFICIAL_RCV_USER](#official_rcv_user) - 승인 공시업무 수신 사용자 (8컬럼)
- [OFFICIAL_SIGNATURE](#official_signature) - 서명 관리 (11컬럼)

## CODE
- 논리명: **코드**
- 카테고리: MASTER
- Primary Key: `COLUMN_NM, CODE_ID`
- 컬럼 수: **12**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `COLUMN_NM` | 컬럼 이름 | VARCHAR |  |  |  |  |
| 2 | `CODE_ID` | 코드 ID | INT |  |  |  |  |
| 3 | `CODE_NM` | 코드 이름 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `ORDER_NO` | 순서 번호 | INT |  |  |  |  |
| 5 | `DEL_CK` | 삭제 확인 | BIT |  | NN |  |  |
| 6 | `UPDATE_DT` | 수정 일자 | DATETIME |  |  |  |  |
| 7 | `DEL_DT` | 삭제 일자 | DATETIME |  |  |  |  |
| 8 | `REG_DT` | 등록 일자 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 20 | `NN` | PK |  |  |  |  |  |
| 100 | `NN` |  |  |  |  |  |  |

---

## GAME
- 논리명: **경기**
- 카테고리: MASTER
- Primary Key: `LE_ID, SR_ID, G_ID`
- 컬럼 수: **24**
- 상세: 2. SR_ID : 1 – 시범경기, 0 – 정규경기, 6 – 순위결정전, 4 – 와일드카드결정전, 3 – 준플레이오프, 5 – 플레이
오프, 7 – 한국시리즈, 9 – 올스타전, 8 - 국제전

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `G_DT` | 경기 날짜 | VARCHAR |  |  |  |  |
| 6 | `G_TM` | 경기 시간 | VARCHAR |  |  |  |  |
| 7 | `H_T_ID` | 홈 팀 ID | CHAR |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |
| 8 | `A_T_ID` | 방문 팀 ID | CHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `S_ID` | 구장 ID | VARCHAR |  |  |  |  |
| 10 | `S_NM` | 구장 이름 | VARCHAR |  |  |  |  |
| 11 | `END_CK` | 종료 체크 | BIT |  |  |  |  |
| 12 | `CANCEL_CK` | 경기 취소 체크 | BIT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `CANCEL_SC_ID` | 경기 취소 사유 코드 | SMALLINT |  |  |  |  |
| 14 | `SUSPENDED_CK` | 서스펜디드 체크 | BIT |  |  |  |  |
| 15 | `UPDATE_DT` | 업데이트 일자 | DATETIME |  |  |  |  |
| 16 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## GAME_SECTION
- 논리명: **경기 구분**
- 카테고리: MASTER
- Primary Key: `SC_SC, SC_ID`
- 컬럼 수: **7**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_SC` | 코드 구분 | VARCHAR |  |  |  |  |
| 2 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## GAME_ASSIGN
- 논리명: **경기 인원 배정**
- 카테고리: MASTER
- Primary Key: `LE_ID, SR_ID, G_ID`
- 컬럼 수: **28**
- 상세: 2. SR_ID : 1 – 시범경기, 0 – 정규경기, 6 – 순위결정전, 4 – 와일드카드결정전, 3 – 준플레이오프, 5 – 플레이
오프, 7 – 한국시리즈, 9 – 올스타전, 8 - 국제전

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `AWAY_ID` | 원정 팀 ID | CHAR |  |  |  |  |
| 6 | `HOME_ID` | 홈 팀 ID | CHAR |  |  |  |  |
| 7 | `S_ID` | 구장 ID | CHAR |  |  |  |  |
| 8 | `HEADER_NO` | 더블헤더 번호 | TINYINT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `OPT_U_ID` | 운영자 ID | VARCHAR |  |  |  |  |
| 10 | `UMPC_P_ID` | 주심 ID | INT |  |  |  |  |
| 11 | `UMP1_P_ID` | 1루심 ID | INT |  |  |  |  |
| 12 | `UMP2_P_ID` | 2루심 ID | INT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `UMP3_P_ID` | 3루심 ID | INT |  |  |  |  |
| 14 | `UMPL_P_ID` | 좌선심 ID | INT |  |  |  |  |
| 15 | `UMPR_P_ID` | 우선심 ID | INT |  |  |  |  |
| 16 | `UMPS_P_ID` | 대기심 ID | INT |  |  |  |  |
| 17 | `SCOA_P_ID` | 기록원A ID | INT |  |  |  |  |
| 18 | `SCOB_P_ID` | 기록원B ID | INT |  |  |  |  |
| 19 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## GAME_CANCEL_MEMO
- 논리명: **경기 취소 메모**
- 카테고리: MASTER
- Primary Key: `LE_ID, SR_ID, G_ID`
- 컬럼 수: **11**
- 상세: 2. SR_ID : 1 – 시범경기, 0 – 정규경기, 6 – 순위결정전, 4 – 와일드카드결정전, 3 – 준플레이오프, 5 – 플레이
오프, 7 – 한국시리즈, 9 – 올스타전, 8 - 국제전

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `CANCEL_ME` | 취소 메모 | VARCHAR |  |  |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |

---

## GAME_START_PITCHER
- 논리명: **경기 선발 투수**
- 카테고리: MASTER
- Primary Key: `LE_ID, SR_ID, G_ID`
- 컬럼 수: **15**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `T_PIT_P_ID` | 초 팀 선발 투수 ID | INT |  |  |  |  |
| 6 | `B_PIT_P_ID` | 말 팀 선발 투수 ID | INT |  |  |  |  |
| 7 | `APPR_CK` | 승인 체크 | CHAR |  |  |  |  |
| 8 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |

---

## STADIUM
- 논리명: **구장 정보**
- 카테고리: MASTER
- Primary Key: `SEASON_ID, S_ID`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `S_ID` | 구장 ID | VARCHAR |  |  |  |  |
| 3 | `S_NM` | 구장 이름 | VARCHAR |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 10 | `NN` | PK |  |  |  |  |  |
| 50 | `NN` |  |  |  |  |  |  |

---

## TEAM
- 논리명: **팀 정보**
- 카테고리: MASTER
- Primary Key: `LE_ID, SEASON_ID, T_ID`
- 컬럼 수: **11**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `T_NM` | 팀 이름 | VARCHAR |  |  |  |  |
| 5 | `T_FULL_NM` | 팀 풀네임 | VARCHAR |  |  |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 30 | `NN` |  |  |  |  |  |  |

---

## PLAYER
- 논리명: **선수 명단**
- 카테고리: MASTER
- Primary Key: `LE_ID, SEASON_ID, P_ID`
- 컬럼 수: **27**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 6 | `P_CHN_NM` | 선수 한자 이름 | VARCHAR |  |  |  |  |
| 7 | `P_ENG_NM` | 선수 영문 이름 | VARCHAR |  |  |  |  |
| 8 | `P_FULL_NM` | 선수 풀 네임 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `BACK_NO` | 등 번호 | VARCHAR |  |  |  |  |
| 10 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 11 | `BIRTH_DT` | 생년월일 날짜 | VARCHAR |  |  |  |  |
| 12 | `PIT_DIREC_CD` | 투구 방향 코드 | INT |  |  |  |  |
| 13 | `PIT_FORM_CD` | 투구 폼 코드 | INT |  |  |  |  |
| 14 | `HIT_DIREC_CD` | 타격 방향 코드 | INT |  |  |  |  |
| 15 | `ACTIVE_CD` | 활동 코드 | INT |  |  |  |  |
| 16 | `JOIN_DT` | 입단 날짜 | DATE |  |  |  |  |
| 17 | `SALARY_IF` | 연봉 정보 | VARCHAR |  |  |  |  |
| 18 | `CAREER_IF` | 경력 정보 | VARCHAR |  |  |  |  |
| 19 | `FINAL_CAREER_IF` | 최종 경력 정보 | VARCHAR |  |  |  |  |
| 20 | `FOREIGNER_CK` | 외국인 여부 체크 | BIT |  | NN |  |  |
| 21 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 40 | `NN` |  |  |  |  |  |  |

---

## PLAYER_DRAFT
- 논리명: **선수 신인지명**
- 카테고리: MASTER
- Primary Key: `P_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 2 | `DRAFT_YR` | 드래프트 연도 | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## PLAYER_FA
- 논리명: **선수 FA**
- 카테고리: MASTER
- Primary Key: `LE_ID, SEASON_ID, P_ID`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## PLAYER_CAREER
- 논리명: **선수 경력**
- 카테고리: MASTER
- Primary Key: `CA_RE`
- 컬럼 수: **16**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `CA_RE` | 경력 일련번호 | INT |  |  |  |  |
| 2 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `START_DS` | 시작 일자 | DATE |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `END_DS` | 종료 일자 | DATE |  |  |  |  |
| 5 | `CA_SC` | 경력 구분 | SMALLINT |  |  |  |  |
| 6 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 7 | `BAFORE_T_ID` | 이전 팀 ID | CHAR |  |  |  |  |
| 8 | `ETC_ME` | 기타사항 메모 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## PLAYER_CAREER_SECTION
- 논리명: **선수 경력 구분**
- 카테고리: MASTER
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 50 | `NN` |  |  |  |  |  |  |

---

## PLAYER_SALARY
- 논리명: **선수 연봉**
- 카테고리: MASTER
- Primary Key: `LE_ID, SEASON_ID, P_ID`
- 컬럼 수: **13**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 5 | `PAYMENT_VA` | 계약금 값 | INT |  |  |  |  |
| 6 | `CONTRACT_CN` | 계약기간 수 | SMALLINT |  |  |  |  |
| 7 | `SALARY_VA` | 연봉 값 | INT |  |  |  |  |
| 8 | `OPTION_VA` | 옵션 값 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## SALARY_CAP
- 논리명: **샐리러 캡**
- 카테고리: MASTER
- Primary Key: `LE_ID, SEASON_ID`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `MAX_VA` | 상한액 값 | INT |  |  |  |  |
| 4 | `MIN_VA` | 하한액 값 | INT |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## AREA_SECTION
- 논리명: **지역 구분**
- 카테고리: MASTER
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | TINYINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 10 | `NN` |  |  |  |  |  |  |

---

## COMPETITION_NATION
- 논리명: **대회 국가**
- 카테고리: MASTER
- Primary Key: `COMP_ID`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `COMP_ID` | 대회 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `COMP_YR` | 대회 연도 | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `COMP_CD` | 대회 코드 | VARCHAR |  |  |  |  |
| 4 | `COMP_NM` | 대회 이름 | VARCHAR |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 10 | `NN` |  |  |  |  |  |  |
| 50 | `NN` |  |  |  |  |  |  |

---

## COMPETITION_RESULT_SECTION
- 논리명: **대회 결과 구분**
- 카테고리: MASTER
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 50 | `NN` |  |  |  |  |  |  |

---

## SCHOOL
- 논리명: **학교 정보**
- 카테고리: MASTER
- Primary Key: `AREA_SC, SCH_SC, SCH_NM`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `AREA_SC` | 지역 구분 | TINYINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `SCH_SC` | 학교 구분 | TINYINT |  |  |  |  |
| 3 | `SCH_NM` | 학교 이름 | VARCHAR |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 40 | `NN` | PK |  |  |  |  |  |

---

## SCHOOL_SECTION
- 논리명: **학교 정보 구분**
- 카테고리: MASTER
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | TINYINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## UMPIRE_EVALUATION_GROUP
- 논리명: **심판 행동강령 평가표 그룹**
- 카테고리: MASTER
- Primary Key: `LE_ID, SEASON_ID, P_ID`
- 컬럼 수: **12**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `P_ID` | 심판 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `EVALUATION_CD` | 평가표 코드 | INT |  |  |  |  |
| 5 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 6 | `CHAIRMAN_USER_ID` | 의장 ID | VARCHAR |  |  |  |  |
| 7 | `TEAMLEADER_USER_ID` | 팀 주장 사용자 ID | VARCHAR |  |  |  |  |
| 8 | `GROUP_NO` | 그룹 번호 | SMALLINT |  |  |  |  |
| 9 | `FIRST_SECOND_CK` | 1.5분 심판 확인 | BIT |  |  |  |  |

---

## BOARD_PLAYER_STATE
- 논리명: **선수 이동 현황**
- 카테고리: MASTER
- Primary Key: `BD_SE`
- 컬럼 수: **19**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `BD_SE` | 게시판 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `BD_DT` | 게시판 일자 | DATE |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `BD_SC` | 게시판 구분 | TINYINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEAM_NM` | 팀 이름 | VARCHAR |  |  |  |  |
| 5 | `BEFORE_TEAM_NM` | 이전 팀 이름 | VARCHAR |  |  |  |  |
| 6 | `PLAYER_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 7 | `POS_IF` | 포지션 정보 | VARCHAR |  |  |  |  |
| 8 | `ETC_IF` | 기타사항 정보 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `MAIN_YN` | 메인 여부 | CHAR |  |  |  |  |
| 10 | `NN` |  |  |  |  |  |  |
| 10 | `ORDER_NO` | 순서 번호 | INT |  |  |  |  |
| 11 | `GROUP_NO` | 그룹 번호 | TINYINT |  |  |  |  |
| 12 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## BOARD_PLAYER_STATE_SECTION
- 논리명: **선수 이동 현황 구분**
- 카테고리: MASTER
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | TINYINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 50 | `NN` |  |  |  |  |  |  |

---

## GAME_INFO
- 논리명: **경기 정보**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID`
- 컬럼 수: **30**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `AWAY_ID` | 원정 팀 ID | CHAR |  |  |  |  |
| 6 | `HOME_ID` | 홈 팀 ID | CHAR |  |  |  |  |
| 7 | `START_DT` | 경기 실제 시작 시간 | DATETIME |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |
| 8 | `END_DT` | 경기 실제 종료 시간 | DATETIME |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `USE_DT` | 경기 소요 시간 | TIME |  |  |  |  |
| 10 | `DELAY_TM` | 경기 지연 시간 | VARCHAR |  |  |  |  |
| 11 | `EX_INN9_USE_DT` | 연장 경기 9회까지 소요 시간 | TIME |  |  |  |  |
| 12 | `HALF_SC` | 전후반기 구분 | CHAR |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `UMPC_P_ID` | 주심 ID | INT |  |  |  |  |
| 14 | `UMP1_P_ID` | 1루심 ID | INT |  |  |  |  |
| 15 | `UMP2_P_ID` | 2루심 ID | INT |  |  |  |  |
| 16 | `UMP3_P_ID` | 3루심 ID | INT |  |  |  |  |
| 17 | `UMPL_P_ID` | 좌선심 ID | INT |  |  |  |  |
| 18 | `UMPR_P_ID` | 우선심 ID | INT |  |  |  |  |
| 19 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## GAME_INN_SCORE
- 논리명: **경기 이닝별 점수**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID, INN_NO, TB_SC`
- 컬럼 수: **14**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `INN_NO` | 이닝 번호 | TINYINT |  |  |  |  |
| 5 | `TB_SC` | 초/말 구분 | CHAR |  |  |  |  |
| 6 | `SCORE_CN` | 점수 | SMALLINT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |

---

## GAME_RESULT
- 논리명: **경기 결과**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID`
- 컬럼 수: **12**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `T_SCORE_CN` | 초(원정)팀 점수 | SMALLINT |  |  |  |  |
| 5 | `B_SCORE_CN` | 말(홈)팀 점수 | SMALLINT |  |  |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |

---

## GAME_PLAYER_PITCHER
- 논리명: **경기별 선수 투수**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID, P_ID`
- 컬럼 수: **49**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 7 | `TURN_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 8 | `ERA_RT` | 평균자책점 율 | FLOAT |  |  |  |  |
| 9 | `RESULT_SC` | 결과 구분 | CHAR |  |  |  |  |
| 10 | `START_CK` | 개시 체크 | BIT |  | NN |  |  |
| 11 | `QUIT_CK` | 종료 체크 | BIT |  | NN |  |  |
| 12 | `SHO_CK` | 완봉 체크 | BIT |  | NN |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `CG_CK` | 완투 체크 | BIT |  | NN |  |  |
| 14 | `INN2_CN` | 이닝 수 | SMALLINT |  |  |  |  |
| 15 | `PA_CN` | 타자 수 | SMALLINT |  |  |  |  |
| 16 | `AB_CN` | 타수 수 | SMALLINT |  |  |  |  |
| 17 | `PIT_CN` | 투구 수 | SMALLINT |  |  |  |  |
| 18 | `R_CN` | 실점 수 | SMALLINT |  |  |  |  |
| 19 | `ER_CN` | 자책점 수 | SMALLINT |  |  |  |  |
| 20 | `ERR_CN` | 실책 수 | SMALLINT |  |  |  |  |
| 21 | `HIT_CN` | 안타 수 | SMALLINT |  |  |  |  |
| 22 | `H2_CN` | 2루타 수 | SMALLINT |  |  |  |  |
| 23 | `H3_CN` | 3루타 수 | SMALLINT |  |  |  |  |
| 24 | `HR_CN` | 홈런 수 | SMALLINT |  |  |  |  |
| 25 | `SH_CN` | 희타 수 | SMALLINT |  |  |  |  |
| 26 | `SF_CN` | 희비 수 | SMALLINT |  |  |  |  |
| 27 | `BB_CN` | 볼넷 수 | SMALLINT |  |  |  |  |

---

## GAME_PLAYER_HITTER
- 논리명: **경기별 선수 타자**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID, P_ID`
- 컬럼 수: **54**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 7 | `BAT_TURN_NO` | 타순 순서 번호 | TINYINT |  |  |  |  |
| 8 | `BAT_ORDER_NO` | 타순 번호 | TINYINT |  |  |  |  |
| 9 | `HRA_RT` | 타 율 | FLOAT |  |  |  |  |
| 10 | `PA_CN` | 타석 수 | SMALLINT |  |  |  |  |
| 11 | `AB_CN` | 타수 수 | SMALLINT |  |  |  |  |
| 12 | `RUN_CN` | 득점 수 | SMALLINT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `HIT_CN` | 안타 수 | SMALLINT |  |  |  |  |
| 14 | `H2_CN` | 2루타 수 | SMALLINT |  |  |  |  |
| 15 | `H3_CN` | 3루타 수 | SMALLINT |  |  |  |  |
| 16 | `HR_CN` | 홈런 수 | SMALLINT |  |  |  |  |
| 17 | `RBI_CN` | 타점 수 | SMALLINT |  |  |  |  |
| 18 | `SB_CN` | 도루 수 | SMALLINT |  |  |  |  |
| 19 | `CS_CN` | 도루실패 수 | SMALLINT |  |  |  |  |
| 20 | `RO_CN` | 주루사 수 | SMALLINT |  |  |  |  |
| 21 | `POFF_CN` | 견제사 수 | SMALLINT |  |  |  |  |
| 22 | `SH_CN` | 희타 수 | SMALLINT |  |  |  |  |
| 23 | `SF_CN` | 희비 수 | SMALLINT |  |  |  |  |
| 24 | `BB_CN` | 볼넷 수 | SMALLINT |  |  |  |  |
| 25 | `IB_CN` | 고의4구 수 | SMALLINT |  |  |  |  |
| 26 | `HP_CN` | 사구 수 | SMALLINT |  |  |  |  |
| 27 | `KK_CN` | 삼진 수 | SMALLINT |  |  |  |  |

---

## GAME_TEAM_PITCHER
- 논리명: **경기별 팀 투수**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID, T_ID`
- 컬럼 수: **47**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 7 | `ERA_RT` | 평균자책점 율 | FLOAT |  |  |  |  |
| 8 | `RESULT_SC` | 결과 구분 | CHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `INN2_CN` | 이닝 수 | SMALLINT |  |  |  |  |
| 10 | `AB_CN` | 타수 수 | SMALLINT |  |  |  |  |
| 11 | `R_CN` | 실점 수 | SMALLINT |  |  |  |  |
| 12 | `ER_CN` | 자책점 수 | SMALLINT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `HIT_CN` | 안타 수 | SMALLINT |  |  |  |  |
| 14 | `H2_CN` | 2루타 수 | SMALLINT |  |  |  |  |
| 15 | `H3_CN` | 3루타 수 | SMALLINT |  |  |  |  |
| 16 | `HR_CN` | 홈런 수 | SMALLINT |  |  |  |  |
| 17 | `SH_CN` | 희타 수 | SMALLINT |  |  |  |  |
| 18 | `SF_CN` | 희비 수 | SMALLINT |  |  |  |  |
| 19 | `BB_CN` | 볼넷 수 | SMALLINT |  |  |  |  |
| 20 | `HP_CN` | 사구 수 | SMALLINT |  |  |  |  |
| 21 | `KK_CN` | 삼진 수 | SMALLINT |  |  |  |  |
| 22 | `ERR_CN` | 실책 수 | SMALLINT |  |  |  |  |
| 23 | `QS_CK` | 퀄리티스타트 체크 | BIT |  | NN |  |  |
| 24 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## GAME_TEAM_HITTER
- 논리명: **경기별 팀 타자**
- 카테고리: RECORD
- Primary Key: `LE_ID, SR_ID, G_ID, T_ID`
- 컬럼 수: **46**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 7 | `HRA_RT` | 타 율 | FLOAT |  |  |  |  |
| 8 | `AB_CN` | 타수 수 | SMALLINT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `RUN_CN` | 득점 수 | SMALLINT |  |  |  |  |
| 10 | `HIT_CN` | 안타 수 | SMALLINT |  |  |  |  |
| 11 | `H2_CN` | 2루타 수 | SMALLINT |  |  |  |  |
| 12 | `H3_CN` | 3루타 수 | SMALLINT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `HR_CN` | 홈런 수 | SMALLINT |  |  |  |  |
| 14 | `SB_CN` | 도루 수 | SMALLINT |  |  |  |  |
| 15 | `CS_CN` | 도루실패 수 | SMALLINT |  |  |  |  |
| 16 | `RO_CN` | 주루사 수 | SMALLINT |  |  |  |  |
| 17 | `POFF_CN` | 견제사 수 | SMALLINT |  |  |  |  |
| 18 | `SH_CN` | 희타 수 | SMALLINT |  |  |  |  |
| 19 | `SF_CN` | 희비 수 | SMALLINT |  |  |  |  |
| 20 | `BB_CN` | 볼넷 수 | SMALLINT |  |  |  |  |
| 21 | `HP_CN` | 사구 수 | SMALLINT |  |  |  |  |
| 22 | `ERR_CN` | 실책 수 | SMALLINT |  |  |  |  |
| 23 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## SEASON_PLAYER_ENTRY
- 논리명: **시즌별 선수 엔트리**
- 카테고리: RECORD
- Primary Key: `LE_ID, SEASON_ID, P_ID`
- 컬럼 수: **18**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 5 | `REGDAY_CN` | 선수 등록일 수 | SMALLINT |  |  |  |  |
| 6 | `PITHIT_SC` | 투수 타자 구분 | CHAR |  |  |  |  |
| 7 | `RECORD_CN` | 기록 수 | SMALLINT |  |  |  |  |
| 8 | `FA_REGDAY_CK` | FA 선수 등록일 확인 | BIT |  | NN |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `FA_RECORD_CK` | FA 기록 확인 | BIT |  | NN |  |  |
| 10 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## SEASON_PLAYER_ENTRY_INTNL
- 논리명: **시즌별 선수 엔트리 국제전**
- 카테고리: RECORD
- Primary Key: `LE_ID, SEASON_ID, P_ID, INTNL_SC`
- 컬럼 수: **13**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `INTNL_SC` | 국제전 구분 | VARCHAR |  |  |  |  |
| 5 | `REGDAY_CN` | 선수 등록일 수 | SMALLINT |  |  |  |  |
| 6 | `FA_USE_CK` | FA 사용 확인 | BIT |  | NN |  |  |
| 7 | `MILITARY_CK` | 군 복무 확인 | BIT |  | NN |  |  |
| 8 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 10 | `NN` | PK |  |  |  |  |  |

---

## SEASON_PLAYER_HITTER
- 논리명: **시즌별 선수 타자**
- 카테고리: 
- Primary Key: `LE_ID, SR_ID, SEASON_ID, P_ID, SECTION_CD, GROUP_IF`
- 컬럼 수: **54**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SECTION_CD` | 그룹 구분 코드 | INT |  |  |  |  |
| 6 | `GROUP_IF` | 그룹 정보 | VARCHAR |  |  |  |  |
| 7 | `HRA_RT` | 타 율 | FLOAT |  |  |  |  |
| 8 | `GAME_CN` | 경기 수 | INT |  |  |  |  |
| 9 | `PA_CN` | 타석 수 | INT |  |  |  |  |
| 10 | `AB_CN` | 타수 수 | INT |  |  |  |  |
| 11 | `RUN_CN` | 득점 수 | INT |  |  |  |  |
| 12 | `HIT_CN` | 안타 수 | INT |  |  |  |  |
| 13 | `H2_CN` | 2루타 수 | INT |  |  |  |  |
| 14 | `H3_CN` | 3루타 수 | INT |  |  |  |  |
| 15 | `HR_CN` | 홈런 수 | INT |  |  |  |  |
| 16 | `XBH_CN` | 장타 수 | INT |  |  |  |  |
| 17 | `TB_CN` | 루타 수 | INT |  |  |  |  |
| 18 | `MH_HITTER_CN` | 멀티안타 타자 수 | INT |  |  |  |  |
| 19 | `RBI_CN` | 타점 수 | INT |  |  |  |  |
| 20 | `NN` | PK |  |  |  |  |  |
| 20 | `SB_CN` | 도루 수 | INT |  |  |  |  |
| 21 | `CS_CN` | 도루실패 수 | INT |  |  |  |  |
| 22 | `SB_RT` | 도루성공 율 | FLOAT |  |  |  |  |
| 23 | `RO_CN` | 주루사 수 | INT |  |  |  |  |
| 24 | `POFF_CN` | 견제사 수 | INT |  |  |  |  |
| 25 | `SH_CN` | 희타 수 | INT |  |  |  |  |
| 26 | `SF_CN` | 희비 수 | INT |  |  |  |  |
| 27 | `BB_CN` | 볼넷 수 | INT |  |  |  |  |

---

## SEASON_PLAYER_PITCHER
- 논리명: **시즌별 선수 투수**
- 카테고리: 
- Primary Key: `LE_ID, SR_ID, SEASON_ID, P_ID, SECTION_SC, GROUP_IF`
- 컬럼 수: **54**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SECTION_CD` | 그룹 구분 코드 | INT |  |  |  |  |
| 6 | `GROUP_IF` | 그룹 정보 | VARCHAR |  |  |  |  |
| 7 | `ERA_RT` | 평균자책점 율 | FLOAT |  |  |  |  |
| 8 | `GAME_CN` | 경기 수 | INT |  |  |  |  |
| 9 | `START_CN` | 개시 수 | INT |  |  |  |  |
| 10 | `QUIT_CN` | 종료 수 | INT |  |  |  |  |
| 11 | `W_CN` | 승 수 | INT |  |  |  |  |
| 12 | `START_W_CN` | 선발승 수 | INT |  |  |  |  |
| 13 | `RELIEF_W_CN` | 구원승 수 | INT |  |  |  |  |
| 14 | `L_CN` | 패 수 | INT |  |  |  |  |
| 15 | `D_CN` | 무승부 수 | INT |  |  |  |  |
| 16 | `HOLD_CN` | 홀드 수 | INT |  |  |  |  |
| 17 | `SV_CN` | 세이브 수 | INT |  |  |  |  |
| 18 | `SHO_CN` | 완봉 수 | INT |  |  |  |  |
| 19 | `CG_CN` | 완투 수 | INT |  |  |  |  |
| 20 | `NN` | PK |  |  |  |  |  |
| 20 | `INN2_CN` | 이닝 수 | INT |  |  |  |  |
| 21 | `WRA_RT` | 승 률 | FLOAT |  |  |  |  |
| 22 | `PA_CN` | 타자 수 | INT |  |  |  |  |
| 23 | `AB_CN` | 타수 수 | INT |  |  |  |  |
| 24 | `PIT_CN` | 투구 수 | INT |  |  |  |  |
| 25 | `R_CN` | 실점 수 | INT |  |  |  |  |
| 26 | `ER_CN` | 자책점 수 | INT |  |  |  |  |
| 27 | `HIT_CN` | 안타 수 | INT |  |  |  |  |

---

## SEASON_TEAM_ENTRY
- 논리명: **시즌별 팀 엔트리**
- 카테고리: 
- Primary Key: `LE_ID, SEASON_ID, T_ID`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `T_ID` | 선수 ID | CHAR |  |  |  |  |
| 4 | `REGDAY_CN` | 선수 등록일 수 | SMALLINT |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## SEASON_TEAM_PITCHER
- 논리명: **시즌 그룹별 팀 투수**
- 카테고리: 
- Primary Key: `LE_ID, SR_ID, SEASON_ID, T_ID, SECTION_CD, GROUP_IF`
- 컬럼 수: **54**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SECTION_CD` | 그룹 구분 코드 | INT |  |  |  |  |
| 6 | `GROUP_IF` | 그룹 정보 | VARCHAR |  |  |  |  |
| 7 | `ERA_RT` | 평균자책점 율 | FLOAT |  |  |  |  |
| 8 | `GAME_CN` | 경기 수 | INT |  |  |  |  |
| 9 | `W_CN` | 승 수 | INT |  |  |  |  |
| 10 | `L_CN` | 패 수 | INT |  |  |  |  |
| 11 | `HOLD_CN` | 홀드 수 | INT |  |  |  |  |
| 12 | `SV_CN` | 세이브 수 | INT |  |  |  |  |
| 13 | `SHO_CN` | 완봉 수 | INT |  |  |  |  |
| 14 | `CG_CN` | 완투 수 | INT |  |  |  |  |
| 15 | `INN2_CN` | 이닝 수 | INT |  |  |  |  |
| 16 | `WRA_RT` | 승 율 | FLOAT |  |  |  |  |
| 17 | `PA_CN` | 타자 수 | INT |  |  |  |  |
| 18 | `AB_CN` | 타수 수 | INT |  |  |  |  |
| 19 | `PIT_CN` | 투구 수 | INT |  |  |  |  |
| 20 | `NN` | PK |  |  |  |  |  |
| 20 | `R_CN` | 실점 수 | INT |  |  |  |  |
| 21 | `ER_CN` | 자책점 수 | INT |  |  |  |  |
| 22 | `HIT_CN` | 안타 수 | INT |  |  |  |  |
| 23 | `H2_CN` | 2루타 수 | INT |  |  |  |  |
| 24 | `H3_CN` | 3루타 수 | INT |  |  |  |  |
| 25 | `HR_CN` | 홈런 수 | INT |  |  |  |  |
| 26 | `SH_CN` | 희타 수 | INT |  |  |  |  |
| 27 | `SF_CN` | 희비 수 | INT |  |  |  |  |

---

## SEASON_TEAM_HITTER
- 논리명: **시즌 그룹별 팀 타자**
- 카테고리: 
- Primary Key: `LE_ID, SR_ID, SEASON_ID, T_ID, SECTION_ID, GROUP_IF`
- 컬럼 수: **54**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SECTION_CD` | 그룹 구분 코드 | INT |  |  |  |  |
| 6 | `GROUP_IF` | 그룹 정보 | VARCHAR |  |  |  |  |
| 7 | `HRA_RT` | 타 율 | FLOAT |  |  |  |  |
| 8 | `GAME_CN` | 경기 수 | INT |  |  |  |  |
| 9 | `PA_CN` | 타석 수 | INT |  |  |  |  |
| 10 | `AB_CN` | 타수 수 | INT |  |  |  |  |
| 11 | `RUN_CN` | 득점 수 | INT |  |  |  |  |
| 12 | `HIT_CN` | 안타 수 | INT |  |  |  |  |
| 13 | `H2_CN` | 2루타 수 | INT |  |  |  |  |
| 14 | `H3_CN` | 3루타 수 | INT |  |  |  |  |
| 15 | `HR_CN` | 홈런 수 | INT |  |  |  |  |
| 16 | `TB_CN` | 루타 수 | INT |  |  |  |  |
| 17 | `MH_HITTER_CN` | 멀티안타 타자 수 | INT |  |  |  |  |
| 18 | `RBI_CN` | 타점 수 | INT |  |  |  |  |
| 19 | `SB_CN` | 도루 수 | INT |  |  |  |  |
| 20 | `NN` | PK |  |  |  |  |  |
| 20 | `CS_CN` | 도루실패 수 | INT |  |  |  |  |
| 21 | `SB_RT` | 도루성공 율 | FLOAT |  |  |  |  |
| 22 | `RO_CN` | 주루사 수 | INT |  |  |  |  |
| 23 | `POFF_CN` | 견제사 수 | INT |  |  |  |  |
| 24 | `SH_CN` | 희타 수 | INT |  |  |  |  |
| 25 | `SF_CN` | 희비 수 | INT |  |  |  |  |
| 26 | `BB_CN` | 볼넷 수 | INT |  |  |  |  |
| 27 | `IB_CN` | 고의4구 수 | INT |  |  |  |  |

---

## TEAMRANK
- 논리명: **팀 순위**
- 카테고리: 
- Primary Key: `LE_ID, SR_ID, SEASON_ID, T_ID`
- 컬럼 수: **13**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 5 | `GROUP_SC` | 그룹 구분 | VARCHAR |  |  |  |  |
| 6 | `RANK_NO` | 순위 번호 | TINYINT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## PLAYER_BASE
- 논리명: **선수 승인 확인**
- 카테고리: 
- Primary Key: `SEASON_ID, P_NM, BIRTH_DT`
- 컬럼 수: **31**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 3 | `BIRTH_DT` | 생년월일 날짜 | VARCHAR |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 6 | `P_CHN_NM` | 선수 한자 이름 | VARCHAR |  |  |  |  |
| 7 | `P_ENG_NM` | 선수 영어 이름 | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `P_FULL_NM` | 선수 풀 네임 | VARCHAR |  |  |  |  |
| 9 | `BACK_NO` | 등 번호 | VARCHAR |  |  |  |  |
| 10 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 11 | `HEIGHT_VA` | 키 값 | FLOAT |  |  |  |  |
| 12 | `WEIGHT_VA` | 몸무게 값 | FLOAT |  |  |  |  |
| 13 | `PIT_DIREC_CD` | 투구 방향 코드 | INT |  |  |  |  |
| 14 | `PIT_FORM_CD` | 투구 폼 코드 | INT |  |  |  |  |
| 15 | `HIT_DIREC_CD` | 타격 방향 코드 | INT |  |  |  |  |
| 16 | `REG_CD` | 등록 코드 | INT |  |  |  |  |
| 17 | `ACTIVE_CD` | 활동 코드 | INT |  |  |  |  |
| 18 | `JOIN_DT` | 입단 일자 | DATE |  |  |  |  |
| 19 | `JOIN_TEAM_IF` | 입단 팀 정보 | VARCHAR |  |  |  |  |
| 20 | `PAYMENT_VA` | 계약금 값 | INT |  |  |  |  |
| 21 | `PAYMENT_MONEY_CD` | 계약 금액 코드 | INT |  |  |  |  |
| 22 | `SALARY_VA` | 연봉 값 | INT |  |  |  |  |
| 23 | `SALARY_MONEY_CD` | 연봉 금액 코드 | INT |  |  |  |  |
| 24 | `BLOOD_SC` | 혈액형 구분 | VARCHAR |  |  |  |  |
| 25 | `SCH_LITTLE_NM` | 학교 축약 이름 | VARCHAR |  |  |  |  |
| 26 | `SCH_ELE_AREA_SC` | 초등학교 지역 구분 | TINYINT |  |  |  |  |
| 27 | `SCH_ELE_NM` | 초등학교 이름 | VARCHAR |  |  |  |  |
| 40 | `NN` | PK |  |  |  |  |  |

---

## PLAYER_PENALTY
- 논리명: **선수 징계 관리**
- 카테고리: 
- Primary Key: `PENALTY_SE`
- 컬럼 수: **14**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `PENALTY_SE` | 징계 일련번호 | INT |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `PENALTY_CD` | 징계 코드 | INT |  |  |  |  |
| 6 | `PENALTY_START_DT` | 징계 시작 일자 | DATE |  |  |  |  |
| 7 | `PENALTY_GAME_CN` | 징계 경기 수 | SMALLINT |  |  |  |  |
| 8 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |

---

## COMPETITION_RESULT
- 논리명: **대회 결과**
- 카테고리: 
- Primary Key: `COMP_ID, RESULT_SC`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `COMP_ID` | 대회 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `RESULT_SC` | 결과 구분 | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## ENTRY_REG
- 논리명: **엔트리 입력**
- 카테고리: 
- Primary Key: `LE_ID, SEASON_ID, ENTRY_DT, T_ID, P_ID`
- 컬럼 수: **20**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` | Y |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `ENTRY_DT` | 엔트리 일자 | VARCHAR |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 7 | `BACK_NO` | 등 번호 | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_YN` | 등록 연도 | CHAR |  |  |  |  |
| 10 | `CHANGE_CK` | 교체 확인 | BIT |  | NN |  |  |
| 11 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 40 | `NN` |  |  |  |  |  |  |

---

## ENTRY_REG_ETC
- 논리명: **엔트리 등록 기타사항**
- 카테고리: 
- Primary Key: `LE_ID, SEASON_ID, ENTRY_DT, T_ID, P_ID`
- 컬럼 수: **17**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `ENTRY_DT` | 엔트리 일자 | VARCHAR |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 7 | `GROUP_ID` | 그룹 ID | SMALLINT |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `REG_REASON_CD` | 등록 이유 코드 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## ENTRY_REG_ETC_MASTER
- 논리명: **엔트리 입력 기타사항 마스터**
- 카테고리: 
- Primary Key: `MASTER_SE`
- 컬럼 수: **19**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `START_DT` | 시작 일자 | VARCHAR |  |  |  |  |
| 7 | `END_DT` | 종료 일자 | VARCHAR |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |
| 8 | `GROUP_ID` | 그룹 ID | SMALLINT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_REASON_CD` | 등록 이유 코드 | INT |  |  |  |  |
| 10 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## ENTRY_REG_LOG
- 논리명: **엔트리 입력 로그**
- 카테고리: 
- Primary Key: `ALARM_ID, LE_ID, SEASON_ID, ENTRY_DT, T_ID, P_ID`
- 컬럼 수: **22**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ALARM_ID` | 알람 ID | BIGINT |  |  |  |  |
| 1 | `NN` | Y |  |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `ENTRY_DT` | 엔트리 일자 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 6 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 7 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `BACK_NO` | 등 번호 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 10 | `REG_YN` | 등록 연도 | CHAR |  |  |  |  |
| 11 | `CHANGE_CK` | 교체 확인 | BIT |  | NN |  |  |
| 12 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 40 | `NN` |  |  |  |  |  |  |

---

## ENTRY_REG_MASTER
- 논리명: **엔트리 입력 마스터**
- 카테고리: 
- Primary Key: `LE_ID, SEASON_ID, ENTRY_DT, T_ID`
- 컬럼 수: **18**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | INT |  |  |  |  |
| 2 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `ENTRY_DT` | 엔드리 일자 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 5 | `APPROVE_CK` | 승인 확인 | BIT |  | NN |  |  |
| 6 | `APPROVE_ID_VA` | 승인 ID 값 | VARCHAR |  |  |  |  |
| 7 | `APPROVE_IP_VA` | 승인 IP 값 | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `APPROVE_DT` | 승인 일자 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_ID_VA` | 등록 ID 값 | VARCHAR |  |  |  |  |
| 10 | `REG_IP_VA` | 등록 IP 값 | VARCHAR |  |  |  |  |
| 11 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## ENTRY_REG_MASTER_LOG
- 논리명: **엔트리 입력 마스터 로그**
- 카테고리: 
- Primary Key: `ALARM_ID`
- 컬럼 수: **18**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ALARM_ID` | 알람 ID | BIGINT |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `ENTRY_DT` | 엔트리 일자 | VARCHAR |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 6 | `IP_VA` | IP 값 | VARCHAR |  |  |  |  |
| 7 | `ID_VA` | ID 값 | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` |  |  |  |  |  |  |
| 8 | `ACT_CD` | 활동 코드 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 10 | `NN` |  |  |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## ENTRY_SETUP
- 논리명: **엔트리 인원 관리**
- 카테고리: 
- Primary Key: `S_DT, E_DT, LE_ID`
- 컬럼 수: **16**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `S_DT` | 시작 일자 | VARCHAR |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `E_DT` | 종료 일자 | VARCHAR |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `P_ENTRY_CN` | 일반 엔트리 수 | SMALLINT |  |  |  |  |
| 6 | `DH_P_ENTRY_CN` | 더블헤더 선수 엔트리 수 | SMALLINT |  |  |  |  |
| 7 | `C_ENTRY_CN` | 코치 엔트리 수 | SMALLINT |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `QC_ENTRY_CN` | QC코치 엔트리 수 | SMALLINT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## LINEUP
- 논리명: **실시간 경기 엔트리**
- 카테고리: LIVE
- Primary Key: `LE_ID, SR_ID, G_ID, P_ID, BAT_ORDER_NO, POS_TURN_NO, POS_SC`
- 컬럼 수: **32**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 5 | `BAT_ORDER_NO` | 선수 타순 번호 | TINYINT |  |  |  |  |
| 6 | `POS_TURN_NO` | 선수 포지션 순서 번호 | TINYINT |  |  |  |  |
| 7 | `POS_SC` | 선수 포지션 구분 | CHAR |  |  |  |  |
| 8 | `BAT_TURN_NO` | 선수 타순 순서 번호 | TINYINT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 10 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 11 | `CH_INN_NO` | 교체 시점 이닝 번호 | TINYINT |  |  |  |  |
| 12 | `CH_BAT_AROUND_NO` | 교체 시점 일순 번호 | TINYINT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `CH_BAT_ORDER_NO` | 교체 시점 타자 타순 번호 | TINYINT |  |  |  |  |
| 14 | `CH_PIT_BALL_CN` | 교체 시점 투수의 투구 수 | SMALLINT |  |  |  |  |
| 15 | `PLAY_NO` | 선수 플레이 번호 | TINYINT |  |  |  |  |
| 16 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## IE_GAME_MATRIX_MIX
- 논리명: **실시간 경기 매트릭스 MIX**
- 카테고리: LIVE
- Primary Key: `LE_ID, SR_ID, G_ID, SEQ_NO`
- 컬럼 수: **49**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `SEQ_NO` | 일련 번호 | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `INN_NO` | 이닝 번호 | TINYINT |  |  |  |  |
| 7 | `BAT_AROUND_NO` | 일순 번호 | TINYINT |  |  |  |  |
| 8 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 9 | `BEFORE_OUT_CN` | 이전 아웃카운트 수 | TINYINT |  |  |  |  |
| 10 | `BEFORE_AWAY_SCORE_CN` | 이전 원정 팀 점수 | SMALLINT |  |  |  |  |
| 11 | `BEFORE_HOME_SCORE_CN` | 이전 홈 팀 점수 | SMALLINT |  |  |  |  |
| 12 | `BEFORE_SCORE_GAP_CN` | 이전 점수차 수 | SMALLINT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `BEFORE_RUNNER_SC` | 이전 주자 상황 구분 | TINYINT |  |  |  |  |
| 14 | `AFTER_OUT_CN` | 이후 아웃카운트 수 | TINYINT |  |  |  |  |
| 15 | `AFTER_AWAY_SCORE_CN` | 이후 원정 팀 점수 | SMALLINT |  |  |  |  |
| 16 | `AFTER_HOME_SCORE_CN` | 이후 홈 팀 점수 | SMALLINT |  |  |  |  |
| 17 | `AFTER_SCORE_GAP_CN` | 이후 점수차 수 | SMALLINT |  |  |  |  |
| 18 | `AFTER_RUNNER_SC` | 이후 주자 상황 구분 | TINYINT |  |  |  |  |
| 19 | `BAT_P_ID` | 타자 ID | INT |  |  |  |  |
| 20 | `PIT_P_ID` | 투수 ID | INT |  |  |  |  |
| 21 | `RUN_P_ID` | 주자 ID | INT |  |  |  |  |
| 22 | `HOW_ID` | HOW ID | CHAR |  |  |  |  |
| 23 | `LIVETEXT_IF` | 문자중계 정보 | VARCHAR |  |  |  |  |
| 24 | `BEFORE_WE_RT` | 이전 승리 확 율 | FLOAT |  |  |  |  |
| 25 | `AFTER_WE_RT` | 이후 승리 확 율 | FLOAT |  |  |  |  |
| 26 | `WPA_RT` | 승리 기여도 율 | FLOAT |  |  |  |  |
| 27 | `LI_RT` | 상황 중요도 율 | FLOAT |  |  |  |  |
| 1000 | `NN` |  |  |  |  |  |  |

---

## IE_GAME_LIVETEXT
- 논리명: **실시간 경기 문자중계**
- 카테고리: LIVE
- Primary Key: `LE_ID, SR_ID, G_ID, SEQ_NO`
- 컬럼 수: **27**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 4 | `SEQ_NO` | 일련 번호 | SMALLINT |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `INN_NO` | 이닝 번호 | TINYINT |  |  |  |  |
| 7 | `BAT_AROUND_NO` | 일순 번호 | TINYINT |  |  |  |  |
| 8 | `TB_SC` | 초말 구분 | CHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `LIVETEXT_IF` | 문자중계 정보 | VARCHAR |  |  |  |  |
| 10 | `TEXTSTYLE_SC` | 문자스타일 구분 | TINYINT |  |  |  |  |
| 11 | `BAT_P_ID` | 타자 ID | INT |  |  |  |  |
| 12 | `BAT_ORDER_NO` | 타자 타순 번호 | TINYINT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `PA_PIT_NO` | 타석별 투구 번호 | SMALLINT |  |  |  |  |
| 14 | `PIT_P_ID` | 투수 ID | INT |  |  |  |  |
| 15 | `PIT_RESULT_SC` | 투구 결과 구분 | CHAR |  |  |  |  |
| 16 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 200 | `NN` |  |  |  |  |  |  |

---

## ALARM
- 논리명: **알람**
- 카테고리: 
- Primary Key: `ALARM_ID`
- 컬럼 수: **20**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ALARM_ID` | 알람 ID | BIGINT |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `ALARM_CD` | 알람 코드 | INT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `ALARM_VA` | 알람 값 | VARCHAR |  |  |  |  |
| 6 | `ALARM_DT` | 알람 일자 | DATETIME |  |  |  |  |
| 7 | `REG_ID` | 등록 ID | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `REG_COMPANY_CD` | 등록 회사 코드 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_T_ID` | 등록 팀 ID | CHAR |  |  |  |  |
| 10 | `REG_IP_IF` | 등록 IP 정보 | VARCHAR |  |  |  |  |
| 11 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |
| 100 | `NN` |  |  |  |  |  |  |

---

## ALARM_RCV_USER
- 논리명: **알람 수신 사용자**
- 카테고리: ALARM
- Primary Key: `ALARM_ID, USER_ID`
- 컬럼 수: **15**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ALARM_ID` | 알람 ID | BIGINT |  |  |  |  |
| 2 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 3 | `READ_CK` | 읽기 확인 | BIT |  | NN |  |  |
| 4 | `READ_DT` | 읽기 일자 | DATETIME |  |  |  |  |
| 5 | `DEL_CK` | 삭제 확인 | BIT |  | NN |  |  |
| 6 | `DEL_ID` | 삭제 ID | VARCHAR |  |  |  |  |
| 7 | `DEL_IP_IF` | 삭제 IP 정보 | VARCHAR |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `DEL_DT` | 삭제 일자 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `TEXT_SEND_CK` | 텍스트 전송 확인 | BIT |  | NN |  |  |
| 10 | `TEXT_SEND_SUCC_CK` | 텍스트 전송 성공 확인 | BIT |  | NN |  |  |
| 11 | `TEXT_SEND_DT` | 텍스트 전송 일자 | DATETIME |  |  |  |  |
| 12 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 15 | `NN` | PK |  |  |  |  |  |

---

## FILE_CENTER
- 논리명: **자료실**
- 카테고리: 업무관련
- Primary Key: `FILE_SE`
- 컬럼 수: **13**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `FILE_SE` | 파일 일련번호 | INT |  |  |  |  |
| 2 | `FILE_SC` | 파일 구분 | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `FILE_NM` | 파일 이름 | VARCHAR |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `FILE_LK` | 파일 링크 | VARCHAR |  |  |  |  |
| 5 | `UPLOAD_DT` | 업로드 일자 | DATE |  |  |  |  |
| 6 | `REG_T_ID` | 등록 팀 ID | CHAR |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 100 | `NN` |  |  |  |  |  |  |
| 100 | `NN` |  |  |  |  |  |  |

---

## FILE_CENTER_SECTION
- 논리명: **자료실 구분**
- 카테고리: 업무관련
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 30 | `NN` |  |  |  |  |  |  |

---

## CLUB_REQUEST
- 논리명: **구단 문의**
- 카테고리: 업무관련
- Primary Key: `REQ_SE`
- 컬럼 수: **19**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 문의 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REQ_SC` | 문의 구분 | SMALLINT |  |  |  |  |
| 5 | `REQ_DT` | 문의 일자 | DATETIME |  |  |  |  |
| 6 | `REQ_TT` | 문의 이름(배경) | VARCHAR |  |  |  |  |
| 7 | `REQ_CT` | 문의 내용 | VARCHAR |  |  |  |  |
| 8 | `FILE_NM` | 파일 이름 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `FILE_LK` | 파일 링크 | VARCHAR |  |  |  |  |
| 10 | `REPLY_CT` | 답변 내용 | VARCHAR |  |  |  |  |
| 11 | `REPLY_CK` | 답변 상태 체크 | CHAR |  |  |  |  |
| 12 | `REPLY_DT` | 답변 시간 | DATETIME |  |  |  |  |
| 13 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## CLUB_REQUEST_SECTION
- 논리명: **구단 문의 구분**
- 카테고리: 업무관련
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 30 | `NN` |  |  |  |  |  |  |

---

## GENERAL_REQUEST
- 논리명: **일반 업무 요청**
- 카테고리: 업무관련
- Primary Key: `REQ_SE`
- 컬럼 수: **17**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REQ_T_ID` | 요청 팀 ID | CHAR |  |  |  |  |
| 5 | `ITEM_SC` | 신청 항목 구분 | SMALLINT |  |  |  |  |
| 6 | `REQ_DT` | 요청 일자 | DATE |  |  |  |  |
| 7 | `FILE_NM` | 파일 이름 | VARCHAR |  |  |  |  |
| 8 | `APPROVAL_DT` | 승인 일자 | DATE |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `APPROVAL_CK` | 승인 체크 | BIT |  | NN |  |  |
| 10 | `RETURN_CK` | 반송 확인 | BIT |  | NN |  |  |
| 11 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_ITEM_NOTE
- 논리명: **승인 신청 항목 판독 구분 노트**
- 카테고리: APPROVAL
- Primary Key: `ITEM_SC, NOTE_ID`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ITEM_SC` | 신청 항목 구분 | SMALLINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NOTE_ID` | 노트 ID | TINYINT |  |  |  |  |
| 3 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 50 | `NN` |  |  |  |  |  |  |

---

## APPROVAL_ITEM_SECTION
- 논리명: **승인 신청 항목 판독 구분**
- 카테고리: APPROVAL
- Primary Key: `SC_ID`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `APPROVAL_CS` | 승인 구분 TINTINT |  |  |  |  |  |
| 3 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 4 | `DEL_CK` | 삭제 확인 | BIT |  | NN |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 40 | `NN` |  |  |  |  |  |  |

---

## APPROVAL_MASTER
- 논리명: **승인 마스터**
- 카테고리: APPROVAL
- Primary Key: `APPROVAL_SE`
- 컬럼 수: **20**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `REQ_TABLE_ID` | 요청 테이블 ID | TINYINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID SMALLIINT |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `REQ_T_ID` | 요청 팀 ID | CHAR |  | NN |  |  |
| 6 | `ITEM_SC` | 신청 항목 구분 | SMALLINT |  |  |  |  |
| 7 | `REQ_DT` | 요청 일자 | DATE |  |  |  |  |
| 8 | `FILE_NM` | 파일 이름 | VARCHAR |  |  |  |  |
| 8 | `GETDATE()` |  |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `APPROVAL_CK` | 승인 확인 | BIT |  | NN |  |  |
| 10 | `RETURN_CK` | 반송 확인 | BIT |  | NN |  |  |
| 11 | `UPDATE_DT` | 업데이트 일자 | DATETIME |  |  |  |  |
| 12 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_REQUEST_ETC
- 논리명: **승인 요청 기타 사항**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## APPROVAL_REQUEST_GAME
- 논리명: **승인 요청 경기**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **19**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 5 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 6 | `BF_G_TM` | 변경 전 경기 시간 | VARCHAR |  |  |  |  |
| 7 | `AF_G_TM` | 변경 후 경기 시간 | VARCHAR |  |  |  |  |
| 8 | `BF_S_ID` | 변경 전 구장 ID | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `AF_S_ID` | 변경 후 구장 ID | VARCHAR |  |  |  |  |
| 10 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 11 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 12 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 13 | `NN` |  |  |  |  |  |  |

---

## APPROVAL_REQUEST_OBJECTION
- 논리명: **승인 요청 반대**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **18**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 5 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 6 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 7 | `INN_NO` | 이닝 번호 | TINYINT |  |  |  |  |
| 8 | `BAT_ORDER_NO` | 타자 타순 번호 | TINYINT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `RECORD_CD` | 기록 코드 | TINYINT |  |  |  |  |
| 10 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 11 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 12 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 13 | `NN` |  |  |  |  |  |  |

---

## APPROVAL_REQUEST_PLAYER_CHANGE
- 논리명: **승인 요청 선수 교체**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **25**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `BF_P_NM` | 변경 전 선수 이름 | VARCHAR |  |  |  |  |
| 7 | `AF_P_NM` | 변경 후 선수 이름 | VARCHAR |  |  |  |  |
| 8 | `BF_P_CHN_NM` | 변경 전 선수 한자 이름 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `AF_P_CHN_NM` | 변경 후 선수 한자 이름 | VARCHAR |  |  |  |  |
| 10 | `BF_BACK_NO` | 변경 전 선수 등 번호 | VARCHAR |  |  |  |  |
| 11 | `AF_BACK_NO` | 변경 후 선수 등 번호 | VARCHAR |  |  |  |  |
| 12 | `BF_POS_CD` | 변경 전 선수 포지션 코드 | INT |  |  |  |  |
| 13 | `AF_POS_CD` | 변경 후 선수 포지션 코드 | INT |  |  |  |  |
| 14 | `BF_ACTIVE_CD` | 변경 전 선수 활동 코드 | INT |  |  |  |  |
| 15 | `AF_ACTIVE_CD` | 변경 후 선수 활동 코드 | INT |  |  |  |  |
| 16 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 17 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 18 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_REQUEST_PLAYER_FA_CONTRACT
- 논리명: **승인 요청 FA 선수 계약**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **22**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 7 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 8 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `QUALIFY_YEARS_CN` | 인정 년 수 | TINYINT |  |  |  |  |
| 10 | `QUALIFY_SC` | 인정 구분 | INT |  |  |  |  |
| 11 | `PAYMENT_IF` | 계약금 정보 | VARCHAR |  |  |  |  |
| 12 | `SALARY_IF` | 연봉 정보 | VARCHAR |  |  |  |  |
| 13 | `CONTRACT_DT` | 계약 일자 | DATE |  |  |  |  |
| 14 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 15 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 16 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_REQUEST_PLAYER_FA_INOUT
- 논리명: **승인 요청 선수 FA 트레이드**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **25**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `IN_T_ID` | 양도 팀 ID | CHAR |  |  |  |  |
| 6 | `IN_P_ID` | 양도 선수 ID | INT |  |  |  |  |
| 7 | `IN_P_NM` | 양도 선수 이름 | VARCHAR |  |  |  |  |
| 8 | `IN_POS_CD` | 양도 포지션 구분 | INT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `OUT_T_ID` | 양도 전 팀 ID | CHAR |  |  |  |  |
| 10 | `OUT_P_ID` | 양도 전 선수 ID | INT |  |  |  |  |
| 11 | `INOUT_DT` | 트레이드 일자 | DATE |  |  |  |  |
| 12 | `NOTE_IF` | 노트 정보 VARSCHAR |  |  |  |  |  |
| 13 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 14 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_REQUEST_PLAYER_INOUT
- 논리명: **승인 요청 선수 트레이드**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **29**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 7 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 8 | `INOUT_SC` | 트레이드 구분 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `OUT_T_ID` | 양도 전 팀 ID | CHAR |  |  |  |  |
| 10 | `IN_T_ID` | 양도 팀 ID | CHAR |  |  |  |  |
| 11 | `INOUT_DT` | 트레이드 일자 | DATE |  |  |  |  |
| 12 | `BF_BACK_NO` | 트레이드 이전 등 번호 | VARCHAR |  |  |  |  |
| 13 | `AF_BACK_NO` | 트레이드 이후 등 번호 | VARCHAR |  |  |  |  |
| 14 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 15 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 16 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_REQUEST_PLAYER_NEW
- 논리명: **승인 요청 선수 신규**
- 카테고리: APPROVAL
- Primary Key: `REQ_SE`
- 컬럼 수: **26**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_NM` | 선수 이름 | VARCHAR |  |  |  |  |
| 6 | `P_FULL_NM` | 선수 풀 네임 | VARCHAR |  |  |  |  |
| 7 | `P_ENG_NM` | 선수 영어 이름 | VARCHAR |  |  |  |  |
| 8 | `BIRTH_DT` | 생년월일 일자 | DATE |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `BACK_NO` | 등 번호 | VARCHAR |  |  |  |  |
| 10 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 11 | `PIT_DIREC_CD` | 투구 방향 코드 | INT |  |  |  |  |
| 12 | `PIT_FORM_CD` | 투구 폼 코드 | INT |  |  |  |  |
| 13 | `HIT_DIREC_CD` | 타격 방향 코드 | INT |  |  |  |  |
| 14 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 15 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 16 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 40 | `NN` |  |  |  |  |  |  |

---

## APPROVAL_REQUEST_PLAYER_REG
- 논리명: **승인 요청 선수 등록**
- 카테고리: 
- Primary Key: `REQ_SE`
- 컬럼 수: **22**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 6 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 7 | `BIRTH_DT` | 생년월일 일자 | DATE |  |  |  |  |
| 8 | `POS_CD` | 포지션 코드 | INT |  |  |  |  |
| 8 | `GETDATE()` |  |  |  |  |  |  |
| 9 | `START_DT` | 시작 일자 | DATE |  |  |  |  |
| 10 | `PERIOD_CN` | 기간 수 | INT |  |  |  |  |
| 11 | `APPLICANT_NM` | 응모자 이름 | VARCHAR |  |  |  |  |
| 12 | `NOTE_IF` | 노트 정보 | VARCHAR |  |  |  |  |
| 13 | `ORDER_NO` | 순서 번호 | TINYINT |  |  |  |  |
| 14 | `PLAYER_REQ_DT` | 선수 요청 일자 | DATETIME |  |  |  |  |
| 15 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## APPROVAL_REQUEST_TABLE_LIST
- 논리명: **승인 요청 테이블 목록**
- 카테고리: 
- Primary Key: `TABLE_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `TABLE_ID` | 테이블 ID | TINYINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `TABLE_NM` | 테이블 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 40 | `NN` |  |  |  |  |  |  |

---

## APPROVAL_REQUEST_TEAM_REGISTER
- 논리명: **승인 요청 팀 등록**
- 카테고리: 
- Primary Key: `REQ_SE`
- 컬럼 수: **13**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `REQ_SE` | 요청 일련번호 | INT |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 5 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 6 | `RECORD_DT` | 기록 일자 | DATE |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## APPROVAL_SECTION
- 논리명: **승인 구분**
- 카테고리: 
- Primary Key: `SC_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | TINYINT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## MONITORING_COVID_BASIC
- 논리명: **코로나 19 주요 점검 사항**
- 카테고리: MONITORING
- Primary Key: `COVID_SE, QUESTION_SC, QUESTION_NO`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `COVID_SE` | 코로나 19 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `QUESTION_SC` | 질문 구분 | CHAR |  |  |  |  |
| 3 | `QUESTION_NO` | 질문 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `ANSWER_YN` | 답변 여부 | CHAR |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_COVID_MASTER
- 논리명: **코로나 19 주요사항 마스터**
- 카테고리: MONITORING
- Primary Key: `MASTER_SE, COVID_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `COVID_SE` | 코로나 19 일련번호 | INT |  |  |  |  |
| 3 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 5 | `USER_ID` | 제춛자 ID | VARCHAR |  |  |  |  |
| 6 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_COVID_SPECIAL
- 논리명: **코로나 19 주요 특이 사항**
- 카테고리: MONITORING
- Primary Key: `COVID_SE`
- 컬럼 수: **5**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `COVID_SE` | 코로나 19 일련번호 | INT |  |  |  |  |
| 2 | `SPECIAL_CT` | 특이사항 내용 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_DISPUTE_REPORT
- 논리명: **분쟁 및 사고 보고서**
- 카테고리: MONITORING
- Primary Key: `MASTER_SE, DISPUTE_SE`
- 컬럼 수: **12**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `DISPUTE_SE` | 분쟁 일련번호 | INT |  |  |  |  |
| 3 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 5 | `USER_ID` | 제출자 ID | VARCHAR |  |  |  |  |
| 6 | `REPORT_CT` | 보고서 내용 | VARCHAR |  |  |  |  |
| 7 | `ADD_CT` | 추가의견 내용 | VARCHAR |  |  |  |  |
| 8 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## MONITORING_EVALUATION_BASIC
- 논리명: **행동강령 평가표 일반**
- 카테고리: MONITORING
- Primary Key: `EVALUATION_SE, QUESTION_SC, QUESTION_NO`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `EVALUATION_SE` | 행동강령 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `QUESTION_SC` | 평가표 구분 | CHAR |  |  |  |  |
| 3 | `QUESTION_NO` | 질문 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `POINT_VA` | 점수 값 | SMALLINT |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_EVALUATION_CONTENT
- 논리명: **행동강령 평가표 내용**
- 카테고리: MONITORING
- Primary Key: `EVALUATION_SE`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `EVALUATION_SE` | 행동강령 일련번호 | INT |  |  |  |  |
| 2 | `VAR_CT` | 비디오 판독결과 내용 | VARCHAR |  |  |  |  |
| 3 | `OPINION_CT` | 이원장 또는 팀장 의견 내용 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_EVALUATION_MASTER
- 논리명: **행동강령 평가표 마스터**
- 카테고리: MONITORING
- Primary Key: `EVALUATION_SE`
- 컬럼 수: **18**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `EVALUATION_SE` | 행동강령 일련번호 | INT |  |  |  |  |
| 1 | `NN` |  |  |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `EVALUATION_SC` | 평가표 구분 | CHAR |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `MONTH` | 월 | SMALLINT |  |  |  |  |
| 6 | `UMP_P_ID` | 피평가자 ID | INT |  |  |  |  |
| 7 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 8 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `USER_ID` | 제출자(평가자) ID | VARCHAR |  |  |  |  |
| 10 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 11 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## MONITORING_EVALUATION_ROUNDUP
- 논리명: **행동강령 평가표 모음**
- 카테고리: MONITORING
- Primary Key: `EVALUATION_SE`
- 컬럼 수: **16**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `EVALUATION_SE` | 행동강령 일련번호 | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 4 | `MONTH` | 월 | SMALLINT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `UMP_P_ID` | 피평가자 ID | INT |  |  |  |  |
| 6 | `USER_ID` | 제출자(평가자) ID | VARCHAR |  |  |  |  |
| 7 | `MANAGE_SCORE` | 경기 운영 점수 | FLOAT |  |  |  |  |
| 8 | `RULE_SCORE` | 규칙, 규정 점수 | FLOAT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |

---

## MONITORING_GAME_BASIC
- 논리명: **경기 영상 모니터링 기본**
- 카테고리: MONITORING
- Primary Key: `GAME_SE, TYPE_SC, QUESTION_NO`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `GAME_SE` | 경기 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `TYPE_SC` | 선수 구분 | CHAR |  |  |  |  |
| 3 | `QUESTION_NO` | 질문 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `ANSWER_YN` | 질문 답변 | CHAR |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_GAME_DETAIL
- 논리명: **경기 영상 세부 모니터링 사항**
- 카테고리: MONITORING
- Primary Key: `INN_NO, TB_SC, GAME_SE`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `GAME_SE` | 경기 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `INN_NO` | 이닝 번호 | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `TB_SC` | 초/말 구분 | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `DETAIL_CT` | 상세 내용 | VARCHAR |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_GAME_MASTER
- 논리명: **경기 영상 모니터링 마스터**
- 카테고리: MONITORING
- Primary Key: `GAME_SE, MASTER_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `GAME_SE` | 경기 일련번호 | INT |  |  |  |  |
| 3 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 5 | `USER_ID` | 제출자 ID | VARCHAR |  |  |  |  |
| 6 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_ILLEGAL_CHECKLIST
- 논리명: **부정행위방지 모니터링 체크리스트**
- 카테고리: MONITORING
- Primary Key: `ILLEGAL_SE, ILLEGAL_SC, QUESTION_NO`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ILLEGAL_SE` | 부정행위 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `ILLEGAL_SC` | 부정행위 구분 | CHAR |  |  |  |  |
| 3 | `QUESTION_NO` | 질문 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `ANSWER_YN` | 답변 | CHAR |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_ILLEGAL_CONTENT
- 논리명: **부정행위 모니터링 내용 및 조치사항**
- 카테고리: MONITORING
- Primary Key: `ILLEGAL_SE, CONTENT_SE`
- 컬럼 수: **13**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ILLEGAL_SE` | 부정행위 일련번호 | INT |  |  |  |  |
| 2 | `CONTENT_SE` | 내용 일련번호 | INT |  |  |  |  |
| 3 | `WORK_CT` | 업무 내용 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `PERSONAL_IF` | 적발자 인적사항 정보 | VARCHAR |  |  |  |  |
| 5 | `DATE_IF` | 적발 일시 정보 | VARCHAR |  |  |  |  |
| 6 | `PLACE_IF` | 적발 장소 정보 | VARCHAR |  |  |  |  |
| 7 | `CONTENT_IF` | 적발 내용 정보 | VARCHAR |  |  |  |  |
| 8 | `PHONE_IF` | 연락처 정보 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `ACTION_IF` | 기타 조치 사항 정보 | VARCHAR |  |  |  |  |
| 10 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## MONITORING_ILLEGAL_FILE
- 논리명: **부정행위방지 모니터링 첨부파일**
- 카테고리: MONITORING
- Primary Key: `CONTENT_SE, FILE_NO`
- 컬럼 수: **7**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `CONTENT_SE` | 내용 일련번호 | INT |  |  |  |  |
| 2 | `FILE_NO` | 첨부파일 번호 | INT |  |  |  |  |
| 3 | `FILE_LK` | 첨부파일 경로 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_ILLEGAL_MASTER
- 논리명: **부정행위방지 모니터링 마스터**
- 카테고리: MONITORING
- Primary Key: `MASTER_SE, ILLEGAL_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `ILLEGAL_SE` | 부정행위 일련번호 | INT |  |  |  |  |
| 3 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 5 | `USER_ID` | 제출자 ID | VARCHAR |  |  |  |  |
| 6 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_MASTER
- 논리명: **경기 모니터링 평가 마스터**
- 카테고리: MONITORING
- Primary Key: `MASTER_SE, LE_ID, SR_ID, G_ID`
- 컬럼 수: **25**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `LE_ID` | 리그 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `SR_ID` | 시리즈 ID | SMALLINT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `G_ID` | 경기 ID | CHAR |  |  |  |  |
| 5 | `SEASON_ID` | 시즌 ID | SMALLINT |  |  |  |  |
| 6 | `GAME_CK` | 경기영상, 경기 모니터링 확인 | BIT |  |  |  |  |
| 7 | `OPERATION_CK` | 운영위원, 심판육성위원 모니터링 확인 | BIT |  |  |  |  |
| 8 | `COVID_CK` | 코로나 19 확인 | BIT |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `DISPUTE_CK` | 분쟁 및 사고 확인 | BIT |  |  |  |  |
| 10 | `SPEED_CK` | 경기 스피드업 확인 | BIT |  |  |  |  |
| 11 | `ILLEGAL_CK` | 부정행위방지 모니터링 확인 | BIT |  |  |  |  |
| 12 | `EVALUATION_A_CK` | 행동강령 평가표1(심판위원장) 확인 | BIT |  |  |  |  |
| 13 | `NN` | PK |  |  |  |  |  |
| 13 | `EVALUATION_B_CK` | 행동강령 평가표2(심판위원장) 확인 | BIT |  |  |  |  |
| 14 | `EVALUATION_C_CK` | 행동강령 평가표(심판팀장용) 확인 | BIT |  |  |  |  |
| 15 | `UMPIRE_A_CK` | 심판위원보고서(심판위원장) 확인 | BIT |  |  |  |  |
| 16 | `UMPIRE_B_CK` | 심판위원보고서(심판팀장) 확인 | BIT |  |  |  |  |
| 17 | `UMPIRE_C_CK` | 심판위원보고서(퓨처스심판육성위원)확인 | BIT |  |  |  |  |
| 18 | `EDUCATION_CK` | 심판위원 교육 현황(퓨처스전용) 확인 | BIT |  |  |  |  |
| 19 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## MONITORING_OPERATION_GAME
- 논리명: **경기 모니터링 사항**
- 카테고리: MONITORING
- Primary Key: `OPERATION_SE, QUESTION_SC, QUESTION_NO`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OPERATION_SE` | 질문 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `QUESTION_SC` | 질문 구분 | CHAR |  |  |  |  |
| 3 | `QUESTION_NO` | 질문 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `ANSWER_YN` | 답변 | CHAR |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_OPERATION_MASTER
- 논리명: **경기 모니터링 마스터**
- 카테고리: MONITORING
- Primary Key: `OPERATION_SE, MASTER_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `OPERATION_SE` | 위원 일련번호 | INT |  |  |  |  |
| 3 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 5 | `USER_ID` | 제출자 ID | VARCHAR |  |  |  |  |
| 6 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_OPERATION_SPECIAL
- 논리명: **경기 모니터링 특이 사항**
- 카테고리: MONITORING
- Primary Key: `OPERATION_SE`
- 컬럼 수: **5**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OPERATION_SE` | 위원 일련번호 | INT |  |  |  |  |
| 2 | `SPECIAL_CT` | 특이사항 내용 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_OPERATION_UMPIRE
- 논리명: **운영, 심판육성위원 모니터링 심판평가**
- 카테고리: MONITORING
- Primary Key: `OPERATION_SE, UMPIRE_POS_CD, UMPIRE_EVALUATION_CD`
- 컬럼 수: **12**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OPERATION_SE` | 위원 일련번호 | INT |  |  |  |  |
| 2 | `UMPIRE_POS_CD` | 심판 위치 코드 | INT |  |  |  |  |
| 3 | `UMPIRE_EVALUATION_CD` | 심판 구분 코드 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `EVALUATION_NO` | 평가 번호 | INT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `P_ID` | 심판 ID | INT |  |  |  |  |
| 6 | `POINT_VA` | 점수 값 | SMALLINT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_SPEED_BASIC
- 논리명: **경기 스피드업 위반**
- 카테고리: MONITORING
- Primary Key: `SPEED_SE, VIOLATION_SC, VIOLATION_NO, T_ID`
- 컬럼 수: **14**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SPEED_SE` | 스피드업 일련번호 | INT |  |  |  |  |
| 2 | `VIOLATION_SC` | 위반 구분 | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `VIOLATION_NO` | 위반 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 5 | `INN_NO` | 이닝 번호 | SMALLINT |  |  |  |  |
| 6 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 7 | `VIOLATION_TM` | 위반 시간 | TIME |  |  |  |  |
| 8 | `VIOLATION_CT` | 위반 사유 내용 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## MONITORING_SPEED_MASTER
- 논리명: **경기 스피드업 위반 마스터**
- 카테고리: MONITORING
- Primary Key: `MASTER_SE, SPEED_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 2 | `SPEED_SE` | 스피드업 일련번호 | INT |  |  |  |  |
| 3 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 5 | `USER_ID` | 제출자 ID | VARCHAR |  |  |  |  |
| 6 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 7 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_SPEED_UNIFORM
- 논리명: **경기 스피드업 위반 유니폼**
- 카테고리: MONITORING
- Primary Key: `SPEED_SE, VIOLATION_SC, VIOLATION_NO, T_ID`
- 컬럼 수: **11**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SPEED_SE` | 스피드업 일련번호 | INT |  |  |  |  |
| 2 | `VIOLATION_SC` | 위반 구분 | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 3 | `VIOLATION_NO` | 위반 번호 | INT |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 5 | `P_ID` | 선수 ID | INT |  |  |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## MONITORING_UMPIRE_REPORT
- 논리명: **심판 위원 보고서**
- 카테고리: MONITORING
- Primary Key: `MASTER_SE, UMPIRE_SE, UMPIRE_SC`
- 컬럼 수: **15**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `MASTER_SE` | 마스터 일련번호 | INT |  |  |  |  |
| 1 | `NN` | PK |  |  |  |  |  |
| 2 | `UMPIRE_SE` | 심판위원 일련번호 | INT |  |  |  |  |
| 3 | `UMPIRE_SC` | 심판위원 구분 | CHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `SUBMIT_CK` | 제출 확인 | BIT |  |  |  |  |
| 5 | `TEMP_CK` | 임시저장 확인 | BIT |  |  |  |  |
| 6 | `UMP_P_ID` | 보고자 ID | INT |  |  |  |  |
| 7 | `USER_ID` | 등록 ID | VARCHAR |  |  |  |  |
| 8 | `REPORT_CT` | 보고서 내용 | VARCHAR |  |  |  |  |
| 8 | `N` | GETDATE() |  |  |  |  |  |
| 9 | `ADD_CT` | 추가의견 내용 | VARCHAR |  |  |  |  |
| 10 | `DEL_CK` | 삭제 확인 | BIT |  |  |  |  |
| 11 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |

---

## OFFICIAL_ADDRESS_GROUP
- 논리명: **주소록 관리**
- 카테고리: OFFICAL
- Primary Key: `GROUP_SE`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `GROUP_SE` | 그룹 일련번호 | INT |  |  |  |  |
| 2 | `GROUP_NM` | 그룹 이름 | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 30 | `NN` |  |  |  |  |  |  |

---

## OFFICIAL_ADDRESS_USER
- 논리명: **주소록 사용자**
- 카테고리: OFFICAL
- Primary Key: `GROUP_SE, USER_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `GROUP_SE` | 그룹 일련번호 | INT |  |  |  |  |
| 2 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |

---

## OFFICIAL_ALARM
- 논리명: **승인 공시업무 알람**
- 카테고리: OFFICAL
- Primary Key: `OFFICIAL_SE, ALARM_ID`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OFFICIAL_SE` | 승인 공시업무 일련번호 | INT |  |  |  |  |
| 2 | `ALARM_ID` | 알람 ID | BIGINT |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## OFFICIAL_APPROVAL_GROUP
- 논리명: **승인 공시업무 그룹 관리**
- 카테고리: OFFICAL
- Primary Key: `OFFICIAL_SE, APPROVAL_SE`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OFFICIAL_SE` | 승인 공시 업무 일련번호 | INT |  |  |  |  |
| 2 | `APPROVAL_SE` | 승인 일련번호 | INT |  |  |  |  |
| 3 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## OFFICIAL_ITEM_TEXT
- 논리명: **텍스트 기존 값 관리**
- 카테고리: OFFICAL
- Primary Key: `ITEM_SC`
- 컬럼 수: **6**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `ITEM_SC` | 신청 항목 구분 | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `OFFICIAL_TT` | 승인 공시업무 제목 | VARCHAR |  |  |  |  |
| 3 | `OFFICIAL_CT` | 승인 공시업무 내용 | VARCHAR |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## OFFICIAL_MASTER
- 논리명: **승인 공시업무 마스터**
- 카테고리: OFFICAL
- Primary Key: `OFFICIAL_SE`
- 컬럼 수: **9**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OFFICIAL_SE` | 승인 공시업무 일련번호 | INT |  |  |  |  |
| 2 | `OFFICIAL_TT` | 승인 공시업무 제목 | VARCHAR |  |  |  |  |
| 3 | `OFFICIAL_CT` | 승인 공시업무 내용 | VARCHAR |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `SIGN_CT` | 서명 내용 | VARCHAR |  |  |  |  |
| 5 | `OFFICIAL_DT` | 승인 공시업무 일자 | DATE |  |  |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |

---

## OFFICIAL_RCV_USER
- 논리명: **승인 공시업무 수신 사용자**
- 카테고리: OFFICAL
- Primary Key: `OFFICIAL_SE, RCV_SC, USER_ID`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `OFFICIAL_SE` | 승인 공시업무 일련번호 | INT |  |  |  |  |
| 2 | `RCV_SC` | 수신 구분 | INT |  |  |  |  |
| 3 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 15 | `NN` | PK |  |  |  |  |  |

---

## OFFICIAL_SIGNATURE
- 논리명: **서명 관리**
- 카테고리: OFFICAL
- Primary Key: `SIGN_SE`
- 컬럼 수: **11**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SIGN_SE` | 서명 일련번호 | INT |  |  |  |  |
| 2 | `DEPARTMENT_IF` | 회사 정보 | VARCHAR |  |  |  |  |
| 3 | `POSITION_IF` | 직책 정보 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `SIGNER_NM` | 서명 이름 | VARCHAR |  |  |  |  |
| 5 | `SIGN1_CT` | 서명1 내용 | VARCHAR |  |  |  |  |
| 6 | `SIGN2_CT` | 서명2 내용 | VARCHAR |  |  |  |  |
| 7 | `SIGN3_CT` | 서명3 내용 | VARCHAR |  |  |  |  |
| 8 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 10 | `NN` |  |  |  |  |  |  |

---

## USER
- 논리명: **사용자 정보**
- 카테고리: 
- Primary Key: `USER_ID`
- 컬럼 수: **19**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 2 | `AUTH_CD` | 인증 코드 | INT |  |  |  |  |
| 3 | `EVALUATION_CD` | 평가 코드 | INT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 4 | `COMPANY_CD` | 회사 코드 | INT |  |  |  |  |
| 4 | `NN` |  |  |  |  |  |  |
| 5 | `T_ID` | 팀 ID | CHAR |  |  |  |  |
| 6 | `USER_PW` | 사용자 비밀번호 | VARCHAR |  |  |  |  |
| 7 | `USER_NM` | 사용자 이름 | VARCHAR |  |  |  |  |
| 8 | `EMAIL_VA` | 이메일 값 | VARCHAR |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 9 | `PHONE_VA` | 전화번호 값 | VARCHAR |  |  |  |  |
| 10 | `HAND_PHONE_VA` | 핸드폰 값 | VARCHAR |  |  |  |  |
| 11 | `DEL_CK` | 삭제 확인 | BIT |  | NN |  |  |
| 12 | `UPDATE_DT` | 업데이트 일자 | DATETIME |  |  |  |  |
| 13 | `DEL_DT` | 삭제 일자 | DATETIME |  |  |  |  |
| 14 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 15 | `NN` | PK |  |  |  |  |  |
| 256 | `NN` |  |  |  |  |  |  |

---

## USER_ALARM_CK
- 논리명: **사용자 알람 체크**
- 카테고리: 
- Primary Key: `USER_ID, ALARM_CD`
- 컬럼 수: **7**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 2 | `ALARM_CD` | 알람 코드 | INT |  |  |  |  |
| 3 | `RCV_CK` | 수신 확인 | BIT |  | NN |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 15 | `NN` | PK |  |  |  |  |  |

---

## USER_BLOCK_LOG
- 논리명: **사용자 차단 로그**
- 카테고리: 
- Primary Key: `LOG_SE`
- 컬럼 수: **11**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LOG_SE` | 로그 일련번호 | INT |  |  |  |  |
| 2 | `LOG_DT` | 로그 일자 | DATE |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `IP_IF` | IP 정보 | VARCHAR |  |  |  |  |
| 4 | `NN` | PK |  |  |  |  |  |
| 4 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 5 | `UNBLOCK_CK` | 차단해제 확인 | BIT |  | NN |  |  |
| 6 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |

---

## USER_LOG_SECTION
- 논리명: **사용자 로그 구분**
- 카테고리: 
- Primary Key: `SC_ID`
- 컬럼 수: **8**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 2 | `NN` | PK |  |  |  |  |  |
| 2 | `SC_NM` | 구분 이름 | VARCHAR |  |  |  |  |
| 3 | `GROUP_SC` | 그룹 구분 | VARCHAR |  |  |  |  |
| 4 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |
| 20 | `NN` |  |  |  |  |  |  |

---

## USER_LOGIN_LOG
- 논리명: **사용자 로그인 로그**
- 카테고리: 
- Primary Key: `LOG_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LOG_SE` | 로그 일련번호 | BIGINT |  |  |  |  |
| 2 | `LOG_DT` | 로그 일자 | DATE |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `USER_ID` | 사용자 ID | VARCHAR |  |  |  |  |
| 4 | `ACCESS_SC` | 접근 구분 | VARCHAR |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 10 | `NN` |  |  |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |

---

## USER_LOGIN_TRY_LOG
- 논리명: **사용자 로그인 시도 로그**
- 카테고리: 
- Primary Key: `LOG_SE`
- 컬럼 수: **10**

| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |
|---|--------|--------|-----------|------|------|----|--------|
| 1 | `LOG_SE` | 로그 일련번호 | BIGINT |  |  |  |  |
| 2 | `LOG_DT` | 로그 일자 | DATE |  |  |  |  |
| 2 | `NN` |  |  |  |  |  |  |
| 3 | `NN` |  |  |  |  |  |  |
| 3 | `IP_IF` | IP 정보 | VARCHAR |  |  |  |  |
| 4 | `SC_ID` | 구분 ID | SMALLINT |  |  |  |  |
| 5 | `REG_DT` | 입력 시간 | DATETIME |  |  |  |  |
| 8 | `NN` | PK |  |  |  |  |  |
| 8 | `NN` | GETDATE() |  |  |  |  |  |
| 15 | `NN` |  |  |  |  |  |  |

---
