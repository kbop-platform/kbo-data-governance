#!/usr/bin/env python3
"""
OPS 테이블 명세서 PDF 파싱 스크립트
- 111개 테이블의 컬럼 상세 정보 추출
- raw/ops-schema.json, raw/ops-schema.md 저장
"""
import fitz  # PyMuPDF
import json
import re
import os

PDF_PATH = '/home/user/dev/data-dict/KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf'
RAW_DIR = '/home/user/dev/data-dict/raw'

def extract_all_text(pdf_path):
    """PDF에서 전체 텍스트 추출"""
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append({'page': i + 1, 'text': text})
    doc.close()
    return pages

def parse_table_page(text, page_num):
    """테이블 명세 페이지에서 테이블 정보 파싱"""
    lines = text.strip().split('\n')

    table_info = {
        'page': page_num,
        'physical_name': '',
        'logical_name': '',
        'category': '',
        'columns': []
    }

    # 테이블명 추출 - "TABLE DESCRIPTION" 이후
    # 패턴: No. XX  PHYSICAL_NAME  논리명
    for i, line in enumerate(lines):
        # No. 패턴으로 테이블 시작 감지
        no_match = re.match(r'No\.\s*(\d+)', line)
        if no_match:
            table_info['no'] = int(no_match.group(1))

        # Physical Name 찾기
        if 'Physical Name' in line or 'Physical  Name' in line:
            # 같은 줄 또는 다음 줄에서 값 추출
            pn_match = re.search(r'Physical\s+Name\s+(\S+)', line)
            if pn_match:
                table_info['physical_name'] = pn_match.group(1)
            elif i + 1 < len(lines):
                table_info['physical_name'] = lines[i + 1].strip()

        if 'Logical Name' in line or 'Logical  Name' in line:
            ln_match = re.search(r'Logical\s+Name\s+(.+)', line)
            if ln_match:
                table_info['logical_name'] = ln_match.group(1).strip()
            elif i + 1 < len(lines):
                table_info['logical_name'] = lines[i + 1].strip()

    # 컬럼 파싱 - 테이블 형태의 데이터
    # 헤더: No  Physical Name  Logical Name  Data Type  Length  NULL  PK  Default
    in_columns = False
    col_header_found = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 컬럼 헤더 감지
        if ('Data Type' in stripped or 'Data  Type' in stripped) and 'Physical' in stripped:
            col_header_found = True
            in_columns = True
            continue

        if not in_columns:
            continue

        # 빈 줄이나 페이지 끝 감지
        if stripped == '' or 'TABLE DESCRIPTION' in stripped:
            continue

        # 숫자로 시작하는 줄 = 컬럼 데이터
        col_match = re.match(r'^(\d+)\s+(.+)', stripped)
        if col_match:
            col_no = int(col_match.group(1))
            rest = col_match.group(2)

            # 컬럼 데이터 파싱 시도
            col = parse_column_line(col_no, rest)
            if col:
                table_info['columns'].append(col)

    return table_info if table_info['physical_name'] else None

def parse_column_line(col_no, text):
    """컬럼 라인 파싱"""
    # 다양한 패턴 시도
    # 패턴: PHYSICAL_NAME LOGICAL_NAME DATA_TYPE LENGTH NULL PK DEFAULT

    parts = text.split()
    if len(parts) < 3:
        return None

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

    # 첫 번째는 항상 Physical Name
    col['physical_name'] = parts[0]

    # 나머지에서 데이터 타입 찾기
    # 데이터 타입 키워드
    type_keywords = ['BIGINT', 'INT', 'INTEGER', 'SMALLINT', 'TINYINT',
                     'VARCHAR', 'NVARCHAR', 'CHAR', 'NCHAR', 'TEXT', 'NTEXT',
                     'DATETIME', 'DATE', 'TIME', 'TIMESTAMP', 'DATETIME2',
                     'BIT', 'FLOAT', 'REAL', 'DECIMAL', 'NUMERIC',
                     'IMAGE', 'VARBINARY', 'BINARY', 'UNIQUEIDENTIFIER']

    type_idx = -1
    for idx, p in enumerate(parts[1:], 1):
        p_upper = p.upper().rstrip(',').rstrip(')')
        # 괄호 포함 체크: VARCHAR(100) 등
        base_type = re.split(r'[\(\)]', p_upper)[0]
        if base_type in type_keywords:
            type_idx = idx
            break

    if type_idx > 0:
        # type 이전까지가 logical name
        col['logical_name'] = ' '.join(parts[1:type_idx])

        # data type
        type_str = parts[type_idx].upper()
        col['data_type'] = type_str

        # type 이후 파싱
        remaining = parts[type_idx + 1:]

        # Length, NULL, PK, Default 순서로 파싱
        for j, r in enumerate(remaining):
            r_upper = r.upper()
            if r_upper in ('Y', 'N', 'NULL', 'NOT'):
                col['nullable'] = r_upper
            elif r_upper == 'PK' or r_upper == 'P':
                col['pk'] = 'PK'
            elif re.match(r'^\d+$', r):
                if not col['length']:
                    col['length'] = r
            elif r_upper in ('GETDATE()', 'GETDATE', "''", '0', '1'):
                col['default'] = r
    else:
        # 타입을 찾지 못한 경우 - 최선의 추정
        col['logical_name'] = ' '.join(parts[1:])

    return col

def extract_tables_by_structured_parsing(pages):
    """구조화된 파싱으로 테이블 추출"""
    tables = []
    current_table = None

    for page_data in pages:
        text = page_data['text']
        page_num = page_data['page']

        # 페이지 6부터 테이블 시작 (1-5는 목차)
        if page_num < 6:
            continue

        result = parse_table_page(text, page_num)
        if result and result['physical_name']:
            # 새 테이블이면 이전 것 저장
            if current_table and current_table['physical_name'] != result['physical_name']:
                tables.append(current_table)
                current_table = result
            elif current_table and current_table['physical_name'] == result['physical_name']:
                # 같은 테이블의 연속 페이지 - 컬럼 추가
                current_table['columns'].extend(result['columns'])
            else:
                current_table = result
        elif current_table and result:
            # physical_name 없으면 연속 페이지
            current_table['columns'].extend(result.get('columns', []))

    if current_table:
        tables.append(current_table)

    return tables

def extract_with_table_detection(pages):
    """PDF 텍스트에서 테이블 추출 (개선된 방법)"""
    all_text = '\n'.join([p['text'] for p in pages[5:]])  # page 6부터

    tables = []

    # "No. N" 패턴으로 테이블 분리
    # 각 테이블 섹션 찾기
    sections = re.split(r'(?=No\.\s*\d+)', all_text)

    for section in sections:
        if not section.strip():
            continue

        no_match = re.match(r'No\.\s*(\d+)', section)
        if not no_match:
            continue

        table_no = int(no_match.group(1))
        lines = section.strip().split('\n')

        table = {
            'no': table_no,
            'physical_name': '',
            'logical_name': '',
            'columns': []
        }

        # 테이블명 추출
        for i, line in enumerate(lines):
            if 'Physical Name' in line or 'Physical  Name' in line:
                # 같은 줄에서 추출
                match = re.search(r'Physical\s+Name\s+(\S+)', line)
                if match:
                    table['physical_name'] = match.group(1)
                else:
                    # 다음 줄에서 찾기
                    for j in range(i+1, min(i+3, len(lines))):
                        if lines[j].strip() and not lines[j].strip().startswith('Logical'):
                            table['physical_name'] = lines[j].strip().split()[0]
                            break

            if 'Logical Name' in line or 'Logical  Name' in line:
                match = re.search(r'Logical\s+Name\s+(.+?)(?:\s{2,}|$)', line)
                if match:
                    table['logical_name'] = match.group(1).strip()

        # 컬럼 추출 - 숫자로 시작하는 줄에서
        in_col_section = False
        for line in lines:
            stripped = line.strip()
            if 'Data Type' in stripped and ('Physical' in stripped or 'No' in stripped):
                in_col_section = True
                continue

            if not in_col_section:
                continue

            # No. N 으로 새 테이블 시작하면 중단
            if re.match(r'No\.\s*\d+', stripped):
                break

            # 숫자로 시작하는 컬럼 라인
            col_match = re.match(r'^(\d+)\s+(\S+)\s+(.*)', stripped)
            if col_match:
                col_no = int(col_match.group(1))
                phys_name = col_match.group(2)
                rest = col_match.group(3)

                col = {
                    'no': col_no,
                    'physical_name': phys_name,
                    'logical_name': '',
                    'data_type': '',
                    'length': '',
                    'nullable': '',
                    'pk': '',
                    'default': ''
                }

                # rest에서 정보 추출
                rest_parts = rest.split()

                type_keywords = {'BIGINT', 'INT', 'INTEGER', 'SMALLINT', 'TINYINT',
                                'VARCHAR', 'NVARCHAR', 'CHAR', 'NCHAR', 'TEXT', 'NTEXT',
                                'DATETIME', 'DATETIME2', 'DATE', 'TIME', 'TIMESTAMP',
                                'BIT', 'FLOAT', 'REAL', 'DECIMAL', 'NUMERIC',
                                'IMAGE', 'VARBINARY', 'BINARY', 'UNIQUEIDENTIFIER'}

                type_idx = -1
                for idx, p in enumerate(rest_parts):
                    base = re.split(r'[\(\)]', p.upper())[0]
                    if base in type_keywords:
                        type_idx = idx
                        break

                if type_idx >= 0:
                    col['logical_name'] = ' '.join(rest_parts[:type_idx])
                    col['data_type'] = rest_parts[type_idx].upper()

                    after_type = rest_parts[type_idx + 1:]
                    for p in after_type:
                        pu = p.upper().strip()
                        if re.match(r'^\d+$', pu):
                            col['length'] = pu
                        elif pu in ('Y', 'N'):
                            if not col['nullable']:
                                col['nullable'] = pu
                            elif not col['pk'] and pu == 'Y':
                                pass  # 두번째 Y/N은 다른 의미일 수 있음
                        elif pu == 'PK' or (pu == 'P' and not col['pk']):
                            col['pk'] = 'PK'
                        elif pu in ('GETDATE()', "''", '0', '1', 'NULL', "N''"):
                            col['default'] = p
                else:
                    col['logical_name'] = rest

                table['columns'].append(col)

        if table['physical_name']:
            tables.append(table)

    return tables

def tables_to_markdown(tables):
    """테이블 목록을 마크다운으로 변환"""
    lines = ["# OPS 테이블 명세서 (Sports2i)", ""]
    lines.append(f"테이블 수: {len(tables)}개")
    lines.append(f"출처: KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf")
    lines.append("")

    # 목차
    lines.append("## 목차")
    for t in tables:
        no = t.get('no', '?')
        pn = t['physical_name']
        ln = t.get('logical_name', '')
        cc = len(t['columns'])
        lines.append(f"{no}. [{pn}](#{pn.lower()}) - {ln} ({cc}컬럼)")
    lines.append("")

    # 각 테이블 상세
    for t in tables:
        pn = t['physical_name']
        ln = t.get('logical_name', '')
        lines.append(f"## {pn}")
        lines.append(f"- 논리명: **{ln}**")
        lines.append(f"- 컬럼 수: **{len(t['columns'])}**")
        lines.append(f"- 페이지: {t.get('page', '?')}")
        lines.append("")

        if t['columns']:
            lines.append("| # | 컬럼명 | 논리명 | 데이터 타입 | 길이 | NULL | PK | 기본값 |")
            lines.append("|---|--------|--------|-----------|------|------|----|--------|")
            for col in t['columns']:
                lines.append(f"| {col['no']} | `{col['physical_name']}` | {col['logical_name']} | {col['data_type']} | {col['length']} | {col['nullable']} | {col['pk']} | {col['default']} |")
        else:
            lines.append("*(컬럼 파싱 실패)*")

        lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)

def main():
    print("PDF 파싱 시작...")
    pages = extract_all_text(PDF_PATH)
    print(f"총 {len(pages)} 페이지")

    # 방법 1: 구조화된 파싱
    print("\n구조화된 파싱 시도...")
    tables1 = extract_tables_by_structured_parsing(pages)
    print(f"방법1: {len(tables1)} 테이블 추출")

    # 방법 2: 텍스트 분할 파싱
    print("\n텍스트 분할 파싱 시도...")
    tables2 = extract_with_table_detection(pages)
    print(f"방법2: {len(tables2)} 테이블 추출")

    # 더 많이 추출된 결과 사용
    tables = tables2 if len(tables2) >= len(tables1) else tables1

    # 컬럼 없는 테이블이 있으면 다른 결과에서 보충
    other = tables1 if tables == tables2 else tables2
    other_map = {t['physical_name']: t for t in other}

    for t in tables:
        if not t['columns'] and t['physical_name'] in other_map:
            alt = other_map[t['physical_name']]
            if alt['columns']:
                t['columns'] = alt['columns']

    # 통계 출력
    total_cols = sum(len(t['columns']) for t in tables)
    empty_tables = [t['physical_name'] for t in tables if not t['columns']]

    print(f"\n=== 최종 결과 ===")
    print(f"테이블: {len(tables)}개")
    print(f"총 컬럼: {total_cols}개")
    if empty_tables:
        print(f"컬럼 파싱 실패: {len(empty_tables)}개 - {empty_tables}")

    for t in tables:
        print(f"  {t.get('no', '?'):3}. {t['physical_name']:45s} | {t.get('logical_name', ''):20s} | {len(t['columns']):3d} cols")

    # JSON 저장
    json_path = os.path.join(RAW_DIR, 'ops-schema.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(tables, f, ensure_ascii=False, indent=2)
    print(f"\nJSON 저장: {json_path}")

    # Markdown 저장
    md_path = os.path.join(RAW_DIR, 'ops-schema.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(tables_to_markdown(tables))
    print(f"Markdown 저장: {md_path}")

if __name__ == '__main__':
    main()
