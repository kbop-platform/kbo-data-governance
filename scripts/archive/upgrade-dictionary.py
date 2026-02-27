#!/usr/bin/env python3
"""
dictionary/ 파일 일괄 업그레이드:
  1) 버전 태그 추가 (최종수정, 출처)
  2) 컬럼 상세 테이블에 '표준명(안)' 컬럼 추가
"""
import os, re, glob
from datetime import date
from config import STANDARD_MAP, suggest_standard_name, BASE_DIR

DICT_DIR = os.path.join(BASE_DIR, "dictionary")
TODAY = date.today().strftime("%Y-%m-%d")


def process_file(filepath):
    """dictionary md 파일 처리: 버전 태그 + 표준명 컬럼 추가"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    table_name = os.path.splitext(os.path.basename(filepath))[0]

    # ── 1) 버전 태그 ──
    # 기존 버전 태그가 있으면 교체, 없으면 제목 바로 아래 삽입
    version_line = f"> 최종수정: {TODAY} | 출처: column-metadata.json"
    if lines and lines[0].startswith("> 최종수정"):
        lines[0] = version_line
    elif lines and lines[0].startswith("# "):
        lines.insert(1, "")
        lines.insert(2, version_line)
    else:
        lines.insert(0, version_line)

    # ── 2) 컬럼 상세 테이블에 표준명(안) 추가 ──
    new_lines = []
    in_column_table = False
    header_done = False

    for line in lines:
        stripped = line.rstrip()

        # 컬럼 상세 테이블 헤더 감지
        if re.match(r'\|\s*#\s*\|\s*컬럼명\s*\|', stripped):
            in_column_table = True
            header_done = False
            # 이미 표준명 있으면 스킵
            if "표준명(안)" in stripped:
                new_lines.append(line)
                in_column_table = False
                continue
            new_lines.append(stripped + " 표준명(안) |")
            continue

        if in_column_table and not header_done:
            # separator 행 (|---|---| ...)
            if re.match(r'\|[-\s|]+\|', stripped):
                new_lines.append(stripped + "------|")
                header_done = True
                continue

        if in_column_table and header_done:
            # 데이터 행
            if stripped.startswith("|") and not stripped.startswith("##"):
                # 컬럼명 추출 (2번째 셀)
                cells = [c.strip() for c in stripped.split("|")]
                # cells[0] = '', cells[1] = #, cells[2] = 컬럼명, ...
                if len(cells) >= 3:
                    col_raw = cells[2].strip("`").strip()
                    std_name = suggest_standard_name(col_raw)
                    new_lines.append(stripped + f" `{std_name}` |")
                    continue
            else:
                # 테이블 끝
                in_column_table = False

        new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    return table_name


def main():
    md_files = []
    for domain in ["game", "stats", "realtime", "master"]:
        domain_dir = os.path.join(DICT_DIR, domain)
        if not os.path.isdir(domain_dir):
            continue
        for f in sorted(os.listdir(domain_dir)):
            if f.endswith(".md") and f != "README.md":
                md_files.append(os.path.join(domain_dir, f))

    print(f"대상 파일: {len(md_files)}개")
    for fp in md_files:
        name = process_file(fp)
        print(f"  ✓ {name}")

    print(f"\n완료: {len(md_files)}개 파일 업데이트 ({TODAY})")


if __name__ == "__main__":
    main()
