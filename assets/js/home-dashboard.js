/* === KBO DataHub - Home Dashboard (dynamic) === */
(function () {
  'use strict';

  var DATA_FILES = {
    instances:  'assets/data/catalog-instances.json',
    columns:    'assets/data/catalog-columns.json',
    tables:     'assets/data/dictionary-tables.json',
    glossary:   'assets/data/glossary-terms.json',
    codes:      'assets/data/code-dictionary.json',
    domains:    'assets/data/domain-types.json'
  };

  /* ── helpers ── */

  function getBaseUrl() {
    var scripts = document.getElementsByTagName('script');
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].src || '';
      var idx = src.indexOf('assets/js/home-dashboard.js');
      if (idx !== -1) return src.substring(0, idx);
    }
    return './';
  }

  function fmt(n) {
    if (n >= 1e6) return (n / 1e6).toFixed(1).replace(/\.0$/, '') + 'M';
    if (n >= 1e3) return n.toLocaleString('en-US');
    return String(n);
  }

  /* ── data fetch ── */

  function fetchAll(base) {
    var keys = Object.keys(DATA_FILES);
    var promises = keys.map(function (k) {
      return fetch(base + DATA_FILES[k])
        .then(function (r) { return r.json(); })
        .catch(function () { return { rows: [] }; });
    });
    return Promise.all(promises).then(function (results) {
      var out = {};
      keys.forEach(function (k, i) { out[k] = results[i]; });
      return out;
    });
  }

  /* ── compute stats ── */

  function computeStats(data) {
    var inst = data.instances.rows || [];
    var cols = data.columns.rows || [];
    var tbls = data.tables.rows || [];
    var gloss = data.glossary.rows || [];
    var codes = data.codes.rows || [];
    var doms = data.domains.rows || [];

    var dbSet = {};
    inst.forEach(function (r) { dbSet[r.db_name] = 1; });
    var dbCount = Object.keys(dbSet).length;

    var totalRows = 0;
    inst.forEach(function (r) { totalRows += (r.row_count || 0); });

    var generated = data.tables.generated || data.instances.generated || '';

    return {
      dbCount: dbCount,
      tableCount: tbls.length,
      columnCount: cols.length,
      totalRows: totalRows,
      instanceCount: inst.length,
      glossaryCount: gloss.length,
      codeCount: codes.length,
      domainTypeCount: doms.length,
      generated: generated
    };
  }

  /* ── render hero stats ── */

  function renderHero(stats) {
    var el = document.getElementById('hero-stats');
    if (!el) return;

    var date = stats.generated || new Date().toISOString().slice(0, 10);

    var items = [
      { num: fmt(stats.dbCount),       label: '데이터베이스' },
      { num: fmt(stats.tableCount),    label: '테이블' },
      { num: fmt(stats.columnCount),   label: '컬럼' },
      { num: fmt(stats.totalRows),     label: '총 행수' },
      { num: fmt(stats.instanceCount), label: '인스턴스' }
    ];

    var html = items.map(function (it) {
      return '<div class="home-hero-stat">'
        + '<div class="stat-num">' + it.num + '</div>'
        + '<div class="stat-label">' + it.label + '</div>'
        + '</div>';
    }).join('');

    html += '<div class="home-hero-stat home-hero-stat--date">'
      + '<div class="stat-num">' + date + '</div>'
      + '<div class="stat-label">갱신일자</div>'
      + '</div>';

    el.innerHTML = html;
  }

  /* ── card tag counts ── */

  function renderCardCounts(stats) {
    var map = {
      'tag-instances':    fmt(stats.instanceCount) + ' 인스턴스',
      'tag-columns':      fmt(stats.columnCount) + ' 컬럼',
      'tag-glossary':     fmt(stats.glossaryCount) + ' 용어',
      'tag-tables':       fmt(stats.tableCount) + '종 테이블',
      'tag-codes':        fmt(stats.codeCount) + ' 코드',
      'tag-domain-types': fmt(stats.domainTypeCount) + ' 도메인'
    };
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.textContent = map[id];
    });
  }

  /* ── init ── */

  function init() {
    var root = document.getElementById('home-dashboard');
    if (!root) return;

    var base = getBaseUrl();
    fetchAll(base).then(function (data) {
      var stats = computeStats(data);
      renderHero(stats);
      renderCardCounts(stats);
    });
  }

  /* MkDocs Material instant loading compatible */
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { init(); });
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
