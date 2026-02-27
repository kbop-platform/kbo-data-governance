---
title: BatTotal
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">BatTotal</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: PCODE, GYEAR, SEC</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">13,616</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">23</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">D+1</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">통계분석팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>PCODE, GYEAR, SEC</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 - Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">통계분석팀 (R-04)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">D+1 (전일 경기 반영)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [약어 사전](../../standards-dict/abbreviations.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">23개</span></div>

<div class="dict-encoding-warn">`TEAM` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨 (예: `·Ôµ¥`=롯데, `»ï¼º`=삼성). nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">char(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEC</span></td><td><span class="col-std">series_cd</span></td><td><span class="col-type">varchar(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, 9999=통산)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">TEAM</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">varchar(6)</span></td><td></td><td></td><td><span class="col-desc">팀 코드 (HH=한화, LG, SK, HT=KIA, LT=롯데, OB=두산, SS=삼성, WO=키움, NC, KT 등 2자리)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">HRA</span></td><td><span class="col-std">avg</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타율</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">GAMENUM</span></td><td><span class="col-std">game_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 수</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">AB</span></td><td><span class="col-std">ab</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수 (At Bat)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">RUN</span></td><td><span class="col-std">run</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">H2</span></td><td><span class="col-std">h2b</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2루타</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">H3</span></td><td><span class="col-std">h3b</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">3루타</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">TB</span></td><td><span class="col-std">tb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">루타 (Total Bases)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">RBI</span></td><td><span class="col-std">rbi</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타점</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">SB</span></td><td><span class="col-std">sb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">CS</span></td><td><span class="col-std">cs</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루실패</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">SH</span></td><td><span class="col-std">sh</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생번트</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">SF</span></td><td><span class="col-std">sf</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생플라이</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">HP</span></td><td><span class="col-std">hbp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">사구 (Hit by Pitch)</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">KK</span></td><td><span class="col-std">so</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">GD</span></td><td><span class="col-std">gidp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">병살타</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">ERR</span></td><td><span class="col-std">err</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실책</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">5개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> &mdash; 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SEC</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TEAM</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-ref">팀 식별자 - [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TB</code><span class="code-desc"> &mdash; 루타</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>PCODE</td><td>10005</td><td>10005</td><td>10005</td></tr>
<tr><td>GYEAR</td><td>1982</td><td>1983</td><td>1984</td></tr>
<tr><td>SEC</td><td>1982</td><td>1983</td><td>1984</td></tr>
<tr><td>TEAM</td><td>ÇØÅÂ</td><td>»ï¼º</td><td>OB</td></tr>
<tr><td>HRA</td><td>0.259</td><td>0.211</td><td>0.252</td></tr>
<tr><td>GAMENUM</td><td>76</td><td>12</td><td>80</td></tr>
<tr><td>AB</td><td>282</td><td>19</td><td>274</td></tr>
<tr><td>RUN</td><td>46</td><td>1</td><td>29</td></tr>
<tr><td>HIT</td><td>73</td><td>4</td><td>69</td></tr>
<tr><td>H2</td><td>9</td><td>0</td><td>14</td></tr>
<tr><td>H3</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td>HR</td><td>1</td><td>0</td><td>4</td></tr>
<tr><td>TB</td><td>87</td><td>4</td><td>99</td></tr>
<tr><td>RBI</td><td>12</td><td>2</td><td>38</td></tr>
<tr><td>SB</td><td>32</td><td>1</td><td>12</td></tr>
<tr><td>CS</td><td>10</td><td>0</td><td>6</td></tr>
<tr><td>SH</td><td>5</td><td>1</td><td>7</td></tr>
<tr><td>SF</td><td>2</td><td>0</td><td>1</td></tr>
<tr><td>BB</td><td>31</td><td>1</td><td>15</td></tr>
<tr><td>HP</td><td>3</td><td>1</td><td>2</td></tr>
<tr><td>KK</td><td>20</td><td>5</td><td>15</td></tr>
<tr><td>GD</td><td>3</td><td>0</td><td>5</td></tr>
<tr><td>ERR</td><td>5</td><td>1</td><td>25</td></tr>
</tbody></table>
</div>

</div>
