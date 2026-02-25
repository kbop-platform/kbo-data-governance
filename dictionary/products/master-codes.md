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
    <span class="p-badge p-badge-refresh">연 1회</span>
  </div>
  <div class="product-hero-title">기준 데이터</div>
  <div class="product-hero-sub">Master Codes</div>
  <div class="product-hero-desc">전 시스템에서 참조하는 기준 마스터 데이터를 제공한다. 팀 코드, 구장 코드 등 변경 빈도가 낮은 참조 데이터.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">2</div><div class="product-stat-label">테이블</div></div>
  <div class="product-stat"><div class="product-stat-val">10</div><div class="product-stat-label">컬럼</div></div>
  <div class="product-stat"><div class="product-stat-val">연 1회</div><div class="product-stat-label">갱신 주기</div></div>
  <div class="product-stat"><div class="product-stat-val">Tier 3</div><div class="product-stat-label">데이터 티어</div></div>
</div>

<div class="product-warn">
  <div>팀 코드(OB, SK 등)는 구단명 변경에도 <strong>불변</strong>이다. 이력 관리는 TEAM 테이블의 연도별 팀명으로 처리한다.</div>
</div>

<!-- ── 포함 테이블 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>포함 테이블</h2>
    <span class="product-section-count">2개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>역할</th><th>티어</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="../master/TEAM/">TEAM</a></span></td><td>팀 마스터 (연도별 팀명 이력)</td><td><span class="tier-badge t3">T3</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../master/STADIUM/">STADIUM</a></span></td><td>구장 마스터 (연도별 구장명)</td><td><span class="tier-badge t3">T3</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 조인 관계 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>조인 관계</h2></div>
  <div class="product-join"><span class="join-root">TEAM</span> <span class="join-key">(SEASON_ID, T_ID)</span>
  └─ 전 시스템에서 FK 참조

<span class="join-root">STADIUM</span> <span class="join-key">(gyear, stadium)</span>
  └─ 전 시스템에서 FK 참조</div>
</div>

<!-- ── 소비자 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>소비자</h2>
    <span class="product-section-count">3개</span>
  </div>
  <div class="product-consumers">
    <div class="product-consumer">
      <div class="product-consumer-icon">🔗</div>
      <div class="product-consumer-name">전 시스템</div>
      <div class="product-consumer-use">FK 참조 (팀·구장 코드)</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">⚙️</div>
      <div class="product-consumer-name">운영팀</div>
      <div class="product-consumer-use">구단·구장 관리</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">🌐</div>
      <div class="product-consumer-name">외부 API</div>
      <div class="product-consumer-use">코드 조회 서비스</div>
    </div>
  </div>
</div>

<!-- ── 품질 SLA ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>품질 SLA</h2></div>
  <div class="product-sla">
    <div class="product-sla-card">
      <div class="product-sla-metric">갱신 주기</div>
      <div class="product-sla-target">연 1회<br>시즌 전 갱신</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">변경 반영</div>
      <div class="product-sla-target">구단명 변경·신규 구장 등<br>확정 즉시</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">무결성</div>
      <div class="product-sla-target">코드 삭제 금지<br>이력 보존 원칙</div>
    </div>
  </div>
</div>

<!-- ── 데이터 흐름 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>데이터 흐름</h2></div>
  <div class="product-flow">

```mermaid
flowchart LR
    HQ[KBO 사무국] -->|코드 확정| DB1[DB1 MASTER]
    DB1 --> 경기[경기 기록 시스템]
    DB1 --> 통계[통계 시스템]
    DB1 --> 실시간[실시간 중계]
    DB1 --> API[REST API]
    API --> 외부[외부 서비스]
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
        <div class="product-ref-desc">team_id, stadium_id 정의</div>
      </div>
    </a>
    <a class="product-ref" href="../../standards/code-dictionary/">
      <div class="product-ref-icon">📖</div>
      <div class="product-ref-body">
        <div class="product-ref-title">코드 사전</div>
        <div class="product-ref-desc">팀 코드, 구장 코드</div>
      </div>
    </a>
  </div>
</div>

</div>
