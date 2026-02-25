---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

# 용어 사전

> KBO 업무 용어를 한 화면에서 검색·필터 — 야구 기록, 경기 운영, 코드 체계, 데이터 품질

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
  <select id="sel-category" data-field="category"><option value="">분류</option></select>
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
