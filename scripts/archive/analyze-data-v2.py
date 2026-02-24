#!/usr/bin/env python3
"""
DB 실제 데이터 분석 스크립트 v2
- charset=UTF8 적용으로 한글 깨짐 해결
- 실제 컬럼명 기반 쿼리
"""
import pymssql
import json
import os
import time
from pathlib import Path

_BASE = str(Path(__file__).resolve().parent.parent.parent)
_env_path = os.path.join(_BASE, ".env")
if os.path.exists(_env_path):
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())

SERVER = os.environ.get("MSSQL_SERVER", "")
PORT = int(os.environ.get("MSSQL_PORT", "1433"))
USER = os.environ.get("MSSQL_USER", "")
PASSWORD = os.environ.get("MSSQL_PASSWORD", "")
RAW_DIR = os.path.join(_BASE, "raw")

DB = 'DB2_BASEBALL_220328'
DB_NEW = 'DB2_BASEBALL_NEW_220328'
DB_MINOR = 'DB2_MINOR_BASEBALL_220328'
DB_SEASON = 'DB2_BASEBALL_2_220328'

def safe_query(cursor, query, label=""):
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description] if cursor.description else []
        return rows, col_names
    except Exception as e:
        print(f"  [WARN] {label}: {str(e)[:80]}")
        return [], []

def rows_to_dicts(rows, cols):
    return [{cols[i]: (str(v).strip() if v is not None else None) for i, v in enumerate(row)} for row in rows]

def main():
    conn = pymssql.connect(server=SERVER, port=PORT, user=USER, password=PASSWORD,
                           database='master', charset='UTF8')
    cursor = conn.cursor()
    results = {}

    # 먼저 각 테이블의 실제 컬럼명 확인
    print("=== 0. 실제 컬럼명 확인 ===\n")
    check_tables = [
        (DB, 'GAMEINFO'), (DB, 'GAMECONTAPP'), (DB, 'Hitter'), (DB, 'Pitcher'),
        (DB, 'Score'), (DB, 'KBO_BATRESULT'), (DB, 'KBO_PITRESULT'),
        (DB, 'GAME_MEMO'), (DB, 'GAME_HR'), (DB, 'GAMEINFO_WEATHER'),
        (DB, 'PITCHCLOCK'), (DB, 'DEFEN'), (DB, 'ENTRY'), (DB, 'BatTotal'),
        (DB_NEW, 'person'), (DB_NEW, 'person2'), (DB_NEW, 'CANCEL_GAME'),
        (DB_NEW, 'KBO_schedule'), (DB_NEW, 'STADIUM'), (DB_NEW, 'PERSON_FA'),
        (DB_SEASON, 'TEAM'), (DB_SEASON, 'SEASON_PLAYER_HITTER'),
        (DB_MINOR, 'PERSON'), (DB_MINOR, 'KBO_SCHEDULE'),
    ]

    actual_columns = {}
    for db, table in check_tables:
        key = f"{db}.{table}"
        rows, _ = safe_query(cursor,
            f"SELECT c.name FROM [{db}].sys.columns c JOIN [{db}].sys.tables t ON c.object_id=t.object_id WHERE t.name='{table}' ORDER BY c.column_id",
            key)
        cols = [r[0] for r in rows]
        actual_columns[key] = cols
        print(f"  {table:30s} ({db[:20]}): {cols}")
        time.sleep(0.05)

    print("\n=== 1. 코드성 컬럼 고유값 추출 ===\n")

    code_queries = {
        # BatTotal - SEC (시즌구분 코드)
        'BatTotal.SEC': f"SELECT SEC, COUNT(*) cnt FROM [{DB}].dbo.BatTotal GROUP BY SEC ORDER BY SEC",
        # ENTRY - TB (팀구분: T=홈, B=원정), POSI (포지션)
        'ENTRY.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.ENTRY ORDER BY TB",
        'ENTRY.POSI': f"SELECT POSI, COUNT(*) cnt FROM [{DB}].dbo.ENTRY GROUP BY POSI ORDER BY POSI",
        # DEFEN - TB, POSI
        'DEFEN.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.DEFEN ORDER BY TB",
        'DEFEN.POSI': f"SELECT POSI, COUNT(*) cnt FROM [{DB}].dbo.DEFEN GROUP BY POSI ORDER BY POSI",
        # GAMECONTAPP - HOW (결과코드), PLACE, TB, INN
        'GAMECONTAPP.HOW': f"SELECT HOW, COUNT(*) cnt FROM [{DB}].dbo.GAMECONTAPP GROUP BY HOW ORDER BY HOW",
        'GAMECONTAPP.PLACE': f"SELECT PLACE, COUNT(*) cnt FROM [{DB}].dbo.GAMECONTAPP GROUP BY PLACE ORDER BY PLACE",
        'GAMECONTAPP.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.GAMECONTAPP ORDER BY TB",
        'GAMECONTAPP.INN2': f"SELECT INN2, COUNT(*) cnt FROM [{DB}].dbo.GAMECONTAPP GROUP BY INN2 ORDER BY INN2",
        # GAMEINFO - STADIUM, HTEAM, VTEAM 등
        'GAMEINFO.STADIUM': f"SELECT DISTINCT STADIUM FROM [{DB}].dbo.GAMEINFO ORDER BY STADIUM",
        'GAMEINFO.HTEAM': f"SELECT DISTINCT HTEAM FROM [{DB}].dbo.GAMEINFO ORDER BY HTEAM",
    }

    # GAMEINFO에 VTEAM이 있는지 확인
    gi_cols = actual_columns.get(f'{DB}.GAMEINFO', [])
    if 'VTEAM' in gi_cols:
        code_queries['GAMEINFO.VTEAM'] = f"SELECT DISTINCT VTEAM FROM [{DB}].dbo.GAMEINFO ORDER BY VTEAM"
    if 'ATEAM' in gi_cols:
        code_queries['GAMEINFO.ATEAM'] = f"SELECT DISTINCT ATEAM FROM [{DB}].dbo.GAMEINFO ORDER BY ATEAM"
    if 'GTIME' in gi_cols:
        code_queries['GAMEINFO.GTIME_sample'] = f"SELECT TOP 5 GTIME FROM [{DB}].dbo.GAMEINFO"
    if 'STADIUM2' in gi_cols:
        code_queries['GAMEINFO.STADIUM2'] = f"SELECT DISTINCT STADIUM2 FROM [{DB}].dbo.GAMEINFO ORDER BY STADIUM2"

    # TeamRank - TEAM
    code_queries['TeamRank.TEAM'] = f"SELECT DISTINCT TEAM FROM [{DB}].dbo.TeamRank ORDER BY TEAM"

    # person POSITION, HITTYPE
    p_cols = actual_columns.get(f'{DB_NEW}.person', [])
    for c in ['POSITION', 'HITTYPE', 'CAREER', 'TEAM']:
        if c in p_cols:
            code_queries[f'person.{c}'] = f"SELECT [{c}], COUNT(*) cnt FROM [{DB_NEW}].dbo.person GROUP BY [{c}] ORDER BY [{c}]"

    # MINOR PERSON
    mp_cols = actual_columns.get(f'{DB_MINOR}.PERSON', [])
    for c in ['POSITION', 'HITTYPE', 'TEAM']:
        if c in mp_cols:
            code_queries[f'MINOR_PERSON.{c}'] = f"SELECT [{c}], COUNT(*) cnt FROM [{DB_MINOR}].dbo.PERSON GROUP BY [{c}] ORDER BY [{c}]"

    # KBO_BATRESULT - 실제 컬럼 기반
    br_cols = actual_columns.get(f'{DB}.KBO_BATRESULT', [])
    for c in ['HOW', 'PLACE', 'GRD', 'BALLCOUNT', 'FIELD']:
        if c in br_cols:
            code_queries[f'KBO_BATRESULT.{c}'] = f"SELECT [{c}], COUNT(*) cnt FROM [{DB}].dbo.KBO_BATRESULT GROUP BY [{c}] ORDER BY cnt DESC"

    # KBO_PITRESULT
    pr_cols = actual_columns.get(f'{DB}.KBO_PITRESULT', [])
    for c in ['HOW', 'PLACE', 'GRD']:
        if c in pr_cols:
            code_queries[f'KBO_PITRESULT.{c}'] = f"SELECT [{c}], COUNT(*) cnt FROM [{DB}].dbo.KBO_PITRESULT GROUP BY [{c}] ORDER BY cnt DESC"

    # PITCHCLOCK
    pc_cols = actual_columns.get(f'{DB}.PITCHCLOCK', [])
    for c in pc_cols:
        if c not in ('GMKEY', 'GDAY', 'SERNO', 'INN', 'INPUTTIME') and 'NAME' not in c and 'CODE' not in c.upper():
            pass
    # 그냥 전체 샘플
    code_queries['PITCHCLOCK_sample'] = f"SELECT TOP 5 * FROM [{DB}].dbo.PITCHCLOCK"

    # GAMEINFO_WEATHER
    gw_cols = actual_columns.get(f'{DB}.GAMEINFO_WEATHER', [])
    for c in gw_cols:
        if c not in ('GMKEY', 'GDAY', 'GYEAR', 'INPUTTIME'):
            code_queries[f'GAMEINFO_WEATHER.{c}'] = f"SELECT DISTINCT [{c}] FROM [{DB}].dbo.GAMEINFO_WEATHER ORDER BY [{c}]"

    # GAME_MEMO
    gm_cols = actual_columns.get(f'{DB}.GAME_MEMO', [])
    for c in ['PLACE', 'HOW', 'SESSION']:
        if c in gm_cols:
            code_queries[f'GAME_MEMO.{c}'] = f"SELECT DISTINCT [{c}] FROM [{DB}].dbo.GAME_MEMO ORDER BY [{c}]"

    # BROADCASTING_CD
    code_queries['BROADCASTING_CD'] = f"SELECT * FROM [BROADCAST_BASEBALL].dbo.BROADCASTING_CD"

    for label, query in code_queries.items():
        print(f"  {label}...", end=" ")
        rows, cols = safe_query(cursor, query, label)
        if cols and len(cols) >= 2:
            data = rows_to_dicts(rows, cols)
            results[label] = data
            print(f"{len(data)} values")
        elif cols:
            vals = [str(r[0]).strip() if r[0] is not None else 'NULL' for r in rows]
            results[label] = vals
            print(f"{len(vals)} values: {vals[:10]}{'...' if len(vals)>10 else ''}")
        else:
            results[label] = []
            print("empty")
        time.sleep(0.1)

    print("\n=== 2. 식별자 샘플 추출 ===\n")

    id_queries = {
        'GMKEY_samples': f"SELECT DISTINCT TOP 30 GMKEY FROM [{DB}].dbo.GAMEINFO ORDER BY GMKEY",
        'GMKEY_length': f"SELECT DISTINCT LEN(GMKEY) as len FROM [{DB}].dbo.GAMEINFO",
        'PCODE_samples': f"SELECT DISTINCT TOP 30 PCODE FROM [{DB}].dbo.ENTRY ORDER BY PCODE",
        'PCODE_length': f"SELECT LEN(PCODE) as len, COUNT(*) cnt FROM [{DB}].dbo.ENTRY GROUP BY LEN(PCODE)",
        'GAMECONTAPP_SERNO': f"SELECT GMKEY, MIN(SERNO) mn, MAX(SERNO) mx, COUNT(*) cnt FROM [{DB}].dbo.GAMECONTAPP GROUP BY GMKEY ORDER BY GMKEY",
    }

    # GAMEINFO full sample - 동적으로 구성
    gi_col_list = ', '.join([f'[{c}]' for c in gi_cols]) if gi_cols else '*'
    id_queries['GAMEINFO_sample'] = f"SELECT TOP 5 {gi_col_list} FROM [{DB}].dbo.GAMEINFO ORDER BY GMKEY DESC"

    # person sample
    if p_cols:
        p_col_list = ', '.join([f'[{c}]' for c in p_cols])
        id_queries['person_sample'] = f"SELECT TOP 20 {p_col_list} FROM [{DB_NEW}].dbo.person ORDER BY PCODE"

    # person2 sample
    p2_cols = actual_columns.get(f'{DB_NEW}.person2', [])
    if p2_cols:
        p2_col_list = ', '.join([f'[{c}]' for c in p2_cols])
        id_queries['person2_sample'] = f"SELECT TOP 15 {p2_col_list} FROM [{DB_NEW}].dbo.person2 ORDER BY PCODE"

    # KBO_schedule sample
    ks_cols = actual_columns.get(f'{DB_NEW}.KBO_schedule', [])
    if ks_cols:
        ks_col_list = ', '.join([f'[{c}]' for c in ks_cols])
        id_queries['KBO_schedule_sample'] = f"SELECT TOP 10 {ks_col_list} FROM [{DB_NEW}].dbo.KBO_schedule ORDER BY GMKEY DESC"

    # CANCEL_GAME
    cg_cols = actual_columns.get(f'{DB_NEW}.CANCEL_GAME', [])
    if cg_cols:
        cg_col_list = ', '.join([f'[{c}]' for c in cg_cols])
        id_queries['CANCEL_GAME_sample'] = f"SELECT TOP 10 {cg_col_list} FROM [{DB_NEW}].dbo.CANCEL_GAME"

    # TEAM
    t_cols = actual_columns.get(f'{DB_SEASON}.TEAM', [])
    if t_cols:
        t_col_list = ', '.join([f'[{c}]' for c in t_cols])
        id_queries['TEAM_all'] = f"SELECT DISTINCT {t_col_list} FROM [{DB_SEASON}].dbo.TEAM ORDER BY 1"

    # STADIUM
    s_cols = actual_columns.get(f'{DB_NEW}.STADIUM', [])
    if s_cols:
        s_col_list = ', '.join([f'[{c}]' for c in s_cols])
        id_queries['STADIUM_all'] = f"SELECT DISTINCT {s_col_list} FROM [{DB_NEW}].dbo.STADIUM ORDER BY 1"

    # PERSON_FA
    id_queries['PERSON_FA_all'] = f"SELECT * FROM [{DB_NEW}].dbo.PERSON_FA"

    # Score sample
    id_queries['Score_sample'] = f"SELECT TOP 2 * FROM [{DB}].dbo.Score ORDER BY GMKEY DESC"

    # DB1 GMKEY 범위 (누적 데이터)
    id_queries['DB1_GMKEY_range'] = f"SELECT MIN(GMKEY) min_key, MAX(GMKEY) max_key, COUNT(*) cnt FROM [DB1_BASEBALL_220328].dbo.GAMEINFO"

    # GAME_HR sample
    gh_cols = actual_columns.get(f'{DB}.GAME_HR', [])
    if gh_cols:
        gh_col_list = ', '.join([f'[{c}]' for c in gh_cols])
        id_queries['GAME_HR_sample'] = f"SELECT TOP 10 {gh_col_list} FROM [{DB}].dbo.GAME_HR ORDER BY GMKEY DESC"

    # Hitter sample
    h_cols = actual_columns.get(f'{DB}.Hitter', [])
    if h_cols:
        h_col_list = ', '.join([f'[{c}]' for c in h_cols])
        id_queries['Hitter_sample'] = f"SELECT TOP 5 {h_col_list} FROM [{DB}].dbo.Hitter ORDER BY GMKEY DESC"

    # Pitcher sample
    pit_cols = actual_columns.get(f'{DB}.Pitcher', [])
    if pit_cols:
        pit_col_list = ', '.join([f'[{c}]' for c in pit_cols])
        id_queries['Pitcher_sample'] = f"SELECT TOP 5 {pit_col_list} FROM [{DB}].dbo.Pitcher ORDER BY GMKEY DESC"

    # KBO_BATRESULT sample
    if br_cols:
        br_col_list = ', '.join([f'[{c}]' for c in br_cols])
        id_queries['KBO_BATRESULT_sample'] = f"SELECT TOP 3 {br_col_list} FROM [{DB}].dbo.KBO_BATRESULT"

    # KBO_PITRESULT sample
    if pr_cols:
        pr_col_list = ', '.join([f'[{c}]' for c in pr_cols])
        id_queries['KBO_PITRESULT_sample'] = f"SELECT TOP 5 {pr_col_list} FROM [{DB}].dbo.KBO_PITRESULT"

    # MINOR KBO_SCHEDULE
    mks_cols = actual_columns.get(f'{DB_MINOR}.KBO_SCHEDULE', [])
    if mks_cols:
        mks_col_list = ', '.join([f'[{c}]' for c in mks_cols])
        id_queries['MINOR_KBO_SCHEDULE_sample'] = f"SELECT TOP 5 {mks_col_list} FROM [{DB_MINOR}].dbo.KBO_SCHEDULE ORDER BY GMKEY DESC"

    # FALL_LEAGUE samples
    id_queries['FALL_LEAGUE_GAME_KBO'] = f"SELECT TOP 5 * FROM [FALL_LEAGUE_BASEBALL].dbo.GAME_KBO ORDER BY G_ID DESC"
    id_queries['FALL_LEAGUE_PERSON_BASE'] = f"SELECT TOP 10 * FROM [FALL_LEAGUE_BASEBALL].dbo.PERSON_BASE"
    id_queries['FALL_LEAGUE_RECORD'] = f"SELECT TOP 5 * FROM [FALL_LEAGUE_BASEBALL].dbo.FALL_LEAGUE_RECORD"

    # BROADCASTING
    id_queries['BROADCASTING_RATE_sample'] = f"SELECT TOP 5 * FROM [BROADCAST_BASEBALL].dbo.BROADCASTING_RATE ORDER BY GYEAR DESC"
    id_queries['BROADCASTING_schedule_sample'] = f"SELECT TOP 5 * FROM [BROADCAST_BASEBALL].dbo.BROADCASTING_schedule ORDER BY GYEAR DESC"

    for label, query in id_queries.items():
        print(f"  {label}...", end=" ")
        rows, cols = safe_query(cursor, query, label)
        if rows and cols:
            if len(cols) == 1:
                results[label] = [str(r[0]).strip() if r[0] is not None else None for r in rows]
            else:
                results[label] = rows_to_dicts(rows, cols)
            print(f"{len(rows)} rows")
        else:
            results[label] = []
            print("empty")
        time.sleep(0.1)

    print("\n=== 3. 데이터 타입 통계 ===\n")

    for db_name in [DB, DB_NEW, DB_MINOR]:
        rows, _ = safe_query(cursor, f"""
            SELECT tp.name, COUNT(*) cnt
            FROM [{db_name}].sys.columns c
            JOIN [{db_name}].sys.types tp ON c.user_type_id = tp.user_type_id
            JOIN [{db_name}].sys.tables t ON c.object_id = t.object_id
            WHERE t.name NOT LIKE 'MSpeer%' AND t.name NOT LIKE 'sys%' AND t.name NOT LIKE 'dt%'
            GROUP BY tp.name ORDER BY cnt DESC
        """, f"types_{db_name}")
        dist = {r[0]: r[1] for r in rows}
        results[f'data_type_dist_{db_name}'] = dist
        print(f"  {db_name}: {dist}")

    conn.close()

    out_path = os.path.join(RAW_DIR, 'data-samples.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n저장 완료: {out_path}")

if __name__ == '__main__':
    main()
