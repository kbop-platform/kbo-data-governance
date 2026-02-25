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
  <a href="../glossary/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M1 2.828c.885-.37 2.154-.769 3.388-.893C5.33 1.827 6.16 1.882 6.84 2.28c.142.083.27.177.382.28.113-.103.24-.197.382-.28C8.283 1.882 9.114 1.827 10.056 1.935c1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687c-.935-.531-2.12-.603-3.213-.492C2.663 2.307 1.474 2.649.556 3v9.75A.5.5 0 0 1 0 12.5v-10a.5.5 0 0 1 .336-.472z"/></svg></span> 용어 사전 <span class="tab-count">134</span></a>
</div>

<!-- Stats Cards -->
<div class="grid-stats">
  <div class="stat-card">
    <div class="stat-value" id="stat-instances">248</div>
    <div class="stat-label">인스턴스</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-tables">39</div>
    <div class="stat-label">테이블</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-dbs">17</div>
    <div class="stat-label">DB</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-rows">25.7M</div>
    <div class="stat-label">총 행수</div>
  </div>
</div>

<!-- Filter Bar -->
<div class="grid-filter-bar">
  <input type="text" id="grid-search" class="filter-search" placeholder="검색... (Ctrl+F)">
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
    <label class="filter-label" for="sel-schema_gen">세대</label>
    <select id="sel-schema_gen" data-field="schema_gen"><option value="">전체</option></select>
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
