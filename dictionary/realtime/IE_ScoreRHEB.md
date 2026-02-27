---
title: IE_ScoreRHEB
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">실시간</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">IE_ScoreRHEB</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gameID, GYEAR, bHome</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">30,860</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">7</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">실시간</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">S2i 운영</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gameID, GYEAR, bHome</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 - Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">S2i 운영 (R-06)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">실시간 (&lt; 5초)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀, 앱 서비스</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[실시간 경기](../products/live-game.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">7개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gameID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">Run</span></td><td><span class="col-std">run</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">Hit</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">Error</span></td><td><span class="col-std">err</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실책</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">BallFour</span></td><td><span class="col-std">ball_four_if</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷 여부</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">bHome</span></td><td><span class="col-std">home_if</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">홈팀 여부 (1=홈, 0=원정)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">6개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Run</code><span class="code-desc"> &mdash; 득점</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Hit</code><span class="code-desc"> &mdash; 안타</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>Error</code><span class="code-desc"> &mdash; 실책</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>15,978</td></tr>
<tr><td>1</td><td>10,087</td></tr>
<tr><td>2</td><td>3,584</td></tr>
<tr><td>3</td><td>939</td></tr>
<tr><td>4</td><td>225</td></tr>
<tr><td>5</td><td>39</td></tr>
<tr><td>6</td><td>7</td></tr>
<tr><td>8</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>BallFour</code><span class="code-desc"> &mdash; 볼넷 여부</span></summary>
<div class="code-ref">고유값 17종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>bHome</code><span class="code-desc"> &mdash; 홈팀 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>15,430</td></tr>
<tr><td>0</td><td>15,430</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gameID</td><td>20040313HDHH0</td><td>20040313HDHH0</td><td>20040313LGSS0</td></tr>
<tr><td>GYEAR</td><td>2004</td><td>2004</td><td>2004</td></tr>
<tr><td>Run</td><td>6</td><td>4</td><td>7</td></tr>
<tr><td>Hit</td><td>10</td><td>6</td><td>13</td></tr>
<tr><td>Error</td><td>0</td><td>2</td><td>0</td></tr>
<tr><td>BallFour</td><td>10</td><td>4</td><td>5</td></tr>
<tr><td>bHome</td><td>0</td><td>1</td><td>0</td></tr>
</tbody></table>
</div>

</div>
