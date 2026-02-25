---
title: STADIUM
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Public</span>
  </div>
  <div class="dict-hero-title">STADIUM</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gyear, stadium</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">487</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">3</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">연 1회</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">데이터 관리자</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gyear, stadium</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 — Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">데이터 관리자 (R-01)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">연 1회 (시즌 전)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">전 시스템</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Public</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[기준 데이터](../products/master-codes.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">3개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gyear</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">char(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">연도</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">stadium</span></td><td><span class="col-std">stadium_cd</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">구장 코드</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">stadium_key</span></td><td><span class="col-std"></span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">3개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>gyear</code><span class="code-desc"> — 연도</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>stadium</code><span class="code-desc"> — 구장 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>Àá½Ç</td><td>45</td></tr>
<tr><td>ÇÑ¹ç</td><td>43</td></tr>
<tr><td>»çÁ÷</td><td>41</td></tr>
<tr><td>Ã»ÁÖ</td><td>39</td></tr>
<tr><td>½Ã¹Î</td><td>34</td></tr>
<tr><td>¸¶»ê</td><td>33</td></tr>
<tr><td>¹«µî</td><td>32</td></tr>
<tr><td>¼ö¿ø</td><td>30</td></tr>
<tr><td>¹®ÇÐ</td><td>25</td></tr>
<tr><td>ÀÎÃµ</td><td>22</td></tr>
<tr><td>±¤ÁÖ</td><td>19</td></tr>
<tr><td>ÀüÁÖ</td><td>17</td></tr>
<tr><td>±º»ê</td><td>15</td></tr>
<tr><td>Æ÷Ç×</td><td>13</td></tr>
<tr><td>¿ï»ê</td><td>11</td></tr>
<tr><td>´ë±¸</td><td>11</td></tr>
<tr><td>°íÃ´</td><td>11</td></tr>
<tr><td>¸ñµ¿</td><td>8</td></tr>
<tr><td>Ã¢¿ø</td><td>8</td></tr>
<tr><td>±¸´ö</td><td>7</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>stadium_key</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>JS</td><td>45</td></tr>
<tr><td>DJ</td><td>43</td></tr>
<tr><td>SJ</td><td>41</td></tr>
<tr><td>CJ</td><td>39</td></tr>
<tr><td>DG</td><td>34</td></tr>
<tr><td>MS</td><td>33</td></tr>
<tr><td>KJ</td><td>31</td></tr>
<tr><td>SW</td><td>30</td></tr>
<tr><td>MH</td><td>25</td></tr>
<tr><td>IC</td><td>21</td></tr>
<tr><td>JJ</td><td>19</td></tr>
<tr><td>KS</td><td>14</td></tr>
<tr><td>KC</td><td>13</td></tr>
<tr><td>PH</td><td>13</td></tr>
<tr><td>GC</td><td>11</td></tr>
<tr><td>DK</td><td>11</td></tr>
<tr><td>UL</td><td>11</td></tr>
<tr><td>CW</td><td>8</td></tr>
<tr><td>MD</td><td>8</td></tr>
<tr><td>KD</td><td>7</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gyear</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>stadium</td><td>±¸´ö</td><td>µ¿´ë¹®</td><td>¸¶»ê</td></tr>
<tr><td>stadium_key</td><td>KD</td><td>DM</td><td>MS</td></tr>
</tbody></table>
</div>

</div>
