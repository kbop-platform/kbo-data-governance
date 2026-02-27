#!/usr/bin/env python3
"""scripts/audit-data.py - DB 실데이터 수집 (파이프라인 보조)

39개 테이블의 코드성 컬럼 실데이터를 DB에서 직접 조회하여
raw/data-audit.json에 저장한다.
dictionary 컬럼 설명 보강의 근거 자료로 사용.

사용법:
    python3 scripts/audit-data.py
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from config import TABLE_DB_MAP, CODE_NAMES, BASE_DIR
from db_helper import get_connection


def is_code_column(col_name, data_type, max_length):
    """코드성 컬럼 판별 (extract-columns.py 로직과 동일)"""
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


def audit_table(cursor, table_name, db_name):
    """단일 테이블 감사 수행"""
    cursor.execute(f"USE [{db_name}]")

    # 1) 행 수
    cursor.execute(f"""
        SELECT SUM(p.rows) FROM sys.partitions p
        JOIN sys.tables t ON p.object_id = t.object_id
        WHERE t.name = '{table_name}' AND p.index_id IN (0,1)
    """)
    row_count = cursor.fetchone()[0] or 0

    # 2) 컬럼 메타
    cursor.execute(f"""
        SELECT c.name, t.name AS data_type, c.max_length
        FROM sys.columns c
        JOIN sys.types t ON c.user_type_id = t.user_type_id
        WHERE c.object_id = OBJECT_ID('{table_name}')
        ORDER BY c.column_id
    """)
    cols_raw = cursor.fetchall()

    if not cols_raw:
        return None

    columns = {}
    for col_name, dtype, max_len in cols_raw:
        # nvarchar max_length → 문자 수
        display_len = max_len
        if dtype in ('nvarchar', 'nchar') and max_len > 0:
            display_len = max_len // 2

        is_code = is_code_column(col_name, dtype, display_len)

        col_result = {
            "is_code": is_code,
        }

        # 3) NULL 비율
        try:
            cursor.execute(f"""
                SELECT COUNT(*) AS total,
                       COUNT(*) - COUNT([{col_name}]) AS null_cnt
                FROM [{table_name}]
            """)
            total, null_cnt = cursor.fetchone()
            col_result["null_count"] = null_cnt
            col_result["null_pct"] = round(null_cnt / total * 100, 1) if total > 0 else 0.0
        except Exception as e:
            col_result["null_count"] = -1
            col_result["null_pct"] = -1
            col_result["error_null"] = str(e)

        if is_code:
            # 4) 코드성 컬럼: GROUP BY TOP 30
            try:
                cursor.execute(f"""
                    SELECT TOP 30 [{col_name}], COUNT(*) AS cnt
                    FROM [{table_name}]
                    WHERE [{col_name}] IS NOT NULL
                    GROUP BY [{col_name}]
                    ORDER BY cnt DESC
                """)
                distincts = []
                for row in cursor.fetchall():
                    val = str(row[0]).strip() if row[0] is not None else ""
                    distincts.append({"value": val, "count": row[1]})
                col_result["distinct_values"] = distincts
            except Exception as e:
                col_result["distinct_values"] = []
                col_result["error_group"] = str(e)

            # 샘플도 추가
            try:
                cursor.execute(f"""
                    SELECT DISTINCT TOP 10 [{col_name}]
                    FROM [{table_name}]
                    WHERE [{col_name}] IS NOT NULL
                """)
                col_result["samples"] = [str(r[0]).strip() for r in cursor.fetchall()]
            except Exception:
                col_result["samples"] = []
        else:
            # 5) 비코드 컬럼: 다양한 샘플 TOP 10
            try:
                cursor.execute(f"""
                    SELECT DISTINCT TOP 10 [{col_name}]
                    FROM [{table_name}]
                    WHERE [{col_name}] IS NOT NULL
                """)
                col_result["samples"] = [str(r[0]).strip() for r in cursor.fetchall()]
            except Exception as e:
                col_result["samples"] = []
                col_result["error_sample"] = str(e)

        columns[col_name] = col_result

    return {
        "row_count": row_count,
        "columns": columns,
    }


def main():
    conn = get_connection(timeout=120, login_timeout=30)
    cursor = conn.cursor()

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "tables": {},
    }

    tables = sorted(TABLE_DB_MAP.items())
    total = len(tables)

    for idx, (table_name, db_name) in enumerate(tables, 1):
        print(f"[{idx:2d}/{total}] {table_name} @ {db_name} ... ", end="", flush=True)

        try:
            table_data = audit_table(cursor, table_name, db_name)
            if table_data is None:
                print("SKIP (no columns)")
                continue

            result["tables"][table_name] = table_data
            code_cols = sum(1 for c in table_data["columns"].values() if c["is_code"])
            print(f"OK  rows={table_data['row_count']:,}  cols={len(table_data['columns'])}  code={code_cols}")
        except Exception as e:
            print(f"ERROR: {e}")
            result["tables"][table_name] = {"error": str(e)}

    conn.close()

    out_path = Path(BASE_DIR) / "raw" / "data-audit.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)

    print(f"\n완료: {len(result['tables'])}개 테이블 → {out_path}")


if __name__ == "__main__":
    main()
