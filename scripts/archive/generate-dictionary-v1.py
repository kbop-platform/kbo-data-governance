#!/usr/bin/env python3
"""column-metadata.json에서 도메인별 테이블 사전 마크다운 생성"""
import json
import os
from pathlib import Path
from config import DOMAINS, COLUMN_DESC, BASE_DIR

META_PATH = os.path.join(BASE_DIR, 'raw', 'column-metadata.json')
DICT_DIR = os.path.join(BASE_DIR, 'dictionary')

def get_description(col_name, data_type, distinct_values):
    """컬럼 설명 생성"""
    # 직접 매핑
    if col_name in COLUMN_DESC:
        return COLUMN_DESC[col_name]

    # TB는 맥락에 따라 다름 (타격 테이블에서는 총루타, 경기에서는 팀구분)
    if col_name == 'TB' and data_type == 'int':
        return '총루타 (Total Bases)'

    # INN 이닝 관련
    if col_name.startswith('INN') and col_name not in ('INN', 'INN2', 'INN_NO'):
        return f'이닝 점수 컬럼'

    # Score 이닝 컬럼
    for prefix in ('T', 'B'):
        for i in range(1, 26):
            if col_name == f'{prefix}{i}':
                side = '원정' if prefix == 'T' else '홈'
                return f'{i}회 {side}팀 점수'

    # _CN, _RT, _IF, _SC 접미사
    if col_name.endswith('_CN'):
        return f'{col_name[:-3]} 건수'
    if col_name.endswith('_RT'):
        return f'{col_name[:-3]} 비율'
    if col_name.endswith('_IF'):
        return f'{col_name[:-3]} 여부 (Y/N)'
    if col_name.endswith('_SC'):
        return f'{col_name[:-3]} 상태코드'
    if col_name.endswith('_CD'):
        return f'{col_name[:-3]} 코드'
    if col_name.endswith('_VA'):
        return f'{col_name[:-3]} 값'
    if col_name.endswith('_ME'):
        return f'{col_name[:-3]} 메모'
    if col_name.endswith('_NM'):
        return f'{col_name[:-3]} 명칭'
    if col_name.endswith('_DT'):
        return f'{col_name[:-3]} 일시'
    if col_name.endswith('_TM'):
        return f'{col_name[:-3]} 시각'
    if col_name.endswith('_NO'):
        return f'{col_name[:-3]} 번호'

    return ''

def format_distinct(distinct_values, max_show=8):
    """코드값 포맷"""
    if not distinct_values:
        return ''
    items = []
    for d in distinct_values[:max_show]:
        v = d['value']
        c = d['count']
        items.append(f'`{v}`({c:,})')
    rest = len(distinct_values) - max_show
    result = ', '.join(items)
    if rest > 0:
        result += f' 외 {rest}건'
    return result

def generate_table_md(table_name, meta):
    """하나의 테이블에 대한 마크다운 생성"""
    lines = []
    lines.append(f"# {table_name}")
    lines.append("")

    lines.append(f"| 항목 | 값 |")
    lines.append(f"|------|-----|")
    lines.append(f"| 대표 DB | `{meta['representative_db']}` |")
    lines.append(f"| 행 수 | {meta['row_count']:,} |")
    lines.append(f"| 컬럼 수 | {meta['column_count']} |")
    lines.append(f"| PK | `{', '.join(meta['pk_columns'])}` |")
    lines.append(f"| 스키마 세대 | {meta['schema_generation']} |")
    lines.append("")

    lines.append("## 컬럼 상세")
    lines.append("")
    lines.append("| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 |")
    lines.append("|---|--------|------|------|------|----|------|")

    for col in meta['columns']:
        pk = "PK" if col['is_pk'] else ""
        null = "" if col['is_nullable'] else "NN"
        desc = get_description(col['name'], col['data_type'], col.get('distinct_values'))
        # 길이 표시
        if col['data_type'] in ('int', 'bigint', 'smallint', 'tinyint', 'bit', 'float', 'real', 'datetime', 'datetime2', 'date', 'time'):
            length = ''
        else:
            length = str(col['max_length'])

        lines.append(f"| {col['ordinal']} | `{col['name']}` | {col['data_type']} | {length} | {null} | {pk} | {desc} |")

    # 코드값 섹션
    code_cols = [c for c in meta['columns'] if c.get('distinct_values')]
    if code_cols:
        lines.append("")
        lines.append("## 코드값 / 고유값")
        lines.append("")
        for col in code_cols:
            lines.append(f"### `{col['name']}`")
            lines.append("")
            lines.append(f"| 값 | 건수 |")
            lines.append(f"|-----|------|")
            for d in col['distinct_values'][:20]:
                lines.append(f"| `{d['value']}` | {d['count']:,} |")
            lines.append("")

    # 샘플 데이터
    lines.append("## 샘플 데이터")
    lines.append("")
    lines.append("| 컬럼 | 샘플 |")
    lines.append("|------|------|")
    for col in meta['columns']:
        samples = col.get('sample_values', [])
        if samples:
            sample_str = ', '.join(f'`{s}`' for s in samples[:3])
        else:
            sample_str = '(NULL)'
        lines.append(f"| `{col['name']}` | {sample_str} |")
    lines.append("")

    return '\n'.join(lines)


def main():
    with open(META_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 도메인별 디렉토리 생성 및 파일 생성
    for domain, info in DOMAINS.items():
        domain_dir = os.path.join(DICT_DIR, domain)
        os.makedirs(domain_dir, exist_ok=True)

        # 도메인 인덱스
        index_lines = [f"# {info['label']} 테이블 사전", ""]
        index_lines.append(f"| 테이블 | 컬럼 수 | 행 수 | PK | 스키마 |")
        index_lines.append(f"|--------|--------|-------|-----|--------|")

        for tname in info['tables']:
            if tname not in data['tables']:
                print(f"  SKIP: {tname} (not in metadata)")
                continue

            meta = data['tables'][tname]
            pk_str = ', '.join(meta['pk_columns'])
            index_lines.append(f"| [{tname}](./{tname}.md) | {meta['column_count']} | {meta['row_count']:,} | {pk_str} | {meta['schema_generation']} |")

            # 개별 파일
            md = generate_table_md(tname, meta)
            out_path = os.path.join(domain_dir, f"{tname}.md")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md)
            print(f"  {domain}/{tname}.md ({meta['column_count']} cols)")

        index_lines.append("")
        index_path = os.path.join(domain_dir, "README.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(index_lines))
        print(f"  {domain}/README.md")

    print(f"\nDone. Generated {sum(len(d['tables']) for d in DOMAINS.values())} table docs in {len(DOMAINS)} domains.")

if __name__ == '__main__':
    main()
