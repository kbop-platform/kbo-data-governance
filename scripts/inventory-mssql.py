#!/usr/bin/env python3
"""
MSSQL Database Inventory Script
"""
import json, sys, os
from datetime import datetime
from pathlib import Path
import pymssql
from config import load_env, BASE_DIR
from db_helper import get_connection

load_env()
SERVER = os.environ.get("MSSQL_SERVER", "")
PORT = int(os.environ.get("MSSQL_PORT", "1433"))
USER = os.environ.get("MSSQL_USER", "")
OUTPUT_DIR = os.path.join(BASE_DIR, "raw")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mssql-inventory.json")

def connect(database="master"):
    return get_connection(database=database)

def find_working_password():
    try:
        conn = connect()
        conn.close()
        pwd = os.environ.get("MSSQL_PASSWORD", "")
        print("[OK] Connected: " + pwd[:4] + "***")
        return True
    except pymssql.OperationalError as e:
        print("[FAIL] Connection: " + str(e))
        print("[ERROR] No valid password.")
        sys.exit(1)

def get_all_databases(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sys.databases ORDER BY name")
    return [r[0] for r in cur.fetchall()]

def get_tables_with_columns(conn, db):
    cur = conn.cursor()
    q = ("USE [" + db + "]; "
         "SELECT t.TABLE_NAME, COUNT(c.COLUMN_NAME) "
         "FROM INFORMATION_SCHEMA.TABLES t "
         "LEFT JOIN INFORMATION_SCHEMA.COLUMNS c "
         "ON t.TABLE_SCHEMA=c.TABLE_SCHEMA AND t.TABLE_NAME=c.TABLE_NAME "
         "WHERE t.TABLE_TYPE=%s GROUP BY t.TABLE_NAME ORDER BY t.TABLE_NAME")
    cur.execute(q, ("BASE TABLE",))
    return cur.fetchall()

def get_row_counts(conn, db):
    cur = conn.cursor()
    q = ("USE [" + db + "]; "
         "SELECT o.name, SUM(p.row_count) "
         "FROM sys.dm_db_partition_stats p "
         "INNER JOIN sys.objects o ON p.object_id=o.object_id "
         "WHERE o.type=%s AND p.index_id IN (0,1) "
         "GROUP BY o.name ORDER BY o.name")
    cur.execute(q, ("U",))
    return dict((r[0], r[1]) for r in cur.fetchall())

def inventory_database(db):
    try:
        conn = connect(database=db)
    except Exception as e:
        print("  [WARN] " + db + ": " + str(e))
        return None
    try:
        tc = get_tables_with_columns(conn, db)
        rc = get_row_counts(conn, db)
        tables = []
        for tn, cc in tc:
            tables.append({"table_name": tn, "column_count": cc, "row_count": rc.get(tn, 0)})
        return tables
    except Exception as e:
        print("  [ERROR] " + db + ": " + str(e))
        return None
    finally:
        conn.close()

def main():
    sep = "=" * 70
    print(sep)
    print("MSSQL Database Inventory")
    print("Server: " + SERVER + ":" + str(PORT))
    print("User: " + USER)
    print("Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(sep)
    print()

    print("[1] Testing connection...")
    find_working_password()
    print()

    print("[2] Listing all databases...")
    conn = connect()
    all_dbs = get_all_databases(conn)
    conn.close()
    print("    Found " + str(len(all_dbs)) + " databases:")
    for d in all_dbs:
        pfx = "  >> " if d.startswith(("DB1_", "DB2_")) else "     "
        print("    " + pfx + d)
    print()

    targets = [d for d in all_dbs if d.startswith(("DB1_", "DB2_"))]
    print("[3] Target databases: " + str(len(targets)))
    print()

    print("[4] Inventorying tables...")
    results = []
    unique_tables = set()
    for i, db in enumerate(targets, 1):
        dt = "DB1" if db.startswith("DB1_") else "DB2"
        print("    [" + str(i) + "/" + str(len(targets)) + "] " + db + " (" + dt + ")")
        tables = inventory_database(db)
        if tables is not None:
            for t in tables:
                unique_tables.add(t["table_name"])
            tr = sum(t["row_count"] for t in tables)
            print("           -> " + str(len(tables)) + " tables, " + "{:,}".format(tr) + " rows")
            results.append({"db_name": db, "db_type": dt, "tables": tables})
        else:
            results.append({"db_name": db, "db_type": dt, "tables": [], "error": "Could not query"})
    print()

    db1 = [r for r in results if r["db_type"] == "DB1"]
    db2 = [r for r in results if r["db_type"] == "DB2"]
    tt = sum(len(r["tables"]) for r in results)
    summary = {
        "total_dbs": len(results), "db1_count": len(db1), "db2_count": len(db2),
        "total_tables": tt, "total_unique_tables": len(unique_tables),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "server": SERVER + ":" + str(PORT), "user": USER,
        "all_databases_on_server": all_dbs
    }
    output = {"databases": results, "summary": summary}

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print("[5] Output: " + OUTPUT_FILE)
    print()

    print(sep)
    print("SUMMARY")
    print(sep)
    fmt = "  {:<45} {:>7} {:>12}"
    print("  Total databases:    " + str(summary["total_dbs"]))
    print("    - DB1_*:          " + str(summary["db1_count"]))
    print("    - DB2_*:          " + str(summary["db2_count"]))
    print("  Total tables:       " + str(summary["total_tables"]))
    print("  Unique tables:      " + str(summary["total_unique_tables"]))
    print()
    print("  Per-database breakdown:")
    print(fmt.format("Database", "Tables", "Total Rows"))
    print("  " + "-"*45 + " " + "-"*7 + " " + "-"*12)
    for r in results:
        tc2 = len(r["tables"])
        tr2 = sum(t["row_count"] for t in r["tables"])
        print(fmt.format(r["db_name"], tc2, "{:,}".format(tr2)))
    print()

    flat = []
    for r in results:
        for t in r["tables"]:
            flat.append({"db": r["db_name"], "table": t["table_name"],
                         "rows": t["row_count"], "cols": t["column_count"]})
    if flat:
        flat.sort(key=lambda x: x["rows"], reverse=True)
        fmt2 = "  {:<35} {:<30} {:>12} {:>6}"
        print("  Top 20 tables by row count:")
        print(fmt2.format("Database", "Table", "Rows", "Cols"))
        print("  " + "-"*35 + " " + "-"*30 + " " + "-"*12 + " " + "-"*6)
        for t in flat[:20]:
            ds = t["db"][:33] + ".." if len(t["db"]) > 35 else t["db"]
            print(fmt2.format(ds, t["table"], "{:,}".format(t["rows"]), t["cols"]))
    print()
    print(sep)
    print("Done.")

if __name__ == "__main__":
    main()
