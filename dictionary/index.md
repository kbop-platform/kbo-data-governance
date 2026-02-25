---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

<!-- Stats Cards -->
<div class="grid-stats">
  <div class="stat-card">
    <div class="stat-value" id="stat-tables">39</div>
    <div class="stat-label">테이블</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-columns">787</div>
    <div class="stat-label">컬럼</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-total-rows">25.7M</div>
    <div class="stat-label">총 행수</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-domains">4</div>
    <div class="stat-label">도메인</div>
  </div>
</div>

<!-- Filter Bar -->
<div class="grid-filter-bar">
  <input type="text" id="grid-search" class="filter-search" placeholder="검색... (Ctrl+F)">
  <div class="filter-group">
    <label class="filter-label" for="sel-domain">도메인</label>
    <select id="sel-domain" data-field="domain"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-schema_gen">세대</label>
    <select id="sel-schema_gen" data-field="schema_gen"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-tier">티어</label>
    <select id="sel-tier" data-field="tier"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-owner">오너</label>
    <select id="sel-owner" data-field="owner"><option value="">전체</option></select>
  </div>
  <button id="btn-reset" class="btn-reset">초기화</button>
</div>

<!-- Filter Chips -->
<div class="grid-chips" id="filter-chips"></div>

<!-- AG Grid -->
<div id="dictionary-grid" class="ag-theme-alpine ag-theme-kbo" style="height:60vh;width:100%"></div>

<!-- Status Bar -->
<div class="grid-status">
  <div class="status-left">
    <span id="status-count">39건 표시</span>
  </div>
  <div>
    <button id="btn-csv" class="btn-csv">CSV 다운로드</button>
    <span style="margin-left:8px;font-size:11px;color:#aaa">2026-02-25 갱신</span>
  </div>
</div>

---

<details class="dict-reference" markdown>
<summary>데이터 흐름도</summary>

```
┌─────────────────┐     경기 당일 전송      ┌──────────────────┐
│  S2i 운영 DB     │ ──────────────────────→ │  DB2 (시즌 13개)  │
│  (Sports2i 외주) │                         │  시즌별 경기 데이터 │
└─────────────────┘                         └────────┬─────────┘
                                                     │ 확정 후 반영
                                                     ▼
                                             ┌──────────────────┐
                                             │  DB1 (영구 4개)    │
                                             │  누적/마스터 데이터 │
                                             └──────────────────┘

┌─────────────────┐     KBO 자체 구축       ┌──────────────────┐
│  KBO 분석팀      │ ──────────────────────→ │  KBO 자체 DB      │
│  (내부)          │                         │  세이버/P-b-P 등   │
└─────────────────┘                         └──────────────────┘
```

- **DB2**: 경기 당일 S2i가 전송. 시즌 데이터
- **DB1**: DB2 확정 후 반영. 영구/누적
- **KBO 자체**: 세이버메트릭스, pitch-by-pitch 등 S2i 미제공 데이터

</details>

<details class="dict-reference" markdown>
<summary>테이블 간 주요 관계</summary>

**핵심 FK 관계**

```
GAME_INFO (game_id)
  ├── HITTER         (game_id, season_yr, player_id)
  ├── PITCHER         (game_id, season_yr, player_id)
  ├── SCORE           (game_id, season_yr, top_bottom_cd)
  ├── GAME_CONT_APP   (game_id, season_yr, seq_no)
  ├── ENTRY           (game_id, season_yr, turn_no, player_id, position_cd)
  ├── DEFEN           (game_id, season_yr)
  ├── GAME_HR         (game_id)
  └── GAME_MEMO       (game_id)

PERSON (player_id)
  ├── HITTER         (player_id)
  ├── PITCHER         (player_id)
  ├── ENTRY           (player_id)
  ├── BAT_TOTAL       (player_id)
  └── PIT_TOTAL       (player_id)

TEAM (team_id, season_id)
  ├── TEAM_RANK       (team_cd, season_yr)
  └── GAME_INFO       (home_team_cd, away_team_cd)
```

**실시간 테이블 관계**

실시간(IE_*) 테이블은 독립적으로 운영되며, `gameID`(=game_id)로 경기 기록 도메인과 연결.

```
IE_LIVE_TEXT (gameID) ← 실시간 문자 중계
IE_BALL_COUNT (gameID) ← 볼카운트 현재 상태
IE_BATTER_RECORD (gameID, PlayerID) ← 타자 누적
IE_PITCHER_RECORD (gameID, PlayerID) ← 투수 누적
IE_GAME_STATE (GAMEID) ← 경기 상태
IE_SCORE_RHEB (gameID) ← R/H/E/B 요약
IE_SCORE_INNING (gameID) ← 이닝 점수
IE_GAME_LIST (gameID) ← 당일 경기 목록
IE_LOG ← 시스템 로그 (FK 없음)
```

</details>

<details class="dict-reference" markdown>
<summary>스키마 세대 분포</summary>

| 세대 | 식별 패턴 | 테이블 수 | 주요 특징 |
|------|----------|----------|----------|
| **구세대 (legacy)** | GMKEY/PCODE, camelCase·PascalCase 혼용 | 24종 | 1982년~ 축적 데이터. `varchar` 한글, `float` 비율 |
| **신세대 (new)** | G_ID/P_ID, `_CD`·`_CN`·`_SC` 접미사 | 6종 | 2022년~ 추가. `nvarchar`, 정수 ID |
| **미분류 (unknown)** | 양쪽 패턴 혼합 또는 판별 불가 | 9종 | IE_* 실시간 등. S2i 확인 필요 |

**구세대 → 신세대 전환 우선순위**:

1. GAME_INFO, HITTER, PITCHER — 핵심 경기 기록 (가장 많이 조회)
2. BAT_TOTAL, PIT_TOTAL — 통계 조회 빈도 높음
3. ENTRY, DEFEN, SCORE — 경기 부속 기록
4. IE_* — 실시간 테이블은 API/WebSocket 전환 시 함께

</details>

<details class="dict-reference" markdown>
<summary>참고 문서</summary>

- [데이터 프로덕트](products/game-summary.md) — 비즈니스 단위별 데이터 구조
- [데이터 리니지](lineage.md) — 데이터 흐름 추적, 영향도 분석
- [표준 명명 규칙](../standards/naming-rules.md) — 레거시→표준 변환 규칙
- [ID 체계](../standards/id-system.md) — game_id, player_id 등 6종 ID 정의
- [도메인 타입](../standards/domain-types.md) — 접미사별 MSSQL 타입 매핑
- [코드 사전](../standards/code-dictionary.md) — how_cd, place_cd 등 코드값
- [업무 용어 사전](../glossary/business-terms.md) — 용어 정의 ~165개
- [컬럼 매핑](../migration/column-mapping.md) — AS-IS→TO-BE 컬럼 전수 매핑

</details>

</div>
