#!/usr/bin/env python3
"""40종 테이블 컬럼 메타데이터 + 샘플 추출"""
import pymssql
import json
import os
from pathlib import Path
from config import TABLE_DB_MAP, CODE_NAMES, BASE_DIR
from db_helper import get_connection


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

def main():
    result = {"tables": {}}
    conn = get_connection()
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

        pk_cols = [c['name'] for c in columns if c['is_pk']]

        result["tables"][table_name] = {
            "representative_db": db_name,
            "row_count": row_count,
            "pk_columns": pk_cols,
            "column_count": len(columns),
            "columns": columns
        }

        print(f"  Columns: {len(columns)}, Rows: {row_count:,}")
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
