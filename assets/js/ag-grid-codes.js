/* AG Grid - 코드 사전 (standards-dict/codes.md) */
(function () {
  "use strict";

  var G = window.AgGridCommon;
  var gridApi = null;
  var allRows = [];

  var DROPDOWN_FIELDS = ["code_group"];
  var DROPDOWN_IDS = { code_group: "sel-code-group" };
  var DROPDOWN_LABELS = { code_group: "코드그룹" };

  var COLUMN_DEFS = [
    { headerName: "코드그룹", field: "code_group", width: 150, filter: false, pinned: "left",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "코드", field: "code", width: 80, filter: false, pinned: "left",
      cellStyle: { fontWeight: "600", fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "한글", field: "name_ko", width: 160, filter: "agTextColumnFilter" },
    { headerName: "영문", field: "name_en", width: 180, filter: "agTextColumnFilter" },
    { headerName: "분류", field: "subcategory", width: 120, filter: false },
    { headerName: "건수", field: "count", width: 90, filter: false,
      cellStyle: { textAlign: "right", fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "사용 테이블", field: "used_tables", width: 200, filter: "agTextColumnFilter",
      tooltipField: "used_tables" },
    { headerName: "비고", field: "note", flex: 1, minWidth: 140, filter: false, tooltipField: "note" },
  ];

  var filterEngine = G.createFilterEngine({
    dropdownFields: DROPDOWN_FIELDS,
    haystackFields: ["code_group", "code", "name_ko", "name_en", "subcategory", "used_tables", "note"],
    searchableColumns: [
      { field: "code_group", label: "코드그룹" },
      { field: "code", label: "코드" },
      { field: "name_ko", label: "한글" },
      { field: "name_en", label: "영문" },
      { field: "used_tables", label: "사용 테이블" }
    ]
  });

  var dropdownEngine = G.createDropdownEngine({
    filterEngine: filterEngine,
    allRows: function () { return allRows; },
    gridApi: function () { return gridApi; },
    dropdownFields: DROPDOWN_FIELDS,
    dropdownIds: DROPDOWN_IDS,
    dropdownLabels: DROPDOWN_LABELS,
    csvFileName: "KBO_코드사전.csv"
  });

  /* ── Stats ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var groups = new Set();
    gridApi.forEachNodeAfterFilter(function (n) { if (n.data) groups.add(n.data.code_group); });
    G.setText("stat-codes-total", displayed === total ? G.formatNumber(total) : G.formatNumber(displayed) + " / " + G.formatNumber(total));
    G.setText("stat-code-groups", groups.size);
    G.setText("status-count", G.formatNumber(displayed) + " / " + G.formatNumber(total) + "건");
  }

  function initGrid() {
    var gridDiv = document.getElementById("codes-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(G.getBaseUrl() + "assets/data/code-dictionary.json")
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
        console.error("code-dictionary.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    G.bindStandardEvents({
      gridId: "codes-grid",
      dropdownEngine: dropdownEngine,
      filterEngine: filterEngine,
      gridApi: function () { return gridApi; }
    });
  }

  G.mkDocsReady("codes-grid", initGrid, bindEvents);
})();
