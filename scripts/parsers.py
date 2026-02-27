#!/usr/bin/env python3
"""scripts/parsers.py - dictionary .md 파싱 공통 모듈

dictionary/{domain}/{table}.md 파일을 HTML/Markdown 양립 파싱하고,
column-metadata.json + config.py 기반 폴백 컬럼 목록을 생성한다.
"""

import re
from config import COLUMN_DESC, STANDARD_MAP, TABLE_OVERRIDES


# ── HTML 파싱 ──────────────────────────────────────────────────

def _parse_meta_html(text):
    """HTML dict-info-grid에서 메타 파싱"""
    meta = {}
    META_KEYS = {
        "데이터 티어": ("tier", lambda v: re.sub(r"\s*-.*", "", v)),
        "데이터 오너": ("owner", lambda v: re.sub(r"\s*\(.*?\)", "", v)),
        "접근 수준": ("access", lambda v: v),
        "대표 DB": ("representative_db", lambda v: v),
    }
    for m in re.finditer(
        r'<span class="dict-info-label">([^<]+)</span>'
        r'<span class="dict-info-value">(.*?)</span></div>',
        text,
    ):
        label = m.group(1).strip()
        raw_val = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if label in META_KEYS:
            key, fn = META_KEYS[label]
            meta[key] = fn(raw_val)

    qs = re.search(
        r'<div class="dict-qs-val">([0-9,]+)</div>'
        r'<div class="dict-qs-label">행 수</div>',
        text,
    )
    if qs:
        meta["row_count"] = int(qs.group(1).replace(",", ""))

    return meta


def _parse_columns_html(text):
    """HTML dict-col-table에서 컬럼 파싱"""
    columns = []
    for m in re.finditer(
        r'<tr>'
        r'<td[^>]*>(\d+)</td>'
        r'<td><span class="col-name">([^<]*)</span></td>'
        r'<td><span class="col-std">([^<]*)</span></td>'
        r'<td><span class="col-type">([^<]*)</span></td>'
        r'<td>(.*?)</td>'
        r'<td>(.*?)</td>'
        r'<td><span class="col-desc">([^<]*)</span></td>'
        r'</tr>',
        text,
    ):
        nullable_raw = m.group(5)
        pk_raw = m.group(6)
        columns.append({
            "ordinal": int(m.group(1)),
            "column_name": m.group(2).strip(),
            "std_name": m.group(3).strip(),
            "data_type": m.group(4).strip(),
            "max_length": "",
            "is_nullable": "" if "NN" in nullable_raw else "Y",
            "is_pk": "PK" if "PK" in pk_raw else "",
            "description": m.group(7).strip(),
        })
    return columns


# ── Markdown 파싱 ──────────────────────────────────────────────

def _parse_meta_markdown(text):
    """레거시 Markdown 파이프 테이블에서 메타 파싱"""
    meta = {}
    for m in re.finditer(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|", text, re.MULTILINE):
        key = m.group(1).strip()
        val = m.group(2).strip()
        if key == "데이터 티어":
            meta["tier"] = re.sub(r"\s*-.*", "", val)
        elif key == "데이터 오너":
            meta["owner"] = re.sub(r"\s*\(.*?\)", "", val)
        elif key == "접근 수준":
            meta["access"] = val
        elif key == "행 수":
            meta["row_count"] = int(re.sub(r"[,\s]", "", val))
        elif key == "대표 DB":
            meta["representative_db"] = val.strip("`")
    return meta


def _parse_columns_markdown(text):
    """레거시 Markdown 파이프 테이블에서 컬럼 파싱"""
    columns = []
    in_column_table = False
    header_found = False
    for line in text.split("\n"):
        stripped = line.strip()
        if "## 컬럼 상세" in stripped:
            in_column_table = True
            continue
        if in_column_table and stripped.startswith("|"):
            cols = [c.strip() for c in stripped.split("|")]
            if len(cols) < 9:
                continue
            if cols[1] in ("#", "---", ""):
                if cols[1] == "#":
                    header_found = True
                continue
            if re.match(r"^-+$", cols[1]):
                continue
            if not header_found:
                continue
            try:
                ordinal = int(cols[1])
            except (ValueError, IndexError):
                continue
            columns.append({
                "ordinal": ordinal,
                "column_name": cols[2].strip("`").strip(),
                "data_type": cols[3].strip(),
                "max_length": cols[4].strip(),
                "is_nullable": cols[5].strip(),
                "is_pk": cols[6].strip(),
                "description": cols[7].strip() if len(cols) > 7 else "",
                "std_name": cols[8].strip().strip("`") if len(cols) > 8 else "",
            })
        elif in_column_table and stripped.startswith("##") and "컬럼 상세" not in stripped:
            break
    return columns


# ── 공개 API ──────────────────────────────────────────────────

def parse_dictionary_md(md_path):
    """단일 dictionary md 파일에서 메타 + 컬럼 상세 파싱 (HTML/Markdown 양립)"""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    is_html = "dict-detail-page" in text

    if is_html:
        meta = _parse_meta_html(text)
        columns = _parse_columns_html(text)
    else:
        meta = _parse_meta_markdown(text)
        columns = _parse_columns_markdown(text)

    return meta, columns


def columns_from_metadata(table_name, cm):
    """dictionary HTML 파싱 실패 시 column-metadata.json + config.py 폴백"""
    columns = []
    for c in cm.get("columns", []):
        cn = c.get("name", "")
        override = TABLE_OVERRIDES.get((table_name, cn))
        if override:
            desc, std = override
        else:
            desc = COLUMN_DESC.get(cn, "")
            std = STANDARD_MAP.get(cn, "")
        columns.append({
            "ordinal": c.get("ordinal", 0),
            "column_name": cn,
            "data_type": c.get("data_type", ""),
            "max_length": str(c.get("max_length", "")),
            "is_nullable": "Y" if c.get("is_nullable") else "",
            "is_pk": "PK" if c.get("is_pk") else "",
            "description": desc,
            "std_name": std,
        })
    return columns
