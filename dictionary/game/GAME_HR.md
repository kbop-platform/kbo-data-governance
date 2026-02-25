---
title: GAME_HR
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-new">신세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">GAME_HR</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: LE_ID, SR_ID, G_ID, SEQ_NO</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">7,784</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">15</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>LE_ID, SR_ID, G_ID, SEQ_NO</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">new (신세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">미디어, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">15개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">LE_ID</span></td><td><span class="col-std">league_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">리그 ID (1=1군)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">SR_ID</span></td><td><span class="col-std">series_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시리즈 ID (0=정규시즌)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">G_ID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (YYYYMMDDVVHH# 형식)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">INN_NO</span></td><td><span class="col-std">inn_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝 번호</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">TB_SC</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 구분 코드 (T=원정, B=홈)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">BAT_P_ID</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">PIT_P_ID</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">PLACE_SC</span></td><td><span class="col-std">place_sc</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">PLACE 상태코드</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">HR_DISTANCE_VA</span></td><td><span class="col-std">hr_distance_va</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">HR_DISTANCE 값</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">DIREC_SC</span></td><td><span class="col-std">direc_sc</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">DIREC 상태코드</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">SCORE_CN</span></td><td><span class="col-std">score_cn</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SCORE 건수</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">RECORD_DT</span></td><td><span class="col-std">record_dt</span></td><td><span class="col-type">varchar(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">RECORD 일시</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">SEQ_NO</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">순번</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">REG_DT</span></td><td><span class="col-std">reg_dt</span></td><td><span class="col-type">datetime</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">등록 일시</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">13개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>LE_ID</code><span class="code-desc"> — 리그 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>7,784</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SR_ID</code><span class="code-desc"> — 시리즈 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>7,172</td></tr>
<tr><td>1</td><td>330</td></tr>
<tr><td>8</td><td>94</td></tr>
<tr><td>7</td><td>51</td></tr>
<tr><td>5</td><td>44</td></tr>
<tr><td>6</td><td>40</td></tr>
<tr><td>3</td><td>35</td></tr>
<tr><td>4</td><td>9</td></tr>
<tr><td>9</td><td>9</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SEASON_ID</code><span class="code-desc"> — 시즌 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>2024</td><td>1,576</td></tr>
<tr><td>2020</td><td>1,422</td></tr>
<tr><td>2025</td><td>1,280</td></tr>
<tr><td>2021</td><td>1,233</td></tr>
<tr><td>2022</td><td>1,184</td></tr>
<tr><td>2023</td><td>1,089</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>G_ID</code><span class="code-desc"> — 경기 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>20220918OBSK0</td><td>9</td></tr>
<tr><td>20250720WOSS0</td><td>9</td></tr>
<tr><td>20210622LGSK0</td><td>8</td></tr>
<tr><td>20220706LTSK0</td><td>8</td></tr>
<tr><td>20200819HHSK0</td><td>8</td></tr>
<tr><td>20200728LGSK0</td><td>8</td></tr>
<tr><td>20200908WOSK0</td><td>8</td></tr>
<tr><td>20240915SSSK0</td><td>8</td></tr>
<tr><td>20220929WOSK0</td><td>7</td></tr>
<tr><td>20240711NCSS0</td><td>7</td></tr>
<tr><td>20241015LGSS0</td><td>7</td></tr>
<tr><td>20201002WOSK0</td><td>7</td></tr>
<tr><td>20220924OBSK0</td><td>7</td></tr>
<tr><td>20201022LTSK0</td><td>7</td></tr>
<tr><td>20250509HHWO0</td><td>7</td></tr>
<tr><td>20200527LGHH0</td><td>7</td></tr>
<tr><td>20250916SKNC0</td><td>7</td></tr>
<tr><td>20240831HTSS0</td><td>7</td></tr>
<tr><td>20240620LTKT0</td><td>7</td></tr>
<tr><td>20240615SSNC0</td><td>7</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN_NO</code><span class="code-desc"> — 이닝 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>4</td><td>959</td></tr>
<tr><td>3</td><td>916</td></tr>
<tr><td>5</td><td>877</td></tr>
<tr><td>1</td><td>875</td></tr>
<tr><td>8</td><td>871</td></tr>
<tr><td>6</td><td>869</td></tr>
<tr><td>7</td><td>851</td></tr>
<tr><td>2</td><td>804</td></tr>
<tr><td>9</td><td>673</td></tr>
<tr><td>10</td><td>48</td></tr>
<tr><td>11</td><td>27</td></tr>
<tr><td>12</td><td>14</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB_SC</code><span class="code-desc"> — 팀 구분 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>3,892</td></tr>
<tr><td>T</td><td>3,892</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>BAT_P_ID</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PIT_P_ID</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>PLACE_SC</code><span class="code-desc"> — PLACE 상태코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>E</td><td>7,666</td></tr>
<tr><td>R</td><td>90</td></tr>
<tr><td>H</td><td>28</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>HR_DISTANCE_VA</code><span class="code-desc"> — HR_DISTANCE 값</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>115</td><td>1,866</td></tr>
<tr><td>120</td><td>1,642</td></tr>
<tr><td>110</td><td>1,498</td></tr>
<tr><td>125</td><td>1,439</td></tr>
<tr><td>130</td><td>582</td></tr>
<tr><td>105</td><td>551</td></tr>
<tr><td>135</td><td>122</td></tr>
<tr><td>100</td><td>42</td></tr>
<tr><td>0</td><td>19</td></tr>
<tr><td>140</td><td>19</td></tr>
<tr><td>145</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>DIREC_SC</code><span class="code-desc"> — DIREC 상태코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>7</td><td>3,311</td></tr>
<tr><td>9</td><td>2,331</td></tr>
<tr><td>78</td><td>810</td></tr>
<tr><td>8</td><td>720</td></tr>
<tr><td>89</td><td>612</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SCORE_CN</code><span class="code-desc"> — SCORE 건수</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>4,173</td></tr>
<tr><td>2</td><td>2,280</td></tr>
<tr><td>3</td><td>1,083</td></tr>
<tr><td>4</td><td>248</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>RECORD_DT</code><span class="code-desc"> — RECORD 일시</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>19:36</td><td>48</td></tr>
<tr><td>19:20</td><td>47</td></tr>
<tr><td>19:30</td><td>46</td></tr>
<tr><td>18:34</td><td>45</td></tr>
<tr><td>18:33</td><td>45</td></tr>
<tr><td>19:24</td><td>44</td></tr>
<tr><td>19:33</td><td>43</td></tr>
<tr><td>18:41</td><td>42</td></tr>
<tr><td>19:27</td><td>41</td></tr>
<tr><td>18:45</td><td>41</td></tr>
<tr><td>18:37</td><td>41</td></tr>
<tr><td>19:28</td><td>41</td></tr>
<tr><td>19:41</td><td>41</td></tr>
<tr><td>18:42</td><td>41</td></tr>
<tr><td>19:22</td><td>40</td></tr>
<tr><td>19:29</td><td>39</td></tr>
<tr><td>19:50</td><td>39</td></tr>
<tr><td>18:59</td><td>39</td></tr>
<tr><td>20:19</td><td>38</td></tr>
<tr><td>19:52</td><td>38</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>LE_ID</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>SR_ID</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SEASON_ID</td><td>2020</td><td>2020</td><td>2020</td></tr>
<tr><td>G_ID</td><td>20200505LTKT0</td><td>20200505LTKT0</td><td>20200505LTKT0</td></tr>
<tr><td>INN_NO</td><td>6</td><td>7</td><td>8</td></tr>
<tr><td>TB_SC</td><td>B</td><td>T</td><td>T</td></tr>
<tr><td>BAT_P_ID</td><td>68050</td><td>50506</td><td>78513</td></tr>
<tr><td>PIT_P_ID</td><td>50558</td><td>65062</td><td>77563</td></tr>
<tr><td>PLACE_SC</td><td>E</td><td>E</td><td>E</td></tr>
<tr><td>HR_DISTANCE_VA</td><td>115</td><td>105</td><td>110</td></tr>
<tr><td>DIREC_SC</td><td>9</td><td>7</td><td>7</td></tr>
<tr><td>SCORE_CN</td><td>1</td><td>3</td><td>2</td></tr>
<tr><td>RECORD_DT</td><td>16:49</td><td>17:12</td><td>17:35</td></tr>
<tr><td>SEQ_NO</td><td>2160</td><td>2620</td><td>3120</td></tr>
<tr><td>REG_DT</td><td>2025-09-12 17:17:02.067000</td><td>2025-09-12 17:17:02.067000</td><td>2025-09-12 17:17:02.067000</td></tr>
</tbody></table>
</div>

</div>
