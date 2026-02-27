---
hide:
  - toc
---

<div class="lineage-page product-page" markdown>

<div class="product-hero">
  <div class="product-hero-badges">
    <span class="p-badge p-badge-product">거버넌스</span>
    <span class="p-badge">39 테이블</span>
    <span class="p-badge">4 도메인</span>
  </div>
  <div class="product-hero-title">데이터 리니지</div>
  <div class="product-hero-sub">Data Lineage</div>
  <div class="product-hero-desc">소스 시스템에서 소비자 시스템까지, 데이터가 어디서 오고 어디로 가는지를 시스템·테이블·컬럼 3단계로 추적한다.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">3</div><div class="product-stat-label">소스 시스템</div></div>
  <div class="product-stat"><div class="product-stat-val">DB1 + DB2</div><div class="product-stat-label">저장소</div></div>
  <div class="product-stat"><div class="product-stat-val">5단계</div><div class="product-stat-label">생명주기</div></div>
  <div class="product-stat"><div class="product-stat-val">6종</div><div class="product-stat-label">핵심 ID</div></div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- 1. 시스템 레벨 리니지                       -->
<!-- ══════════════════════════════════════════ -->
<div class="product-section">
  <div class="product-section-hdr"><h2>1. 시스템 레벨 리니지</h2></div>
  <p style="font-size:14px;color:#444;margin:0 0 12px">데이터가 시스템 간 어떻게 흐르는지를 나타낸다.</p>
  <div class="product-flow">

```mermaid
flowchart TB
    subgraph 외부["외부 시스템"]
        S2i[S2i 운영 시스템]
        KMA[기상청 API]
    end
    subgraph DB2["DB2 - 시즌 데이터 (13개)"]
        DB2_B["DB2_BASEBALL_YYYY"]
        DB2_M["DB2_MINOR_YYYY"]
        DB2_F["DB2_FUTURES_YYYY"]
    end
    subgraph DB1["DB1 - 영구 데이터 (4개)"]
        DB1_B[DB1_BASEBALL]
        DB1_MA[DB1_MASTER]
        DB1_MN[DB1_MINOR]
    end
    subgraph KBO자체["KBO 자체 구축"]
        SABER[세이버메트릭스]
        PBP[Pitch-by-Pitch]
    end
    subgraph 소비자["소비자 시스템"]
        API[REST API]
        WS[WebSocket]
        BI[통계 대시보드]
        APP[팬 서비스 앱]
    end
    S2i -->|"경기 당일 전송"| DB2_B
    S2i -->|"경기 당일 전송"| DB2_M
    S2i -->|"경기 당일 전송"| DB2_F
    KMA -->|"기상 데이터"| DB2_B
    DB2_B -->|"확정 후 반영"| DB1_B
    DB2_M -->|"확정 후 반영"| DB1_MN
    DB1_B --> SABER
    DB1_B --> PBP
    DB1_B --> API
    DB1_MA --> API
    DB2_B --> WS
    DB1_B --> BI
    API --> APP
    WS --> APP
```

  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- 2. 테이블 레벨 리니지                       -->
<!-- ══════════════════════════════════════════ -->
<div class="product-section">
  <div class="product-section-hdr"><h2>2. 테이블 레벨 리니지</h2></div>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:16px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">2.1 경기 기록</h2>
    <span class="product-section-count">12개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>소스</th><th>갱신</th><th>저장소</th><th>소비자</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="game/GAMEINFO/">GAMEINFO</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>방송팀, 기록팀, API</td></tr>
      <tr><td><span class="tbl-name"><a href="game/Hitter/">Hitter</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀, 통계팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/Pitcher/">Pitcher</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀, 통계팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/Score/">Score</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>방송팀, API</td></tr>
      <tr><td><span class="tbl-name"><a href="game/ENTRY/">ENTRY</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/GAMECONTAPP/">GAMECONTAPP</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀, 분석팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/DEFEN/">DEFEN</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/GAME_HR/">GAME_HR</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>미디어, API</td></tr>
      <tr><td><span class="tbl-name"><a href="game/GAME_MEMO/">GAME_MEMO</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/GAME_MEMO_PITCHCLOCK/">GAME_MEMO_PITCHCLOCK</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/PITCHCLOCK/">PITCHCLOCK</a></span></td><td>S2i</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀</td></tr>
      <tr><td><span class="tbl-name"><a href="game/GAMEINFO_WEATHER/">GAMEINFO_WEATHER</a></span></td><td>기상청 API</td><td>경기 당일</td><td>DB2</td><td>방송팀</td></tr>
    </tbody>
  </table>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:20px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">2.2 통계</h2>
    <span class="product-section-count">10개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>소스</th><th>갱신</th><th>저장소</th><th>소비자</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="stats/BatTotal/">BatTotal</a></span></td><td>경기 기록 집계</td><td>D+1</td><td>DB1</td><td>통계팀, API</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/PitTotal/">PitTotal</a></span></td><td>경기 기록 집계</td><td>D+1</td><td>DB1</td><td>통계팀, API</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/TeamRank/">TeamRank</a></span></td><td>경기 결과 집계</td><td>D+1</td><td>DB1</td><td>미디어, API</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/KBO_BATRESULT/">KBO_BATRESULT</a></span></td><td>경기별 이닝 집계</td><td>경기 당일</td><td>DB2 → DB1</td><td>분석팀</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/KBO_PITRESULT/">KBO_PITRESULT</a></span></td><td>경기별 투수 집계</td><td>경기 당일</td><td>DB2 → DB1</td><td>분석팀</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/KBO_ETCGAME/">KBO_ETCGAME</a></span></td><td>기타 이벤트</td><td>경기 당일</td><td>DB2 → DB1</td><td>기록팀</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/SEASON_PLAYER_HITTER/">SEASON_PLAYER_HITTER</a></span></td><td>시즌 집계</td><td>D+1</td><td>DB2</td><td>통계팀, API</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/SEASON_PLAYER_HITTER_SITUATION/">SEASON_PLAYER_HITTER_SITUATION</a></span></td><td>시즌 상황별</td><td>D+1</td><td>DB2</td><td>분석팀</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/SEASON_PLAYER_PITCHER/">SEASON_PLAYER_PITCHER</a></span></td><td>시즌 집계</td><td>D+1</td><td>DB2</td><td>통계팀, API</td></tr>
      <tr><td><span class="tbl-name"><a href="stats/SEASON_PLAYER_PITCHER_SITUATION/">SEASON_PLAYER_PITCHER_SITUATION</a></span></td><td>시즌 상황별</td><td>D+1</td><td>DB2</td><td>분석팀</td></tr>
    </tbody>
  </table>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:20px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">2.3 실시간</h2>
    <span class="product-section-count">9개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>소스</th><th>갱신</th><th>저장소</th><th>소비자</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="realtime/IE_LiveText/">IE_LiveText</a></span></td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td><span class="tbl-name"><a href="realtime/IE_BallCount/">IE_BallCount</a></span></td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td><span class="tbl-name"><a href="realtime/IE_BatterRecord/">IE_BatterRecord</a></span></td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td><span class="tbl-name"><a href="realtime/IE_PitcherRecord/">IE_PitcherRecord</a></span></td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td><span class="tbl-name"><a href="realtime/IE_GAMESTATE/">IE_GAMESTATE</a></span></td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td>IE_MatchPlayer</td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td>IE_Lineup</td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td>IE_BatOrder</td><td>S2i 실시간</td><td>&lt;5초</td><td>DB2</td><td>방송팀, 앱, WebSocket</td></tr>
      <tr><td><span class="tbl-name"><a href="realtime/IE_log/">IE_log</a></span></td><td>시스템 자동</td><td>실시간</td><td>DB2</td><td>운영팀</td></tr>
    </tbody>
  </table>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:20px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">2.4 마스터</h2>
    <span class="product-section-count">8개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>소스</th><th>갱신</th><th>저장소</th><th>소비자</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="master/person/">person</a></span></td><td>KBO 기록팀</td><td>시즌 전</td><td>DB1</td><td>전 시스템</td></tr>
      <tr><td><span class="tbl-name"><a href="master/person2/">person2</a></span></td><td>KBO 기록팀</td><td>시즌 전</td><td>DB1</td><td>전 시스템</td></tr>
      <tr><td><span class="tbl-name"><a href="master/PERSON/">PERSON</a></span></td><td>KBO 기록팀</td><td>시즌 전</td><td>DB1</td><td>전 시스템</td></tr>
      <tr><td><span class="tbl-name"><a href="master/PERSON_FA/">PERSON_FA</a></span></td><td>KBO 기록팀</td><td>FA 발생 시</td><td>DB1</td><td>기록팀, 인사팀</td></tr>
      <tr><td><span class="tbl-name"><a href="master/TEAM/">TEAM</a></span></td><td>KBO 사무국</td><td>연 1회</td><td>DB1</td><td>전 시스템</td></tr>
      <tr><td><span class="tbl-name"><a href="master/STADIUM/">STADIUM</a></span></td><td>KBO 사무국</td><td>연 1회</td><td>DB1</td><td>전 시스템</td></tr>
      <tr><td><span class="tbl-name"><a href="master/KBO_schedule/">KBO_schedule</a></span></td><td>KBO 경기운영팀</td><td>시즌 전 일괄</td><td>DB1</td><td>전 시스템</td></tr>
      <tr><td><span class="tbl-name"><a href="master/CANCEL_GAME/">CANCEL_GAME</a></span></td><td>KBO 경기운영팀</td><td>발생 즉시</td><td>DB2</td><td>운영팀, 방송팀</td></tr>
    </tbody>
  </table>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- 3. 컬럼 레벨 리니지                         -->
<!-- ══════════════════════════════════════════ -->
<div class="product-section">
  <div class="product-section-hdr"><h2>3. 컬럼 레벨 리니지 - 핵심 식별자</h2></div>
  <p style="font-size:14px;color:#444;margin:0 0 12px">핵심 ID가 테이블 간 어떻게 참조되는지를 추적한다. → <a href="../standards/id-system/" style="color:#2563eb">ID 체계 문서</a></p>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:16px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">3.1 game_id (현행: GMKEY)</h2>
  </div>
  <div class="product-flow">

```mermaid
flowchart LR
    GI[GAMEINFO.GMKEY] --> H[Hitter.GMKEY]
    GI --> P[Pitcher.GMKEY]
    GI --> S[Score.GMKEY]
    GI --> E[ENTRY.GMKEY]
    GI --> GC[GAMECONTAPP.GMKEY]
    GI --> D[DEFEN.GMKEY]
    GI --> KB[KBO_BATRESULT.GMKEY]
    GI --> KP[KBO_PITRESULT.GMKEY]
    GI --> KE[KBO_ETCGAME.GMKEY]
    GI --> KS[KBO_schedule.gmkey]
    GI2["GAMEINFO.GMKEY ≈ IE_*.gameID"] -.-> IL[IE_LiveText.gameID]
    GI2 -.-> IB[IE_BallCount.gameID]
    GI2 -.-> IG[IE_GAMESTATE.GAMEID]
```

  </div>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:16px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">3.2 player_id (현행: PCODE)</h2>
  </div>
  <div class="product-flow">

```mermaid
flowchart LR
    PS[person.PCODE] --> H[Hitter.PCODE]
    PS --> P[Pitcher.PCODE]
    PS --> E[ENTRY.PCODE]
    PS --> BT[BatTotal.PCODE]
    PS --> PT[PitTotal.PCODE]
    PS --> KB[KBO_BATRESULT.PCODE]
    PS --> KP[KBO_PITRESULT.PCODE]
    PS2["person ≈ SEASON_PLAYER_*"] -.-> SH[SEASON_PLAYER_HITTER.P_ID]
    PS2 -.-> SP[SEASON_PLAYER_PITCHER.P_ID]
```

  </div>

  <div class="product-section-hdr" style="border-bottom:none;margin-top:16px;margin-bottom:8px;padding-bottom:0">
    <h2 style="font-size:15px">3.3 team_id (현행: TEAM.T_ID / VTEAM, HTEAM)</h2>
  </div>
  <div class="product-flow">

```mermaid
flowchart LR
    T[TEAM.T_ID] --> GI_V[GAMEINFO.VTEAM]
    T --> GI_H[GAMEINFO.HTEAM]
    T --> TR[TeamRank.TEAM]
    T --> H[Hitter.TB]
    T --> P[Pitcher.TB]
```

  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- 4. 데이터 생명주기                          -->
<!-- ══════════════════════════════════════════ -->
<div class="product-section">
  <div class="product-section-hdr"><h2>4. 데이터 생명주기</h2></div>
  <table class="product-table lifecycle-table">
    <thead><tr><th>단계</th><th>설명</th><th>상태</th></tr></thead>
    <tbody>
      <tr><td>1. 수집</td><td>S2i에서 경기 당일 DB2로 전송</td><td>DRAFT</td></tr>
      <tr><td>2. 검증</td><td>기록위원회 검토 (무결성, 정합성 확인)</td><td>REVIEW</td></tr>
      <tr><td>3. 확정</td><td>공식 기록으로 확정, DB1 반영</td><td>CONFIRMED</td></tr>
      <tr><td>4. 수정</td><td>확정 후 오류 발견 시 수정</td><td>REVISED</td></tr>
      <tr><td>5. 보존</td><td>영구 보존 (삭제 불가)</td><td>ARCHIVED</td></tr>
    </tbody>
  </table>
  <div class="lineage-note" style="margin-top:8px">
    → <a href="../governance/change-process/">변경 관리 절차</a> - 상태 전환 절차 &nbsp;|&nbsp;
    → <a href="../standards/code-dictionary/">코드 사전</a> - record_status_cd 정의
  </div>
</div>

<!-- ══════════════════════════════════════════ -->
<!-- 5. 영향도 분석                              -->
<!-- ══════════════════════════════════════════ -->
<div class="product-section">
  <div class="product-section-hdr"><h2>5. 영향도 분석 매트릭스</h2></div>
  <p style="font-size:14px;color:#444;margin:0 0 10px">특정 테이블 변경 시 영향을 받는 다른 테이블과 시스템을 정리한다.</p>
  <table class="product-table">
    <thead><tr><th>변경 테이블</th><th>영향받는 테이블</th><th>영향 시스템</th><th>영향도</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name">GAMEINFO</span></td><td>Hitter, Pitcher, Score, ENTRY, GAMECONTAPP, DEFEN, IE_*</td><td>방송, API, 통계</td><td><span class="impact-critical">Critical</span></td></tr>
      <tr><td><span class="tbl-name">person</span></td><td>Hitter, Pitcher, ENTRY, BatTotal, PitTotal, SEASON_PLAYER_*</td><td>전 시스템</td><td><span class="impact-critical">Critical</span></td></tr>
      <tr><td><span class="tbl-name">TEAM</span></td><td>GAMEINFO, TeamRank</td><td>전 시스템</td><td><span class="impact-high">High</span></td></tr>
      <tr><td><span class="tbl-name">STADIUM</span></td><td>GAMEINFO, KBO_schedule</td><td>운영, 방송</td><td><span class="impact-medium">Medium</span></td></tr>
      <tr><td><span class="tbl-name">BatTotal</span></td><td>(소비 전용)</td><td>통계, API</td><td><span class="impact-low">Low</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 관련 문서 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>관련 문서</h2></div>
  <div class="product-refs">
    <a class="product-ref" href="../standards/id-system/">
      <div class="product-ref-body">
        <div class="product-ref-title">ID 체계</div>
        <div class="product-ref-desc">game_id, player_id 등 6종 핵심 ID 정의</div>
      </div>
    </a>
    <a class="product-ref" href="../governance/change-process/">
      <div class="product-ref-body">
        <div class="product-ref-title">변경 관리 절차</div>
        <div class="product-ref-desc">DRAFT → CONFIRMED 상태 전환 절차</div>
      </div>
    </a>
    <a class="product-ref" href="../standards/code-dictionary/">
      <div class="product-ref-body">
        <div class="product-ref-title">코드 사전</div>
        <div class="product-ref-desc">record_status_cd, how_cd 등 코드값 정의</div>
      </div>
    </a>
  </div>
</div>

</div>
