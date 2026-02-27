---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

<!-- Catalog Sub-Tabs -->
<div class="catalog-tabs">
  <a href="../instances/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm2 .5v3h5v-3H2zm0 5v3h5v-3H2zm0 5v2.5h5v-2.5H2zm7-10v3h5v-3H9zm0 5v3h5v-3H9zm0 5v2.5h5V12.5H9z"/></svg></span> 테이블 목록 <span class="tab-count">248</span></a>
  <a href="../columns/" class="active"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M3 4.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1z"/></svg></span> 컬럼 검색 <span class="tab-count">787</span></a>
</div>

<div class="grid-stats-inline">
  <span class="stat-inline"><strong id="stat-columns">787</strong> 컬럼</span>
  <span class="stat-inline"><strong id="stat-tables">39</strong> 테이블</span>
  <span class="stat-inline"><strong id="stat-domains">4</strong> 도메인</span>
  <span class="stat-inline"><strong id="stat-rows">25.7M</strong> 총 행수</span>
  <span class="stat-inline"><strong id="stat-tier1">12</strong> Tier 1</span>
</div>

<!-- Filter Bar -->
<div class="grid-filter-bar">
  <div class="search-group">
    <select id="search-scope" class="search-scope"><option value="">전체</option></select>
    <input type="text" id="grid-search" class="filter-search" placeholder="검색... (Ctrl+F)">
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-domain">도메인</label>
    <select id="sel-domain" data-field="domain"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-table">테이블</label>
    <select id="sel-table" data-field="table_name"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-type">타입</label>
    <select id="sel-type" data-field="data_type"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-tier">티어</label>
    <select id="sel-tier" data-field="tier"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-owner">오너</label>
    <select id="sel-owner" data-field="owner"><option value="">전체</option></select>
  </div>
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
