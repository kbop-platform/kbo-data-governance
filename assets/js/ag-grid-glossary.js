/* AG Grid — 용어 사전 (catalog/glossary.md)
   외부 필터 API + 캐스케이딩 드롭다운 */
(function () {
  "use strict";

  var gridApi = null;
  var allRows = [];

  var extFilter = { category: "", search: "" };

  var COLUMN_DEFS = [
    { headerName: "분류", field: "category", width: 130, filter: false, pinned: "left" },
    { headerName: "용어", field: "term_ko", width: 120, filter: "agTextColumnFilter", pinned: "left", cellStyle: { fontWeight: "600" } },
    { headerName: "영문", field: "term_en", width: 180, filter: "agTextColumnFilter" },
    { headerName: "약어", field: "abbreviation", width: 70, filter: "agTextColumnFilter", cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "정의", field: "definition", flex: 2, minWidth: 250, filter: "agTextColumnFilter", tooltipField: "definition" },
    { headerName: "DB 컬럼", field: "db_column", width: 180, filter: "agTextColumnFilter", cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "관련 테이블", field: "related_tables", width: 160, filter: "agTextColumnFilter" },
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

  /* ── 외부 필터 ── */
  function isExternalFilterPresent() {
    return extFilter.category !== "" || extFilter.search !== "";
  }

  function doesExternalFilterPass(node) {
    var d = node.data;
    if (!d) return false;
    if (extFilter.category && d.category !== extFilter.category) return false;
    if (extFilter.search) {
      var q = extFilter.search.toLowerCase();
      var hay = ((d.term_ko || "") + " " + (d.term_en || "") + " " + (d.definition || "") + " " + (d.db_column || "")).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    return true;
  }

  /* ── 캐스케이딩 ── */
  function updateCascadingDropdown() {
    var sel = document.getElementById("sel-category");
    if (!sel) return;
    var validValues = new Set();
    allRows.forEach(function (r) {
      var pass = true;
      if (extFilter.search) {
        var q = extFilter.search.toLowerCase();
        var hay = ((r.term_ko || "") + " " + (r.term_en || "") + " " + (r.definition || "") + " " + (r.db_column || "")).toLowerCase();
        if (hay.indexOf(q) === -1) pass = false;
      }
      if (pass && r.category) validValues.add(r.category);
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
    else { sel.value = ""; extFilter.category = ""; }
  }

  function onDropdownChange() {
    var sel = document.getElementById("sel-category");
    extFilter.category = sel ? sel.value : "";
    if (gridApi) gridApi.onFilterChanged();
  }

  function onSearchInput(e) {
    extFilter.search = e.target.value.trim();
    updateCascadingDropdown();
    if (gridApi) gridApi.onFilterChanged();
  }

  function resetAll() {
    extFilter.category = "";
    extFilter.search = "";
    var si = document.getElementById("grid-search");
    if (si) si.value = "";
    var sel = document.getElementById("sel-category");
    if (sel) sel.value = "";
    if (gridApi) gridApi.setFilterModel(null);
    updateCascadingDropdown();
    if (gridApi) gridApi.onFilterChanged();
  }

  /* ── Stats ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var cats = new Set();
    gridApi.forEachNodeAfterFilter(function (n) { if (n.data) cats.add(n.data.category); });
    setText("stat-terms", displayed === total ? formatNumber(total) : formatNumber(displayed) + " / " + formatNumber(total));
    setText("stat-categories", cats.size);
    setText("status-count", formatNumber(displayed) + " / " + formatNumber(total) + "건");
  }

  /* ── Chips ── */
  function renderChips() {
    var c = document.getElementById("filter-chips");
    if (!c) return;
    c.innerHTML = "";
    if (!extFilter.category) return;
    var chip = document.createElement("span");
    chip.className = "chip";
    chip.innerHTML = '<span class="chip-label">분류: ' + extFilter.category + '</span><span class="chip-close">&times;</span>';
    c.appendChild(chip);
    c.querySelector(".chip-close").addEventListener("click", function () {
      extFilter.category = "";
      var sel = document.getElementById("sel-category");
      if (sel) sel.value = "";
      if (gridApi) gridApi.onFilterChanged();
    });
  }

  function exportCsv() {
    if (!gridApi) return;
    gridApi.exportDataAsCsv({ fileName: "KBO_용어사전.csv", processCellCallback: function (p) { return p.value; } });
  }

  var NO_ROWS =
    '<div style="padding:40px;text-align:center">' +
    '<div style="font-size:14px;color:#888;margin-bottom:12px">일치하는 항목이 없습니다</div>' +
    '<button onclick="document.getElementById(\'btn-reset\').click()" style="padding:6px 16px;border:1px solid #ddd;border-radius:6px;background:#fff;cursor:pointer;font-size:12px">필터 초기화</button></div>';

  function initGrid() {
    var gridDiv = document.getElementById("glossary-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(getBaseUrl() + "assets/data/glossary-terms.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        allRows = data.rows || [];
        // 초기 드롭다운
        var sel = document.getElementById("sel-category");
        if (sel) {
          var cats = new Set();
          allRows.forEach(function (r) { if (r.category) cats.add(r.category); });
          Array.from(cats).sort().forEach(function (v) {
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
        console.error("glossary-terms.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    var si = document.getElementById("grid-search");
    if (si) si.addEventListener("input", debounce(onSearchInput, 200));
    var sc = document.getElementById("sel-category");
    if (sc) sc.addEventListener("change", onDropdownChange);
    var br = document.getElementById("btn-reset");
    if (br) br.addEventListener("click", resetAll);
    var bc = document.getElementById("btn-csv");
    if (bc) bc.addEventListener("click", exportCsv);

    document.addEventListener("keydown", function (e) {
      if (!document.getElementById("glossary-grid")) return;
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
      if (document.getElementById("glossary-grid")) { initGrid(); bindEvents(); }
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      if (document.getElementById("glossary-grid")) { initGrid(); bindEvents(); }
    });
  }
})();
