#!/usr/bin/env python3
# column-diff.py - Analyzes 75 tables with column count mismatches
# between backup DB and S2i, queries MSSQL for actual column names.

import json
import os
from collections import defaultdict, Counter
from pathlib import Path
import pymssql
from config import BASE_DIR
from db_helper import get_connection
INPUT_FILE = os.path.join(BASE_DIR, "raw", "excel-inventory.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "raw", "column-diff.json")


def load_mismatched_tables(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    sheets = data["comparison_table"]["sheets"]
    tables = []
    for sheet_name, rows in sheets.items():
        for row in rows:
            if (row.get("column_match") is False
                and row.get("backup_column_count")
                and row.get("s2i_column_count")):
                tables.append(row)
    return tables


def main():
    SEP = "=" * 80
    print(SEP)
    print("  Column Count Mismatch Analysis (column-diff)")
    print(SEP)
    print()

    tables = load_mismatched_tables(INPUT_FILE)
    print("Loaded %d mismatched tables from excel-inventory.json." % len(tables))
    print()
    print("Querying MSSQL for column lists...")
    print()

    conn_cache = {}
    results = []

    for i, t in enumerate(tables):
        db_name = t["backup_db_name"]
        table_name = t["backup_table_name"]
        s2i_table = t.get("s2i_table_name", "") or ""
        backup_col_count = t["backup_column_count"]
        s2i_col_count = t["s2i_column_count"]
        diff = s2i_col_count - backup_col_count

        if diff > 0:
            diff_direction = "s2i_more"
        elif diff < 0:
            diff_direction = "backup_more"
        else:
            diff_direction = "equal"

        if db_name not in conn_cache:
            try:
                conn = get_connection(database=db_name)
                conn_cache[db_name] = conn
                print("  [Connected] %s" % db_name)
            except Exception as e:
                print("  [Error] %s: %s" % (db_name, e))
                conn_cache[db_name] = None

        conn = conn_cache[db_name]
        backup_columns = []
        error_msg = None

        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS "
                    "WHERE TABLE_NAME = %s ORDER BY ORDINAL_POSITION",
                    (table_name,))
                backup_columns = [row[0] for row in cur.fetchall()]
            except Exception as e:
                error_msg = str(e)
        else:
            error_msg = "DB connection failed"

        actual_count = len(backup_columns)
        count_note = ""
        if backup_columns and actual_count != backup_col_count:
            count_note = "Excel(%d) vs actual DB(%d) mismatch" % (backup_col_count, actual_count)

        result = {
            "backup_db": db_name,
            "backup_table": table_name,
            "s2i_table": s2i_table,
            "backup_col_count": backup_col_count,
            "s2i_col_count": s2i_col_count,
            "actual_backup_col_count": actual_count,
            "diff": diff,
            "diff_direction": diff_direction,
            "backup_columns": sorted(backup_columns),
            "note": t.get("note") or "",
            "reason": t.get("reason") or "",
        }
        if count_note:
            result["count_discrepancy"] = count_note
        if error_msg:
            result["error"] = error_msg
        results.append(result)

        if (i + 1) % 10 == 0 or (i + 1) == len(tables):
            print("  Progress: %d/%d" % (i + 1, len(tables)))

    for conn in conn_cache.values():
        if conn:
            try:
                conn.close()
            except:
                pass

    print()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Results saved to %s" % OUTPUT_FILE)
    print()

    print_summary(results, SEP)


def print_summary(results, SEP):
    groups = defaultdict(list)
    for r in results:
        groups[r["diff"]].append(r)

    print(SEP)
    print("  Analysis Summary")
    print(SEP)
    print()

    print("## Column Count Diff Distribution (s2i - backup)")
    print("-" * 50)
    for diff_val in sorted(groups.keys()):
        grp_items = groups[diff_val]
        direction = "S2i has more" if diff_val > 0 else "Backup has more"
        print("  %+d (%s): %d tables" % (diff_val, direction, len(grp_items)))
    print()

    plus1 = groups.get(1, [])
    if plus1:
        _analyze_plus1(plus1, SEP)

    minus1 = groups.get(-1, [])
    if minus1:
        _print_pattern_group(minus1, -1, SEP)

    for diff_val in sorted(groups.keys()):
        if diff_val <= 1:
            continue
        _print_pattern_group(groups[diff_val], diff_val, SEP)

    for diff_val in sorted(groups.keys()):
        if diff_val >= -1:
            continue
        _print_pattern_group(groups[diff_val], diff_val, SEP)

    discrepancies = [r for r in results if r.get("count_discrepancy")]
    if discrepancies:
        print(SEP)
        print("  Excel vs Actual DB Column Count Discrepancies (%d)" % len(discrepancies))
        print(SEP)
        print()
        for r in discrepancies:
            print("  %s.%s: %s" % (r["backup_db"], r["backup_table"], r["count_discrepancy"]))
        print()

    error_items = [r for r in results if r.get("error")]
    if error_items:
        print(SEP)
        print("  Errors (%d tables)" % len(error_items))
        print(SEP)
        print()
        for r in error_items:
            print("  %s.%s: %s" % (r["backup_db"], r["backup_table"], r["error"]))
        print()

    print(SEP)
    print("  Final Statistics")
    print(SEP)
    total = len(results)
    success = len([r for r in results if r["backup_columns"] and not r.get("error")])
    print("  Total tables: %d" % total)
    print("  Column query success: %d" % success)
    print("  Query failures/errors: %d" % (total - success))
    print("  Output file: %s" % OUTPUT_FILE)
    print()


def _print_pattern_group(items, diff_val, SEP):
    if diff_val > 0:
        label = "+%d Pattern (%d tables) -- S2i has %d more columns" % (diff_val, len(items), diff_val)
    elif diff_val == -1:
        label = "-1 Pattern (%d tables) -- Backup has 1 more column" % len(items)
    else:
        label = "%d Pattern (%d tables) -- Backup has %d more columns" % (diff_val, len(items), abs(diff_val))
    print(SEP)
    print("  " + label)
    print(SEP)
    print()
    for r in sorted(items, key=lambda x: (x["backup_db"], x["backup_table"])):
        cols = ", ".join(sorted(r["backup_columns"]))
        print("  %s.%s -> S2i: %s" % (r["backup_db"], r["backup_table"], r["s2i_table"]))
        print("    Backup columns(%d): %s" % (r["actual_backup_col_count"], cols))
        if r.get("reason"):
            print("    Reason: %s" % r["reason"])
        print()


def _analyze_plus1(plus1, SEP):
    print(SEP)
    print("  +1 Pattern Analysis (%d tables)" % len(plus1))
    print("  Tables where S2i has exactly 1 extra column")
    print(SEP)
    print()

    col_sets = {}
    for r in plus1:
        key = "%s.%s" % (r["backup_db"], r["backup_table"])
        col_sets[key] = set(r["backup_columns"])

    print("  %-35s %-30s %-6s %-6s" % ("Backup DB", "Table", "Bkup", "S2i"))
    print("  " + "-" * 80)
    for r in sorted(plus1, key=lambda x: (x["backup_db"], x["backup_table"])):
        print("  %-35s %-30s %-6d %-6d" % (
            r["backup_db"], r["backup_table"],
            r["actual_backup_col_count"], r["s2i_col_count"]))
    print()

    by_db = defaultdict(list)
    for r in plus1:
        by_db[r["backup_db"]].append(r)

    print("  ## +1 Tables by DB:")
    print("  " + "-" * 50)
    for db in sorted(by_db.keys()):
        db_items = by_db[db]
        print("    %s: %d tables" % (db, len(db_items)))
        for r in db_items:
            print("      - %s (%d -> %d)" % (
                r["backup_table"], r["actual_backup_col_count"], r["s2i_col_count"]))
    print()

    print("  ## Column Frequency in +1 Tables (top 30):")
    print("  " + "-" * 60)
    col_freq = Counter()
    for r in plus1:
        for c in r["backup_columns"]:
            col_freq[c] += 1

    for col, cnt in col_freq.most_common(30):
        pct = cnt * 100.0 / len(plus1)
        bar = "#" * int(pct / 2)
        print("    %-25s %3d/%d (%5.1f%%) %s" % (col, cnt, len(plus1), pct, bar))
    print()

    if col_sets:
        all_cols = list(col_sets.values())
        common_all = all_cols[0].copy()
        for s in all_cols[1:]:
            common_all = common_all & s
        print("  ## Columns common to ALL +1 tables: %d" % len(common_all))
        if common_all:
            for c in sorted(common_all):
                print("    - %s" % c)
        else:
            print("    (none)")
        print()

    by_table = defaultdict(list)
    for r in plus1:
        by_table[r["backup_table"]].append(r)

    multi_db_tables = {k: v for k, v in by_table.items() if len(v) > 1}
    if multi_db_tables:
        print("  ## Same table name across multiple DBs (%d tables):" % len(multi_db_tables))
        print("  " + "-" * 60)
        for tname in sorted(multi_db_tables.keys()):
            t_items = multi_db_tables[tname]
            print("    Table: %s" % tname)
            col_lists = []
            for r in t_items:
                cols_str = ", ".join(sorted(r["backup_columns"]))
                print("      DB: %s" % r["backup_db"])
                print("        Columns(%d): %s" % (r["actual_backup_col_count"], cols_str))
                col_lists.append(set(r["backup_columns"]))
            if len(col_lists) >= 2:
                common = col_lists[0].copy()
                for s in col_lists[1:]:
                    common = common & s
                all_union = col_lists[0].copy()
                for s in col_lists[1:]:
                    all_union = all_union | s
                diff_cols = all_union - common
                if diff_cols:
                    print("      >> Diff columns: %s" % ", ".join(sorted(diff_cols)))
                else:
                    print("      >> Identical column structure across all DBs")
            print()
    print()

    print("  ## Inferring the column S2i added:")
    print("  " + "-" * 60)
    print()

    print("    [Method 1] Compare tables within same DB with similar structure")
    print()

    for db in sorted(by_db.keys()):
        db_items = by_db[db]
        if len(db_items) < 2:
            continue
        printed_header = False
        for j in range(len(db_items)):
            for k in range(j + 1, len(db_items)):
                r1, r2 = db_items[j], db_items[k]
                s1 = set(r1["backup_columns"])
                s2 = set(r2["backup_columns"])
                common = s1 & s2
                only1 = s1 - s2
                only2 = s2 - s1
                denom = max(len(s1 | s2), 1)
                overlap_pct = len(common) * 100.0 / denom
                if overlap_pct >= 50:
                    if not printed_header:
                        print("    DB: %s" % db)
                        printed_header = True
                    print("      %s vs %s (overlap: %.0f%%)" % (
                        r1["backup_table"], r2["backup_table"], overlap_pct))
                    if only1:
                        print("        Only in %s: %s" % (
                            r1["backup_table"], ", ".join(sorted(only1))))
                    if only2:
                        print("        Only in %s: %s" % (
                            r2["backup_table"], ", ".join(sorted(only2))))
        if printed_header:
            print()

    print("    [Method 2] Compare tables with same backup column count")
    print()
    by_colcount = defaultdict(list)
    for r in plus1:
        by_colcount[r["actual_backup_col_count"]].append(r)

    for cnt in sorted(by_colcount.keys()):
        cnt_items = by_colcount[cnt]
        if len(cnt_items) < 2:
            continue
        print("      Backup column count = %d (%d tables):" % (cnt, len(cnt_items)))
        col_lists = [set(r["backup_columns"]) for r in cnt_items]
        common = col_lists[0].copy()
        for s in col_lists[1:]:
            common = common & s
        union_set = col_lists[0].copy()
        for s in col_lists[1:]:
            union_set = union_set | s
        unique_cols = union_set - common
        print("        Common columns: %d" % len(common))
        if unique_cols:
            print("        Diff columns: %s" % ", ".join(sorted(unique_cols)))
        else:
            table_names = [r["backup_table"] for r in cnt_items]
            print("        Identical structure: %s" % ", ".join(table_names))

        for r in cnt_items:
            cols = ", ".join(sorted(r["backup_columns"]))
            print("        %s.%s: %s" % (r["backup_db"], r["backup_table"], cols))
        print()


if __name__ == "__main__":
    main()
