#!/usr/bin/env python3
"""
extract-mapping.py
dictionary/ .md 파일에서 컬럼 매핑 정보를 추출하여
migration/column-mapping.md 를 생성한다.

Usage:
    python scripts/extract-mapping.py
"""

import os
import re
from pathlib import Path
from datetime import date
from config import DOMAIN_ORDER, DOMAIN_TABLES, STANDARD_TABLE_NAMES, BASE_DIR

DICT_DIR = Path(BASE_DIR) / "dictionary"
OUTPUT_DIR = Path(BASE_DIR) / "migration"
OUTPUT_FILE = OUTPUT_DIR / "column-mapping.md"


def parse_column_table(filepath):
    text = filepath.read_text(encoding="utf-8")
    lines_list = text.split("\n")

    start_idx = None
    for i, line in enumerate(lines_list):
        if line.strip().startswith("## 컬럼 상세"):
            start_idx = i
            break
    if start_idx is None:
        return []

    header_idx = None
    for i in range(start_idx + 1, min(start_idx + 5, len(lines_list))):
        if lines_list[i].strip().startswith("| #"):
            header_idx = i
            break
    if header_idx is None:
        return []

    sep_idx = header_idx + 1
    if sep_idx >= len(lines_list) or not re.match(r"^\|[\s\-|]+\|$", lines_list[sep_idx].strip()):
        return []

    columns = []
    for i in range(sep_idx + 1, len(lines_list)):
        line = lines_list[i].strip()
        if not line or line.startswith("##"):
            break
        if not line.startswith("|"):
            break

        cells = [c.strip() for c in line.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]

        if len(cells) < 8:
            continue

        BT = "`"
        columns.append({
            "num": cells[0].strip(),
            "col_name": cells[1].strip().strip(BT),
            "col_type": cells[2].strip(),
            "col_len": cells[3].strip(),
            "nullable": cells[4].strip(),
            "pk": cells[5].strip(),
            "desc": cells[6].strip(),
            "std_name": cells[7].strip().strip(BT),
        })

    return columns


def infer_standard_type(std_name, current_type, current_len, desc):
    if not std_name:
        return format_current_type(current_type, current_len)

    if std_name.endswith("_id"):
        if std_name == "game_id":
            return "char(13)"
        if std_name in ("player_id",):
            return "int"
        if std_name in ("league_id", "series_id", "season_id", "status_id"):
            return "smallint"
        if std_name == "team_id":
            return "char(2)"
        if std_name == "stadium_id":
            return "char(2)"
        return format_current_type(current_type, current_len)

    if std_name.endswith("_nm"):
        return "nvarchar(100)"
    if std_name.endswith("_cd"):
        return "varchar(10)"
    if std_name.endswith("_sc"):
        return "varchar(10)"
    if std_name.endswith("_cn"):
        return "int"
    if std_name.endswith("_rt"):
        return "decimal(8,5)"
    if std_name.endswith("_dt"):
        if current_type == "datetime":
            return "datetime2"
        return "char(8)"
    if std_name.endswith("_yr"):
        if current_type in ("smallint", "int", "tinyint"):
            return "smallint"
        return "char(4)"
    if std_name.endswith("_tm"):
        return "char(4)"
    if std_name.endswith("_if"):
        return "bit"
    if std_name.endswith("_va"):
        return "int"
    if std_name.endswith("_no"):
        return "int"
    if std_name.endswith("_text"):
        return "nvarchar(200)"

    if re.match(r"inn_\d+_(top|bot)$", std_name):
        return "smallint"
    if re.match(r"inn_\d+_(score|loss|out3_score)$", std_name):
        return format_current_type(current_type, current_len)

    baseball_stats = {
        "avg", "era", "whip", "obp", "slg", "ops",
        "hit", "run", "hr", "h2b", "h3b", "rbi",
        "sb", "cs", "sh", "sf", "bb", "ibb", "hbp",
        "so", "gidp", "err", "lob", "pa", "ab",
        "tb_cn", "win", "lose", "draw", "save", "hold",
        "cg", "sho", "qs", "bsv", "wp", "bk",
        "ip", "tbf", "np", "r", "er",
    }
    if std_name in baseball_stats:
        if current_type == "float":
            return "decimal(8,5)"
        return format_current_type(current_type, current_len)

    return format_current_type(current_type, current_len)


def format_current_type(col_type, col_len):
    if col_len:
        return f"{col_type}({col_len})"
    return col_type


def determine_conversion_rule(col, std_type):
    col_name = col["col_name"]
    std_name = col["std_name"]
    current_type = col["col_type"]
    current_len = col["col_len"]
    current_full = format_current_type(current_type, current_len)

    if not std_name:
        return "이름 변경"

    if col_name == std_name:
        if current_full == std_type:
            return "직접 매핑 (이름 유지)"
        return _type_change_rule(current_type, current_len, std_type)

    if current_full == std_type:
        return "이름 변경"

    rule = _type_change_rule(current_type, current_len, std_type)
    if rule != "이름 변경":
        return rule

    return "이름 변경"


def _type_change_rule(current_type, current_len, std_type):
    current_full = format_current_type(current_type, current_len)
    if current_full == std_type:
        return "이름 변경"

    A = "\u2192"

    if current_type == "varchar" and std_type.startswith("nvarchar"):
        return f"인코딩 변환 (varchar{A}nvarchar)"
    if current_type in ("float", "real") and std_type.startswith("decimal"):
        return f"타입 변환 ({current_type}{A}decimal)"
    if current_type in ("smallint", "tinyint") and std_type == "int":
        return f"타입 확장 ({current_type}{A}int)"
    if current_type == "varchar" and std_type == "int":
        return f"타입 변환 (varchar{A}int)"
    if current_type == "char" and current_len == "1" and std_type == "bit":
        return f"타입 변환 (char{A}bit)"
    if current_type == "tinyint" and std_type == "bit":
        return f"타입 변환 (tinyint{A}bit)"
    if current_type == "datetime" and std_type == "datetime2":
        return f"타입 변환 (datetime{A}datetime2)"
    if current_type == "nvarchar" and std_type.startswith("nvarchar"):
        return "길이 변경"
    if current_type == "char" and std_type.startswith("char"):
        cur_len = current_len or ""
        std_len_match = re.search(r"\((\d+)\)", std_type)
        std_len = std_len_match.group(1) if std_len_match else ""
        if cur_len != std_len:
            return f"길이 변경 (char({cur_len}){A}{std_type})"
        return "이름 변경"
    if current_type == "varchar" and std_type.startswith("char"):
        return f"타입 변환 (varchar{A}char)"
    if current_type == "varchar" and std_type == "smallint":
        return f"타입 변환 (varchar{A}smallint)"
    if current_type == "smallint" and std_type == "smallint":
        return "이름 변경"
    if current_type == "int" and std_type == "int":
        return "이름 변경"
    if current_type == "varchar" and std_type.startswith("varchar"):
        return "길이 변경"
    if current_type == "tinyint" and std_type == "smallint":
        return f"타입 확장 (tinyint{A}smallint)"
    return "이름 변경"


def generate_output(all_data):
    today = date.today().isoformat()
    A = "\u2192"
    DASH = "\u2014"

    total_tables = 0
    total_columns = 0
    name_change_count = 0
    type_change_count = 0
    direct_map_count = 0

    for domain, tables in all_data.items():
        for table_name, rows in tables.items():
            total_tables += 1
            for row in rows:
                total_columns += 1
                rule = row["rule"]
                if "직접 매핑" in rule:
                    direct_map_count += 1
                elif ("타입 변환" in rule or "타입 확장" in rule
                      or "인코딩 변환" in rule or "길이 변경" in rule):
                    type_change_count += 1
                else:
                    name_change_count += 1

    out = []
    out.append(f"# 컬럼 매핑 매트릭스 (AS-IS {A} TO-BE)")
    out.append("")
    out.append(f"> 최종수정: {today} | 자동 생성: scripts/extract-mapping.py")
    out.append("")
    out.append("본 문서는 현행 시스템(AS-IS)의 컬럼을 신규 시스템(TO-BE) 표준으로 매핑한 전수 목록이다.")
    out.append("수행사 마이그레이션 핸드오프 문서로 활용한다.")
    out.append("")
    out.append(f"{A} 참고: [도메인 사전](../standards-dict/domains.md) {DASH} 표준 타입 상세")
    out.append(f"{A} 참고: [ID 체계](../standards/id-system.md) {DASH} 식별자 형식")
    out.append("")
    out.append("## 요약")
    out.append("")
    out.append("| 항목 | 수치 |")
    out.append("|------|------|")
    out.append(f"| 총 테이블 | {total_tables} |")
    out.append(f"| 총 컬럼 | {total_columns} |")
    out.append(f"| 이름 변경 | {name_change_count} |")
    out.append(f"| 타입 변환 필요 | {type_change_count} |")
    out.append(f"| 직접 매핑 | {direct_map_count} |")
    out.append("")
    out.append("---")

    section_num = 0
    for domain_key, domain_label in DOMAIN_ORDER:
        section_num += 1
        out.append("")
        out.append(f"## {section_num}. {domain_label} ({domain_key}/)")
        tables = all_data.get(domain_key, {})
        for table_name in DOMAIN_TABLES.get(domain_key, []):
            if table_name not in tables:
                continue
            rows = tables[table_name]
            std_table = STANDARD_TABLE_NAMES.get(table_name, table_name.upper())
            out.append("")
            out.append(f"### {table_name} {A} {std_table}")
            out.append("")
            out.append("| # | 현행 컬럼 | 현행 타입 | 표준 컬럼 | 표준 타입 | 변환 규칙 | 비고 |")
            out.append("|---|----------|----------|----------|----------|----------|------|")
            for row in rows:
                n = row["num"]
                cn = row["col_name"]
                ct = row["current_type"]
                sn = row["std_name"]
                st = row["std_type"]
                ru = row["rule"]
                no = row["note"]
                out.append(f"| {n} | {cn} | {ct} | {sn} | {st} | {ru} | {no} |")

    out.append("")
    return "\n".join(out)


def main():
    all_data = {}

    for domain_key, domain_label in DOMAIN_ORDER:
        domain_dir = DICT_DIR / domain_key
        if not domain_dir.exists():
            print(f"[WARN] 디렉토리 없음: {domain_dir}")
            continue

        all_data[domain_key] = {}

        for table_name in DOMAIN_TABLES.get(domain_key, []):
            md_file = domain_dir / f"{table_name}.md"
            if not md_file.exists():
                print(f"[WARN] 파일 없음: {md_file}")
                continue

            columns = parse_column_table(md_file)
            if not columns:
                print(f"[WARN] 컬럼 상세 없음: {md_file}")
                continue

            rows = []
            for col in columns:
                std_type = infer_standard_type(
                    col["std_name"], col["col_type"], col["col_len"], col["desc"]
                )
                rule = determine_conversion_rule(col, std_type)
                note = "PK" if col["pk"] == "PK" else ""
                rows.append({
                    "num": col["num"],
                    "col_name": col["col_name"],
                    "current_type": format_current_type(col["col_type"], col["col_len"]),
                    "std_name": col["std_name"],
                    "std_type": std_type,
                    "rule": rule,
                    "note": note,
                })

            all_data[domain_key][table_name] = rows

    output = generate_output(all_data)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(output, encoding="utf-8")

    total_tables = sum(len(tables) for tables in all_data.values())
    total_columns = sum(
        len(rows) for tables in all_data.values() for rows in tables.values()
    )
    print(f"처리 완료: {total_tables}개 테이블, {total_columns}개 컬럼")
    print(f"출력 파일: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
