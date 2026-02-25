#!/usr/bin/env python3
"""dictionary/*.md + raw/column-metadata.json + glossary/business-terms.md →
   assets/data/catalog-columns.json, assets/data/glossary-terms.json,
   assets/data/catalog-instances.json

AG Grid 카탈로그 데이터 생성 스크립트
"""

import json, os, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

DOMAIN_MAP = {
    "game": "경기 기록",
    "stats": "통계",
    "realtime": "실시간",
    "master": "마스터",
}

# ── 1. column-metadata.json 로드 ─────────────────────────────
def load_column_metadata():
    p = BASE / "raw" / "column-metadata.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f)["tables"]

# ── 2. dictionary/index.md 에서 table_std_name 파싱 ──────────
def parse_index_std_names():
    """index.md 테이블에서 테이블명 → 표준명(안) 매핑"""
    p = BASE / "dictionary" / "index.md"
    mapping = {}
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            if len(cols) < 5:
                continue
            # cols[0] is empty (before first |)
            # cols[2] = 테이블명 (contains [name](link))
            # cols[3] = 표준명(안)
            table_cell = cols[2]
            std_cell = cols[3]
            m = re.search(r"\[([^\]]+)\]", table_cell)
            if m and std_cell and std_cell not in ("표준명(안)", "---", "--------"):
                tname = m.group(1)
                mapping[tname] = std_cell
    return mapping

# ── 2b. dictionary/index.md 에서 설명 파싱 ────────────────────
def parse_index_descriptions():
    """index.md 테이블에서 테이블명 → 설명 매핑"""
    p = BASE / "dictionary" / "index.md"
    mapping = {}
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            if len(cols) < 12:
                continue
            table_cell = cols[2]
            desc_cell = cols[11]
            m = re.search(r"\[([^\]]+)\]", table_cell)
            if m and desc_cell and desc_cell not in ("설명", "---", "--------"):
                tname = m.group(1)
                mapping[tname] = desc_cell
    return mapping

# ── 3. dictionary/{domain}/{table}.md 파싱 ────────────────────
def parse_dictionary_md(md_path):
    """단일 dictionary md 파일에서 메타 + 컬럼 상세 파싱"""
    meta = {}
    columns = []
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    # 메타 테이블 (| 항목 | 값 | 형태)
    for m in re.finditer(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|", text, re.MULTILINE):
        key = m.group(1).strip()
        val = m.group(2).strip()
        if key == "데이터 티어":
            # "Tier 1 — Critical" → "Tier 1"
            meta["tier"] = re.sub(r"\s*[—\-].*", "", val)
        elif key == "데이터 오너":
            # "기록위원회 (R-03)" → "기록위원회"
            meta["owner"] = re.sub(r"\s*\(.*?\)", "", val)
        elif key == "갱신 주기":
            # "경기 당일 (S2i 전송)" → "경기 당일"
            meta["refresh"] = re.sub(r"\s*\(.*?\)", "", val)
        elif key == "접근 수준":
            meta["access"] = val
        elif key == "스키마 세대":
            meta["schema_gen"] = val
        elif key == "행 수":
            meta["row_count"] = int(re.sub(r"[,\s]", "", val))
        elif key == "대표 DB":
            meta["representative_db"] = val.strip("`")

    # 컬럼 상세 테이블
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
            # 헤더 행 스킵
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
            col_name = cols[2].strip("`").strip()
            data_type = cols[3].strip()
            max_length = cols[4].strip()
            nullable = cols[5].strip()
            pk = cols[6].strip()
            description = cols[7].strip() if len(cols) > 7 else ""
            std_name = cols[8].strip() if len(cols) > 8 else ""
            # 표준명에서 backtick 제거
            std_name = std_name.strip("`")

            columns.append({
                "ordinal": ordinal,
                "column_name": col_name,
                "data_type": data_type,
                "max_length": max_length,
                "is_nullable": nullable,
                "is_pk": pk,
                "description": description,
                "std_name": std_name,
            })
        elif in_column_table and stripped.startswith("##") and "컬럼 상세" not in stripped:
            break  # 다음 섹션

    return meta, columns

# ── 4. 컬럼 카탈로그 JSON 생성 ────────────────────────────────
def build_catalog_columns():
    col_meta = load_column_metadata()
    std_names = parse_index_std_names()
    rows = []

    for domain_key, domain_label in DOMAIN_MAP.items():
        domain_dir = BASE / "dictionary" / domain_key
        if not domain_dir.exists():
            continue
        for md_file in sorted(domain_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue
            table_name = md_file.stem
            meta, columns = parse_dictionary_md(md_file)

            # column-metadata.json 에서 보충
            cm = col_meta.get(table_name, {})
            row_count = meta.get("row_count", cm.get("row_count", 0))
            schema_gen = meta.get("schema_gen", cm.get("schema_generation", "unknown"))

            table_std_name = std_names.get(table_name, "")
            table_doc_url = f"dictionary/{domain_key}/{table_name}/"

            # columns 가 비어있으면 column-metadata.json 에서 가져오기
            if not columns and table_name in col_meta:
                for c in cm.get("columns", []):
                    columns.append({
                        "ordinal": c.get("ordinal", 0),
                        "column_name": c.get("name", ""),
                        "data_type": c.get("data_type", ""),
                        "max_length": str(c.get("max_length", "")),
                        "is_nullable": "" if c.get("is_nullable") else "NN",
                        "is_pk": "PK" if c.get("is_pk") else "",
                        "description": "",
                        "std_name": "",
                    })

            for col in columns:
                rows.append({
                    "domain": domain_label,
                    "domain_key": domain_key,
                    "table_name": table_name,
                    "table_std_name": table_std_name,
                    "column_name": col["column_name"],
                    "ordinal": col["ordinal"],
                    "data_type": col["data_type"],
                    "max_length": col["max_length"],
                    "is_nullable": col["is_nullable"],
                    "is_pk": col["is_pk"],
                    "description": col["description"],
                    "std_name": col["std_name"],
                    "tier": meta.get("tier", ""),
                    "owner": meta.get("owner", ""),
                    "refresh": meta.get("refresh", ""),
                    "access": meta.get("access", ""),
                    "schema_gen": schema_gen,
                    "row_count": row_count,
                    "table_doc_url": table_doc_url,
                })

    return rows

# ── 5. 용어 사전 JSON 생성 ────────────────────────────────────
def build_glossary_terms():
    p = BASE / "glossary" / "business-terms.md"
    with open(p, encoding="utf-8") as f:
        text = f.read()

    rows = []
    current_category = ""

    # 섹션 구분: ## N. or ### N.N
    for line in text.split("\n"):
        stripped = line.strip()

        # 카테고리 감지
        hm = re.match(r"^#{2,3}\s+[\d.]+\s+(.+)", stripped)
        if hm:
            current_category = hm.group(1).strip()
            continue

        # 부록/색인 헤딩 이후 중단
        if stripped.startswith("#") and ("부록" in stripped or "색인" in stripped):
            break

        if not stripped.startswith("|"):
            continue

        cols = [c.strip() for c in stripped.split("|")]
        # 최소 cols 수 확인 (빈 첫/끝 포함)
        if len(cols) < 4:
            continue

        # 헤더/구분선 스킵
        if cols[1] in ("용어", "---", "") or re.match(r"^-+$", cols[1]):
            continue

        term_ko = cols[1] if len(cols) > 1 else ""
        if not term_ko or term_ko.startswith("--"):
            continue

        # 섹션마다 헤더가 다름
        # 2.1~2.4: 용어 | 영문 | 약어 | 정의 | DB 컬럼 | 관련 테이블
        # 3.1~3.3, 5, 6: 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블
        # 3.2: 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블
        # 4: 용어 | 코드명 | 정의 | 값 예시 | DB 컬럼
        # 7: 용어 | 정의

        # 6컬럼 이상 = 약어 있는 형태 (2.1~2.4)
        if len(cols) >= 8 and current_category and any(
            k in current_category for k in ["타격", "투수", "수비", "비율", "세이버"]
        ):
            term_en = cols[2]
            abbreviation = cols[3]
            definition = cols[4]
            db_column = cols[5]
            related_tables = cols[6] if len(cols) > 6 else ""
        elif len(cols) >= 7 and "코드" in current_category:
            # 코드 체계: 용어 | 코드명 | 정의 | 값 예시 | DB 컬럼
            term_en = cols[2]  # 코드명
            abbreviation = ""
            definition = cols[3]
            db_column = cols[5] if len(cols) > 5 else ""
            related_tables = ""
        elif len(cols) >= 4 and "품질" in current_category:
            # 7. 데이터 품질: 용어 | 정의
            term_en = ""
            abbreviation = ""
            definition = cols[2]
            db_column = ""
            related_tables = ""
        elif len(cols) >= 7:
            # 3.x, 5, 6: 용어 | 영문 | 정의 | DB 컬럼 | 관련 테이블
            term_en = cols[2]
            abbreviation = ""
            definition = cols[3]
            db_column = cols[4]
            related_tables = cols[5] if len(cols) > 5 else ""
        else:
            continue

        rows.append({
            "category": current_category,
            "term_ko": term_ko,
            "term_en": term_en,
            "abbreviation": abbreviation,
            "definition": definition,
            "db_column": db_column,
            "related_tables": related_tables,
        })

    return rows

# ── 6. 인스턴스 매트릭스 JSON 생성 ────────────────────────────
LEAGUE_MAP = {
    "DB1_BASEBALL_220328":          "KBO",
    "DB1_BASEBALL_2_220328":        "KBO",
    "DB2_BASEBALL_220328":          "KBO",
    "DB2_BASEBALL_2_220328":        "KBO",
    "DB2_BASEBALL_NEW_220328":      "KBO",
    "DB1_MINOR_BASEBALL_220328":    "마이너",
    "DB1_MINOR_SO_BASEBALL":        "마이너",
    "DB2_MINOR_BASEBALL_220328":    "마이너",
    "DB2_MINOR_BASEBALL_NEW_220328":"마이너",
    "DB2_MINOR_SO_BASEBALL":        "마이너",
    "DB2_MINOR_SO_BASEBALL_NEW":    "마이너",
    "DB2_POSTSEASON":               "포스트시즌",
    "DB2_MINOR_POSTSEASON":         "포스트시즌",
    "DB2_EXHIBITION":               "시범경기",
    "DB2_ALLSTAR":                  "올스타",
    "DB2_INTERNATIONAL":            "국제대회",
    "DB2_OTHER_GAME":               "기타",
}

SYSTEM_TABLE_PREFIXES = (
    "MSpeer_", "MSpub_", "sysdiagrams", "dtproperties", "oauth2_",
    "sysarticle", "syspub", "sysrepl", "sysschema", "syssub", "systran",
)

def build_catalog_instances():
    """mssql-inventory.json + dictionary 메타 → 인스턴스 매트릭스 JSON"""
    # 1) mssql-inventory.json 로드
    inv_path = BASE / "raw" / "mssql-inventory.json"
    with open(inv_path, encoding="utf-8") as f:
        inventory = json.load(f)

    # 2) column-metadata.json 로드 (schema_generation)
    col_meta = load_column_metadata()

    # 3) dictionary 파일 목록 → table_name→(domain, meta) 매핑
    #    exact match (person vs PERSON), case-insensitive fallback
    dict_exact = {}   # table_name → {domain_key, domain, meta, doc_url}
    dict_ci = {}      # table_name.lower() → {domain_key, domain, meta, doc_url}

    for domain_key, domain_label in DOMAIN_MAP.items():
        domain_dir = BASE / "dictionary" / domain_key
        if not domain_dir.exists():
            continue
        for md_file in sorted(domain_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue
            tname = md_file.stem
            meta, _ = parse_dictionary_md(md_file)
            entry = {
                "domain_key": domain_key,
                "domain": domain_label,
                "meta": meta,
                "doc_url": f"dictionary/{domain_key}/{tname}/",
            }
            dict_exact[tname] = entry
            # case-insensitive: person.md와 PERSON.md 모두 등록하되
            # exact match 우선이므로 ci는 보조용
            dict_ci[tname.lower()] = entry

    # 4) index.md 에서 tier/owner 파싱 (보조)
    index_meta = parse_index_meta()

    # 5) index.md 에서 표준명(안), 설명 파싱
    std_names = parse_index_std_names()
    idx_descs = parse_index_descriptions()

    # 6) 인스턴스 행 생성
    rows = []
    for db in inventory["databases"]:
        db_name = db["db_name"]
        db_type = db["db_type"]
        league = LEAGUE_MAP.get(db_name, "기타")

        for tbl in db["tables"]:
            table_name = tbl["table_name"]

            # 시스템 테이블 필터
            if any(table_name.startswith(p) for p in SYSTEM_TABLE_PREFIXES):
                continue

            column_count = tbl.get("column_count", 0)
            row_count = tbl.get("row_count", 0)

            # dictionary 매핑: exact → ci fallback
            dentry = dict_exact.get(table_name)
            if not dentry:
                dentry = dict_ci.get(table_name.lower())

            if dentry:
                domain = dentry["domain"]
                table_doc_url = dentry["doc_url"]
                meta = dentry["meta"]
                tier = meta.get("tier", "")
                owner = meta.get("owner", "")
                refresh = meta.get("refresh", "")
                access = meta.get("access", "")
            else:
                domain = ""
                table_doc_url = ""
                tier = ""
                owner = ""
                refresh = ""
                access = ""

            # index.md 보조 (dictionary md에 없으면)
            idx = index_meta.get(table_name) or index_meta.get(table_name.lower(), {})
            if not tier and idx:
                tier = idx.get("tier", "")
            if not owner and idx:
                owner = idx.get("owner", "")

            # schema_generation (column-metadata.json)
            cm = col_meta.get(table_name, {})
            if not cm:
                # case-insensitive fallback
                for k, v in col_meta.items():
                    if k.lower() == table_name.lower():
                        cm = v
                        break
            schema_gen = cm.get("schema_generation", "")

            # pk_columns (column-metadata.json)
            pk_cols = cm.get("pk_columns", [])
            pk_columns = ", ".join(pk_cols) if pk_cols else ""

            # table_std_name, description (index.md)
            table_std_name = std_names.get(table_name, "")
            if not table_std_name:
                # case-insensitive fallback
                for k, v in std_names.items():
                    if k.lower() == table_name.lower():
                        table_std_name = v
                        break
            description = idx_descs.get(table_name, "")
            if not description:
                for k, v in idx_descs.items():
                    if k.lower() == table_name.lower():
                        description = v
                        break

            # table_name_ci (case-insensitive 그룹 키)
            table_name_ci = table_name.lower()

            rows.append({
                "db_name": db_name,
                "db_type": db_type,
                "league": league,
                "table_name": table_name,
                "table_name_ci": table_name_ci,
                "table_std_name": table_std_name,
                "domain": domain,
                "column_count": column_count,
                "row_count": row_count,
                "tier": tier,
                "owner": owner,
                "schema_gen": schema_gen,
                "pk_columns": pk_columns,
                "refresh": refresh,
                "access": access,
                "description": description,
                "table_doc_url": table_doc_url,
            })

    return rows

def parse_index_meta():
    """index.md 테이블에서 테이블명 → {tier, owner} 매핑 (보조용)"""
    p = BASE / "dictionary" / "index.md"
    mapping = {}
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            if len(cols) < 10:
                continue
            table_cell = cols[2]
            m = re.search(r"\[([^\]]+)\]", table_cell)
            if not m:
                continue
            tname = m.group(1)
            # cols 순서: # | 테이블명 | 표준명(안) | 컬럼 수 | 행 수 | PK | 세대 | 티어 | 오너 | 갱신 주기 | 설명
            tier = cols[8].strip() if len(cols) > 8 else ""
            owner = cols[9].strip() if len(cols) > 9 else ""
            if tier and tier not in ("티어", "---", "--------"):
                mapping[tname] = {"tier": tier, "owner": owner}
                mapping[tname.lower()] = {"tier": tier, "owner": owner}
    return mapping

# ── 7. 딕셔너리 테이블 요약 JSON 생성 ─────────────────────────
def build_dictionary_tables():
    """39종 테이블 요약 JSON 생성 (Dictionary AG Grid용)"""
    col_meta = load_column_metadata()
    std_names = parse_index_std_names()
    idx_descs = parse_index_descriptions()

    rows = []
    for domain_key, domain_label in DOMAIN_MAP.items():
        domain_dir = BASE / "dictionary" / domain_key
        if not domain_dir.exists():
            continue
        for md_file in sorted(domain_dir.glob("*.md")):
            if md_file.name in ("README.md", "index.md"):
                continue
            table_name = md_file.stem
            meta, columns = parse_dictionary_md(md_file)

            # column-metadata.json 보충
            cm = col_meta.get(table_name, {})
            if not cm:
                for k, v in col_meta.items():
                    if k.lower() == table_name.lower():
                        cm = v
                        break

            row_count = meta.get("row_count", cm.get("row_count", 0))
            schema_gen = meta.get("schema_gen", cm.get("schema_generation", "unknown"))
            pk_cols = cm.get("pk_columns", [])
            pk_columns = ", ".join(pk_cols) if pk_cols else ""

            table_std_name = std_names.get(table_name, "")
            if not table_std_name:
                for k, v in std_names.items():
                    if k.lower() == table_name.lower():
                        table_std_name = v
                        break
            description = idx_descs.get(table_name, "")
            if not description:
                for k, v in idx_descs.items():
                    if k.lower() == table_name.lower():
                        description = v
                        break

            column_count = len(columns) if columns else cm.get("column_count", 0)

            # 컬럼 요약 (사이드패널용)
            col_summary = []
            for c in columns[:50]:
                col_summary.append({
                    "name": c["column_name"],
                    "type": c["data_type"],
                    "pk": c["is_pk"],
                    "desc": c["description"],
                })

            rows.append({
                "domain": domain_label,
                "domain_key": domain_key,
                "table_name": table_name,
                "table_std_name": table_std_name,
                "column_count": column_count,
                "row_count": row_count,
                "pk_columns": pk_columns,
                "schema_gen": schema_gen,
                "tier": meta.get("tier", ""),
                "owner": meta.get("owner", ""),
                "refresh": meta.get("refresh", ""),
                "description": description,
                "table_doc_url": f"dictionary/{domain_key}/{table_name}/",
                "columns": col_summary,
            })

    return rows

# ── main ──────────────────────────────────────────────────────
def main():
    out_dir = BASE / "assets" / "data"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 컬럼 카탈로그
    cat_rows = build_catalog_columns()
    cat_path = out_dir / "catalog-columns.json"
    with open(cat_path, "w", encoding="utf-8") as f:
        json.dump({"generated": "2026-02-25", "rows": cat_rows}, f, ensure_ascii=False, indent=2)
    print(f"catalog-columns.json: {len(cat_rows)} rows")

    # 용어 사전
    glo_rows = build_glossary_terms()
    glo_path = out_dir / "glossary-terms.json"
    with open(glo_path, "w", encoding="utf-8") as f:
        json.dump({"generated": "2026-02-25", "rows": glo_rows}, f, ensure_ascii=False, indent=2)
    print(f"glossary-terms.json: {len(glo_rows)} rows")

    # 인스턴스 매트릭스
    inst_rows = build_catalog_instances()
    inst_path = out_dir / "catalog-instances.json"
    with open(inst_path, "w", encoding="utf-8") as f:
        json.dump({"generated": "2026-02-25", "rows": inst_rows}, f, ensure_ascii=False, indent=2)
    print(f"catalog-instances.json: {len(inst_rows)} rows")

    # 딕셔너리 테이블 요약
    dict_rows = build_dictionary_tables()
    dict_path = out_dir / "dictionary-tables.json"
    with open(dict_path, "w", encoding="utf-8") as f:
        json.dump({"generated": "2026-02-25", "rows": dict_rows}, f, ensure_ascii=False, indent=2)
    print(f"dictionary-tables.json: {len(dict_rows)} rows")

if __name__ == "__main__":
    main()
