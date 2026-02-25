---
hide:
  - toc
---

<div class="product-page" markdown>

<div class="product-hero">
  <div class="product-hero-badges">
    <span class="p-badge p-badge-product">데이터 프로덕트</span>
    <span class="p-badge p-badge-version">v1</span>
    <span class="p-badge p-badge-domain">실시간</span>
    <span class="p-badge p-badge-refresh">실시간 (&lt;5초)</span>
  </div>
  <div class="product-hero-title">실시간 경기</div>
  <div class="product-hero-sub">Live Game</div>
  <div class="product-hero-desc">진행 중인 경기의 실시간 상태를 소비자에게 전달한다. WebSocket/API를 통해 실시간 스코어, 볼카운트, 선수 기록을 제공.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">7</div><div class="product-stat-label">테이블</div></div>
  <div class="product-stat"><div class="product-stat-val">82</div><div class="product-stat-label">컬럼</div></div>
  <div class="product-stat"><div class="product-stat-val">&lt; 5초</div><div class="product-stat-label">지연 시간</div></div>
  <div class="product-stat"><div class="product-stat-val">Tier 1~2</div><div class="product-stat-label">데이터 티어</div></div>
</div>

<!-- ── 포함 테이블 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>포함 테이블</h2>
    <span class="product-section-count">7개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>역할</th><th>티어</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_LiveText/">IE_LiveText</a></span></td><td>실시간 문자 중계</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_BallCount/">IE_BallCount</a></span></td><td>현재 볼카운트 상태</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_GAMESTATE/">IE_GAMESTATE</a></span></td><td>경기 진행 상태</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_ScoreRHEB/">IE_ScoreRHEB</a></span></td><td>점수/안타/실책/볼넷 요약</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_Scoreinning/">IE_Scoreinning</a></span></td><td>이닝별 실시간 점수</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_BatterRecord/">IE_BatterRecord</a></span></td><td>타자 실시간 누적 기록</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../realtime/IE_PitcherRecord/">IE_PitcherRecord</a></span></td><td>투수 실시간 누적 기록</td><td><span class="tier-badge t2">T2</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 조인 관계 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>조인 관계</h2></div>
  <div class="product-join"><span class="join-root">IE_GameList</span> <span class="join-key">(gameID, GYEAR)</span>
  ├─ IE_LiveText       <span class="join-key">ON gameID, GYEAR</span>
  ├─ IE_BallCount      <span class="join-key">ON gameID, GYEAR</span>
  ├─ IE_GAMESTATE      <span class="join-key">ON gameID, GYEAR</span>
  ├─ IE_ScoreRHEB      <span class="join-key">ON gameID, GYEAR</span>
  ├─ IE_Scoreinning    <span class="join-key">ON gameID, GYEAR</span>
  ├─ IE_BatterRecord   <span class="join-key">ON gameID, GYEAR</span>
  └─ IE_PitcherRecord  <span class="join-key">ON gameID, GYEAR</span></div>
</div>

<!-- ── 소비자 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>소비자</h2>
    <span class="product-section-count">4개</span>
  </div>
  <div class="product-consumers">
    <div class="product-consumer">
      <div class="product-consumer-icon">📺</div>
      <div class="product-consumer-name">방송팀</div>
      <div class="product-consumer-use">중계 화면 실시간 데이터</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📱</div>
      <div class="product-consumer-name">앱 서비스</div>
      <div class="product-consumer-use">팬 실시간 스코어 조회</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">⚡</div>
      <div class="product-consumer-name">WebSocket 클라이언트</div>
      <div class="product-consumer-use">실시간 이벤트 스트림 소비</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📰</div>
      <div class="product-consumer-name">외부 미디어</div>
      <div class="product-consumer-use">속보·문자 중계</div>
    </div>
  </div>
</div>

<!-- ── 품질 SLA ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>품질 SLA</h2></div>
  <div class="product-sla">
    <div class="product-sla-card">
      <div class="product-sla-metric">지연 시간</div>
      <div class="product-sla-target">&lt; 5초<br>S2i 전송 → DB2 저장</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">가용성</div>
      <div class="product-sla-target">99.9%<br>경기 중 지속 가용</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">완결성</div>
      <div class="product-sla-target">100%<br>모든 타석 이벤트 누락 없음</div>
    </div>
  </div>
</div>

<!-- ── 데이터 흐름 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>데이터 흐름</h2></div>
  <div class="product-flow">

```mermaid
flowchart LR
    S2i[S2i 기록원] -->|실시간 전송| DB2[DB2 시즌 DB]
    DB2 --> WS[WebSocket 서버]
    DB2 --> API[REST API]
    WS --> 방송[방송 중계]
    WS --> 앱[모바일 앱]
    API --> 미디어[외부 미디어]
```

  </div>
</div>

<!-- ── 관련 표준 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>관련 표준</h2></div>
  <div class="product-refs">
    <a class="product-ref" href="../../standards/id-system/">
      <div class="product-ref-icon">🔑</div>
      <div class="product-ref-body">
        <div class="product-ref-title">ID 체계</div>
        <div class="product-ref-desc">game_id, player_id 정의</div>
      </div>
    </a>
    <a class="product-ref" href="../../standards/code-dictionary/">
      <div class="product-ref-icon">📖</div>
      <div class="product-ref-body">
        <div class="product-ref-title">코드 사전</div>
        <div class="product-ref-desc">how_cd, place_cd 등 이벤트 코드</div>
      </div>
    </a>
  </div>
</div>

</div>
