#!/usr/bin/env python3
"""
DB 실제 데이터 분석 스크립트
- 코드성 컬럼의 고유값 추출
- 식별자(GMKEY, PCODE 등) 패턴 분석
- 결과를 raw/data-samples.json에 저장
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

# 분석 대상: 가장 완전한 DB2_BASEBALL_220328 (1군 정규시즌)
DB = 'DB2_BASEBALL_220328'
DB_NEW = 'DB2_BASEBALL_NEW_220328'
DB_MINOR = 'DB2_MINOR_BASEBALL_220328'
DB_SEASON = 'DB2_BASEBALL_2_220328'

def safe_query(cursor, query, label=""):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"  [WARN] {label}: {e}")
        return []

def main():
    conn = pymssql.connect(server=SERVER, port=PORT, user=USER, password=PASSWORD, database='master')
    cursor = conn.cursor()
    results = {}

    print("=== 1. 코드성 컬럼 고유값 추출 ===\n")

    # 코드성 컬럼 추출 쿼리들
    code_queries = {
        # BatTotal
        'BatTotal.SEC': f"SELECT DISTINCT SEC FROM [{DB}].dbo.BatTotal ORDER BY SEC",
        # ENTRY
        'ENTRY.TEAM': f"SELECT DISTINCT TEAM FROM [{DB}].dbo.ENTRY ORDER BY TEAM",
        'ENTRY.POSI': f"SELECT DISTINCT POSI FROM [{DB}].dbo.ENTRY ORDER BY POSI",
        'ENTRY.TURN': f"SELECT DISTINCT TOP 30 TURN FROM [{DB}].dbo.ENTRY ORDER BY TURN",
        # DEFEN
        'DEFEN.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.DEFEN ORDER BY TB",
        'DEFEN.POSI': f"SELECT DISTINCT POSI FROM [{DB}].dbo.DEFEN ORDER BY POSI",
        # GAMECONTAPP
        'GAMECONTAPP.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.GAMECONTAPP ORDER BY TB",
        'GAMECONTAPP.HOW': f"SELECT DISTINCT HOW FROM [{DB}].dbo.GAMECONTAPP ORDER BY HOW",
        'GAMECONTAPP.PLACE': f"SELECT DISTINCT PLACE FROM [{DB}].dbo.GAMECONTAPP ORDER BY PLACE",
        'GAMECONTAPP.OCOUNT': f"SELECT DISTINCT OCOUNT FROM [{DB}].dbo.GAMECONTAPP ORDER BY OCOUNT",
        'GAMECONTAPP.INN': f"SELECT DISTINCT INN FROM [{DB}].dbo.GAMECONTAPP ORDER BY INN",
        'GAMECONTAPP.INN2': f"SELECT DISTINCT INN2 FROM [{DB}].dbo.GAMECONTAPP ORDER BY INN2",
        # GAMEINFO
        'GAMEINFO.SESSION(cancel)': f"SELECT DISTINCT SESSION FROM [{DB}].dbo.GAMEINFO ORDER BY SESSION",
        'GAMEINFO.STADIUM': f"SELECT DISTINCT STADIUM FROM [{DB}].dbo.GAMEINFO ORDER BY STADIUM",
        'GAMEINFO.HTEAM': f"SELECT DISTINCT HTEAM FROM [{DB}].dbo.GAMEINFO ORDER BY HTEAM",
        'GAMEINFO.ATEAM': f"SELECT DISTINCT ATEAM FROM [{DB}].dbo.GAMEINFO ORDER BY ATEAM",
        # Hitter
        'Hitter.POSI': f"SELECT DISTINCT POSI FROM [{DB}].dbo.Hitter ORDER BY POSI",
        'Hitter.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.Hitter ORDER BY TB",
        # Score
        'Score.TB': f"SELECT DISTINCT TB FROM [{DB}].dbo.Score ORDER BY TB",
        # KBO_BATRESULT
        'KBO_BATRESULT.PLACE': f"SELECT DISTINCT PLACE FROM [{DB}].dbo.KBO_BATRESULT ORDER BY PLACE",
        'KBO_BATRESULT.BALLCOUNT': f"SELECT DISTINCT TOP 30 BALLCOUNT FROM [{DB}].dbo.KBO_BATRESULT ORDER BY BALLCOUNT",
        'KBO_BATRESULT.HOW': f"SELECT DISTINCT HOW FROM [{DB}].dbo.KBO_BATRESULT ORDER BY HOW",
        # KBO_PITRESULT
        'KBO_PITRESULT.PLACE': f"SELECT DISTINCT PLACE FROM [{DB}].dbo.KBO_PITRESULT ORDER BY PLACE",
        # GAME_MEMO
        'GAME_MEMO.SESSION': f"SELECT DISTINCT SESSION FROM [{DB}].dbo.GAME_MEMO ORDER BY SESSION",
        # person (NEW DB)
        'person.POSITION': f"SELECT DISTINCT POSITION FROM [{DB_NEW}].dbo.person ORDER BY POSITION",
        'person.POSI': f"SELECT DISTINCT POSI FROM [{DB_NEW}].dbo.person ORDER BY POSI",
        'person.T_CD': f"SELECT DISTINCT T_CD FROM [{DB_NEW}].dbo.person ORDER BY T_CD",
        'person.HITTYPE': f"SELECT DISTINCT HITTYPE FROM [{DB_NEW}].dbo.person ORDER BY HITTYPE",
        # KBO_schedule
        'KBO_schedule.S_NM': f"SELECT DISTINCT S_NM FROM [{DB_NEW}].dbo.KBO_schedule ORDER BY S_NM",
        'KBO_schedule.T_NM': f"SELECT DISTINCT T_NM FROM [{DB_NEW}].dbo.KBO_schedule ORDER BY T_NM",
        'KBO_schedule.HOME_NM': f"SELECT DISTINCT HOME_NM FROM [{DB_NEW}].dbo.KBO_schedule ORDER BY HOME_NM",
        'KBO_schedule.AWAY_NM': f"SELECT DISTINCT AWAY_NM FROM [{DB_NEW}].dbo.KBO_schedule ORDER BY AWAY_NM",
        # TEAM
        'TEAM.T_NM': f"SELECT DISTINCT T_NM FROM [{DB_SEASON}].dbo.TEAM ORDER BY T_NM",
        # STADIUM
        'STADIUM.S_NM': f"SELECT DISTINCT S_NM FROM [{DB_NEW}].dbo.STADIUM ORDER BY S_NM",
        # TeamRank
        'TeamRank.TEAM': f"SELECT DISTINCT TEAM FROM [{DB}].dbo.TeamRank ORDER BY TEAM",
        # MINOR - PERSON
        'MINOR_PERSON.POSITION': f"SELECT DISTINCT POSITION FROM [{DB_MINOR}].dbo.PERSON ORDER BY POSITION",
        'MINOR_PERSON.POSI': f"SELECT DISTINCT POSI FROM [{DB_MINOR}].dbo.PERSON ORDER BY POSI",
        # GAMEINFO_WEATHER
        'GAMEINFO_WEATHER.WEATHER': f"SELECT DISTINCT WEATHER FROM [{DB}].dbo.GAMEINFO_WEATHER ORDER BY WEATHER",
        # PITCHCLOCK
        'PITCHCLOCK.VIOLATION_TYPE': f"SELECT DISTINCT VIOLATION_TYPE FROM [{DB}].dbo.PITCHCLOCK ORDER BY VIOLATION_TYPE",
        'PITCHCLOCK.VIOLATION_RESULT': f"SELECT DISTINCT VIOLATION_RESULT FROM [{DB}].dbo.PITCHCLOCK ORDER BY VIOLATION_RESULT",
    }

    for label, query in code_queries.items():
        print(f"  {label}...", end=" ")
        rows = safe_query(cursor, query, label)
        vals = [str(r[0]).strip() if r[0] is not None else 'NULL' for r in rows]
        results[label] = vals
        print(f"{len(vals)} values: {vals[:15]}{'...' if len(vals)>15 else ''}")
        time.sleep(0.1)

    print("\n=== 2. 식별자 샘플 추출 ===\n")

    id_queries = {
        # GMKEY 패턴 분석
        'GMKEY_samples': f"SELECT DISTINCT TOP 30 GMKEY FROM [{DB}].dbo.GAMEINFO ORDER BY GMKEY",
        'GMKEY_length': f"SELECT DISTINCT LEN(GMKEY) as len FROM [{DB}].dbo.GAMEINFO",
        'GMKEY_pattern': f"SELECT TOP 5 GMKEY, GDAY, STADIUM, HTEAM, ATEAM, GYEAR FROM [{DB}].dbo.GAMEINFO ORDER BY GMKEY",
        # PCODE 패턴
        'PCODE_samples': f"SELECT DISTINCT TOP 30 PCODE FROM [{DB}].dbo.ENTRY ORDER BY PCODE",
        'PCODE_length': f"SELECT DISTINCT LEN(PCODE) as len FROM [{DB}].dbo.ENTRY",
        # person 키
        'person_PCODE_samples': f"SELECT TOP 20 PCODE, P_NM, BIRTH, T_CD, POSITION, POSI, HITTYPE FROM [{DB_NEW}].dbo.person ORDER BY PCODE",
        'person2_samples': f"SELECT TOP 10 * FROM [{DB_NEW}].dbo.person2",
        # SERNO 범위
        'GAMECONTAPP_SERNO_range': f"SELECT MIN(SERNO), MAX(SERNO), COUNT(DISTINCT SERNO) FROM [{DB}].dbo.GAMECONTAPP",
        # GYEAR 범위
        'GYEAR_range': f"SELECT DISTINCT GYEAR FROM [{DB}].dbo.GAMEINFO ORDER BY GYEAR",
        # CANCEL_GAME 샘플
        'CANCEL_GAME_samples': f"SELECT TOP 10 * FROM [{DB_NEW}].dbo.CANCEL_GAME ORDER BY GMKEY",
        # KBO_schedule 식별자
        'KBO_schedule_samples': f"SELECT TOP 10 GMKEY, G_DT, G_TM, S_NM, HOME_NM, AWAY_NM FROM [{DB_NEW}].dbo.KBO_schedule ORDER BY GMKEY DESC",
        # GAME_HR 샘플
        'GAME_HR_samples': f"SELECT TOP 10 * FROM [{DB}].dbo.GAME_HR ORDER BY GMKEY DESC",
        # GAMEINFO 전체 컬럼 샘플
        'GAMEINFO_full_sample': f"SELECT TOP 3 * FROM [{DB}].dbo.GAMEINFO ORDER BY GMKEY DESC",
        # Score 전체 컬럼 샘플
        'Score_full_sample': f"SELECT TOP 2 * FROM [{DB}].dbo.Score ORDER BY GMKEY DESC",
        # PERSON_FA 샘플
        'PERSON_FA_samples': f"SELECT TOP 10 * FROM [{DB_NEW}].dbo.PERSON_FA",
        # STADIUM 전체
        'STADIUM_all': f"SELECT * FROM [{DB_NEW}].dbo.STADIUM",
        # DB1 누적 GMKEY 범위
        'DB1_GMKEY_range': f"SELECT MIN(GMKEY) as min_key, MAX(GMKEY) as max_key FROM [DB1_BASEBALL_220328].dbo.GAMEINFO",
        # DB1 GYEAR 범위
        'DB1_GYEAR_range': f"SELECT DISTINCT GYEAR FROM [DB1_BASEBALL_220328].dbo.GAMEINFO ORDER BY GYEAR",
        # FALL_LEAGUE 샘플
        'FALL_LEAGUE_GAME_KBO': f"SELECT TOP 5 * FROM [FALL_LEAGUE_BASEBALL].dbo.GAME_KBO ORDER BY G_ID DESC",
        # BROADCASTING 샘플
        'BROADCASTING_CD_all': f"SELECT * FROM [BROADCAST_BASEBALL].dbo.BROADCASTING_CD",
        'BROADCASTING_RATE_sample': f"SELECT TOP 5 * FROM [BROADCAST_BASEBALL].dbo.BROADCASTING_RATE ORDER BY GYEAR DESC",
    }

    for label, query in id_queries.items():
        print(f"  {label}...", end=" ")
        rows = safe_query(cursor, query, label)
        if rows:
            # 컬럼명 가져오기
            col_names = [desc[0] for desc in cursor.description] if cursor.description else []
            formatted = []
            for row in rows:
                if col_names:
                    formatted.append({col_names[i]: (str(v).strip() if v is not None else None) for i, v in enumerate(row)})
                else:
                    formatted.append([str(v).strip() if v is not None else None for v in row])
            results[label] = formatted
            print(f"{len(formatted)} rows")
        else:
            results[label] = []
            print("empty")
        time.sleep(0.1)

    print("\n=== 3. 데이터 타입 통계 ===\n")

    # 전체 DB의 컬럼 데이터타입 분포
    type_query = f"""
    SELECT tp.name as data_type, COUNT(*) as cnt
    FROM [{DB}].sys.columns c
    JOIN [{DB}].sys.types tp ON c.user_type_id = tp.user_type_id
    JOIN [{DB}].sys.tables t ON c.object_id = t.object_id
    WHERE t.name NOT LIKE 'MSpeer%' AND t.name NOT LIKE 'sys%' AND t.name != 'dtproperties'
    GROUP BY tp.name
    ORDER BY cnt DESC
    """
    rows = safe_query(cursor, type_query, "data_type_stats")
    results['data_type_distribution'] = {r[0]: r[1] for r in rows}
    print(f"  데이터 타입 분포: {results['data_type_distribution']}")

    conn.close()

    # 결과 저장
    out_path = os.path.join(RAW_DIR, 'data-samples.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n저장 완료: {out_path}")

if __name__ == '__main__':
    main()
