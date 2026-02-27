#!/usr/bin/env python3
"""dictionary/{domain}/{table}.md HTML 생성 스크립트 (파이프라인 #5)

.enriched-cache.json에서 메타데이터를 읽고,
raw/column-metadata.json에서 컬럼/코드/샘플 데이터를 읽어
Jinja2 템플릿으로 dictionary 상세 페이지를 생성합니다.
"""

import json, re, html
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from config import DOMAIN_LABELS, COLUMN_DESC, STANDARD_MAP, TABLE_OVERRIDES

BASE = Path(__file__).resolve().parent.parent
DOCS = BASE / "docs"
META_PATH = BASE / "raw" / "column-metadata.json"
TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"


def _init_jinja():
    """Jinja2 Environment 초기화"""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    return env.get_template("detail-page.html.j2")


def esc(s):
    """HTML 이스케이프"""
    return html.escape(str(s)) if s else ""


def parse_enriched_md(md_path):
    """기존 enriched .md 파일에서 메타 + 노트 파싱"""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    meta = {}

    # 메타 테이블 파싱
    for m in re.finditer(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|", text, re.MULTILINE):
        key = m.group(1).strip()
        val = m.group(2).strip()
        if key == "대표 DB":
            meta["db"] = val.strip("`")
        elif key == "행 수":
            meta["row_count"] = val
        elif key == "컬럼 수":
            meta["column_count"] = val
        elif key == "PK":
            meta["pk"] = val.strip("`")
        elif key == "데이터 티어":
            meta["tier"] = val
        elif key == "데이터 오너":
            meta["owner"] = val
        elif key == "소비자":
            meta["consumers"] = val
        elif key == "데이터 프로덕트":
            meta["product"] = val
        elif key == "접근 수준":
            meta["access"] = val
        elif key == "관련 표준":
            meta["standards"] = val

    # 최종수정 라인
    hm = re.search(r"최종수정:\s*(\S+)\s*\|\s*버전:\s*(\S+)", text)
    if hm:
        meta["last_modified"] = hm.group(1)
        meta["version"] = hm.group(2)

    # 관련 테이블 노트 (> 로 시작하는 블록, 메타테이블 바로 뒤)
    notes = []
    meta_end = text.find("## 컬럼 상세")
    if meta_end > 0:
        between = text[:meta_end]
        lines = between.split("\n")
        in_note = False
        note_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("> **관련 테이블"):
                in_note = True
                note_lines.append(stripped[2:])
            elif in_note and stripped.startswith(">"):
                note_lines.append(stripped[2:] if len(stripped) > 2 else "")
            elif in_note:
                in_note = False
                if note_lines:
                    notes.append("\n".join(note_lines))
                    note_lines = []
        if note_lines:
            notes.append("\n".join(note_lines))

    meta["notes"] = notes

    # EUC-KR 경고
    euckr_match = re.search(r">\s*\*\*EUC-KR 참고\*\*:\s*(.+?)(?:\n(?!>)|\Z)", text, re.DOTALL)
    if euckr_match:
        meta["euckr_warn"] = euckr_match.group(1).strip()

    # 코드값 섹션에서 참조 링크 파싱
    code_refs = {}
    for cm in re.finditer(r"### `(\w+)`\s*\n\s*\n\s*→\s*(.+)", text):
        col_name = cm.group(1)
        ref_text = cm.group(2).strip()
        code_refs[col_name] = ref_text
    meta["code_refs"] = code_refs

    return meta


def get_col_desc_and_std(col_name, data_type, table_name=''):
    """컬럼 설명 + 표준명 반환 (TABLE_OVERRIDES 우선)"""
    override_key = (table_name, col_name)
    if override_key in TABLE_OVERRIDES:
        return TABLE_OVERRIDES[override_key]

    if col_name in COLUMN_DESC:
        return COLUMN_DESC[col_name], STANDARD_MAP.get(col_name, '')

    for prefix in ('T', 'B'):
        for i in range(1, 26):
            if col_name == f'{prefix}{i}':
                side = '원정' if prefix == 'T' else '홈'
                sfx = 'away' if prefix == 'T' else 'home'
                return f'{i}회 {side}팀 점수', f'inn{i}_{sfx}_sc'

    suffixes = {
        '_CN': ('건수', '_cn'), '_RT': ('비율', '_rt'), '_IF': ('여부 (Y/N)', '_if'),
        '_SC': ('상태코드', '_sc'), '_CD': ('코드', '_cd'), '_VA': ('값', '_va'),
        '_ME': ('메모', '_nm'), '_NM': ('명칭', '_nm'), '_DT': ('일시', '_dt'),
        '_TM': ('시각', '_tm'), '_NO': ('번호', '_no'),
    }
    upper = col_name.upper()
    for sfx, (label, std_sfx) in suffixes.items():
        if upper.endswith(sfx):
            base = col_name[:-len(sfx)]
            return f'{base} {label}', col_name.lower()

    return '', ''


def format_type(data_type, max_length):
    """타입 포맷"""
    dt = data_type.strip().lower()
    ml = str(max_length).strip()
    no_len_types = ('int', 'bigint', 'smallint', 'tinyint', 'bit', 'float',
                    'real', 'datetime', 'datetime2', 'date', 'time')
    if dt in no_len_types or not ml or ml in ('0', '-1', 'None', ''):
        if ml == '-1':
            return f"{dt}(max)"
        return dt
    return f"{dt}({ml})"


def _build_context(table_name, domain_key, domain_label, raw_meta, enriched):
    """Jinja2 템플릿용 context dict 생성"""
    # 히어로 헤더
    tier_raw = enriched.get("tier", "")
    tier_short = re.sub(r"\s*-.*", "", tier_raw).strip()
    tier_class = "tier-1" if "1" in tier_short else "tier-2" if "2" in tier_short else "tier-3"

    access = enriched.get("access", "Internal")
    pk_str = ", ".join(raw_meta.get("pk_columns", []))
    db_name = enriched.get("db", raw_meta.get("representative_db", ""))
    db_short = re.sub(r"_\d{6}$", "", db_name)

    # 퀵 스탯
    row_count = raw_meta.get("row_count", 0)
    col_count = raw_meta.get("column_count", len(raw_meta.get("columns", [])))
    owner = enriched.get("owner", "")
    owner_short = re.sub(r"\s*\(.*?\)", "", owner).strip()

    # 컬럼 상세
    columns_raw = raw_meta.get("columns", [])
    columns = []
    for col in columns_raw:
        name = col["name"]
        dtype = col.get("data_type", "")
        ml = col.get("max_length", "")
        nullable = col.get("is_nullable", False)
        is_pk = col.get("is_pk", False)
        ordinal = col.get("ordinal", "")

        desc, std_name = get_col_desc_and_std(name, dtype, table_name)
        type_str = format_type(dtype, ml)
        null_html = '<span class="nn-mark">NN</span>' if not nullable else ""
        pk_html = '<span class="pk-badge">PK</span>' if is_pk else ""

        columns.append({
            "ordinal": ordinal,
            "name": esc(name),
            "std_name": esc(std_name),
            "type_str": esc(type_str),
            "null_html": null_html,
            "pk_html": pk_html,
            "desc": esc(desc),
        })

    # 코드값 / 고유값
    code_cols = [c for c in columns_raw if c.get("distinct_values")]
    code_refs = enriched.get("code_refs", {})
    code_entries = []
    processed = set()

    for col in columns_raw:
        name = col["name"]
        dv = col.get("distinct_values")
        ref = code_refs.get(name)
        if not dv and not ref:
            continue
        processed.add(name)

        desc, _ = get_col_desc_and_std(name, col.get("data_type", ""), table_name)
        desc_short = esc(desc.split("(")[0].strip() if desc else "")

        values = None
        if not ref and dv:
            values = [{"value": esc(str(d.get("value", ""))),
                        "count_fmt": f'{d.get("count", 0):,}'} for d in dv]

        code_entries.append({
            "name": esc(name),
            "desc_short": desc_short,
            "open": bool(dv and len(dv) <= 10),
            "ref": ref,
            "code_values": values,
        })

    for name, ref in code_refs.items():
        if name in processed:
            continue
        desc, _ = get_col_desc_and_std(name, "", table_name)
        desc_short = esc(desc.split("(")[0].strip() if desc else "")
        code_entries.append({
            "name": esc(name),
            "desc_short": desc_short,
            "open": False,
            "ref": ref,
            "code_values": None,
        })

    total_code_cols = len(set(
        [c["name"] for c in code_cols] + list(code_refs.keys())
    ))

    # 샘플 데이터
    sample_cols = []
    for col in columns_raw:
        if not col.get("sample_values"):
            continue
        samples = col["sample_values"][:3]
        cells = []
        for i in range(3):
            if i < len(samples):
                cells.append(f'<td>{esc(str(samples[i]))}</td>')
            else:
                cells.append('<td><span class="dict-sample-null">NULL</span></td>')
        sample_cols.append({"name": esc(col["name"]), "cells": cells})

    return {
        "table_name": esc(table_name),
        "domain_label": esc(domain_label),
        "tier_short": esc(tier_short),
        "tier_class": tier_class,
        "tier_raw": esc(tier_raw) if tier_raw else "",
        "access": esc(access),
        "access_val": esc(enriched.get("access", "")),
        "pk_str": esc(pk_str),
        "db_name": esc(db_name),
        "db_short": esc(db_short),
        "row_count_fmt": f"{row_count:,}",
        "col_count": col_count,
        "owner": esc(owner),
        "owner_short": esc(owner_short),
        "consumers": esc(enriched.get("consumers", "")),
        "product": enriched.get("product", ""),
        "standards": enriched.get("standards", ""),
        "notes": enriched.get("notes", []),
        "euckr_warn": esc(enriched.get("euckr_warn", "")),
        "columns": columns,
        "code_entries": code_entries,
        "total_code_cols": total_code_cols,
        "sample_cols": sample_cols,
    }


def main():
    template = _init_jinja()

    # raw 메타데이터 로드
    with open(META_PATH, encoding="utf-8") as f:
        raw_data = json.load(f)["tables"]

    # enriched 캐시 로드 (있으면)
    cache_path = BASE / "dictionary" / ".enriched-cache.json"
    enriched_cache = {}
    if cache_path.exists():
        with open(cache_path, encoding="utf-8") as f:
            enriched_cache = json.load(f)
        print(f"enriched 캐시 로드: {len(enriched_cache)}개")

    total = 0
    for domain_key, domain_label in DOMAIN_LABELS.items():
        domain_dir = DOCS / "dictionary" / domain_key
        if not domain_dir.exists():
            continue

        for md_file in sorted(domain_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue

            table_name = md_file.stem

            # raw 데이터
            raw_meta = raw_data.get(table_name, {})
            if not raw_meta:
                for k, v in raw_data.items():
                    if k.lower() == table_name.lower():
                        raw_meta = v
                        break

            if not raw_meta:
                print(f"  SKIP: {table_name} (not in column-metadata.json)")
                continue

            # enriched 데이터: 캐시 우선, 없으면 현재 .md 파싱
            if table_name in enriched_cache:
                enriched = enriched_cache[table_name]
            else:
                enriched = parse_enriched_md(md_file)

            # context 생성 + 템플릿 렌더링
            ctx = _build_context(
                table_name, domain_key, domain_label, raw_meta, enriched
            )
            content = template.render(ctx)

            md_file.write_text(content, encoding="utf-8")
            total += 1
            print(f"  {domain_key}/{table_name}.md ✓")

    print(f"\n완료: {total}개 테이블 상세 페이지 생성")


if __name__ == "__main__":
    main()
