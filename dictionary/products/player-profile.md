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
    <span class="p-badge p-badge-refresh">시즌 전</span>
  </div>
  <div class="product-hero-title">선수 프로필</div>
  <div class="product-hero-sub">Player Profile</div>
  <div class="product-hero-desc">선수의 기본 인적 사항, 경력, 계약 정보를 통합 제공한다. 시즌 개시 전 갱신되며, 시즌 중 이적/FA 발생 시 수시 갱신.</div>
</div>

<div class="product-stats">
  <div class="product-stat"><div class="product-stat-val">4</div><div class="product-stat-label">테이블</div></div>
  <div class="product-stat"><div class="product-stat-val">57</div><div class="product-stat-label">컬럼</div></div>
  <div class="product-stat"><div class="product-stat-val">시즌 전</div><div class="product-stat-label">갱신 주기</div></div>
  <div class="product-stat"><div class="product-stat-val">Tier 1~3</div><div class="product-stat-label">데이터 티어</div></div>
</div>

<div class="product-security">
  <div><strong>Restricted 등급</strong> - person 테이블은 PII(개인식별정보)를 포함한다. 외부 제공 시 생년월일, 연봉 등 민감 필드의 비식별화가 필수이다.</div>
</div>

<!-- ── 포함 테이블 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>포함 테이블</h2>
    <span class="product-section-count">4개</span>
  </div>
  <table class="product-table">
    <thead><tr><th>테이블</th><th>역할</th><th>티어</th></tr></thead>
    <tbody>
      <tr><td><span class="tbl-name"><a href="../master/person/">person</a></span></td><td>선수 마스터 (이름·생년·포지션·경력)</td><td><span class="tier-badge t1">T1</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../master/person2/">person2</a></span></td><td>선수 보조 정보</td><td><span class="tier-badge t3">T3</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../master/PERSON/">PERSON</a></span></td><td>선수 마스터 (마이너)</td><td><span class="tier-badge t3">T3</span></td></tr>
      <tr><td><span class="tbl-name"><a href="../master/PERSON_FA/">PERSON_FA</a></span></td><td>FA 선수 정보</td><td><span class="tier-badge t3">T3</span></td></tr>
    </tbody>
  </table>
</div>

<!-- ── 조인 관계 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>조인 관계</h2></div>
  <div class="product-join"><span class="join-root">person</span> <span class="join-key">(GYEAR, PCODE)</span>
  ├─ person2     <span class="join-key">ON GYEAR, PCODE</span>
  ├─ PERSON      <span class="join-key">ON PCODE (마이너 연계)</span>
  └─ PERSON_FA   <span class="join-key">(FK 없음, PCODE 기반 수동 매핑)</span></div>
</div>

<!-- ── 소비자 ── -->
<div class="product-section">
  <div class="product-section-hdr">
    <h2>소비자</h2>
    <span class="product-section-count">4개</span>
  </div>
  <div class="product-consumers">
    <div class="product-consumer">
      <div class="product-consumer-icon">📋</div>
      <div class="product-consumer-name">기록팀</div>
      <div class="product-consumer-use">선수 등록·말소 관리</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">👔</div>
      <div class="product-consumer-name">인사팀</div>
      <div class="product-consumer-use">계약 관리</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">📰</div>
      <div class="product-consumer-name">미디어</div>
      <div class="product-consumer-use">선수 프로필 카드</div>
    </div>
    <div class="product-consumer">
      <div class="product-consumer-icon">🔗</div>
      <div class="product-consumer-name">외부 API</div>
      <div class="product-consumer-use">선수 조회 서비스</div>
    </div>
  </div>
</div>

<!-- ── 품질 SLA ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>품질 SLA</h2></div>
  <div class="product-sla">
    <div class="product-sla-card">
      <div class="product-sla-metric">갱신 시점</div>
      <div class="product-sla-target">시즌 개시 전<br>전체 갱신</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">수시 갱신</div>
      <div class="product-sla-target">이적·FA·신인 드래프트 후<br>1영업일 내</div>
    </div>
    <div class="product-sla-card">
      <div class="product-sla-metric">PII 보호</div>
      <div class="product-sla-target">생년월일, 연봉 →<br>Restricted 등급</div>
    </div>
  </div>
</div>

<!-- ── 데이터 흐름 ── -->
<div class="product-section">
  <div class="product-section-hdr"><h2>데이터 흐름</h2></div>
  <div class="product-flow">

```mermaid
flowchart LR
    HR[KBO 인사팀] -->|선수 등록/변경| DB1[DB1 MASTER]
    DB1 --> API[REST API]
    DB1 --> 신규[신규 시스템]
    API --> 미디어[미디어/앱]
    API -->|비식별화| 외부[외부 서비스]
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
        <div class="product-ref-desc">player_id (PCODE → P_ID 전환) 정의</div>
      </div>
    </a>
    <a class="product-ref" href="../../standards/domain-types/">
      <div class="product-ref-icon">📐</div>
      <div class="product-ref-body">
        <div class="product-ref-title">도메인 타입</div>
        <div class="product-ref-desc">날짜·문자열 타입 표준</div>
      </div>
    </a>
    <a class="product-ref" href="../../governance/data-security/">
      <div class="product-ref-icon">🔒</div>
      <div class="product-ref-body">
        <div class="product-ref-title">데이터 보안</div>
        <div class="product-ref-desc">PII 등급 분류 및 비식별화 정책</div>
      </div>
    </a>
  </div>
</div>

</div>
