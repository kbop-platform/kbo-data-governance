/* AG Grid - 용어 사전 (standards-dict/glossary.md) */
(function () {
  "use strict";

  var G = window.AgGridCommon;
  var gridApi = null;
  var allRows = [];

  var DROPDOWN_FIELDS = ["category"];
  var DROPDOWN_IDS = { category: "sel-category" };
  var DROPDOWN_LABELS = { category: "분류" };

  var COLUMN_DEFS = [
    { headerName: "분류", field: "category", width: 130, filter: false, pinned: "left" },
    { headerName: "용어", field: "term_ko", width: 120, filter: "agTextColumnFilter", pinned: "left", cellStyle: { fontWeight: "600" } },
    { headerName: "영문", field: "term_en", width: 180, filter: "agTextColumnFilter" },
    { headerName: "약어", field: "abbreviation", width: 70, filter: "agTextColumnFilter", cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "정의", field: "definition", flex: 2, minWidth: 250, filter: "agTextColumnFilter", tooltipField: "definition" },
    { headerName: "DB 컬럼", field: "db_column", width: 180, filter: "agTextColumnFilter", cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "관련 테이블", field: "related_tables", width: 160, filter: "agTextColumnFilter" },
  ];

  var filterEngine = G.createFilterEngine({
    dropdownFields: DROPDOWN_FIELDS,
    haystackFields: ["term_ko", "term_en", "definition", "db_column"],
    searchableColumns: [
      { field: "term_ko", label: "용어" },
      { field: "term_en", label: "영문" },
      { field: "definition", label: "정의" },
      { field: "db_column", label: "DB 컬럼" }
    ]
  });

  var dropdownEngine = G.createDropdownEngine({
    filterEngine: filterEngine,
    allRows: function () { return allRows; },
    gridApi: function () { return gridApi; },
    dropdownFields: DROPDOWN_FIELDS,
    dropdownIds: DROPDOWN_IDS,
    dropdownLabels: DROPDOWN_LABELS,
    csvFileName: "KBO_용어사전.csv"
  });

  /* ── Stats ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var cats = new Set();
    gridApi.forEachNodeAfterFilter(function (n) { if (n.data) cats.add(n.data.category); });
    G.setText("stat-terms", displayed === total ? G.formatNumber(total) : G.formatNumber(displayed) + " / " + G.formatNumber(total));
    G.setText("stat-categories", cats.size);
    G.setText("status-count", G.formatNumber(displayed) + " / " + G.formatNumber(total) + "건");
  }

  function initGrid() {
    var gridDiv = document.getElementById("glossary-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(G.getBaseUrl() + "assets/data/glossary-terms.json")
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
        console.error("glossary-terms.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    G.bindStandardEvents({
      gridId: "glossary-grid",
      dropdownEngine: dropdownEngine,
      filterEngine: filterEngine,
      gridApi: function () { return gridApi; }
    });
  }

  G.mkDocsReady("glossary-grid", initGrid, bindEvents);
})();
