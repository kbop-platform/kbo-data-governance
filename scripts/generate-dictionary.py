#!/usr/bin/env python3
"""column-metadata.json에서 도메인별 테이블 사전 마크다운 생성"""
import json
import os
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)
META_PATH = os.path.join(BASE_DIR, 'raw', 'column-metadata.json')
DICT_DIR = os.path.join(BASE_DIR, 'dictionary')

# 도메인 분류
DOMAINS = {
    'game': {
        'label': '경기 기록',
        'tables': ['GAMEINFO', 'GAMECONTAPP', 'ENTRY', 'Hitter', 'Pitcher',
                    'Score', 'DEFEN', 'GAME_HR', 'GAME_MEMO', 'GAME_MEMO_PITCHCLOCK',
                    'GAMEINFO_WEATHER', 'PITCHCLOCK']
    },
    'stats': {
        'label': '통계/집계',
        'tables': ['BatTotal', 'PitTotal', 'TeamRank', 'KBO_BATRESULT',
                    'KBO_PITRESULT', 'KBO_ETCGAME',
                    'SEASON_PLAYER_HITTER', 'SEASON_PLAYER_PITCHER',
                    'SEASON_PLAYER_HITTER_SITUATION', 'SEASON_PLAYER_PITCHER_SITUATION']
    },
    'realtime': {
        'label': '실시간/인터페이스',
        'tables': ['IE_LiveText', 'IE_BatterRecord', 'IE_PitcherRecord',
                    'IE_BallCount', 'IE_Scoreinning', 'IE_ScoreRHEB',
                    'IE_GameList', 'IE_GAMESTATE', 'IE_log']
    },
    'master': {
        'label': '마스터/참조',
        'tables': ['person', 'person2', 'PERSON', 'PERSON_FA',
                    'TEAM', 'STADIUM', 'KBO_schedule', 'CANCEL_GAME']
    }
}

# 컬럼 설명 매핑 (공통 컬럼)
COLUMN_DESCRIPTIONS = {
    # 식별자
    'GMKEY': '경기 고유키 (YYYYMMDDVVHH#, 13자리)',
    'G_ID': '경기 ID (YYYYMMDDVVHH# 형식)',
    'GDAY': '경기 일자 (YYYYMMDD)',
    'GYEAR': '시즌 연도 (4자리, "9999"=통산)',
    'PCODE': '선수 코드 (5~6자리 숫자 문자열)',
    'P_ID': '선수 ID (정수)',
    'LE_ID': '리그 ID (1=1군)',
    'SR_ID': '시리즈 ID (0=정규시즌)',
    'SEASON_ID': '시즌 ID (연도)',
    'T_ID': '팀 코드 (2자리)',
    'SEQ_NO': '순번',
    'SEQ': '순번',
    'SERNO': '일련번호',
    # 경기 정보
    'TB': '팀 구분 (T=원정/Top, B=홈/Bottom)',
    'TB_SC': '팀 구분 코드 (T=원정, B=홈)',
    'INN': '이닝 번호',
    'INN_NO': '이닝 번호',
    'INN2': '이닝 세부 (아웃수 환산 또는 연장 구분)',
    'OCOUNT': '아웃 카운트 (0,1,2,4=이닝종료)',
    'HOW': '플레이 결과 코드 (H1=안타, HR=홈런, KK=삼진 등 49종)',
    'PLACE': '타구 방향 (0~9=포지션번호, S=삼진 등)',
    'POSI': '포지션 코드 (XY: X=교체순번, Y=포지션)',
    # 타격
    'AB': '타수 (At Bat)',
    'PA': '타석 (Plate Appearance)',
    'HIT': '안타',
    'H2': '2루타',
    'H3': '3루타',
    'HR': '홈런',
    'RBI': '타점',
    'RUN': '득점',
    'BB': '볼넷',
    'HP': '사구 (Hit by Pitch)',
    'IB': '고의사구 (Intentional BB)',
    'KK': '삼진',
    'GD': '병살타',
    'SB': '도루',
    'CS': '도루실패',
    'SF': '희생플라이',
    'SH': '희생번트',
    'ERR': '실책',
    'LOB': '잔루',
    'HRA': '타율',
    'TB_stat': '총루타 (Total Bases)',  # TB as stat vs TB as team
    # 투수
    'W': '승',
    'L': '패',
    'SV': '세이브',
    'HOLD': '홀드',
    'ERA': '평균자책점',
    'ER': '자책점',
    'R': '실점',
    'BF': '상대타자수',
    'NP': '투구수',
    'CG': '완투',
    'SHO': '완봉',
    'WLS': '승패세 (W=승, L=패, S=세이브)',
    'BK': '보크',
    'WP': '폭투',
    # 팀/기타
    'TEAM': '팀 코드 (2자리, HH=키움, HT=KIA 등)',
    'NAME': '선수명 (varchar=EUC-KR 깨짐 가능)',
    'LEAGUE': '리그',
    'RANK': '순위',
    'GAME': '경기 수',
    'GAMENUM': '경기 수',
    'WIN': '승',
    'LOSE': '패',
    'SAME': '무승부',
    'WRA': '승률',
    'SEC': '구간 (시즌연도 또는 "9999"=통산)',
    'TURN': '타순',
    'ONETURN': '타순 (1~9)',
    'START': '선발 여부',
    'QUIT': '종료 여부',
    'INPUTTIME': '입력 시각',
    'REG_DT': '등록 일시',
    # IE
    'gameID': '경기 ID (GMKEY와 동일 형식)',
    'GAMEID': '경기 ID',
    'SeqNO': '순번',
    'BatOrder': '타순',
    'PlayerID': '선수 코드',
    'bHome': '홈팀 여부',
    'inning': '이닝',
    'STATUS_ID': '경기 상태 코드',
    'LIVETEXT': '실시간 문자 중계 텍스트',
    # 스케줄
    'HOME': '홈팀 코드',
    'VISIT': '원정팀 코드',
    'HSCORE': '홈팀 점수',
    'VSCORE': '원정팀 점수',
    'STADIUM': '구장',
    'SNAME': '구장명',
    'ENDYN': '종료 여부',
    'CANCLE': '취소 여부',
    'DHEADER': '더블헤더 번호',
    'SUSPENDED': '서스펜디드 여부',
    'GMONTH': '경기 월',
    'GTIME': '경기 시간',
    'Week': '요일',
    'attendance': '관중수',
    'game_flag': '경기 유형 플래그',
    'BROADCAST1': '방송사1',
    'BROADCAST2': '방송사2',
    'broadcast3': '방송사3',
    'broadcast4': '방송사4',
    # 마스터
    'stadium': '구장 코드',
    'gyear': '연도',
    'gmkey': '경기 고유키',
    'gamedate': '경기 일자',
    # 선수
    'BIRTH': '생년월일',
    'HEIGHT': '키',
    'WEIGHT': '몸무게',
    'CAREER': '경력',
    'HAND': '투타 (좌/우)',
    'HITTYPE': '타석 방향',
    'POSITION': '포지션',
    'INDATE': '입단일',
    'NUM': '등번호',
    # Score
    'CONT': '연속 기록',
    'CONTINUE': '연속 기록',
    'continue': '연속 기록',
    # 기타
    'RESULT': '결과',
    'BESSION': '세션',
    'FIRST_IF': '첫 여부 플래그',
    'LAST_IF': '마지막 여부 플래그',
    'SECTION_CD': '구간 코드',
    'GROUP_IF': '그룹 여부',
    'SITUATION_IF': '상황 구분',
}

def get_description(col_name, data_type, distinct_values):
    """컬럼 설명 생성"""
    # 직접 매핑
    if col_name in COLUMN_DESCRIPTIONS:
        return COLUMN_DESCRIPTIONS[col_name]

    # TB는 맥락에 따라 다름 (타격 테이블에서는 총루타, 경기에서는 팀구분)
    if col_name == 'TB' and data_type == 'int':
        return '총루타 (Total Bases)'

    # INN 이닝 관련
    if col_name.startswith('INN') and col_name not in ('INN', 'INN2', 'INN_NO'):
        return f'이닝 점수 컬럼'

    # Score 이닝 컬럼
    for prefix in ('T', 'B'):
        for i in range(1, 26):
            if col_name == f'{prefix}{i}':
                side = '원정' if prefix == 'T' else '홈'
                return f'{i}회 {side}팀 점수'

    # _CN, _RT, _IF, _SC 접미사
    if col_name.endswith('_CN'):
        return f'{col_name[:-3]} 건수'
    if col_name.endswith('_RT'):
        return f'{col_name[:-3]} 비율'
    if col_name.endswith('_IF'):
        return f'{col_name[:-3]} 여부 (Y/N)'
    if col_name.endswith('_SC'):
        return f'{col_name[:-3]} 상태코드'
    if col_name.endswith('_CD'):
        return f'{col_name[:-3]} 코드'
    if col_name.endswith('_VA'):
        return f'{col_name[:-3]} 값'
    if col_name.endswith('_ME'):
        return f'{col_name[:-3]} 메모'
    if col_name.endswith('_NM'):
        return f'{col_name[:-3]} 명칭'
    if col_name.endswith('_DT'):
        return f'{col_name[:-3]} 일시'
    if col_name.endswith('_TM'):
        return f'{col_name[:-3]} 시각'
    if col_name.endswith('_NO'):
        return f'{col_name[:-3]} 번호'

    return ''

def format_distinct(distinct_values, max_show=8):
    """코드값 포맷"""
    if not distinct_values:
        return ''
    items = []
    for d in distinct_values[:max_show]:
        v = d['value']
        c = d['count']
        items.append(f'`{v}`({c:,})')
    rest = len(distinct_values) - max_show
    result = ', '.join(items)
    if rest > 0:
        result += f' 외 {rest}건'
    return result

def generate_table_md(table_name, meta):
    """하나의 테이블에 대한 마크다운 생성"""
    lines = []
    lines.append(f"# {table_name}")
    lines.append("")

    lines.append(f"| 항목 | 값 |")
    lines.append(f"|------|-----|")
    lines.append(f"| 대표 DB | `{meta['representative_db']}` |")
    lines.append(f"| 행 수 | {meta['row_count']:,} |")
    lines.append(f"| 컬럼 수 | {meta['column_count']} |")
    lines.append(f"| PK | `{', '.join(meta['pk_columns'])}` |")
    lines.append(f"| 스키마 세대 | {meta['schema_generation']} |")
    lines.append("")

    lines.append("## 컬럼 상세")
    lines.append("")
    lines.append("| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 |")
    lines.append("|---|--------|------|------|------|----|------|")

    for col in meta['columns']:
        pk = "PK" if col['is_pk'] else ""
        null = "" if col['is_nullable'] else "NN"
        desc = get_description(col['name'], col['data_type'], col.get('distinct_values'))
        # 길이 표시
        if col['data_type'] in ('int', 'bigint', 'smallint', 'tinyint', 'bit', 'float', 'real', 'datetime', 'datetime2', 'date', 'time'):
            length = ''
        else:
            length = str(col['max_length'])

        lines.append(f"| {col['ordinal']} | `{col['name']}` | {col['data_type']} | {length} | {null} | {pk} | {desc} |")

    # 코드값 섹션
    code_cols = [c for c in meta['columns'] if c.get('distinct_values')]
    if code_cols:
        lines.append("")
        lines.append("## 코드값 / 고유값")
        lines.append("")
        for col in code_cols:
            lines.append(f"### `{col['name']}`")
            lines.append("")
            lines.append(f"| 값 | 건수 |")
            lines.append(f"|-----|------|")
            for d in col['distinct_values'][:20]:
                lines.append(f"| `{d['value']}` | {d['count']:,} |")
            lines.append("")

    # 샘플 데이터
    lines.append("## 샘플 데이터")
    lines.append("")
    lines.append("| 컬럼 | 샘플 |")
    lines.append("|------|------|")
    for col in meta['columns']:
        samples = col.get('sample_values', [])
        if samples:
            sample_str = ', '.join(f'`{s}`' for s in samples[:3])
        else:
            sample_str = '(NULL)'
        lines.append(f"| `{col['name']}` | {sample_str} |")
    lines.append("")

    return '\n'.join(lines)


def main():
    with open(META_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 도메인별 디렉토리 생성 및 파일 생성
    for domain, info in DOMAINS.items():
        domain_dir = os.path.join(DICT_DIR, domain)
        os.makedirs(domain_dir, exist_ok=True)

        # 도메인 인덱스
        index_lines = [f"# {info['label']} 테이블 사전", ""]
        index_lines.append(f"| 테이블 | 컬럼 수 | 행 수 | PK | 스키마 |")
        index_lines.append(f"|--------|--------|-------|-----|--------|")

        for tname in info['tables']:
            if tname not in data['tables']:
                print(f"  SKIP: {tname} (not in metadata)")
                continue

            meta = data['tables'][tname]
            pk_str = ', '.join(meta['pk_columns'])
            index_lines.append(f"| [{tname}](./{tname}.md) | {meta['column_count']} | {meta['row_count']:,} | {pk_str} | {meta['schema_generation']} |")

            # 개별 파일
            md = generate_table_md(tname, meta)
            out_path = os.path.join(domain_dir, f"{tname}.md")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md)
            print(f"  {domain}/{tname}.md ({meta['column_count']} cols)")

        index_lines.append("")
        index_path = os.path.join(domain_dir, "README.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(index_lines))
        print(f"  {domain}/README.md")

    print(f"\nDone. Generated {sum(len(d['tables']) for d in DOMAINS.values())} table docs in {len(DOMAINS)} domains.")

if __name__ == '__main__':
    main()
