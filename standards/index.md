---
hide:
  - toc
---

<div class="sl-landing">

<div class="sl-hero">
  <div class="sl-hero-title">Standards & Governance</div>
  <div class="sl-hero-desc">데이터 표준 정의와 거버넌스 정책을 체계적으로 관리합니다.</div>
  <div class="sl-hero-stats">
    <div class="sl-hero-stat">
      <div class="stat-num">8</div>
      <div class="stat-label">문서</div>
    </div>
    <div class="sl-hero-stat">
      <div class="stat-num">4</div>
      <div class="stat-label">계층 명명</div>
    </div>
    <div class="sl-hero-stat">
      <div class="stat-num">6</div>
      <div class="stat-label">핵심 ID</div>
    </div>
    <div class="sl-hero-stat">
      <div class="stat-num">6</div>
      <div class="stat-label">역할 정의</div>
    </div>
  </div>
</div>

<div class="sl-group-title">표준 정의</div>

<div class="sl-cards">

  <a class="sl-card" href="naming-rules/">
    <div class="sl-card-head">
      <div class="sl-card-title">명명 규칙</div>
      <span class="sl-card-type">DB · API · Kafka · WS</span>
    </div>
    <p class="sl-card-desc">4계층(DB/API/Kafka/WebSocket) 네이밍 컨벤션. snake_case 기반, 접미사 체계, 비표준 약어 주의사항.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">테이블 명명</span>
      <span class="sl-card-tag">컬럼 접미사</span>
      <span class="sl-card-tag">비표준 약어</span>
    </div>
  </a>

  <a class="sl-card" href="id-system/">
    <div class="sl-card-head">
      <div class="sl-card-title">ID 체계</div>
      <span class="sl-card-type">6종 ID</span>
    </div>
    <p class="sl-card-desc">game_id, player_id, team_id 등 6종 핵심 식별자. 레거시(GMKEY/PCODE) → 표준 전환 규칙.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">구세대 매핑</span>
      <span class="sl-card-tag">신세대 ID</span>
      <span class="sl-card-tag">생성 규칙</span>
    </div>
  </a>

</div>

<div class="sl-group-title">거버넌스</div>

<div class="sl-cards">

  <a class="sl-card" href="../governance/data-ownership/">
    <div class="sl-card-head">
      <div class="sl-card-title">데이터 오너십</div>
      <span class="sl-card-type">역할 · 오너십</span>
    </div>
    <p class="sl-card-desc">도메인별 데이터 오너, 스튜어드, 엔지니어 역할 정의. 3인 팀 운영 체계.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">RACI 매트릭스</span>
      <span class="sl-card-tag">도메인 담당</span>
    </div>
  </a>

  <a class="sl-card" href="../governance/quality-rules/">
    <div class="sl-card-head">
      <div class="sl-card-title">품질 규칙</div>
      <span class="sl-card-type">SLA · KPI</span>
    </div>
    <p class="sl-card-desc">데이터 품질 SLA, 이상치 탐지 규칙, KPI 대시보드 기준. 완전성·정확성·적시성 지표.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">SLA 정의</span>
      <span class="sl-card-tag">이상치 탐지</span>
      <span class="sl-card-tag">KPI</span>
    </div>
  </a>

  <a class="sl-card" href="../governance/change-process/">
    <div class="sl-card-head">
      <div class="sl-card-title">변경 관리 절차</div>
      <span class="sl-card-type">절차 · 승인</span>
    </div>
    <p class="sl-card-desc">스키마·코드값 변경 요청부터 승인까지. Fast-Track 프로세스, 3인 팀 현실화.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">변경 요청</span>
      <span class="sl-card-tag">Fast-Track</span>
      <span class="sl-card-tag">승인 절차</span>
    </div>
  </a>

  <a class="sl-card" href="../governance/table-design-guide/">
    <div class="sl-card-head">
      <div class="sl-card-title">테이블 설계 가이드</div>
      <span class="sl-card-type">설계 · 인덱스</span>
    </div>
    <p class="sl-card-desc">정규화 전략, 인덱스 설계, 파티셔닝 기준. 신규 테이블 생성 시 참고.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">정규화</span>
      <span class="sl-card-tag">인덱스 전략</span>
      <span class="sl-card-tag">파티셔닝</span>
    </div>
  </a>

  <a class="sl-card" href="../governance/data-security/">
    <div class="sl-card-head">
      <div class="sl-card-title">데이터 보안</div>
      <span class="sl-card-type">RBAC · PII</span>
    </div>
    <p class="sl-card-desc">데이터 분류 체계, 역할 기반 접근 제어(RBAC), PII 처리 정책.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">분류 체계</span>
      <span class="sl-card-tag">접근 제어</span>
      <span class="sl-card-tag">PII 마스킹</span>
    </div>
  </a>

  <a class="sl-card" href="../governance/disaster-recovery/">
    <div class="sl-card-head">
      <div class="sl-card-title">재해 복구</div>
      <span class="sl-card-type">RTO · RPO</span>
    </div>
    <p class="sl-card-desc">RTO/RPO 목표, 백업 정책, 복구 절차. 티어별 복구 우선순위 정의.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">백업 정책</span>
      <span class="sl-card-tag">복구 절차</span>
      <span class="sl-card-tag">티어별 우선순위</span>
    </div>
  </a>

</div>

</div>
