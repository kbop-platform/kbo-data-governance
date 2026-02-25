/* AG Grid — 컬럼 카탈로그 (catalog/columns.md)
   외부 필터 API (isExternalFilterPresent + doesExternalFilterPass) 사용
   캐스케이딩 드롭다운: 필터 선택 시 다른 드롭다운 옵션을 연동 갱신 */
(function () {
  "use strict";

  var gridApi = null;
  var allRows = [];

  /* ── 외부 필터 상태 ── */
  var extFilter = {
    domain: "",
    table_name: "",
    data_type: "",
    tier: "",
    owner: "",
    search: "",
  };

  /* ── 드롭다운 필드 목록 (순서 = 캐스케이딩 우선순위) ── */
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
      headerName: "도메인",
      field: "domain",
      width: 90,
      filter: false,
      pinned: "left",
    },
    {
      headerName: "테이블",
      field: "table_name",
      width: 140,
      filter: false,
      pinned: "left",
      cellRenderer: function (p) {
        if (!p.value) return "";
        var url = p.data.table_doc_url;
        var std = p.data.table_std_name;
        var tip = std ? std : "";
        return (
          '<a href="' + getBaseUrl() + url +
          '" title="' + tip +
          '" style="color:var(--kbo-accent,#4A7BF7);text-decoration:none">' +
          p.value + "</a>"
        );
      },
    },
    {
      headerName: "#",
      field: "ordinal",
      width: 50,
      filter: "agNumberColumnFilter",
      sort: "asc",
    },
    {
      headerName: "컬럼명",
      field: "column_name",
      width: 150,
      filter: "agTextColumnFilter",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    {
      headerName: "타입",
      field: "data_type",
      width: 85,
      filter: false,
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    {
      headerName: "길이",
      field: "max_length",
      width: 60,
      filter: "agNumberColumnFilter",
    },
    {
      headerName: "NULL",
      field: "is_nullable",
      width: 55,
      filter: false,
      cellRenderer: function (p) {
        return p.value === "NN" ? '<span class="cell-badge-nn">NN</span>' : "";
      },
    },
    {
      headerName: "PK",
      field: "is_pk",
      width: 50,
      filter: false,
      cellRenderer: function (p) {
        return p.value === "PK" ? '<span class="cell-badge-pk">PK</span>' : "";
      },
    },
    {
      headerName: "설명",
      field: "description",
      flex: 2,
      minWidth: 200,
      filter: "agTextColumnFilter",
      tooltipField: "description",
    },
    {
      headerName: "표준명(안)",
      field: "std_name",
      width: 150,
      filter: "agTextColumnFilter",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
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
      width: 100,
      filter: false,
    },
    {
      headerName: "행수",
      field: "row_count",
      width: 90,
      filter: "agNumberColumnFilter",
      valueFormatter: function (p) {
        return p.value != null ? p.value.toLocaleString("ko-KR") : "";
      },
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

  /* ── 외부 필터 API ── */
  function isExternalFilterPresent() {
    return extFilter.domain !== "" ||
           extFilter.table_name !== "" ||
           extFilter.data_type !== "" ||
           extFilter.tier !== "" ||
           extFilter.owner !== "" ||
           extFilter.search !== "";
  }

  function doesExternalFilterPass(node) {
    var d = node.data;
    if (!d) return false;
    if (extFilter.domain && d.domain !== extFilter.domain) return false;
    if (extFilter.table_name && d.table_name !== extFilter.table_name) return false;
    if (extFilter.data_type && d.data_type !== extFilter.data_type) return false;
    if (extFilter.tier && d.tier !== extFilter.tier) return false;
    if (extFilter.owner && d.owner !== extFilter.owner) return false;
    if (extFilter.search) {
      var q = extFilter.search.toLowerCase();
      var haystack = (
        (d.column_name || "") + " " +
        (d.description || "") + " " +
        (d.std_name || "") + " " +
        (d.table_name || "") + " " +
        (d.domain || "")
      ).toLowerCase();
      if (haystack.indexOf(q) === -1) return false;
    }
    return true;
  }

  /* ── 캐스케이딩 드롭다운 옵션 갱신 ── */
  function updateCascadingDropdowns() {
    /* 현재 필터 상태에서 각 드롭다운에 표시할 옵션 계산:
       자기 자신을 제외한 나머지 필터를 적용한 행 집합에서 옵션 추출 */
    DROPDOWN_FIELDS.forEach(function (targetField) {
      var validValues = new Set();
      allRows.forEach(function (row) {
        var pass = true;
        // 검색어 필터
        if (extFilter.search) {
          var q = extFilter.search.toLowerCase();
          var haystack = (
            (row.column_name || "") + " " + (row.description || "") + " " +
            (row.std_name || "") + " " + (row.table_name || "") + " " + (row.domain || "")
          ).toLowerCase();
          if (haystack.indexOf(q) === -1) pass = false;
        }
        // 다른 드롭다운 필터 적용 (자기 자신 제외)
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
      // 옵션 재구성
      while (sel.options.length > 1) sel.remove(1);
      Array.from(validValues).sort().forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v;
        opt.textContent = v;
        sel.appendChild(opt);
      });

      // 현재 선택값 복원 (유효하면)
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
    // 드롭다운에서 extFilter 동기화
    DROPDOWN_FIELDS.forEach(function (f) {
      var sel = document.getElementById(DROPDOWN_IDS[f]);
      extFilter[f] = sel ? sel.value : "";
    });
    // 캐스케이딩 갱신
    updateCascadingDropdowns();
    // 그리드 필터 트리거
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
    extFilter.domain = "";
    extFilter.table_name = "";
    extFilter.data_type = "";
    extFilter.tier = "";
    extFilter.owner = "";
    extFilter.search = "";
    var si = document.getElementById("grid-search");
    if (si) si.value = "";
    // 내장 컬럼 필터도 초기화
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

    setText("stat-columns", displayed === total ? formatNumber(total) : formatNumber(displayed) + " / " + formatNumber(total));
    setText("stat-tables", tables.size);
    setText("stat-domains", domains.size);
    setText("stat-rows", (totalRowCount / 1e6).toFixed(1) + "M");
    setText("stat-tier1", tier1);
    setText("status-count", formatNumber(displayed) + " / " + formatNumber(total) + "건");
    setText("status-tables", tables.size + " 테이블");
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
      chip.innerHTML =
        '<span class="chip-label">' + DROPDOWN_LABELS[f] + ": " + extFilter[f] + "</span>" +
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
      fileName: "KBO_컬럼_카탈로그.csv",
      processCellCallback: function (p) { return p.value; },
    });
  }

  /* ── 반응형 ── */
  function handleResponsive() {
    if (!gridApi) return;
    var narrow = window.innerWidth < 1200;
    gridApi.setColumnsVisible(["owner", "row_count"], !narrow);
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
        opt.textContent = v;
        sel.appendChild(opt);
      });
    });
  }

  /* ── 메인 ── */
  function initGrid() {
    var gridDiv = document.getElementById("catalog-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(getBaseUrl() + "assets/data/catalog-columns.json")
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
        console.error("catalog-columns.json 로드 실패:", err);
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
      if (!document.getElementById("catalog-grid")) return;
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
      if (document.getElementById("catalog-grid")) { initGrid(); bindEvents(); }
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      if (document.getElementById("catalog-grid")) { initGrid(); bindEvents(); }
    });
  }
})();
