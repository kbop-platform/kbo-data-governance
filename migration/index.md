---
hide:
  - toc
---

<div class="sl-landing">

<div class="sl-hero">
  <div class="sl-hero-title">Migration</div>
  <div class="sl-hero-desc">S2i 레거시 DB에서 신규 시스템으로의 마이그레이션 설계와 매핑 정의.</div>
  <div class="sl-hero-stats">
    <div class="sl-hero-stat">
      <div class="stat-num">787</div>
      <div class="stat-label">컬럼 매핑</div>
    </div>
    <div class="sl-hero-stat">
      <div class="stat-num">39</div>
      <div class="stat-label">테이블</div>
    </div>
    <div class="sl-hero-stat">
      <div class="stat-num">252</div>
      <div class="stat-label">인스턴스</div>
    </div>
    <div class="sl-hero-stat">
      <div class="stat-num">17</div>
      <div class="stat-label">DB</div>
    </div>
  </div>
</div>

<div class="sl-cards">

  <a class="sl-card" href="design-decisions/">
    <div class="sl-card-head">
      <div class="sl-card-title">설계 결정 사항</div>
      <span class="sl-card-type">기술</span>
    </div>
    <p class="sl-card-desc">타입 전환(varchar→nvarchar), 인코딩(EUC-KR→UTF-8), 합계행 처리, 미확인 코드 정리 등 핵심 설계 결정.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">타입 전환</span>
      <span class="sl-card-tag">인코딩</span>
      <span class="sl-card-tag">합계행 처리</span>
    </div>
  </a>

  <a class="sl-card" href="column-mapping/">
    <div class="sl-card-head">
      <div class="sl-card-title">컬럼 매핑</div>
      <span class="sl-card-type">참조</span>
    </div>
    <p class="sl-card-desc">787개 컬럼 AS-IS → TO-BE 전수 매핑 매트릭스. 레거시 컬럼명, 표준명, 타입 변환 포함.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">787 컬럼</span>
      <span class="sl-card-tag">AS-IS → TO-BE</span>
      <span class="sl-card-tag">전수 매핑</span>
    </div>
  </a>

  <a class="sl-card" href="table-mapping/">
    <div class="sl-card-head">
      <div class="sl-card-title">테이블 매핑</div>
      <span class="sl-card-type">참조</span>
    </div>
    <p class="sl-card-desc">S2i 운영 DB ↔ 백업 DB 테이블 대조. 248개 인스턴스 매핑, DB별 분포 현황.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">S2i ↔ 백업DB</span>
      <span class="sl-card-tag">인스턴스 대조</span>
    </div>
  </a>

  <a class="sl-card" href="column-diff/">
    <div class="sl-card-head">
      <div class="sl-card-title">컬럼 차이 분석</div>
      <span class="sl-card-type">분석</span>
    </div>
    <p class="sl-card-desc">S2i 대비 백업 DB의 컬럼 차이 분석. 49개 테이블 +1 컬럼, DEFEN +6, ENTRY -1 등 상세.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">차이 분석</span>
      <span class="sl-card-tag">+1 컬럼</span>
      <span class="sl-card-tag">불일치 추적</span>
    </div>
  </a>

</div>

</div>
