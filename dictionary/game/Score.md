---
title: Score
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">Score</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GMKEY, GDAY</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">23,579</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">60</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 — Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">60개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">1T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">1B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">2T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">2B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">3T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">3B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">4T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">4B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">5T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">5B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">6T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">6B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">7T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">7B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">8T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">8B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">9T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">9B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">10T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">10B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">11T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">11B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">12T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">12B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">13T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">13B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">14T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">30</td><td><span class="col-name">14B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">31</td><td><span class="col-name">15T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">32</td><td><span class="col-name">15B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">33</td><td><span class="col-name">16T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">34</td><td><span class="col-name">16B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">35</td><td><span class="col-name">17T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">36</td><td><span class="col-name">17B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">37</td><td><span class="col-name">18T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">38</td><td><span class="col-name">18B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">39</td><td><span class="col-name">19T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">40</td><td><span class="col-name">19B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">41</td><td><span class="col-name">20T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">42</td><td><span class="col-name">20B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">43</td><td><span class="col-name">21T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">44</td><td><span class="col-name">21B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">45</td><td><span class="col-name">22T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">46</td><td><span class="col-name">22B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">47</td><td><span class="col-name">23T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">48</td><td><span class="col-name">23B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">49</td><td><span class="col-name">24T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">50</td><td><span class="col-name">24B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">51</td><td><span class="col-name">25T</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">52</td><td><span class="col-name">25B</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">53</td><td><span class="col-name">TPOINT</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">54</td><td><span class="col-name">BPOINT</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">55</td><td><span class="col-name">THIT</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">56</td><td><span class="col-name">BHIT</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">57</td><td><span class="col-name">TERR</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">58</td><td><span class="col-name">BERR</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">59</td><td><span class="col-name">TBBHP</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">60</td><td><span class="col-name">BBBHP</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">51개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> — 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>1T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,782</td></tr>
<tr><td>1</td><td>3,565</td></tr>
<tr><td>2</td><td>1,773</td></tr>
<tr><td>3</td><td>836</td></tr>
<tr><td>4</td><td>393</td></tr>
<tr><td>5</td><td>131</td></tr>
<tr><td>6</td><td>63</td></tr>
<tr><td>7</td><td>20</td></tr>
<tr><td>9</td><td>7</td></tr>
<tr><td>8</td><td>7</td></tr>
<tr><td>11</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>1B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>15,847</td></tr>
<tr><td>1</td><td>3,895</td></tr>
<tr><td>2</td><td>2,016</td></tr>
<tr><td>3</td><td>985</td></tr>
<tr><td>4</td><td>475</td></tr>
<tr><td>5</td><td>211</td></tr>
<tr><td>6</td><td>84</td></tr>
<tr><td>7</td><td>33</td></tr>
<tr><td>8</td><td>17</td></tr>
<tr><td>9</td><td>8</td></tr>
<tr><td>10</td><td>5</td></tr>
<tr><td>11</td><td>2</td></tr>
<tr><td>13</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>2T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>17,565</td></tr>
<tr><td>1</td><td>3,277</td></tr>
<tr><td>2</td><td>1,492</td></tr>
<tr><td>3</td><td>640</td></tr>
<tr><td>4</td><td>328</td></tr>
<tr><td>5</td><td>160</td></tr>
<tr><td>6</td><td>69</td></tr>
<tr><td>7</td><td>27</td></tr>
<tr><td>8</td><td>13</td></tr>
<tr><td>9</td><td>4</td></tr>
<tr><td>11</td><td>2</td></tr>
<tr><td>10</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>2B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>17,127</td></tr>
<tr><td>1</td><td>3,506</td></tr>
<tr><td>2</td><td>1,607</td></tr>
<tr><td>3</td><td>730</td></tr>
<tr><td>4</td><td>328</td></tr>
<tr><td>5</td><td>149</td></tr>
<tr><td>6</td><td>62</td></tr>
<tr><td>7</td><td>35</td></tr>
<tr><td>8</td><td>19</td></tr>
<tr><td>9</td><td>15</td></tr>
<tr><td>10</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>3T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,948</td></tr>
<tr><td>1</td><td>3,353</td></tr>
<tr><td>2</td><td>1,721</td></tr>
<tr><td>3</td><td>859</td></tr>
<tr><td>4</td><td>387</td></tr>
<tr><td>5</td><td>183</td></tr>
<tr><td>6</td><td>70</td></tr>
<tr><td>7</td><td>36</td></tr>
<tr><td>8</td><td>9</td></tr>
<tr><td>10</td><td>5</td></tr>
<tr><td>9</td><td>5</td></tr>
<tr><td>11</td><td>1</td></tr>
<tr><td>16</td><td>1</td></tr>
<tr><td>12</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>3B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,742</td></tr>
<tr><td>1</td><td>3,404</td></tr>
<tr><td>2</td><td>1,746</td></tr>
<tr><td>3</td><td>919</td></tr>
<tr><td>4</td><td>442</td></tr>
<tr><td>5</td><td>190</td></tr>
<tr><td>6</td><td>80</td></tr>
<tr><td>7</td><td>28</td></tr>
<tr><td>8</td><td>15</td></tr>
<tr><td>9</td><td>8</td></tr>
<tr><td>10</td><td>2</td></tr>
<tr><td>11</td><td>2</td></tr>
<tr><td>13</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>4T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,926</td></tr>
<tr><td>1</td><td>3,601</td></tr>
<tr><td>2</td><td>1,666</td></tr>
<tr><td>3</td><td>775</td></tr>
<tr><td>4</td><td>350</td></tr>
<tr><td>5</td><td>134</td></tr>
<tr><td>6</td><td>72</td></tr>
<tr><td>7</td><td>36</td></tr>
<tr><td>8</td><td>14</td></tr>
<tr><td>9</td><td>5</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>4B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,669</td></tr>
<tr><td>1</td><td>3,556</td></tr>
<tr><td>2</td><td>1,819</td></tr>
<tr><td>3</td><td>812</td></tr>
<tr><td>4</td><td>393</td></tr>
<tr><td>5</td><td>191</td></tr>
<tr><td>6</td><td>77</td></tr>
<tr><td>7</td><td>32</td></tr>
<tr><td>8</td><td>16</td></tr>
<tr><td>9</td><td>7</td></tr>
<tr><td>10</td><td>4</td></tr>
<tr><td>11</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>5T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>17,074</td></tr>
<tr><td>1</td><td>3,378</td></tr>
<tr><td>2</td><td>1,664</td></tr>
<tr><td>3</td><td>796</td></tr>
<tr><td>4</td><td>365</td></tr>
<tr><td>5</td><td>173</td></tr>
<tr><td>6</td><td>74</td></tr>
<tr><td>7</td><td>27</td></tr>
<tr><td>8</td><td>18</td></tr>
<tr><td>9</td><td>7</td></tr>
<tr><td>11</td><td>1</td></tr>
<tr><td>10</td><td>1</td></tr>
<tr><td>12</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>5B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,738</td></tr>
<tr><td>1</td><td>3,506</td></tr>
<tr><td>2</td><td>1,751</td></tr>
<tr><td>3</td><td>847</td></tr>
<tr><td>4</td><td>410</td></tr>
<tr><td>5</td><td>182</td></tr>
<tr><td>6</td><td>77</td></tr>
<tr><td>7</td><td>42</td></tr>
<tr><td>8</td><td>15</td></tr>
<tr><td>9</td><td>5</td></tr>
<tr><td>10</td><td>4</td></tr>
<tr><td>11</td><td>1</td></tr>
<tr><td>-1</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>6T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,920</td></tr>
<tr><td>1</td><td>3,569</td></tr>
<tr><td>2</td><td>1,682</td></tr>
<tr><td>3</td><td>780</td></tr>
<tr><td>4</td><td>338</td></tr>
<tr><td>5</td><td>150</td></tr>
<tr><td>6</td><td>70</td></tr>
<tr><td>-1</td><td>26</td></tr>
<tr><td>7</td><td>20</td></tr>
<tr><td>8</td><td>13</td></tr>
<tr><td>9</td><td>6</td></tr>
<tr><td>10</td><td>3</td></tr>
<tr><td>11</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>6B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,663</td></tr>
<tr><td>1</td><td>3,616</td></tr>
<tr><td>2</td><td>1,697</td></tr>
<tr><td>3</td><td>862</td></tr>
<tr><td>4</td><td>406</td></tr>
<tr><td>5</td><td>160</td></tr>
<tr><td>6</td><td>82</td></tr>
<tr><td>-1</td><td>42</td></tr>
<tr><td>7</td><td>32</td></tr>
<tr><td>8</td><td>11</td></tr>
<tr><td>10</td><td>6</td></tr>
<tr><td>11</td><td>1</td></tr>
<tr><td>9</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>7T</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 15종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>7B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,888</td></tr>
<tr><td>1</td><td>3,428</td></tr>
<tr><td>2</td><td>1,618</td></tr>
<tr><td>3</td><td>869</td></tr>
<tr><td>4</td><td>397</td></tr>
<tr><td>5</td><td>157</td></tr>
<tr><td>6</td><td>86</td></tr>
<tr><td>-1</td><td>76</td></tr>
<tr><td>7</td><td>33</td></tr>
<tr><td>8</td><td>13</td></tr>
<tr><td>10</td><td>6</td></tr>
<tr><td>9</td><td>6</td></tr>
<tr><td>12</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>8T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>17,026</td></tr>
<tr><td>1</td><td>3,434</td></tr>
<tr><td>2</td><td>1,625</td></tr>
<tr><td>3</td><td>771</td></tr>
<tr><td>4</td><td>364</td></tr>
<tr><td>5</td><td>167</td></tr>
<tr><td>-1</td><td>89</td></tr>
<tr><td>6</td><td>51</td></tr>
<tr><td>7</td><td>25</td></tr>
<tr><td>8</td><td>17</td></tr>
<tr><td>10</td><td>4</td></tr>
<tr><td>9</td><td>3</td></tr>
<tr><td>11</td><td>2</td></tr>
<tr><td>13</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>8B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>16,839</td></tr>
<tr><td>1</td><td>3,412</td></tr>
<tr><td>2</td><td>1,743</td></tr>
<tr><td>3</td><td>802</td></tr>
<tr><td>4</td><td>356</td></tr>
<tr><td>5</td><td>176</td></tr>
<tr><td>-1</td><td>111</td></tr>
<tr><td>6</td><td>64</td></tr>
<tr><td>7</td><td>47</td></tr>
<tr><td>8</td><td>12</td></tr>
<tr><td>9</td><td>12</td></tr>
<tr><td>10</td><td>4</td></tr>
<tr><td>13</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>9T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>17,305</td></tr>
<tr><td>1</td><td>3,299</td></tr>
<tr><td>2</td><td>1,557</td></tr>
<tr><td>3</td><td>706</td></tr>
<tr><td>4</td><td>324</td></tr>
<tr><td>5</td><td>171</td></tr>
<tr><td>-1</td><td>120</td></tr>
<tr><td>6</td><td>55</td></tr>
<tr><td>7</td><td>21</td></tr>
<tr><td>8</td><td>14</td></tr>
<tr><td>9</td><td>5</td></tr>
<tr><td>10</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>9B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>10,528</td></tr>
<tr><td>0</td><td>9,800</td></tr>
<tr><td>1</td><td>2,011</td></tr>
<tr><td>2</td><td>794</td></tr>
<tr><td>3</td><td>290</td></tr>
<tr><td>4</td><td>104</td></tr>
<tr><td>5</td><td>32</td></tr>
<tr><td>6</td><td>14</td></tr>
<tr><td>7</td><td>4</td></tr>
<tr><td>8</td><td>1</td></tr>
<tr><td>9</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>10T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>21,690</td></tr>
<tr><td>0</td><td>1,426</td></tr>
<tr><td>1</td><td>235</td></tr>
<tr><td>2</td><td>108</td></tr>
<tr><td>3</td><td>64</td></tr>
<tr><td>4</td><td>31</td></tr>
<tr><td>5</td><td>14</td></tr>
<tr><td>6</td><td>7</td></tr>
<tr><td>7</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>10B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>21,692</td></tr>
<tr><td>0</td><td>1,394</td></tr>
<tr><td>1</td><td>423</td></tr>
<tr><td>2</td><td>38</td></tr>
<tr><td>3</td><td>21</td></tr>
<tr><td>4</td><td>8</td></tr>
<tr><td>5</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>11T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>22,521</td></tr>
<tr><td>0</td><td>804</td></tr>
<tr><td>1</td><td>133</td></tr>
<tr><td>2</td><td>51</td></tr>
<tr><td>3</td><td>34</td></tr>
<tr><td>4</td><td>16</td></tr>
<tr><td>5</td><td>12</td></tr>
<tr><td>6</td><td>5</td></tr>
<tr><td>9</td><td>2</td></tr>
<tr><td>8</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>11B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>22,523</td></tr>
<tr><td>0</td><td>770</td></tr>
<tr><td>1</td><td>242</td></tr>
<tr><td>2</td><td>30</td></tr>
<tr><td>3</td><td>8</td></tr>
<tr><td>4</td><td>5</td></tr>
<tr><td>5</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>12T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,047</td></tr>
<tr><td>0</td><td>387</td></tr>
<tr><td>1</td><td>76</td></tr>
<tr><td>2</td><td>33</td></tr>
<tr><td>3</td><td>18</td></tr>
<tr><td>4</td><td>13</td></tr>
<tr><td>6</td><td>3</td></tr>
<tr><td>5</td><td>1</td></tr>
<tr><td>10</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>12B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,048</td></tr>
<tr><td>0</td><td>390</td></tr>
<tr><td>1</td><td>119</td></tr>
<tr><td>2</td><td>19</td></tr>
<tr><td>3</td><td>2</td></tr>
<tr><td>4</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>13T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,473</td></tr>
<tr><td>0</td><td>84</td></tr>
<tr><td>1</td><td>12</td></tr>
<tr><td>2</td><td>7</td></tr>
<tr><td>3</td><td>2</td></tr>
<tr><td>6</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>13B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,473</td></tr>
<tr><td>0</td><td>85</td></tr>
<tr><td>1</td><td>20</td></tr>
<tr><td>3</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>14T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,531</td></tr>
<tr><td>0</td><td>39</td></tr>
<tr><td>2</td><td>6</td></tr>
<tr><td>1</td><td>2</td></tr>
<tr><td>4</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>14B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,531</td></tr>
<tr><td>0</td><td>34</td></tr>
<tr><td>1</td><td>13</td></tr>
<tr><td>2</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>15T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,564</td></tr>
<tr><td>0</td><td>13</td></tr>
<tr><td>1</td><td>1</td></tr>
<tr><td>3</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>15B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,564</td></tr>
<tr><td>0</td><td>11</td></tr>
<tr><td>1</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>16T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,578</td></tr>
<tr><td>0</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>16B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,578</td></tr>
<tr><td>0</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>17T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,578</td></tr>
<tr><td>0</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>17B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,578</td></tr>
<tr><td>0</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>18T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,578</td></tr>
<tr><td>0</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>18B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,578</td></tr>
<tr><td>1</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>19T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>19B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>20T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>20B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>21T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>21B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>22T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>22B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>23T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>23B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>24T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>24B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>25T</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>25B</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-1</td><td>23,579</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>19820327SSLG0</td><td>19820328HDSS0</td><td>19820328HTLT0</td></tr>
<tr><td>GDAY</td><td>19820327</td><td>19820328</td><td>19820328</td></tr>
<tr><td>1T</td><td>2</td><td>0</td><td>0</td></tr>
<tr><td>1B</td><td>0</td><td>0</td><td>7</td></tr>
<tr><td>2T</td><td>3</td><td>1</td><td>0</td></tr>
<tr><td>2B</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>3T</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>3B</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>4T</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>4B</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>5T</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>5B</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>6T</td><td>1</td><td>3</td><td>1</td></tr>
<tr><td>6B</td><td>1</td><td>0</td><td>6</td></tr>
<tr><td>7T</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>7B</td><td>3</td><td>2</td><td>0</td></tr>
<tr><td>8T</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>8B</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>9T</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>9B</td><td>0</td><td>0</td><td>-1</td></tr>
<tr><td>10T</td><td>0</td><td>-1</td><td>-1</td></tr>
<tr><td>10B</td><td>4</td><td>-1</td><td>-1</td></tr>
<tr><td>11T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>11B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>12T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>12B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>13T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>13B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>14T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>14B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>15T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>15B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>16T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>16B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>17T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>17B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>18T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>18B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>19T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>19B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>20T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>20B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>21T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>21B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>22T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>22B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>23T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>23B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>24T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>24B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>25T</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>25B</td><td>-1</td><td>-1</td><td>-1</td></tr>
<tr><td>TPOINT</td><td>7</td><td>5</td><td>2</td></tr>
<tr><td>BPOINT</td><td>11</td><td>3</td><td>14</td></tr>
<tr><td>THIT</td><td>10</td><td>8</td><td>4</td></tr>
<tr><td>BHIT</td><td>16</td><td>7</td><td>9</td></tr>
<tr><td>TERR</td><td>0</td><td>2</td><td>3</td></tr>
<tr><td>BERR</td><td>3</td><td>0</td><td>1</td></tr>
<tr><td>TBBHP</td><td>3</td><td>4</td><td>3</td></tr>
<tr><td>BBBHP</td><td>10</td><td>9</td><td>12</td></tr>
</tbody></table>
</div>

</div>
