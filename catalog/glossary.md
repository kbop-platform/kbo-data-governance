---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

<!-- Catalog Sub-Tabs -->
<div class="catalog-tabs">
  <a href="../instances/"><span class="tab-icon">&#9638;</span> 테이블 목록 <span class="tab-count">248</span></a>
  <a href="../columns/"><span class="tab-icon">&#9776;</span> 컬럼 검색 <span class="tab-count">787</span></a>
  <a href="../glossary/" class="active"><span class="tab-icon">&#9733;</span> 용어 사전 <span class="tab-count">134</span></a>
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
