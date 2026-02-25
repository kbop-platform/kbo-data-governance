/* AG Grid — 도메인 사전 (catalog/domains.md)
   실제 컬럼 데이터 기반 1:1 도메인 매핑 (suffix + physical_type) */
(function () {
  "use strict";

  var gridApi = null;
  var allRows = [];

  var extFilter = { suffix: "", gap: "", search: "" };

  var COLUMN_DEFS = [
    { headerName: "접미사", field: "suffix", width: 90, filter: false, pinned: "left",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px", fontWeight: "600" } },
    { headerName: "분류", field: "label", width: 80, filter: false, pinned: "left" },
    { headerName: "물리타입", field: "physical_type", width: 130, filter: "agTextColumnFilter",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" } },
    { headerName: "컬럼수", field: "column_count", width: 90, filter: false,
      sort: "desc",
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
    return extFilter.suffix !== "" || extFilter.gap !== "" || extFilter.search !== "";
  }

  function doesExternalFilterPass(node) {
    var d = node.data;
    if (!d) return false;
    if (extFilter.suffix && d.suffix !== extFilter.suffix) return false;
    if (extFilter.gap && d.gap !== extFilter.gap) return false;
    if (extFilter.search) {
      var q = extFilter.search.toLowerCase();
      var hay = ((d.suffix || "") + " " + (d.label || "") + " " + (d.physical_type || "") +
        " " + (d.example_columns || "") + " " + (d.std_target || "") +
        " " + (d.gap || "") + " " + (d.domain_id || "")).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    return true;
  }

  /* -- 캐스케이딩 드롭다운 -- */
  function buildHaystack(r) {
    return ((r.suffix || "") + " " + (r.label || "") + " " + (r.physical_type || "") +
      " " + (r.example_columns || "") + " " + (r.std_target || "") +
      " " + (r.gap || "") + " " + (r.domain_id || "")).toLowerCase();
  }

  function updateCascadingDropdowns() {
    var selSuffix = document.getElementById("sel-suffix");
    var selGap = document.getElementById("sel-gap");

    var validSuffixes = new Set();
    var validGaps = new Set();

    allRows.forEach(function (r) {
      var pass = true;
      if (extFilter.search) {
        if (buildHaystack(r).indexOf(extFilter.search.toLowerCase()) === -1) pass = false;
      }
      if (pass && extFilter.gap && r.gap !== extFilter.gap) pass = false;
      if (pass) validSuffixes.add(r.suffix);

      pass = true;
      if (extFilter.search) {
        if (buildHaystack(r).indexOf(extFilter.search.toLowerCase()) === -1) pass = false;
      }
      if (pass && extFilter.suffix && r.suffix !== extFilter.suffix) pass = false;
      if (pass) validGaps.add(r.gap);
    });

    updateSelectOptions(selSuffix, validSuffixes, extFilter.suffix);
    updateSelectOptions(selGap, validGaps, extFilter.gap);
  }

  function updateSelectOptions(sel, validSet, currentVal) {
    if (!sel) return;
    var opts = sel.querySelectorAll("option");
    for (var i = 1; i < opts.length; i++) {
      var v = opts[i].value;
      opts[i].disabled = !validSet.has(v);
      opts[i].style.color = validSet.has(v) ? "" : "#ccc";
    }
    if (currentVal && !validSet.has(currentVal)) {
      sel.value = "";
      extFilter[sel.dataset.field] = "";
    }
  }

  function populateDropdowns() {
    var selSuffix = document.getElementById("sel-suffix");
    var selGap = document.getElementById("sel-gap");

    if (selSuffix) {
      var suffixes = [];
      var seen = {};
      allRows.forEach(function (r) {
        if (!seen[r.suffix]) { seen[r.suffix] = true; suffixes.push(r.suffix); }
      });
      suffixes.sort();
      suffixes.forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v; opt.textContent = v;
        selSuffix.appendChild(opt);
      });
    }

    if (selGap) {
      ["일치", "전환 필요"].forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v; opt.textContent = v;
        selGap.appendChild(opt);
      });
    }
  }

  function onDropdownChange(e) {
    var field = e.target.dataset.field;
    if (field) extFilter[field] = e.target.value;
    updateCascadingDropdowns();
    updateChips();
    if (gridApi) gridApi.onFilterChanged();
  }

  function onSearchInput(e) {
    extFilter.search = e.target.value.trim();
    updateCascadingDropdowns();
    updateChips();
    if (gridApi) gridApi.onFilterChanged();
  }

  /* -- Filter Chips -- */
  function updateChips() {
    var box = document.getElementById("filter-chips");
    if (!box) return;
    var html = "";
    if (extFilter.suffix) html += '<span class="chip">접미사: ' + extFilter.suffix + ' <button data-field="suffix">&times;</button></span>';
    if (extFilter.gap) html += '<span class="chip">GAP: ' + extFilter.gap + ' <button data-field="gap">&times;</button></span>';
    if (extFilter.search) html += '<span class="chip">검색: ' + extFilter.search + ' <button data-field="search">&times;</button></span>';
    box.innerHTML = html;
    box.querySelectorAll("button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var f = this.dataset.field;
        extFilter[f] = "";
        if (f === "search") { var si = document.getElementById("grid-search"); if (si) si.value = ""; }
        else {
          var sel = document.querySelector('select[data-field="' + f + '"]');
          if (sel) sel.value = "";
        }
        updateCascadingDropdowns();
        updateChips();
        if (gridApi) gridApi.onFilterChanged();
      });
    });
  }

  function resetAll() {
    extFilter.suffix = "";
    extFilter.gap = "";
    extFilter.search = "";
    var si = document.getElementById("grid-search");
    if (si) si.value = "";
    document.querySelectorAll(".grid-filter-bar select").forEach(function (s) { s.value = ""; });
    updateCascadingDropdowns();
    updateChips();
    if (gridApi) gridApi.setFilterModel(null);
    if (gridApi) gridApi.onFilterChanged();
  }

  /* -- Stats -- */
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
    setText("stat-domains-total", displayed === total ? formatNumber(total) : formatNumber(displayed) + " / " + formatNumber(total));
    setText("stat-columns-covered", formatNumber(totalCols));
    setText("stat-suffixes", "11");
    setText("stat-match-rate", displayed > 0 ? Math.round(matchCount / displayed * 100) + "%" : "0%");
    setText("status-count", formatNumber(displayed) + " / " + formatNumber(total) + "건");
  }

  function exportCsv() {
    if (!gridApi) return;
    gridApi.exportDataAsCsv({ fileName: "KBO_도메인사전.csv", processCellCallback: function (p) { return p.value; } });
  }

  var NO_ROWS =
    '<div style="padding:40px;text-align:center">' +
    '<div style="font-size:14px;color:#888;margin-bottom:12px">일치하는 항목이 없습니다</div>' +
    '<button onclick="document.getElementById(\'btn-reset\').click()" style="padding:6px 16px;border:1px solid #ddd;border-radius:6px;background:#fff;cursor:pointer;font-size:12px">필터 초기화</button></div>';

  function initGrid() {
    var gridDiv = document.getElementById("domain-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(getBaseUrl() + "assets/data/domain-types.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        allRows = data.rows || [];
        populateDropdowns();

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
          onFilterChanged: function () { updateStats(); },
          onGridReady: function (p) { gridApi = p.api; updateStats(); },
        });
      })
      .catch(function (err) {
        console.error("domain-types.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    var si = document.getElementById("grid-search");
    if (si) si.addEventListener("input", debounce(onSearchInput, 200));
    var br = document.getElementById("btn-reset");
    if (br) br.addEventListener("click", resetAll);
    var bc = document.getElementById("btn-csv");
    if (bc) bc.addEventListener("click", exportCsv);

    document.querySelectorAll(".grid-filter-bar select").forEach(function (sel) {
      sel.addEventListener("change", onDropdownChange);
    });

    document.addEventListener("keydown", function (e) {
      if (!document.getElementById("domain-grid")) return;
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
          updateCascadingDropdowns();
          updateChips();
          if (gridApi) gridApi.onFilterChanged();
        }
      }
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      if (document.getElementById("domain-grid")) { initGrid(); bindEvents(); }
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      if (document.getElementById("domain-grid")) { initGrid(); bindEvents(); }
    });
  }
})();
