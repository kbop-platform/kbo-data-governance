#!/usr/bin/env python3
"""
OPS 테이블 명세서 PDF 파싱 v2
- 줄 단위 텍스트 기반 파싱
"""
import fitz
import json
import re
import os

PDF_PATH = '/home/user/dev/data-dict/KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf'
RAW_DIR = '/home/user/dev/data-dict/raw'

TYPE_KEYWORDS = {'BIGINT', 'INT', 'INTEGER', 'SMALLINT', 'TINYINT',
                 'VARCHAR', 'NVARCHAR', 'CHAR', 'NCHAR', 'TEXT', 'NTEXT',
                 'DATETIME', 'DATETIME2', 'DATE', 'TIME',
                 'BIT', 'FLOAT', 'REAL', 'DECIMAL', 'NUMERIC',
                 'IMAGE', 'VARBINARY', 'BINARY'}

def parse_pdf():
    doc = fitz.open(PDF_PATH)
    tables = []

    # 먼저 TABLE LIST (p2-5)에서 목록 추출
    table_list = []
    for page_num in range(1, 5):
        page = doc[page_num]
        text = page.get_text()
        lines = text.strip().split('\n')
        current_category = ''
        for line in lines:
            line = line.strip()
            # "No Category Table Name Description Attribute" 헤더 스킵
            if not line or 'TABLE LIST' in line or 'Project Name' in line or 'Creator' in line:
                continue
            if 'System Name' in line or 'Created' in line or '페이지' in line or '스포츠투아이' in line:
                continue
            if 'KBO 테이블 명세서' in line or 'No' == line or 'Category' in line:
                continue

            # 숫자로 시작하는 줄 = 테이블 항목
            m = re.match(r'^(\d+)$', line)
            if m:
                # 다음 줄들에서 category, name, desc 추출됨
                table_list.append({'no': int(m.group(1)), 'category': '', 'name': '', 'desc': ''})
                continue

            # 카테고리명 (MASTER, RECORD, LIVE 등)
            if line in ('MASTER', 'RECORD', 'LIVE', 'ALARM', 'APPROVAL', 'MONITORING',
                        'OFFICAL', 'USER', '업무관련'):
                current_category = line
                if table_list and not table_list[-1]['category']:
                    table_list[-1]['category'] = line
                continue

            # 테이블명이나 설명 할당
            if table_list:
                last = table_list[-1]
                if not last['category'] and current_category:
                    last['category'] = current_category
                if not last['name']:
                    last['name'] = line
                elif not last['desc']:
                    last['desc'] = line
                # Attribute는 무시

    print(f"TABLE LIST에서 {len(table_list)} 항목 추출")

    # TABLE DESCRIPTION 파싱 (p6~125)
    for page_num in range(5, len(doc)):
        page = doc[page_num]
        text = page.get_text()
        lines = text.strip().split('\n')

        # Table Name 찾기
        table_name = ''
        table_desc = ''
        primary_key = ''
        table_detail = ''

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line == 'Table Name' and i + 1 < len(lines):
                table_name = lines[i + 1].strip()
                i += 2
                continue

            if line == 'Description' and i + 1 < len(lines) and not table_desc:
                # Description 뒤에 오는 줄이 실제 설명
                candidate = lines[i + 1].strip()
                if candidate and candidate not in ('Primary Key', 'Foreign Key', 'Index Key'):
                    table_desc = candidate
                i += 2
                continue

            if line == 'Primary Key' and i + 1 < len(lines):
                pk_candidate = lines[i + 1].strip()
                if pk_candidate and pk_candidate not in ('Foreign Key', 'Index Key', ''):
                    primary_key = pk_candidate
                i += 2
                continue

            if line == 'Table Detail Description' and i + 1 < len(lines):
                detail_lines = []
                for j in range(i + 1, len(lines)):
                    dl = lines[j].strip()
                    if dl and '페이지' not in dl and '스포츠투아이' not in dl and 'KBO 테이블' not in dl:
                        detail_lines.append(dl)
                table_detail = '\n'.join(detail_lines)
                break

            i += 1

        if not table_name:
            continue

        # 컬럼 파싱
        columns = []
        col_section = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            # 컬럼 헤더 감지
            if stripped == 'No' and i + 1 < len(lines) and 'Physical Name' in lines[i + 1]:
                col_section = True
                # 헤더 줄들 스킵
                continue

            if 'Physical Name' in stripped and 'Logical Name' in stripped:
                col_section = True
                continue

            if stripped in ('No', 'Physical Name', 'Logical Name', 'Data Type', 'Len', 'NULL', 'PK', 'Default'):
                continue

            if stripped == 'Table Detail Description':
                col_section = False
                continue

            if not col_section:
                continue

            # 숫자로 시작하면 컬럼 번호
            m = re.match(r'^(\d+)$', stripped)
            if m:
                col_no = int(m.group(1))

                # 이후 줄들에서 컬럼 정보 수집
                col = {
                    'no': col_no,
                    'physical_name': '',
                    'logical_name': '',
                    'data_type': '',
                    'length': '',
                    'nullable': '',
                    'pk': '',
                    'default': ''
                }

                # 다음 줄들을 소비하면서 파싱
                remaining_parts = []
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    # 다음 컬럼 번호나 섹션 시작이면 중단
                    if re.match(r'^\d+$', next_line):
                        break
                    if next_line == 'Table Detail Description':
                        break
                    if next_line:
                        remaining_parts.append(next_line)
                    j += 1

                # remaining_parts에서 정보 추출
                parse_column_parts(col, remaining_parts)
                if col['physical_name']:
                    columns.append(col)

        # 테이블 저장
        if table_name and columns:
            # TABLE LIST에서 카테고리 찾기
            category = ''
            for tl in table_list:
                if tl['name'] == table_name:
                    category = tl['category']
                    break

            table = {
                'physical_name': table_name,
                'logical_name': table_desc,
                'category': category,
                'primary_key': primary_key,
                'detail': table_detail,
                'columns': columns,
                'page': page_num + 1
            }
            # 중복 체크 (같은 테이블이 2페이지에 걸친 경우)
            existing = next((t for t in tables if t['physical_name'] == table_name), None)
            if existing:
                # 컬럼이 더 많으면 교체, 아니면 추가
                existing_nos = {c['no'] for c in existing['columns']}
                for c in columns:
                    if c['no'] not in existing_nos:
                        existing['columns'].append(c)
                if table_detail and not existing['detail']:
                    existing['detail'] = table_detail
            else:
                tables.append(table)

    doc.close()
    return tables, table_list

def parse_column_parts(col, parts):
    """컬럼 파트들에서 정보 추출"""
    if not parts:
        return

    # parts 예시: ['COLUMN_NM', '컬럼 이름', 'VARCHAR', '20', 'NN', 'PK', '']
    # 또는: ['LE_ID', '리그 ID', 'SMALLINT', '2', 'NN', 'PK']
    # 또는 줄이 합쳐진 경우: ['BEFORE_HOME_SCORE_CN 이전 홈 팀 점수', 'SMALLINT', '2', 'NN']

    # 먼저 모든 parts를 하나로 합쳐서 다시 분리
    all_tokens = []
    for p in parts:
        all_tokens.extend(p.split())

    if not all_tokens:
        return

    # 첫 토큰 = physical name
    col['physical_name'] = all_tokens[0]

    # 데이터 타입 위치 찾기
    type_idx = -1
    for idx, token in enumerate(all_tokens[1:], 1):
        if token.upper() in TYPE_KEYWORDS:
            type_idx = idx
            break

    if type_idx < 0:
        # 타입을 못 찾으면 logical name만
        col['logical_name'] = ' '.join(all_tokens[1:])
        return

    # type 이전 = logical name
    col['logical_name'] = ' '.join(all_tokens[1:type_idx])
    col['data_type'] = all_tokens[type_idx].upper()

    # type 이후
    after = all_tokens[type_idx + 1:]
    for token in after:
        tu = token.upper()
        if re.match(r'^\d+$', tu):
            if not col['length']:
                col['length'] = tu
        elif tu == 'NN':
            col['nullable'] = 'NN'
        elif tu == 'PK':
            col['pk'] = 'PK'
        elif tu in ('GETDATE()', "''", '0', '1', "N''"):
            col['default'] = token
        # 그 외는 무시 (빈 문자열 등)

def tables_to_markdown(tables):
    """마크다운 변환"""
    lines = ["# OPS 테이블 명세서 (Sports2i)", ""]
    lines.append(f"출처: KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf")
    lines.append(f"테이블 수: {len(tables)}개")
    total_cols = sum(len(t['columns']) for t in tables)
    lines.append(f"총 컬럼 수: {total_cols}개")
    lines.append("")

    # 카테고리별 목차
    categories = {}
    for t in tables:
        cat = t.get('category', '미분류')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(t)

    lines.append("## 카테고리별 목차")
    for cat, cat_tables in categories.items():
        lines.append(f"\n### {cat} ({len(cat_tables)}개)")
        for t in cat_tables:
            lines.append(f"- [{t['physical_name']}](#{t['physical_name'].lower()}) - {t['logical_name']} ({len(t['columns'])}컬럼)")
    lines.append("")

    # 각 테이블 상세
    for t in tables:
        pn = t['physical_name']
        lines.append(f"## {pn}")
        lines.append(f"- 논리명: **{t['logical_name']}**")
        lines.append(f"- 카테고리: {t.get('category', '미분류')}")
        lines.append(f"- Primary Key: `{t.get('primary_key', '')}`")
        lines.append(f"- 컬럼 수: **{len(t['columns'])}**")
        if t.get('detail'):
            lines.append(f"- 상세: {t['detail']}")
        lines.append("")

        if t['columns']:
            lines.append("| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |")
            lines.append("|---|--------|--------|-----------|------|------|----|--------|")
            for col in sorted(t['columns'], key=lambda c: c['no']):
                lines.append(f"| {col['no']} | `{col['physical_name']}` | {col['logical_name']} | {col['data_type']} | {col['length']} | {col['nullable']} | {col['pk']} | {col['default']} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)

def main():
    tables, table_list = parse_pdf()

    total_cols = sum(len(t['columns']) for t in tables)
    empty = [t['physical_name'] for t in tables if not t['columns']]

    print(f"\n=== 최종 결과 ===")
    print(f"TABLE LIST: {len(table_list)}개")
    print(f"파싱된 테이블: {len(tables)}개")
    print(f"총 컬럼: {total_cols}개")
    if empty:
        print(f"컬럼 없음: {empty}")

    print(f"\n--- 테이블별 ---")
    for t in tables:
        cat = t.get('category', '?')
        print(f"  [{cat:12s}] {t['physical_name']:45s} | {t['logical_name']:25s} | {len(t['columns']):3d} cols | PK: {t.get('primary_key', '')}")

    # JSON
    json_path = os.path.join(RAW_DIR, 'ops-schema.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(tables, f, ensure_ascii=False, indent=2)
    print(f"\nJSON: {json_path}")

    # Markdown
    md_path = os.path.join(RAW_DIR, 'ops-schema.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(tables_to_markdown(tables))
    print(f"MD: {md_path}")

    # TABLE LIST에 있지만 파싱 안된 테이블 확인
    parsed_names = {t['physical_name'] for t in tables}
    missing = [tl for tl in table_list if tl['name'] and tl['name'] not in parsed_names]
    if missing:
        print(f"\n파싱 누락 ({len(missing)}개):")
        for m in missing:
            print(f"  {m['no']:3d}. [{m['category']}] {m['name']} - {m['desc']}")

if __name__ == '__main__':
    main()
