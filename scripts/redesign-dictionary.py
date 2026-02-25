#!/usr/bin/env python3
"""Dictionary 상세 페이지 리디자인 스크립트

기존 enriched .md 파일에서 메타데이터를 읽고,
raw/column-metadata.json에서 컬럼/코드/샘플 데이터를 읽어
새로운 HTML 템플릿으로 재생성합니다.
"""

import json, re, os, html
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DOCS = BASE / "docs"
META_PATH = BASE / "raw" / "column-metadata.json"

DOMAIN_MAP = {
    "game": "경기 기록",
    "stats": "통계",
    "realtime": "실시간",
    "master": "마스터",
}

# ── 표준명 매핑 (generate-dictionary.py 에서 가져옴) ──
COLUMN_DESCRIPTIONS = {
    'GMKEY': ('경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)', 'game_id'),
    'G_ID': ('경기 ID (YYYYMMDDVVHH# 형식)', 'game_id'),
    'GDAY': ('경기 일자 (YYYYMMDD)', 'game_dt'),
    'GYEAR': ('시즌 연도 (4자리, "9999"=통산)', 'season_yr'),
    'PCODE': ('선수 코드 (5~6자리 숫자 문자열)', 'player_id'),
    'P_ID': ('선수 ID (정수)', 'player_id'),
    'LE_ID': ('리그 ID (1=1군)', 'league_id'),
    'SR_ID': ('시리즈 ID (0=정규시즌)', 'series_id'),
    'SEASON_ID': ('시즌 ID (연도)', 'season_id'),
    'T_ID': ('팀 코드 (2자리)', 'team_id'),
    'SEQ_NO': ('순번', 'seq_no'),
    'SEQ': ('순번', 'seq_no'),
    'SERNO': ('일련번호', 'serial_no'),
    'TB': ('팀 구분 (T=원정/Top, B=홈/Bottom)', 'top_bottom_cd'),
    'TB_SC': ('팀 구분 코드 (T=원정, B=홈)', 'top_bottom_cd'),
    'INN': ('이닝 번호', 'inn_no'),
    'INN_NO': ('이닝 번호', 'inn_no'),
    'INN2': ('이닝 세부 (아웃수 환산 또는 연장 구분)', 'inn_detail_no'),
    'OCOUNT': ('아웃 카운트 (0,1,2,4=이닝종료)', 'out_cn'),
    'HOW': ('플레이 결과 코드 (H1=안타, HR=홈런, KK=삼진 등 49종)', 'how_cd'),
    'PLACE': ('타구 방향 (0~9=포지션번호, S=삼진 등)', 'place_cd'),
    'POSI': ('포지션 코드 (XY: X=교체순번, Y=포지션)', 'position_cd'),
    'AB': ('타수 (At Bat)', 'ab'),
    'PA': ('타석 (Plate Appearance)', 'pa'),
    'HIT': ('안타', 'hit'),
    'Hit': ('안타', 'hit'),
    'H2': ('2루타', 'h2b'),
    'H3': ('3루타', 'h3b'),
    'HR': ('홈런', 'hr'),
    'RBI': ('타점', 'rbi'),
    'RUN': ('득점', 'run'),
    'Run': ('득점', 'run'),
    'BB': ('볼넷', 'bb'),
    'HP': ('사구 (Hit by Pitch)', 'hbp'),
    'IB': ('고의사구 (Intentional BB)', 'ibb'),
    'KK': ('삼진', 'so'),
    'GD': ('병살타', 'gidp'),
    'SB': ('도루', 'sb'),
    'CS': ('도루실패', 'cs'),
    'SF': ('희생플라이', 'sf'),
    'SH': ('희생번트', 'sh'),
    'ERR': ('실책', 'err'),
    'LOB': ('잔루', 'lob'),
    'HRA': ('타율', 'avg'),
    'W': ('승', 'win_cn'),
    'L': ('패', 'lose_cn'),
    'SV': ('세이브', 'save_cn'),
    'HOLD': ('홀드', 'hold_cn'),
    'ERA': ('평균자책점', 'era'),
    'ER': ('자책점', 'er'),
    'R': ('실점', 'r'),
    'BF': ('상대타자수', 'bf'),
    'NP': ('투구수', 'np'),
    'CG': ('완투', 'cg'),
    'SHO': ('완봉', 'sho'),
    'WLS': ('승패세 (W=승, L=패, S=세이브)', 'wls_cd'),
    'BK': ('보크', 'bk'),
    'WP': ('폭투', 'wp'),
    'TEAM': ('팀 코드 (2자리, HH=키움, HT=KIA 등)', 'team_cd'),
    'NAME': ('선수명 (varchar=EUC-KR 깨짐 가능)', 'player_nm'),
    'LEAGUE': ('리그', 'league_nm'),
    'RANK': ('순위', 'rank_no'),
    'GAME': ('경기 수', 'game_cn'),
    'GAMENUM': ('경기 수', 'game_cn'),
    'WIN': ('승', 'win_cn'),
    'LOSE': ('패', 'lose_cn'),
    'SAME': ('무승부', 'draw_cn'),
    'WRA': ('승률', 'win_rt'),
    'SEC': ('구간 (시즌연도 또는 "9999"=통산)', 'series_cd'),
    'TURN': ('타순', 'turn_no'),
    'ONETURN': ('타순 (1~9)', 'one_turn_if'),
    'START': ('선발 여부', 'start_if'),
    'QUIT': ('종료 여부', 'quit_if'),
    'INPUTTIME': ('입력 시각', 'input_tm'),
    'REG_DT': ('등록 일시', 'reg_dt'),
    'gameID': ('경기 ID (GMKEY와 동일 형식)', 'game_id'),
    'GAMEID': ('경기 ID', 'game_id'),
    'SeqNO': ('순번', 'seq_no'),
    'BatOrder': ('타순', 'bat_order_no'),
    'PlayerID': ('선수 코드', 'player_id'),
    'bHome': ('홈팀 여부', 'home_if'),
    'inning': ('이닝', 'inn_no'),
    'STATUS_ID': ('경기 상태 코드', 'status_cd'),
    'LIVETEXT': ('실시간 문자 중계 텍스트', 'live_text_nm'),
    'HOME': ('홈팀 코드', 'home_team_cd'),
    'VISIT': ('원정팀 코드', 'away_team_cd'),
    'HSCORE': ('홈팀 점수', 'home_score_cn'),
    'VSCORE': ('원정팀 점수', 'away_score_cn'),
    'STADIUM': ('구장', 'stadium_nm'),
    'SNAME': ('구장명', 'stadium_nm'),
    'ENDYN': ('종료 여부', 'end_if'),
    'CANCLE': ('취소 여부', 'cancel_if'),
    'DHEADER': ('더블헤더 번호', 'doubleheader_no'),
    'SUSPENDED': ('서스펜디드 여부', 'suspended_if'),
    'GMONTH': ('경기 월', 'game_month_no'),
    'GTIME': ('경기 시간', 'game_tm'),
    'Week': ('요일', 'game_week_nm'),
    'attendance': ('관중수', 'crowd_cn'),
    'game_flag': ('경기 유형 플래그', 'game_flag_cd'),
    'BROADCAST1': ('방송사1', 'broadcast1_nm'),
    'BROADCAST2': ('방송사2', 'broadcast2_nm'),
    'broadcast3': ('방송사3', 'broadcast3_nm'),
    'broadcast4': ('방송사4', 'broadcast4_nm'),
    'stadium': ('구장 코드', 'stadium_cd'),
    'gyear': ('연도', 'season_yr'),
    'gmkey': ('경기 고유키', 'game_id'),
    'gamedate': ('경기 일자', 'game_dt'),
    'BIRTH': ('생년월일', 'birth_dt'),
    'HEIGHT': ('키', 'height_va'),
    'WEIGHT': ('몸무게', 'weight_va'),
    'CAREER': ('경력', 'career_nm'),
    'HAND': ('투타 (좌/우)', 'hand_cd'),
    'HITTYPE': ('타석 방향', 'bat_throw_cd'),
    'POSITION': ('포지션', 'position_nm'),
    'INDATE': ('입단일', 'join_dt'),
    'NUM': ('등번호', 'back_no'),
    'CONT': ('연속 기록', 'continue_cn'),
    'CONTINUE': ('연속 기록', 'continue_cn'),
    'continue': ('연속 기록', 'continue_cn'),
    'RESULT': ('결과', 'result_cd'),
    'BESSION': ('세션', 'session_cd'),
    'DBHD': ('더블헤더 번호 (0=일반, 1=1차, 2=2차)', 'doubleheader_no'),
    'STAD': ('구장 코드', 'stadium_cd'),
    'UMPC': ('주심 이름', 'umpire_chief_nm'),
    'UMP1': ('1루심 이름', 'umpire_1b_nm'),
    'UMP2': ('2루심 이름', 'umpire_2b_nm'),
    'UMP3': ('3루심 이름', 'umpire_3b_nm'),
    'UMPL': ('좌측 외야심 이름', 'umpire_lf_nm'),
    'UMPR': ('우측 외야심 이름', 'umpire_rf_nm'),
    'SCOA': ('기록원 A 이름', 'scorer_a_nm'),
    'SCOB': ('기록원 B 이름', 'scorer_b_nm'),
    'TEMP': ('기온 (×10, 예: 270=27.0℃)', 'temperature_va'),
    'MOIS': ('습도 (%)', 'humidity_va'),
    'WEATH': ('날씨 코드 (F=맑음, C=흐림, R=비)', 'weather_cd'),
    'WIND': ('풍향 (16방위)', 'wind_dir_cd'),
    'WINS': ('풍속 (m/s)', 'wind_speed_va'),
    'GWEEK': ('요일 (EUC-KR 인코딩)', 'game_week_nm'),
    'CROWD': ('관중수', 'crowd_cn'),
    'CHAJUN': ('차전 (라운드 번호)', 'round_no'),
    'STTM': ('경기 시작 시각 (HHMM)', 'start_tm'),
    'ENTM': ('경기 종료 시각 (HHMM)', 'end_tm'),
    'DLTM': ('지연 시간 (분)', 'delay_tm'),
    'GMTM': ('경기 소요 시간 (분)', 'game_duration_tm'),
    'POS': ('포지션 코드', 'position_cd'),
    'BACKNUM': ('등번호', 'back_no'),
    'ENGNAME': ('영문 이름', 'player_eng_nm'),
    'CNAME': ('한자 이름', 'player_hanja_nm'),
    'PROMISE': ('계약금', 'signing_bonus_va'),
    'MONEY': ('연봉', 'salary_va'),
    'DRAFT': ('드래프트 정보', 'draft_nm'),
    'Error': ('실책', 'err'),
    'BallFour': ('볼넷 여부', 'ball_four_if'),
    'TB_stat': ('루타 (Total Bases) — 안타로 획득한 총 루수', 'tb_cn'),
}


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
        elif key == "스키마 세대":
            meta["schema_gen"] = val
        elif key == "데이터 티어":
            meta["tier"] = val
        elif key == "데이터 오너":
            meta["owner"] = val
        elif key == "갱신 주기":
            meta["refresh"] = val
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
    # 노트: > **관련 테이블**: ... 또는 EUC-KR 참고 등
    # 메타테이블과 ## 컬럼 상세 사이에 있는 > 블록 추출
    meta_end = text.find("## 컬럼 상세")
    if meta_end > 0:
        between = text[:meta_end]
        # 메타 테이블 이후의 > 블록
        lines = between.split("\n")
        in_note = False
        note_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("> **관련 테이블"):
                in_note = True
                note_lines.append(stripped[2:])  # > 제거
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

    # 코드값 섹션에서 참조 링크 파싱 (→ 선수 식별자 등)
    code_refs = {}
    for cm in re.finditer(r"### `(\w+)`\s*\n\s*\n\s*→\s*(.+)", text):
        col_name = cm.group(1)
        ref_text = cm.group(2).strip()
        code_refs[col_name] = ref_text
    meta["code_refs"] = code_refs

    return meta


def get_col_desc_and_std(col_name, data_type):
    """컬럼 설명 + 표준명 반환"""
    if col_name in COLUMN_DESCRIPTIONS:
        desc, std = COLUMN_DESCRIPTIONS[col_name]
        return desc, std

    # TB 특수 처리
    if col_name == 'TB' and data_type == 'int':
        return '루타 (Total Bases) — 안타로 획득한 총 루수', 'tb_cn'

    # 이닝 점수 컬럼
    for prefix in ('T', 'B'):
        for i in range(1, 26):
            if col_name == f'{prefix}{i}':
                side = '원정' if prefix == 'T' else '홈'
                sfx = 'away' if prefix == 'T' else 'home'
                return f'{i}회 {side}팀 점수', f'inn{i}_{sfx}_sc'

    # 접미사 기반
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


def generate_detail_page(table_name, domain_key, domain_label, raw_meta, enriched):
    """HTML 템플릿 기반 상세 페이지 생성"""
    lines = []

    # Frontmatter
    lines.append("---")
    lines.append(f"title: {table_name}")
    lines.append("---")
    lines.append("")
    lines.append('<div class="dict-detail-page" markdown>')
    lines.append("")

    # ── 히어로 헤더 ──
    tier_raw = enriched.get("tier", "")
    tier_short = re.sub(r"\s*[—\-].*", "", tier_raw).strip()
    tier_class = "tier-1" if "1" in tier_short else "tier-2" if "2" in tier_short else "tier-3"

    gen = enriched.get("schema_gen", raw_meta.get("schema_generation", "unknown"))
    gen_class = f"gen-{gen}"
    gen_label = {"legacy": "구세대", "new": "신세대"}.get(gen, "미분류")

    access = enriched.get("access", "Internal")

    # 테이블 설명 라인 구성
    pk_str = ", ".join(raw_meta.get("pk_columns", []))
    db_name = enriched.get("db", raw_meta.get("representative_db", ""))
    db_short = re.sub(r"_\d{6}$", "", db_name)  # 날짜 접미사 제거

    lines.append('<div class="dict-hero">')
    lines.append('  <div class="dict-hero-badges">')
    lines.append(f'    <span class="dict-badge badge-domain">{esc(domain_label)}</span>')
    if tier_short:
        lines.append(f'    <span class="dict-badge badge-tier {tier_class}">{esc(tier_short)}</span>')
    lines.append(f'    <span class="dict-badge badge-gen {gen_class}">{esc(gen_label)}</span>')
    lines.append(f'    <span class="dict-badge badge-access">{esc(access)}</span>')
    lines.append('  </div>')
    lines.append(f'  <div class="dict-hero-title">{esc(table_name)}</div>')
    lines.append(f'  <div class="dict-hero-sub">{esc(db_short)} &middot; PK: {esc(pk_str)}</div>')
    lines.append('</div>')
    lines.append("")

    # ── 퀵 스탯 ──
    row_count = raw_meta.get("row_count", 0)
    col_count = raw_meta.get("column_count", len(raw_meta.get("columns", [])))
    refresh = enriched.get("refresh", "")
    refresh_short = re.sub(r"\s*\(.*?\)", "", refresh).strip()
    owner = enriched.get("owner", "")
    owner_short = re.sub(r"\s*\(.*?\)", "", owner).strip()

    lines.append('<div class="dict-quick-stats">')
    lines.append(f'  <div class="dict-qs"><div class="dict-qs-val">{row_count:,}</div><div class="dict-qs-label">행 수</div></div>')
    lines.append(f'  <div class="dict-qs"><div class="dict-qs-val">{col_count}</div><div class="dict-qs-label">컬럼</div></div>')
    if refresh_short:
        lines.append(f'  <div class="dict-qs"><div class="dict-qs-val">{esc(refresh_short)}</div><div class="dict-qs-label">갱신 주기</div></div>')
    if owner_short:
        lines.append(f'  <div class="dict-qs"><div class="dict-qs-val">{esc(owner_short)}</div><div class="dict-qs-label">오너</div></div>')
    lines.append('</div>')
    lines.append("")

    # ── 메타 정보 그리드 ──
    lines.append('<div class="dict-info-grid">')

    def info_item(label, value, full=False):
        cls = ' class="dict-info-item full"' if full else ' class="dict-info-item"'
        lines.append(f'  <div{cls}><span class="dict-info-label">{esc(label)}</span><span class="dict-info-value">{value}</span></div>')

    info_item("대표 DB", f'<code>{esc(db_name)}</code>')
    info_item("PK", f'<code>{esc(pk_str)}</code>')
    info_item("스키마 세대", f'{esc(gen)} ({esc(gen_label)})')
    info_item("데이터 티어", esc(tier_raw) if tier_raw else "-")
    info_item("데이터 오너", esc(owner) if owner else "-")
    info_item("갱신 주기", esc(refresh) if refresh else "-")

    consumers = enriched.get("consumers", "")
    if consumers:
        info_item("소비자", esc(consumers))

    access_val = enriched.get("access", "")
    if access_val:
        info_item("접근 수준", esc(access_val))

    product = enriched.get("product", "")
    if product:
        info_item("데이터 프로덕트", product, full=True)  # already has markdown links

    standards = enriched.get("standards", "")
    if standards:
        info_item("관련 표준", standards, full=True)

    lines.append('</div>')
    lines.append("")

    # ── 관련 테이블 노트 ──
    for note in enriched.get("notes", []):
        lines.append(f'<div class="dict-note">')
        lines.append(note)
        lines.append('</div>')
        lines.append("")

    # ── 컬럼 상세 ──
    columns = raw_meta.get("columns", [])
    lines.append(f'<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">{len(columns)}개</span></div>')
    lines.append("")

    # EUC-KR 경고
    euckr = enriched.get("euckr_warn", "")
    if euckr:
        lines.append(f'<div class="dict-encoding-warn">{esc(euckr)}</div>')
        lines.append("")

    lines.append('<div style="overflow-x:auto">')
    lines.append('<table class="dict-col-table"><thead>')
    lines.append('<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>')
    lines.append('</thead><tbody>')

    for col in columns:
        name = col["name"]
        dtype = col.get("data_type", "")
        ml = col.get("max_length", "")
        nullable = col.get("is_nullable", False)
        is_pk = col.get("is_pk", False)
        ordinal = col.get("ordinal", "")

        desc, std_name = get_col_desc_and_std(name, dtype)
        type_str = format_type(dtype, ml)

        null_html = "" if not nullable else ""
        null_html = '<span class="nn-mark">NN</span>' if not nullable else ""
        pk_html = '<span class="pk-badge">PK</span>' if is_pk else ""

        lines.append(f'<tr>'
                     f'<td class="col-num">{ordinal}</td>'
                     f'<td><span class="col-name">{esc(name)}</span></td>'
                     f'<td><span class="col-std">{esc(std_name)}</span></td>'
                     f'<td><span class="col-type">{esc(type_str)}</span></td>'
                     f'<td>{null_html}</td>'
                     f'<td>{pk_html}</td>'
                     f'<td><span class="col-desc">{esc(desc)}</span></td>'
                     f'</tr>')

    lines.append('</tbody></table>')
    lines.append('</div>')
    lines.append("")

    # ── 코드값 / 고유값 ──
    code_cols = [c for c in columns if c.get("distinct_values")]
    code_refs = enriched.get("code_refs", {})

    # 참조만 있는 컬럼도 포함
    has_any_code = bool(code_cols) or bool(code_refs)

    if has_any_code:
        total_code_cols = len(set(
            [c["name"] for c in code_cols] + list(code_refs.keys())
        ))
        lines.append(f'<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">{total_code_cols}개 컬럼</span></div>')
        lines.append("")
        lines.append('<div class="dict-codes-section">')

        # 이미 처리한 컬럼 추적
        processed = set()

        for col in columns:
            name = col["name"]
            dv = col.get("distinct_values")
            ref = code_refs.get(name)

            if not dv and not ref:
                continue
            processed.add(name)

            desc, _ = get_col_desc_and_std(name, col.get("data_type", ""))
            desc_short = desc.split("(")[0].strip() if desc else ""

            open_attr = ""
            # 코드값이 있고 20개 이하면 기본 열기
            if dv and len(dv) <= 10:
                open_attr = " open"

            lines.append(f'<details class="dict-code-group"{open_attr}>')
            lines.append(f'<summary><code>{esc(name)}</code><span class="code-desc"> — {esc(desc_short)}</span></summary>')

            if ref:
                lines.append(f'<div class="code-ref">{ref}</div>')
            elif dv:
                lines.append('<div class="code-body">')
                lines.append('<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>')
                shown = dv[:20]
                for d in shown:
                    v = d.get("value", "")
                    c = d.get("count", 0)
                    lines.append(f'<tr><td>{esc(str(v))}</td><td>{c:,}</td></tr>')
                lines.append('</tbody></table>')
                if len(dv) > 20:
                    lines.append(f'<div class="code-overflow-note">외 {len(dv) - 20}건 — 전체 목록은 raw/column-metadata.json 참조</div>')
                lines.append('</div>')

            lines.append('</details>')

        # 코드 참조만 있는 컬럼 (distinct_values 없는)
        for name, ref in code_refs.items():
            if name in processed:
                continue
            desc, _ = get_col_desc_and_std(name, "")
            desc_short = desc.split("(")[0].strip() if desc else ""
            lines.append(f'<details class="dict-code-group">')
            lines.append(f'<summary><code>{esc(name)}</code><span class="code-desc"> — {esc(desc_short)}</span></summary>')
            lines.append(f'<div class="code-ref">{ref}</div>')
            lines.append('</details>')

        lines.append('</div>')
        lines.append("")

    # ── 샘플 데이터 ──
    sample_cols = [c for c in columns if c.get("sample_values")]
    if sample_cols:
        lines.append(f'<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>')
        lines.append("")
        lines.append('<div class="dict-sample-section">')
        lines.append('<table class="dict-sample-table"><thead>')
        lines.append('<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>')
        lines.append('</thead><tbody>')

        for col in sample_cols:
            name = col["name"]
            samples = col["sample_values"][:3]
            cells = []
            for i in range(3):
                if i < len(samples):
                    v = str(samples[i])
                    cells.append(f'<td>{esc(v)}</td>')
                else:
                    cells.append('<td><span class="dict-sample-null">NULL</span></td>')
            lines.append(f'<tr><td>{esc(name)}</td>{"".join(cells)}</tr>')

        lines.append('</tbody></table>')
        lines.append('</div>')
        lines.append("")

    lines.append('</div>')
    lines.append("")

    return "\n".join(lines)


def main():
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
    for domain_key, domain_label in DOMAIN_MAP.items():
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

            # 새 페이지 생성
            content = generate_detail_page(
                table_name, domain_key, domain_label, raw_meta, enriched
            )

            md_file.write_text(content, encoding="utf-8")
            total += 1
            print(f"  {domain_key}/{table_name}.md ✓")

    print(f"\n완료: {total}개 테이블 상세 페이지 리디자인")


if __name__ == "__main__":
    main()
