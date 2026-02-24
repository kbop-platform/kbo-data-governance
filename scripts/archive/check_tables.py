#!/usr/bin/env python3
"""주요 DB별 테이블 구조 조회 스크립트"""
import pymssql
import time
import os
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

def connect():
    return pymssql.connect(server=SERVER, port=PORT, user=USER, password=PASSWORD, database='master')

def main():
    conn = connect()
    cursor = conn.cursor()

    # TEST_ 와 시스템 DB 제외한 주요 DB 목록
    main_dbs = [
        'DB1_BASEBALL_220328', 'DB1_BASEBALL_2_220328',
        'DB2_BASEBALL_220328', 'DB2_BASEBALL_2_220328', 'DB2_BASEBALL_NEW_220328',
        'DB2_POSTSEASON', 'DB2_ALLSTAR', 'DB2_EXHIBITION', 'DB2_INTERNATIONAL',
        'DB1_MINOR_BASEBALL_220328', 'DB1_MINOR_SO_BASEBALL',
        'DB2_MINOR_BASEBALL_220328', 'DB2_MINOR_BASEBALL_NEW_220328',
        'DB2_MINOR_POSTSEASON', 'DB2_MINOR_SO_BASEBALL', 'DB2_MINOR_SO_BASEBALL_NEW',
        'BROADCAST_BASEBALL', 'DB2_OTHER_GAME', 'FALL_LEAGUE_BASEBALL'
    ]

    for db in main_dbs:
        try:
            cursor.execute(f"""
                SELECT t.name, SUM(p.rows), COUNT(c.column_id)
                FROM [{db}].sys.tables t
                LEFT JOIN [{db}].sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0,1)
                LEFT JOIN [{db}].sys.columns c ON t.object_id = c.object_id
                GROUP BY t.name
                ORDER BY t.name
            """)
            rows = cursor.fetchall()
            print(f"\n===== {db} ({len(rows)} tables) =====")
            for r in rows:
                print(f"  {r[0]:45s} | rows: {r[1]:>10,} | cols: {r[2]:>3}")
        except Exception as e:
            print(f"\n===== {db} -> ACCESS DENIED =====")
        time.sleep(0.1)

    conn.close()

if __name__ == '__main__':
    main()
