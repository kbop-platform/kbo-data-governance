#!/usr/bin/env python3
"""Compile comprehensive table type summary across specified backup DBs."""
import json
import os

BASE = '/home/user/dev/data-dict/raw'

files = {
    'DB2_BASEBALL': 'DB2_BASEBALL_220328.json',
    'DB2_BASEBALL_NEW': 'DB2_BASEBALL_NEW_220328.json',
    'DB2_EXHIBITION': 'DB2_EXHIBITION.json',
    'FALL_LEAGUE': 'FALL_LEAGUE_BASEBALL.json',
    'BROADCAST': 'BROADCAST_BASEBALL.json'
}

all_tables = {}

for db_label, filename in files.items():
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tables = data.get('tables', {})
    for tbl_name, tbl_data in tables.items():
        tbl_name_clean = tbl_name.strip()
        if tbl_name_clean not in all_tables:
            all_tables[tbl_name_clean] = {'dbs': {}, 'columns_by_db': {}}

        cols = tbl_data.get('columns', [])
        row_count = tbl_data.get('row_count', 0)
        all_tables[tbl_name_clean]['dbs'][db_label] = {
            'col_count': len(cols), 'row_count': row_count
        }
        all_tables[tbl_name_clean]['columns_by_db'][db_label] = []

        for col in cols:
            col_info = {
                'name': col['name'],
                'data_type': col['data_type'],
                'max_length': col.get('max_length', ''),
                'precision': col.get('precision', 0),
                'scale': col.get('scale', 0),
                'is_nullable': col.get('is_nullable', True),
                'is_pk': col.get('is_pk', False),
                'default_value': col.get('default_value'),
            }
            all_tables[tbl_name_clean]['columns_by_db'][db_label].append(col_info)


def format_type(c):
    dt = c['data_type']
    if dt in ('char', 'varchar', 'nchar', 'nvarchar', 'binary', 'varbinary'):
        ml = c['max_length']
        if dt.startswith('n') and isinstance(ml, int) and ml > 0:
            ml = ml // 2
        return f"{dt}({ml})"
    elif dt in ('decimal', 'numeric') and c['precision']:
        return f"{dt}({c['precision']},{c['scale']})"
    elif dt == 'float':
        return 'float'
    else:
        return dt


for tbl_name in sorted(all_tables.keys(), key=str.lower):
    info = all_tables[tbl_name]
    db_list = list(info['dbs'].keys())

    db_details = []
    for db, meta in info['dbs'].items():
        db_details.append(f"{db} ({meta['col_count']} cols, {meta['row_count']:,} rows)")

    print("=" * 80)
    print(f"TABLE: {tbl_name}")
    print(f"  Present in: {', '.join(db_details)}")

    # Build unified column set - use DB with most columns as canonical
    max_db = max(info['dbs'], key=lambda d: info['dbs'][d]['col_count'])
    canonical_cols = info['columns_by_db'][max_db]

    printed_names = set()
    col_lines = []

    for c in canonical_cols:
        type_str = format_type(c)
        nullable = 'NULL' if c['is_nullable'] else 'NOT NULL'
        pk = ' [PK]' if c['is_pk'] else ''
        default = f" DEFAULT {c['default_value']}" if c['default_value'] else ''

        present_in = []
        for db, cols in info['columns_by_db'].items():
            if any(cc['name'] == c['name'] for cc in cols):
                present_in.append(db)

        extra = ''
        if len(present_in) < len(db_list):
            extra = f'  [only: {", ".join(present_in)}]'

        col_lines.append(
            f"    {c['name']:40s} {type_str:20s} {nullable:8s}{pk}{default}{extra}"
        )
        printed_names.add(c['name'])

    # Add columns that only exist in non-canonical DBs
    for db, cols in info['columns_by_db'].items():
        if db == max_db:
            continue
        for c in cols:
            if c['name'] not in printed_names:
                type_str = format_type(c)
                nullable = 'NULL' if c['is_nullable'] else 'NOT NULL'
                pk = ' [PK]' if c['is_pk'] else ''
                default = f" DEFAULT {c['default_value']}" if c['default_value'] else ''
                present_in = []
                for db2, cols2 in info['columns_by_db'].items():
                    if any(cc['name'] == c['name'] for cc in cols2):
                        present_in.append(db2)
                col_lines.append(
                    f"    {c['name']:40s} {type_str:20s} {nullable:8s}{pk}{default}  [only: {', '.join(present_in)}]"
                )
                printed_names.add(c['name'])

    print(f"  Total unique columns: {len(printed_names)}")
    print(f"  {'_'*76}")
    print(f"    {'COLUMN NAME':40s} {'DATA TYPE':20s} {'NULL':8s} FLAGS")
    print(f"    {'_'*40} {'_'*20} {'_'*8} {'_'*20}")
    for cl in col_lines:
        print(cl)
    print()


print()
print("=" * 80)
print("GRAND SUMMARY")
print("=" * 80)
print(f"Total unique table types across 5 DBs: {len(all_tables)}")
print()
print("DBs analyzed:")
for db_label in files:
    tbl_count = sum(1 for info in all_tables.values() if db_label in info['dbs'])
    print(f"  {db_label}: {tbl_count} tables")

print()
print("Table type inventory:")
for i, tbl_name in enumerate(sorted(all_tables.keys(), key=str.lower), 1):
    info = all_tables[tbl_name]
    dbs = list(info['dbs'].keys())
    max_cols = max(m['col_count'] for m in info['dbs'].values())
    total_rows = sum(m['row_count'] for m in info['dbs'].values())
    print(f"  {i:2d}. {tbl_name:45s} {max_cols:3d} cols  {total_rows:>10,} total rows  -> {', '.join(dbs)}")
