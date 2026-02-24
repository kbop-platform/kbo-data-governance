# 표준 약어 사전

> 최종수정: 2026-02-24 | 출처: analysis/naming-patterns.md, scripts/upgrade-dictionary.py

## 1. 개요

KBO 데이터 시스템에서 사용하는 모든 약어를 정의한다.
40종 테이블, 787개 컬럼에서 추출한 약어를 카테고리별로 분류하고, 레거시명과 표준명(안)의 대응 관계를 명시한다.

- 야구 기록 약어는 **국제 표준**을 우선 적용한다 (MLB/KBO 공식 기록 기준).
- KBO 시스템 고유 약어는 Section 7에 별도 정리한다.
- 컬럼 접미사 규칙은 Section 6에서 다룬다.

→ 참고: [명명 규칙](./naming-rules.md) — 약어와 접미사를 조합한 컬럼 네이밍 규칙
→ 참고: [도메인 타입 정의](./domain-types.md) — 접미사별 데이터 타입 매핑

---

## 2. 식별자 약어

| 약어 | 영문 풀네임 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|-----------|------|-----------|-----------|
| GM | Game | 경기 | GMKEY | game_id |
| G | Game | 경기 | G_ID, GDAY, GYEAR | game_id, game_dt, season_yr |
| P | Player | 선수 | PCODE, P_ID | player_id |
| T | Team | 팀 | T_ID | team_id |
| S | Stadium / Season / Series | 구장/시즌/시리즈 | S_NM, SEASON_ID, SR_ID | stadium_nm, season_id, series_id |
| LE | League | 리그 | LE_ID | league_id |
| SR | Series | 시리즈 | SR_ID | series_id |

---

## 3. 야구 기록 약어

### 3.1 타격 (Batting)

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| PA | Plate Appearance | 타석 | PA, PA_CN | pa, pa_cn |
| AB | At Bat | 타수 | AB, AB_CN | ab, ab_cn |
| HIT | Hit | 안타 | HIT, HIT_CN | hit, hit_cn |
| H1 | Single | 1루타 | H1 | h1b |
| H2 | Double | 2루타 | H2, H2_CN | h2b, h2b_cn |
| H3 | Triple | 3루타 | H3, H3_CN | h3b, h3b_cn |
| HR | Home Run | 홈런 | HR, HR_CN | hr, hr_cn |
| RBI | Runs Batted In | 타점 | RBI, RBI_CN | rbi, rbi_cn |
| RUN | Run Scored | 득점 | RUN, RUN_CN | run, run_cn |
| BB | Base on Balls | 볼넷 | BB, BB_CN | bb, bb_cn |
| HBP | Hit by Pitch | 사구 | **HP**, HP_CN | hbp, hbp_cn |
| IBB | Intentional Walk | 고의사구 | **IB**, IB_CN | ibb, ibb_cn |
| SO | Strikeout | 삼진 | **KK**, KK_CN | so, so_cn |
| SB | Stolen Base | 도루 | SB, SB_CN | sb, sb_cn |
| CS | Caught Stealing | 도루실패 | CS, CS_CN | cs, cs_cn |
| SH | Sacrifice Hit | 희생번트 | SH, SH_CN | sh, sh_cn |
| SF | Sacrifice Fly | 희생플라이 | SF, SF_CN | sf, sf_cn |
| GIDP | Grounded into DP | 병살타 | **GD**, GD_CN | gidp, gidp_cn |
| ERR | Error | 실책 | ERR, ERR_CN | err, err_cn |
| LOB | Left on Base | 잔루 | LOB | lob |
| TB | Total Bases | 루타 | TB (int) | tb_cn |
| XBH | Extra Base Hit | 장타 | XBH_CN | xbh_cn |

> **주의**: TB는 이중 의미. 루타(int)일 때 `tb_cn`, 팀구분(char T/B)일 때 `top_bottom_cd`. → Section 7 참고.

### 3.2 타격 비율 (Batting Rates)

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| AVG | Batting Average | 타율 | **HRA**, HRA_RT | avg, avg_rt |
| OBP | On-Base Percentage | 출루율 | OBP_RT | obp_rt |
| SLG | Slugging Percentage | 장타율 | SLG_RT | slg_rt |
| OPS | OBP + SLG | OPS | OPS_RT | ops_rt |
| ISO | Isolated Power | 순장타율 | ISO_RT | iso_rt |
| BABIP | Batting Avg on Balls in Play | BABIP | BABIP_RT | babip_rt |
| SB% | Stolen Base Percentage | 도루 성공률 | SB_RT | sb_rt |

### 3.3 투수 (Pitching)

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| IP | Innings Pitched | 이닝 | **INN**, INN2_CN | ip, ip_cn |
| BF | Batters Faced | 상대타자수 | BF | bf |
| W | Win | 승리 | W, W_CN | win, win_cn |
| L | Loss | 패배 | L, L_CN | loss, loss_cn |
| SV | Save | 세이브 | SV, SV_CN | sv, sv_cn |
| HLD | Hold | 홀드 | HOLD, HOLD_CN | hld, hld_cn |
| BS | Blown Save | 블론세이브 | BS, BS_CN | bs, bs_cn |
| CG | Complete Game | 완투 | CG, CG_CN | cg, cg_cn |
| SHO | Shutout | 완봉 | SHO, SHO_CN | sho, sho_cn |
| ER | Earned Run | 자책점 | ER, ER_CN | er, er_cn |
| ERA | Earned Run Average | 평균자책점 | ERA, ERA_RT | era, era_rt |
| WP | Wild Pitch | 폭투 | WP, WP_CN | wp, wp_cn |
| BK | Balk | 보크 | BK, BK_CN | bk, bk_cn |
| PB | Passed Ball | 포일 | PB | pb |
| WLS | Win/Loss/Save | 승패세 | WLS | wls_cd |
| QS | Quality Start | QS | QS_CN | qs_cn |
| R | Runs Allowed | 실점 | R, R_CN | runs_cn |
| NP | Number of Pitches | 투구수 | PIT_CN | pitch_cn |
| START | Start (Game) | 선발 출장 | START, START_CN | start_if, start_cn |

### 3.4 투수 비율 (Pitching Rates)

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| ERA | Earned Run Average | 평균자책점 | ERA_RT | era_rt |
| WHIP | Walks+Hits per IP | WHIP | WHIP_RT | whip_rt |
| K/BB | Strikeout-to-Walk Ratio | 삼진/볼넷 비율 | KK_BB_RT | so_bb_rt |
| BB/K | Walk-to-Strikeout Ratio | 볼넷/삼진 비율 | BB_KK_RT | bb_so_rt |
| FO/GO | Fly Out / Ground Out | 플라이/땅볼 비율 | FOGO_RT | fo_go_rt |
| OAVG | Opponent Batting Average | 피안타율 | OAVG_RT | opp_avg_rt |
| OOBP | Opponent OBP | 피출루율 | OOBP_RT | opp_obp_rt |
| OSLG | Opponent SLG | 피장타율 | OSLG_RT | opp_slg_rt |
| OOPS | Opponent OPS | 피OPS | OOPS_RT | opp_ops_rt |
| wRC | Weighted Runs Created | 가중득점생산 | WRA, WRA_RT | wrc, wrc_rt |

### 3.5 수비 (Fielding)

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| PO | Put Out | 자살(刺殺) | PO | po |
| AST | Assist | 보살(補殺) | **ASS** | ast |
| DP | Double Play | 병살 | DP | dp |
| POFF | Pickoff | 견제사 | POFF_CN | poff_cn |
| FO | Fly Out | 플라이아웃 | FO_CN | fo_cn |
| GO | Ground Out | 땅볼아웃 | GO_CN | go_cn |

---

## 4. 경기 정보 약어

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| STTM | Start Time | 시작시간 | STTM, START_TM | start_tm |
| ENTM | End Time | 종료시간 | ENTM, END_TM | end_tm |
| DLTM | Delay Time | 지연시간 | DLTM | delay_tm |
| GMTM | Game Time | 경기시간(분) | GMTM | game_duration_tm |
| STAD | Stadium Code | 구장코드 | STAD | stadium_cd |
| UMPC | Umpire Chief | 주심 | UMPC | umpire_chief_nm |
| UMP1 | Umpire 1st Base | 1루심 | UMP1 | umpire_1b_nm |
| UMP2 | Umpire 2nd Base | 2루심 | UMP2 | umpire_2b_nm |
| UMP3 | Umpire 3rd Base | 3루심 | UMP3 | umpire_3b_nm |
| SCOA | Scorer A | 기록원 A | SCOA | scorer_a_nm |
| SCOB | Scorer B | 기록원 B | SCOB | scorer_b_nm |
| TEMP | Temperature | 기온 (×10 정수) | TEMP | temperature_va |
| MOIS | Moisture | 습도 (%) | MOIS | humidity_va |
| WEATH | Weather | 날씨 코드 | WEATH | weather_cd |
| WIND | Wind Direction | 풍향 | WIND | wind_dir_cd |
| WINS | Wind Speed | 풍속 (m/s) | WINS | wind_speed_va |
| CROWD | Crowd | 관중수 | CROWD, CROWD_CN | crowd_cn |
| DBHD | Doubleheader | 더블헤더 번호 | DBHD | doubleheader_no |
| CHAJUN | Round | 차전(라운드) | CHAJUN | round_no |

---

## 5. 시스템/운영 약어

| 약어 | 영문 | 한글 | 레거시 컬럼 | 표준명(안) |
|------|------|------|-----------|-----------|
| REG_DT | Registration DateTime | 등록 일시 | REG_DT | reg_dt |
| RECORD_DT | Record DateTime | 기록 시점 | RECORD_DT | record_dt |
| SEQ / SERNO | Sequence Number | 순번 | SERNO, SEQ, SEQ_NO | seq_no |
| TURN | Batting Turn | 타순+교체순번 | TURN | turn_no |
| ONETURN | One Turn | 타석별 고유 순번 | ONETURN | one_turn_no |
| BAT_ORDER | Batting Order | 타순 | BAT_ORDER_NO | bat_order_no |
| POSI | Position (encoded) | 포지션 (XY 형식) | POSI | position_cd |
| HOW | How (Play Result) | 플레이 결과 코드 | HOW | how_cd |
| PLACE | Place (Direction) | 타구 방향 | PLACE, PLACE_SC | place_cd, place_sc |
| BCNT | Ball Count | 볼카운트 | BCNT, BCOUNT | ball_count_cd |
| BROAD_CD | Broadcasting Code | 방송사 코드 | BROAD_CD | broad_cd |
| SECTION_CD | Section Code | 구간 코드 | SECTION_CD | section_cd |
| GROUP_SC | Group Sub Code | 그룹 구분 | GROUP_SC | group_sc |
| CANCEL_SC | Cancel Sub Code | 취소 구분 | CANCEL_SC_ID | cancel_sc_id |
| GAME_SC | Game Status Code | 경기 상태 | GAME_SC_ID | game_sc_id |

### 테이블 접두사

| 접두사 | 의미 | 영문 | 해당 테이블 수 |
|--------|------|------|--------------|
| IE_ | Input/Entry | 기록입력 시스템 | 9종 |
| KBO_ | KBO Official | KBO 공식 데이터 | 4종 |
| GAME_ | Game | 경기 관련 | 5종 |
| SEASON_ | Season | 시즌 통계 | 6종 |
| CANCEL_ | Cancel | 취소 관련 | 1종 |
| FALL_LEAGUE_ | Fall League | 가을리그 | 1종 |

---

## 6. 접미사 규칙

신세대 스키마에서 컬럼명 끝에 붙는 접미사로, 데이터의 **성격(도메인 타입)**을 나타낸다.

| 접미사 | 의미 | 영문 | MSSQL 타입 | 예시 컬럼 |
|--------|------|------|-----------|----------|
| `_id` | 식별자 | Identifier | varchar/int | game_id, player_id, team_id |
| `_nm` | 이름 | Name | nvarchar | player_nm, stadium_nm |
| `_cd` | 코드 | Code | varchar | team_cd, weather_cd, how_cd |
| `_sc` | 구분코드 | Sub Code | varchar | top_bottom_sc, place_sc |
| `_cn` | 수량/건수 | Count | int | pa_cn, hr_cn, crowd_cn |
| `_rt` | 비율 | Rate | decimal | avg_rt, era_rt, obp_rt |
| `_if` | 플래그(Y/N) | Flag | bit | group_if, cancel_if |
| `_dt` | 일시 | DateTime | datetime2 | reg_dt, game_dt |
| `_tm` | 시간 | Time | char(4)/int | start_tm, end_tm, game_duration_tm |
| `_va` | 값 | Value | int/decimal | temperature_va, hr_distance_va |
| `_no` | 번호 | Number | int | seq_no, inning_no, bat_order_no |

### 접미사 생략 규칙

경기 단위(play-by-play) 테이블의 **야구 기록 약어**는 접미사 없이 사용한다:
- `pa`, `ab`, `hit`, `hr`, `rbi`, `bb`, `so`, `sb` 등

시즌 집계(SEASON_PLAYER_*) 테이블에서는 `_cn` 접미사를 붙인다:
- `pa_cn`, `ab_cn`, `hit_cn`, `hr_cn` 등

비율/평균은 항상 `_rt` 접미사를 사용한다:
- `avg_rt`, `era_rt`, `obp_rt`, `slg_rt`

→ 참고: [도메인 타입 정의](./domain-types.md) — 접미사별 MSSQL 타입 상세 매핑

---

## 7. KBO 비표준 약어 주의사항

KBO 레거시 시스템(Sports2i)에서 국제 표준과 다르게 사용하는 약어. 표준명(안)은 국제 표준 기준으로 정의했다.

| KBO 레거시 | 국제 표준 | 표준명(안) | 한글 | 비고 |
|-----------|----------|-----------|------|------|
| `KK` | SO (Strikeout) | `so` | 삼진 | K/SO가 국제 표준 |
| `HP` | HBP (Hit by Pitch) | `hbp` | 사구 | |
| `IB` | IBB (Intentional BB) | `ibb` | 고의사구 | |
| `HRA` | AVG / BA | `avg` | 타율 | HRA는 KBO 고유. 국제적으로 HR Average와 혼동 |
| `GD` | GIDP | `gidp` | 병살타 | Grounded into Double Play |
| `ASS` | AST (Assist) | `ast` | 보살 | S2i 고유 약어 |
| `INN` | IP (Innings Pitched) | `ip` | 이닝 | IP가 국제 표준 |
| `WRA` | wRC (Weighted Runs Created) | `wrc` | 가중득점생산 | |
| `BRA` | BA (Batting Average) | `bat_avg` | 팀 타율 | 확인 필요 |
| `LRA` | — | `left_avg` | 좌타자 타율? | 의미 확인 필요 |

### 이중 의미 약어

| 약어 | 의미 1 | 의미 2 | 구분 방법 |
|------|--------|--------|----------|
| `TB` | Total Bases (루타, int) | Top/Bottom (팀구분, char) | 타입으로 구분: int=루타, char(1)=팀구분 |
| | 표준: `tb_cn` | 표준: `top_bottom_cd` / `top_bottom_sc` | |
| `R` | Runs Allowed (실점) | Runs Scored (득점) | 맥락으로 구분: 투수=실점, Score=실점행 |
| | 표준: `runs_cn` | | |
| `INN` | Innings Pitched (투구 이닝) | Inning Score (이닝별 점수) | INN 단독=투구, INN1~INN25=이닝 점수 |
| | 표준: `ip` | 표준: `inn_{N}_score` | |

---

## 부록 A: 전체 약어 알파벳순 색인

| 약어 | 분류 | 한글 | 참조 |
|------|------|------|------|
| AB | 타격 | 타수 | 3.1 |
| ASS/AST | 수비 | 보살 | 3.5, 7 |
| AVG (HRA) | 타격비율 | 타율 | 3.2, 7 |
| BABIP | 타격비율 | BABIP | 3.2 |
| BB | 타격 | 볼넷 | 3.1 |
| BF | 투수 | 상대타자수 | 3.3 |
| BK | 투수 | 보크 | 3.3 |
| BROAD_CD | 시스템 | 방송사코드 | 5 |
| BS | 투수 | 블론세이브 | 3.3 |
| CG | 투수 | 완투 | 3.3 |
| CHAJUN | 경기 | 차전 | 4 |
| CROWD | 경기 | 관중수 | 4 |
| CS | 타격 | 도루실패 | 3.1 |
| DBHD | 경기 | 더블헤더 | 4 |
| DLTM | 경기 | 지연시간 | 4 |
| DP | 수비 | 병살 | 3.5 |
| ENTM | 경기 | 종료시간 | 4 |
| ER | 투수 | 자책점 | 3.3 |
| ERA | 투수비율 | 평균자책점 | 3.4 |
| ERR | 타격 | 실책 | 3.1 |
| FO/GO | 투수비율 | 플라이/땅볼 | 3.4 |
| G / GM | 식별자 | 경기 | 2 |
| GD/GIDP | 타격 | 병살타 | 3.1, 7 |
| GMTM | 경기 | 경기시간 | 4 |
| H1 | 타격 | 1루타 | 3.1 |
| H2 | 타격 | 2루타 | 3.1 |
| H3 | 타격 | 3루타 | 3.1 |
| HBP (HP) | 타격 | 사구 | 3.1, 7 |
| HIT | 타격 | 안타 | 3.1 |
| HLD | 투수 | 홀드 | 3.3 |
| HOW | 시스템 | 플레이결과 | 5 |
| HR | 타격 | 홈런 | 3.1 |
| HRA → AVG | 타격비율 | 타율 | 3.2, 7 |
| IBB (IB) | 타격 | 고의사구 | 3.1, 7 |
| INN → IP | 투수 | 이닝 | 3.3, 7 |
| ISO | 타격비율 | 순장타율 | 3.2 |
| KK → SO | 타격 | 삼진 | 3.1, 7 |
| L | 투수 | 패배 | 3.3 |
| LE | 식별자 | 리그 | 2 |
| LOB | 타격 | 잔루 | 3.1 |
| MOIS | 경기 | 습도 | 4 |
| OBP | 타격비율 | 출루율 | 3.2 |
| OPS | 타격비율 | OPS | 3.2 |
| P | 식별자 | 선수 | 2 |
| PA | 타격 | 타석 | 3.1 |
| PB | 투수 | 포일 | 3.3 |
| PLACE | 시스템 | 타구방향 | 5 |
| PO | 수비 | 자살 | 3.5 |
| POFF | 수비 | 견제사 | 3.5 |
| POSI | 시스템 | 포지션 | 5 |
| QS | 투수 | QS | 3.3 |
| R | 투수 | 실점 | 3.3 |
| RBI | 타격 | 타점 | 3.1 |
| RUN | 타격 | 득점 | 3.1 |
| S | 식별자 | 구장/시즌 | 2 |
| SB | 타격 | 도루 | 3.1 |
| SCOA/B | 경기 | 기록원 | 4 |
| SF | 타격 | 희생플라이 | 3.1 |
| SH | 타격 | 희생번트 | 3.1 |
| SHO | 투수 | 완봉 | 3.3 |
| SLG | 타격비율 | 장타율 | 3.2 |
| SO (KK) | 타격 | 삼진 | 3.1, 7 |
| SR | 식별자 | 시리즈 | 2 |
| STAD | 경기 | 구장코드 | 4 |
| STTM | 경기 | 시작시간 | 4 |
| SV | 투수 | 세이브 | 3.3 |
| T | 식별자 | 팀 | 2 |
| TB | 타격/이중 | 루타/팀구분 | 3.1, 7 |
| TEMP | 경기 | 기온 | 4 |
| UMPC | 경기 | 주심 | 4 |
| W | 투수 | 승리 | 3.3 |
| WEATH | 경기 | 날씨 | 4 |
| WHIP | 투수비율 | WHIP | 3.4 |
| WIND | 경기 | 풍향 | 4 |
| WINS | 경기 | 풍속 | 4 |
| WLS | 투수 | 승패세 | 3.3 |
| WP | 투수 | 폭투 | 3.3 |
| wRC (WRA) | 투수비율 | 가중득점생산 | 3.4, 7 |
| XBH | 타격 | 장타 | 3.1 |
