---
title: IE_BatterRecord
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">실시간</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">IE_BatterRecord</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gameID, GYEAR, BatOrder, PlayerID, SeqNO</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">451,166</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">25</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">실시간</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">S2i 운영</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gameID, GYEAR, BatOrder, PlayerID, SeqNO</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">S2i 운영 (R-06)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">실시간 (&lt; 5초)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[실시간 경기](../products/live-game.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">25개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gameID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (GMKEY와 동일 형식)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">BatOrder</span></td><td><span class="col-std">bat_order_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">타순</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">Position</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">PositionName</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">PlayerName</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(15)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">PlayerID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">SeqNO</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">순번</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">OAB</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">Run</span></td><td><span class="col-std">run</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">H1</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">H2</span></td><td><span class="col-std">h2b</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2루타</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">H3</span></td><td><span class="col-std">h3b</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">3루타</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">RBI</span></td><td><span class="col-std">rbi</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타점</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">Steal</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">CS</span></td><td><span class="col-std">cs</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루실패</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">SH</span></td><td><span class="col-std">sh</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생번트</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">SF</span></td><td><span class="col-std">sf</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생플라이</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">HBP</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">SO</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">DP</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">TP</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">bHome</span></td><td><span class="col-std">home_if</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 여부</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">22개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> — 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>BatOrder</code><span class="code-desc"> — 타순</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Position</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>7</td><td>45,926</td></tr>
<tr><td>2</td><td>45,632</td></tr>
<tr><td>4</td><td>44,261</td></tr>
<tr><td>9</td><td>43,844</td></tr>
<tr><td>5</td><td>42,335</td></tr>
<tr><td>3</td><td>42,287</td></tr>
<tr><td>8</td><td>41,828</td></tr>
<tr><td>10</td><td>41,432</td></tr>
<tr><td>6</td><td>41,308</td></tr>
<tr><td>0</td><td>38,309</td></tr>
<tr><td>11</td><td>20,690</td></tr>
<tr><td>1</td><td>3,314</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PlayerID</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SeqNO</code><span class="code-desc"> — 순번</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>276,289</td></tr>
<tr><td>2</td><td>108,570</td></tr>
<tr><td>3</td><td>51,176</td></tr>
<tr><td>4</td><td>11,015</td></tr>
<tr><td>5</td><td>3,138</td></tr>
<tr><td>6</td><td>718</td></tr>
<tr><td>7</td><td>181</td></tr>
<tr><td>8</td><td>54</td></tr>
<tr><td>9</td><td>18</td></tr>
<tr><td>10</td><td>4</td></tr>
<tr><td>11</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>OAB</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>4</td><td>110,980</td></tr>
<tr><td>3</td><td>93,450</td></tr>
<tr><td>1</td><td>82,170</td></tr>
<tr><td>0</td><td>64,969</td></tr>
<tr><td>2</td><td>60,137</td></tr>
<tr><td>5</td><td>36,013</td></tr>
<tr><td>6</td><td>3,306</td></tr>
<tr><td>7</td><td>141</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>Run</code><span class="code-desc"> — 득점</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>319,235</td></tr>
<tr><td>1</td><td>105,606</td></tr>
<tr><td>2</td><td>22,545</td></tr>
<tr><td>3</td><td>3,433</td></tr>
<tr><td>4</td><td>327</td></tr>
<tr><td>5</td><td>17</td></tr>
<tr><td>6</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>H1</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>284,152</td></tr>
<tr><td>1</td><td>123,966</td></tr>
<tr><td>2</td><td>35,859</td></tr>
<tr><td>3</td><td>6,468</td></tr>
<tr><td>4</td><td>681</td></tr>
<tr><td>5</td><td>38</td></tr>
<tr><td>6</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>H2</code><span class="code-desc"> — 2루타</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>401,703</td></tr>
<tr><td>1</td><td>45,991</td></tr>
<tr><td>2</td><td>3,323</td></tr>
<tr><td>3</td><td>147</td></tr>
<tr><td>4</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>H3</code><span class="code-desc"> — 3루타</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>446,232</td></tr>
<tr><td>1</td><td>4,897</td></tr>
<tr><td>2</td><td>36</td></tr>
<tr><td>3</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>HR</code><span class="code-desc"> — 홈런</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>424,675</td></tr>
<tr><td>1</td><td>25,018</td></tr>
<tr><td>2</td><td>1,417</td></tr>
<tr><td>3</td><td>50</td></tr>
<tr><td>4</td><td>6</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>RBI</code><span class="code-desc"> — 타점</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>350,495</td></tr>
<tr><td>1</td><td>65,816</td></tr>
<tr><td>2</td><td>23,300</td></tr>
<tr><td>3</td><td>7,970</td></tr>
<tr><td>4</td><td>2,599</td></tr>
<tr><td>5</td><td>697</td></tr>
<tr><td>6</td><td>200</td></tr>
<tr><td>7</td><td>74</td></tr>
<tr><td>8</td><td>12</td></tr>
<tr><td>9</td><td>2</td></tr>
<tr><td>11</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>Steal</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>425,665</td></tr>
<tr><td>1</td><td>23,514</td></tr>
<tr><td>2</td><td>1,824</td></tr>
<tr><td>3</td><td>151</td></tr>
<tr><td>4</td><td>11</td></tr>
<tr><td>5</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>CS</code><span class="code-desc"> — 도루실패</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>439,457</td></tr>
<tr><td>1</td><td>11,560</td></tr>
<tr><td>2</td><td>147</td></tr>
<tr><td>3</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SH</code><span class="code-desc"> — 희생번트</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>435,512</td></tr>
<tr><td>1</td><td>15,031</td></tr>
<tr><td>2</td><td>606</td></tr>
<tr><td>3</td><td>17</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SF</code><span class="code-desc"> — 희생플라이</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>440,895</td></tr>
<tr><td>1</td><td>10,111</td></tr>
<tr><td>2</td><td>158</td></tr>
<tr><td>3</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>BB</code><span class="code-desc"> — 볼넷</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>350,461</td></tr>
<tr><td>1</td><td>84,794</td></tr>
<tr><td>2</td><td>14,170</td></tr>
<tr><td>3</td><td>1,589</td></tr>
<tr><td>4</td><td>144</td></tr>
<tr><td>5</td><td>6</td></tr>
<tr><td>6</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>HBP</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>433,427</td></tr>
<tr><td>1</td><td>17,212</td></tr>
<tr><td>2</td><td>515</td></tr>
<tr><td>3</td><td>12</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SO</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>274,486</td></tr>
<tr><td>1</td><td>134,415</td></tr>
<tr><td>2</td><td>35,954</td></tr>
<tr><td>3</td><td>5,833</td></tr>
<tr><td>4</td><td>457</td></tr>
<tr><td>5</td><td>21</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>DP</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>426,504</td></tr>
<tr><td>1</td><td>23,974</td></tr>
<tr><td>2</td><td>679</td></tr>
<tr><td>3</td><td>9</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>TP</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>451,145</td></tr>
<tr><td>1</td><td>21</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>bHome</code><span class="code-desc"> — 홈팀 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>226,414</td></tr>
<tr><td>1</td><td>224,752</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gameID</td><td>20040310LTSS0</td><td>20040310LTSS0</td><td>20040310LTSS0</td></tr>
<tr><td>GYEAR</td><td>2004</td><td>2004</td><td>2004</td></tr>
<tr><td>BatOrder</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>Position</td><td>9</td><td>8</td><td>7</td></tr>
<tr><td>PositionName</td><td>¿ìÀÍ¼ö</td><td>Áß°ß¼ö</td><td>ÁÂÀÍ¼ö</td></tr>
<tr><td>PlayerName</td><td>¹ÚÇÑÀÌ</td><td>±è´ëÀÍ</td><td>±èÁÖÂù</td></tr>
<tr><td>PlayerID</td><td>71432</td><td>96503</td><td>70410</td></tr>
<tr><td>SeqNO</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>OAB</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>Run</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>H1</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>H2</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>H3</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HR</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>RBI</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>Steal</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>CS</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SH</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SF</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BB</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HBP</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SO</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>DP</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>TP</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>bHome</td><td>1</td><td>0</td><td>0</td></tr>
</tbody></table>
</div>

</div>
