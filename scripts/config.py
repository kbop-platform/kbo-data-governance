#!/usr/bin/env python3
"""scripts/config.py - 공유 상수 및 유틸리티

모든 데이터 사전 파이프라인 스크립트에서 공통으로 사용하는 상수를 중앙 관리한다.
정적 매핑 데이터는 scripts/data/*.json에서 로드하고,
동적 이닝 패턴은 런타임에 merge한다.
"""
import json
import os
import re
from pathlib import Path


# ============================================================
# A. 기본 경로
# ============================================================
BASE_DIR = str(Path(__file__).resolve().parent.parent)
_DATA_DIR = Path(__file__).resolve().parent / "data"


def _load_json(filename):
    """scripts/data/ 디렉토리에서 JSON 파일 로드"""
    with open(_DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# B. .env 로딩
# ============================================================
def load_env():
    """프로젝트 루트의 .env 파일에서 환경 변수를 로딩한다."""
    env_path = os.path.join(BASE_DIR, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())


# ============================================================
# C. 도메인 분류
# ============================================================
DOMAINS = {
    'game': {
        'label': '경기 기록',
        'tables': [
            'GAMEINFO', 'GAMEINFO_WEATHER', 'GAMECONTAPP', 'ENTRY',
            'Hitter', 'Pitcher', 'Score', 'DEFEN',
            'GAME_HR', 'GAME_MEMO', 'GAME_MEMO_PITCHCLOCK', 'PITCHCLOCK',
        ],
    },
    'stats': {
        'label': '통계',
        'tables': [
            'BatTotal', 'PitTotal', 'TeamRank',
            'KBO_BATRESULT', 'KBO_PITRESULT', 'KBO_ETCGAME',
            'SEASON_PLAYER_HITTER', 'SEASON_PLAYER_HITTER_SITUATION',
            'SEASON_PLAYER_PITCHER', 'SEASON_PLAYER_PITCHER_SITUATION',
        ],
    },
    'realtime': {
        'label': '실시간',
        'tables': [
            'IE_LiveText', 'IE_BallCount', 'IE_BatterRecord',
            'IE_PitcherRecord', 'IE_GameList', 'IE_GAMESTATE',
            'IE_ScoreRHEB', 'IE_Scoreinning', 'IE_log',
        ],
    },
    'master': {
        'label': '마스터',
        'tables': [
            'person', 'person2', 'PERSON', 'PERSON_FA',
            'TEAM', 'STADIUM', 'KBO_schedule', 'CANCEL_GAME',
        ],
    },
}

# 편의 접근자
DOMAIN_LABELS = {k: v['label'] for k, v in DOMAINS.items()}
DOMAIN_TABLES = {k: v['tables'] for k, v in DOMAINS.items()}
DOMAIN_ORDER = [(k, v['label']) for k, v in DOMAINS.items()]
TABLE_TO_DOMAIN = {}
for _k, _v in DOMAINS.items():
    for _t in _v['tables']:
        TABLE_TO_DOMAIN[_t] = _k


# ============================================================
# D. 표준명 매핑: 레거시 컬럼명 → snake_case 표준명(안)
#    정본: scripts/data/standard-map.json + 이닝 동적 패턴
# ============================================================
STANDARD_MAP = _load_json("standard-map.json")

# 이닝별 점수 패턴 동적 생성 (#B, #T, INN#, INN#_3, IL#)
for _i in range(1, 26):
    STANDARD_MAP[f"{_i}B"] = f"inn_{_i}_bot"
    STANDARD_MAP[f"{_i}T"] = f"inn_{_i}_top"
    STANDARD_MAP[f"INN{_i}"] = f"inn_{_i}_score"
    STANDARD_MAP[f"INN{_i}_3"] = f"inn_{_i}_out3_score"
    STANDARD_MAP[f"IL{_i}"] = f"inn_{_i}_loss"


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
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', col_name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    return s.lower()


# ============================================================
# E. 컬럼 설명
#    정본: scripts/data/column-desc.json + 이닝 동적 패턴
# ============================================================
COLUMN_DESC = _load_json("column-desc.json")

# 이닝 패턴 자동 생성
# Score: {N}T, {N}B
for _i in range(1, 26):
    COLUMN_DESC[f'{_i}T'] = f'{_i}회 초 득점 (-1=미진행)'
    COLUMN_DESC[f'{_i}B'] = f'{_i}회 말 득점 (-1=미진행)'

# KBO_BATRESULT: INN{N}, IL{N}, INN{N}_3
for _i in range(1, 26):
    COLUMN_DESC[f'INN{_i}'] = f'{_i}회 타격 결과 (HOW 코드, EUC-KR)'
    COLUMN_DESC[f'IL{_i}'] = f'{_i}회 교체타자 타격 결과'
    COLUMN_DESC[f'INN{_i}_3'] = f'{_i}회 3아웃 후 타격 결과'

# 테이블별 오버라이드 (동일 컬럼명이 다른 의미)
# 값: (설명, 표준명)  - 기본 COLUMN_DESC/STANDARD_MAP 대신 적용
TABLE_OVERRIDES = {
    ('BatTotal', 'TB'):           ('루타 (Total Bases)', 'tb_cn'),
    ('KBO_PITRESULT', 'POS'):     ('등판 순서·포지션 코드 (11=선발, 21=2번째, 31=3번째, ..., A1=10번째, B1=11번째, C1=12번째)', 'appear_order_pos_cd'),
    ('KBO_PITRESULT', 'CHANGEINN'):('교체 이닝', 'change_inn_no'),
    ('KBO_PITRESULT', 'S'):       ('피안타', 'hit_allowed_cn'),
    ('KBO_PITRESULT', 'BBHP'):    ('볼넷+사구 합계', 'bb_hbp_cn'),
    ('Pitcher', 'POS'):           ('등판 순서·포지션 코드 (11=선발, 21=2번째, 31=3번째, ..., A1=10번째, B1=11번째, C1=12번째)', 'appear_order_pos_cd'),
}


# ============================================================
# F. 표준 테이블명
# ============================================================
STANDARD_TABLE_NAMES = {
    "GAMEINFO": "GAME_INFO",
    "GAMEINFO_WEATHER": "GAME_INFO_WEATHER",
    "GAMECONTAPP": "GAME_CONT_APP",
    "ENTRY": "ENTRY",
    "Hitter": "HITTER",
    "Pitcher": "PITCHER",
    "Score": "SCORE",
    "DEFEN": "DEFEN",
    "GAME_HR": "GAME_HR",
    "GAME_MEMO": "GAME_MEMO",
    "GAME_MEMO_PITCHCLOCK": "GAME_MEMO_PITCHCLOCK",
    "PITCHCLOCK": "PITCHCLOCK",
    "BatTotal": "BAT_TOTAL",
    "PitTotal": "PIT_TOTAL",
    "TeamRank": "TEAM_RANK",
    "KBO_BATRESULT": "KBO_BAT_RESULT",
    "KBO_PITRESULT": "KBO_PIT_RESULT",
    "KBO_ETCGAME": "KBO_ETC_GAME",
    "SEASON_PLAYER_HITTER": "SEASON_PLAYER_HITTER",
    "SEASON_PLAYER_HITTER_SITUATION": "SEASON_PLAYER_HITTER_SITUATION",
    "SEASON_PLAYER_PITCHER": "SEASON_PLAYER_PITCHER",
    "SEASON_PLAYER_PITCHER_SITUATION": "SEASON_PLAYER_PITCHER_SITUATION",
    "IE_LiveText": "IE_LIVE_TEXT",
    "IE_BallCount": "IE_BALL_COUNT",
    "IE_BatterRecord": "IE_BATTER_RECORD",
    "IE_PitcherRecord": "IE_PITCHER_RECORD",
    "IE_GameList": "IE_GAME_LIST",
    "IE_GAMESTATE": "IE_GAME_STATE",
    "IE_ScoreRHEB": "IE_SCORE_RHEB",
    "IE_Scoreinning": "IE_SCORE_INNING",
    "IE_log": "IE_LOG",
    "person": "PERSON",
    "person2": "PERSON2",
    "PERSON": "PERSON",
    "PERSON_FA": "PERSON_FA",
    "TEAM": "TEAM",
    "STADIUM": "STADIUM",
    "KBO_schedule": "KBO_SCHEDULE",
    "CANCEL_GAME": "CANCEL_GAME",
}


# ============================================================
# G. 테이블-DB 매핑 (대표 DB 선정)
# ============================================================
TABLE_DB_MAP = {
    # 경기 기록 (DB1_BASEBALL 우선)
    'Hitter': 'DB1_BASEBALL_220328',
    'Pitcher': 'DB1_BASEBALL_220328',
    'ENTRY': 'DB1_BASEBALL_220328',
    'GAMECONTAPP': 'DB1_BASEBALL_220328',
    'GAMEINFO': 'DB1_BASEBALL_220328',
    'Score': 'DB1_BASEBALL_220328',
    'BatTotal': 'DB1_BASEBALL_220328',
    'PitTotal': 'DB1_BASEBALL_220328',
    'TeamRank': 'DB1_BASEBALL_220328',
    'DEFEN': 'DB1_BASEBALL_220328',
    'GAME_HR': 'DB1_BASEBALL_220328',
    'GAME_MEMO': 'DB1_BASEBALL_220328',
    'GAME_MEMO_PITCHCLOCK': 'DB1_BASEBALL_220328',
    # 집계/결과
    'KBO_BATRESULT': 'DB2_BASEBALL_220328',
    'KBO_PITRESULT': 'DB2_BASEBALL_220328',
    'KBO_ETCGAME': 'DB2_BASEBALL_220328',
    # 시즌 통계
    'SEASON_PLAYER_HITTER': 'DB1_BASEBALL_2_220328',
    'SEASON_PLAYER_PITCHER': 'DB1_BASEBALL_2_220328',
    'SEASON_PLAYER_HITTER_SITUATION': 'DB1_BASEBALL_2_220328',
    'SEASON_PLAYER_PITCHER_SITUATION': 'DB1_BASEBALL_2_220328',
    # 실시간/IE
    'IE_LiveText': 'DB2_BASEBALL_NEW_220328',
    'IE_BatterRecord': 'DB2_BASEBALL_NEW_220328',
    'IE_PitcherRecord': 'DB2_BASEBALL_NEW_220328',
    'IE_BallCount': 'DB2_BASEBALL_NEW_220328',
    'IE_Scoreinning': 'DB2_BASEBALL_NEW_220328',
    'IE_ScoreRHEB': 'DB2_BASEBALL_NEW_220328',
    'IE_GameList': 'DB2_BASEBALL_NEW_220328',
    'IE_GAMESTATE': 'DB2_BASEBALL_NEW_220328',
    'IE_log': 'DB2_BASEBALL_NEW_220328',
    # 스케줄/마스터
    'KBO_schedule': 'DB2_BASEBALL_NEW_220328',
    'person': 'DB2_BASEBALL_NEW_220328',
    'person2': 'DB2_BASEBALL_NEW_220328',
    'PERSON': 'DB2_MINOR_BASEBALL_220328',
    'PERSON_FA': 'DB2_BASEBALL_NEW_220328',
    'TEAM': 'DB2_BASEBALL_2_220328',
    'STADIUM': 'DB2_BASEBALL_NEW_220328',
    'CANCEL_GAME': 'DB2_BASEBALL_NEW_220328',
    # 기타
    'GAMEINFO_WEATHER': 'DB2_BASEBALL_220328',
    'PITCHCLOCK': 'DB2_BASEBALL_220328',
}


# ============================================================
# H. 코드성 컬럼 판별 집합
# ============================================================
CODE_NAMES = {
    'TB', 'HOW', 'PLACE', 'POSI', 'WLS', 'LEAGUE', 'TEAM', 'WEATH',
    'START', 'QUIT', 'OCOUNT', 'ENDYN', 'CANCLE', 'DHEADER',
    'TB_SC', 'PLACE_SC', 'DIREC_SC', 'PIT_RESULT_SC',
    'STATUS_ID', 'LE_ID', 'SR_ID', 'SEASON_ID',
    'SUSPENDED', 'game_flag', 'FIRST_IF', 'LAST_IF', 'RESULT',
}
