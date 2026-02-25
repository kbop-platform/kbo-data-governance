---
hide:
  - toc
---

<div class="product-page" markdown>

<div class="product-hero">
  <div class="product-hero-badges">
    <span class="p-badge p-badge-product">데이터 프로덕트</span>
    <span class="p-badge p-badge-version">v1</span>
    <span class="p-badge p-badge-domain">마스터</span>
    <span class="p-badge p-badge-refresh">시즌 전 일괄</span>
  </div>
  <div class="product-hero-title">일정 관리</div>
  <div class="product-hero-sub">Schedule</div>
  <div class="product-hero-desc">시즌 경기 일정, 취소/우천 중단 경기, 기상 정보를 관리한다. 시즌 전 일괄 등록 후 변경 시 즉시 갱신.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">3</div><div class="product-stat-label">테이블</div></div>
  <div class="product-stat"><div class="product-stat-val">40</div><div class="product-stat-label">컬럼</div></div>
  <div class="product-stat"><div class="product-stat-val">시즌 전</div><div class="product-stat-label">초기 등록</div></div>
  <div class="product-stat"><div class="product-stat-val">Tier 2~3</div><div class="product-stat-label">데이터 티어</div></div>
</div>

<!-- ── 포함 테이블 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>포함 테이블</h2>
    <span class="product-section-count">3개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>역할</th><th>티어</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="../master/KBO_schedule/">KBO_schedule</a></span></td><td>경기 일정 (시즌 전체)</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../master/CANCEL_GAME/">CANCEL_GAME</a></span></td><td>취소·우천 중단 경기</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/GAMEINFO_WEATHER/">GAMEINFO_WEATHER</a></span></td><td>기상청 상세 날씨</td><td><span class="tier-badge t3">T3</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 조인 관계 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>조인 관계</h2></div>
  <div class="product-join"><span class="join-root">KBO_schedule</span> <span class="join-key">(gmkey, gamedate)</span>
  ├─ CANCEL_GAME        <span class="join-key">ON G_ID</span>
  └─ GAMEINFO_WEATHER   <span class="join-key">ON code (구장 코드 기반)</span></div>
</div>

<!-- ── 소비자 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>소비자</h2>
    <span class="product-section-count">4개</span>
  </div>
  <div class="product-consumers">
    <div class="product-consumer">
      <div class="product-consumer-icon">⚙️</div>
      <div class="product-consumer-name">운영팀</div>
      <div class="product-consumer-use">일정 관리 및 변경 처리</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📺</div>
      <div class="product-consumer-name">방송팀</div>
      <div class="product-consumer-use">중계 편성</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📱</div>
      <div class="product-consumer-name">팬 서비스</div>
      <div class="product-consumer-use">일정 조회 앱·웹</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">🏟️</div>
      <div class="product-consumer-name">구단</div>
      <div class="product-consumer-use">원정 일정 확인</div>
    </div>
  </div>
</div>

<!-- ── 품질 SLA ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>품질 SLA</h2></div>
  <div class="product-sla">
    <div class="product-sla-card">
      <div class="product-sla-metric">초기 등록</div>
      <div class="product-sla-target">시즌 전<br>일괄 등록</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">변경 반영</div>
      <div class="product-sla-target">우천 취소 등<br>발생 시 1시간 내</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">정확성</div>
      <div class="product-sla-target">일정 오류율 0%<br>공식 발표 대비</div>
    </div>
  </div>
</div>

<!-- ── 데이터 흐름 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>데이터 흐름</h2></div>
  <div class="product-flow">

```mermaid
flowchart LR
    OPS[KBO 경기운영팀] -->|시즌 전 등록| DB1[DB1 KBO_schedule]
    OPS -->|변경 발생| DB1
    DB1 --> API[REST API]
    DB1 --> 앱[모바일 앱]
    DB1 --> 웹[웹 서비스]
    API --> 구단[구단 시스템]
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
        <div class="product-ref-desc">game_id, series_id 정의</div>
      </div>
    </a>
    <a class="product-ref" href="../../standards/code-dictionary/">
      <div class="product-ref-icon">📖</div>
      <div class="product-ref-body">
        <div class="product-ref-title">코드 사전</div>
        <div class="product-ref-desc">series_id (시리즈 구분 코드)</div>
      </div>
    </a>
  </div>
</div>

</div>
