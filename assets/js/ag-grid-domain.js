/* AG Grid - 도메인 사전 (standards-dict/domains.md)
   disable 모드 캐스케이딩 + 검색 칩 */
(function () {
  "use strict";

  var G = window.AgGridCommon;
  var gridApi = null;
  var allRows = [];

  var DROPDOWN_FIELDS = ["suffix", "gap"];
  var DROPDOWN_IDS = { suffix: "sel-suffix", gap: "sel-gap" };
  var DROPDOWN_LABELS = { suffix: "접미사", gap: "GAP" };

  var COLUMN_DEFS = [
    { headerName: "접미사", field: "suffix", width: 90, filter: false, pinned: "left",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px", fontWeight: "600" } },
    { headerName: "분류", field: "label", width: 80, filter: false, pinned: "left" },
    { headerName: "물리타입", field: "physical_type", width: 130, filter: "agTextColumnFilter",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "컬럼수", field: "column_count", width: 90, filter: false, sort: "desc",
      cellStyle: { textAlign: "right", fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "테이블수", field: "table_count", width: 90, filter: false,
      cellStyle: { textAlign: "right", fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "NULL%", field: "nullable_pct", width: 80, filter: false,
      cellStyle: { textAlign: "right", fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "PK%", field: "pk_pct", width: 80, filter: false,
      cellStyle: { textAlign: "right", fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "대표컬럼", field: "example_columns", width: 200, filter: "agTextColumnFilter",
      tooltipField: "example_columns",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "11px", color: "#666" } },
    { headerName: "표준목표", field: "std_target", width: 180, filter: false,
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px", color: "#1565c0" } },
    { headerName: "GAP", field: "gap", width: 100, filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var color = p.value === "일치" ? "#2e7d32" : "#c62828";
        var bg = p.value === "일치" ? "#e8f5e9" : "#fce4ec";
        return '<span style="display:inline-block;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600;color:' + color + ';background:' + bg + '">' + p.value + '</span>';
      }
    },
  ];

  var filterEngine = G.createFilterEngine({
    dropdownFields: DROPDOWN_FIELDS,
    haystackFn: function (d) {
      return ((d.suffix || "") + " " + (d.label || "") + " " + (d.physical_type || "") +
        " " + (d.example_columns || "") + " " + (d.std_target || "") +
        " " + (d.gap || "") + " " + (d.domain_id || "")).toLowerCase();
    },
    searchableColumns: [
      { field: "suffix", label: "접미사" },
      { field: "label", label: "분류" },
      { field: "physical_type", label: "물리타입" },
      { field: "example_columns", label: "대표컬럼" },
      { field: "std_target", label: "표준목표" }
    ]
  });

  var dropdownEngine = G.createDropdownEngine({
    filterEngine: filterEngine,
    allRows: function () { return allRows; },
    gridApi: function () { return gridApi; },
    dropdownFields: DROPDOWN_FIELDS,
    dropdownIds: DROPDOWN_IDS,
    dropdownLabels: DROPDOWN_LABELS,
    cascadeMode: "disable",
    fixedValues: { gap: ["일치", "전환 필요"] },
    includeSearchChip: true,
    csvFileName: "KBO_도메인사전.csv"
  });

  /* ── Stats ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var totalCols = 0;
    var matchCount = 0;
    for (var i = 0; i < displayed; i++) {
      var row = gridApi.getDisplayedRowAtIndex(i);
      if (row && row.data) {
        totalCols += row.data.column_count || 0;
        if (row.data.gap === "일치") matchCount++;
      }
    }
    G.setText("stat-domains-total", displayed === total ? G.formatNumber(total) : G.formatNumber(displayed) + " / " + G.formatNumber(total));
    G.setText("stat-columns-covered", G.formatNumber(totalCols));
    G.setText("stat-suffixes", "11");
    G.setText("stat-match-rate", displayed > 0 ? Math.round(matchCount / displayed * 100) + "%" : "0%");
    G.setText("status-count", G.formatNumber(displayed) + " / " + G.formatNumber(total) + "건");
  }

  function initGrid() {
    var gridDiv = document.getElementById("domain-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(G.getBaseUrl() + "assets/data/domain-types.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        allRows = data.rows || [];
        dropdownEngine.populate();

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
          onGridReady: function (p) { gridApi = p.api; updateStats(); },
        });
      })
      .catch(function (err) {
        console.error("domain-types.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    G.bindStandardEvents({
      gridId: "domain-grid",
      dropdownEngine: dropdownEngine,
      filterEngine: filterEngine,
      gridApi: function () { return gridApi; }
    });
  }

  G.mkDocsReady("domain-grid", initGrid, bindEvents);
})();
