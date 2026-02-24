#!/usr/bin/env python3
"""40종 테이블 컬럼 메타데이터 + 샘플 추출"""
import pymssql
import json
import os
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)

# Load credentials from .env
_env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(_env_path):
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())

SERVER = os.environ.get("MSSQL_SERVER", "") + ":" + os.environ.get("MSSQL_PORT", "1433")
USER = os.environ.get("MSSQL_USER", "")
PASSWORD = os.environ.get("MSSQL_PASSWORD", "")

# 테이블별 대표 DB 선정 (가장 데이터 많은 DB 우선)
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

# 코드성 컬럼 판별
CODE_NAMES = {'TB', 'HOW', 'PLACE', 'POSI', 'WLS', 'LEAGUE', 'TEAM', 'WEATH',
              'START', 'QUIT', 'OCOUNT', 'ENDYN', 'CANCLE', 'DHEADER',
              'TB_SC', 'PLACE_SC', 'DIREC_SC', 'PIT_RESULT_SC',
              'STATUS_ID', 'LE_ID', 'SR_ID', 'SEASON_ID',
              'SUSPENDED', 'game_flag', 'FIRST_IF', 'LAST_IF', 'RESULT'}

def is_code_column(col_name, data_type, max_length):
    if col_name.upper() in {n.upper() for n in CODE_NAMES}:
        return True
    for suffix in ('_SC', '_CD', '_ID', '_IF', '_FLAG', '_TYPE'):
        if col_name.upper().endswith(suffix):
            return True
    if data_type in ('char', 'varchar', 'nchar', 'nvarchar') and max_length <= 10:
        return True
    if data_type in ('tinyint', 'smallint', 'bit'):
        return True
    return False

def get_schema_gen(columns):
    names = {c['name'].upper() for c in columns}
    if 'G_ID' in names or 'LE_ID' in names or 'P_ID' in names:
        return 'new'
    if 'GMKEY' in names or 'PCODE' in names:
        return 'legacy'
    return 'unknown'

def main():
    result = {"tables": {}}
    conn = pymssql.connect(SERVER, USER, PASSWORD)
    cursor = conn.cursor()

    for table_name, db_name in sorted(TABLE_DB_MAP.items()):
        print(f"\n{'='*60}")
        print(f"  {table_name} @ {db_name}")
        print(f"{'='*60}")

        cursor.execute(f"USE [{db_name}]")

        # 1) 컬럼 메타데이터
        cursor.execute(f"""
            SELECT
                c.name AS col_name,
                t.name AS data_type,
                c.max_length,
                c.is_nullable,
                c.column_id,
                CASE WHEN ic.column_id IS NOT NULL THEN 1 ELSE 0 END AS is_pk
            FROM sys.columns c
            JOIN sys.types t ON c.user_type_id = t.user_type_id
            LEFT JOIN (
                SELECT ic.object_id, ic.column_id
                FROM sys.index_columns ic
                JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
                WHERE i.is_primary_key = 1
            ) ic ON c.object_id = ic.object_id AND c.column_id = ic.column_id
            WHERE c.object_id = OBJECT_ID('{table_name}')
            ORDER BY c.column_id
        """)
        cols_raw = cursor.fetchall()

        if not cols_raw:
            print(f"  WARNING: no columns found")
            continue

        # row count
        try:
            cursor.execute(f"""
                SELECT SUM(p.rows) FROM sys.partitions p
                JOIN sys.tables t ON p.object_id = t.object_id
                WHERE t.name = '{table_name}' AND p.index_id IN (0,1)
            """)
            row_count = cursor.fetchone()[0] or 0
        except:
            row_count = 0

        columns = []
        for col_name, dtype, max_len, is_null, ordinal, is_pk in cols_raw:
            # nvarchar max_length is in bytes (×2)
            display_len = max_len
            if dtype in ('nvarchar', 'nchar') and max_len > 0:
                display_len = max_len // 2

            col = {
                "name": col_name,
                "data_type": dtype,
                "max_length": display_len,
                "is_nullable": bool(is_null),
                "is_pk": bool(is_pk),
                "ordinal": ordinal,
                "sample_values": [],
                "distinct_values": None
            }

            # 2) 샘플 (TOP 3)
            try:
                cursor.execute(f"SELECT TOP 3 [{col_name}] FROM [{table_name}] WHERE [{col_name}] IS NOT NULL")
                samples = [str(r[0]).strip() for r in cursor.fetchall()]
                col["sample_values"] = samples[:3]
            except Exception as e:
                col["sample_values"] = [f"ERROR: {e}"]

            # 3) 코드성 컬럼이면 distinct values
            if is_code_column(col_name, dtype, display_len):
                try:
                    cursor.execute(f"""
                        SELECT TOP 20 [{col_name}], COUNT(*) as cnt
                        FROM [{table_name}]
                        WHERE [{col_name}] IS NOT NULL
                        GROUP BY [{col_name}]
                        ORDER BY cnt DESC
                    """)
                    distincts = [{"value": str(r[0]).strip(), "count": r[1]} for r in cursor.fetchall()]
                    col["distinct_values"] = distincts
                except Exception as e:
                    col["distinct_values"] = [{"value": f"ERROR: {e}", "count": 0}]

            columns.append(col)

        schema_gen = get_schema_gen(columns)
        pk_cols = [c['name'] for c in columns if c['is_pk']]

        result["tables"][table_name] = {
            "representative_db": db_name,
            "row_count": row_count,
            "schema_generation": schema_gen,
            "pk_columns": pk_cols,
            "column_count": len(columns),
            "columns": columns
        }

        print(f"  Columns: {len(columns)}, Rows: {row_count:,}, Schema: {schema_gen}")
        print(f"  PK: {pk_cols}")
        for c in columns:
            pk_mark = " [PK]" if c['is_pk'] else ""
            null_mark = " NULL" if c['is_nullable'] else " NN"
            sample = c['sample_values'][:2]
            dv = ""
            if c['distinct_values']:
                vals = [d['value'] for d in c['distinct_values'][:5]]
                dv = f" codes={vals}"
            print(f"    {c['ordinal']:2d}. {c['name']:30s} {c['data_type']:10s}({c['max_length']}){null_mark}{pk_mark} ex:{sample}{dv}")

    conn.close()

    out_path = os.path.join(BASE_DIR, 'raw', 'column-metadata.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n\nSaved to {out_path}")
    print(f"Tables: {len(result['tables'])}")

if __name__ == '__main__':
    main()
