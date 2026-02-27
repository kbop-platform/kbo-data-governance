/* AG Grid - 공통 유틸리티 + 팩토리
   5개 그리드 파일의 공유 로직을 추출.
   IIFE 패턴, ES5 호환, window.AgGridCommon 네임스페이스. */
(function () {
  "use strict";

  var AGC = {};

  /* ══════════════════════════════════════
     A. 순수 유틸리티
     ══════════════════════════════════════ */

  AGC.debounce = function (fn, ms) {
    var t;
    return function () {
      var a = arguments, c = this;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(c, a); }, ms);
    };
  };

  AGC.getBaseUrl = function () {
    var loc = window.location.pathname;
    var segments = ["/catalog/", "/dictionary/", "/standards-dict/"];
    var idx = -1;
    for (var i = 0; i < segments.length; i++) {
      idx = loc.indexOf(segments[i]);
      if (idx >= 0) break;
    }
    return idx >= 0 ? loc.substring(0, idx + 1) : "/";
  };

  AGC.formatNumber = function (n) {
    return n != null ? n.toLocaleString("ko-KR") : "0";
  };

  AGC.setText = function (id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = val;
  };

  AGC.NO_ROWS =
    '<div style="padding:40px;text-align:center">' +
    '<div style="font-size:14px;color:#888;margin-bottom:12px">일치하는 항목이 없습니다</div>' +
    '<button onclick="document.getElementById(\'btn-reset\').click()" ' +
    'style="padding:6px 16px;border:1px solid #ddd;border-radius:6px;background:#fff;cursor:pointer;font-size:12px">필터 초기화</button></div>';

  /* ══════════════════════════════════════
     B. createFilterEngine 팩토리
     ══════════════════════════════════════
     config = {
       dropdownFields: ["domain", "table_name", ...],
       haystackFields: ["column_name", "description", ...],
       haystackFn: null  // 선택: (row) → string
     }
     반환: { extFilter, isPresent, doesPass, resetAll }
  */
  AGC.createFilterEngine = function (config) {
    var dropdownFields = config.dropdownFields || [];
    var haystackFields = config.haystackFields || [];
    var haystackFn = config.haystackFn || null;
    var searchableColumns = config.searchableColumns || [];

    // extFilter 초기화: 각 드롭다운 필드 + search + searchScope
    var extFilter = { search: "", searchScope: "" };
    dropdownFields.forEach(function (f) { extFilter[f] = ""; });

    function buildHaystack(d) {
      // searchScope가 설정된 경우 해당 필드만 반환
      if (extFilter.searchScope) {
        return (d[extFilter.searchScope] || "").toString().toLowerCase();
      }
      if (haystackFn) return haystackFn(d);
      var parts = [];
      haystackFields.forEach(function (f) { parts.push(d[f] || ""); });
      return parts.join(" ").toLowerCase();
    }

    function isPresent() {
      if (extFilter.search !== "") return true;
      for (var i = 0; i < dropdownFields.length; i++) {
        if (extFilter[dropdownFields[i]] !== "") return true;
      }
      return false;
    }

    function doesPass(node) {
      var d = node.data;
      if (!d) return false;
      for (var i = 0; i < dropdownFields.length; i++) {
        var f = dropdownFields[i];
        if (extFilter[f] && d[f] !== extFilter[f]) return false;
      }
      if (extFilter.search) {
        var q = extFilter.search.toLowerCase();
        var hay = buildHaystack(d);
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    }

    function resetAll() {
      extFilter.search = "";
      extFilter.searchScope = "";
      dropdownFields.forEach(function (f) { extFilter[f] = ""; });
    }

    return {
      extFilter: extFilter,
      isPresent: isPresent,
      doesPass: doesPass,
      resetAll: resetAll,
      buildHaystack: buildHaystack,
      searchableColumns: searchableColumns
    };
  };

  /* ══════════════════════════════════════
     C. createDropdownEngine 팩토리
     ══════════════════════════════════════
     config = {
       filterEngine: filterEngineInstance,
       allRows: function() { return allRows; },
       gridApi: function() { return gridApi; },
       dropdownFields: [...],
       dropdownIds: { field: "sel-id", ... },
       dropdownLabels: { field: "한글명", ... },
       displayTransforms: { field: { raw: "표시값" } },  // 선택
       cascadeMode: "rebuild" | "disable",
       fixedValues: { gap: ["일치", "전환 필요"] },               // 선택
       includeSearchChip: false,                                  // 선택
       csvFileName: "export.csv"
     }
  */
  AGC.createDropdownEngine = function (config) {
    var fe = config.filterEngine;
    var extFilter = fe.extFilter;
    var dropdownFields = config.dropdownFields || [];
    var dropdownIds = config.dropdownIds || {};
    var dropdownLabels = config.dropdownLabels || {};
    var displayTransforms = config.displayTransforms || {};
    var cascadeMode = config.cascadeMode || "rebuild";
    var fixedValues = config.fixedValues || {};
    var includeSearchChip = config.includeSearchChip || false;
    var csvFileName = config.csvFileName || "export.csv";

    function getDisplayText(field, value) {
      if (displayTransforms[field] && displayTransforms[field][value]) {
        return displayTransforms[field][value];
      }
      return value;
    }

    /* ── 초기 드롭다운 채우기 ── */
    function populate() {
      var rows = config.allRows();
      dropdownFields.forEach(function (f) {
        var sel = document.getElementById(dropdownIds[f]);
        if (!sel) return;
        if (fixedValues[f]) {
          fixedValues[f].forEach(function (v) {
            var opt = document.createElement("option");
            opt.value = v;
            opt.textContent = getDisplayText(f, v);
            sel.appendChild(opt);
          });
        } else {
          var vals = new Set();
          rows.forEach(function (r) { if (r[f]) vals.add(r[f]); });
          Array.from(vals).sort().forEach(function (v) {
            var opt = document.createElement("option");
            opt.value = v;
            opt.textContent = getDisplayText(f, v);
            sel.appendChild(opt);
          });
        }
      });

      // 검색 범위 셀렉트 옵션 채우기
      var scopeSel = document.getElementById("search-scope");
      var sCols = fe.searchableColumns || [];
      if (scopeSel && sCols.length > 0) {
        sCols.forEach(function (sc) {
          var opt = document.createElement("option");
          opt.value = sc.field;
          opt.textContent = sc.label;
          scopeSel.appendChild(opt);
        });
      }
    }

    /* ── 캐스케이딩 드롭다운 갱신 ── */
    function update() {
      var rows = config.allRows();
      dropdownFields.forEach(function (targetField) {
        if (fixedValues[targetField]) {
          // 고정 옵션 필드는 disable 방식으로 처리
          _updateDisable(targetField, rows);
          return;
        }
        if (cascadeMode === "disable") {
          _updateDisable(targetField, rows);
        } else {
          _updateRebuild(targetField, rows);
        }
      });
    }

    function _getValidValues(targetField, rows) {
      var validValues = new Set();
      rows.forEach(function (row) {
        var pass = true;
        if (extFilter.search) {
          var q = extFilter.search.toLowerCase();
          if (fe.buildHaystack(row).indexOf(q) === -1) pass = false;
        }
        if (pass) {
          dropdownFields.forEach(function (f) {
            if (f !== targetField && extFilter[f] && row[f] !== extFilter[f]) {
              pass = false;
            }
          });
        }
        if (pass && row[targetField]) {
          validValues.add(row[targetField]);
        }
      });
      return validValues;
    }

    function _updateRebuild(targetField, rows) {
      var sel = document.getElementById(dropdownIds[targetField]);
      if (!sel) return;
      var validValues = _getValidValues(targetField, rows);
      var currentVal = sel.value;
      while (sel.options.length > 1) sel.remove(1);
      Array.from(validValues).sort().forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v;
        opt.textContent = getDisplayText(targetField, v);
        sel.appendChild(opt);
      });
      if (validValues.has(currentVal)) {
        sel.value = currentVal;
      } else {
        sel.value = "";
        extFilter[targetField] = "";
      }
    }

    function _updateDisable(targetField, rows) {
      var sel = document.getElementById(dropdownIds[targetField]);
      if (!sel) return;
      var validValues = _getValidValues(targetField, rows);
      var opts = sel.querySelectorAll("option");
      for (var i = 1; i < opts.length; i++) {
        var v = opts[i].value;
        opts[i].disabled = !validValues.has(v);
        opts[i].style.color = validValues.has(v) ? "" : "#ccc";
      }
      var currentVal = sel.value;
      if (currentVal && !validValues.has(currentVal)) {
        sel.value = "";
        extFilter[targetField] = "";
      }
    }

    /* ── 드롭다운 변경 ── */
    function onChange() {
      dropdownFields.forEach(function (f) {
        var sel = document.getElementById(dropdownIds[f]);
        extFilter[f] = sel ? sel.value : "";
      });
      update();
      renderChips();
      var api = config.gridApi();
      if (api) api.onFilterChanged();
    }

    /* ── 검색 입력 ── */
    function onSearch(e) {
      extFilter.search = e.target.value.trim();
      var scopeSel = document.getElementById("search-scope");
      if (scopeSel) extFilter.searchScope = scopeSel.value;
      update();
      renderChips();
      var api = config.gridApi();
      if (api) api.onFilterChanged();
    }

    /* ── 초기화 ── */
    function reset() {
      fe.resetAll();
      var si = document.getElementById("grid-search");
      if (si) {
        si.value = "";
        si.placeholder = "검색... (Ctrl+F)";
      }
      var scopeSel = document.getElementById("search-scope");
      if (scopeSel) scopeSel.value = "";
      dropdownFields.forEach(function (f) {
        var sel = document.getElementById(dropdownIds[f]);
        if (sel) sel.value = "";
      });
      var api = config.gridApi();
      if (api) api.setFilterModel(null);
      update();
      renderChips();
      if (api) api.onFilterChanged();
    }

    /* ── Filter Chips ── */
    function renderChips() {
      var container = document.getElementById("filter-chips");
      if (!container) return;
      container.innerHTML = "";

      var hasAny = false;
      dropdownFields.forEach(function (f) {
        if (!extFilter[f]) return;
        hasAny = true;
        var chip = document.createElement("span");
        chip.className = "chip";
        var displayVal = getDisplayText(f, extFilter[f]);
        chip.innerHTML =
          '<span class="chip-label">' + dropdownLabels[f] + ": " + displayVal + "</span>" +
          '<span class="chip-close" data-field="' + f + '">&times;</span>';
        container.appendChild(chip);
      });

      if (extFilter.search && (includeSearchChip || extFilter.searchScope)) {
        hasAny = true;
        var scopeLabel = "검색";
        if (extFilter.searchScope) {
          var sCols = fe.searchableColumns || [];
          for (var si = 0; si < sCols.length; si++) {
            if (sCols[si].field === extFilter.searchScope) {
              scopeLabel = sCols[si].label;
              break;
            }
          }
        }
        var sChip = document.createElement("span");
        sChip.className = "chip";
        sChip.innerHTML =
          '<span class="chip-label">' + scopeLabel + ": " + extFilter.search + "</span>" +
          '<span class="chip-close" data-field="search">&times;</span>';
        container.appendChild(sChip);
      }

      if (hasAny) {
        var clearAll = document.createElement("button");
        clearAll.className = "chip-clear-all";
        clearAll.textContent = "모두 지우기";
        clearAll.addEventListener("click", reset);
        container.appendChild(clearAll);

        container.querySelectorAll(".chip-close").forEach(function (btn) {
          btn.addEventListener("click", function () {
            var f = this.dataset.field;
            extFilter[f] = "";
            if (f === "search") {
              var si = document.getElementById("grid-search");
              if (si) si.value = "";
            } else {
              var sel = document.getElementById(dropdownIds[f]);
              if (sel) sel.value = "";
            }
            update();
            renderChips();
            var api = config.gridApi();
            if (api) api.onFilterChanged();
          });
        });
      }
    }

    /* ── CSV 내보내기 ── */
    function exportCsv() {
      var api = config.gridApi();
      if (!api) return;
      api.exportDataAsCsv({
        fileName: csvFileName,
        processCellCallback: function (p) { return p.value; }
      });
    }

    return {
      populate: populate,
      update: update,
      onChange: onChange,
      onSearch: onSearch,
      reset: reset,
      renderChips: renderChips,
      exportCsv: exportCsv
    };
  };

  /* ══════════════════════════════════════
     D. bindStandardEvents
     ══════════════════════════════════════
     config = {
       gridId: "catalog-grid",
       dropdownEngine: dropdownEngineInstance,
       filterEngine: filterEngineInstance,
       gridApi: function() { return gridApi; },
       searchId: "grid-search",
       resetId: "btn-reset",
       csvId: "btn-csv",
       extraBind: function() {}  // 선택: 추가 이벤트
     }
  */
  AGC.bindStandardEvents = function (config) {
    var de = config.dropdownEngine;
    var fe = config.filterEngine;
    var gridId = config.gridId;

    // 검색 입력
    var si = document.getElementById(config.searchId || "grid-search");
    if (si) si.addEventListener("input", AGC.debounce(de.onSearch, 200));

    // 검색 범위 셀렉트
    var scopeSel = document.getElementById("search-scope");
    if (scopeSel) {
      scopeSel.addEventListener("change", function () {
        fe.extFilter.searchScope = scopeSel.value;
        // placeholder 업데이트
        var searchInput = document.getElementById(config.searchId || "grid-search");
        if (searchInput) {
          if (scopeSel.value) {
            var label = scopeSel.options[scopeSel.selectedIndex].textContent;
            searchInput.placeholder = label + " 검색... (Ctrl+F)";
          } else {
            searchInput.placeholder = "검색... (Ctrl+F)";
          }
        }
        // 검색어가 있으면 필터 재적용
        if (fe.extFilter.search) {
          de.update();
          de.renderChips();
          var api = config.gridApi();
          if (api) api.onFilterChanged();
        }
      });
    }

    // 드롭다운 변경 - data-field 셀렉터 사용 (다중 드롭다운)
    document.querySelectorAll(".grid-filter-bar select[data-field]").forEach(function (sel) {
      sel.addEventListener("change", de.onChange);
    });

    // 단일 드롭다운 (data-field 없는 경우, search-scope 제외)
    document.querySelectorAll(".grid-filter-bar select:not([data-field]):not(#search-scope)").forEach(function (sel) {
      sel.addEventListener("change", de.onChange);
    });

    // 초기화
    var br = document.getElementById(config.resetId || "btn-reset");
    if (br) br.addEventListener("click", de.reset);

    // CSV
    var bc = document.getElementById(config.csvId || "btn-csv");
    if (bc) bc.addEventListener("click", de.exportCsv);

    // 키보드: Ctrl+F / Escape
    document.addEventListener("keydown", function (e) {
      if (!document.getElementById(gridId)) return;
      if ((e.ctrlKey || e.metaKey) && e.key === "f") {
        e.preventDefault();
        var s = document.getElementById(config.searchId || "grid-search");
        if (s) s.focus();
      }
      if (e.key === "Escape") {
        var s2 = document.getElementById(config.searchId || "grid-search");
        if (s2 && document.activeElement === s2) {
          s2.value = "";
          fe.extFilter.search = "";
          de.update();
          de.renderChips();
          var api = config.gridApi();
          if (api) api.onFilterChanged();
        }
      }
    });

    // 추가 바인딩
    if (config.extraBind) config.extraBind();
  };

  /* ══════════════════════════════════════
     E. mkDocsReady 헬퍼
     ══════════════════════════════════════ */
  AGC.mkDocsReady = function (gridId, initFn, bindFn) {
    function run() {
      if (document.getElementById(gridId)) { initFn(); bindFn(); }
    }
    if (typeof document$ !== "undefined") {
      document$.subscribe(run);
    } else {
      document.addEventListener("DOMContentLoaded", run);
    }
  };

  /* ── 네임스페이스 노출 ── */
  window.AgGridCommon = AGC;
})();
