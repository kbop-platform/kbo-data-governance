/* AG Grid — 코드 사전 (catalog/codes.md)
   외부 필터 API + 코드 그룹 드롭다운 */
(function () {
  "use strict";

  var gridApi = null;
  var allRows = [];

  var extFilter = { code_group: "", search: "" };

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

  function getBaseUrl() {
    var loc = window.location.pathname;
    var idx = loc.indexOf("/catalog/");
    return idx >= 0 ? loc.substring(0, idx + 1) : "/";
  }

  function debounce(fn, ms) {
    var t;
    return function () {
      var a = arguments, c = this;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(c, a); }, ms);
    };
  }

  function setText(id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = val;
  }

  function formatNumber(n) { return n != null ? n.toLocaleString("ko-KR") : "0"; }

  /* -- 외부 필터 -- */
  function isExternalFilterPresent() {
    return extFilter.code_group !== "" || extFilter.search !== "";
  }

  function doesExternalFilterPass(node) {
    var d = node.data;
    if (!d) return false;
    if (extFilter.code_group && d.code_group !== extFilter.code_group) return false;
    if (extFilter.search) {
      var q = extFilter.search.toLowerCase();
      var hay = ((d.code_group || "") + " " + (d.code || "") + " " + (d.name_ko || "") +
        " " + (d.name_en || "") + " " + (d.subcategory || "") + " " +
        (d.used_tables || "") + " " + (d.note || "")).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    return true;
  }

  /* -- 캐스케이딩 드롭다운 -- */
  function updateCascadingDropdown() {
    var sel = document.getElementById("sel-code-group");
    if (!sel) return;
    var validValues = new Set();
    allRows.forEach(function (r) {
      var pass = true;
      if (extFilter.search) {
        var q = extFilter.search.toLowerCase();
        var hay = ((r.code_group || "") + " " + (r.code || "") + " " + (r.name_ko || "") +
          " " + (r.name_en || "") + " " + (r.subcategory || "") +
          " " + (r.used_tables || "") + " " + (r.note || "")).toLowerCase();
        if (hay.indexOf(q) === -1) pass = false;
      }
      if (pass && r.code_group) validValues.add(r.code_group);
    });
    var cur = sel.value;
    while (sel.options.length > 1) sel.remove(1);
    Array.from(validValues).sort().forEach(function (v) {
      var opt = document.createElement("option");
      opt.value = v;
      opt.textContent = v;
      sel.appendChild(opt);
    });
    if (validValues.has(cur)) { sel.value = cur; }
    else { sel.value = ""; extFilter.code_group = ""; }
  }

  function onDropdownChange() {
    var sel = document.getElementById("sel-code-group");
    extFilter.code_group = sel ? sel.value : "";
    if (gridApi) gridApi.onFilterChanged();
  }

  function onSearchInput(e) {
    extFilter.search = e.target.value.trim();
    updateCascadingDropdown();
    if (gridApi) gridApi.onFilterChanged();
  }

  function resetAll() {
    extFilter.code_group = "";
    extFilter.search = "";
    var si = document.getElementById("grid-search");
    if (si) si.value = "";
    var sel = document.getElementById("sel-code-group");
    if (sel) sel.value = "";
    if (gridApi) gridApi.setFilterModel(null);
    updateCascadingDropdown();
    if (gridApi) gridApi.onFilterChanged();
  }

  /* -- Stats -- */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var groups = new Set();
    gridApi.forEachNodeAfterFilter(function (n) { if (n.data) groups.add(n.data.code_group); });
    setText("stat-codes-total", displayed === total ? formatNumber(total) : formatNumber(displayed) + " / " + formatNumber(total));
    setText("stat-code-groups", groups.size);
    setText("status-count", formatNumber(displayed) + " / " + formatNumber(total) + "건");
  }

  /* -- Chips -- */
  function renderChips() {
    var c = document.getElementById("filter-chips");
    if (!c) return;
    c.innerHTML = "";
    if (!extFilter.code_group) return;
    var chip = document.createElement("span");
    chip.className = "chip";
    chip.innerHTML = '<span class="chip-label">코드그룹: ' + extFilter.code_group + '</span><span class="chip-close">&times;</span>';
    c.appendChild(chip);
    c.querySelector(".chip-close").addEventListener("click", function () {
      extFilter.code_group = "";
      var sel = document.getElementById("sel-code-group");
      if (sel) sel.value = "";
      if (gridApi) gridApi.onFilterChanged();
    });
  }

  function exportCsv() {
    if (!gridApi) return;
    gridApi.exportDataAsCsv({ fileName: "KBO_코드사전.csv", processCellCallback: function (p) { return p.value; } });
  }

  var NO_ROWS =
    '<div style="padding:40px;text-align:center">' +
    '<div style="font-size:14px;color:#888;margin-bottom:12px">일치하는 항목이 없습니다</div>' +
    '<button onclick="document.getElementById(\'btn-reset\').click()" style="padding:6px 16px;border:1px solid #ddd;border-radius:6px;background:#fff;cursor:pointer;font-size:12px">필터 초기화</button></div>';

  function initGrid() {
    var gridDiv = document.getElementById("codes-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(getBaseUrl() + "assets/data/code-dictionary.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        allRows = data.rows || [];

        // 초기 드롭다운
        var sel = document.getElementById("sel-code-group");
        if (sel) {
          var groups = new Set();
          allRows.forEach(function (r) { if (r.code_group) groups.add(r.code_group); });
          Array.from(groups).sort().forEach(function (v) {
            var opt = document.createElement("option");
            opt.value = v;
            opt.textContent = v;
            sel.appendChild(opt);
          });
        }

        agGrid.createGrid(gridDiv, {
          columnDefs: COLUMN_DEFS,
          rowData: allRows,
          defaultColDef: { sortable: true, resizable: true, suppressMovable: true },
          animateRows: true,
          enableCellTextSelection: true,
          tooltipShowDelay: 300,
          overlayNoRowsTemplate: NO_ROWS,
          isExternalFilterPresent: isExternalFilterPresent,
          doesExternalFilterPass: doesExternalFilterPass,
          onFilterChanged: function () { updateStats(); renderChips(); },
          onGridReady: function (p) { gridApi = p.api; updateStats(); },
        });
      })
      .catch(function (err) {
        console.error("code-dictionary.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    var si = document.getElementById("grid-search");
    if (si) si.addEventListener("input", debounce(onSearchInput, 200));
    var sc = document.getElementById("sel-code-group");
    if (sc) sc.addEventListener("change", onDropdownChange);
    var br = document.getElementById("btn-reset");
    if (br) br.addEventListener("click", resetAll);
    var bc = document.getElementById("btn-csv");
    if (bc) bc.addEventListener("click", exportCsv);

    document.addEventListener("keydown", function (e) {
      if (!document.getElementById("codes-grid")) return;
      if ((e.ctrlKey || e.metaKey) && e.key === "f") {
        e.preventDefault();
        var s = document.getElementById("grid-search");
        if (s) s.focus();
      }
      if (e.key === "Escape") {
        var s2 = document.getElementById("grid-search");
        if (s2 && document.activeElement === s2) {
          s2.value = "";
          extFilter.search = "";
          updateCascadingDropdown();
          if (gridApi) gridApi.onFilterChanged();
        }
      }
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      if (document.getElementById("codes-grid")) { initGrid(); bindEvents(); }
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      if (document.getElementById("codes-grid")) { initGrid(); bindEvents(); }
    });
  }
})();
