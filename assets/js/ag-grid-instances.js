/* AG Grid - 인스턴스 현황 (catalog/instances.md) */
(function () {
  "use strict";

  var G = window.AgGridCommon;
  var gridApi = null;
  var allRows = [];

  var DROPDOWN_FIELDS = ["db_name", "db_type", "league", "domain", "tier", "table_name"];
  var DROPDOWN_IDS = {
    db_name: "sel-db_name",
    db_type: "sel-db_type",
    league: "sel-league",
    domain: "sel-domain",
    tier: "sel-tier",
    table_name: "sel-table_name",
  };
  var DROPDOWN_LABELS = {
    db_name: "DB명",
    db_type: "DB타입",
    league: "리그",
    domain: "도메인",
    tier: "티어",
    table_name: "테이블",
  };

  var COLUMN_DEFS = [
    {
      headerName: "DB명", field: "db_name", width: 220, filter: false, pinned: "left",
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "12px" },
    },
    { headerName: "DB타입", field: "db_type", width: 70, filter: false },
    { headerName: "리그", field: "league", width: 90, filter: false },
    {
      headerName: "테이블 (물리명)", field: "table_name", width: 180, filter: false,
      cellRenderer: function (p) {
        if (!p.value) return "";
        var url = p.data.table_doc_url;
        var style = "font-family:JetBrains Mono,monospace;font-weight:700;font-size:12px;";
        if (!url) return '<span style="' + style + '">' + p.value + "</span>";
        return '<a href="' + G.getBaseUrl() + url +
          '" style="' + style + 'color:var(--kbo-accent,#4A7BF7);text-decoration:none">' +
          p.value + "</a>";
      },
    },
{ headerName: "도메인", field: "domain", width: 90, filter: false },
    {
      headerName: "PK", field: "pk_columns", width: 160, filter: false,
      cellStyle: { fontFamily: "JetBrains Mono, monospace", fontSize: "11px" },
      tooltipField: "pk_columns",
    },
    { headerName: "컬럼수", field: "column_count", width: 75, filter: "agNumberColumnFilter" },
    {
      headerName: "행수", field: "row_count", width: 110, filter: "agNumberColumnFilter",
      valueFormatter: function (p) {
        return p.value != null ? p.value.toLocaleString("ko-KR") : "";
      },
    },
    {
      headerName: "티어", field: "tier", width: 70, filter: false,
      valueFormatter: function (p) { return p.value ? p.value.replace("Tier ", "T") : ""; },
    },
    { headerName: "오너", field: "owner", width: 110, filter: false },
    {
      headerName: "설명", field: "description", flex: 1, minWidth: 150, filter: false,
      tooltipField: "description", cellStyle: { fontSize: "12px" },
    },
  ];

  var filterEngine = G.createFilterEngine({
    dropdownFields: DROPDOWN_FIELDS,
    haystackFn: function (d) {
      return (
        (d.db_name || "") + " " + (d.table_name || "") + " " +
        (d.domain || "") + " " +
        (d.league || "") + " " + (d.owner || "") + " " +
        (d.tier || "") + " " + (d.pk_columns || "") + " " +
        (d.description || "")
      ).toLowerCase();
    },
    searchableColumns: [
      { field: "db_name", label: "DB명" },
      { field: "table_name", label: "테이블" },
      { field: "domain", label: "도메인" },
      { field: "pk_columns", label: "PK" },
      { field: "description", label: "설명" }
    ]
  });

  var dropdownEngine = G.createDropdownEngine({
    filterEngine: filterEngine,
    allRows: function () { return allRows; },
    gridApi: function () { return gridApi; },
    dropdownFields: DROPDOWN_FIELDS,
    dropdownIds: DROPDOWN_IDS,
    dropdownLabels: DROPDOWN_LABELS,
    csvFileName: "KBO_인스턴스_현황.csv"
  });

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

    G.setText("stat-instances", displayed === total ? G.formatNumber(total) : G.formatNumber(displayed) + " / " + G.formatNumber(total));
    G.setText("stat-tables", tables.size);
    G.setText("stat-dbs", dbs.size);
    G.setText("stat-rows", (totalRowCount / 1e6).toFixed(1) + "M");
    G.setText("status-count", G.formatNumber(displayed) + " / " + G.formatNumber(total) + "건");
    G.setText("status-tables", tables.size + " 테이블");
    G.setText("status-dbs", dbs.size + " DB");
  }

  /* ── 반응형 ── */
  function handleResponsive() {
    if (!gridApi) return;
    var w = window.innerWidth;
    var narrow = w < 1200;
    var veryNarrow = w < 900;
    gridApi.setColumnsVisible(["owner", "column_count", "description"], !narrow);
    gridApi.setColumnsVisible(["pk_columns"], !veryNarrow);
  }

  /* ══════════════════════════════════════
     사이드 패널 (로컬 유지)
     ══════════════════════════════════════ */
  var columnDataCache = null;
  var dictDataCache = null;

  function loadColumnData() {
    if (columnDataCache) return Promise.resolve(columnDataCache);
    return fetch(G.getBaseUrl() + "assets/data/catalog-columns.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        columnDataCache = data.rows || [];
        return columnDataCache;
      });
  }

  function loadDictData() {
    if (dictDataCache) return Promise.resolve(dictDataCache);
    return loadColumnData().then(function (cols) {
      var map = {};
      cols.forEach(function (c) {
        var key = c.table_name;
        if (!map[key]) map[key] = { table_name: key, columns: [] };
        map[key].columns.push({
          name: c.column_name,
          type: c.data_type,
          pk: c.is_pk === "PK" ? "PK" : "",
          desc: c.description || ""
        });
      });
      dictDataCache = Object.values(map);
      return dictDataCache;
    });
  }

  function escHtml(s) {
    if (!s) return "";
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function metaItem(label, value) {
    return '<div class="sp-meta-item"><div class="sp-meta-label">' + label + '</div><div class="sp-meta-value">' + escHtml(String(value)) + '</div></div>';
  }

  function createPanelDOM() {
    if (document.getElementById("sp-overlay")) return;

    var overlay = document.createElement("div");
    overlay.id = "sp-overlay";
    overlay.className = "side-panel-overlay";
    overlay.addEventListener("click", closePanel);

    var panel = document.createElement("div");
    panel.id = "sp-panel";
    panel.className = "side-panel";
    panel.innerHTML =
      '<div class="side-panel-header">' +
        '<div>' +
          '<div class="side-panel-header-title" id="sp-title"></div>' +
          '<div class="side-panel-header-sub" id="sp-subtitle"></div>' +
        '</div>' +
        '<button class="side-panel-close" id="sp-close">&times;</button>' +
      '</div>' +
      '<div class="side-panel-body" id="sp-body"></div>' +
      '<div class="side-panel-footer">' +
        '<a class="sp-link-detail" id="sp-detail-link" href="#">상세 보기 &rarr;</a>' +
        '<span class="sp-instance-count" id="sp-instance-count"></span>' +
      '</div>';

    document.body.appendChild(overlay);
    document.body.appendChild(panel);

    document.getElementById("sp-close").addEventListener("click", closePanel);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && panel.classList.contains("open")) {
        closePanel();
      }
    });

    /* 상세 보기 클릭 시 패널 닫고 이동 */
    document.getElementById("sp-detail-link").addEventListener("click", function () {
      closePanel();
    });

    /* bfcache 복원 시 패널 닫기 (뒤로가기) */
    window.addEventListener("pageshow", function (e) {
      if (e.persisted) closePanel();
    });
  }

  function openPanel(rowData) {
    createPanelDOM();
    var overlay = document.getElementById("sp-overlay");
    var panel = document.getElementById("sp-panel");

    document.getElementById("sp-title").textContent = rowData.table_name;
    document.getElementById("sp-subtitle").textContent =
      rowData.domain + (rowData.tier ? " · " + rowData.tier : "");

    var detailLink = document.getElementById("sp-detail-link");
    if (rowData.table_doc_url) {
      detailLink.href = G.getBaseUrl() + rowData.table_doc_url;
      detailLink.style.display = "";
    } else {
      detailLink.style.display = "none";
    }

    var instanceCount = 0;
    allRows.forEach(function (r) {
      if (r.table_name_ci === rowData.table_name_ci) instanceCount++;
    });
    document.getElementById("sp-instance-count").textContent = instanceCount + "개 인스턴스";

    var body = document.getElementById("sp-body");
    var html = '<div class="sp-meta">';
    html += metaItem("도메인", rowData.domain);
    html += metaItem("티어", rowData.tier || "-");
    html += metaItem("오너", rowData.owner || "-");
    html += metaItem("컬럼 수", rowData.column_count || 0);
    html += metaItem("행 수", G.formatNumber(rowData.row_count || 0));
    html += metaItem("DB", rowData.db_name);
    if (rowData.pk_columns) {
      html += '<div class="sp-meta-item full"><div class="sp-meta-label">PK</div><div class="sp-meta-value mono">' + escHtml(rowData.pk_columns) + '</div></div>';
    }
    if (rowData.description) {
      html += '<div class="sp-meta-item full"><div class="sp-meta-label">설명</div><div class="sp-meta-value">' + escHtml(rowData.description) + '</div></div>';
    }
    html += '</div>';

    body.innerHTML = html + '<div class="sp-section"><div class="sp-section-title">컬럼 목록</div><div id="sp-col-loading" style="font-size:12px;color:#999;padding:8px 0">로딩 중...</div></div>';

    requestAnimationFrame(function () {
      overlay.classList.add("open");
      panel.classList.add("open");
    });

    loadDictData().then(function (dictRows) {
      var match = null;
      for (var i = 0; i < dictRows.length; i++) {
        if (dictRows[i].table_name.toLowerCase() === rowData.table_name.toLowerCase()) {
          match = dictRows[i];
          break;
        }
      }
      var colSection = body.querySelector(".sp-section");
      if (match && match.columns && match.columns.length > 0) {
        var tbl = '<table class="sp-columns-table"><thead><tr><th>컬럼명</th><th>타입</th><th>설명</th></tr></thead><tbody>';
        match.columns.forEach(function (c) {
          tbl += '<tr><td><span class="col-name">' + escHtml(c.name) + '</span>';
          if (c.pk === "PK") tbl += '<span class="col-pk">PK</span>';
          tbl += '</td><td><span class="col-type">' + escHtml(c.type) + '</span></td>';
          tbl += '<td><span class="col-desc">' + escHtml(c.desc || "") + '</span></td></tr>';
        });
        tbl += '</tbody></table>';
        colSection.innerHTML = '<div class="sp-section-title">컬럼 목록 (' + match.columns.length + ')</div>' + tbl;
      } else {
        colSection.innerHTML = '<div class="sp-section-title">컬럼 목록</div><div style="font-size:12px;color:#999;padding:4px 0">컬럼 정보 없음</div>';
      }
    });
  }

  function closePanel() {
    var overlay = document.getElementById("sp-overlay");
    var panel = document.getElementById("sp-panel");
    if (overlay) overlay.classList.remove("open");
    if (panel) panel.classList.remove("open");
  }

  /* ── 메인 ── */
  function initGrid() {
    var gridDiv = document.getElementById("instance-grid");
    if (!gridDiv || gridDiv.dataset.initialized === "true") return;
    gridDiv.dataset.initialized = "true";

    fetch(G.getBaseUrl() + "assets/data/catalog-instances.json")
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
          onRowClicked: function (e) {
            if (e.data) openPanel(e.data);
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
        console.error("catalog-instances.json 로드 실패:", err);
        gridDiv.innerHTML = '<div style="padding:40px;text-align:center;color:#c62828">데이터 로드 실패</div>';
      });
  }

  function bindEvents() {
    G.bindStandardEvents({
      gridId: "instance-grid",
      dropdownEngine: dropdownEngine,
      filterEngine: filterEngine,
      gridApi: function () { return gridApi; },
      extraBind: function () {
        window.addEventListener("resize", G.debounce(handleResponsive, 150));
      }
    });
  }

  G.mkDocsReady("instance-grid", initGrid, bindEvents);
})();
