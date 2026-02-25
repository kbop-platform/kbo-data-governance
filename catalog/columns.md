---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

<!-- Stats Cards -->
<div class="grid-stats">
  <div class="stat-card">
    <div class="stat-value" id="stat-columns">787</div>
    <div class="stat-label">전체 컬럼</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-tables">39</div>
    <div class="stat-label">테이블</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-domains">4</div>
    <div class="stat-label">도메인</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-rows">25.7M</div>
    <div class="stat-label">총 행수</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-tier1">12</div>
    <div class="stat-label">Tier 1</div>
  </div>
</div>

<!-- Filter Bar -->
<div class="grid-filter-bar">
  <input type="text" id="grid-search" class="filter-search" placeholder="검색... (Ctrl+F)">
  <select id="sel-domain" data-field="domain"><option value="">도메인</option></select>
  <select id="sel-table" data-field="table_name"><option value="">테이블</option></select>
  <select id="sel-type" data-field="data_type"><option value="">타입</option></select>
  <select id="sel-tier" data-field="tier"><option value="">티어</option></select>
  <select id="sel-owner" data-field="owner"><option value="">오너</option></select>
  <button id="btn-reset" class="btn-reset">초기화</button>
</div>

<!-- Filter Chips -->
<div class="grid-chips" id="filter-chips"></div>

<!-- AG Grid -->
<div id="catalog-grid" class="ag-theme-alpine ag-theme-kbo" style="height:70vh;width:100%"></div>

<!-- Status Bar -->
<div class="grid-status">
  <div class="status-left">
    <span id="status-count">787건 표시</span>
    <span id="status-tables">39 테이블</span>
  </div>
  <div>
    <button id="btn-csv" class="btn-csv">CSV 다운로드</button>
    <span style="margin-left:8px;font-size:11px;color:#aaa">2026-02-25 갱신</span>
  </div>
</div>

</div>
