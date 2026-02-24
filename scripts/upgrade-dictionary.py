#!/usr/bin/env python3
"""
dictionary/ 파일 일괄 업그레이드:
  1) 버전 태그 추가 (최종수정, 출처)
  2) 컬럼 상세 테이블에 '표준명(안)' 컬럼 추가
"""
import os, re, glob
from datetime import date

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICT_DIR = os.path.join(BASE, "dictionary")
TODAY = date.today().strftime("%Y-%m-%d")

# ──────────────────────────────────────────────────────────
# 표준명 매핑: 레거시 컬럼명 → snake_case 표준명(안)
# 규칙:
#   - 식별자: _id 접미사
#   - 이름:   _nm 접미사
#   - 코드:   _cd 접미사
#   - 수량:   _cn 접미사
#   - 비율:   _rt 접미사
#   - 일시:   _dt 접미사
#   - 시간:   _tm 접미사
#   - 플래그: _if 접미사
#   - 야구 통계 약어: 국제 표준 유지 (소문자)
# ──────────────────────────────────────────────────────────

STANDARD_MAP = {
    # === 식별자 (ID) ===
    "GMKEY":    "game_id",
    "gameID":   "game_id",
    "GAMEID":   "game_id",
    "gmkey":    "game_id",
    "G_ID":     "game_id",
    "PCODE":    "player_id",
    "P_ID":     "player_id",
    "PlayerID": "player_id",
    "T_ID":     "team_id",
    "LE_ID":    "league_id",
    "SR_ID":    "series_id",
    "SEASON_ID":"season_id",
    "STATUS_ID":"status_id",
    "GAME_SC_ID": "game_sc_id",
    "CANCEL_SC_ID": "cancel_sc_id",
    "REQ_T_ID": "req_team_id",
    "BAT_P_ID": "bat_player_id",
    "PIT_P_ID": "pit_player_id",

    # === 시즌/날짜/시간 ===
    "GYEAR":    "season_yr",
    "gyear":    "season_yr",
    "GDAY":     "game_dt",
    "gday":     "game_dt",
    "gamedate": "game_dt",
    "gmonth":   "game_mon",
    "STTM":     "start_tm",
    "START_TM": "start_tm",
    "ENTM":     "end_tm",
    "END_TM":   "end_tm",
    "DLTM":     "delay_tm",
    "GMTM":     "game_duration_tm",
    "USE_TM":   "use_tm",
    "gtime":    "game_tm",
    "INPUTTIME":"input_tm",
    "InsertedTime": "inserted_tm",
    "REG_DT":   "reg_dt",
    "RECORD_DT":"record_dt",
    "G_DT":     "game_dt",
    "G_TM":     "game_tm",
    "INDATE":   "join_dt",

    # === 팀 ===
    "TEAM":     "team_cd",
    "Team":     "team_cd",
    "HTEAM":    "home_team_cd",
    "VTEAM":    "away_team_cd",
    "home":     "home_team_cd",
    "visit":    "away_team_cd",
    "home_key": "home_team_id",
    "visit_key":"away_team_id",
    "HomeName": "home_team_nm",
    "VisitName":"away_team_nm",
    "HomeMascot":"home_mascot_nm",
    "VisitMascot":"away_mascot_nm",

    # === 구장/날씨 ===
    "STADIUM":  "stadium_nm",
    "stadium":  "stadium_nm",
    "STAD":     "stadium_cd",
    "stadium_key": "stadium_id",
    "TEMP":     "temperature_va",
    "temp":     "temperature_va",
    "MOIS":     "humidity_va",
    "humi":     "humidity_va",
    "WEATH":    "weather_cd",
    "WIND":     "wind_dir_cd",
    "WINS":     "wind_speed_va",
    "wspeed":   "wind_speed_va",
    "wdirk":    "wind_dir_cd",
    "rain":     "rain_if",
    "snow":     "snow_if",
    "CROWD":    "crowd_cn",
    "CROWD_CN": "crowd_cn",

    # === 심판/기록원 ===
    "UMPC":     "umpire_chief_nm",
    "UMP1":     "umpire_1b_nm",
    "UMP2":     "umpire_2b_nm",
    "UMP3":     "umpire_3b_nm",
    "UMPL":     "umpire_lf_nm",
    "UMPR":     "umpire_rf_nm",
    "SCOA":     "scorer_a_nm",
    "SCOB":     "scorer_b_nm",

    # === 경기 메타 ===
    "DBHD":     "doubleheader_no",
    "dheader":  "doubleheader_no",
    "CHAJUN":   "round_no",
    "SEC":      "series_cd",
    "SECTION_CD":"section_cd",
    "LEAGUE":   "league_cd",
    "GAMENUM":  "game_no",
    "GAME_CN":  "game_cn",

    # === 선수 인적 ===
    "NAME":     "player_nm",
    "PlayerName":"player_nm",
    "ENGNAME":  "player_eng_nm",
    "FIRST_NM": "first_nm",
    "LAST_NM":  "last_nm",
    "FIRST_ENG_NM":"first_eng_nm",
    "LAST_ENG_NM": "last_eng_nm",
    "CNAME":    "player_hanja_nm",
    "BIRTH":    "birth_dt",
    "HEIGHT":   "height_va",
    "WEIGHT":   "weight_va",
    "BACKNUM":  "back_no",
    "POS":      "position_cd",
    "POSITION": "position_nm",
    "Position": "position_nm",
    "PositionName":"position_nm",
    "POSI":     "position_cd",
    "HITTYPE":  "bat_throw_cd",
    "CAREER":   "career_nm",
    "DRAFT":    "draft_nm",
    "PROMISE":  "signing_bonus_va",
    "MONEY":    "salary_va",

    # === 엔트리/라인업 ===
    "BatOrder":  "bat_order_no",
    "BAT_ORDER_NO":"bat_order_no",
    "ORDER_NO": "order_no",
    "TURN":     "turn_no",
    "RTURN":    "real_turn_no",
    "CHTURN":   "change_turn_no",
    "ONETURN":  "one_turn_if",
    "CHANGEINN":"change_inn_no",

    # === 투구/타격 이벤트 ===
    "HOW":      "how_cd",
    "PLACE":    "place_cd",
    "PLACE_SC": "place_sc",
    "DIREC_SC": "direc_sc",
    "TB":       "top_bottom_cd",
    "TB_SC":    "top_bottom_sc",
    "bTop":     "top_bottom_cd",
    "FIELD":    "field_cd",
    "DETAIL":   "detail_nm",
    "BCNT":     "ball_count_cd",
    "BCOUNT":   "ball_count_cd",
    "CHBCNT":   "change_ball_count_cd",
    "RESULT":   "result_cd",
    "batResult":"bat_result_cd",
    "PIT_RESULT_SC":"pit_result_sc",
    "RUNNER":   "runner_cd",
    "OPTION":   "option_cd",
    "CATCHER":  "catcher_id",
    "CATNAME":  "catcher_nm",
    "batter":   "batter_id",
    "pitcher":  "pitcher_id",
    "HITTER":   "hitter_nm",
    "HITNAME":  "hitter_nm",
    "PITCHER":  "pitcher_nm",
    "PITNAME":  "pitcher_nm",

    # === 볼카운트 ===
    "ball":     "ball_cn",
    "strike":   "strike_cn",
    "out":      "out_cn",
    "BallFour": "ball_four_if",
    "PitchBallCnt": "pitch_ball_cn",
    "PitchStrikeCnt":"pitch_strike_cn",
    "PITCHCLOCK":"pitch_clock_cd",

    # === 주자 ===
    "base1":    "base_1b_id",
    "base2":    "base_2b_id",
    "base3":    "base_3b_id",
    "BASE1A":   "base_1b_after_id",
    "BASE2A":   "base_2b_after_id",
    "BASE3A":   "base_3b_after_id",
    "BASE1B":   "base_1b_before_id",
    "BASE2B":   "base_2b_before_id",
    "BASE3B":   "base_3b_before_id",

    # === 이닝 점수 ===
    "inning":   "inning_no",
    "Inning":   "inning_no",
    "INN_NO":   "inning_no",
    "CHIN":     "change_inning_no",
    "CHIN2":    "change_inning2_no",
    "bHome":    "home_if",

    # === 순번/시퀀스 ===
    "SERNO":    "seq_no",
    "SEQ":      "seq_no",
    "SEQ_NO":   "seq_no",
    "SeqNO":    "seq_no",

    # === 타자 기록 통계 (국제 약어 유지) ===
    "PA":       "pa",
    "PA_CN":    "pa_cn",
    "AB":       "ab",
    "AB_CN":    "ab_cn",
    "HIT":      "hit",
    "Hit":      "hit",
    "HIT_CN":   "hit_cn",
    "H1":       "h1b",
    "H2":       "h2b",
    "H2_CN":    "h2b_cn",
    "H3":       "h3b",
    "H3_CN":    "h3b_cn",
    "HR":       "hr",
    "HR_CN":    "hr_cn",
    "HR_DISTANCE_VA":"hr_distance_va",
    "RBI":      "rbi",
    "RBI_CN":   "rbi_cn",
    "RUN":      "run",
    "Run":      "run",
    "RUN_CN":   "run_cn",
    "BB":       "bb",
    "BB_CN":    "bb_cn",
    "HP":       "hbp",
    "HP_CN":    "hbp_cn",
    "HBP":      "hbp",
    "IB":       "ibb",
    "IB_CN":    "ibb_cn",
    "KK":       "so",
    "KK_CN":    "so_cn",
    "SO":       "so",
    "SB":       "sb",
    "SB_CN":    "sb_cn",
    "SB_RT":    "sb_rt",
    "CS":       "cs",
    "CS_CN":    "cs_cn",
    "Steal":    "sb",
    "SH":       "sh",
    "SH_CN":    "sh_cn",
    "SF":       "sf",
    "SF_CN":    "sf_cn",
    "GD":       "gidp",
    "GD_CN":    "gidp_cn",
    "ERR":      "err",
    "ERR_CN":   "err_cn",
    "Error":    "err",
    "LOB":      "lob",
    "DP":       "dp",

    # === 타율/비율 통계 ===
    "HRA":      "avg",
    "HRA_RT":   "avg_rt",
    "OBP_RT":   "obp_rt",
    "SLG_RT":   "slg_rt",
    "OPS_RT":   "ops_rt",
    "ISO_RT":   "iso_rt",
    "BABIP_RT": "babip_rt",
    "WRA":      "wrc",
    "WRA_RT":   "wrc_rt",
    "BRA":      "bat_avg",
    "LRA":      "left_avg",
    "PH_HRA_RT":"pinch_avg_rt",
    "SP_HRA_RT":"vs_sp_avg_rt",
    "OAVG_RT":  "opp_avg_rt",
    "OOBP_RT":  "opp_obp_rt",
    "OOPS_RT":  "opp_ops_rt",
    "OSLG_RT":  "opp_slg_rt",

    # === 투수 기록 통계 ===
    "INN":      "ip",
    "INN2_CN":  "ip_cn",
    "BF":       "bf",
    "ER":       "er",
    "ER_CN":    "er_cn",
    "ERA":      "era",
    "ERA_RT":   "era_rt",
    "WHIP_RT":  "whip_rt",
    "CG":       "cg",
    "CG_CN":    "cg_cn",
    "SHO":      "sho",
    "SHO_CN":   "sho_cn",
    "WP":       "wp",
    "WP_CN":    "wp_cn",
    "BK":       "bk",
    "BK_CN":    "bk_cn",
    "PB":       "pb",
    "W":        "win",
    "W_CN":     "win_cn",
    "L":        "loss",
    "L_CN":     "loss_cn",
    "SV":       "sv",
    "SV_CN":    "sv_cn",
    "HOLD":     "hld",
    "Hold":     "hld",
    "HOLD_CN":  "hld_cn",
    "BS":       "bs",
    "BS_CN":    "bs_cn",
    "WLS":      "wls_cd",
    "WIN":      "win",
    "LOSE":     "loss",
    "GAME":     "game_cn",
    "START":    "start_if",
    "START_CN": "start_cn",
    "START_W_CN":"start_win_cn",
    "RELIEF_W_CN":"relief_win_cn",
    "QS_CN":    "qs_cn",
    "QUIT":     "quit",
    "QUIT_CN":  "quit_cn",

    # === 수비 통계 ===
    "PO":       "po",
    "ASS":      "ast",
    "POFF_CN":  "poff_cn",

    # === 투구 관련 ===
    "PIT_CN":   "pitch_cn",
    "GAME_PIT_NO":"game_pitch_no",
    "GAME_PIT_AVG_RT":"game_pitch_avg_rt",
    "PA_PIT_NO":"pa_pitch_no",
    "PA_PIT_RT":"pa_pitch_rt",
    "INN_PIT_AVG_RT":"inn_pitch_avg_rt",
    "GAME_BB_RT":"game_bb_rt",
    "GAME_KK_RT":"game_so_rt",
    "KK_BB_RT": "so_bb_rt",
    "BB_KK_RT": "bb_so_rt",
    "FOGO_RT":  "fo_go_rt",
    "FO_CN":    "fo_cn",
    "GO_CN":    "go_cn",
    "RO_CN":    "ro_cn",
    "D_CN":     "double_cn",
    "XBH_CN":   "xbh_cn",
    "WIN_HIT_CN":"win_hit_cn",
    "MH_HITTER_CN":"mh_hitter_cn",
    "BAT_AROUND_NO":"bat_around_no",
    "TB_CN":    "tb_cn",

    # === 합산 관련 ===
    "OAB":      "opp_ab",
    "OCOUNT":   "opp_count",
    "BHIT":     "bunt_hit",
    "BBBHP":    "bb_bunt_hbp",
    "BBHP":     "bb_hbp",
    "BBHP_CN":  "bb_hbp_cn",
    "TBBHP":    "total_bb_hbp",
    "THIT":     "total_hit",
    "TERR":     "total_err",
    "BPOINT":   "bat_point",
    "TPOINT":   "total_point",
    "BSCORE":   "bat_score",
    "TSCORE":   "total_score",
    "BERR":     "bat_err",
    "TP":       "total_put",

    # === 스코어보드 ===
    "R":        "runs_cn",
    "R_CN":     "runs_cn",
    "S":        "hits_cn",
    "RANK":     "rank_no",
    "SAME":     "same_rank_if",
    "AVG5":     "avg_5g",
    "AVGS":     "avg_season",
    "Score":    "score_cn",
    "SCORE_CN": "score_cn",
    "hscore":   "home_score",
    "vscore":   "away_score",

    # === 실시간/라이브 ===
    "LiveText":  "live_text",
    "LIVETEXT":  "live_text",
    "textStyle": "text_style_cd",
    "icon40":    "icon_40_cd",
    "code":      "code_cd",
    "continue":  "continue_if",

    # === 플래그/상태 ===
    "cancel_flag":    "cancel_if",
    "CANCEL_SC_NM":   "cancel_sc_nm",
    "game_flag":      "game_type_cd",
    "end_flag":       "end_if",
    "suspended_flag": "suspended_if",
    "GROUP_IF":       "group_if",
    "FIRST_IF":       "first_if",
    "LAST_IF":        "last_if",
    "SITUATION_IF":   "situation_if",
    "T_RECORDPAGE_IF":"recordpage_if",

    # === 지역 ===
    "area_wide":"area_wide_nm",
    "area_city":"area_city_nm",
    "area_dong":"area_dong_nm",
    "tm":       "team_cd",

    # === FA ===
    "BROAD_CD": "broad_cd",

    # === 기타/ETC ===
    "ETC_ME":   "etc_memo",
    "GWEEK":    "game_week_nm",
    "gweek":    "game_week_nm",
    "hpcode":   "home_pitcher_id",
    "vpcode":   "away_pitcher_id",
}

# 이닝별 점수 패턴 (#B, #T, INN#, INN#_3, IL#)
def _gen_inning_maps():
    m = {}
    for i in range(1, 26):
        m[f"{i}B"] = f"inn_{i}_bot"
        m[f"{i}T"] = f"inn_{i}_top"
        m[f"INN{i}"] = f"inn_{i}_score"
        m[f"INN{i}_3"] = f"inn_{i}_out3_score"
        m[f"IL{i}"] = f"inn_{i}_loss"
    return m

STANDARD_MAP.update(_gen_inning_maps())


def suggest_standard_name(col_name):
    """레거시 컬럼명 → 표준명(안) 변환"""
    # 1) 명시적 매핑
    if col_name in STANDARD_MAP:
        return STANDARD_MAP[col_name]

    # 2) 이미 신세대 접미사가 있는 컬럼 → 소문자
    new_gen_suffixes = ("_ID", "_NM", "_CD", "_CN", "_RT", "_IF", "_DT",
                        "_TM", "_VA", "_NO", "_SC")
    for sfx in new_gen_suffixes:
        if col_name.endswith(sfx):
            return col_name.lower()

    # 3) 기본: snake_case 변환
    # PascalCase → snake_case
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', col_name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    return s.lower()


def process_file(filepath):
    """dictionary md 파일 처리: 버전 태그 + 표준명 컬럼 추가"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    table_name = os.path.splitext(os.path.basename(filepath))[0]

    # ── 1) 버전 태그 ──
    # 기존 버전 태그가 있으면 교체, 없으면 제목 바로 아래 삽입
    version_line = f"> 최종수정: {TODAY} | 출처: column-metadata.json"
    if lines and lines[0].startswith("> 최종수정"):
        lines[0] = version_line
    elif lines and lines[0].startswith("# "):
        lines.insert(1, "")
        lines.insert(2, version_line)
    else:
        lines.insert(0, version_line)

    # ── 2) 컬럼 상세 테이블에 표준명(안) 추가 ──
    new_lines = []
    in_column_table = False
    header_done = False

    for line in lines:
        stripped = line.rstrip()

        # 컬럼 상세 테이블 헤더 감지
        if re.match(r'\|\s*#\s*\|\s*컬럼명\s*\|', stripped):
            in_column_table = True
            header_done = False
            # 이미 표준명 있으면 스킵
            if "표준명(안)" in stripped:
                new_lines.append(line)
                in_column_table = False
                continue
            new_lines.append(stripped + " 표준명(안) |")
            continue

        if in_column_table and not header_done:
            # separator 행 (|---|---| ...)
            if re.match(r'\|[-\s|]+\|', stripped):
                new_lines.append(stripped + "------|")
                header_done = True
                continue

        if in_column_table and header_done:
            # 데이터 행
            if stripped.startswith("|") and not stripped.startswith("##"):
                # 컬럼명 추출 (2번째 셀)
                cells = [c.strip() for c in stripped.split("|")]
                # cells[0] = '', cells[1] = #, cells[2] = 컬럼명, ...
                if len(cells) >= 3:
                    col_raw = cells[2].strip("`").strip()
                    std_name = suggest_standard_name(col_raw)
                    new_lines.append(stripped + f" `{std_name}` |")
                    continue
            else:
                # 테이블 끝
                in_column_table = False

        new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    return table_name


def main():
    md_files = []
    for domain in ["game", "stats", "realtime", "master"]:
        domain_dir = os.path.join(DICT_DIR, domain)
        if not os.path.isdir(domain_dir):
            continue
        for f in sorted(os.listdir(domain_dir)):
            if f.endswith(".md") and f != "README.md":
                md_files.append(os.path.join(domain_dir, f))

    print(f"대상 파일: {len(md_files)}개")
    for fp in md_files:
        name = process_file(fp)
        print(f"  ✓ {name}")

    print(f"\n완료: {len(md_files)}개 파일 업데이트 ({TODAY})")


if __name__ == "__main__":
    main()
