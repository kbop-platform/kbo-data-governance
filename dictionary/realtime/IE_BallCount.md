---
title: IE_BallCount
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">실시간</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">IE_BallCount</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gameID, GYEAR</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">15,482</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">11</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">실시간</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">S2i 운영</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gameID, GYEAR</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 — Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">S2i 운영 (R-06)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">실시간 (&lt; 5초)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀, 앱 서비스</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[실시간 경기](../products/live-game.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">11개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gameID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (GMKEY와 동일 형식)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">strike</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">ball</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">out</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">base1</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">base2</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">base3</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">pitcher</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">batter</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">batResult</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(50)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">9개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> — 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>strike</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>5,621</td></tr>
<tr><td>3</td><td>3,883</td></tr>
<tr><td>2</td><td>3,207</td></tr>
<tr><td>1</td><td>2,771</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>ball</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>6,701</td></tr>
<tr><td>1</td><td>4,272</td></tr>
<tr><td>2</td><td>2,996</td></tr>
<tr><td>3</td><td>1,513</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>out</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>3</td><td>12,327</td></tr>
<tr><td>0</td><td>2,253</td></tr>
<tr><td>2</td><td>462</td></tr>
<tr><td>1</td><td>440</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>base1</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>9,616</td></tr>
<tr><td>6</td><td>693</td></tr>
<tr><td>8</td><td>674</td></tr>
<tr><td>7</td><td>656</td></tr>
<tr><td>9</td><td>649</td></tr>
<tr><td>1</td><td>647</td></tr>
<tr><td>5</td><td>641</td></tr>
<tr><td>3</td><td>638</td></tr>
<tr><td>2</td><td>635</td></tr>
<tr><td>4</td><td>631</td></tr>
<tr><td>13</td><td>1</td></tr>
<tr><td>12</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>base2</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>11,185</td></tr>
<tr><td>1</td><td>538</td></tr>
<tr><td>6</td><td>511</td></tr>
<tr><td>4</td><td>495</td></tr>
<tr><td>8</td><td>494</td></tr>
<tr><td>7</td><td>484</td></tr>
<tr><td>3</td><td>468</td></tr>
<tr><td>5</td><td>463</td></tr>
<tr><td>2</td><td>431</td></tr>
<tr><td>9</td><td>412</td></tr>
<tr><td>11</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>base3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>13,080</td></tr>
<tr><td>5</td><td>291</td></tr>
<tr><td>6</td><td>289</td></tr>
<tr><td>4</td><td>274</td></tr>
<tr><td>1</td><td>271</td></tr>
<tr><td>7</td><td>268</td></tr>
<tr><td>8</td><td>266</td></tr>
<tr><td>3</td><td>257</td></tr>
<tr><td>2</td><td>250</td></tr>
<tr><td>9</td><td>235</td></tr>
<tr><td>19</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>pitcher</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>batter</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gameID</td><td>20040310LTSS0</td><td>20040313HDHH0</td><td>20040313LGSS0</td></tr>
<tr><td>GYEAR</td><td>2004</td><td>2004</td><td>2004</td></tr>
<tr><td>strike</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>ball</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>out</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>base1</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>base2</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>base3</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>pitcher</td><td>94526</td><td>96720</td><td>93453</td></tr>
<tr><td>batter</td><td>94539</td><td>98742</td><td>93112</td></tr>
<tr><td>batResult</td><td>-</td><td>4±¸|»ïÁø</td><td>»ïÁø</td></tr>
</tbody></table>
</div>

</div>
