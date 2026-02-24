#!/usr/bin/env python3
"""
MSSQL 백업DB + Excel 비교표 — 처음부터 새로 분석
OPS PDF 제외, 두 소스만으로 분석
"""
import json

MSSQL_PATH = '/home/user/dev/data-dict/raw/mssql-inventory.json'
EXCEL_PATH = '/home/user/dev/data-dict/raw/excel-inventory.json'

# MSSQL 시스템 테이블 제외 패턴
SYSTEM_PREFIXES = ('MSpeer_', 'MSpub_', 'sysarticle', 'syspub', 'sysrepl',
                   'sysschema', 'syssub', 'systran', 'sysdiag', 'sysexten',
                   'sysmergearticles', 'sysmerge', 'MSdynamic', 'MSmerge',
                   'MSrepl', 'MSsub', 'MSsnap')

def is_system_table(name):
    return any(name.startswith(p) or name.lower().startswith(p.lower()) for p in SYSTEM_PREFIXES)

with open(MSSQL_PATH, 'r', encoding='utf-8') as f:
    mssql = json.load(f)
with open(EXCEL_PATH, 'r', encoding='utf-8') as f:
    excel = json.load(f)

# ============================================================
# 1. MSSQL 백업DB 테이블 목록 (시스템 테이블 제외)
# ============================================================
print("=" * 80)
print("1. MSSQL 백업DB 테이블 인벤토리")
print("=" * 80)

mssql_all = {}  # db_name -> [tables]
mssql_unique = {}  # table_name -> [db_names]
total_rows_all = 0

for db in mssql['databases']:
    db_name = db['db_name']
    user_tables = [t for t in db['tables'] if not is_system_table(t['table_name'])]
    mssql_all[db_name] = user_tables
    for t in user_tables:
        total_rows_all += t['row_count']
        if t['table_name'] not in mssql_unique:
            mssql_unique[t['table_name']] = []
        mssql_unique[t['table_name']].append(db_name)

# DB1 vs DB2 분리
db1_dbs = {k: v for k, v in mssql_all.items() if k.startswith('DB1_')}
db2_dbs = {k: v for k, v in mssql_all.items() if k.startswith('DB2_')}

print(f"\n총 DB 수: {len(mssql_all)}개 (DB1: {len(db1_dbs)}, DB2: {len(db2_dbs)})")
total_user_tables = sum(len(v) for v in mssql_all.values())
print(f"총 테이블 인스턴스: {total_user_tables}개 (시스템 테이블 제외)")
print(f"고유 테이블명: {len(mssql_unique)}종")
print(f"총 행 수: {total_rows_all:,}")

print(f"\n### DB1 (영구/누적) - {len(db1_dbs)}개 DB")
for db_name in sorted(db1_dbs.keys()):
    tables = db1_dbs[db_name]
    rows = sum(t['row_count'] for t in tables)
    print(f"  {db_name}: {len(tables)}개 테이블, {rows:,} rows")
    for t in sorted(tables, key=lambda x: x['table_name']):
        print(f"    - {t['table_name']} ({t['column_count']}col, {t['row_count']:,}rows)")

print(f"\n### DB2 (시즌/진행) - {len(db2_dbs)}개 DB")
for db_name in sorted(db2_dbs.keys()):
    tables = db2_dbs[db_name]
    rows = sum(t['row_count'] for t in tables)
    print(f"  {db_name}: {len(tables)}개 테이블, {rows:,} rows")
    for t in sorted(tables, key=lambda x: x['table_name']):
        print(f"    - {t['table_name']} ({t['column_count']}col, {t['row_count']:,}rows)")

# ============================================================
# 2. Excel 비교표 테이블 목록
# ============================================================
print("\n" + "=" * 80)
print("2. Excel 비교표 테이블 목록")
print("=" * 80)

excel_rows = []
for sheet_name, rows in excel['comparison_table']['sheets'].items():
    for r in rows:
        r['_sheet'] = sheet_name
        excel_rows.append(r)

print(f"\n총 행 수: {len(excel_rows)}개")
for sheet_name, rows in excel['comparison_table']['sheets'].items():
    print(f"  {sheet_name}: {len(rows)}개")

# Excel에서 백업DB별 테이블 목록
excel_by_db = {}
for r in excel_rows:
    db = r['backup_db_name']
    if db not in excel_by_db:
        excel_by_db[db] = []
    excel_by_db[db].append(r)

print(f"\nExcel 백업DB 목록 ({len(excel_by_db)}개):")
for db_name in sorted(excel_by_db.keys()):
    rows = excel_by_db[db_name]
    has_s2i = sum(1 for r in rows if r['s2i_table_name'])
    no_s2i = sum(1 for r in rows if not r['s2i_table_name'])
    print(f"  {db_name}: {len(rows)}개 (S2i 매핑 {has_s2i}, 없음 {no_s2i})")

# Excel 고유 테이블명
excel_backup_tables = set()
excel_s2i_tables = set()
for r in excel_rows:
    if r['backup_table_name']:
        excel_backup_tables.add(r['backup_table_name'])
    if r['s2i_table_name']:
        excel_s2i_tables.add(r['s2i_table_name'])

print(f"\nExcel 백업측 고유 테이블명: {len(excel_backup_tables)}종")
print(f"Excel S2i측 고유 테이블명: {len(excel_s2i_tables)}종")

# ============================================================
# 3. MSSQL ↔ Excel 비교
# ============================================================
print("\n" + "=" * 80)
print("3. MSSQL 백업DB ↔ Excel 비교")
print("=" * 80)

# DB별 비교
print("\n### DB별 테이블 수 비교")
all_db_names = sorted(set(list(mssql_all.keys()) + list(excel_by_db.keys())))
for db_name in all_db_names:
    m_count = len(mssql_all.get(db_name, []))
    e_count = len(excel_by_db.get(db_name, []))
    diff = m_count - e_count
    marker = "" if diff == 0 else f" (차이: {diff:+d})"
    in_m = "O" if db_name in mssql_all else "X"
    in_e = "O" if db_name in excel_by_db else "X"
    print(f"  {db_name:40s} | MSSQL:{m_count:3d} | Excel:{e_count:3d}{marker}  [{in_m}/{in_e}]")

# MSSQL에만 있는 DB
mssql_only_dbs = set(mssql_all.keys()) - set(excel_by_db.keys())
excel_only_dbs = set(excel_by_db.keys()) - set(mssql_all.keys())
print(f"\nMSSQL에만 있는 DB: {sorted(mssql_only_dbs)}")
print(f"Excel에만 있는 DB: {sorted(excel_only_dbs)}")

# 테이블 단위 상세 비교
print("\n### 테이블 단위 비교 (DB별)")
total_match = 0
total_mssql_only = 0
total_excel_only = 0

for db_name in sorted(set(mssql_all.keys()) & set(excel_by_db.keys())):
    m_tables = {t['table_name'] for t in mssql_all[db_name]}
    e_tables = {r['backup_table_name'] for r in excel_by_db[db_name]}

    both = m_tables & e_tables
    m_only = m_tables - e_tables
    e_only = e_tables - m_tables

    total_match += len(both)
    total_mssql_only += len(m_only)
    total_excel_only += len(e_only)

    if m_only or e_only:
        print(f"\n  {db_name}:")
        if m_only:
            print(f"    MSSQL에만: {sorted(m_only)}")
        if e_only:
            print(f"    Excel에만: {sorted(e_only)}")

print(f"\n### 테이블 비교 요약 (공통 DB 기준)")
print(f"  양쪽 모두: {total_match}개")
print(f"  MSSQL에만: {total_mssql_only}개")
print(f"  Excel에만: {total_excel_only}개")

# ============================================================
# 4. S2i 비교 현황 (Excel 기준)
# ============================================================
print("\n" + "=" * 80)
print("4. S2i 비교 현황 (Excel 기준)")
print("=" * 80)

has_s2i = [r for r in excel_rows if r['s2i_table_name']]
no_s2i = [r for r in excel_rows if not r['s2i_table_name']]

print(f"\nS2i 매핑 있음: {len(has_s2i)}개")
print(f"S2i 매핑 없음 (백업에만): {len(no_s2i)}개")

# 컬럼/행 일치 통계
col_true = sum(1 for r in has_s2i if r['column_match'] == True)
col_false = sum(1 for r in has_s2i if r['column_match'] == False)
row_true = sum(1 for r in has_s2i if r['row_match'] == True)
row_false = sum(1 for r in has_s2i if r['row_match'] == False)

print(f"\nS2i 매핑 {len(has_s2i)}개 중:")
print(f"  컬럼 일치: {col_true}, 불일치: {col_false}")
print(f"  행 일치:   {row_true}, 불일치: {row_false}")

# 테이블명 차이
name_diff = [(r['backup_table_name'], r['s2i_table_name'], r['backup_db_name'])
             for r in has_s2i if r['backup_table_name'] != r['s2i_table_name']]
print(f"\n테이블명 차이: {len(name_diff)}개")
for bt, st, db in sorted(name_diff):
    print(f"  {db}: {bt} → {st}")

# S2i 없는 테이블
print(f"\nS2i 매핑 없는 테이블 ({len(no_s2i)}개):")
for r in sorted(no_s2i, key=lambda x: (x['backup_db_name'], x['backup_table_name'])):
    note = r.get('note', '') or ''
    print(f"  {r['backup_db_name']}: {r['backup_table_name']} ({r['backup_column_count']}col, {r['backup_row_count']:,}rows) [{note}]")

# ============================================================
# 5. 고유 테이블명 전체 목록
# ============================================================
print("\n" + "=" * 80)
print("5. MSSQL 고유 테이블명 전체 목록 ({0}종)".format(len(mssql_unique)))
print("=" * 80)

for tname in sorted(mssql_unique.keys()):
    dbs = mssql_unique[tname]
    db1_count = sum(1 for d in dbs if d.startswith('DB1_'))
    db2_count = sum(1 for d in dbs if d.startswith('DB2_'))
    print(f"  {tname:45s} | DB1:{db1_count} DB2:{db2_count} | 총 {len(dbs)}개 DB")

# ============================================================
# 6. 국제대회 정보
# ============================================================
print("\n" + "=" * 80)
print("6. 국제대회 ({0}개)".format(len(excel['international']['tournaments'])))
print("=" * 80)
for t in excel['international']['tournaments']:
    print(f"  {t.get('year', '?')}: {t.get('tournament', t.get('name', '?'))}")

print("\n\nDONE.")
