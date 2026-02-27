# 업무 용어 사전

> 최종수정: 2026-02-24 | KBO 데이터 표준 정의서 (RFP DAR-001)

## 1. 개요

KBO 데이터 시스템에서 사용하는 업무 용어를 정의한다. 이 문서는 데이터 사전(`dictionary/`)의 컬럼 설명과 연동되며, 기술팀뿐 아니라 기록위원·운영팀·경영진 등 비기술 이해관계자도 참조할 수 있도록 작성한다.

**사용법**:
- 각 용어의 "DB 컬럼"은 표준명(안)이며, 레거시명은 괄호 안에 표기
- "관련 테이블"은 해당 용어가 사용되는 주요 테이블
- 부록의 가나다순 색인으로 빠른 검색 가능

→ 참고: [약어 사전](../standards-dict/abbreviations.md) - 약어 정의
→ 참고: [코드 사전](../standards-dict/codes.md) - 코드값 상세

---

## 2. 야구 기록 용어

### 2.1 타격 기록

| 용어 | 영문 | 약어 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|------|---------|------------|
| 타석 | Plate Appearance | PA | 타자가 타석에 들어선 횟수. 볼넷·사구·희생 포함 | `pa` (레거시: `PA`) | Hitter, BatTotal |
| 타수 | At Bat | AB | 타석에서 볼넷·사구·희생번트·희생플라이를 제외한 횟수 | `ab` (레거시: `AB`) | Hitter, BatTotal |
| 안타 | Hit | HIT | 타자가 안전하게 출루한 타격. 1루타+2루타+3루타+홈런 | `hit` (레거시: `HIT`) | Hitter, BatTotal |
| 1루타 | Single | H1 | 타격 후 1루까지 진루한 안타 | `h1b` (레거시: `H1`) | Hitter |
| 2루타 | Double | H2 | 타격 후 2루까지 진루한 안타 | `h2b` (레거시: `H2`) | Hitter, BatTotal |
| 3루타 | Triple | H3 | 타격 후 3루까지 진루한 안타 | `h3b` (레거시: `H3`) | Hitter, BatTotal |
| 홈런 | Home Run | HR | 타격 후 본루까지 진루한 안타 | `hr` (레거시: `HR`) | Hitter, BatTotal, GAME_HR |
| 타점 | Runs Batted In | RBI | 타자의 타격·희생 등으로 주자가 득점한 수 | `rbi` (레거시: `RBI`) | Hitter, BatTotal |
| 득점 | Run Scored | RUN | 주자가 본루를 밟아 득점한 횟수 | `run` (레거시: `RUN`) | Hitter, BatTotal |
| 볼넷 | Base on Balls | BB | 투수가 4볼을 던져 타자에게 1루를 내준 것 | `bb` (레거시: `BB`) | Hitter, Pitcher, BatTotal |
| 사구 | Hit by Pitch | HBP | 투수의 공이 타자 몸에 맞아 1루로 출루 | `hbp` (레거시: `HP`) | Hitter, BatTotal |
| 고의사구 | Intentional Walk | IBB | 투수가 의도적으로 볼넷을 허용한 것 | `ibb` (레거시: `IB`) | Hitter, BatTotal |
| 삼진 | Strikeout | SO | 3스트라이크로 타자가 아웃된 것 | `so` (레거시: `KK`) | Hitter, Pitcher, BatTotal |
| 도루 | Stolen Base | SB | 주자가 투수의 투구 중 다음 루로 진루 | `sb` (레거시: `SB`) | Hitter, BatTotal |
| 도루실패 | Caught Stealing | CS | 도루 시도 중 태그아웃 | `cs` (레거시: `CS`) | Hitter, BatTotal |
| 희생번트 | Sacrifice Hit | SH | 타자가 번트로 자신을 희생하여 주자를 진루시킨 것 | `sh` (레거시: `SH`) | Hitter, BatTotal |
| 희생플라이 | Sacrifice Fly | SF | 외야 플라이로 자신은 아웃되나 3루 주자가 득점 | `sf` (레거시: `SF`) | Hitter, BatTotal |
| 병살타 | Grounded into DP | GIDP | 타자의 타격으로 2명의 주자가 동시 아웃 | `gidp` (레거시: `GD`) | Hitter, BatTotal |
| 실책 | Error | ERR | 수비수의 실수로 주자가 진루하거나 타자가 출루 | `err` (레거시: `ERR`) | Hitter, DEFEN |
| 잔루 | Left on Base | LOB | 이닝 종료 시 루상에 남은 주자 수 | `lob` (레거시: `LOB`) | Hitter |
| 루타 | Total Bases | TB | 안타로 획득한 총 루수. 1루타×1 + 2루타×2 + 3루타×3 + 홈런×4 | `tb_cn` (레거시: `TB` int) | BatTotal |
| 장타 | Extra Base Hit | XBH | 2루타 이상의 안타 (2루타+3루타+홈런) | `xbh_cn` (레거시: `XBH_CN`) | SEASON_PLAYER_HITTER |

### 2.2 투수 기록

| 용어 | 영문 | 약어 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|------|---------|------------|
| 이닝 | Innings Pitched | IP | 투수가 던진 이닝 수. 1이닝=3아웃, 2/3이닝=2아웃 | `ip` (레거시: `INN`) | Pitcher, PitTotal |
| 상대타자수 | Batters Faced | BF | 투수가 상대한 총 타자 수 | `bf` (레거시: `BF`) | Pitcher, PitTotal |
| 승리 | Win | W | 경기에서 승리 투수로 기록된 것 | `win` (레거시: `W`) | Pitcher, PitTotal |
| 패배 | Loss | L | 경기에서 패전 투수로 기록된 것 | `loss` (레거시: `L`) | Pitcher, PitTotal |
| 세이브 | Save | SV | 리드를 지키며 경기를 마무리한 구원 투수에게 부여 | `sv` (레거시: `SV`) | Pitcher, PitTotal |
| 홀드 | Hold | HLD | 리드 상황에서 등판하여 리드를 유지한 구원 투수 | `hld` (레거시: `HOLD`) | Pitcher, PitTotal |
| 블론세이브 | Blown Save | BS | 세이브 상황에서 리드를 내준 것 | `bs` (레거시: `BS`) | Pitcher, PitTotal |
| 완투 | Complete Game | CG | 투수가 경기 전체를 혼자 던진 것 | `cg` (레거시: `CG`) | Pitcher, PitTotal |
| 완봉 | Shutout | SHO | 완투하면서 무실점으로 경기를 마친 것 | `sho` (레거시: `SHO`) | Pitcher, PitTotal |
| 자책점 | Earned Run | ER | 투수의 책임으로 인정되는 실점 (실책 제외) | `er` (레거시: `ER`) | Pitcher, PitTotal |
| 실점 | Runs Allowed | R | 투수 등판 중 상대팀이 기록한 총 득점 | `runs_cn` (레거시: `R`) | Pitcher, PitTotal |
| 투구수 | Number of Pitches | NP | 경기에서 투수가 던진 총 투구 수 | `pitch_cn` (레거시: `PIT_CN`) | Pitcher |
| 폭투 | Wild Pitch | WP | 포수가 잡을 수 없는 투구로 주자가 진루 | `wp` (레거시: `WP`) | Pitcher, PitTotal |
| 보크 | Balk | BK | 투수의 규칙 위반 동작으로 주자에게 진루 허용 | `bk` (레거시: `BK`) | Pitcher, PitTotal |
| 포일 | Passed Ball | PB | 포수가 잡을 수 있었던 투구를 놓쳐 주자가 진루 | `pb` (레거시: `PB`) | DEFEN |
| 승패세 | Win/Loss/Save | WLS | 투수의 경기 결과 (W=승, L=패, S=세이브) | `wls_cd` (레거시: `WLS`) | Pitcher |
| QS | Quality Start | QS | 선발 투수가 6이닝 이상, 자책점 3점 이하로 던진 경기 | `qs_cn` (레거시: `QS_CN`) | PitTotal, SEASON_PLAYER_PITCHER |
| 선발 | Start | START | 경기 첫 이닝부터 등판한 투수 | `start_if` (레거시: `START`) | Pitcher |

### 2.3 수비 기록

| 용어 | 영문 | 약어 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|------|---------|------------|
| 자살 | Put Out | PO | 수비수가 직접 아웃을 기록한 것 (플라이 캐치, 태그 등) | `po` (레거시: `PO`) | DEFEN |
| 보살 | Assist | AST | 다른 수비수의 아웃을 도운 것 (송구 등) | `ast` (레거시: `ASS`) | DEFEN |
| 병살 | Double Play | DP | 하나의 수비 플레이에서 2명의 주자를 아웃시킨 것 | `dp` (레거시: `DP`) | DEFEN |
| 견제사 | Pickoff | POFF | 투수 또는 포수가 루상 주자를 견제하여 아웃시킨 것 | `poff_cn` (레거시: `POFF_CN`) | PitTotal |
| 플라이아웃 | Fly Out | FO | 타구가 공중에서 수비수에게 잡혀 아웃 | `fo_cn` (레거시: `FO_CN`) | PitTotal |
| 땅볼아웃 | Ground Out | GO | 타구가 땅에 튀어 수비수에게 잡혀 아웃 | `go_cn` (레거시: `GO_CN`) | PitTotal |

### 2.4 비율/세이버메트릭스

| 용어 | 영문 | 약어 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|------|---------|------------|
| 타율 | Batting Average | AVG | 안타/타수. 타자의 안타 생산 능력 지표 | `avg_rt` (레거시: `HRA`) | BatTotal, SEASON_PLAYER_HITTER |
| 출루율 | On-Base Percentage | OBP | (안타+볼넷+사구)/(타수+볼넷+사구+희생플라이) | `obp_rt` (레거시: `OBP_RT`) | SEASON_PLAYER_HITTER |
| 장타율 | Slugging Percentage | SLG | 루타/타수. 장타력 지표 | `slg_rt` (레거시: `SLG_RT`) | SEASON_PLAYER_HITTER |
| OPS | OBP + SLG | OPS | 출루율+장타율. 타자 종합 공격력 지표 | `ops_rt` (레거시: `OPS_RT`) | SEASON_PLAYER_HITTER |
| 순장타율 | Isolated Power | ISO | 장타율-타율. 순수 장타 능력 | `iso_rt` (레거시: `ISO_RT`) | SEASON_PLAYER_HITTER |
| BABIP | Batting Avg on Balls in Play | BABIP | 인플레이 타구 중 안타 비율. 운 vs 실력 판별 | `babip_rt` (레거시: `BABIP_RT`) | SEASON_PLAYER_HITTER |
| 평균자책점 | Earned Run Average | ERA | 9이닝당 자책점 수. 투수의 핵심 지표 | `era_rt` (레거시: `ERA`) | PitTotal, SEASON_PLAYER_PITCHER |
| WHIP | Walks+Hits per IP | WHIP | 이닝당 허용 볼넷+안타. 투수 안정성 지표 | `whip_rt` (레거시: `WHIP_RT`) | SEASON_PLAYER_PITCHER |
| 삼진/볼넷 비율 | Strikeout-to-Walk Ratio | K/BB | 삼진수/볼넷수. 투수 제구력 지표 | `so_bb_rt` (레거시: `KK_BB_RT`) | SEASON_PLAYER_PITCHER |
| 피안타율 | Opponent Batting Average | OAVG | 상대 타자의 타율. 피안타/상대타수 | `opp_avg_rt` (레거시: `OAVG_RT`) | SEASON_PLAYER_PITCHER |
| 피출루율 | Opponent OBP | OOBP | 상대 타자의 출루율 | `opp_obp_rt` (레거시: `OOBP_RT`) | SEASON_PLAYER_PITCHER |
| 피장타율 | Opponent SLG | OSLG | 상대 타자의 장타율 | `opp_slg_rt` (레거시: `OSLG_RT`) | SEASON_PLAYER_PITCHER |
| 피OPS | Opponent OPS | OOPS | 상대 타자의 OPS | `opp_ops_rt` (레거시: `OOPS_RT`) | SEASON_PLAYER_PITCHER |
| 가중득점생산 | Weighted Runs Created | wRC | 타자의 득점 기여를 가중치로 환산한 세이버메트릭스 지표 | `wrc` (레거시: `WRA`) | SEASON_PLAYER_HITTER |
| 도루 성공률 | Stolen Base Percentage | SB% | 도루성공/(도루성공+도루실패) | `sb_rt` (레거시: `SB_RT`) | SEASON_PLAYER_HITTER |

---

## 3. 경기 운영 용어

### 3.1 경기 일반

| 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|---------|------------|
| 경기키 | Game Key | 경기를 고유하게 식별하는 13자리 코드 (YYYYMMDDVVHH#) | `game_id` (레거시: `GMKEY`) | 전체 |
| 경기일자 | Game Date | 경기가 열린 날짜 (YYYYMMDD) | `game_dt` (레거시: `GDAY`) | GAMEINFO, Hitter, Pitcher |
| 시즌 연도 | Season Year | 해당 시즌의 4자리 연도. 9999=통산 기록 | `season_yr` (레거시: `GYEAR`) | 전체 |
| 더블헤더 | Doubleheader | 같은 날 같은 팀이 2경기를 치르는 것. 번호로 구분 (0/1/2) | `doubleheader_no` (레거시: `DBHD`) | GAMEINFO |
| 차전 | Round | 포스트시즌 등에서 몇 번째 경기인지 나타내는 번호 | `round_no` (레거시: `CHAJUN`) | GAMEINFO |
| 관중수 | Attendance | 해당 경기의 입장 관중 수 | `crowd_cn` (레거시: `CROWD`) | GAMEINFO |
| 경기수 | Game Number | 시즌 중 해당 팀/선수의 누적 경기 수 | `game_cn` (레거시: `GAMENUM`) | BatTotal, PitTotal |
| 구간 | Section | 집계 구분. 시즌 연도 또는 9999(통산) | `series_cd` (레거시: `SEC`) | BatTotal, PitTotal |
| 초/말 | Top/Bottom | 이닝의 전반(초, T=원정팀 공격)과 후반(말, B=홈팀 공격) | `top_bottom_cd` (레거시: `TB` char) | Hitter, Pitcher, Score |
| 아웃카운트 | Out Count | 현재 이닝의 아웃 수 (0, 1, 2, 4=이닝종료) | `out_count` (레거시: `OCOUNT`) | GAMECONTAPP |
| 경기 요일 | Day of Week | 경기가 열린 요일 | `game_week_cd` (레거시: `GWEEK`) | GAMEINFO |

### 3.2 심판/기록원

| 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|---------|------------|
| 주심 | Home Plate Umpire | 홈플레이트 뒤에서 스트라이크/볼을 판정하는 심판 | `umpire_chief_nm` (레거시: `UMPC`) | GAMEINFO |
| 1루심 | 1st Base Umpire | 1루 라인을 담당하는 심판 | `umpire_1b_nm` (레거시: `UMP1`) | GAMEINFO |
| 2루심 | 2nd Base Umpire | 2루 부근을 담당하는 심판 | `umpire_2b_nm` (레거시: `UMP2`) | GAMEINFO |
| 3루심 | 3rd Base Umpire | 3루 라인을 담당하는 심판 | `umpire_3b_nm` (레거시: `UMP3`) | GAMEINFO |
| 기록원 A | Scorer A | 경기 공식 기록을 담당하는 기록원 (1인) | `scorer_a_nm` (레거시: `SCOA`) | GAMEINFO |
| 기록원 B | Scorer B | 경기 공식 기록을 담당하는 기록원 (2인) | `scorer_b_nm` (레거시: `SCOB`) | GAMEINFO |

### 3.3 경기 환경

| 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|---------|------------|
| 시작시간 | Start Time | 경기 시작 시각 (HHmm 형식) | `start_tm` (레거시: `STTM`) | GAMEINFO |
| 종료시간 | End Time | 경기 종료 시각 | `end_tm` (레거시: `ENTM`) | GAMEINFO |
| 지연시간 | Delay Time | 우천 등으로 중단된 시간 | `delay_tm` (레거시: `DLTM`) | GAMEINFO |
| 경기시간 | Game Duration | 경기 소요 시간 (분 단위) | `game_duration_tm` (레거시: `GMTM`) | GAMEINFO |
| 기온 | Temperature | 경기 시작 시점 기온 (×10 정수 저장, API에서 /10 변환) | `temperature_va` (레거시: `TEMP`) | GAMEINFO |
| 습도 | Humidity | 경기 시작 시점 습도 (%) | `humidity_va` (레거시: `MOIS`) | GAMEINFO |
| 날씨 | Weather | 경기 시 날씨 상태 (맑음/흐림/비 등) | `weather_cd` (레거시: `WEATH`) | GAMEINFO |
| 풍향 | Wind Direction | 바람이 부는 방향 (16방위 코드) | `wind_dir_cd` (레거시: `WIND`) | GAMEINFO |
| 풍속 | Wind Speed | 바람의 세기 (m/s) | `wind_speed_va` (레거시: `WINS`) | GAMEINFO |
| 구장 | Stadium | 경기가 열리는 야구장 | `stadium_cd` (레거시: `STAD`) | GAMEINFO |

---

## 4. 코드 체계 용어

| 용어 | 코드명 | 정의 | 값 예시 | DB 컬럼 |
|------|--------|------|---------|---------|
| 플레이 결과 | how_cd | 타석의 최종 결과를 나타내는 코드. 49종 | H1=싱글, HR=홈런, KK=삼진, GR=땅볼아웃 | `how_cd` |
| 타구 방향 | place_cd | 타구가 날아간 방향/포지션 번호 | 1=투수, 6=유격수, 78=좌중간 | `place_cd` |
| 포지션 | position_cd | 선수의 수비 위치. XY 2자리 형식 (X=교체순번, Y=포지션) | 01=투수(선발), 12=포수(1차교체) | `position_cd` |
| 투타 유형 | bat_throw_cd | 선수의 투구 손/타격 손 조합 | RR=우투우타, LL=좌투좌타, RS=우투양타 | `bat_throw_cd` |
| 경기 유형 | game_type_cd | 경기 종류 구분 | 0=정규시즌, 1=포스트시즌, 3=올스타전, 5=시범경기 | `game_type_cd` |
| 경기 상태 | game_sc_id | 경기 진행 상태 | 10=예정, 20=진행중, 70=종료, 80=취소 | `game_sc_id` |
| 취소 구분 | cancel_sc_id | 경기 취소/중단 사유 | 코드값 → 코드 사전 참조 | `cancel_sc_id` |
| 방송사 | broadcasting_cd | 경기를 중계하는 방송사 코드 | 0=비해당, 1=SBS, 2=KBS2, 8=SPOTV | `broad_cd` |
| 날씨 코드 | weather_cd | 경기 시 날씨 상태 코드 | F=맑음, C=흐림, R=비 | `weather_cd` |
| 기록 상태 | record_status_cd | 경기 기록의 처리 단계 | DRAFT→REVIEW→CONFIRMED→REVISED | `record_status_cd` |
| 구간 코드 | section_cd | 시즌 통계 집계 구간 (전반기/후반기/전체 등) | 코드값 → 코드 사전 참조 | `section_cd` |
| 그룹 구분 | group_sc | 그룹/조 구분 (가을리그 등) | 코드값 → 코드 사전 참조 | `group_sc` |

→ 참고: [코드 사전](../standards-dict/codes.md) - 각 코드의 전체 허용값 목록

---

## 5. 선수/팀 용어

| 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|---------|------------|
| 선수 코드 | Player Code | 선수를 고유하게 식별하는 코드 (5~6자리 숫자) | `player_id` (레거시: `PCODE`) | 전체 |
| 선수명 | Player Name | 선수의 한글 이름 | `player_nm` (레거시: `NAME`) | person |
| 영문명 | English Name | 선수의 영문 이름 | `player_eng_nm` (레거시: `ENGNAME`) | person |
| 한자명 | Chinese Name | 선수 이름의 한자 표기 | `player_hanja_nm` (레거시: `CNAME`) | person |
| 팀 코드 | Team Code | 팀을 식별하는 2자리 코드 (HH=키움, HT=KIA 등) | `team_id` (레거시: `T_ID`) | 전체 |
| 등번호 | Back Number | 선수 유니폼 뒷면의 번호 | `back_no` (레거시: `BACKNUM`) | person |
| 포지션 | Position | 선수의 주 수비 위치 (1=투수~9=우익수) | `position_cd` (레거시: `POS`) | person |
| 포지션명 | Position Name | 수비 위치의 한글 이름 (투수, 포수, 내야, 외야 등) | `position_nm` (레거시: `POSITION`) | person |
| 생년월일 | Birth Date | 선수의 생년월일 (YYYYMMDD) | `birth_dt` (레거시: `BIRTH`) | person |
| 키 | Height | 선수의 키 (cm) | `height_va` (레거시: `HEIGHT`) | person |
| 몸무게 | Weight | 선수의 체중 (kg) | `weight_va` (레거시: `WEIGHT`) | person |
| 입단일 | Join Date | 프로 구단에 입단한 날짜 | `join_dt` (레거시: `INDATE`) | person |
| 경력 | Career | 선수의 학교·팀 이력 (EUC-KR 인코딩) | `career_nm` (레거시: `CAREER`) | person |
| 드래프트 | Draft | 신인 드래프트 정보 | `draft_nm` (레거시: `DRAFT`) | person |
| 계약금 | Signing Bonus | 입단 계약금 (문자열, EUC-KR) | `signing_bonus_va` (레거시: `PROMISE`) | person |
| 연봉 | Salary | 연간 급여 (문자열, EUC-KR) | `salary_va` (레거시: `MONEY`) | person |

---

## 6. 시스템/실시간 용어

| 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블 |
|------|------|------|---------|------------|
| 등록 일시 | Registration DateTime | 데이터가 시스템에 등록된 시각 | `reg_dt` (레거시: `REG_DT`) | person, GAMEINFO |
| 입력 시각 | Input Time | 기록원이 데이터를 입력한 시각 | `input_dt` (레거시: `INPUTTIME`) | GAMECONTAPP |
| 순번 | Sequence Number | 동일 키 내에서 행을 구분하는 순차 번호 | `seq_no` (레거시: `SEQ_NO`, `SERNO`) | GAMECONTAPP, KBO_ETCGAME |
| 타순 | Batting Order | 경기에서 타석에 들어서는 순서 (1~9) | `turn_no` (레거시: `TURN`) | Hitter, ENTRY |
| 실시간 중계 | Live Text | 경기 중 문자로 전달되는 실시간 중계 텍스트 | `live_text` (레거시: `LIVETEXT`) | IE_LiveText |
| 텍스트 스타일 | Text Style | 중계 텍스트의 표시 유형 코드 (득점·교체·일반 등) | `text_style_cd` (레거시: `textStyle`) | IE_LiveText |
| 볼카운트 | Ball Count | 현재 타석의 볼-스트라이크-아웃 카운트 | `ball_count_cd` (레거시: `BCNT`) | IE_BallCount, GAMECONTAPP |
| 주자 상태 | Base Runner | 각 루에 주자 존재 여부 또는 선수 코드 | `base1b`~`base3a` | GAMECONTAPP, IE_BallCount |
| 피치클럭 | Pitch Clock | 투수의 투구 준비 시간 제한 (초) | - | PITCHCLOCK |
| 경기 상태 | Game State | 현재 경기의 진행 상태 (예정/진행중/종료 등) | `game_sc_id` (레거시: `STATUS_ID`) | IE_GAMESTATE |

---

## 7. 데이터 품질 용어

| 용어 | 정의 |
|------|------|
| EUC-KR 인코딩 | 레거시 시스템에서 한글을 저장하는 문자 인코딩. varchar 컬럼에 저장된 한글이 nvarchar 환경에서 깨져 보이는 원인. 표준은 nvarchar(UTF-16) |
| NULL vs 0 구분 | 비율 컬럼에서 NULL=분모 없음(타석 0), 0.000=분모 있으나 분자 0(타석 있지만 안타 0). 의미가 다름 |
| -1 센티널 | Score 테이블의 이닝 점수에서 -1=해당 이닝 미진행. NULL 대신 정수 센티널 사용 |
| 9999 예약값 | GYEAR(시즌 연도)에서 9999=통산(Career Total) 기록을 나타내는 예약값 |
| T/B 합계행 | Hitter/Pitcher 등에서 PCODE='T' 또는 'B'인 행은 개인 기록이 아닌 팀 합계. 원정/홈 구분 |
| 레거시/신세대 공존 | 동일 DB에 구세대 스키마(GMKEY/PCODE)와 신세대 스키마(G_ID/P_ID/_CD/_CN 접미사)가 혼재 |
| varchar 숫자 ID | PCODE는 varchar(10)이지만 실제 값은 5~6자리 숫자. 표준에서는 int로 전환 권고 |
| 이닝 피벗 컬럼 | Score, KBO_BATRESULT 테이블에서 이닝 1~25까지 컬럼이 가로로 펼쳐진 구조 (1T, 1B, 2T, ...) |

---

## 부록: 용어 색인 (가나다순)

| 용어 | 섹션 |
|------|------|
| -1 센티널 | 7 |
| 9999 예약값 | 7 |
| EUC-KR 인코딩 | 7 |
| BABIP | 2.4 |
| OPS | 2.4 |
| QS | 2.2 |
| WHIP | 2.4 |
| wRC | 2.4 |
| 가중득점생산 | 2.4 |
| 관중수 | 3.1 |
| 경기 상태 | 6 |
| 경기 요일 | 3.1 |
| 경기시간 | 3.3 |
| 경기수 | 3.1 |
| 경기키 | 3.1 |
| 경기일자 | 3.1 |
| 경력 | 5 |
| 계약금 | 5 |
| 고의사구 | 2.1 |
| 구간 | 3.1 |
| 구간 코드 | 4 |
| 구장 | 3.3 |
| 기록 상태 | 4 |
| 기록원 | 3.2 |
| 기온 | 3.3 |
| 날씨 | 3.3 |
| 날씨 코드 | 4 |
| 등록 일시 | 6 |
| 등번호 | 5 |
| 더블헤더 | 3.1 |
| 도루 | 2.1 |
| 도루 성공률 | 2.4 |
| 도루실패 | 2.1 |
| 드래프트 | 5 |
| 루타 | 2.1 |
| 땅볼아웃 | 2.3 |
| 몸무게 | 5 |
| 방송사 | 4 |
| 병살 | 2.3 |
| 병살타 | 2.1 |
| 보살 | 2.3 |
| 보크 | 2.2 |
| 볼넷 | 2.1 |
| 볼카운트 | 6 |
| 블론세이브 | 2.2 |
| 사구 | 2.1 |
| 삼진 | 2.1 |
| 삼진/볼넷 비율 | 2.4 |
| 상대타자수 | 2.2 |
| 생년월일 | 5 |
| 선발 | 2.2 |
| 선수 코드 | 5 |
| 선수명 | 5 |
| 세이브 | 2.2 |
| 순번 | 6 |
| 순장타율 | 2.4 |
| 승리 | 2.2 |
| 승패세 | 2.2 |
| 시작시간 | 3.3 |
| 시즌 연도 | 3.1 |
| 실점 | 2.2 |
| 실시간 중계 | 6 |
| 실책 | 2.1 |
| 안타 | 2.1 |
| 아웃카운트 | 3.1 |
| 영문명 | 5 |
| 연봉 | 5 |
| 완봉 | 2.2 |
| 완투 | 2.2 |
| 원정/홈 | 3.1 |
| 이닝 | 2.2 |
| 이닝 피벗 컬럼 | 7 |
| 입단일 | 5 |
| 입력 시각 | 6 |
| 자살 | 2.3 |
| 자책점 | 2.2 |
| 잔루 | 2.1 |
| 장타 | 2.1 |
| 장타율 | 2.4 |
| 종료시간 | 3.3 |
| 주심 | 3.2 |
| 주자 상태 | 6 |
| 지연시간 | 3.3 |
| 차전 | 3.1 |
| 초/말 | 3.1 |
| 출루율 | 2.4 |
| 취소 구분 | 4 |
| 키 | 5 |
| 타격 방향 | 5 |
| 타석 | 2.1 |
| 타수 | 2.1 |
| 타순 | 6 |
| 타율 | 2.4 |
| 타점 | 2.1 |
| 텍스트 스타일 | 6 |
| 투구수 | 2.2 |
| 팀 코드 | 5 |
| 패배 | 2.2 |
| 평균자책점 | 2.4 |
| 포지션 | 5 |
| 포일 | 2.2 |
| 폭투 | 2.2 |
| 플라이아웃 | 2.3 |
| 플레이 결과 | 4 |
| 피OPS | 2.4 |
| 피안타율 | 2.4 |
| 피장타율 | 2.4 |
| 피출루율 | 2.4 |
| 피치클럭 | 6 |
| 한자명 | 5 |
| 홀드 | 2.2 |
| 홈런 | 2.1 |
| 희생번트 | 2.1 |
| 희생플라이 | 2.1 |
| 습도 | 3.3 |
| 풍속 | 3.3 |
| 풍향 | 3.3 |
| 견제사 | 2.3 |
