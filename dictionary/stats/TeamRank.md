---
title: TeamRank
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">TeamRank</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GYEAR, SEC, TEAM</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">373</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">30</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">D+1</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">통계분석팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GYEAR, SEC, TEAM</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">통계분석팀 (R-04)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">D+1 (전일 경기 반영)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">미디어, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">30개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">nvarchar(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">SEC</span></td><td><span class="col-std">series_cd</span></td><td><span class="col-type">varchar(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">구간 (시즌연도 또는 &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">RANK</span></td><td><span class="col-std">rank_no</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">순위</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">LEAGUE</span></td><td><span class="col-std">league_nm</span></td><td><span class="col-type">char(5)</span></td><td></td><td></td><td><span class="col-desc">리그</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">TEAM</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">nvarchar(6)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">팀 코드 (2자리, HH=키움, HT=KIA 등)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">GAME</span></td><td><span class="col-std">game_cn</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">경기 수</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">WIN</span></td><td><span class="col-std">win_cn</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">승</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">LOSE</span></td><td><span class="col-std">lose_cn</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">패</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">SAME</span></td><td><span class="col-std">draw_cn</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">무승부</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">WRA</span></td><td><span class="col-std">win_rt</span></td><td><span class="col-type">real</span></td><td></td><td></td><td><span class="col-desc">승률</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">AB</span></td><td><span class="col-std">ab</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">타수 (At Bat)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">SB</span></td><td><span class="col-std">sb</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">도루</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">RUN</span></td><td><span class="col-std">run</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">INN</span></td><td><span class="col-std">inn_no</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">이닝 번호</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">INN2</span></td><td><span class="col-std">inn_detail_no</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">이닝 세부 (아웃수 환산 또는 연장 구분)</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">R</span></td><td><span class="col-std">r</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">실점</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">ER</span></td><td><span class="col-std">er</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">자책점</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">ERR</span></td><td><span class="col-std">err</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">실책</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">HRA</span></td><td><span class="col-std">avg</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">타율</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">LRA</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">BRA</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">ERA</span></td><td><span class="col-std">era</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">평균자책점</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">continue</span></td><td><span class="col-std">continue_cn</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">연속 기록</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">H2</span></td><td><span class="col-std">h2b</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">2루타</span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">H3</span></td><td><span class="col-std">h3b</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">3루타</span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">HP</span></td><td><span class="col-std">hbp</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">사구 (Hit by Pitch)</span></td></tr>
<tr><td class="col-num">30</td><td><span class="col-name">SF</span></td><td><span class="col-std">sf</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">희생플라이</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">5개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> — 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SEC</code><span class="code-desc"> — 구간</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>LEAGUE</code><span class="code-desc"> — 리그</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>154</td></tr>
<tr><td>magic</td><td>8</td></tr>
<tr><td>dream</td><td>8</td></tr>
<tr><td>0</td><td>8</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>TEAM</code><span class="code-desc"> — 팀 코드</span></summary>
<div class="code-ref">팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INN</code><span class="code-desc"> — 이닝 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>10</td></tr>
<tr><td>1108 1/3</td><td>3</td></tr>
<tr><td>1115 2/3</td><td>3</td></tr>
<tr><td>1119</td><td>3</td></tr>
<tr><td>1120 2/3</td><td>3</td></tr>
<tr><td>1121 1/3</td><td>3</td></tr>
<tr><td>1123 2/3</td><td>3</td></tr>
<tr><td>1128</td><td>3</td></tr>
<tr><td>1129</td><td>3</td></tr>
<tr><td>1129 1/3</td><td>3</td></tr>
<tr><td>1134 2/3</td><td>3</td></tr>
<tr><td>1163 2/3</td><td>3</td></tr>
<tr><td>1181 1/3</td><td>3</td></tr>
<tr><td>1183</td><td>3</td></tr>
<tr><td>1186 1/3</td><td>3</td></tr>
<tr><td>1264</td><td>3</td></tr>
<tr><td>1268 2/3</td><td>3</td></tr>
<tr><td>1269</td><td>3</td></tr>
<tr><td>1271</td><td>3</td></tr>
<tr><td>1272 1/3</td><td>3</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GYEAR</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>SEC</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>RANK</td><td>5</td><td>6</td><td>2</td></tr>
<tr><td>LEAGUE</td><td>dream</td><td>dream</td><td>magic</td></tr>
<tr><td>TEAM</td><td>롯데</td><td>삼미</td><td>삼성</td></tr>
<tr><td>GAME</td><td>80</td><td>80</td><td>80</td></tr>
<tr><td>WIN</td><td>31</td><td>15</td><td>54</td></tr>
<tr><td>LOSE</td><td>49</td><td>65</td><td>26</td></tr>
<tr><td>SAME</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>WRA</td><td>0.3880000114440918</td><td>0.18799999356269836</td><td>0.675000011920929</td></tr>
<tr><td>AB</td><td>2628</td><td>2653</td><td>2649</td></tr>
<tr><td>HIT</td><td>674</td><td>637</td><td>705</td></tr>
<tr><td>HR</td><td>59</td><td>40</td><td>57</td></tr>
<tr><td>SB</td><td>84</td><td>74</td><td>147</td></tr>
<tr><td>RUN</td><td>353</td><td>302</td><td>425</td></tr>
<tr><td>INN</td><td>713 2/3</td><td>692</td><td>704 1/3</td></tr>
<tr><td>INN2</td><td>2141</td><td>2076</td><td>2113</td></tr>
<tr><td>R</td><td>385</td><td>574</td><td>257</td></tr>
<tr><td>ER</td><td>313</td><td>478</td><td>211</td></tr>
<tr><td>ERR</td><td>97</td><td>117</td><td>81</td></tr>
<tr><td>HRA</td><td>0.256</td><td>0.240</td><td>0.266</td></tr>
<tr><td>LRA</td><td>0.373</td><td>0.345</td><td>0.392</td></tr>
<tr><td>BRA</td><td>0.347</td><td>0.306</td><td>0.349</td></tr>
<tr><td>ERA</td><td>3.95</td><td>6.22</td><td>2.70</td></tr>
<tr><td>continue</td><td>2ÆÐ</td><td>1ÆÐ</td><td>2½Â</td></tr>
<tr><td>H2</td><td>112</td><td>117</td><td>126</td></tr>
<tr><td>H3</td><td>8</td><td>20</td><td>18</td></tr>
<tr><td>BB</td><td>326</td><td>221</td><td>307</td></tr>
<tr><td>HP</td><td>40</td><td>29</td><td>30</td></tr>
<tr><td>SF</td><td>27</td><td>19</td><td>18</td></tr>
</tbody></table>
</div>

</div>
