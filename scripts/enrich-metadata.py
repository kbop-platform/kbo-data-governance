#!/usr/bin/env python3
"""enrich-metadata.py

dictionary/ 내 39개 테이블 .md 파일에 7가지 메타데이터 필드를 추가한다.

추가 필드:
  1. 데이터 티어
  2. 데이터 오너
  3. 갱신 주기
  4. 소비자
  5. 데이터 프로덕트
  6. 접근 수준
  7. 관련 표준

사용법:
    python scripts/enrich-metadata.py
"""

import os
import re
import sys
from pathlib import Path

TIER = {
    'GAMEINFO': 'Tier 1 — Critical',
    'Hitter': 'Tier 1 — Critical',
    'Pitcher': 'Tier 1 — Critical',
    'Score': 'Tier 1 — Critical',
    'ENTRY': 'Tier 1 — Critical',
    'GAMECONTAPP': 'Tier 1 — Critical',
    'IE_LiveText': 'Tier 1 — Critical',
    'IE_BallCount': 'Tier 1 — Critical',
    'IE_GAMESTATE': 'Tier 1 — Critical',
    'IE_ScoreRHEB': 'Tier 1 — Critical',
    'IE_Scoreinning': 'Tier 1 — Critical',
    'person': 'Tier 1 — Critical',
    'BatTotal': 'Tier 2 — Standard',
    'PitTotal': 'Tier 2 — Standard',
    'TeamRank': 'Tier 2 — Standard',
    'KBO_BATRESULT': 'Tier 2 — Standard',
    'KBO_PITRESULT': 'Tier 2 — Standard',
    'SEASON_PLAYER_HITTER': 'Tier 2 — Standard',
    'SEASON_PLAYER_HITTER_SITUATION': 'Tier 2 — Standard',
    'SEASON_PLAYER_PITCHER': 'Tier 2 — Standard',
    'SEASON_PLAYER_PITCHER_SITUATION': 'Tier 2 — Standard',
    'DEFEN': 'Tier 2 — Standard',
    'GAME_HR': 'Tier 2 — Standard',
    'GAME_MEMO': 'Tier 2 — Standard',
    'KBO_schedule': 'Tier 2 — Standard',
    'CANCEL_GAME': 'Tier 2 — Standard',
    'IE_BatterRecord': 'Tier 2 — Standard',
    'IE_PitcherRecord': 'Tier 2 — Standard',
    'TEAM': 'Tier 3 — Reference',
    'STADIUM': 'Tier 3 — Reference',
    'GAMEINFO_WEATHER': 'Tier 3 — Reference',
    'PERSON_FA': 'Tier 3 — Reference',
    'person2': 'Tier 3 — Reference',
    'PERSON': 'Tier 3 — Reference',
    'IE_log': 'Tier 3 — Reference',
    'IE_GameList': 'Tier 3 — Reference',
    'PITCHCLOCK': 'Tier 3 — Reference',
    'GAME_MEMO_PITCHCLOCK': 'Tier 3 — Reference',
    'KBO_ETCGAME': 'Tier 3 — Reference',
}

OWNER = {
    'GAMEINFO': '기록위원회 (R-03)',
    'GAMEINFO_WEATHER': '기록위원회 (R-03)',
    'GAMECONTAPP': '기록위원회 (R-03)',
    'ENTRY': '기록위원회 (R-03)',
    'Hitter': '기록위원회 (R-03)',
    'Pitcher': '기록위원회 (R-03)',
    'Score': '기록위원회 (R-03)',
    'DEFEN': '기록위원회 (R-03)',
    'GAME_HR': '기록위원회 (R-03)',
    'GAME_MEMO': '기록위원회 (R-03)',
    'GAME_MEMO_PITCHCLOCK': '기록위원회 (R-03)',
    'PITCHCLOCK': '기록위원회 (R-03)',
    'KBO_BATRESULT': '기록위원회 (R-03)',
    'KBO_PITRESULT': '기록위원회 (R-03)',
    'KBO_ETCGAME': '기록위원회 (R-03)',
    'person': '기록위원회 (R-03)',
    'person2': '기록위원회 (R-03)',
    'PERSON': '기록위원회 (R-03)',
    'PERSON_FA': '기록위원회 (R-03)',
    'BatTotal': '통계분석팀 (R-04)',
    'PitTotal': '통계분석팀 (R-04)',
    'TeamRank': '통계분석팀 (R-04)',
    'SEASON_PLAYER_HITTER': '통계분석팀 (R-04)',
    'SEASON_PLAYER_HITTER_SITUATION': '통계분석팀 (R-04)',
    'SEASON_PLAYER_PITCHER': '통계분석팀 (R-04)',
    'SEASON_PLAYER_PITCHER_SITUATION': '통계분석팀 (R-04)',
    'IE_LiveText': 'S2i 운영 (R-06)',
    'IE_BallCount': 'S2i 운영 (R-06)',
    'IE_BatterRecord': 'S2i 운영 (R-06)',
    'IE_PitcherRecord': 'S2i 운영 (R-06)',
    'IE_GameList': 'S2i 운영 (R-06)',
    'IE_GAMESTATE': 'S2i 운영 (R-06)',
    'IE_ScoreRHEB': 'S2i 운영 (R-06)',
    'IE_Scoreinning': 'S2i 운영 (R-06)',
    'IE_log': 'S2i 운영 (R-06)',
    'TEAM': '데이터 관리자 (R-01)',
    'STADIUM': '데이터 관리자 (R-01)',
    'KBO_schedule': '경기운영팀 (R-05)',
    'CANCEL_GAME': '경기운영팀 (R-05)',
}

REFRESH = {
    'GAMEINFO': '경기 당일 (S2i 전송)',
    'GAMECONTAPP': '경기 당일 (S2i 전송)',
    'ENTRY': '경기 당일 (S2i 전송)',
    'Hitter': '경기 당일 (S2i 전송)',
    'Pitcher': '경기 당일 (S2i 전송)',
    'Score': '경기 당일 (S2i 전송)',
    'DEFEN': '경기 당일 (S2i 전송)',
    'GAME_HR': '경기 당일 (S2i 전송)',
    'GAME_MEMO': '경기 당일 (S2i 전송)',
    'GAME_MEMO_PITCHCLOCK': '경기 당일 (S2i 전송)',
    'PITCHCLOCK': '경기 당일 (S2i 전송)',
    'KBO_BATRESULT': '경기 당일 (S2i 전송)',
    'KBO_PITRESULT': '경기 당일 (S2i 전송)',
    'KBO_ETCGAME': '경기 당일 (S2i 전송)',
    'GAMEINFO_WEATHER': '경기 당일 (기상청)',
    'BatTotal': 'D+1 (전일 경기 반영)',
    'PitTotal': 'D+1 (전일 경기 반영)',
    'TeamRank': 'D+1 (전일 경기 반영)',
    'SEASON_PLAYER_HITTER': 'D+1 (시즌 중)',
    'SEASON_PLAYER_HITTER_SITUATION': 'D+1 (시즌 중)',
    'SEASON_PLAYER_PITCHER': 'D+1 (시즌 중)',
    'SEASON_PLAYER_PITCHER_SITUATION': 'D+1 (시즌 중)',
    'IE_LiveText': '실시간 (< 5초)',
    'IE_BallCount': '실시간 (< 5초)',
    'IE_BatterRecord': '실시간 (< 5초)',
    'IE_PitcherRecord': '실시간 (< 5초)',
    'IE_GameList': '실시간 (< 5초)',
    'IE_GAMESTATE': '실시간 (< 5초)',
    'IE_ScoreRHEB': '실시간 (< 5초)',
    'IE_Scoreinning': '실시간 (< 5초)',
    'IE_log': '실시간 (자동 생성)',
    'person': '시즌 전 갱신',
    'person2': '시즌 전 갱신',
    'PERSON': '시즌 전 갱신',
    'PERSON_FA': 'FA 발생 시 수시',
    'TEAM': '연 1회 (시즌 전)',
    'STADIUM': '연 1회 (시즌 전)',
    'KBO_schedule': '시즌 전 일괄',
    'CANCEL_GAME': '발생 즉시',
}

CONSUMERS = {
    'GAMEINFO': '기록팀, 방송팀, 통계팀, 외부 API',
    'GAMEINFO_WEATHER': '방송팀',
    'GAMECONTAPP': '기록팀, 분석팀',
    'ENTRY': '기록팀, 방송팀',
    'Hitter': '기록팀, 통계팀, 외부 API',
    'Pitcher': '기록팀, 통계팀, 외부 API',
    'Score': '방송팀, 외부 API',
    'DEFEN': '기록팀',
    'GAME_HR': '미디어, 외부 API',
    'GAME_MEMO': '기록팀',
    'GAME_MEMO_PITCHCLOCK': '기록팀',
    'PITCHCLOCK': '기록팀',
    'BatTotal': '통계팀, 외부 API',
    'PitTotal': '통계팀, 외부 API',
    'TeamRank': '미디어, 외부 API',
    'KBO_BATRESULT': '분석팀',
    'KBO_PITRESULT': '분석팀',
    'KBO_ETCGAME': '기록팀',
    'SEASON_PLAYER_HITTER': '통계팀, 외부 API',
    'SEASON_PLAYER_HITTER_SITUATION': '분석팀',
    'SEASON_PLAYER_PITCHER': '통계팀, 외부 API',
    'SEASON_PLAYER_PITCHER_SITUATION': '분석팀',
    'IE_LiveText': '방송팀, 앱 서비스',
    'IE_BallCount': '방송팀, 앱 서비스',
    'IE_BatterRecord': '방송팀',
    'IE_PitcherRecord': '방송팀',
    'IE_GameList': '앱 서비스',
    'IE_GAMESTATE': '방송팀, 앱 서비스',
    'IE_ScoreRHEB': '방송팀, 앱 서비스',
    'IE_Scoreinning': '방송팀, 앱 서비스',
    'IE_log': '시스템 관리자',
    'person': '전 시스템',
    'person2': '기록팀',
    'PERSON': '기록팀',
    'PERSON_FA': '기록팀, 인사팀',
    'TEAM': '전 시스템',
    'STADIUM': '전 시스템',
    'KBO_schedule': '전 시스템',
    'CANCEL_GAME': '운영팀, 방송팀',
}

PRODUCT = {
    'GAMEINFO': '[경기 요약](../products/game-summary.md)',
    'Hitter': '[경기 요약](../products/game-summary.md)',
    'Pitcher': '[경기 요약](../products/game-summary.md)',
    'Score': '[경기 요약](../products/game-summary.md)',
    'ENTRY': '[경기 요약](../products/game-summary.md)',
    'GAMECONTAPP': '[경기 요약](../products/game-summary.md)',
    'DEFEN': '[경기 요약](../products/game-summary.md)',
    'GAME_HR': '[경기 요약](../products/game-summary.md)',
    'GAME_MEMO': '[경기 요약](../products/game-summary.md)',
    'GAME_MEMO_PITCHCLOCK': '[경기 요약](../products/game-summary.md)',
    'PITCHCLOCK': '[경기 요약](../products/game-summary.md)',
    'GAMEINFO_WEATHER': '[일정 관리](../products/schedule.md)',
    'IE_LiveText': '[실시간 경기](../products/live-game.md)',
    'IE_BallCount': '[실시간 경기](../products/live-game.md)',
    'IE_BatterRecord': '[실시간 경기](../products/live-game.md)',
    'IE_PitcherRecord': '[실시간 경기](../products/live-game.md)',
    'IE_GameList': '[실시간 경기](../products/live-game.md)',
    'IE_GAMESTATE': '[실시간 경기](../products/live-game.md)',
    'IE_ScoreRHEB': '[실시간 경기](../products/live-game.md)',
    'IE_Scoreinning': '[실시간 경기](../products/live-game.md)',
    'IE_log': '[실시간 경기](../products/live-game.md)',
    'person': '[선수 프로필](../products/player-profile.md)',
    'person2': '[선수 프로필](../products/player-profile.md)',
    'PERSON': '[선수 프로필](../products/player-profile.md)',
    'PERSON_FA': '[선수 프로필](../products/player-profile.md)',
    'BatTotal': '[시즌 통계](../products/season-stats.md)',
    'PitTotal': '[시즌 통계](../products/season-stats.md)',
    'TeamRank': '[시즌 통계](../products/season-stats.md)',
    'KBO_BATRESULT': '[시즌 통계](../products/season-stats.md)',
    'KBO_PITRESULT': '[시즌 통계](../products/season-stats.md)',
    'KBO_ETCGAME': '[시즌 통계](../products/season-stats.md)',
    'SEASON_PLAYER_HITTER': '[시즌 통계](../products/season-stats.md)',
    'SEASON_PLAYER_HITTER_SITUATION': '[시즌 통계](../products/season-stats.md)',
    'SEASON_PLAYER_PITCHER': '[시즌 통계](../products/season-stats.md)',
    'SEASON_PLAYER_PITCHER_SITUATION': '[시즌 통계](../products/season-stats.md)',
    'TEAM': '[기준 데이터](../products/master-codes.md)',
    'STADIUM': '[기준 데이터](../products/master-codes.md)',
    'KBO_schedule': '[일정 관리](../products/schedule.md)',
    'CANCEL_GAME': '[일정 관리](../products/schedule.md)',
}

ACCESS = {
    'person': 'Restricted',
    'person2': 'Restricted',
    'PERSON': 'Restricted',
    'PERSON_FA': 'Restricted',
}
PUBLIC_TABLES = {'TEAM', 'STADIUM', 'KBO_schedule', 'CANCEL_GAME'}

STANDARDS = {
    'GAMEINFO': '[ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md)',
    'GAMECONTAPP': '[코드 사전](../../standards/code-dictionary.md)',
    'ENTRY': '[코드 사전](../../standards/code-dictionary.md)',
    'Hitter': '[ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md)',
    'Pitcher': '[ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md)',
    'Score': '[ID 체계](../../standards/id-system.md)',
    'DEFEN': '[약어 사전](../../standards/abbreviations.md)',
    'GAME_HR': '[ID 체계](../../standards/id-system.md)',
    'BatTotal': '[ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md)',
    'PitTotal': '[ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md)',
    'TeamRank': '[ID 체계](../../standards/id-system.md)',
    'KBO_BATRESULT': '[코드 사전](../../standards/code-dictionary.md)',
    'KBO_PITRESULT': '[코드 사전](../../standards/code-dictionary.md)',
    'person': '[ID 체계](../../standards/id-system.md), [도메인 타입](../../standards/domain-types.md)',
    'TEAM': '[ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md)',
    'STADIUM': '[ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md)',
    'KBO_schedule': '[ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md)',
}

SKIP_FILES = {'README.md', 'index.md', 'lineage.md'}
DOMAINS = ['game', 'stats', 'realtime', 'master']
TODAY = '2026-02-25'


def get_access_level(table_name):
    if table_name in ACCESS:
        return ACCESS[table_name]
    if table_name in PUBLIC_TABLES:
        return 'Public'
    return 'Internal'


def get_standards(table_name):
    return STANDARDS.get(table_name, '[도메인 타입](../../standards/domain-types.md)')


def build_new_rows(table_name):
    rows = [
        '| 데이터 티어 | {} |'.format(TIER[table_name]),
        '| 데이터 오너 | {} |'.format(OWNER[table_name]),
        '| 갱신 주기 | {} |'.format(REFRESH[table_name]),
        '| 소비자 | {} |'.format(CONSUMERS[table_name]),
        '| 데이터 프로덕트 | {} |'.format(PRODUCT[table_name]),
        '| 접근 수준 | {} |'.format(get_access_level(table_name)),
        '| 관련 표준 | {} |'.format(get_standards(table_name)),
    ]
    return '\n'.join(rows)


def process_file(filepath, table_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    schema_pattern = re.compile(r'^(\| 스키마 세대 \|.*\|)$', re.MULTILINE)
    match = schema_pattern.search(content)
    if not match:
        print('  [WARN] 스키마 세대 행을 찾을 수 없음: {}'.format(filepath))
        return False

    insert_pos = match.end()
    new_rows = build_new_rows(table_name)
    content = content[:insert_pos] + '\n' + new_rows + content[insert_pos:]

    version_pattern = re.compile(r'^> 최종수정:.*$', re.MULTILINE)
    new_version = '> 최종수정: {} | 버전: 2 | 출처: column-metadata.json'.format(TODAY)
    content, count = version_pattern.subn(new_version, content)
    if count == 0:
        print('  [WARN] 버전 태그를 찾을 수 없음: {}'.format(filepath))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    dict_root = project_root / 'dictionary'

    if not dict_root.is_dir():
        print('[ERROR] dictionary/ 디렉터리 없음: {}'.format(dict_root))
        sys.exit(1)

    success_count = 0
    skip_count = 0
    warn_count = 0

    for domain in DOMAINS:
        domain_dir = dict_root / domain
        if not domain_dir.is_dir():
            print('[WARN] 도메인 디렉터리 없음: {}'.format(domain_dir))
            continue

        print('\n=== {}/ ==='.format(domain))

        for md_file in sorted(domain_dir.glob('*.md')):
            if md_file.name in SKIP_FILES:
                continue

            table_name = md_file.stem

            if table_name not in TIER:
                print('  [SKIP] 사전 미등록: {}'.format(md_file.name))
                skip_count += 1
                continue

            ok = process_file(str(md_file), table_name)
            if ok:
                print('  [OK] {}'.format(md_file.name))
                success_count += 1
            else:
                warn_count += 1

    print('\n--- 완료 ---')
    print('성공: {}개 파일'.format(success_count))
    if skip_count:
        print('건너뜀: {}개 파일'.format(skip_count))
    if warn_count:
        print('경고: {}개 파일'.format(warn_count))


if __name__ == '__main__':
    main()
