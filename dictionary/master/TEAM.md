---
title: TEAM
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-access">Public</span>
  </div>
  <div class="dict-hero-title">TEAM</div>
  <div class="dict-hero-sub">DB2_BASEBALL_2 &middot; PK: SEASON_ID, T_ID</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">401</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">7</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">연 1회</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">데이터 관리자</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_2_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>SEASON_ID, T_ID</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 - Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">데이터 관리자 (R-01)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">연 1회 (시즌 전)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">전 시스템</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Public</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[기준 데이터](../products/master-codes.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [코드 사전](../../standards-dict/codes.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">7개</span></div>

<div class="dict-encoding-warn">`GROUP_SC` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">2</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">T_ID</span></td><td><span class="col-std">team_id</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">팀 코드 (2자리)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">FIRST_NM</span></td><td><span class="col-std">first_nm</span></td><td><span class="col-type">varchar(50)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 한글명 앞부분 (모기업/지역)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">LAST_NM</span></td><td><span class="col-std">last_nm</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">팀 한글명 뒷부분 (마스코트)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">FIRST_ENG_NM</span></td><td><span class="col-std">first_eng_nm</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">팀 영문명 앞부분 (모기업/지역)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">LAST_ENG_NM</span></td><td><span class="col-std">last_eng_nm</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">팀 영문명 뒷부분 (마스코트)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">GROUP_SC</span></td><td><span class="col-std">group_sc</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">조 구분 코드 (DREAM=드림리그, MAGIC=매직리그)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">3개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>SEASON_ID</code><span class="code-desc"> &mdash; 시즌 ID</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>T_ID</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>SS</td><td>45</td></tr>
<tr><td>LT</td><td>45</td></tr>
<tr><td>LG</td><td>45</td></tr>
<tr><td>OB</td><td>45</td></tr>
<tr><td>HT</td><td>45</td></tr>
<tr><td>HH</td><td>41</td></tr>
<tr><td>SK</td><td>27</td></tr>
<tr><td>HD</td><td>26</td></tr>
<tr><td>WO</td><td>19</td></tr>
<tr><td>WE</td><td>14</td></tr>
<tr><td>EA</td><td>14</td></tr>
<tr><td>NC</td><td>14</td></tr>
<tr><td>KT</td><td>12</td></tr>
<tr><td>SB</td><td>9</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>GROUP_SC</code><span class="code-desc"> &mdash; 조 구분 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>ALLSTAR</td><td>28</td></tr>
<tr><td>MAGIC</td><td>8</td></tr>
<tr><td>DREAM</td><td>8</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>SEASON_ID</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>T_ID</td><td>HD</td><td>HT</td><td>LG</td></tr>
<tr><td>FIRST_NM</td><td>»ï¹Ì</td><td>ÇØÅÂ</td><td>MBC</td></tr>
<tr><td>LAST_NM</td><td>½´ÆÛ½ºÅ¸Áî</td><td>Å¸ÀÌ°ÅÁî</td><td>Ã»·æ</td></tr>
<tr><td>FIRST_ENG_NM</td><td>LOTTE</td><td>SAMSUNG</td><td>LOTTE</td></tr>
<tr><td>LAST_ENG_NM</td><td>GIANTS</td><td>LIONS</td><td>GIANTS</td></tr>
<tr><td>GROUP_SC</td><td>DREAM</td><td>MAGIC</td><td>DREAM</td></tr>
</tbody></table>
</div>

</div>
