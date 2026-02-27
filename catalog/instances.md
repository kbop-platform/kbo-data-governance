---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

<!-- Catalog Sub-Tabs -->
<div class="catalog-tabs">
  <a href="../instances/" class="active"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm2 .5v3h5v-3H2zm0 5v3h5v-3H2zm0 5v2.5h5v-2.5H2zm7-10v3h5v-3H9zm0 5v3h5v-3H9zm0 5v2.5h5V12.5H9z"/></svg></span> 테이블 목록 <span class="tab-count">248</span></a>
  <a href="../columns/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M3 4.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1z"/></svg></span> 컬럼 검색 <span class="tab-count">787</span></a>
</div>

<div class="grid-stats-inline">
  <span class="stat-inline"><strong id="stat-instances">248</strong> 인스턴스</span>
  <span class="stat-inline"><strong id="stat-tables">39</strong> 테이블</span>
  <span class="stat-inline"><strong id="stat-dbs">17</strong> DB</span>
  <span class="stat-inline"><strong id="stat-rows">25.7M</strong> 총 행수</span>
</div>

<div class="grid-filter-bar">
  <div class="search-group">
    <select id="search-scope" class="search-scope"><option value="">전체</option></select>
    <input type="text" id="grid-search" class="filter-search" placeholder="검색... (Ctrl+F)">
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-db_name">DB명</label>
    <select id="sel-db_name" data-field="db_name"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-db_type">DB타입</label>
    <select id="sel-db_type" data-field="db_type"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-league">리그</label>
    <select id="sel-league" data-field="league"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-domain">도메인</label>
    <select id="sel-domain" data-field="domain"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-tier">티어</label>
    <select id="sel-tier" data-field="tier"><option value="">전체</option></select>
  </div>
  <div class="filter-group">
    <label class="filter-label" for="sel-table_name">테이블</label>
    <select id="sel-table_name" data-field="table_name"><option value="">전체</option></select>
  </div>
  <button id="btn-reset" class="btn-reset">초기화</button>
</div>

<!-- Filter Chips -->
<div class="grid-chips" id="filter-chips"></div>

<!-- AG Grid -->
<div id="instance-grid" class="ag-theme-alpine ag-theme-kbo" style="height:70vh;width:100%"></div>

<!-- Status Bar -->
<div class="grid-status">
  <div class="status-left">
    <span id="status-count">248건 표시</span>
    <span id="status-tables">39 테이블</span>
    <span id="status-dbs">17 DB</span>
  </div>
  <div>
    <button id="btn-csv" class="btn-csv">CSV 다운로드</button>
    <span style="margin-left:8px;font-size:11px;color:#aaa">2026-02-25 갱신</span>
  </div>
</div>

</div>
