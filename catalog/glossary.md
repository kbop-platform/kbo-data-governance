---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

<!-- Catalog Sub-Tabs -->
<div class="catalog-tabs">
  <a href="../instances/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm2 .5v3h5v-3H2zm0 5v3h5v-3H2zm0 5v2.5h5v-2.5H2zm7-10v3h5v-3H9zm0 5v3h5v-3H9zm0 5v2.5h5V12.5H9z"/></svg></span> 테이블 목록 <span class="tab-count">248</span></a>
  <a href="../columns/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M3 4.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1z"/></svg></span> 컬럼 검색 <span class="tab-count">787</span></a>
  <a href="../glossary/" class="active"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M1 2.828c.885-.37 2.154-.769 3.388-.893C5.33 1.827 6.16 1.882 6.84 2.28c.142.083.27.177.382.28.113-.103.24-.197.382-.28C8.283 1.882 9.114 1.827 10.056 1.935c1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687c-.935-.531-2.12-.603-3.213-.492C2.663 2.307 1.474 2.649.556 3v9.75A.5.5 0 0 1 0 12.5v-10a.5.5 0 0 1 .336-.472z"/></svg></span> 용어 사전 <span class="tab-count">134</span></a>
  <a href="../domains/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8l3.147-3.146zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8l-3.147-3.146z"/></svg></span> 도메인 사전 <span class="tab-count">93</span></a>
  <a href="../codes/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M8.39 12.648a1.32 1.32 0 0 0-.015.18c0 .305.21.508.5.508.266 0 .492-.172.555-.477l.554-2.703h1.204c.421 0 .617-.234.617-.547 0-.312-.188-.53-.617-.53h-.985l.516-2.524h1.265c.43 0 .618-.227.618-.547 0-.313-.188-.532-.618-.532h-1.046l.476-2.304a1.06 1.06 0 0 0 .016-.164.51.51 0 0 0-.516-.516.54.54 0 0 0-.539.43l-.523 2.554H7.617l.477-2.304c.008-.04.015-.118.015-.164a.512.512 0 0 0-.523-.516.539.539 0 0 0-.531.43L6.53 5.484H5.414c-.43 0-.617.22-.617.532 0 .312.187.539.617.539h.906l-.515 2.523H4.609c-.421 0-.609.219-.609.531 0 .313.188.547.61.547h.985l-.516 2.304c-.008.04-.015.118-.015.163 0 .305.21.508.5.508.266 0 .492-.172.554-.477l.555-2.498h2.078l-.555 2.492zm.508-3.649a1855.5 1855.5 0 0 1-.062.289h-2.078l.515-2.523h2.086l-.461 2.234z"/></svg></span> 코드 사전 <span class="tab-count">168</span></a>
</div>

<!-- Stats Cards -->
<div class="grid-stats">
  <div class="stat-card">
    <div class="stat-value" id="stat-terms">134</div>
    <div class="stat-label">전체 용어</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="stat-categories">11</div>
    <div class="stat-label">분류</div>
  </div>
</div>

<!-- Filter Bar -->
<div class="grid-filter-bar">
  <input type="text" id="grid-search" class="filter-search" placeholder="검색... (Ctrl+F)">
  <div class="filter-group">
    <label class="filter-label" for="sel-category">분류</label>
    <select id="sel-category" data-field="category"><option value="">전체</option></select>
  </div>
  <button id="btn-reset" class="btn-reset">초기화</button>
</div>

<!-- Filter Chips -->
<div class="grid-chips" id="filter-chips"></div>

<!-- AG Grid -->
<div id="glossary-grid" class="ag-theme-alpine ag-theme-kbo" style="height:70vh;width:100%"></div>

<!-- Status Bar -->
<div class="grid-status">
  <div class="status-left">
    <span id="status-count">134건 표시</span>
  </div>
  <div>
    <button id="btn-csv" class="btn-csv">CSV 다운로드</button>
    <span style="margin-left:8px;font-size:11px;color:#aaa">2026-02-25 갱신</span>
  </div>
</div>

</div>
