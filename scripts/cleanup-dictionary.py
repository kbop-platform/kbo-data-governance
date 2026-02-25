#!/usr/bin/env python3
"""dictionary/ 39개 파일 정리 스크립트

- FK 컬럼 코드값 → 참조 한 줄로 대체
- 연속값(BIRTH, HEIGHT 등) → 범위 요약으로 대체
- 나머지 코드값 → 상위 5행만 유지
- 샘플 데이터 → 상위 10행만 유지
"""

import re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

# FK 컬럼: 선수/경기/팀 등 외래키
FK_COLUMNS = {
    # 선수 FK
    "PCODE", "P_ID", "PlayerID", "HITTER", "PITCHER", "CATCHER",
    "BatOrder",  # IE_BatterRecord의 BatOrder는 선수 식별
    # 경기 FK (단, GMKEY는 PK이므로 제외)
    "gameID", "GAMEID",
    # 팀 FK (TEAM.md 자체에서는 유지)
    # "TEAM", "T_ID" → 별도 처리
}

# 연속값 컬럼: 프로파일링 데이터, 코드 아님
CONTINUOUS_COLUMNS = {
    "BIRTH", "HEIGHT", "WEIGHT", "INDATE",
    "MONEY", "PROMISE", "CAREER", "DRAFT",
    "ENGNAME", "CNAME", "NAME",
    # 점수/통계 연속값
    "GMTM", "ENTM", "STTM", "DLTM",
    "TEMP", "MOIS", "WINS",
    # 시간/날짜 패턴
    "REG_DT", "INPUTTIME",
}

# 고카디널리티 패턴 (값이 모두 숫자이고 20행 가득 차면 FK/연속)
def is_high_cardinality_numeric(values):
    """값 목록이 대부분 숫자이면 True"""
    if len(values) < 15:
        return False
    numeric = sum(1 for v in values if re.match(r"^-?\d+\.?\d*$", v.strip("`").strip()))
    return numeric / len(values) > 0.8


def get_fk_reference(col_name):
    """FK 컬럼에 대한 참조 문구"""
    if col_name in ("PCODE", "P_ID", "PlayerID", "HITTER", "PITCHER", "CATCHER", "BatOrder"):
        return "→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조"
    if col_name in ("gameID", "GAMEID"):
        return "→ 경기 식별자 — [경기 정보(GAMEINFO)](../game/GAMEINFO.md) 참조"
    return "→ FK 참조"


def process_file(md_path):
    """단일 dictionary .md 파일 정리"""
    with open(md_path, encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    result = []
    i = 0
    total = len(lines)
    in_code_section = False
    in_sample_section = False
    current_col = None
    code_table_rows = []
    sample_rows = 0
    stats = {"removed_sections": 0, "compressed_sections": 0}

    # 이 파일의 테이블명 (TEAM.md에서는 TEAM 자체 코드 유지)
    table_name = md_path.stem

    while i < total:
        line = lines[i]
        stripped = line.strip()

        # ── 코드값 / 고유값 섹션 시작 ──
        if stripped.startswith("## 코드값") or stripped.startswith("## 코드값 / 고유값"):
            in_code_section = True
            in_sample_section = False
            result.append(line)
            i += 1
            # 직후 빈 줄이나 > 블럭쿼트 유지
            while i < total:
                sl = lines[i].strip()
                if sl.startswith(">") or sl == "":
                    result.append(lines[i])
                    i += 1
                else:
                    break
            continue

        # ── 샘플 데이터 섹션 시작 ──
        if stripped.startswith("## 샘플 데이터"):
            in_code_section = False
            in_sample_section = True
            sample_rows = 0
            result.append(line)
            i += 1
            continue

        # ── 다른 ## 섹션이 오면 코드/샘플 모두 종료 ──
        if stripped.startswith("## ") and not stripped.startswith("## 코드값") and not stripped.startswith("## 샘플"):
            in_code_section = False
            in_sample_section = False
            result.append(line)
            i += 1
            continue

        # ── 코드값 섹션 내부 처리 ──
        if in_code_section:
            # ### `COLUMN_NAME` 감지
            col_match = re.match(r"^###\s+`?(\w+)`?", stripped)
            if col_match:
                # 이전 컬럼 테이블 플러시
                if current_col and code_table_rows:
                    flush_code_table(result, current_col, code_table_rows, table_name, stats)
                    code_table_rows = []

                current_col = col_match.group(1)
                code_table_rows = []
                i += 1
                continue

            # 테이블 행 수집
            if stripped.startswith("|"):
                code_table_rows.append(line)
                i += 1
                continue

            # 빈 줄
            if stripped == "":
                if current_col and code_table_rows:
                    flush_code_table(result, current_col, code_table_rows, table_name, stats)
                    code_table_rows = []
                    current_col = None
                result.append(line)
                i += 1
                continue

            # > 블럭쿼트 (EUC-KR 참고 등)
            if stripped.startswith(">"):
                if current_col and code_table_rows:
                    flush_code_table(result, current_col, code_table_rows, table_name, stats)
                    code_table_rows = []
                    current_col = None
                result.append(line)
                i += 1
                continue

            result.append(line)
            i += 1
            continue

        # ── 샘플 데이터 섹션 내부 처리 ──
        if in_sample_section:
            if stripped.startswith("|"):
                sample_rows += 1
                if sample_rows <= 12:  # 헤더 + 구분선 + 10행
                    result.append(line)
                # 나머지 스킵
                i += 1
                continue
            else:
                result.append(line)
                i += 1
                continue

        # ── 일반 행 ──
        result.append(line)
        i += 1

    # 마지막 코드 테이블 플러시
    if in_code_section and current_col and code_table_rows:
        flush_code_table(result, current_col, code_table_rows, table_name, stats)

    return "\n".join(result), stats


def flush_code_table(result, col_name, table_rows, table_name, stats):
    """코드 테이블을 정리하여 result에 추가"""

    # FK 컬럼 → 참조 한 줄
    if col_name in FK_COLUMNS:
        # TEAM.md 내부에서 T_ID는 자기 자신이므로 유지
        result.append(f"### `{col_name}`\n")
        result.append(get_fk_reference(col_name))
        result.append("")
        stats["removed_sections"] += 1
        return

    # 팀 FK (TEAM, T_ID) - TEAM.md가 아닌 곳에서만 제거
    if col_name in ("TEAM", "T_ID") and table_name not in ("TEAM",):
        result.append(f"### `{col_name}`\n")
        result.append("→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조")
        result.append("")
        stats["removed_sections"] += 1
        return

    # 연속값 → 범위 요약
    if col_name in CONTINUOUS_COLUMNS:
        result.append(f"### `{col_name}`\n")
        result.append("→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조")
        result.append("")
        stats["removed_sections"] += 1
        return

    # 데이터 행 파싱 (헤더/구분선 제외)
    data_rows = []
    header_rows = []
    for row in table_rows:
        stripped = row.strip()
        cols = [c.strip() for c in stripped.split("|")]
        if len(cols) < 3:
            continue
        val = cols[1]
        if val in ("값", "---", "") or re.match(r"^-+$", val):
            header_rows.append(row)
            continue
        data_rows.append(row)

    # 고카디널리티 체크 (파싱된 값들)
    values = []
    for row in data_rows:
        cols = [c.strip() for c in row.strip().split("|")]
        if len(cols) >= 2:
            values.append(cols[1].strip("`").strip())

    if is_high_cardinality_numeric(values):
        result.append(f"### `{col_name}`\n")
        result.append(f"→ 고유값 {len(data_rows)}종 이상 — 상세 분포는 `raw/column-metadata.json` 참조")
        result.append("")
        stats["removed_sections"] += 1
        return

    # 일반 코드값 → 상위 5행만 유지
    result.append(f"### `{col_name}`\n")
    for h in header_rows:
        result.append(h)

    kept = data_rows[:5]
    for row in kept:
        result.append(row)

    if len(data_rows) > 5:
        result.append("")
        result.append(f"> 외 {len(data_rows) - 5}건 — 전체 목록은 `raw/column-metadata.json` 참조")
        stats["compressed_sections"] += 1
    result.append("")


def main():
    domains = ["game", "stats", "realtime", "master"]
    total_before = 0
    total_after = 0
    file_count = 0

    for domain in domains:
        domain_dir = BASE / "dictionary" / domain
        if not domain_dir.exists():
            continue
        for md_file in sorted(domain_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue

            before = md_file.read_text(encoding="utf-8")
            before_lines = len(before.split("\n"))

            cleaned, stats = process_file(md_file)
            after_lines = len(cleaned.split("\n"))

            md_file.write_text(cleaned, encoding="utf-8")

            reduction = before_lines - after_lines
            pct = (reduction / before_lines * 100) if before_lines > 0 else 0
            total_before += before_lines
            total_after += after_lines
            file_count += 1

            if reduction > 0:
                print(f"  {md_file.name:<40s} {before_lines:>4d} → {after_lines:>4d}  ({-reduction:>+4d}, {pct:>4.0f}% 감소)  FK제거={stats['removed_sections']} 압축={stats['compressed_sections']}")

    total_reduction = total_before - total_after
    pct = (total_reduction / total_before * 100) if total_before > 0 else 0
    print(f"\n  합계: {file_count}개 파일  {total_before} → {total_after} 줄  ({-total_reduction:+d}, {pct:.0f}% 감소)")


if __name__ == "__main__":
    main()
