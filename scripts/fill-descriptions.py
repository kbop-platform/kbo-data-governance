#!/usr/bin/env python3
"""dictionary/**/*.md의 빈 컬럼 설명을 일괄 채움

Phase 4-2: 컬럼 설명 커버리지 ~58% → ~100%

사용법:
  python scripts/fill-descriptions.py          # 실행 (파일 수정)
  python scripts/fill-descriptions.py --dry-run # 변경 내용만 미리보기
"""
import os
import re
import sys
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)
DICT_DIR = os.path.join(BASE_DIR, 'dictionary')


# ============================================================
# 1. 공통 컬럼 설명 맵
#    - generate-dictionary.py COLUMN_DESCRIPTIONS 기반 (~140개)
#    - 신규 추가 (~210개)
# ============================================================
COLUMN_DESC = {
    # ── 식별자 ──
    'GMKEY':     '경기 고유키 (YYYYMMDDVVHH#)',
    'G_ID':      '경기 ID (YYYYMMDDVVHH# 형식)',
    'GDAY':      '경기 일자 (YYYYMMDD)',
    'GYEAR':     '시즌 연도 (4자리, "9999"=통산)',
    'PCODE':     '선수 코드 (5~6자리 숫자)',
    'P_ID':      '선수 ID (정수)',
    'LE_ID':     '리그 ID (1=1군)',
    'SR_ID':     '시리즈 ID (0=정규시즌)',
    'SEASON_ID': '시즌 ID (연도)',
    'T_ID':      '팀 코드 (2자리)',
    'SEQ_NO':    '순번',
    'SEQ':       '순번',
    'SERNO':     '일련번호',
    'ORDER_NO':  '정렬 순번',

    # ── 경기 구분 ──
    'TB':      '팀 구분 (T=원정, B=홈)',
    'TB_SC':   '팀 구분 코드 (T=원정, B=홈)',
    'INN':     '이닝',
    'INN_NO':  '이닝 번호',
    'INN2':    '이닝 세부 (아웃수 환산)',
    'OCOUNT':  '아웃 카운트 (0-2, 4=이닝종료)',
    'HOW':     '플레이 결과 코드 (49종)',
    'PLACE':   '타구 방향 (포지션번호)',
    'POSI':    '포지션 코드 (XY 형식)',
    'TURN':    '타순',
    'ONETURN': '타순 (1~9)',

    # ── 경기 환경 (GAMEINFO) ──
    'DBHD':    '더블헤더 번호 (0=일반, 1=1차, 2=2차)',
    'VTEAM':   '원정팀 코드',
    'HTEAM':   '홈팀 코드',
    'STTM':    '경기 시작 시각 (HHMM)',
    'ENTM':    '경기 종료 시각 (HHMM)',
    'DLTM':    '지연 시간 (분)',
    'GMTM':    '경기 소요 시간 (분)',
    'STAD':    '구장 코드',
    'STADIUM': '구장명',
    'SNAME':   '구장 약칭',
    'UMPC':    '주심 이름',
    'UMP1':    '1루심 이름',
    'UMP2':    '2루심 이름',
    'UMP3':    '3루심 이름',
    'UMPL':    '좌측 외야심 이름',
    'UMPR':    '우측 외야심 이름',
    'SCOA':    '기록원 A 이름',
    'SCOB':    '기록원 B 이름',
    'TEMP':    '기온 (×10, 예: 270=27.0℃)',
    'MOIS':    '습도 (%)',
    'WEATH':   '날씨 코드 (F=맑음, C=흐림, R=비)',
    'WIND':    '풍향 (16방위)',
    'WINS':    '풍속 (m/s)',
    'GWEEK':   '요일 (EUC-KR 인코딩)',
    'CROWD':   '관중수',
    'CHAJUN':  '차전 (라운드 번호)',

    # ── GAMECONTAPP ──
    'BCOUNT':  '투구 시퀀스 상세 (S/B/T/F/H 등)',
    'RTURN':   '실제 타순 (교체 포함)',
    'FIELD':   '수비 배치 코드',
    'HITTER':  '타자 선수 코드',
    'HITNAME': '타자 이름 (EUC-KR)',
    'PITNAME': '투수 이름 (EUC-KR)',
    'PITCHER': '투수 선수 코드',
    'CATNAME': '포수 이름 (EUC-KR)',
    'CATCHER': '포수 선수 코드',
    'BCNT':    '볼카운트 (S-B 형식)',
    'TSCORE':  '원정팀 누적 득점',
    'BSCORE':  '홈팀 누적 득점',
    'BASE1B':  '1루 주자 타순 (플레이 전)',
    'BASE2B':  '2루 주자 타순 (플레이 전)',
    'BASE3B':  '3루 주자 타순 (플레이 전)',
    'BASE1A':  '1루 주자 타순 (플레이 후)',
    'BASE2A':  '2루 주자 타순 (플레이 후)',
    'BASE3A':  '3루 주자 타순 (플레이 후)',

    # ── Score 요약 ──
    'TPOINT': '원정팀 총득점',
    'BPOINT': '홈팀 총득점',
    'THIT':   '원정팀 총안타',
    'BHIT':   '홈팀 총안타',
    'TERR':   '원정팀 총실책',
    'BERR':   '홈팀 총실책',
    'TBBHP':  '원정팀 볼넷+사구 합계',
    'BBBHP':  '홈팀 볼넷+사구 합계',

    # ── 타격 기록 ──
    'AB':  '타수 (At Bat)',
    'PA':  '타석 (Plate Appearance)',
    'HIT': '안타',
    'H2':  '2루타',
    'H3':  '3루타',
    'HR':  '홈런',
    'RBI': '타점',
    'RUN': '득점',
    'BB':  '볼넷',
    'HP':  '사구 (Hit by Pitch)',
    'IB':  '고의사구 (Intentional BB)',
    'KK':  '삼진',
    'GD':  '병살타',
    'SB':  '도루',
    'CS':  '도루실패',
    'SF':  '희생플라이',
    'SH':  '희생번트',
    'ERR': '실책',
    'LOB': '잔루',
    'HRA': '타율',

    # ── 투수 기록 ──
    'W':    '승',
    'L':    '패',
    'SV':   '세이브',
    'HOLD': '홀드',
    'BS':   '블론세이브 (Blown Save)',
    'ERA':  '평균자책점',
    'ER':   '자책점',
    'R':    '실점',
    'BF':   '상대타자수',
    'NP':   '투구수',
    'CG':   '완투',
    'SHO':  '완봉',
    'WLS':  '승패세 (W=승, L=패, S=세이브)',
    'BK':   '보크',
    'WP':   '폭투',
    'PB':   '포일 (Passed Ball)',

    # ── 수비 ──
    'PO':  '자살 (Put Out)',
    'ASS': '보살 (Assist)',
    'DP':  '병살 (Double Play)',

    # ── 팀/순위 ──
    'TEAM':    '팀 코드',
    'LEAGUE':  '리그',
    'RANK':    '순위',
    'GAME':    '경기 수',
    'GAMENUM': '경기 수',
    'WIN':     '승',
    'LOSE':    '패',
    'SAME':    '무승부',
    'WRA':     '승률',
    'SEC':     '시리즈 구분',
    'LRA':     '좌타자 대 타율',
    'BRA':     '대타율 (Batting Avg Against)',

    # ── 선수 마스터 ──
    'NAME':     '선수명',
    'ENGNAME':  '영문 이름',
    'CNAME':    '한자 이름',
    'BIRTH':    '생년월일',
    'HEIGHT':   '키 (cm)',
    'WEIGHT':   '몸무게 (kg)',
    'POS':      '포지션 코드',
    'HITTYPE':  '투타 유형',
    'BACKNUM':  '등번호',
    'CAREER':   '경력',
    'INDATE':   '입단일',
    'POSITION': '포지션명',
    'PROMISE':  '계약금',
    'MONEY':    '연봉',
    'DRAFT':    '드래프트 정보',
    'OPTION':   'FA 옵션',
    'NUM':      '등번호',

    # ── ENTRY ──
    'CHIN':      '교체 이닝',
    'CHTURN':    '교체 타순',
    'CHBCNT':    '교체 시점 볼카운트',
    'CHIN2':     '교체 이닝 세부',
    'CHANGEINN': '교체 이닝',

    # ── KBO_BATRESULT 요약 ──
    'AVGS': '시즌 누적 타율',
    'AVG5': '최근 5경기 타율',

    # ── KBO_PITRESULT ──
    'S':    '피안타',
    'BBHP': '볼넷+사구 합계',

    # ── 기타 기록 ──
    'START':    '선발 여부',
    'QUIT':     '강판 여부',
    'continue': '연속 기록',
    'CONTINUE': '연속 기록',
    'CONT':     '연속 기록',
    'RESULT':   '결과',
    'BESSION':  '세션',

    # ── 신세대 접미사 컬럼 ──
    'SECTION_CD':   '구간 코드',
    'GROUP_IF':     '그룹 구분',
    'SITUATION_IF': '상황 구분',
    'FIRST_IF':     '첫 여부 플래그',
    'LAST_IF':      '마지막 여부 플래그',

    # ── GAME_MEMO / GAME_MEMO_PITCHCLOCK ──
    'REQ_T_ID':      '요청 팀 코드',
    'START_TM':      '시작 시각',
    'END_TM':        '종료 시각',
    'USE_TM':        '사용 시간',
    'ETC_ME':        '기타 메모',
    'BAT_ORDER_NO':  '타순 번호',
    'BAT_AROUND_NO': '타석 회전 번호',
    'PA_PIT_NO':     '타석 투구 번호',
    'GAME_PIT_NO':   '경기 투구 번호',
    'PIT_RESULT_SC': '투구 결과 상태코드',
    'BAT_P_ID':      '타자 선수 ID',
    'PIT_P_ID':      '투수 선수 ID',

    # ── PITCHCLOCK ──
    'PITCHCLOCK': '피치클락 위반 코드',
    'RUNNER':     '주자 상태 코드',
    'DETAIL':     '상세 내용',

    # ── KBO_schedule (소문자) ──
    'end_flag':      '종료 여부 (0/1)',
    'gmonth':        '경기 월',
    'gday':          '경기 일',
    'gweek':         '요일',
    'home':          '홈팀명',
    'home_key':      '홈팀 코드',
    'visit':         '원정팀명',
    'visit_key':     '원정팀 코드',
    'stadium_key':   '구장 코드',
    'dheader':       '더블헤더 번호',
    'hpcode':        '홈팀 선발투수 코드',
    'vpcode':        '원정팀 선발투수 코드',
    'gtime':         '경기 시작 시각',
    'hscore':        '홈팀 점수',
    'vscore':        '원정팀 점수',
    'cancel_flag':   '취소 여부 (0/1)',
    'suspended_flag': '서스펜디드 여부 (0/1)',
    'game_flag':     '경기 유형 코드',

    # ── CANCEL_GAME / 스케줄 공통 (대문자) ──
    'ENDYN':      '종료 여부',
    'CANCLE':     '취소 여부',
    'DHEADER':    '더블헤더 번호',
    'SUSPENDED':  '서스펜디드 여부',
    'GMONTH':     '경기 월',
    'GTIME':      '경기 시각',
    'Week':       '요일',
    'attendance': '관중수',
    'HOME':       '홈팀 코드',
    'VISIT':      '원정팀 코드',
    'HSCORE':     '홈팀 점수',
    'VSCORE':     '원정팀 점수',
    'BROADCAST1': '방송사 1',
    'BROADCAST2': '방송사 2',
    'broadcast3': '방송사 3',
    'broadcast4': '방송사 4',
    'stadium':    '구장 코드',
    'gyear':      '연도',
    'gmkey':      '경기 고유키',
    'gamedate':   '경기 일자',

    # ── IE 실시간 (공통) ──
    'LiveText':    '실시간 문자 중계 텍스트',
    'LIVETEXT':    '실시간 문자 중계 텍스트',
    'textStyle':   '텍스트 스타일 코드',
    'Inning':      '이닝',
    'inning':      '이닝',
    'bTop':        '초/말 구분 (1=초, 0=말)',
    'bHome':       '홈팀 여부',
    'SeqNO':       '순번',
    'STATUS_ID':   '경기 상태 코드',
    'GAMEID':      '경기 ID',
    'gameID':      '경기 ID',
    'REG_DT':      '등록 일시',
    'INPUTTIME':   '입력 시각',
    'InsertedTime': '데이터 입력 시각',

    # ── IE_BallCount ──
    'strike':    '스트라이크 카운트',
    'ball':      '볼 카운트',
    'out':       '아웃 카운트',
    'base1':     '1루 주자 여부',
    'base2':     '2루 주자 여부',
    'base3':     '3루 주자 여부',
    'pitcher':   '투수 선수 코드',
    'batter':    '타자 선수 코드',
    'batResult': '타격 결과 텍스트',

    # ── IE_BatterRecord / IE_PitcherRecord ──
    'Position':       '포지션 코드 (숫자)',
    'PositionName':   '포지션명 (EUC-KR)',
    'PlayerName':     '선수명 (EUC-KR)',
    'PlayerID':       '선수 코드',
    'BatOrder':       '타순',
    'OAB':            '상대 타수',
    'Run':            '득점',
    'H1':             '단타',
    'Steal':          '도루',
    'HBP':            '사구 (Hit by Pitch)',
    'SO':             '삼진',
    'TP':             '삼중살 (Triple Play)',
    'Hit':            '안타',
    'Error':          '실책',
    'BallFour':       '볼넷 여부',
    'Score':          '득점',
    'PitchBallCnt':   '볼 투구 수',
    'PitchStrikeCnt': '스트라이크 투구 수',

    # ── IE_GameList ──
    'HomeName':    '홈팀명',
    'HomeMascot':  '홈팀 마스코트명',
    'VisitName':   '원정팀명',
    'VisitMascot': '원정팀 마스코트명',

    # ── IE_ScoreRHEB ──
    # Run, Hit, Error → 위에서 PascalCase로 이미 정의

    # ── IE_Scoreinning ──
    # Score → 위에서 이미 정의

    # ── GAMEINFO_WEATHER ──
    'code':      '관측 지점 코드',
    'area_wide': '광역 지역명',
    'area_city': '시/군 지역명',
    'area_dong': '동/읍/면 지역명',
    'tm':        '관측 시각',
    'icon40':    '날씨 아이콘 코드',
    'temp':      '기온 (℃)',
    'humi':      '습도 (%)',
    'rain':      '강수량',
    'snow':      '적설량',
    'wdirk':     '풍향',
    'wspeed':    '풍속 (m/s)',

    # ── STADIUM ──
    'stadium_key': '구장 코드',

    # ── PitTotal (PascalCase) ──
    'Team': '팀 코드',
    'Hold': '홀드',
}

# ============================================================
# 2. 이닝 패턴 자동 생성
# ============================================================
# Score: {N}T, {N}B
for i in range(1, 26):
    COLUMN_DESC[f'{i}T'] = f'{i}회 초 득점 (-1=미진행)'
    COLUMN_DESC[f'{i}B'] = f'{i}회 말 득점 (-1=미진행)'

# KBO_BATRESULT: INN{N}, IL{N}, INN{N}_3
for i in range(1, 26):
    COLUMN_DESC[f'INN{i}'] = f'{i}회 타격 결과 (HOW 코드, EUC-KR)'
    COLUMN_DESC[f'IL{i}'] = f'{i}회 교체타자 타격 결과'
    COLUMN_DESC[f'INN{i}_3'] = f'{i}회 3아웃 후 타격 결과'

# ============================================================
# 3. 테이블별 오버라이드 (동일 컬럼명이 다른 의미)
# ============================================================
TABLE_OVERRIDES = {
    # BatTotal: TB = 루타 (Total Bases) — 다른 테이블에서는 팀 구분
    ('BatTotal', 'TB'):  '루타 (Total Bases)',
    # KBO_PITRESULT: POS = 등판 순서
    ('KBO_PITRESULT', 'POS'):  '등판 순서 (S=선발, R=구원)',
    ('KBO_PITRESULT', 'CHANGEINN'): '교체 이닝',
    ('KBO_PITRESULT', 'S'):    '피안타',
    ('KBO_PITRESULT', 'BBHP'): '볼넷+사구 합계',
    # Pitcher: POS = 등판 순서
    ('Pitcher', 'POS'): '등판 순서 (S=선발, R=구원)',
}


# ============================================================
# 마크다운 파싱 및 채우기
# ============================================================
# 컬럼 상세 테이블 데이터 행 패턴
ROW_RE = re.compile(
    r'^\|\s*\d+\s*'       # | # |
    r'\|\s*`([^`]+)`\s*'  # | `COL_NAME` |
    r'\|'                  # type 시작
)


def extract_table_name(filepath):
    """파일명에서 테이블명 추출 (확장자 제거)"""
    return Path(filepath).stem


def fill_descriptions(filepath, dry_run=False):
    """하나의 dictionary md 파일의 빈 설명 채움.

    Returns: (filled_count, existing_count, unfilled_names)
    """
    table_name = extract_table_name(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filled = 0
    existing = 0
    unfilled = []

    for i, line in enumerate(lines):
        # 컬럼 상세 테이블 행인지 확인
        m = ROW_RE.match(line)
        if not m:
            continue

        col_name = m.group(1).strip()

        # | 로 분할하여 7번째 필드(설명) 확인
        parts = line.split('|')
        # parts: ['', ' # ', ' `COL` ', ' type ', ' len ', ' NULL ', ' PK ', ' desc ', ' std ', '\n']
        if len(parts) < 9:
            continue

        desc = parts[7].strip()
        if desc:
            existing += 1
            continue

        # 설명 조회: TABLE_OVERRIDES 우선 → COLUMN_DESC
        new_desc = TABLE_OVERRIDES.get((table_name, col_name))
        if not new_desc:
            new_desc = COLUMN_DESC.get(col_name, '')

        if not new_desc:
            unfilled.append(col_name)
            continue

        # 설명 채우기
        parts[7] = f' {new_desc} '
        lines[i] = '|'.join(parts)
        filled += 1

    if filled > 0 and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    return filled, existing, unfilled


def main():
    dry_run = '--dry-run' in sys.argv

    print("=" * 60)
    print("컬럼 설명 채우기 (fill-descriptions.py)")
    if dry_run:
        print("  *** DRY-RUN 모드: 파일 수정 없이 미리보기 ***")
    print("=" * 60)

    total_filled = 0
    total_existing = 0
    total_unfilled = 0
    files_modified = 0
    all_unfilled = []

    for domain in sorted(os.listdir(DICT_DIR)):
        domain_path = os.path.join(DICT_DIR, domain)
        if not os.path.isdir(domain_path):
            continue

        for fname in sorted(os.listdir(domain_path)):
            if not fname.endswith('.md') or fname == 'README.md':
                continue

            filepath = os.path.join(domain_path, fname)
            filled, existing, unfilled = fill_descriptions(filepath, dry_run)

            total_filled += filled
            total_existing += existing
            total_unfilled += len(unfilled)

            if filled > 0 or unfilled:
                files_modified += (1 if filled > 0 else 0)
                status = f"+{filled}" if filled > 0 else " 0"
                msg = f"  {domain}/{fname}: {status} 설명 추가 (기존 {existing})"
                if unfilled:
                    msg += f"  [미해결 {len(unfilled)}개: {', '.join(unfilled)}]"
                print(msg)
                all_unfilled.extend(
                    (domain, fname, c) for c in unfilled
                )

    total_cols = total_filled + total_existing + total_unfilled
    coverage = (total_existing + total_filled) / total_cols * 100 if total_cols else 0

    print(f"\n{'=' * 60}")
    print(f"결과 요약")
    print(f"{'=' * 60}")
    print(f"  전체 컬럼:   {total_cols}")
    print(f"  기존 설명:   {total_existing}")
    print(f"  신규 추가:   {total_filled} ({files_modified}개 파일)")
    print(f"  미해결:      {total_unfilled}")
    print(f"  커버리지:    {coverage:.1f}%")

    if all_unfilled:
        print(f"\n미해결 컬럼 목록:")
        for domain, fname, col in all_unfilled:
            print(f"  {domain}/{fname}: {col}")

    if dry_run and total_filled > 0:
        print(f"\n*** DRY-RUN: 실제 적용하려면 --dry-run 없이 실행하세요 ***")


if __name__ == '__main__':
    main()
