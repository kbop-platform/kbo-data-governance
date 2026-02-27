#!/usr/bin/env python3
"""dictionary/**/*.md의 빈 컬럼 설명을 일괄 채움

Phase 4-2: 컬럼 설명 커버리지 ~58% → ~100%

사용법:
  python scripts/fill-descriptions.py          # 실행 (파일 수정)
  python scripts/fill-descriptions.py --dry-run # 변경 내용만 미리보기
"""
import os
import re
import sys
from pathlib import Path

from config import COLUMN_DESC, TABLE_OVERRIDES, BASE_DIR

DICT_DIR = os.path.join(BASE_DIR, 'dictionary')


# ============================================================
# 마크다운 파싱 및 채우기
# ============================================================
# 컬럼 상세 테이블 데이터 행 패턴
ROW_RE = re.compile(
    r'^\|\s*\d+\s*'       # | # |
    r'\|\s*`([^`]+)`\s*'  # | `COL_NAME` |
    r'\|'                  # type 시작
)


def extract_table_name(filepath):
    """파일명에서 테이블명 추출 (확장자 제거)"""
    return Path(filepath).stem


def fill_descriptions(filepath, dry_run=False):
    """하나의 dictionary md 파일의 빈 설명 채움.

    Returns: (filled_count, existing_count, unfilled_names)
    """
    table_name = extract_table_name(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filled = 0
    existing = 0
    unfilled = []

    for i, line in enumerate(lines):
        # 컬럼 상세 테이블 행인지 확인
        m = ROW_RE.match(line)
        if not m:
            continue

        col_name = m.group(1).strip()

        # | 로 분할하여 7번째 필드(설명) 확인
        parts = line.split('|')
        # parts: ['', ' # ', ' `COL` ', ' type ', ' len ', ' NULL ', ' PK ', ' desc ', ' std ', '\n']
        if len(parts) < 9:
            continue

        desc = parts[7].strip()
        if desc:
            existing += 1
            continue

        # 설명 조회: TABLE_OVERRIDES 우선 → COLUMN_DESC
        new_desc = TABLE_OVERRIDES.get((table_name, col_name))
        if not new_desc:
            new_desc = COLUMN_DESC.get(col_name, '')

        if not new_desc:
            unfilled.append(col_name)
            continue

        # 설명 채우기
        parts[7] = f' {new_desc} '
        lines[i] = '|'.join(parts)
        filled += 1

    if filled > 0 and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    return filled, existing, unfilled


def main():
    dry_run = '--dry-run' in sys.argv

    print("=" * 60)
    print("컬럼 설명 채우기 (fill-descriptions.py)")
    if dry_run:
        print("  *** DRY-RUN 모드: 파일 수정 없이 미리보기 ***")
    print("=" * 60)

    total_filled = 0
    total_existing = 0
    total_unfilled = 0
    files_modified = 0
    all_unfilled = []

    for domain in sorted(os.listdir(DICT_DIR)):
        domain_path = os.path.join(DICT_DIR, domain)
        if not os.path.isdir(domain_path):
            continue

        for fname in sorted(os.listdir(domain_path)):
            if not fname.endswith('.md') or fname == 'README.md':
                continue

            filepath = os.path.join(domain_path, fname)
            filled, existing, unfilled = fill_descriptions(filepath, dry_run)

            total_filled += filled
            total_existing += existing
            total_unfilled += len(unfilled)

            if filled > 0 or unfilled:
                files_modified += (1 if filled > 0 else 0)
                status = f"+{filled}" if filled > 0 else " 0"
                msg = f"  {domain}/{fname}: {status} 설명 추가 (기존 {existing})"
                if unfilled:
                    msg += f"  [미해결 {len(unfilled)}개: {', '.join(unfilled)}]"
                print(msg)
                all_unfilled.extend(
                    (domain, fname, c) for c in unfilled
                )

    total_cols = total_filled + total_existing + total_unfilled
    coverage = (total_existing + total_filled) / total_cols * 100 if total_cols else 0

    print(f"\n{'=' * 60}")
    print(f"결과 요약")
    print(f"{'=' * 60}")
    print(f"  전체 컬럼:   {total_cols}")
    print(f"  기존 설명:   {total_existing}")
    print(f"  신규 추가:   {total_filled} ({files_modified}개 파일)")
    print(f"  미해결:      {total_unfilled}")
    print(f"  커버리지:    {coverage:.1f}%")

    if all_unfilled:
        print(f"\n미해결 컬럼 목록:")
        for domain, fname, col in all_unfilled:
            print(f"  {domain}/{fname}: {col}")

    if dry_run and total_filled > 0:
        print(f"\n*** DRY-RUN: 실제 적용하려면 --dry-run 없이 실행하세요 ***")


if __name__ == '__main__':
    main()
