# 컬럼 매핑 매트릭스 (AS-IS → TO-BE)

> 최종수정: 2026-02-25 | 자동 생성: scripts/extract-mapping.py
> 📋 문서 성격: 컬럼 매핑 매트릭스 (As-Is → To-Be)

본 문서는 현행 시스템(AS-IS)의 컬럼을 신규 시스템(TO-BE) 표준으로 매핑한 전수 목록이다.
수행사 마이그레이션 핸드오프 문서로 활용한다.

→ 참고: [도메인 사전](../standards-dict/domains.md) - 표준 타입 상세
→ 참고: [ID 체계](../standards/id-system.md) - 식별자 형식

## 요약

| 항목 | 수치 |
|------|------|
| 총 테이블 | 39 |
| 총 컬럼 | 787 |
| 이름 변경 | 577 |
| 타입 변환 필요 | 210 |
| 직접 매핑 | 0 |

---

## 1. 경기 기록 (game/)

### GAMEINFO → GAME_INFO

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(15) | game_id | char(13) | 길이 변경 (char(15)→char(13)) | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | DBHD | char(10) | doubleheader_no | int | 이름 변경 |  |
| 4 | STADIUM | nvarchar(40) | stadium_nm | nvarchar(100) | 길이 변경 |  |
| 5 | VTEAM | nvarchar(4) | away_team_cd | varchar(10) | 이름 변경 |  |
| 6 | HTEAM | nvarchar(4) | home_team_cd | varchar(10) | 이름 변경 |  |
| 7 | STTM | char(4) | start_tm | char(4) | 이름 변경 |  |
| 8 | ENTM | nvarchar(8) | end_tm | char(4) | 이름 변경 |  |
| 9 | DLTM | nvarchar(8) | delay_tm | char(4) | 이름 변경 |  |
| 10 | GMTM | nvarchar(8) | game_duration_tm | char(4) | 이름 변경 |  |
| 11 | STAD | nvarchar(16) | stadium_cd | varchar(10) | 이름 변경 |  |
| 12 | UMPC | nvarchar(16) | umpire_chief_nm | nvarchar(100) | 길이 변경 |  |
| 13 | UMP1 | nvarchar(16) | umpire_1b_nm | nvarchar(100) | 길이 변경 |  |
| 14 | UMP2 | nvarchar(16) | umpire_2b_nm | nvarchar(100) | 길이 변경 |  |
| 15 | UMP3 | nvarchar(16) | umpire_3b_nm | nvarchar(100) | 길이 변경 |  |
| 16 | UMPL | nvarchar(16) | umpire_lf_nm | nvarchar(100) | 길이 변경 |  |
| 17 | UMPR | nvarchar(16) | umpire_rf_nm | nvarchar(100) | 길이 변경 |  |
| 18 | SCOA | nvarchar(16) | scorer_a_nm | nvarchar(100) | 길이 변경 |  |
| 19 | SCOB | nvarchar(16) | scorer_b_nm | nvarchar(100) | 길이 변경 |  |
| 20 | TEMP | nvarchar(6) | temperature_va | int | 이름 변경 |  |
| 21 | MOIS | nvarchar(6) | humidity_va | int | 이름 변경 |  |
| 22 | WEATH | nvarchar(4) | weather_cd | varchar(10) | 이름 변경 |  |
| 23 | WIND | nvarchar(6) | wind_dir_cd | varchar(10) | 이름 변경 |  |
| 24 | WINS | nvarchar(10) | wind_speed_va | int | 이름 변경 |  |
| 25 | GWEEK | varchar(12) | game_week_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 26 | CROWD | int | crowd_cn | int | 이름 변경 |  |
| 27 | CHAJUN | char(10) | round_no | int | 이름 변경 |  |

### GAMEINFO_WEATHER → GAME_INFO_WEATHER

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | code | varchar(10) | code_cd | varchar(10) | 이름 변경 | PK |
| 2 | area_wide | nvarchar(10) | area_wide_nm | nvarchar(100) | 길이 변경 |  |
| 3 | area_city | nvarchar(10) | area_city_nm | nvarchar(100) | 길이 변경 |  |
| 4 | area_dong | nvarchar(10) | area_dong_nm | nvarchar(100) | 길이 변경 |  |
| 5 | tm | varchar(10) | team_cd | varchar(10) | 이름 변경 | PK |
| 6 | icon40 | nvarchar(10) | icon_40_cd | varchar(10) | 이름 변경 |  |
| 7 | temp | nvarchar(10) | temperature_va | int | 이름 변경 |  |
| 8 | humi | nvarchar(10) | humidity_va | int | 이름 변경 |  |
| 9 | rain | nvarchar(10) | rain_if | bit | 이름 변경 |  |
| 10 | snow | nvarchar(10) | snow_if | bit | 이름 변경 |  |
| 11 | wdirk | nvarchar(10) | wind_dir_cd | varchar(10) | 이름 변경 |  |
| 12 | wspeed | nvarchar(10) | wind_speed_va | int | 이름 변경 |  |

### GAMECONTAPP → GAME_CONT_APP

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | GDAY | char(8) | game_dt | char(8) | 이름 변경 |  |
| 4 | SERNO | smallint | seq_no | int | 타입 확장 (smallint→int) | PK |
| 5 | TURN | char(2) | turn_no | int | 이름 변경 |  |
| 6 | INN | tinyint | ip | tinyint | 이름 변경 |  |
| 7 | TB | char(1) | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 8 | INN2 | char(1) | inn_2_score | char(1) | 이름 변경 |  |
| 9 | OCOUNT | char(1) | opp_count | char(1) | 이름 변경 |  |
| 10 | BCOUNT | varchar(30) | ball_count_cd | varchar(10) | 길이 변경 |  |
| 11 | RTURN | char(2) | real_turn_no | int | 이름 변경 |  |
| 12 | HOW | char(2) | how_cd | varchar(10) | 이름 변경 |  |
| 13 | FIELD | varchar(25) | field_cd | varchar(10) | 길이 변경 |  |
| 14 | PLACE | char(1) | place_cd | varchar(10) | 이름 변경 |  |
| 15 | HITTER | varchar(10) | hitter_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 16 | HITNAME | varchar(20) | hitter_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 17 | PITNAME | varchar(20) | pitcher_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 18 | PITCHER | varchar(10) | pitcher_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 19 | CATNAME | varchar(20) | catcher_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 20 | CATCHER | varchar(10) | catcher_id | varchar(10) | 이름 변경 |  |
| 21 | BCNT | char(3) | ball_count_cd | varchar(10) | 이름 변경 |  |
| 22 | TSCORE | smallint | total_score | smallint | 이름 변경 |  |
| 23 | BSCORE | smallint | bat_score | smallint | 이름 변경 |  |
| 24 | BASE1B | char(2) | base_1b_before_id | char(2) | 이름 변경 |  |
| 25 | BASE2B | char(2) | base_2b_before_id | char(2) | 이름 변경 |  |
| 26 | BASE3B | char(2) | base_3b_before_id | char(2) | 이름 변경 |  |
| 27 | BASE1A | char(2) | base_1b_after_id | char(2) | 이름 변경 |  |
| 28 | BASE2A | char(2) | base_2b_after_id | char(2) | 이름 변경 |  |
| 29 | BASE3A | char(2) | base_3b_after_id | char(2) | 이름 변경 |  |

### ENTRY → ENTRY

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | TURN | char(2) | turn_no | int | 이름 변경 | PK |
| 4 | NAME | varchar(15) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 5 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 6 | TEAM | char(1) | team_cd | varchar(10) | 이름 변경 |  |
| 7 | POSI | char(2) | position_cd | varchar(10) | 이름 변경 | PK |
| 8 | CHIN | varchar(2) | change_inning_no | int | 타입 변환 (varchar→int) |  |
| 9 | CHTURN | char(1) | change_turn_no | int | 이름 변경 |  |
| 10 | CHBCNT | varchar(2) | change_ball_count_cd | varchar(10) | 길이 변경 |  |
| 11 | CHIN2 | char(1) | change_inning2_no | int | 이름 변경 |  |

### Hitter → HITTER

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | TB | char(1) | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 4 | NAME | nvarchar(15) | player_nm | nvarchar(100) | 길이 변경 |  |
| 5 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 6 | TURN | char(2) | turn_no | int | 이름 변경 |  |
| 7 | ONETURN | char(1) | one_turn_if | bit | 타입 변환 (char→bit) |  |
| 8 | PA | int | pa | int | 이름 변경 |  |
| 9 | AB | int | ab | int | 이름 변경 |  |
| 10 | RBI | int | rbi | int | 이름 변경 |  |
| 11 | RUN | int | run | int | 이름 변경 |  |
| 12 | HIT | int | hit | int | 이름 변경 |  |
| 13 | H2 | int | h2b | int | 이름 변경 |  |
| 14 | H3 | int | h3b | int | 이름 변경 |  |
| 15 | HR | int | hr | int | 이름 변경 |  |
| 16 | SB | int | sb | int | 이름 변경 |  |
| 17 | CS | int | cs | int | 이름 변경 |  |
| 18 | SH | int | sh | int | 이름 변경 |  |
| 19 | SF | int | sf | int | 이름 변경 |  |
| 20 | BB | int | bb | int | 이름 변경 |  |
| 21 | IB | int | ibb | int | 이름 변경 |  |
| 22 | HP | int | hbp | int | 이름 변경 |  |
| 23 | KK | int | so | int | 이름 변경 |  |
| 24 | GD | int | gidp | int | 이름 변경 |  |
| 25 | ERR | int | err | int | 이름 변경 |  |
| 26 | LOB | int | lob | int | 이름 변경 |  |

### Pitcher → PITCHER

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | TB | char(1) | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 4 | NAME | varchar(20) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 5 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 6 | POS | varchar(10) | position_cd | varchar(10) | 이름 변경 |  |
| 7 | START | char(1) | start_if | bit | 타입 변환 (char→bit) |  |
| 8 | QUIT | char(1) | quit | char(1) | 이름 변경 |  |
| 9 | CG | int | cg | int | 이름 변경 |  |
| 10 | SHO | int | sho | int | 이름 변경 |  |
| 11 | WLS | char(1) | wls_cd | varchar(10) | 이름 변경 |  |
| 12 | HOLD | smallint | hld | smallint | 이름 변경 |  |
| 13 | INN | varchar(10) | ip | varchar(10) | 이름 변경 |  |
| 14 | INN2 | int | inn_2_score | int | 이름 변경 |  |
| 15 | BF | int | bf | int | 이름 변경 |  |
| 16 | PA | int | pa | int | 이름 변경 |  |
| 17 | AB | int | ab | int | 이름 변경 |  |
| 18 | HIT | int | hit | int | 이름 변경 |  |
| 19 | H2 | int | h2b | int | 이름 변경 |  |
| 20 | H3 | int | h3b | int | 이름 변경 |  |
| 21 | HR | int | hr | int | 이름 변경 |  |
| 22 | SB | int | sb | int | 이름 변경 |  |
| 23 | CS | int | cs | int | 이름 변경 |  |
| 24 | SH | int | sh | int | 이름 변경 |  |
| 25 | SF | int | sf | int | 이름 변경 |  |
| 26 | BB | int | bb | int | 이름 변경 |  |
| 27 | IB | int | ibb | int | 이름 변경 |  |
| 28 | HP | int | hbp | int | 이름 변경 |  |
| 29 | KK | int | so | int | 이름 변경 |  |
| 30 | GD | int | gidp | int | 이름 변경 |  |
| 31 | WP | int | wp | int | 이름 변경 |  |
| 32 | BK | int | bk | int | 이름 변경 |  |
| 33 | ERR | int | err | int | 이름 변경 |  |
| 34 | R | int | runs_cn | int | 이름 변경 |  |
| 35 | ER | int | er | int | 이름 변경 |  |
| 36 | BS | int | bs | int | 이름 변경 |  |

### Score → SCORE

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | 1T | smallint | inn_1_top | smallint | 이름 변경 |  |
| 4 | 1B | smallint | inn_1_bot | smallint | 이름 변경 |  |
| 5 | 2T | smallint | inn_2_top | smallint | 이름 변경 |  |
| 6 | 2B | smallint | inn_2_bot | smallint | 이름 변경 |  |
| 7 | 3T | smallint | inn_3_top | smallint | 이름 변경 |  |
| 8 | 3B | smallint | inn_3_bot | smallint | 이름 변경 |  |
| 9 | 4T | smallint | inn_4_top | smallint | 이름 변경 |  |
| 10 | 4B | smallint | inn_4_bot | smallint | 이름 변경 |  |
| 11 | 5T | smallint | inn_5_top | smallint | 이름 변경 |  |
| 12 | 5B | smallint | inn_5_bot | smallint | 이름 변경 |  |
| 13 | 6T | smallint | inn_6_top | smallint | 이름 변경 |  |
| 14 | 6B | smallint | inn_6_bot | smallint | 이름 변경 |  |
| 15 | 7T | smallint | inn_7_top | smallint | 이름 변경 |  |
| 16 | 7B | smallint | inn_7_bot | smallint | 이름 변경 |  |
| 17 | 8T | smallint | inn_8_top | smallint | 이름 변경 |  |
| 18 | 8B | smallint | inn_8_bot | smallint | 이름 변경 |  |
| 19 | 9T | smallint | inn_9_top | smallint | 이름 변경 |  |
| 20 | 9B | smallint | inn_9_bot | smallint | 이름 변경 |  |
| 21 | 10T | smallint | inn_10_top | smallint | 이름 변경 |  |
| 22 | 10B | smallint | inn_10_bot | smallint | 이름 변경 |  |
| 23 | 11T | smallint | inn_11_top | smallint | 이름 변경 |  |
| 24 | 11B | smallint | inn_11_bot | smallint | 이름 변경 |  |
| 25 | 12T | smallint | inn_12_top | smallint | 이름 변경 |  |
| 26 | 12B | smallint | inn_12_bot | smallint | 이름 변경 |  |
| 27 | 13T | smallint | inn_13_top | smallint | 이름 변경 |  |
| 28 | 13B | smallint | inn_13_bot | smallint | 이름 변경 |  |
| 29 | 14T | smallint | inn_14_top | smallint | 이름 변경 |  |
| 30 | 14B | smallint | inn_14_bot | smallint | 이름 변경 |  |
| 31 | 15T | smallint | inn_15_top | smallint | 이름 변경 |  |
| 32 | 15B | smallint | inn_15_bot | smallint | 이름 변경 |  |
| 33 | 16T | smallint | inn_16_top | smallint | 이름 변경 |  |
| 34 | 16B | smallint | inn_16_bot | smallint | 이름 변경 |  |
| 35 | 17T | smallint | inn_17_top | smallint | 이름 변경 |  |
| 36 | 17B | smallint | inn_17_bot | smallint | 이름 변경 |  |
| 37 | 18T | smallint | inn_18_top | smallint | 이름 변경 |  |
| 38 | 18B | smallint | inn_18_bot | smallint | 이름 변경 |  |
| 39 | 19T | smallint | inn_19_top | smallint | 이름 변경 |  |
| 40 | 19B | smallint | inn_19_bot | smallint | 이름 변경 |  |
| 41 | 20T | smallint | inn_20_top | smallint | 이름 변경 |  |
| 42 | 20B | smallint | inn_20_bot | smallint | 이름 변경 |  |
| 43 | 21T | smallint | inn_21_top | smallint | 이름 변경 |  |
| 44 | 21B | smallint | inn_21_bot | smallint | 이름 변경 |  |
| 45 | 22T | smallint | inn_22_top | smallint | 이름 변경 |  |
| 46 | 22B | smallint | inn_22_bot | smallint | 이름 변경 |  |
| 47 | 23T | smallint | inn_23_top | smallint | 이름 변경 |  |
| 48 | 23B | smallint | inn_23_bot | smallint | 이름 변경 |  |
| 49 | 24T | smallint | inn_24_top | smallint | 이름 변경 |  |
| 50 | 24B | smallint | inn_24_bot | smallint | 이름 변경 |  |
| 51 | 25T | smallint | inn_25_top | smallint | 이름 변경 |  |
| 52 | 25B | smallint | inn_25_bot | smallint | 이름 변경 |  |
| 53 | TPOINT | int | total_point | int | 이름 변경 |  |
| 54 | BPOINT | int | bat_point | int | 이름 변경 |  |
| 55 | THIT | int | total_hit | int | 이름 변경 |  |
| 56 | BHIT | int | bunt_hit | int | 이름 변경 |  |
| 57 | TERR | int | total_err | int | 이름 변경 |  |
| 58 | BERR | int | bat_err | int | 이름 변경 |  |
| 59 | TBBHP | int | total_bb_hbp | int | 이름 변경 |  |
| 60 | BBBHP | int | bb_bunt_hbp | int | 이름 변경 |  |

### DEFEN → DEFEN

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 |  |
| 2 | GDAY | int | game_dt | char(8) | 이름 변경 |  |
| 3 | TB | char(1) | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 4 | ONETURN | int | one_turn_if | bit | 이름 변경 |  |
| 5 | POSI | varchar(5) | position_cd | varchar(10) | 길이 변경 |  |
| 6 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) |  |
| 7 | PO | smallint | po | smallint | 이름 변경 |  |
| 8 | ASS | smallint | ast | smallint | 이름 변경 |  |
| 9 | ERR | smallint | err | smallint | 이름 변경 |  |
| 10 | DP | smallint | dp | smallint | 이름 변경 |  |
| 11 | PB | smallint | pb | smallint | 이름 변경 |  |
| 12 | INPUTTIME | datetime | input_tm | char(4) | 이름 변경 |  |

### GAME_HR → GAME_HR

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | LE_ID | smallint | league_id | smallint | 이름 변경 | PK |
| 2 | SR_ID | smallint | series_id | smallint | 이름 변경 | PK |
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 |  |
| 4 | G_ID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 5 | INN_NO | tinyint | inning_no | int | 타입 확장 (tinyint→int) |  |
| 6 | TB_SC | char(1) | top_bottom_sc | varchar(10) | 이름 변경 |  |
| 7 | BAT_P_ID | int | bat_player_id | int | 이름 변경 |  |
| 8 | PIT_P_ID | int | pit_player_id | int | 이름 변경 |  |
| 9 | PLACE_SC | char(1) | place_sc | varchar(10) | 이름 변경 |  |
| 10 | HR_DISTANCE_VA | smallint | hr_distance_va | int | 타입 확장 (smallint→int) |  |
| 11 | DIREC_SC | varchar(10) | direc_sc | varchar(10) | 이름 변경 |  |
| 12 | SCORE_CN | tinyint | score_cn | int | 타입 확장 (tinyint→int) |  |
| 13 | RECORD_DT | varchar(5) | record_dt | char(8) | 타입 변환 (varchar→char) |  |
| 14 | SEQ_NO | int | seq_no | int | 이름 변경 | PK |
| 15 | REG_DT | datetime | reg_dt | datetime2 | 타입 변환 (datetime→datetime2) |  |

### GAME_MEMO → GAME_MEMO

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | LE_ID | smallint | league_id | smallint | 이름 변경 | PK |
| 2 | SR_ID | smallint | series_id | smallint | 이름 변경 | PK |
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 |  |
| 4 | G_ID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 5 | INN_NO | tinyint | inning_no | int | 타입 확장 (tinyint→int) | PK |
| 6 | BAT_ORDER_NO | tinyint | bat_order_no | int | 타입 확장 (tinyint→int) | PK |
| 7 | BAT_AROUND_NO | tinyint | bat_around_no | int | 타입 확장 (tinyint→int) | PK |
| 8 | TB_SC | char(1) | top_bottom_sc | varchar(10) | 이름 변경 | PK |
| 9 | PA_PIT_NO | smallint | pa_pitch_no | int | 타입 확장 (smallint→int) | PK |
| 10 | GAME_PIT_NO | smallint | game_pitch_no | int | 타입 확장 (smallint→int) |  |
| 11 | P_ID | int | player_id | int | 이름 변경 |  |
| 12 | REQ_T_ID | char(2) | req_team_id | char(2) | 이름 변경 |  |
| 13 | START_TM | varchar(5) | start_tm | char(4) | 타입 변환 (varchar→char) |  |
| 14 | END_TM | varchar(5) | end_tm | char(4) | 타입 변환 (varchar→char) |  |
| 15 | USE_TM | varchar(5) | use_tm | char(4) | 타입 변환 (varchar→char) |  |
| 16 | FIRST_IF | varchar(20) | first_if | bit | 이름 변경 |  |
| 17 | LAST_IF | varchar(20) | last_if | bit | 이름 변경 |  |
| 18 | ETC_ME | varchar(400) | etc_memo | varchar(400) | 이름 변경 |  |
| 19 | ORDER_NO | int | order_no | int | 이름 변경 | PK |
| 20 | REG_DT | datetime | reg_dt | datetime2 | 타입 변환 (datetime→datetime2) |  |

### GAME_MEMO_PITCHCLOCK → GAME_MEMO_PITCHCLOCK

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | LE_ID | smallint | league_id | smallint | 이름 변경 | PK |
| 2 | SR_ID | smallint | series_id | smallint | 이름 변경 | PK |
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 |  |
| 4 | G_ID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 5 | INN_NO | tinyint | inning_no | int | 타입 확장 (tinyint→int) |  |
| 6 | BAT_ORDER_NO | tinyint | bat_order_no | int | 타입 확장 (tinyint→int) |  |
| 7 | BAT_AROUND_NO | tinyint | bat_around_no | int | 타입 확장 (tinyint→int) |  |
| 8 | TB_SC | char(1) | top_bottom_sc | varchar(10) | 이름 변경 |  |
| 9 | PA_PIT_NO | smallint | pa_pitch_no | int | 타입 확장 (smallint→int) |  |
| 10 | GAME_PIT_NO | smallint | game_pitch_no | int | 타입 확장 (smallint→int) |  |
| 11 | T_ID | char(2) | team_id | char(2) | 이름 변경 |  |
| 12 | P_ID | int | player_id | int | 이름 변경 |  |
| 13 | PIT_RESULT_SC | varchar(20) | pit_result_sc | varchar(10) | 길이 변경 |  |
| 14 | ETC_ME | varchar(400) | etc_memo | varchar(400) | 이름 변경 |  |
| 15 | SEQ_NO | int | seq_no | int | 이름 변경 | PK |
| 16 | REG_DT | datetime | reg_dt | datetime2 | 타입 변환 (datetime→datetime2) |  |

### PITCHCLOCK → PITCHCLOCK

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 4 | STADIUM | nvarchar(40) | stadium_nm | nvarchar(100) | 길이 변경 |  |
| 5 | VTEAM | nvarchar(4) | away_team_cd | varchar(10) | 이름 변경 |  |
| 6 | HTEAM | nvarchar(4) | home_team_cd | varchar(10) | 이름 변경 |  |
| 7 | HITNAME | varchar(15) | hitter_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 8 | HITTER | varchar(15) | hitter_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 9 | PITNAME | varchar(15) | pitcher_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 10 | PITCHER | varchar(15) | pitcher_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 11 | CATNAME | varchar(15) | catcher_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 12 | CATCHER | varchar(15) | catcher_id | varchar(15) | 이름 변경 |  |
| 13 | TEAM | nvarchar(4) | team_cd | varchar(10) | 이름 변경 |  |
| 14 | NAME | varchar(15) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 15 | PCODE | varchar(15) | player_id | int | 타입 변환 (varchar→int) |  |
| 16 | PITCHCLOCK | varchar(15) | pitch_clock_cd | varchar(10) | 길이 변경 |  |
| 17 | LIVETEXT | varchar(200) | live_text | nvarchar(200) | 인코딩 변환 (varchar→nvarchar) | PK |
| 18 | RUNNER | varchar(10) | runner_cd | varchar(10) | 이름 변경 |  |
| 19 | DETAIL | varchar(20) | detail_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |

## 2. 통계 (stats/)

### BatTotal → BAT_TOTAL

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 2 | GYEAR | char(4) | season_yr | char(4) | 이름 변경 | PK |
| 3 | SEC | varchar(4) | series_cd | varchar(10) | 길이 변경 | PK |
| 4 | TEAM | varchar(6) | team_cd | varchar(10) | 길이 변경 |  |
| 5 | HRA | float | avg | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 6 | GAMENUM | int | game_cn | int | 이름 변경 |  |
| 7 | AB | int | ab | int | 이름 변경 |  |
| 8 | RUN | int | run | int | 이름 변경 |  |
| 9 | HIT | int | hit | int | 이름 변경 |  |
| 10 | H2 | int | h2b | int | 이름 변경 |  |
| 11 | H3 | int | h3b | int | 이름 변경 |  |
| 12 | HR | int | hr | int | 이름 변경 |  |
| 13 | TB | int | tb_cn | int | 이름 변경 |  |
| 14 | RBI | int | rbi | int | 이름 변경 |  |
| 15 | SB | int | sb | int | 이름 변경 |  |
| 16 | CS | int | cs | int | 이름 변경 |  |
| 17 | SH | int | sh | int | 이름 변경 |  |
| 18 | SF | int | sf | int | 이름 변경 |  |
| 19 | BB | int | bb | int | 이름 변경 |  |
| 20 | HP | int | hbp | int | 이름 변경 |  |
| 21 | KK | int | so | int | 이름 변경 |  |
| 22 | GD | int | gidp | int | 이름 변경 |  |
| 23 | ERR | int | err | int | 이름 변경 |  |

### PitTotal → PIT_TOTAL

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 2 | GYEAR | char(4) | season_yr | char(4) | 이름 변경 | PK |
| 3 | SEC | varchar(4) | series_cd | varchar(10) | 길이 변경 | PK |
| 4 | Team | varchar(6) | team_cd | varchar(10) | 길이 변경 |  |
| 5 | ERA | float | era | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 6 | GAMENUM | smallint | game_cn | int | 타입 확장 (smallint→int) |  |
| 7 | CG | smallint | cg | smallint | 이름 변경 |  |
| 8 | SHO | smallint | sho | smallint | 이름 변경 |  |
| 9 | W | smallint | win | smallint | 이름 변경 |  |
| 10 | L | smallint | loss | smallint | 이름 변경 |  |
| 11 | SV | smallint | sv | smallint | 이름 변경 |  |
| 12 | Hold | smallint | hld | smallint | 이름 변경 |  |
| 13 | BF | smallint | bf | smallint | 이름 변경 |  |
| 14 | INN | varchar(8) | ip | varchar(8) | 이름 변경 |  |
| 15 | INN2 | smallint | inn_2_score | smallint | 이름 변경 |  |
| 16 | HIT | smallint | hit | smallint | 이름 변경 |  |
| 17 | HR | smallint | hr | smallint | 이름 변경 |  |
| 18 | BB | smallint | bb | smallint | 이름 변경 |  |
| 19 | HP | smallint | hbp | smallint | 이름 변경 |  |
| 20 | KK | smallint | so | smallint | 이름 변경 |  |
| 21 | R | smallint | runs_cn | int | 타입 확장 (smallint→int) |  |
| 22 | ER | smallint | er | smallint | 이름 변경 |  |

### TeamRank → TEAM_RANK

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GYEAR | nvarchar(4) | season_yr | char(4) | 이름 변경 | PK |
| 2 | SEC | varchar(4) | series_cd | varchar(10) | 길이 변경 | PK |
| 3 | RANK | int | rank_no | int | 이름 변경 |  |
| 4 | LEAGUE | char(5) | league_cd | varchar(10) | 이름 변경 |  |
| 5 | TEAM | nvarchar(6) | team_cd | varchar(10) | 이름 변경 | PK |
| 6 | GAME | int | game_cn | int | 이름 변경 |  |
| 7 | WIN | int | win | int | 이름 변경 |  |
| 8 | LOSE | int | loss | int | 이름 변경 |  |
| 9 | SAME | int | same_rank_if | bit | 이름 변경 |  |
| 10 | WRA | real | wrc | real | 이름 변경 |  |
| 11 | AB | int | ab | int | 이름 변경 |  |
| 12 | HIT | int | hit | int | 이름 변경 |  |
| 13 | HR | int | hr | int | 이름 변경 |  |
| 14 | SB | int | sb | int | 이름 변경 |  |
| 15 | RUN | int | run | int | 이름 변경 |  |
| 16 | INN | varchar(10) | ip | varchar(10) | 이름 변경 |  |
| 17 | INN2 | int | inn_2_score | int | 이름 변경 |  |
| 18 | R | int | runs_cn | int | 이름 변경 |  |
| 19 | ER | int | er | int | 이름 변경 |  |
| 20 | ERR | int | err | int | 이름 변경 |  |
| 21 | HRA | varchar(50) | avg | varchar(50) | 이름 변경 |  |
| 22 | LRA | varchar(50) | left_avg | varchar(50) | 이름 변경 |  |
| 23 | BRA | varchar(50) | bat_avg | varchar(50) | 이름 변경 |  |
| 24 | ERA | varchar(50) | era | varchar(50) | 이름 변경 |  |
| 25 | continue | varchar(50) | continue_if | bit | 이름 변경 |  |
| 26 | H2 | int | h2b | int | 이름 변경 |  |
| 27 | H3 | int | h3b | int | 이름 변경 |  |
| 28 | BB | int | bb | int | 이름 변경 |  |
| 29 | HP | int | hbp | int | 이름 변경 |  |
| 30 | SF | int | sf | int | 이름 변경 |  |

### KBO_BATRESULT → KBO_BAT_RESULT

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | TB | char(1) | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 4 | NAME | varchar(16) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 5 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 6 | TURN | char(2) | turn_no | int | 이름 변경 |  |
| 7 | ONETURN | char(1) | one_turn_if | bit | 타입 변환 (char→bit) |  |
| 8 | POSITION | varchar(10) | position_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 9 | CHANGEINN | varchar(2) | change_inn_no | int | 타입 변환 (varchar→int) |  |
| 10 | INN1 | varchar(10) | inn_1_score | varchar(10) | 이름 변경 |  |
| 11 | IL1 | varchar(10) | inn_1_loss | varchar(10) | 이름 변경 |  |
| 12 | INN1_3 | varchar(10) | inn_1_out3_score | varchar(10) | 이름 변경 |  |
| 13 | INN2 | varchar(10) | inn_2_score | varchar(10) | 이름 변경 |  |
| 14 | IL2 | varchar(10) | inn_2_loss | varchar(10) | 이름 변경 |  |
| 15 | INN2_3 | varchar(10) | inn_2_out3_score | varchar(10) | 이름 변경 |  |
| 16 | INN3 | varchar(10) | inn_3_score | varchar(10) | 이름 변경 |  |
| 17 | IL3 | varchar(10) | inn_3_loss | varchar(10) | 이름 변경 |  |
| 18 | INN3_3 | varchar(10) | inn_3_out3_score | varchar(10) | 이름 변경 |  |
| 19 | INN4 | varchar(10) | inn_4_score | varchar(10) | 이름 변경 |  |
| 20 | IL4 | varchar(10) | inn_4_loss | varchar(10) | 이름 변경 |  |
| 21 | INN4_3 | varchar(10) | inn_4_out3_score | varchar(10) | 이름 변경 |  |
| 22 | INN5 | varchar(10) | inn_5_score | varchar(10) | 이름 변경 |  |
| 23 | IL5 | varchar(10) | inn_5_loss | varchar(10) | 이름 변경 |  |
| 24 | INN5_3 | varchar(10) | inn_5_out3_score | varchar(10) | 이름 변경 |  |
| 25 | INN6 | varchar(10) | inn_6_score | varchar(10) | 이름 변경 |  |
| 26 | IL6 | varchar(10) | inn_6_loss | varchar(10) | 이름 변경 |  |
| 27 | INN6_3 | varchar(10) | inn_6_out3_score | varchar(10) | 이름 변경 |  |
| 28 | INN7 | varchar(10) | inn_7_score | varchar(10) | 이름 변경 |  |
| 29 | IL7 | varchar(10) | inn_7_loss | varchar(10) | 이름 변경 |  |
| 30 | INN7_3 | varchar(10) | inn_7_out3_score | varchar(10) | 이름 변경 |  |
| 31 | INN8 | varchar(10) | inn_8_score | varchar(10) | 이름 변경 |  |
| 32 | IL8 | varchar(10) | inn_8_loss | varchar(10) | 이름 변경 |  |
| 33 | INN8_3 | varchar(10) | inn_8_out3_score | varchar(10) | 이름 변경 |  |
| 34 | INN9 | varchar(10) | inn_9_score | varchar(10) | 이름 변경 |  |
| 35 | IL9 | varchar(10) | inn_9_loss | varchar(10) | 이름 변경 |  |
| 36 | INN9_3 | varchar(10) | inn_9_out3_score | varchar(10) | 이름 변경 |  |
| 37 | INN10 | varchar(10) | inn_10_score | varchar(10) | 이름 변경 |  |
| 38 | IL10 | varchar(10) | inn_10_loss | varchar(10) | 이름 변경 |  |
| 39 | INN10_3 | varchar(10) | inn_10_out3_score | varchar(10) | 이름 변경 |  |
| 40 | INN11 | varchar(10) | inn_11_score | varchar(10) | 이름 변경 |  |
| 41 | IL11 | varchar(10) | inn_11_loss | varchar(10) | 이름 변경 |  |
| 42 | INN11_3 | varchar(10) | inn_11_out3_score | varchar(10) | 이름 변경 |  |
| 43 | INN12 | varchar(10) | inn_12_score | varchar(10) | 이름 변경 |  |
| 44 | IL12 | varchar(10) | inn_12_loss | varchar(10) | 이름 변경 |  |
| 45 | INN12_3 | varchar(10) | inn_12_out3_score | varchar(10) | 이름 변경 |  |
| 46 | INN13 | varchar(10) | inn_13_score | varchar(10) | 이름 변경 |  |
| 47 | IL13 | varchar(10) | inn_13_loss | varchar(10) | 이름 변경 |  |
| 48 | INN13_3 | varchar(10) | inn_13_out3_score | varchar(10) | 이름 변경 |  |
| 49 | INN14 | varchar(10) | inn_14_score | varchar(10) | 이름 변경 |  |
| 50 | IL14 | varchar(10) | inn_14_loss | varchar(10) | 이름 변경 |  |
| 51 | INN14_3 | varchar(10) | inn_14_out3_score | varchar(10) | 이름 변경 |  |
| 52 | INN15 | varchar(10) | inn_15_score | varchar(10) | 이름 변경 |  |
| 53 | IL15 | varchar(10) | inn_15_loss | varchar(10) | 이름 변경 |  |
| 54 | INN15_3 | varchar(10) | inn_15_out3_score | varchar(10) | 이름 변경 |  |
| 55 | INN16 | varchar(10) | inn_16_score | varchar(10) | 이름 변경 |  |
| 56 | IL16 | varchar(10) | inn_16_loss | varchar(10) | 이름 변경 |  |
| 57 | INN16_3 | varchar(10) | inn_16_out3_score | varchar(10) | 이름 변경 |  |
| 58 | INN17 | varchar(10) | inn_17_score | varchar(10) | 이름 변경 |  |
| 59 | IL17 | varchar(10) | inn_17_loss | varchar(10) | 이름 변경 |  |
| 60 | INN17_3 | varchar(10) | inn_17_out3_score | varchar(10) | 이름 변경 |  |
| 61 | INN18 | varchar(10) | inn_18_score | varchar(10) | 이름 변경 |  |
| 62 | IL18 | varchar(10) | inn_18_loss | varchar(10) | 이름 변경 |  |
| 63 | INN18_3 | varchar(10) | inn_18_out3_score | varchar(10) | 이름 변경 |  |
| 64 | INN19 | varchar(10) | inn_19_score | varchar(10) | 이름 변경 |  |
| 65 | IL19 | varchar(10) | inn_19_loss | varchar(10) | 이름 변경 |  |
| 66 | INN19_3 | varchar(10) | inn_19_out3_score | varchar(10) | 이름 변경 |  |
| 67 | INN20 | varchar(10) | inn_20_score | varchar(10) | 이름 변경 |  |
| 68 | IL20 | varchar(10) | inn_20_loss | varchar(10) | 이름 변경 |  |
| 69 | INN20_3 | varchar(10) | inn_20_out3_score | varchar(10) | 이름 변경 |  |
| 70 | INN21 | varchar(10) | inn_21_score | varchar(10) | 이름 변경 |  |
| 71 | IL21 | varchar(10) | inn_21_loss | varchar(10) | 이름 변경 |  |
| 72 | INN21_3 | varchar(10) | inn_21_out3_score | varchar(10) | 이름 변경 |  |
| 73 | INN22 | varchar(10) | inn_22_score | varchar(10) | 이름 변경 |  |
| 74 | IL22 | varchar(10) | inn_22_loss | varchar(10) | 이름 변경 |  |
| 75 | INN22_3 | varchar(10) | inn_22_out3_score | varchar(10) | 이름 변경 |  |
| 76 | INN23 | varchar(10) | inn_23_score | varchar(10) | 이름 변경 |  |
| 77 | IL23 | varchar(10) | inn_23_loss | varchar(10) | 이름 변경 |  |
| 78 | INN23_3 | varchar(10) | inn_23_out3_score | varchar(10) | 이름 변경 |  |
| 79 | INN24 | varchar(10) | inn_24_score | varchar(10) | 이름 변경 |  |
| 80 | IL24 | varchar(10) | inn_24_loss | varchar(10) | 이름 변경 |  |
| 81 | INN24_3 | varchar(10) | inn_24_out3_score | varchar(10) | 이름 변경 |  |
| 82 | INN25 | varchar(10) | inn_25_score | varchar(10) | 이름 변경 |  |
| 83 | IL25 | varchar(10) | inn_25_loss | varchar(10) | 이름 변경 |  |
| 84 | INN25_3 | varchar(10) | inn_25_out3_score | varchar(10) | 이름 변경 |  |
| 85 | AB | tinyint | ab | tinyint | 이름 변경 |  |
| 86 | RUN | tinyint | run | tinyint | 이름 변경 |  |
| 87 | HIT | tinyint | hit | tinyint | 이름 변경 |  |
| 88 | RBI | tinyint | rbi | tinyint | 이름 변경 |  |
| 89 | AVGS | varchar(5) | avg_season | varchar(5) | 이름 변경 |  |
| 90 | AVG5 | varchar(5) | avg_5g | varchar(5) | 이름 변경 |  |

### KBO_PITRESULT → KBO_PIT_RESULT

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | TB | char(1) | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 4 | NAME | varchar(16) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 5 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 6 | POS | char(2) | position_cd | varchar(10) | 이름 변경 |  |
| 7 | WLS | varchar(1) | wls_cd | varchar(10) | 길이 변경 |  |
| 8 | CHANGEINN | varchar(4) | change_inn_no | int | 타입 변환 (varchar→int) |  |
| 9 | GAME | tinyint | game_cn | int | 타입 확장 (tinyint→int) |  |
| 10 | W | tinyint | win | tinyint | 이름 변경 |  |
| 11 | L | tinyint | loss | tinyint | 이름 변경 |  |
| 12 | S | tinyint | hits_cn | int | 타입 확장 (tinyint→int) |  |
| 13 | INN | varchar(5) | ip | varchar(5) | 이름 변경 |  |
| 14 | PA | tinyint | pa | tinyint | 이름 변경 |  |
| 15 | BF | tinyint | bf | tinyint | 이름 변경 |  |
| 16 | AB | tinyint | ab | tinyint | 이름 변경 |  |
| 17 | HIT | tinyint | hit | tinyint | 이름 변경 |  |
| 18 | HR | tinyint | hr | tinyint | 이름 변경 |  |
| 19 | BBHP | tinyint | bb_hbp | tinyint | 이름 변경 |  |
| 20 | KK | tinyint | so | tinyint | 이름 변경 |  |
| 21 | R | tinyint | runs_cn | int | 타입 확장 (tinyint→int) |  |
| 22 | ER | tinyint | er | tinyint | 이름 변경 |  |
| 23 | ERA | varchar(6) | era | varchar(6) | 이름 변경 |  |

### KBO_ETCGAME → KBO_ETC_GAME

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GMKEY | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GDAY | char(8) | game_dt | char(8) | 이름 변경 | PK |
| 3 | SEQ | tinyint | seq_no | int | 타입 확장 (tinyint→int) | PK |
| 4 | HOW | varchar(16) | how_cd | varchar(10) | 길이 변경 |  |
| 5 | RESULT | varchar(255) | result_cd | varchar(10) | 길이 변경 |  |

### SEASON_PLAYER_HITTER → SEASON_PLAYER_HITTER

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 | PK |
| 4 | P_ID | int | player_id | int | 이름 변경 | PK |
| 5 | SECTION_CD | int | section_cd | varchar(10) | 이름 변경 | PK |
| 6 | GROUP_IF | varchar(20) | group_if | bit | 이름 변경 | PK |
| 7 | HRA_RT | float | avg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 8 | GAME_CN | int | game_cn | int | 이름 변경 |  |
| 9 | PA_CN | int | pa_cn | int | 이름 변경 |  |
| 10 | AB_CN | int | ab_cn | int | 이름 변경 |  |
| 11 | RUN_CN | int | run_cn | int | 이름 변경 |  |
| 12 | HIT_CN | int | hit_cn | int | 이름 변경 |  |
| 13 | H2_CN | int | h2b_cn | int | 이름 변경 |  |
| 14 | H3_CN | int | h3b_cn | int | 이름 변경 |  |
| 15 | HR_CN | int | hr_cn | int | 이름 변경 |  |
| 16 | XBH_CN | int | xbh_cn | int | 이름 변경 |  |
| 17 | TB_CN | int | tb_cn | int | 이름 변경 |  |
| 18 | MH_HITTER_CN | int | mh_hitter_cn | int | 이름 변경 |  |
| 19 | RBI_CN | int | rbi_cn | int | 이름 변경 |  |
| 20 | SB_CN | int | sb_cn | int | 이름 변경 |  |
| 21 | CS_CN | int | cs_cn | int | 이름 변경 |  |
| 22 | SB_RT | float | sb_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 23 | RO_CN | int | ro_cn | int | 이름 변경 |  |
| 24 | POFF_CN | int | poff_cn | int | 이름 변경 |  |
| 25 | SH_CN | int | sh_cn | int | 이름 변경 |  |
| 26 | SF_CN | int | sf_cn | int | 이름 변경 |  |
| 27 | BB_CN | int | bb_cn | int | 이름 변경 |  |
| 28 | IB_CN | int | ibb_cn | int | 이름 변경 |  |
| 29 | HP_CN | int | hbp_cn | int | 이름 변경 |  |
| 30 | BBHP_CN | int | bb_hbp_cn | int | 이름 변경 |  |
| 31 | KK_CN | int | so_cn | int | 이름 변경 |  |
| 32 | GD_CN | int | gidp_cn | int | 이름 변경 |  |
| 33 | ERR_CN | int | err_cn | int | 이름 변경 |  |
| 34 | WIN_HIT_CN | int | win_hit_cn | int | 이름 변경 |  |
| 35 | GO_CN | int | go_cn | int | 이름 변경 |  |
| 36 | FO_CN | int | fo_cn | int | 이름 변경 |  |
| 37 | FOGO_RT | float | fo_go_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 38 | PA_PIT_RT | float | pa_pitch_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 39 | KK_BB_RT | float | so_bb_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 40 | SP_HRA_RT | float | vs_sp_avg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 41 | PH_HRA_RT | float | pinch_avg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 42 | OBP_RT | float | obp_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 43 | SLG_RT | float | slg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 44 | ISO_RT | float | iso_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 45 | OPS_RT | float | ops_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |

### SEASON_PLAYER_HITTER_SITUATION → SEASON_PLAYER_HITTER_SITUATION

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 | PK |
| 4 | P_ID | int | player_id | int | 이름 변경 | PK |
| 5 | SECTION_CD | int | section_cd | varchar(10) | 이름 변경 | PK |
| 6 | SITUATION_IF | varchar(20) | situation_if | bit | 이름 변경 | PK |
| 8 | AB_CN | int | ab_cn | int | 이름 변경 |  |
| 9 | HIT_CN | int | hit_cn | int | 이름 변경 |  |
| 10 | H2_CN | int | h2b_cn | int | 이름 변경 |  |
| 11 | H3_CN | int | h3b_cn | int | 이름 변경 |  |
| 12 | HR_CN | int | hr_cn | int | 이름 변경 |  |
| 13 | RBI_CN | int | rbi_cn | int | 이름 변경 |  |
| 14 | BB_CN | int | bb_cn | int | 이름 변경 |  |
| 15 | HP_CN | int | hbp_cn | int | 이름 변경 |  |
| 16 | KK_CN | int | so_cn | int | 이름 변경 |  |
| 17 | GD_CN | int | gidp_cn | int | 이름 변경 |  |

### SEASON_PLAYER_PITCHER → SEASON_PLAYER_PITCHER

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 | PK |
| 4 | P_ID | int | player_id | int | 이름 변경 | PK |
| 5 | SECTION_CD | int | section_cd | varchar(10) | 이름 변경 | PK |
| 6 | GROUP_IF | varchar(20) | group_if | bit | 이름 변경 | PK |
| 7 | ERA_RT | float | era_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 8 | GAME_CN | int | game_cn | int | 이름 변경 |  |
| 9 | START_CN | int | start_cn | int | 이름 변경 |  |
| 10 | QUIT_CN | int | quit_cn | int | 이름 변경 |  |
| 11 | W_CN | int | win_cn | int | 이름 변경 |  |
| 12 | START_W_CN | int | start_win_cn | int | 이름 변경 |  |
| 13 | RELIEF_W_CN | int | relief_win_cn | int | 이름 변경 |  |
| 14 | L_CN | int | loss_cn | int | 이름 변경 |  |
| 15 | D_CN | int | double_cn | int | 이름 변경 |  |
| 16 | HOLD_CN | int | hld_cn | int | 이름 변경 |  |
| 17 | SV_CN | int | sv_cn | int | 이름 변경 |  |
| 18 | SHO_CN | int | sho_cn | int | 이름 변경 |  |
| 19 | CG_CN | int | cg_cn | int | 이름 변경 |  |
| 20 | INN2_CN | int | ip_cn | int | 이름 변경 |  |
| 21 | WRA_RT | float | wrc_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 22 | PA_CN | int | pa_cn | int | 이름 변경 |  |
| 23 | AB_CN | int | ab_cn | int | 이름 변경 |  |
| 24 | PIT_CN | int | pitch_cn | int | 이름 변경 |  |
| 25 | R_CN | int | runs_cn | int | 이름 변경 |  |
| 26 | ER_CN | int | er_cn | int | 이름 변경 |  |
| 27 | HIT_CN | int | hit_cn | int | 이름 변경 |  |
| 28 | H2_CN | int | h2b_cn | int | 이름 변경 |  |
| 29 | H3_CN | int | h3b_cn | int | 이름 변경 |  |
| 30 | HR_CN | int | hr_cn | int | 이름 변경 |  |
| 31 | SH_CN | int | sh_cn | int | 이름 변경 |  |
| 32 | SF_CN | int | sf_cn | int | 이름 변경 |  |
| 33 | BB_CN | int | bb_cn | int | 이름 변경 |  |
| 34 | IB_CN | int | ibb_cn | int | 이름 변경 |  |
| 35 | HP_CN | int | hbp_cn | int | 이름 변경 |  |
| 36 | BBHP_CN | int | bb_hbp_cn | int | 이름 변경 |  |
| 37 | KK_CN | int | so_cn | int | 이름 변경 |  |
| 38 | GD_CN | int | gidp_cn | int | 이름 변경 |  |
| 39 | BK_CN | int | bk_cn | int | 이름 변경 |  |
| 40 | WP_CN | int | wp_cn | int | 이름 변경 |  |
| 41 | GO_CN | int | go_cn | int | 이름 변경 |  |
| 42 | FO_CN | int | fo_cn | int | 이름 변경 |  |
| 43 | FOGO_RT | float | fo_go_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 46 | BS_CN | int | bs_cn | int | 이름 변경 |  |
| 47 | QS_CN | int | qs_cn | int | 이름 변경 |  |
| 48 | WHIP_RT | float | whip_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 49 | OAVG_RT | float | opp_avg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 50 | OOBP_RT | float | opp_obp_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 51 | OSLG_RT | float | opp_slg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 52 | OOPS_RT | float | opp_ops_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 53 | BABIP_RT | float | babip_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 54 | GAME_KK_RT | float | game_so_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 55 | GAME_BB_RT | float | game_bb_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 56 | GAME_PIT_AVG_RT | float | game_pitch_avg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 57 | INN_PIT_AVG_RT | float | inn_pitch_avg_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |
| 58 | BB_KK_RT | float | bb_so_rt | decimal(8,5) | 타입 변환 (float→decimal) |  |

### SEASON_PLAYER_PITCHER_SITUATION → SEASON_PLAYER_PITCHER_SITUATION

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 | PK |
| 4 | P_ID | int | player_id | int | 이름 변경 | PK |
| 5 | SECTION_CD | int | section_cd | varchar(10) | 이름 변경 | PK |
| 6 | SITUATION_IF | varchar(20) | situation_if | bit | 이름 변경 | PK |
| 7 | AB_CN | int | ab_cn | int | 이름 변경 |  |
| 8 | HIT_CN | int | hit_cn | int | 이름 변경 |  |
| 9 | H2_CN | int | h2b_cn | int | 이름 변경 |  |
| 10 | H3_CN | int | h3b_cn | int | 이름 변경 |  |
| 11 | HR_CN | int | hr_cn | int | 이름 변경 |  |
| 12 | BB_CN | int | bb_cn | int | 이름 변경 |  |
| 13 | HP_CN | int | hbp_cn | int | 이름 변경 |  |
| 14 | KK_CN | int | so_cn | int | 이름 변경 |  |
| 15 | WP_CN | int | wp_cn | int | 이름 변경 |  |
| 16 | BK_CN | int | bk_cn | int | 이름 변경 |  |

## 3. 실시간 (realtime/)

### IE_LiveText → IE_LIVE_TEXT

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | LiveText | varchar(200) | live_text | nvarchar(200) | 인코딩 변환 (varchar→nvarchar) |  |
| 4 | SeqNO | smallint | seq_no | int | 타입 확장 (smallint→int) | PK |
| 5 | Inning | tinyint | inning_no | int | 타입 확장 (tinyint→int) |  |
| 6 | bTop | tinyint | top_bottom_cd | varchar(10) | 이름 변경 |  |
| 7 | textStyle | tinyint | text_style_cd | varchar(10) | 이름 변경 |  |

### IE_BallCount → IE_BALL_COUNT

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | strike | tinyint | strike_cn | int | 타입 확장 (tinyint→int) |  |
| 4 | ball | tinyint | ball_cn | int | 타입 확장 (tinyint→int) |  |
| 5 | out | tinyint | out_cn | int | 타입 확장 (tinyint→int) |  |
| 6 | base1 | tinyint | base_1b_id | tinyint | 이름 변경 |  |
| 7 | base2 | tinyint | base_2b_id | tinyint | 이름 변경 |  |
| 8 | base3 | tinyint | base_3b_id | tinyint | 이름 변경 |  |
| 9 | pitcher | varchar(10) | pitcher_id | varchar(10) | 이름 변경 |  |
| 10 | batter | varchar(10) | batter_id | varchar(10) | 이름 변경 |  |
| 11 | batResult | varchar(50) | bat_result_cd | varchar(10) | 길이 변경 |  |

### IE_BatterRecord → IE_BATTER_RECORD

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | BatOrder | tinyint | bat_order_no | int | 타입 확장 (tinyint→int) | PK |
| 4 | Position | tinyint | position_nm | nvarchar(100) | 이름 변경 |  |
| 5 | PositionName | varchar(20) | position_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 6 | PlayerName | varchar(15) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 7 | PlayerID | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 8 | SeqNO | tinyint | seq_no | int | 타입 확장 (tinyint→int) | PK |
| 9 | OAB | tinyint | opp_ab | tinyint | 이름 변경 |  |
| 10 | Run | tinyint | run | tinyint | 이름 변경 |  |
| 11 | H1 | tinyint | h1b | tinyint | 이름 변경 |  |
| 12 | H2 | tinyint | h2b | tinyint | 이름 변경 |  |
| 13 | H3 | tinyint | h3b | tinyint | 이름 변경 |  |
| 14 | HR | tinyint | hr | tinyint | 이름 변경 |  |
| 15 | RBI | tinyint | rbi | tinyint | 이름 변경 |  |
| 16 | Steal | tinyint | sb | tinyint | 이름 변경 |  |
| 17 | CS | tinyint | cs | tinyint | 이름 변경 |  |
| 18 | SH | tinyint | sh | tinyint | 이름 변경 |  |
| 19 | SF | tinyint | sf | tinyint | 이름 변경 |  |
| 20 | BB | tinyint | bb | tinyint | 이름 변경 |  |
| 21 | HBP | tinyint | hbp | tinyint | 이름 변경 |  |
| 22 | SO | tinyint | so | tinyint | 이름 변경 |  |
| 23 | DP | tinyint | dp | tinyint | 이름 변경 |  |
| 24 | TP | tinyint | total_put | tinyint | 이름 변경 |  |
| 25 | bHome | tinyint | home_if | bit | 타입 변환 (tinyint→bit) |  |

### IE_PitcherRecord → IE_PITCHER_RECORD

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | PlayerName | varchar(15) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 4 | PlayerID | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 5 | SeqNO | tinyint | seq_no | int | 타입 확장 (tinyint→int) |  |
| 6 | Inning | varchar(5) | inning_no | int | 타입 변환 (varchar→int) |  |
| 7 | PA | tinyint | pa | tinyint | 이름 변경 |  |
| 8 | PitchBallCnt | tinyint | pitch_ball_cn | int | 타입 확장 (tinyint→int) |  |
| 9 | PitchStrikeCnt | tinyint | pitch_strike_cn | int | 타입 확장 (tinyint→int) |  |
| 10 | OAB | tinyint | opp_ab | tinyint | 이름 변경 |  |
| 11 | Run | tinyint | run | tinyint | 이름 변경 |  |
| 12 | Hit | tinyint | hit | tinyint | 이름 변경 |  |
| 13 | HR | tinyint | hr | tinyint | 이름 변경 |  |
| 14 | SH | tinyint | sh | tinyint | 이름 변경 |  |
| 15 | SF | tinyint | sf | tinyint | 이름 변경 |  |
| 16 | BB | tinyint | bb | tinyint | 이름 변경 |  |
| 17 | HBP | tinyint | hbp | tinyint | 이름 변경 |  |
| 18 | SO | tinyint | so | tinyint | 이름 변경 |  |
| 19 | BK | tinyint | bk | tinyint | 이름 변경 |  |
| 20 | WP | tinyint | wp | tinyint | 이름 변경 |  |
| 21 | ER | tinyint | er | tinyint | 이름 변경 |  |
| 22 | bHome | tinyint | home_if | bit | 타입 변환 (tinyint→bit) |  |

### IE_GameList → IE_GAME_LIST

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | HomeName | varchar(8) | home_team_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 4 | HomeMascot | varchar(20) | home_mascot_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 5 | VisitName | varchar(8) | away_team_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 6 | VisitMascot | varchar(20) | away_mascot_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |

### IE_GAMESTATE → IE_GAME_STATE

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GAMEID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | STATUS_ID | tinyint | status_id | smallint | 타입 확장 (tinyint→smallint) |  |
| 4 | INN_NO | tinyint | inning_no | int | 타입 확장 (tinyint→int) |  |
| 5 | TB_SC | char(1) | top_bottom_sc | varchar(10) | 이름 변경 |  |

### IE_ScoreRHEB → IE_SCORE_RHEB

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | Run | tinyint | run | tinyint | 이름 변경 |  |
| 4 | Hit | tinyint | hit | tinyint | 이름 변경 |  |
| 5 | Error | tinyint | err | tinyint | 이름 변경 |  |
| 6 | BallFour | tinyint | ball_four_if | bit | 타입 변환 (tinyint→bit) |  |
| 7 | bHome | tinyint | home_if | bit | 타입 변환 (tinyint→bit) | PK |

### IE_Scoreinning → IE_SCORE_INNING

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 3 | inning | tinyint | inning_no | int | 타입 확장 (tinyint→int) | PK |
| 4 | Score | tinyint | score_cn | int | 타입 확장 (tinyint→int) |  |
| 5 | bHome | tinyint | home_if | bit | 타입 변환 (tinyint→bit) | PK |

### IE_log → IE_LOG

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gameID | char(13) | game_id | char(13) | 이름 변경 |  |
| 2 | SeqNO | smallint | seq_no | int | 타입 확장 (smallint→int) |  |
| 3 | InsertedTime | datetime | inserted_tm | char(4) | 이름 변경 |  |

## 4. 마스터 (master/)

### person → PERSON

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 2 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 3 | NAME | varchar(20) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 4 | TEAM | varchar(20) | team_cd | varchar(10) | 길이 변경 |  |
| 5 | T_ID | char(2) | team_id | char(2) | 이름 변경 |  |
| 6 | POS | char(1) | position_cd | varchar(10) | 이름 변경 |  |
| 7 | POSITION | varchar(4) | position_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 8 | BACKNUM | varchar(50) | back_no | int | 타입 변환 (varchar→int) |  |
| 9 | ENGNAME | nvarchar(50) | player_eng_nm | nvarchar(100) | 길이 변경 |  |
| 10 | CNAME | nvarchar(30) | player_hanja_nm | nvarchar(100) | 길이 변경 |  |
| 11 | HITTYPE | varchar(8) | bat_throw_cd | varchar(10) | 길이 변경 |  |
| 12 | BIRTH | varchar(8) | birth_dt | char(8) | 타입 변환 (varchar→char) |  |
| 13 | HEIGHT | varchar(3) | height_va | int | 타입 변환 (varchar→int) |  |
| 14 | WEIGHT | varchar(3) | weight_va | int | 타입 변환 (varchar→int) |  |
| 15 | INDATE | varchar(8) | join_dt | char(8) | 타입 변환 (varchar→char) |  |
| 16 | PROMISE | varchar(12) | signing_bonus_va | int | 타입 변환 (varchar→int) |  |
| 17 | MONEY | varchar(12) | salary_va | int | 타입 변환 (varchar→int) |  |
| 18 | CAREER | varchar(255) | career_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 19 | DRAFT | varchar(70) | draft_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 20 | REG_DT | datetime | reg_dt | datetime2 | 타입 변환 (datetime→datetime2) |  |

### person2 → PERSON2

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 2 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 3 | NAME | varchar(20) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) | PK |
| 4 | TEAM | varchar(8) | team_cd | varchar(10) | 길이 변경 |  |
| 5 | T_ID | char(2) | team_id | char(2) | 이름 변경 |  |
| 6 | POS | char(1) | position_cd | varchar(10) | 이름 변경 |  |
| 7 | POSITION | varchar(4) | position_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 8 | BACKNUM | varchar(50) | back_no | int | 타입 변환 (varchar→int) |  |
| 9 | CNAME | varchar(30) | player_hanja_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 10 | HITTYPE | varchar(8) | bat_throw_cd | varchar(10) | 길이 변경 |  |
| 11 | BIRTH | varchar(8) | birth_dt | char(8) | 타입 변환 (varchar→char) |  |
| 12 | HEIGHT | varchar(3) | height_va | int | 타입 변환 (varchar→int) |  |
| 13 | WEIGHT | varchar(3) | weight_va | int | 타입 변환 (varchar→int) |  |
| 14 | INDATE | varchar(8) | join_dt | char(8) | 타입 변환 (varchar→char) |  |
| 15 | PROMISE | varchar(12) | signing_bonus_va | int | 타입 변환 (varchar→int) |  |
| 16 | MONEY | varchar(12) | salary_va | int | 타입 변환 (varchar→int) |  |
| 17 | CAREER | varchar(70) | career_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |

### PERSON → PERSON

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GYEAR | smallint | season_yr | smallint | 이름 변경 | PK |
| 2 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) | PK |
| 3 | NAME | varchar(20) | player_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 4 | TEAM | varchar(8) | team_cd | varchar(10) | 길이 변경 |  |
| 5 | POS | char(1) | position_cd | varchar(10) | 이름 변경 |  |
| 6 | POSITION | varchar(4) | position_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 7 | BACKNUM | varchar(50) | back_no | int | 타입 변환 (varchar→int) |  |
| 8 | CNAME | varchar(30) | player_hanja_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 9 | HITTYPE | varchar(8) | bat_throw_cd | varchar(10) | 길이 변경 |  |
| 10 | BIRTH | varchar(8) | birth_dt | char(8) | 타입 변환 (varchar→char) |  |
| 11 | HEIGHT | varchar(3) | height_va | int | 타입 변환 (varchar→int) |  |
| 12 | WEIGHT | varchar(3) | weight_va | int | 타입 변환 (varchar→int) |  |
| 13 | INDATE | varchar(8) | join_dt | char(8) | 타입 변환 (varchar→char) |  |
| 14 | PROMISE | varchar(12) | signing_bonus_va | int | 타입 변환 (varchar→int) |  |
| 15 | MONEY | varchar(12) | salary_va | int | 타입 변환 (varchar→int) |  |
| 16 | CAREER | varchar(255) | career_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |

### PERSON_FA → PERSON_FA

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | GYEAR | smallint | season_yr | smallint | 이름 변경 |  |
| 2 | PCODE | varchar(10) | player_id | int | 타입 변환 (varchar→int) |  |
| 3 | MONEY | varchar(12) | salary_va | int | 타입 변환 (varchar→int) |  |
| 4 | OPTION | varchar(12) | option_cd | varchar(10) | 길이 변경 |  |

### TEAM → TEAM

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 2 | SEASON_ID | smallint | season_id | smallint | 이름 변경 | PK |
| 3 | T_ID | char(2) | team_id | char(2) | 이름 변경 | PK |
| 4 | FIRST_NM | varchar(50) | first_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 5 | LAST_NM | varchar(50) | last_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 6 | FIRST_ENG_NM | varchar(50) | first_eng_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 7 | LAST_ENG_NM | varchar(50) | last_eng_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 8 | GROUP_SC | varchar(10) | group_sc | varchar(10) | 이름 변경 |  |

### STADIUM → STADIUM

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gyear | char(4) | season_yr | char(4) | 이름 변경 | PK |
| 2 | stadium | varchar(10) | stadium_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) | PK |
| 3 | stadium_key | char(2) | stadium_id | char(2) | 이름 변경 |  |

### KBO_schedule → KBO_SCHEDULE

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | gmkey | char(13) | game_id | char(13) | 이름 변경 | PK |
| 2 | game_flag | char(1) | game_type_cd | varchar(10) | 이름 변경 |  |
| 3 | end_flag | char(1) | end_if | bit | 타입 변환 (char→bit) |  |
| 4 | gamedate | varchar(8) | game_dt | char(8) | 타입 변환 (varchar→char) | PK |
| 5 | gyear | char(4) | season_yr | char(4) | 이름 변경 |  |
| 6 | gmonth | char(2) | game_mon | char(2) | 이름 변경 |  |
| 7 | gday | char(2) | game_dt | char(8) | 길이 변경 (char(2)→char(8)) |  |
| 8 | gweek | varchar(2) | game_week_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 9 | home | varchar(10) | home_team_cd | varchar(10) | 이름 변경 |  |
| 10 | home_key | char(2) | home_team_id | char(2) | 이름 변경 |  |
| 11 | visit | varchar(10) | away_team_cd | varchar(10) | 이름 변경 |  |
| 12 | visit_key | char(2) | away_team_id | char(2) | 이름 변경 |  |
| 13 | stadium | varchar(10) | stadium_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 14 | stadium_key | char(2) | stadium_id | char(2) | 이름 변경 |  |
| 15 | dheader | char(1) | doubleheader_no | int | 이름 변경 |  |
| 16 | hpcode | char(5) | home_pitcher_id | char(5) | 이름 변경 |  |
| 17 | vpcode | char(5) | away_pitcher_id | char(5) | 이름 변경 |  |
| 18 | gtime | char(5) | game_tm | char(4) | 길이 변경 (char(5)→char(4)) |  |
| 19 | hscore | tinyint | home_score | tinyint | 이름 변경 |  |
| 20 | vscore | tinyint | away_score | tinyint | 이름 변경 |  |
| 21 | cancel_flag | bit | cancel_if | bit | 이름 변경 |  |
| 22 | suspended_flag | bit | suspended_if | bit | 이름 변경 |  |

### CANCEL_GAME → CANCEL_GAME

| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |
|---|----------|----------|----------|----------|----------|------|
| 1 | LE_ID | smallint | league_id | smallint | 이름 변경 | PK |
| 2 | SR_ID | smallint | series_id | smallint | 이름 변경 | PK |
| 3 | SEASON_ID | smallint | season_id | smallint | 이름 변경 |  |
| 4 | G_ID | char(13) | game_id | char(13) | 이름 변경 | PK |
| 5 | CANCEL_SC_NM | varchar(20) | cancel_sc_nm | nvarchar(100) | 인코딩 변환 (varchar→nvarchar) |  |
| 6 | REG_DT | datetime | reg_dt | datetime2 | 타입 변환 (datetime→datetime2) |  |
