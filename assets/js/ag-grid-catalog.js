/* AG Grid - 컬럼 카탈로그 (catalog/columns.md) */
(function () {
  "use strict";

  var G = window.AgGridCommon;
  var gridApi = null;
  var allRows = [];

  var DROPDOWN_FIELDS = ["domain", "table_name", "data_type", "tier", "owner"];
  var DROPDOWN_IDS = {
    domain: "sel-domain",
    table_name: "sel-table",
    data_type: "sel-type",
    tier: "sel-tier",
    owner: "sel-owner",
  };
  var DROPDOWN_LABELS = {
    domain: "도메인",
    table_name: "테이블",
    data_type: "타입",
    tier: "티어",
    owner: "오너",
  };

  var COLUMN_DEFS = [
    {
      headerName: "도메인", field: "domain", width: 90, filter: false, pinned: "left",
    },
    {
      headerName: "테이블", field: "table_name", width: 140, filter: false, pinned: "left",
      cellRenderer: function (p) {
        if (!p.value) return "";
        var url = p.data.table_doc_url;
        var std = p.data.table_std_name;
        var tip = std ? std : "";
        return '<a href="' + G.getBaseUrl() + url +
          '" title="' + tip +
          '" style="color:var(--kbo-accent,#4A7BF7);text-decoration:none">' +
          p.value + "</a>";
      },
    },
    { headerName: "#", field: "ordinal", width: 50, filter: "agNumberColumnFilter", sort: "asc" },
    {
      headerName: "컬럼명", field: "column_name", width: 150, filter: "agTextColumnFilter",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    {
      headerName: "타입", field: "data_type", width: 85, filter: false,
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    { headerName: "길이", field: "max_length", width: 60, filter: "agNumberColumnFilter" },
    {
      headerName: "NULL", field: "is_nullable", width: 55, filter: false,
      cellRenderer: function (p) {
        return p.value === "NN" ? '<span class="cell-badge-nn">NN</span>' : "";
      },
    },
    {
      headerName: "PK", field: "is_pk", width: 50, filter: false,
      cellRenderer: function (p) {
        return p.value === "PK" ? '<span class="cell-badge-pk">PK</span>' : "";
      },
    },
    {
      headerName: "설명", field: "description", flex: 2, minWidth: 200,
      filter: "agTextColumnFilter", tooltipField: "description",
    },
    {
      headerName: "표준명(안)", field: "std_name", width: 150, filter: "agTextColumnFilter",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    {
      headerName: "티어", field: "tier", width: 70, filter: false,
      valueFormatter: function (p) { return p.value ? p.value.replace("Tier ", "T") : ""; },
    },
    { headerName: "오너", field: "owner", width: 100, filter: false },
    {
      headerName: "행수", field: "row_count", width: 90, filter: "agNumberColumnFilter",
      valueFormatter: function (p) {
        return p.value != null ? p.value.toLocaleString("ko-KR") : "";
      },
    },
  ];

  var filterEngine = G.createFilterEngine({
    dropdownFields: DROPDOWN_FIELDS,
    haystackFields: ["column_name", "description", "std_name", "table_name", "domain"],
    searchableColumns: [
      { field: "column_name", label: "컬럼명" },
      { field: "table_name", label: "테이블" },
      { field: "description", label: "설명" },
      { field: "std_name", label: "표준명(안)" },
      { field: "domain", label: "도메인" }
    ]
  });

  var dropdownEngine = G.createDropdownEngine({
    filterEngine: filterEngine,
    allRows: function () { return allRows; },
    gridApi: function () { return gridApi; },
    dropdownFields: DROPDOWN_FIELDS,
    dropdownIds: DROPDOWN_IDS,
    dropdownLabels: DROPDOWN_LABELS,
    csvFileName: "KBO_컬럼_카탈로그.csv"
  });

  /* ── Stats Cards ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var tables = new Set();
    var domains = new Set();
    var tier1 = 0;
    var totalRowCount = 0;
    var tableRowCounts = {};

    gridApi.forEachNodeAfterFilter(function (node) {
      var d = node.data;
      if (!d) return;
      tables.add(d.table_name);
      domains.add(d.domain);
      if (d.tier === "Tier 1") tier1++;
      if (!tableRowCounts[d.table_name]) tableRowCounts[d.table_name] = d.row_count || 0;
    });
    for (var t in tableRowCounts) totalRowCount += tableRowCounts[t];

    G.setText("stat-columns", displayed === total ? G.formatNumber(total) : G.formatNumber(displayed) + " / " + G.formatNumber(total));
    G.setText("stat-tables", tables.size);
    G.setText("stat-domains", domains.size);
    G.setText("stat-rows", (totalRowCount / 1e6).toFixed(1) + "M");
    G.setText("stat-tier1", tier1);
    G.setText("status-count", G.formatNumber(displayed) + " / " + G.formatNumber(total) + "건");
    G.setText("status-tables", tables.size + " 테이블");
  }

  /* ── 반응형 ── */
  function handleResponsive() {
    if (!gridApi) return;
    var narrow = window.innerWidth < 1200;
    gridApi.setColumnsVisible(["owner", "row_count"], !narrow);
  }

  function initGrid() {
    var gridDiv = document.getElementById("catalog-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(G.getBaseUrl() + "assets/data/catalog-columns.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        allRows = data.rows || [];

        agGrid.createGrid(gridDiv, {
          columnDefs: COLUMN_DEFS,
          rowData: allRows,
          defaultColDef: { sortable: true, resizable: true, suppressMovable: true },
          animateRows: true,
          enableCellTextSelection: true,
          tooltipShowDelay: 300,
          overlayNoRowsTemplate: G.NO_ROWS,
          isExternalFilterPresent: filterEngine.isPresent,
          doesExternalFilterPass: filterEngine.doesPass,
          onFilterChanged: function () { updateStats(); dropdownEngine.renderChips(); },
          onRowDoubleClicked: function (e) {
            if (e.data && e.data.table_doc_url) {
              window.location.href = G.getBaseUrl() + e.data.table_doc_url;
            }
          },
          onGridReady: function (params) {
            gridApi = params.api;
            dropdownEngine.populate();
            updateStats();
            handleResponsive();
          },
        });
      })
      .catch(function (err) {
        console.error("catalog-columns.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    G.bindStandardEvents({
      gridId: "catalog-grid",
      dropdownEngine: dropdownEngine,
      filterEngine: filterEngine,
      gridApi: function () { return gridApi; },
      extraBind: function () {
        window.addEventListener("resize", G.debounce(handleResponsive, 150));
      }
    });
  }

  G.mkDocsReady("catalog-grid", initGrid, bindEvents);
})();
