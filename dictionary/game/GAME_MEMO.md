---
title: GAME_MEMO
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-new">신세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">GAME_MEMO</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: LE_ID, SR_ID, G_ID, INN_NO, BAT_ORDER_NO, BAT_AROUND_NO, TB_SC, PA_PIT_NO, ORDER_NO</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">54,544</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">20</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>LE_ID, SR_ID, G_ID, INN_NO, BAT_ORDER_NO, BAT_AROUND_NO, TB_SC, PA_PIT_NO, ORDER_NO</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">new (신세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">20개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">LE_ID</span></td><td><span class="col-std">league_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">리그 ID (1=1군)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">SR_ID</span></td><td><span class="col-std">series_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시리즈 ID (0=정규시즌)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">G_ID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (YYYYMMDDVVHH# 형식)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">INN_NO</span></td><td><span class="col-std">inn_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">이닝 번호</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">BAT_ORDER_NO</span></td><td><span class="col-std">bat_order_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">BAT_ORDER 번호</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">BAT_AROUND_NO</span></td><td><span class="col-std">bat_around_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">BAT_AROUND 번호</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">TB_SC</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">팀 구분 코드 (T=원정, B=홈)</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">PA_PIT_NO</span></td><td><span class="col-std">pa_pit_no</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">PA_PIT 번호</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">GAME_PIT_NO</span></td><td><span class="col-std">game_pit_no</span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc">GAME_PIT 번호</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">P_ID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">선수 ID (정수)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">REQ_T_ID</span></td><td><span class="col-std"></span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">START_TM</span></td><td><span class="col-std">start_tm</span></td><td><span class="col-type">varchar(5)</span></td><td></td><td></td><td><span class="col-desc">START 시각</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">END_TM</span></td><td><span class="col-std">end_tm</span></td><td><span class="col-type">varchar(5)</span></td><td></td><td></td><td><span class="col-desc">END 시각</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">USE_TM</span></td><td><span class="col-std">use_tm</span></td><td><span class="col-type">varchar(5)</span></td><td></td><td></td><td><span class="col-desc">USE 시각</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">FIRST_IF</span></td><td><span class="col-std">first_if</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">FIRST 여부 (Y/N)</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">LAST_IF</span></td><td><span class="col-std">last_if</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">LAST 여부 (Y/N)</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">ETC_ME</span></td><td><span class="col-std">etc_me</span></td><td><span class="col-type">varchar(400)</span></td><td></td><td></td><td><span class="col-desc">ETC 메모</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">ORDER_NO</span></td><td><span class="col-std">order_no</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">ORDER 번호</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">REG_DT</span></td><td><span class="col-std">reg_dt</span></td><td><span class="col-type">datetime</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">등록 일시</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">17개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>LE_ID</code><span class="code-desc"> — 리그 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>54,544</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SR_ID</code><span class="code-desc"> — 시리즈 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>51,456</td></tr>
<tr><td>1</td><td>1,486</td></tr>
<tr><td>7</td><td>439</td></tr>
<tr><td>5</td><td>353</td></tr>
<tr><td>6</td><td>327</td></tr>
<tr><td>3</td><td>302</td></tr>
<tr><td>4</td><td>118</td></tr>
<tr><td>8</td><td>53</td></tr>
<tr><td>9</td><td>10</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SEASON_ID</code><span class="code-desc"> — 시즌 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>2025</td><td>23,978</td></tr>
<tr><td>2024</td><td>13,364</td></tr>
<tr><td>2023</td><td>4,719</td></tr>
<tr><td>2022</td><td>4,377</td></tr>
<tr><td>2020</td><td>4,054</td></tr>
<tr><td>2021</td><td>4,052</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>G_ID</code><span class="code-desc"> — 경기 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>20250827HTSK0</td><td>69</td></tr>
<tr><td>20250730OBHT0</td><td>67</td></tr>
<tr><td>20250815HTOB0</td><td>66</td></tr>
<tr><td>20250703NCHH0</td><td>66</td></tr>
<tr><td>20250709OBLT0</td><td>65</td></tr>
<tr><td>20250626HTWO0</td><td>65</td></tr>
<tr><td>20250830OBLT0</td><td>65</td></tr>
<tr><td>20250821LTLG0</td><td>64</td></tr>
<tr><td>20250910SSHT0</td><td>63</td></tr>
<tr><td>20250724HHOB0</td><td>62</td></tr>
<tr><td>20250501KTOB0</td><td>62</td></tr>
<tr><td>20240410SSLT0</td><td>61</td></tr>
<tr><td>20250831HTKT0</td><td>61</td></tr>
<tr><td>20250607HHHT0</td><td>59</td></tr>
<tr><td>20250425NCSS0</td><td>59</td></tr>
<tr><td>20250814LTHH0</td><td>59</td></tr>
<tr><td>20250903SKHT0</td><td>58</td></tr>
<tr><td>20250425LGHT0</td><td>58</td></tr>
<tr><td>20250628HTLG0</td><td>58</td></tr>
<tr><td>20250816HHNC0</td><td>57</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN_NO</code><span class="code-desc"> — 이닝 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>7</td><td>6,546</td></tr>
<tr><td>5</td><td>6,481</td></tr>
<tr><td>8</td><td>6,453</td></tr>
<tr><td>6</td><td>6,398</td></tr>
<tr><td>3</td><td>6,300</td></tr>
<tr><td>4</td><td>6,135</td></tr>
<tr><td>2</td><td>5,186</td></tr>
<tr><td>1</td><td>5,068</td></tr>
<tr><td>9</td><td>4,818</td></tr>
<tr><td>10</td><td>658</td></tr>
<tr><td>11</td><td>421</td></tr>
<tr><td>12</td><td>78</td></tr>
<tr><td>13</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>BAT_ORDER_NO</code><span class="code-desc"> — BAT_ORDER 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>3</td><td>7,095</td></tr>
<tr><td>2</td><td>6,918</td></tr>
<tr><td>4</td><td>6,797</td></tr>
<tr><td>1</td><td>6,533</td></tr>
<tr><td>5</td><td>5,929</td></tr>
<tr><td>6</td><td>5,591</td></tr>
<tr><td>7</td><td>5,382</td></tr>
<tr><td>8</td><td>5,252</td></tr>
<tr><td>9</td><td>5,047</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>BAT_AROUND_NO</code><span class="code-desc"> — BAT_AROUND 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>54,384</td></tr>
<tr><td>1</td><td>158</td></tr>
<tr><td>3</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB_SC</code><span class="code-desc"> — 팀 구분 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>27,295</td></tr>
<tr><td>T</td><td>27,249</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PA_PIT_NO</code><span class="code-desc"> — PA_PIT 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>25,987</td></tr>
<tr><td>1</td><td>8,387</td></tr>
<tr><td>2</td><td>6,556</td></tr>
<tr><td>3</td><td>4,939</td></tr>
<tr><td>4</td><td>3,755</td></tr>
<tr><td>5</td><td>2,693</td></tr>
<tr><td>6</td><td>1,338</td></tr>
<tr><td>7</td><td>541</td></tr>
<tr><td>8</td><td>207</td></tr>
<tr><td>9</td><td>93</td></tr>
<tr><td>10</td><td>29</td></tr>
<tr><td>11</td><td>10</td></tr>
<tr><td>12</td><td>6</td></tr>
<tr><td>13</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>GAME_PIT_NO</code><span class="code-desc"> — GAME_PIT 번호</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>P_ID</code><span class="code-desc"> — 선수 ID</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>REQ_T_ID</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>48,830</td></tr>
<tr><td>LT</td><td>603</td></tr>
<tr><td>SK</td><td>600</td></tr>
<tr><td>HT</td><td>598</td></tr>
<tr><td>SS</td><td>590</td></tr>
<tr><td>KT</td><td>587</td></tr>
<tr><td>OB</td><td>571</td></tr>
<tr><td>LG</td><td>567</td></tr>
<tr><td>NC</td><td>548</td></tr>
<tr><td>WO</td><td>534</td></tr>
<tr><td>HH</td><td>512</td></tr>
<tr><td>KR</td><td>2</td></tr>
<tr><td>WE</td><td>1</td></tr>
<tr><td>EA</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>START_TM</code><span class="code-desc"> — START 시각</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>00:00</td><td>48,363</td></tr>
<tr><td>18:30</td><td>59</td></tr>
<tr><td>18:34</td><td>38</td></tr>
<tr><td>19:15</td><td>36</td></tr>
<tr><td>19:22</td><td>36</td></tr>
<tr><td>19:41</td><td>36</td></tr>
<tr><td>19:08</td><td>35</td></tr>
<tr><td>19:16</td><td>33</td></tr>
<tr><td>19:02</td><td>33</td></tr>
<tr><td>19:20</td><td>33</td></tr>
<tr><td>19:37</td><td>32</td></tr>
<tr><td>20:29</td><td>32</td></tr>
<tr><td>19:13</td><td>31</td></tr>
<tr><td>20:31</td><td>31</td></tr>
<tr><td>19:14</td><td>31</td></tr>
<tr><td>19:52</td><td>31</td></tr>
<tr><td>20:46</td><td>31</td></tr>
<tr><td>20:01</td><td>30</td></tr>
<tr><td>19:11</td><td>30</td></tr>
<tr><td>18:46</td><td>30</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>END_TM</code><span class="code-desc"> — END 시각</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>00:00</td><td>48,473</td></tr>
<tr><td>19:16</td><td>35</td></tr>
<tr><td>18:35</td><td>34</td></tr>
<tr><td>20:09</td><td>33</td></tr>
<tr><td>19:27</td><td>33</td></tr>
<tr><td>20:31</td><td>33</td></tr>
<tr><td>20:41</td><td>33</td></tr>
<tr><td>19:13</td><td>32</td></tr>
<tr><td>19:15</td><td>32</td></tr>
<tr><td>19:53</td><td>32</td></tr>
<tr><td>19:02</td><td>32</td></tr>
<tr><td>19:18</td><td>31</td></tr>
<tr><td>20:02</td><td>31</td></tr>
<tr><td>19:40</td><td>31</td></tr>
<tr><td>18:47</td><td>31</td></tr>
<tr><td>19:32</td><td>31</td></tr>
<tr><td>19:12</td><td>31</td></tr>
<tr><td>19:11</td><td>30</td></tr>
<tr><td>20:04</td><td>30</td></tr>
<tr><td>19:23</td><td>30</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>USE_TM</code><span class="code-desc"> — USE 시각</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>00:00</td><td>50,830</td></tr>
<tr><td>00:01</td><td>2,398</td></tr>
<tr><td>00:02</td><td>763</td></tr>
<tr><td>00:03</td><td>290</td></tr>
<tr><td>00:04</td><td>18</td></tr>
<tr><td>00:05</td><td>15</td></tr>
<tr><td>00:07</td><td>12</td></tr>
<tr><td>00:30</td><td>11</td></tr>
<tr><td>00:06</td><td>10</td></tr>
<tr><td>00:32</td><td>9</td></tr>
<tr><td>00:09</td><td>9</td></tr>
<tr><td>00:10</td><td>9</td></tr>
<tr><td>00:40</td><td>8</td></tr>
<tr><td>00:08</td><td>5</td></tr>
<tr><td>00:41</td><td>5</td></tr>
<tr><td>00:31</td><td>5</td></tr>
<tr><td>00:20</td><td>5</td></tr>
<tr><td>00:29</td><td>5</td></tr>
<tr><td>00:34</td><td>4</td></tr>
<tr><td>00:43</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>FIRST_IF</code><span class="code-desc"> — FIRST 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>4</td><td>10,683</td></tr>
<tr><td></td><td>9,693</td></tr>
<tr><td>Æ÷¼ö</td><td>8,867</td></tr>
<tr><td>ÄÚÄª½ºÅÂÇÁ</td><td>8,672</td></tr>
<tr><td>C</td><td>4,623</td></tr>
<tr><td>P</td><td>4,304</td></tr>
<tr><td>¾Æ¿ô</td><td>2,442</td></tr>
<tr><td>¼¼ÀÌÇÁ</td><td>2,031</td></tr>
<tr><td>3·ç¼ö</td><td>583</td></tr>
<tr><td>1</td><td>542</td></tr>
<tr><td>À¯°Ý¼ö</td><td>504</td></tr>
<tr><td>ÆÄ¿ï</td><td>380</td></tr>
<tr><td>Æä¾î</td><td>204</td></tr>
<tr><td>2·ç¼ö</td><td>153</td></tr>
<tr><td>½ºÀ®</td><td>149</td></tr>
<tr><td>Á¤»ó</td><td>125</td></tr>
<tr><td>Q</td><td>98</td></tr>
<tr><td>2·çÅ¸</td><td>79</td></tr>
<tr><td>È¨·±</td><td>77</td></tr>
<tr><td>»ç±¸</td><td>70</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>LAST_IF</code><span class="code-desc"> — LAST 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>47,528</td></tr>
<tr><td>¾Æ¿ô</td><td>2,392</td></tr>
<tr><td>¼¼ÀÌÇÁ</td><td>2,081</td></tr>
<tr><td>1,2·ç°£</td><td>711</td></tr>
<tr><td>ÆÄ¿ï</td><td>366</td></tr>
<tr><td>2,3·ç°£</td><td>332</td></tr>
<tr><td>Æä¾î</td><td>218</td></tr>
<tr><td>2·ç</td><td>172</td></tr>
<tr><td>½ºÀ®</td><td>158</td></tr>
<tr><td>Á¤»ó</td><td>109</td></tr>
<tr><td>2·çÅ¸</td><td>83</td></tr>
<tr><td>»ç±¸</td><td>81</td></tr>
<tr><td>È¨·±</td><td>62</td></tr>
<tr><td>³ë ½ºÀ®</td><td>61</td></tr>
<tr><td>ÁÖ½É</td><td>35</td></tr>
<tr><td>º¼</td><td>23</td></tr>
<tr><td>ÀÎÇÃ·¹ÀÌ</td><td>22</td></tr>
<tr><td>2·ç¼ö</td><td>20</td></tr>
<tr><td>3·çÅ¸</td><td>19</td></tr>
<tr><td>¹æÇØ</td><td>14</td></tr>
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
<tr><td>G_ID</td><td>20200505HHSK0</td><td>20200505HHSK0</td><td>20200505LTKT0</td></tr>
<tr><td>INN_NO</td><td>7</td><td>9</td><td>1</td></tr>
<tr><td>BAT_ORDER_NO</td><td>5</td><td>3</td><td>1</td></tr>
<tr><td>BAT_AROUND_NO</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>TB_SC</td><td>B</td><td>B</td><td>T</td></tr>
<tr><td>PA_PIT_NO</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>GAME_PIT_NO</td><td>170</td><td>213</td><td>0</td></tr>
<tr><td>P_ID</td><td>69744</td><td>69744</td><td>0</td></tr>
<tr><td>REQ_T_ID</td><td></td><td></td><td></td></tr>
<tr><td>START_TM</td><td>00:00</td><td>00:00</td><td>14:00</td></tr>
<tr><td>END_TM</td><td>00:00</td><td>00:00</td><td>15:13</td></tr>
<tr><td>USE_TM</td><td>00:00</td><td>00:00</td><td>01:13</td></tr>
<tr><td>FIRST_IF</td><td>ÄÚÄª½ºÅÂÇÁ</td><td>ÄÚÄª½ºÅÂÇÁ</td><td></td></tr>
<tr><td>LAST_IF</td><td></td><td></td><td></td></tr>
<tr><td>ETC_ME</td><td>ÄÚÄª½ºÅÂÇÁ ¸¶¿îµå ¹æ¹®</td><td>ÄÚÄª½ºÅÂÇÁ ¸¶¿îµå ¹æ¹®</td><td>1È¸ÃÊ 1¹øÅ¸¼ø ÃÊ±¸ Àü 14:00 ~ 15:13 (73ºÐ°£) ¿ìÃµ °ü·Ã(À¸)·Î °æ±â°³½Ã Áö¿¬</td></tr>
<tr><td>ORDER_NO</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>REG_DT</td><td>2025-09-12 17:17:03.003000</td><td>2025-09-12 17:17:03.003000</td><td>2025-09-12 17:17:03.003000</td></tr>
</tbody></table>
</div>

</div>
