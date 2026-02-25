---
title: Pitcher
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">Pitcher</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GMKEY, GDAY, PCODE</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">223,624</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">36</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY, PCODE</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 — Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀, 통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">36개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">TB</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">팀 구분 (T=원정/Top, B=홈/Bottom)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">선수명 (varchar=EUC-KR 깨짐 가능)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자 문자열)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">POS</span></td><td><span class="col-std">position_cd</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">포지션 코드</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">START</span></td><td><span class="col-std">start_if</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">선발 여부</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">QUIT</span></td><td><span class="col-std">quit_if</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">종료 여부</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">CG</span></td><td><span class="col-std">cg</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">완투</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">SHO</span></td><td><span class="col-std">sho</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">완봉</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">WLS</span></td><td><span class="col-std">wls_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">승패세 (W=승, L=패, S=세이브)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HOLD</span></td><td><span class="col-std">hold_cn</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홀드</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">INN</span></td><td><span class="col-std">inn_no</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">이닝 번호</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">INN2</span></td><td><span class="col-std">inn_detail_no</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝 세부 (아웃수 환산 또는 연장 구분)</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">BF</span></td><td><span class="col-std">bf</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">상대타자수</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">PA</span></td><td><span class="col-std">pa</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 (Plate Appearance)</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">AB</span></td><td><span class="col-std">ab</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수 (At Bat)</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">H2</span></td><td><span class="col-std">h2b</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2루타</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">H3</span></td><td><span class="col-std">h3b</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">3루타</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">SB</span></td><td><span class="col-std">sb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">CS</span></td><td><span class="col-std">cs</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루실패</span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">SH</span></td><td><span class="col-std">sh</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생번트</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">SF</span></td><td><span class="col-std">sf</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생플라이</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">IB</span></td><td><span class="col-std">ibb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">고의사구 (Intentional BB)</span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">HP</span></td><td><span class="col-std">hbp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">사구 (Hit by Pitch)</span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">KK</span></td><td><span class="col-std">so</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진</span></td></tr>
<tr><td class="col-num">30</td><td><span class="col-name">GD</span></td><td><span class="col-std">gidp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">병살타</span></td></tr>
<tr><td class="col-num">31</td><td><span class="col-name">WP</span></td><td><span class="col-std">wp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">폭투</span></td></tr>
<tr><td class="col-num">32</td><td><span class="col-name">BK</span></td><td><span class="col-std">bk</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">보크</span></td></tr>
<tr><td class="col-num">33</td><td><span class="col-name">ERR</span></td><td><span class="col-std">err</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실책</span></td></tr>
<tr><td class="col-num">34</td><td><span class="col-name">R</span></td><td><span class="col-std">r</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실점</span></td></tr>
<tr><td class="col-num">35</td><td><span class="col-name">ER</span></td><td><span class="col-std">er</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">자책점</span></td></tr>
<tr><td class="col-num">36</td><td><span class="col-name">BS</span></td><td><span class="col-std"></span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">9개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> — 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB</code><span class="code-desc"> — 팀 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>113,318</td></tr>
<tr><td>T</td><td>110,306</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>POS</code><span class="code-desc"> — 포지션 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>11</td><td>47,158</td></tr>
<tr><td>21</td><td>43,635</td></tr>
<tr><td>31</td><td>35,837</td></tr>
<tr><td>41</td><td>25,695</td></tr>
<tr><td>51</td><td>14,683</td></tr>
<tr><td>61</td><td>6,444</td></tr>
<tr><td>71</td><td>2,227</td></tr>
<tr><td>81</td><td>620</td></tr>
<tr><td>91</td><td>135</td></tr>
<tr><td>A1</td><td>26</td></tr>
<tr><td>B1</td><td>5</td></tr>
<tr><td></td><td>1</td></tr>
<tr><td>C1</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>START</code><span class="code-desc"> — 선발 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>47,158</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>QUIT</code><span class="code-desc"> — 종료 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>47,158</td></tr>
<tr><td>0</td><td>2,757</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>WLS</code><span class="code-desc"> — 승패세</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>116,107</td></tr>
<tr><td>L</td><td>46,130</td></tr>
<tr><td>W</td><td>46,130</td></tr>
<tr><td>S</td><td>10,707</td></tr>
<tr><td>0</td><td>2,494</td></tr>
<tr><td>D</td><td>2,056</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>HOLD</code><span class="code-desc"> — 홀드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>203,351</td></tr>
<tr><td>1</td><td>16,915</td></tr>
<tr><td>2</td><td>2,426</td></tr>
<tr><td>3</td><td>786</td></tr>
<tr><td>4</td><td>126</td></tr>
<tr><td>5</td><td>17</td></tr>
<tr><td>6</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN</code><span class="code-desc"> — 이닝 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>41,256</td></tr>
<tr><td>9</td><td>34,662</td></tr>
<tr><td>0 1/3</td><td>18,581</td></tr>
<tr><td>0 2/3</td><td>17,488</td></tr>
<tr><td>8</td><td>12,673</td></tr>
<tr><td>1 1/3</td><td>11,710</td></tr>
<tr><td>2</td><td>11,380</td></tr>
<tr><td>1 2/3</td><td>8,700</td></tr>
<tr><td>6</td><td>7,451</td></tr>
<tr><td>0</td><td>7,150</td></tr>
<tr><td>5</td><td>6,722</td></tr>
<tr><td>3</td><td>5,386</td></tr>
<tr><td>7</td><td>4,924</td></tr>
<tr><td>2 1/3</td><td>4,196</td></tr>
<tr><td>4</td><td>3,688</td></tr>
<tr><td>2 2/3</td><td>3,564</td></tr>
<tr><td>3 1/3</td><td>2,531</td></tr>
<tr><td>5 1/3</td><td>2,521</td></tr>
<tr><td>3 2/3</td><td>2,290</td></tr>
<tr><td>5 2/3</td><td>2,197</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>19820327SSLG0</td><td>19820327SSLG0</td><td>19820327SSLG0</td></tr>
<tr><td>GDAY</td><td>19820327</td><td>19820327</td><td>19820327</td></tr>
<tr><td>TB</td><td>T</td><td>B</td><td>B</td></tr>
<tr><td>NAME</td><td>È²±ÔºÀ</td><td>ÀÌ±æÈ¯</td><td>À¯Á¾°â</td></tr>
<tr><td>PCODE</td><td>80620</td><td>82122</td><td>82175</td></tr>
<tr><td>POS</td><td>11</td><td>11</td><td>21</td></tr>
<tr><td>START</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>QUIT</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>CG</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SHO</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>WLS</td><td></td><td></td><td>W</td></tr>
<tr><td>HOLD</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>INN</td><td>6 2/3</td><td>2</td><td>8</td></tr>
<tr><td>INN2</td><td>20</td><td>6</td><td>24</td></tr>
<tr><td>BF</td><td>105</td><td>50</td><td>116</td></tr>
<tr><td>PA</td><td>31</td><td>13</td><td>31</td></tr>
<tr><td>AB</td><td>28</td><td>10</td><td>29</td></tr>
<tr><td>HIT</td><td>12</td><td>3</td><td>7</td></tr>
<tr><td>H2</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>H3</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>HR</td><td>2</td><td>0</td><td>1</td></tr>
<tr><td>SB</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>CS</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SH</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>SF</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BB</td><td>3</td><td>2</td><td>1</td></tr>
<tr><td>IB</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HP</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>KK</td><td>2</td><td>0</td><td>5</td></tr>
<tr><td>GD</td><td>2</td><td>0</td><td>1</td></tr>
<tr><td>WP</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BK</td><td>1</td><td>2</td><td>0</td></tr>
<tr><td>ERR</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>R</td><td>7</td><td>5</td><td>2</td></tr>
<tr><td>ER</td><td>7</td><td>2</td><td>2</td></tr>
<tr><td>BS</td><td>0</td><td>0</td><td>0</td></tr>
</tbody></table>
</div>

</div>
