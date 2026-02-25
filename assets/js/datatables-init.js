/* DataTables 자동 초기화 — MkDocs Material instant-loading 대응 */
document$.subscribe(function () {
  // AG Grid 페이지에서는 DataTables 초기화 스킵
  if (document.querySelector(".ag-grid-page")) return;

  var tables = document.querySelectorAll(".md-typeset table");
  tables.forEach(function (table) {
    // 이미 초기화된 테이블 스킵
    if ($.fn.dataTable.isDataTable(table)) return;

    // 행 5개 미만이면 스킵 (thead 제외)
    var bodyRows = table.querySelectorAll("tbody tr");
    if (bodyRows.length < 5) return;

    $(table).DataTable({
      pageLength: 25,
      lengthMenu: [10, 25, 50, 100],
      ordering: true,
      searching: true,
      paging: true,
      info: true,
      autoWidth: false,
      language: {
        search: "",
        searchPlaceholder: "테이블 검색...",
        lengthMenu: "_MENU_ 행 표시",
        info: "_TOTAL_건 중 _START_-_END_",
        infoEmpty: "데이터 없음",
        infoFiltered: "(전체 _MAX_건에서 필터)",
        zeroRecords: "일치하는 항목 없음",
        paginate: {
          first: "처음",
          last: "마지막",
          next: "다음",
          previous: "이전",
        },
      },
    });
  });
});
