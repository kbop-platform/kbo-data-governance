/* AG Grid — 인스턴스 현황 (catalog/instances.md)
   외부 필터 API (isExternalFilterPresent + doesExternalFilterPass) 사용
   캐스케이딩 드롭다운: db_type, league, domain, schema_gen, table_name (5개) */
(function () {
  "use strict";

  var gridApi = null;
  var allRows = [];

  /* ── 외부 필터 상태 ── */
  var extFilter = {
    db_type: "",
    league: "",
    domain: "",
    schema_gen: "",
    table_name: "",
    search: "",
  };

  /* ── 드롭다운 필드 목록 (순서 = 캐스케이딩 우선순위) ── */
  var DROPDOWN_FIELDS = ["db_type", "league", "domain", "schema_gen", "table_name"];
  var DROPDOWN_IDS = {
    db_type: "sel-db_type",
    league: "sel-league",
    domain: "sel-domain",
    schema_gen: "sel-schema_gen",
    table_name: "sel-table_name",
  };
  var DROPDOWN_LABELS = {
    db_type: "DB타입",
    league: "리그",
    domain: "도메인",
    schema_gen: "세대",
    table_name: "테이블",
  };

  /* ── 세대 라벨 매핑 ── */
  var GEN_LABELS = {
    legacy: "구세대",
    new: "신세대",
    unknown: "미분류",
  };

  /* ── 갱신 주기 배지 CSS 클래스 매핑 ── */
  var REFRESH_CLASSES = {
    "실시간": "cell-refresh-realtime",
    "경기 당일": "cell-refresh-gameday",
    "경기당일": "cell-refresh-gameday",
    "D+1": "cell-refresh-d1",
    "시즌": "cell-refresh-season",
    "시즌 초": "cell-refresh-season",
    "연 1회": "cell-refresh-yearly",
    "연1회": "cell-refresh-yearly",
    "비정기": "cell-refresh-yearly",
  };

  var COLUMN_DEFS = [
    {
      headerName: "DB명",
      field: "db_name",
      width: 220,
      filter: false,
      pinned: "left",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    {
      headerName: "DB타입",
      field: "db_type",
      width: 70,
      filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var cls = p.value === "DB1" ? "cell-badge-db1" : "cell-badge-db2";
        return '<span class="' + cls + '">' + p.value + "</span>";
      },
    },
    {
      headerName: "리그",
      field: "league",
      width: 90,
      filter: false,
    },
    {
      headerName: "테이블 (물리명)",
      field: "table_name",
      width: 180,
      filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var url = p.data.table_doc_url;
        var style = "font-family:JetBrains Mono,monospace;font-weight:700;font-size:12px;";
        if (!url) return '<span style="' + style + '">' + p.value + "</span>";
        return (
          '<a href="' + getBaseUrl() + url +
          '" style="' + style + 'color:var(--kbo-accent,#4A7BF7);text-decoration:none">' +
          p.value + "</a>"
        );
      },
    },
    {
      headerName: "표준명(안)",
      field: "table_std_name",
      width: 160,
      filter: false,
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "11px", color: "#888" },
    },
    {
      headerName: "도메인",
      field: "domain",
      width: 90,
      filter: false,
    },
    {
      headerName: "세대",
      field: "schema_gen",
      width: 80,
      filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var cls = p.value === "legacy" ? "cell-badge-legacy"
                : p.value === "new" ? "cell-badge-new" : "cell-badge-unknown";
        var label = GEN_LABELS[p.value] || p.value;
        return '<span class="' + cls + '">' + label + "</span>";
      },
    },
    {
      headerName: "PK",
      field: "pk_columns",
      width: 160,
      filter: false,
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "11px" },
      tooltipField: "pk_columns",
    },
    {
      headerName: "컬럼수",
      field: "column_count",
      width: 75,
      filter: "agNumberColumnFilter",
    },
    {
      headerName: "행수",
      field: "row_count",
      width: 110,
      filter: "agNumberColumnFilter",
      valueFormatter: function (p) {
        return p.value != null ? p.value.toLocaleString("ko-KR") : "";
      },
    },
    {
      headerName: "갱신 주기",
      field: "refresh",
      width: 90,
      filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var cls = REFRESH_CLASSES[p.value] || "cell-refresh-yearly";
        return '<span class="' + cls + '">' + p.value + "</span>";
      },
    },
    {
      headerName: "티어",
      field: "tier",
      width: 70,
      filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var cls = p.value === "Tier 1" ? "cell-tier-1"
                : p.value === "Tier 2" ? "cell-tier-2" : "cell-tier-3";
        return '<span class="' + cls + '">' + p.value.replace("Tier ", "T") + "</span>";
      },
    },
    {
      headerName: "오너",
      field: "owner",
      width: 110,
      filter: false,
    },
    {
      headerName: "설명",
      field: "description",
      flex: 1,
      minWidth: 150,
      filter: false,
      tooltipField: "description",
      cellStyle: { fontSize: "12px" },
    },
  ];

  /* ── 유틸리티 ── */
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

  function formatNumber(n) {
    return n != null ? n.toLocaleString("ko-KR") : "0";
  }

  function setText(id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = val;
  }

  /* ── 검색 haystack 생성 ── */
  function buildHaystack(d) {
    return (
      (d.db_name || "") + " " +
      (d.table_name || "") + " " +
      (d.table_std_name || "") + " " +
      (d.domain || "") + " " +
      (d.league || "") + " " +
      (d.owner || "") + " " +
      (d.tier || "") + " " +
      (d.pk_columns || "") + " " +
      (d.description || "")
    ).toLowerCase();
  }

  /* ── 외부 필터 API ── */
  function isExternalFilterPresent() {
    return extFilter.db_type !== "" ||
           extFilter.league !== "" ||
           extFilter.domain !== "" ||
           extFilter.schema_gen !== "" ||
           extFilter.table_name !== "" ||
           extFilter.search !== "";
  }

  function doesExternalFilterPass(node) {
    var d = node.data;
    if (!d) return false;
    if (extFilter.db_type && d.db_type !== extFilter.db_type) return false;
    if (extFilter.league && d.league !== extFilter.league) return false;
    if (extFilter.domain && d.domain !== extFilter.domain) return false;
    if (extFilter.schema_gen && d.schema_gen !== extFilter.schema_gen) return false;
    if (extFilter.table_name && d.table_name !== extFilter.table_name) return false;
    if (extFilter.search) {
      var q = extFilter.search.toLowerCase();
      if (buildHaystack(d).indexOf(q) === -1) return false;
    }
    return true;
  }

  /* ── 캐스케이딩 드롭다운 옵션 갱신 ── */
  function updateCascadingDropdowns() {
    DROPDOWN_FIELDS.forEach(function (targetField) {
      var validValues = new Set();
      allRows.forEach(function (row) {
        var pass = true;
        if (extFilter.search) {
          var q = extFilter.search.toLowerCase();
          if (buildHaystack(row).indexOf(q) === -1) pass = false;
        }
        if (pass) {
          DROPDOWN_FIELDS.forEach(function (f) {
            if (f !== targetField && extFilter[f] && row[f] !== extFilter[f]) {
              pass = false;
            }
          });
        }
        if (pass && row[targetField]) {
          validValues.add(row[targetField]);
        }
      });

      var sel = document.getElementById(DROPDOWN_IDS[targetField]);
      if (!sel) return;

      var currentVal = sel.value;
      while (sel.options.length > 1) sel.remove(1);
      Array.from(validValues).sort().forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v;
        opt.textContent = targetField === "schema_gen" ? (GEN_LABELS[v] || v) : v;
        sel.appendChild(opt);
      });

      if (validValues.has(currentVal)) {
        sel.value = currentVal;
      } else {
        sel.value = "";
        extFilter[targetField] = "";
      }
    });
  }

  /* ── 드롭다운 변경 핸들러 ── */
  function onDropdownChange() {
    DROPDOWN_FIELDS.forEach(function (f) {
      var sel = document.getElementById(DROPDOWN_IDS[f]);
      extFilter[f] = sel ? sel.value : "";
    });
    updateCascadingDropdowns();
    if (gridApi) gridApi.onFilterChanged();
  }

  /* ── 검색 ── */
  function onSearchInput(e) {
    extFilter.search = e.target.value.trim();
    updateCascadingDropdowns();
    if (gridApi) gridApi.onFilterChanged();
  }

  /* ── 초기화 ── */
  function resetAllFilters() {
    extFilter.db_type = "";
    extFilter.league = "";
    extFilter.domain = "";
    extFilter.schema_gen = "";
    extFilter.table_name = "";
    extFilter.search = "";
    var si = document.getElementById("grid-search");
    if (si) si.value = "";
    if (gridApi) gridApi.setFilterModel(null);
    updateCascadingDropdowns();
    if (gridApi) gridApi.onFilterChanged();
  }

  /* ── Stats Cards ── */
  function updateStats() {
    if (!gridApi) return;
    var displayed = gridApi.getDisplayedRowCount();
    var total = allRows.length;
    var tables = new Set();
    var dbs = new Set();
    var totalRowCount = 0;

    gridApi.forEachNodeAfterFilter(function (node) {
      var d = node.data;
      if (!d) return;
      tables.add(d.table_name_ci);
      dbs.add(d.db_name);
      totalRowCount += d.row_count || 0;
    });

    setText("stat-instances", displayed === total ? formatNumber(total) : formatNumber(displayed) + " / " + formatNumber(total));
    setText("stat-tables", tables.size);
    setText("stat-dbs", dbs.size);
    setText("stat-rows", (totalRowCount / 1e6).toFixed(1) + "M");
    setText("status-count", formatNumber(displayed) + " / " + formatNumber(total) + "건");
    setText("status-tables", tables.size + " 테이블");
    setText("status-dbs", dbs.size + " DB");
  }

  /* ── Filter Chips ── */
  function renderChips() {
    var container = document.getElementById("filter-chips");
    if (!container) return;
    container.innerHTML = "";

    var hasAny = false;
    DROPDOWN_FIELDS.forEach(function (f) {
      if (!extFilter[f]) return;
      hasAny = true;
      var chip = document.createElement("span");
      chip.className = "chip";
      var displayVal = f === "schema_gen" ? (GEN_LABELS[extFilter[f]] || extFilter[f]) : extFilter[f];
      chip.innerHTML =
        '<span class="chip-label">' + DROPDOWN_LABELS[f] + ": " + displayVal + "</span>" +
        '<span class="chip-close" data-field="' + f + '">&times;</span>';
      container.appendChild(chip);
    });

    if (hasAny) {
      var clearAll = document.createElement("button");
      clearAll.className = "chip-clear-all";
      clearAll.textContent = "모두 지우기";
      clearAll.addEventListener("click", resetAllFilters);
      container.appendChild(clearAll);

      container.querySelectorAll(".chip-close").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var f = this.dataset.field;
          extFilter[f] = "";
          var sel = document.getElementById(DROPDOWN_IDS[f]);
          if (sel) sel.value = "";
          updateCascadingDropdowns();
          if (gridApi) gridApi.onFilterChanged();
        });
      });
    }
  }

  /* ── CSV ── */
  function exportCsv() {
    if (!gridApi) return;
    gridApi.exportDataAsCsv({
      fileName: "KBO_인스턴스_현황.csv",
      processCellCallback: function (p) { return p.value; },
    });
  }

  /* ── 반응형 ── */
  function handleResponsive() {
    if (!gridApi) return;
    var w = window.innerWidth;
    var narrow = w < 1200;
    var veryNarrow = w < 900;
    gridApi.setColumnsVisible(["owner", "column_count", "description", "table_std_name"], !narrow);
    gridApi.setColumnsVisible(["pk_columns", "refresh", "schema_gen"], !veryNarrow);
  }

  /* ── 빈 상태 ── */
  var NO_ROWS =
    '<div style="padding:40px;text-align:center">' +
    '<div style="font-size:14px;color:#888;margin-bottom:12px">일치하는 항목이 없습니다</div>' +
    '<button onclick="document.getElementById(\'btn-reset\').click()" ' +
    'style="padding:6px 16px;border:1px solid #ddd;border-radius:6px;background:#fff;cursor:pointer;font-size:12px">필터 초기화</button></div>';

  /* ── 초기 드롭다운 채우기 ── */
  function populateDropdowns() {
    DROPDOWN_FIELDS.forEach(function (f) {
      var sel = document.getElementById(DROPDOWN_IDS[f]);
      if (!sel) return;
      var vals = new Set();
      allRows.forEach(function (r) { if (r[f]) vals.add(r[f]); });
      Array.from(vals).sort().forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v;
        opt.textContent = f === "schema_gen" ? (GEN_LABELS[v] || v) : v;
        sel.appendChild(opt);
      });
    });
  }

  /* ── 메인 ── */
  function initGrid() {
    var gridDiv = document.getElementById("instance-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(getBaseUrl() + "assets/data/catalog-instances.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        allRows = data.rows || [];

        agGrid.createGrid(gridDiv, {
          columnDefs: COLUMN_DEFS,
          rowData: allRows,
          defaultColDef: {
            sortable: true,
            resizable: true,
            suppressMovable: true,
          },
          animateRows: true,
          enableCellTextSelection: true,
          tooltipShowDelay: 300,
          overlayNoRowsTemplate: NO_ROWS,
          isExternalFilterPresent: isExternalFilterPresent,
          doesExternalFilterPass: doesExternalFilterPass,
          onFilterChanged: function () {
            updateStats();
            renderChips();
          },
          onRowDoubleClicked: function (e) {
            if (e.data && e.data.table_doc_url) {
              window.location.href = getBaseUrl() + e.data.table_doc_url;
            }
          },
          onGridReady: function (params) {
            gridApi = params.api;
            populateDropdowns();
            updateStats();
            handleResponsive();
          },
        });
      })
      .catch(function (err) {
        console.error("catalog-instances.json 로드 실패:", err);
        gridDiv.innerHTML =
          '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  /* ── 이벤트 바인딩 ── */
  function bindEvents() {
    var si = document.getElementById("grid-search");
    if (si) si.addEventListener("input", debounce(onSearchInput, 200));

    document.querySelectorAll(".grid-filter-bar select[data-field]").forEach(function (sel) {
      sel.addEventListener("change", onDropdownChange);
    });

    var br = document.getElementById("btn-reset");
    if (br) br.addEventListener("click", resetAllFilters);

    var bc = document.getElementById("btn-csv");
    if (bc) bc.addEventListener("click", exportCsv);

    document.addEventListener("keydown", function (e) {
      if (!document.getElementById("instance-grid")) return;
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
          if (gridApi) gridApi.onFilterChanged();
        }
      }
    });

    window.addEventListener("resize", debounce(handleResponsive, 150));
  }

  /* ── MkDocs Material instant loading ── */
  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      if (document.getElementById("instance-grid")) { initGrid(); bindEvents(); }
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      if (document.getElementById("instance-grid")) { initGrid(); bindEvents(); }
    });
  }
})();
