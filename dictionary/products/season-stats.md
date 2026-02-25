---
hide:
  - toc
---

<div class="product-page" markdown>

<div class="product-hero">
  <div class="product-hero-badges">
    <span class="p-badge p-badge-product">데이터 프로덕트</span>
    <span class="p-badge p-badge-version">v1</span>
    <span class="p-badge p-badge-domain">통계</span>
    <span class="p-badge p-badge-refresh">D+1</span>
  </div>
  <div class="product-hero-title">시즌 통계</div>
  <div class="product-hero-sub">Season Stats</div>
  <div class="product-hero-desc">시즌 중·후 집계되는 선수/팀 통계를 제공한다. 타격·투구 합산, 팀 순위, 상황별 통계 포함.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">10</div><div class="product-stat-label">테이블</div></div>
  <div class="product-stat"><div class="product-stat-val">318</div><div class="product-stat-label">컬럼</div></div>
  <div class="product-stat"><div class="product-stat-val">D+1</div><div class="product-stat-label">갱신 주기</div></div>
  <div class="product-stat"><div class="product-stat-val">Tier 2~3</div><div class="product-stat-label">데이터 티어</div></div>
</div>

<div class="product-warn">
  <div><strong>GYEAR=9999</strong>는 통산 기록행이다. 시즌별 조회 시 반드시 제외해야 한다.<br>
  <strong>PCODE='T'</strong> 또는 <strong>PCODE='B'</strong>는 팀 합계행이다. 개인 통계 조회 시 제외 필요.</div>
</div>

<!-- ── 포함 테이블 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>포함 테이블</h2>
    <span class="product-section-count">10개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>역할</th><th>티어</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="../stats/BatTotal/">BatTotal</a></span></td><td>타격 시즌/통산 합산</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/PitTotal/">PitTotal</a></span></td><td>투구 시즌/통산 합산</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/TeamRank/">TeamRank</a></span></td><td>팀 순위 (시즌별)</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/KBO_BATRESULT/">KBO_BATRESULT</a></span></td><td>이닝별 타격 결과 (90컬럼)</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/KBO_PITRESULT/">KBO_PITRESULT</a></span></td><td>투수 경기 결과 상세</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/KBO_ETCGAME/">KBO_ETCGAME</a></span></td><td>기타 경기 이벤트</td><td><span class="tier-badge t3">T3</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/SEASON_PLAYER_HITTER/">SEASON_PLAYER_HITTER</a></span></td><td>시즌별 타자 통계</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/SEASON_PLAYER_HITTER_SITUATION/">SEASON_PLAYER_HITTER_SITUATION</a></span></td><td>타자 상황별 통계</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/SEASON_PLAYER_PITCHER/">SEASON_PLAYER_PITCHER</a></span></td><td>시즌별 투수 통계</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../stats/SEASON_PLAYER_PITCHER_SITUATION/">SEASON_PLAYER_PITCHER_SITUATION</a></span></td><td>투수 상황별 통계</td><td><span class="tier-badge t2">T2</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 조인 관계 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>조인 관계</h2></div>
  <div class="product-join"><span class="join-root">BatTotal / PitTotal</span> <span class="join-key">(PCODE, GYEAR)</span>
  ├─ BatTotal              <span class="join-key">ON PCODE, GYEAR</span>
  ├─ PitTotal              <span class="join-key">ON PCODE, GYEAR</span>
  └─ TeamRank              <span class="join-key">ON GYEAR, TEAM</span>

<span class="join-root">SEASON_PLAYER_*</span> <span class="join-key">(SEASON_ID, P_ID)</span>
  ├─ SEASON_PLAYER_HITTER              <span class="join-key">ON SEASON_ID, P_ID</span>
  ├─ SEASON_PLAYER_HITTER_SITUATION    <span class="join-key">ON SEASON_ID, P_ID</span>
  ├─ SEASON_PLAYER_PITCHER             <span class="join-key">ON SEASON_ID, P_ID</span>
  └─ SEASON_PLAYER_PITCHER_SITUATION   <span class="join-key">ON SEASON_ID, P_ID</span>

<span class="join-root">KBO_BATRESULT / KBO_PITRESULT</span> <span class="join-key">(GMKEY, PCODE)</span>
  ├─ KBO_BATRESULT         <span class="join-key">ON GMKEY, PCODE</span>
  ├─ KBO_PITRESULT         <span class="join-key">ON GMKEY, PCODE</span>
  └─ KBO_ETCGAME           <span class="join-key">ON GMKEY</span></div>
</div>

<!-- ── 소비자 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>소비자</h2>
    <span class="product-section-count">4개</span>
  </div>
  <div class="product-consumers">
    <div class="product-consumer">
      <div class="product-consumer-icon">📊</div>
      <div class="product-consumer-name">통계팀</div>
      <div class="product-consumer-use">리더보드·순위 산출</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📰</div>
      <div class="product-consumer-name">미디어</div>
      <div class="product-consumer-use">기록 기사 작성</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">🔗</div>
      <div class="product-consumer-name">외부 API</div>
      <div class="product-consumer-use">통계 조회 서비스</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">🔬</div>
      <div class="product-consumer-name">분석팀</div>
      <div class="product-consumer-use">세이버메트릭스 분석</div>
    </div>
  </div>
</div>

<!-- ── 품질 SLA ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>품질 SLA</h2></div>
  <div class="product-sla">
    <div class="product-sla-card">
      <div class="product-sla-metric">일일 갱신</div>
      <div class="product-sla-target">시즌 중 D+1<br>전일 경기 결과 반영</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">시즌 확정</div>
      <div class="product-sla-target">시즌 종료 후 30일 내<br>최종 확정</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">통산 기록</div>
      <div class="product-sla-target">GYEAR=9999 행<br>연 1회 갱신</div>
    </div>
  </div>
</div>

<!-- ── 데이터 흐름 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>데이터 흐름</h2></div>
  <div class="product-flow">

```mermaid
flowchart LR
    DB2[DB2 경기 기록] -->|일일 집계| AGG[집계 처리]
    AGG --> DB1_B[DB1 BatTotal/PitTotal]
    AGG --> DB1_S[DB1 SEASON_PLAYER_*]
    DB1_B --> API[REST API]
    DB1_S --> API
    DB1_B --> BI[통계 대시보드]
    DB1_S --> BI
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
        <div class="product-ref-desc">player_id, season_id 정의</div>
      </div>
    </a>
    <a class="product-ref" href="../../standards/domain-types/">
      <div class="product-ref-icon">📐</div>
      <div class="product-ref-body">
        <div class="product-ref-title">도메인 타입</div>
        <div class="product-ref-desc">비율은 decimal 타입 적용</div>
      </div>
    </a>
    <a class="product-ref" href="../../standards/abbreviations/">
      <div class="product-ref-icon">📝</div>
      <div class="product-ref-body">
        <div class="product-ref-title">약어 사전</div>
        <div class="product-ref-desc">타격·투구 통계 약어</div>
      </div>
    </a>
  </div>
</div>

</div>
