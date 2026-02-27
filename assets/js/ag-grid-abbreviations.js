/* AG Grid - 약어 사전 (standards-dict/abbreviations.md) */
(function () {
  "use strict";

  var G = window.AgGridCommon;
  var gridApi = null;
  var allRows = [];

  var DROPDOWN_FIELDS = ["category"];
  var DROPDOWN_IDS = { category: "sel-category" };
  var DROPDOWN_LABELS = { category: "분류" };

  var MONO = { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" };

  var COLUMN_DEFS = [
    { headerName: "분류", field: "category", width: 120, filter: false, pinned: "left" },
    { headerName: "약어", field: "abbreviation", width: 100, filter: "agTextColumnFilter", pinned: "left", cellStyle: Object.assign({ fontWeight: "600" }, MONO) },
    { headerName: "영문", field: "full_name_en", width: 200, filter: "agTextColumnFilter" },
    { headerName: "한글", field: "full_name_ko", width: 120, filter: "agTextColumnFilter" },
    { headerName: "레거시 컬럼", field: "legacy_columns", width: 180, filter: "agTextColumnFilter", cellStyle: MONO },
    { headerName: "표준명(안)", field: "std_name", width: 180, filter: "agTextColumnFilter", cellStyle: MONO },
    { headerName: "비고", field: "note", flex: 1, minWidth: 150, filter: "agTextColumnFilter", tooltipField: "note" },
  ];

  var filterEngine = G.createFilterEngine({
    dropdownFields: DROPDOWN_FIELDS,
    haystackFields: ["abbreviation", "full_name_en", "full_name_ko", "legacy_columns", "std_name"],
    searchableColumns: [
      { field: "abbreviation", label: "약어" },
      { field: "full_name_en", label: "영문" },
      { field: "full_name_ko", label: "한글" },
      { field: "legacy_columns", label: "레거시 컬럼" },
      { field: "std_name", label: "표준명(안)" }
    ]
  });

  var dropdownEngine = G.createDropdownEngine({
    filterEngine: filterEngine,
    allRows: function () { return allRows; },
    gridApi: function () { return gridApi; },
    dropdownFields: DROPDOWN_FIELDS,
    dropdownIds: DROPDOWN_IDS,
    dropdownLabels: DROPDOWN_LABELS,
    csvFileName: "KBO_약어_사전.csv"
  });

  /* ── Stats ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var cats = new Set();
    gridApi.forEachNodeAfterFilter(function (n) { if (n.data) cats.add(n.data.category); });
    G.setText("stat-abbr-total", displayed === total ? G.formatNumber(total) : G.formatNumber(displayed) + " / " + G.formatNumber(total));
    G.setText("stat-categories", cats.size);
    G.setText("status-count", G.formatNumber(displayed) + " / " + G.formatNumber(total) + "건");
  }

  function initGrid() {
    var gridDiv = document.getElementById("abbreviations-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(G.getBaseUrl() + "assets/data/abbreviations.json")
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
        console.error("abbreviations.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    G.bindStandardEvents({
      gridId: "abbreviations-grid",
      dropdownEngine: dropdownEngine,
      filterEngine: filterEngine,
      gridApi: function () { return gridApi; }
    });
  }

  G.mkDocsReady("abbreviations-grid", initGrid, bindEvents);
})();
