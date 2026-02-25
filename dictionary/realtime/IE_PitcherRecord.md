---
title: IE_PitcherRecord
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">실시간</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">IE_PitcherRecord</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gameID, GYEAR, PlayerID</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">134,388</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">22</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">실시간</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">S2i 운영</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gameID, GYEAR, PlayerID</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">S2i 운영 (R-06)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">실시간 (&lt; 5초)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[실시간 경기](../products/live-game.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">22개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gameID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (GMKEY와 동일 형식)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">PlayerName</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(15)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">PlayerID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">SeqNO</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">순번</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">Inning</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">PA</span></td><td><span class="col-std">pa</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 (Plate Appearance)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">PitchBallCnt</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">PitchStrikeCnt</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">OAB</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">Run</span></td><td><span class="col-std">run</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">Hit</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">SH</span></td><td><span class="col-std">sh</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생번트</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">SF</span></td><td><span class="col-std">sf</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생플라이</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">HBP</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">SO</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">BK</span></td><td><span class="col-std">bk</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">보크</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">WP</span></td><td><span class="col-std">wp</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">폭투</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">ER</span></td><td><span class="col-std">er</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">자책점</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">bHome</span></td><td><span class="col-std">home_if</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 여부</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">20개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> — 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PlayerID</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SeqNO</code><span class="code-desc"> — 순번</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>30,718</td></tr>
<tr><td>2</td><td>29,501</td></tr>
<tr><td>3</td><td>27,774</td></tr>
<tr><td>4</td><td>22,354</td></tr>
<tr><td>5</td><td>13,968</td></tr>
<tr><td>6</td><td>6,659</td></tr>
<tr><td>7</td><td>2,467</td></tr>
<tr><td>8</td><td>729</td></tr>
<tr><td>9</td><td>175</td></tr>
<tr><td>10</td><td>36</td></tr>
<tr><td>11</td><td>6</td></tr>
<tr><td>12</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>Inning</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PA</code><span class="code-desc"> — 타석</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PitchBallCnt</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PitchStrikeCnt</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>OAB</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Run</code><span class="code-desc"> — 득점</span></summary>
<div class="code-ref">고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Hit</code><span class="code-desc"> — 안타</span></summary>
<div class="code-ref">고유값 19종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>HR</code><span class="code-desc"> — 홈런</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>113,070</td></tr>
<tr><td>1</td><td>17,681</td></tr>
<tr><td>2</td><td>3,065</td></tr>
<tr><td>3</td><td>492</td></tr>
<tr><td>4</td><td>71</td></tr>
<tr><td>5</td><td>9</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SH</code><span class="code-desc"> — 희생번트</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>121,355</td></tr>
<tr><td>1</td><td>11,686</td></tr>
<tr><td>2</td><td>1,204</td></tr>
<tr><td>3</td><td>131</td></tr>
<tr><td>4</td><td>12</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SF</code><span class="code-desc"> — 희생플라이</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>125,452</td></tr>
<tr><td>1</td><td>8,516</td></tr>
<tr><td>2</td><td>393</td></tr>
<tr><td>3</td><td>26</td></tr>
<tr><td>4</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>BB</code><span class="code-desc"> — 볼넷</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>71,472</td></tr>
<tr><td>1</td><td>36,458</td></tr>
<tr><td>2</td><td>15,289</td></tr>
<tr><td>3</td><td>6,688</td></tr>
<tr><td>4</td><td>2,921</td></tr>
<tr><td>5</td><td>1,113</td></tr>
<tr><td>6</td><td>338</td></tr>
<tr><td>7</td><td>89</td></tr>
<tr><td>8</td><td>17</td></tr>
<tr><td>9</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>HBP</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>119,672</td></tr>
<tr><td>1</td><td>13,069</td></tr>
<tr><td>2</td><td>1,489</td></tr>
<tr><td>3</td><td>145</td></tr>
<tr><td>4</td><td>13</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>SO</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>BK</code><span class="code-desc"> — 보크</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>133,517</td></tr>
<tr><td>1</td><td>857</td></tr>
<tr><td>2</td><td>14</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>WP</code><span class="code-desc"> — 폭투</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>122,628</td></tr>
<tr><td>1</td><td>10,595</td></tr>
<tr><td>2</td><td>1,056</td></tr>
<tr><td>3</td><td>93</td></tr>
<tr><td>4</td><td>15</td></tr>
<tr><td>5</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>ER</code><span class="code-desc"> — 자책점</span></summary>
<div class="code-ref">고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>bHome</code><span class="code-desc"> — 홈팀 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>68,683</td></tr>
<tr><td>0</td><td>65,705</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gameID</td><td>20040309LTSS0</td><td>20040309LTSS0</td><td>20040309LTSS0</td></tr>
<tr><td>GYEAR</td><td>2004</td><td>2004</td><td>2004</td></tr>
<tr><td>PlayerName</td><td>°­¹Î¿µ</td><td>°­¿µ½Ä</td><td>°¡µæ¿°</td></tr>
<tr><td>PlayerID</td><td>70531</td><td>70615</td><td>92501</td></tr>
<tr><td>SeqNO</td><td>3</td><td>1</td><td>1</td></tr>
<tr><td>Inning</td><td>1.0</td><td>5.0</td><td>0.2</td></tr>
<tr><td>PA</td><td>3</td><td>22</td><td>5</td></tr>
<tr><td>PitchBallCnt</td><td>0</td><td>9</td><td>3</td></tr>
<tr><td>PitchStrikeCnt</td><td>6</td><td>37</td><td>9</td></tr>
<tr><td>OAB</td><td>3</td><td>20</td><td>4</td></tr>
<tr><td>Run</td><td>0</td><td>3</td><td>3</td></tr>
<tr><td>Hit</td><td>0</td><td>6</td><td>2</td></tr>
<tr><td>HR</td><td>0</td><td>2</td><td>1</td></tr>
<tr><td>SH</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SF</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BB</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>HBP</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>SO</td><td>0</td><td>5</td><td>2</td></tr>
<tr><td>BK</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>WP</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>ER</td><td>0</td><td>3</td><td>3</td></tr>
<tr><td>bHome</td><td>0</td><td>1</td><td>0</td></tr>
</tbody></table>
</div>

</div>
