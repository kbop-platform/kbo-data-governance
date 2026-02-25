---
hide:
  - toc
  - navigation
---

<div class="ag-grid-page" markdown>

# 인스턴스 현황

> 17개 DB × 248개 테이블 인스턴스 — 물리 배포 현황을 한 화면에서 검색/필터

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
  <select id="sel-db_type" data-field="db_type"><option value="">DB타입</option></select>
  <select id="sel-league" data-field="league"><option value="">리그</option></select>
  <select id="sel-domain" data-field="domain"><option value="">도메인</option></select>
  <select id="sel-table_name" data-field="table_name"><option value="">테이블</option></select>
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
