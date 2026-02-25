---
hide:
  - toc
---

<div class="product-page" markdown>

<div class="product-hero">
  <div class="product-hero-badges">
    <span class="p-badge p-badge-product">데이터 프로덕트</span>
    <span class="p-badge p-badge-version">v1</span>
    <span class="p-badge p-badge-domain">경기 기록</span>
    <span class="p-badge p-badge-refresh">경기 당일</span>
  </div>
  <div class="product-hero-title">경기 요약</div>
  <div class="product-hero-sub">Game Summary</div>
  <div class="product-hero-desc">단일 경기의 전체 결과를 하나의 단위로 제공한다. 라인 스코어, 주요 선수 기록, 경기 메타데이터를 포함.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">8</div><div class="product-stat-label">테이블</div></div>
  <div class="product-stat"><div class="product-stat-val">216</div><div class="product-stat-label">컬럼</div></div>
  <div class="product-stat"><div class="product-stat-val">경기 당일</div><div class="product-stat-label">갱신 주기</div></div>
  <div class="product-stat"><div class="product-stat-val">Tier 1~2</div><div class="product-stat-label">데이터 티어</div></div>
</div>

<!-- ── 포함 테이블 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>포함 테이블</h2>
    <span class="product-section-count">8개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>역할</th><th>티어</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="../game/GAMEINFO/">GAMEINFO</a></span></td><td>경기 기본 정보 (일시·구장·심판·날씨)</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/Hitter/">Hitter</a></span></td><td>경기별 타자 기록</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/Pitcher/">Pitcher</a></span></td><td>경기별 투수 기록</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/Score/">Score</a></span></td><td>이닝별 스코어</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/ENTRY/">ENTRY</a></span></td><td>출전 라인업</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/GAMECONTAPP/">GAMECONTAPP</a></span></td><td>타석별 플레이 상세</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/DEFEN/">DEFEN</a></span></td><td>수비 기록</td><td><span class="tier-badge t2">T2</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../game/GAME_HR/">GAME_HR</a></span></td><td>홈런 상세</td><td><span class="tier-badge t2">T2</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 조인 관계 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>조인 관계</h2></div>
  <div class="product-join"><span class="join-root">GAMEINFO</span> <span class="join-key">(GMKEY / game_id)</span>
  ├─ Hitter       <span class="join-key">ON GMKEY, GDAY</span>
  ├─ Pitcher      <span class="join-key">ON GMKEY, GDAY</span>
  ├─ Score        <span class="join-key">ON GMKEY, GDAY</span>
  ├─ ENTRY        <span class="join-key">ON GMKEY, GDAY</span>
  ├─ GAMECONTAPP  <span class="join-key">ON GMKEY, GYEAR</span>
  ├─ DEFEN        <span class="join-key">ON GMKEY, GDAY</span>
  └─ GAME_HR      <span class="join-key">ON G_ID</span></div>
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
      <div class="product-consumer-use">중계 화면 데이터 제공</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📋</div>
      <div class="product-consumer-name">기록팀</div>
      <div class="product-consumer-use">공식 기록 확정</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📊</div>
      <div class="product-consumer-name">통계팀</div>
      <div class="product-consumer-use">시즌 집계 입력 데이터</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">🔗</div>
      <div class="product-consumer-name">외부 API</div>
      <div class="product-consumer-use">경기 결과 제공</div>
    </div>
  </div>
</div>

<!-- ── 품질 SLA ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>품질 SLA</h2></div>
  <div class="product-sla">
    <div class="product-sla-card">
      <div class="product-sla-metric">완결성</div>
      <div class="product-sla-target">경기 종료 후 30분 내<br>GAMEINFO·Score 수신</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">확정 시한</div>
      <div class="product-sla-target">익일 17:00 전<br>CONFIRMED 상태 전환</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">오류율</div>
      <div class="product-sla-target">&lt; 0.1%<br>FK 불일치 + NULL PK</div>
    </div>
  </div>
</div>

<!-- ── 데이터 흐름 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>데이터 흐름</h2></div>
  <div class="product-flow">

```mermaid
flowchart LR
    S2i[S2i 운영DB] -->|경기 당일| DB2[DB2 시즌 DB]
    DB2 -->|확정 후| DB1[DB1 영구 DB]
    DB1 --> API[REST API]
    DB1 --> BI[통계 대시보드]
    DB2 --> RT[실시간 중계]
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
    <a class="product-ref" href="../../standards/domain-types/">
      <div class="product-ref-icon">📐</div>
      <div class="product-ref-body">
        <div class="product-ref-title">도메인 타입</div>
        <div class="product-ref-desc">컬럼 타입 표준</div>
      </div>
    </a>
  </div>
</div>

</div>
