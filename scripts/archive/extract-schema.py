#!/usr/bin/env python3
"""
MSSQL 전체 DB 스키마 추출 스크립트
- 모든 주요 DB의 테이블/컬럼 상세 정보를 추출
- raw/ 디렉토리에 DB별 JSON + 통합 마크다운 저장
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

# 시스템/복제 테이블 제외 패턴
EXCLUDE_PREFIXES = ('MSpeer_', 'MSpub_', 'sysarticle', 'sysarticleupdates',
                    'syspublications', 'sysreplservers', 'sysschemaarticles',
                    'syssubscriptions', 'systranschemas', 'sysdiagrams', 'dtproperties')

MAIN_DBS = [
    'DB1_BASEBALL_220328', 'DB1_BASEBALL_2_220328',
    'DB2_BASEBALL_220328', 'DB2_BASEBALL_2_220328', 'DB2_BASEBALL_NEW_220328',
    'DB2_POSTSEASON', 'DB2_ALLSTAR', 'DB2_EXHIBITION', 'DB2_INTERNATIONAL',
    'DB1_MINOR_BASEBALL_220328', 'DB1_MINOR_SO_BASEBALL',
    'DB2_MINOR_BASEBALL_220328', 'DB2_MINOR_BASEBALL_NEW_220328',
    'DB2_MINOR_POSTSEASON', 'DB2_MINOR_SO_BASEBALL', 'DB2_MINOR_SO_BASEBALL_NEW',
    'BROADCAST_BASEBALL', 'DB2_OTHER_GAME', 'FALL_LEAGUE_BASEBALL'
]

COLUMN_QUERY = """
SELECT
    t.name AS table_name,
    c.column_id,
    c.name AS column_name,
    tp.name AS data_type,
    c.max_length,
    c.precision,
    c.scale,
    c.is_nullable,
    c.is_identity,
    ISNULL(dc.definition, '') AS default_value,
    ISNULL(ep.value, '') AS description,
    CASE WHEN pk.column_id IS NOT NULL THEN 1 ELSE 0 END AS is_pk,
    CASE WHEN fk.parent_column_id IS NOT NULL THEN 1 ELSE 0 END AS is_fk,
    ISNULL(ref_t.name, '') AS fk_ref_table,
    ISNULL(ref_c.name, '') AS fk_ref_column
FROM [{db}].sys.tables t
JOIN [{db}].sys.columns c ON t.object_id = c.object_id
JOIN [{db}].sys.types tp ON c.user_type_id = tp.user_type_id
LEFT JOIN [{db}].sys.default_constraints dc ON c.default_object_id = dc.object_id
LEFT JOIN [{db}].sys.extended_properties ep
    ON ep.major_id = t.object_id AND ep.minor_id = c.column_id AND ep.name = 'MS_Description'
LEFT JOIN (
    SELECT ic.object_id, ic.column_id
    FROM [{db}].sys.index_columns ic
    JOIN [{db}].sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
    WHERE i.is_primary_key = 1
) pk ON c.object_id = pk.object_id AND c.column_id = pk.column_id
LEFT JOIN [{db}].sys.foreign_key_columns fk
    ON fk.parent_object_id = c.object_id AND fk.parent_column_id = c.column_id
LEFT JOIN [{db}].sys.tables ref_t ON fk.referenced_object_id = ref_t.object_id
LEFT JOIN [{db}].sys.columns ref_c ON fk.referenced_object_id = ref_c.object_id AND fk.referenced_column_id = ref_c.column_id
ORDER BY t.name, c.column_id
"""

INDEX_QUERY = """
SELECT
    t.name AS table_name,
    i.name AS index_name,
    i.type_desc AS index_type,
    i.is_unique,
    i.is_primary_key,
    STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS columns
FROM [{db}].sys.indexes i
JOIN [{db}].sys.tables t ON i.object_id = t.object_id
JOIN [{db}].sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
JOIN [{db}].sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE i.name IS NOT NULL
GROUP BY t.name, i.name, i.type_desc, i.is_unique, i.is_primary_key
ORDER BY t.name, i.name
"""

ROW_COUNT_QUERY = """
SELECT t.name, SUM(p.rows)
FROM [{db}].sys.tables t
JOIN [{db}].sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0,1)
GROUP BY t.name
"""


def is_system_table(name):
    return name.startswith(EXCLUDE_PREFIXES) or name == 'oauth2_registered_client'


def extract_db_schema(cursor, db_name):
    """단일 DB의 스키마 정보 추출"""
    schema = {'db_name': db_name, 'tables': {}}

    # 1) 컬럼 정보
    try:
        cursor.execute(COLUMN_QUERY.format(db=db_name))
        for row in cursor.fetchall():
            tname = row[0]
            if is_system_table(tname):
                continue
            if tname not in schema['tables']:
                schema['tables'][tname] = {'columns': [], 'indexes': [], 'row_count': 0}

            col = {
                'column_id': row[1],
                'name': row[2],
                'data_type': row[3],
                'max_length': row[4],
                'precision': row[5],
                'scale': row[6],
                'is_nullable': bool(row[7]),
                'is_identity': bool(row[8]),
                'default_value': row[9] if row[9] else None,
                'description': str(row[10]) if row[10] else None,
                'is_pk': bool(row[11]),
                'is_fk': bool(row[12]),
                'fk_ref_table': row[13] if row[13] else None,
                'fk_ref_column': row[14] if row[14] else None,
            }
            schema['tables'][tname]['columns'].append(col)
    except Exception as e:
        print(f"  [WARN] 컬럼 조회 실패: {e}")
        return None

    # 2) 인덱스 정보
    try:
        cursor.execute(INDEX_QUERY.format(db=db_name))
        for row in cursor.fetchall():
            tname = row[0]
            if is_system_table(tname) or tname not in schema['tables']:
                continue
            idx = {
                'name': row[1],
                'type': row[2],
                'is_unique': bool(row[3]),
                'is_primary_key': bool(row[4]),
                'columns': row[5],
            }
            schema['tables'][tname]['indexes'].append(idx)
    except Exception as e:
        print(f"  [WARN] 인덱스 조회 실패: {e}")

    # 3) 행 수
    try:
        cursor.execute(ROW_COUNT_QUERY.format(db=db_name))
        for row in cursor.fetchall():
            if row[0] in schema['tables']:
                schema['tables'][row[0]]['row_count'] = row[1]
    except Exception as e:
        print(f"  [WARN] 행수 조회 실패: {e}")

    return schema


def format_type(col):
    """데이터 타입을 읽기 쉽게 포맷"""
    t = col['data_type']
    if t in ('varchar', 'nvarchar', 'char', 'nchar', 'varbinary'):
        length = col['max_length']
        if t.startswith('n') and length > 0:
            length = length // 2
        if length == -1:
            return f"{t}(MAX)"
        return f"{t}({length})"
    elif t in ('decimal', 'numeric'):
        return f"{t}({col['precision']},{col['scale']})"
    elif t in ('float',) and col['precision'] != 53:
        return f"{t}({col['precision']})"
    return t


def schema_to_markdown(schema):
    """스키마를 마크다운 문서로 변환"""
    lines = [f"# {schema['db_name']} 스키마", ""]
    lines.append(f"테이블 수: {len(schema['tables'])}개\n")

    # 목차
    lines.append("## 목차")
    for i, tname in enumerate(sorted(schema['tables'].keys()), 1):
        t = schema['tables'][tname]
        lines.append(f"{i}. [{tname}](#{tname.lower()}) ({len(t['columns'])}컬럼, {t['row_count']:,}행)")
    lines.append("")

    # 테이블별 상세
    for tname in sorted(schema['tables'].keys()):
        t = schema['tables'][tname]
        lines.append(f"## {tname}")
        lines.append(f"- 행 수: **{t['row_count']:,}**")
        lines.append(f"- 컬럼 수: **{len(t['columns'])}**")
        lines.append("")

        # 컬럼 테이블
        lines.append("| # | 컬럼명 | 데이터 타입 | NULL | PK | 기본값 | 설명 |")
        lines.append("|---|--------|------------|------|----|----|------|")
        for col in t['columns']:
            pk = "PK" if col['is_pk'] else ""
            fk = f"FK→{col['fk_ref_table']}.{col['fk_ref_column']}" if col['is_fk'] else ""
            key = pk or fk or ""
            null = "Y" if col['is_nullable'] else "N"
            default = col['default_value'] or ""
            desc = col['description'] or ""
            identity = " (ID)" if col['is_identity'] else ""
            type_str = format_type(col) + identity
            lines.append(f"| {col['column_id']} | `{col['name']}` | {type_str} | {null} | {key} | {default} | {desc} |")
        lines.append("")

        # 인덱스
        if t['indexes']:
            lines.append("**인덱스:**")
            lines.append("| 인덱스명 | 유형 | 고유 | 컬럼 |")
            lines.append("|---------|------|------|------|")
            for idx in t['indexes']:
                unique = "Y" if idx['is_unique'] else "N"
                pk_tag = " (PK)" if idx['is_primary_key'] else ""
                lines.append(f"| {idx['name']}{pk_tag} | {idx['type']} | {unique} | {idx['columns']} |")
            lines.append("")

        lines.append("---\n")

    return "\n".join(lines)


def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    print("MSSQL 스키마 추출 시작...")
    conn = pymssql.connect(server=SERVER, port=PORT, user=USER, password=PASSWORD, database='master')
    cursor = conn.cursor()

    all_schemas = {}

    for db in MAIN_DBS:
        print(f"\n[{db}] 추출 중...")
        schema = extract_db_schema(cursor, db)
        if schema and schema['tables']:
            all_schemas[db] = schema
            table_count = len(schema['tables'])
            col_count = sum(len(t['columns']) for t in schema['tables'].values())
            print(f"  -> {table_count} 테이블, {col_count} 컬럼 추출 완료")

            # DB별 JSON 저장
            json_path = os.path.join(RAW_DIR, f"{db}.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(schema, f, ensure_ascii=False, indent=2)

            # DB별 마크다운 저장
            md_path = os.path.join(RAW_DIR, f"{db}.md")
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(schema_to_markdown(schema))

            print(f"  -> {json_path}")
            print(f"  -> {md_path}")
        else:
            print(f"  -> 추출 실패 또는 빈 DB")

        time.sleep(0.3)

    conn.close()

    # 통합 요약 마크다운
    summary_lines = ["# 전체 DB 스키마 요약", "", f"추출 일시: 2026-02-23", f"DB 수: {len(all_schemas)}개", ""]

    # 전체 테이블 목록 (중복 제거 비교용)
    all_table_names = {}
    for db, schema in all_schemas.items():
        for tname in schema['tables']:
            if tname.upper() not in all_table_names:
                all_table_names[tname.upper()] = []
            all_table_names[tname.upper()].append({
                'db': db,
                'original_name': tname,
                'col_count': len(schema['tables'][tname]['columns']),
                'row_count': schema['tables'][tname]['row_count']
            })

    summary_lines.append("## DB별 테이블 수")
    summary_lines.append("| DB | 테이블 수 | 총 컬럼 수 | 총 행 수 |")
    summary_lines.append("|-----|----------|-----------|---------|")
    for db in MAIN_DBS:
        if db in all_schemas:
            s = all_schemas[db]
            tc = len(s['tables'])
            cc = sum(len(t['columns']) for t in s['tables'].values())
            rc = sum(t['row_count'] for t in s['tables'].values())
            summary_lines.append(f"| {db} | {tc} | {cc} | {rc:,} |")
    summary_lines.append("")

    summary_lines.append(f"## 고유 테이블 유형: {len(all_table_names)}종")
    summary_lines.append("| 테이블명 | 존재하는 DB 수 | 컬럼수 범위 |")
    summary_lines.append("|---------|--------------|-----------|")
    for tname in sorted(all_table_names.keys()):
        entries = all_table_names[tname]
        col_counts = set(e['col_count'] for e in entries)
        col_range = f"{min(col_counts)}~{max(col_counts)}" if len(col_counts) > 1 else str(min(col_counts))
        summary_lines.append(f"| {entries[0]['original_name']} | {len(entries)} | {col_range} |")
    summary_lines.append("")

    summary_path = os.path.join(RAW_DIR, "_SCHEMA_SUMMARY.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(summary_lines))
    print(f"\n통합 요약: {summary_path}")

    print(f"\n=== 추출 완료 ===")
    print(f"총 {len(all_schemas)}개 DB, {len(all_table_names)}종 테이블 유형")
    print(f"저장 위치: {RAW_DIR}/")


if __name__ == '__main__':
    main()
