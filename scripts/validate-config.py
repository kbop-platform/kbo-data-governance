#!/usr/bin/env python3
"""config.py 상수 동기화 검증 스크립트

COLUMN_DESC, STANDARD_MAP, TABLE_OVERRIDES 간 정합성과
raw/column-metadata.json 실제 컬럼 대비 커버리지를 검증한다.

사용법:
    python3 scripts/validate-config.py          # 전체 검증
    python3 scripts/validate-config.py --strict  # 경고도 에러 취급 (CI용)
"""

import json, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))
from config import COLUMN_DESC, STANDARD_MAP, TABLE_OVERRIDES

# ── 상수 ──
VALID_SUFFIXES = {'_id', '_nm', '_cd', '_sc', '_cn', '_rt', '_dt', '_tm',
                  '_if', '_va', '_no'}

# ── 데이터 로드 ──
def load_actual_columns():
    """raw/column-metadata.json에서 (table, column) 쌍과 고유 컬럼명 추출"""
    p = BASE / "raw" / "column-metadata.json"
    if not p.exists():
        return set(), {}
    with open(p, encoding="utf-8") as f:
        tables = json.load(f)["tables"]
    pairs = set()        # {(table_name, col_name), ...}
    col_tables = {}      # {col_name: [table1, table2, ...]}
    for tbl, info in tables.items():
        for c in info.get("columns", []):
            name = c["name"]
            pairs.add((tbl, name))
            col_tables.setdefault(name, []).append(tbl)
    return pairs, col_tables


# ── 검증 함수들 ──
def check_coverage(col_tables):
    """실제 컬럼 대비 COLUMN_DESC / STANDARD_MAP 커버리지"""
    errors, warnings = [], []
    override_cols = {k[1] for k in TABLE_OVERRIDES}
    all_cols = set(col_tables.keys())

    missing_desc = sorted(c for c in all_cols
                          if c not in COLUMN_DESC and c not in override_cols)
    missing_std = sorted(c for c in all_cols
                         if c not in STANDARD_MAP and c not in override_cols)

    if missing_desc:
        warnings.append(
            f"COLUMN_DESC 누락 {len(missing_desc)}개: {missing_desc}")
    if missing_std:
        errors.append(
            f"STANDARD_MAP 누락 {len(missing_std)}개: {missing_std}")

    total = len(all_cols)
    desc_cov = total - len(missing_desc)
    std_cov = total - len(missing_std)
    return errors, warnings, {
        "total_columns": total,
        "desc_coverage": f"{desc_cov}/{total} ({desc_cov/total*100:.1f}%)",
        "std_coverage": f"{std_cov}/{total} ({std_cov/total*100:.1f}%)",
    }


def check_orphan_keys(col_tables):
    """실제 컬럼에 없는 COLUMN_DESC/STANDARD_MAP 키 (이닝 패턴 제외)"""
    warnings = []
    actual = set(col_tables.keys())

    # 이닝 패턴 (1T~25T, 1B~25B, INN1~INN25 등) 제외
    inn_pat = re.compile(r'^(\d+[TB]|INN\d+|INN\d+_3|IL\d+)$')

    desc_only = sorted(k for k in COLUMN_DESC
                       if k not in actual and not inn_pat.match(k))
    std_only = sorted(k for k in STANDARD_MAP
                      if k not in actual and not inn_pat.match(k))

    if desc_only:
        warnings.append(
            f"COLUMN_DESC에만 존재 (실제 컬럼에 없음) {len(desc_only)}개: {desc_only}")
    if std_only:
        warnings.append(
            f"STANDARD_MAP에만 존재 (실제 컬럼에 없음) {len(std_only)}개: {std_only}")

    return [], warnings


def check_desc_vs_std_sync():
    """COLUMN_DESC와 STANDARD_MAP 간 키 불일치"""
    warnings = []

    # 이닝 패턴 제외
    inn_pat = re.compile(r'^(\d+[TB]|INN\d+|INN\d+_3|IL\d+)$')

    desc_keys = {k for k in COLUMN_DESC if not inn_pat.match(k)}
    std_keys = {k for k in STANDARD_MAP if not inn_pat.match(k)}

    in_desc_not_std = sorted(desc_keys - std_keys)
    in_std_not_desc = sorted(std_keys - desc_keys)

    if in_desc_not_std:
        warnings.append(
            f"COLUMN_DESC에만 있고 STANDARD_MAP에 없음 {len(in_desc_not_std)}개: "
            f"{in_desc_not_std}")
    if in_std_not_desc:
        warnings.append(
            f"STANDARD_MAP에만 있고 COLUMN_DESC에 없음 {len(in_std_not_desc)}개: "
            f"{in_std_not_desc}")

    return [], warnings


def check_table_overrides(pairs):
    """TABLE_OVERRIDES가 참조하는 (table, column)이 실제 존재하는지"""
    errors = []
    for (tbl, col), (desc, std) in TABLE_OVERRIDES.items():
        if (tbl, col) not in pairs:
            errors.append(
                f"TABLE_OVERRIDES ({tbl}, {col}): 실제 컬럼에 존재하지 않음")
        if not desc:
            errors.append(
                f"TABLE_OVERRIDES ({tbl}, {col}): 설명이 비어있음")
        if not std:
            errors.append(
                f"TABLE_OVERRIDES ({tbl}, {col}): 표준명이 비어있음")
    return errors, []


def check_naming_convention():
    """STANDARD_MAP 값의 네이밍 규칙 준수 (snake_case)"""
    warnings = []
    for key, val in STANDARD_MAP.items():
        if not val:
            warnings.append(f"STANDARD_MAP['{key}']: 빈 값")
            continue
        if val != val.lower():
            warnings.append(
                f"STANDARD_MAP['{key}'] = '{val}': snake_case가 아님")
    return [], warnings


# ── 메인 ──
def main():
    strict = "--strict" in sys.argv
    pairs, col_tables = load_actual_columns()

    all_errors, all_warnings = [], []
    stats = {}

    checks = [
        ("커버리지 검증", lambda: check_coverage(col_tables)),
        ("고아 키 검증", lambda: check_orphan_keys(col_tables)),
        ("DESC↔STD 동기화", lambda: check_desc_vs_std_sync()),
        ("TABLE_OVERRIDES 참조", lambda: check_table_overrides(pairs)),
        ("네이밍 규칙", lambda: check_naming_convention()),
    ]

    for name, fn in checks:
        result = fn()
        if len(result) == 3:
            errors, warnings, st = result
            stats.update(st)
        else:
            errors, warnings = result

        if errors:
            print(f"\n  ERROR  {name}")
            for e in errors:
                print(f"    {e}")
            all_errors.extend(errors)
        if warnings:
            print(f"\n  WARN   {name}")
            for w in warnings:
                print(f"    {w}")
            all_warnings.extend(warnings)
        if not errors and not warnings:
            print(f"  OK     {name}")

    # 요약
    print(f"\n{'='*60}")
    if stats:
        print(f"  고유 컬럼: {stats['total_columns']}개")
        print(f"  COLUMN_DESC:  {stats['desc_coverage']}")
        print(f"  STANDARD_MAP: {stats['std_coverage']}")
        print(f"  TABLE_OVERRIDES: {len(TABLE_OVERRIDES)}개")

    e_cnt = len(all_errors)
    w_cnt = len(all_warnings)
    print(f"\n  결과: 에러 {e_cnt}개, 경고 {w_cnt}개")

    if e_cnt > 0 or (strict and w_cnt > 0):
        print("  FAIL")
        sys.exit(1)
    else:
        print("  PASS")
        sys.exit(0)


if __name__ == "__main__":
    main()
