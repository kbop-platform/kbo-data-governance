---
title: SEASON_PLAYER_HITTER_SITUATION
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">SEASON_PLAYER_HITTER_SITUATION</div>
  <div class="dict-hero-sub">DB1_BASEBALL_2 &middot; PK: SEASON_ID, P_ID, SECTION_CD, SITUATION_IF</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">360,625</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">14</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">D+1</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">통계분석팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_2_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>SEASON_ID, P_ID, SECTION_CD, SITUATION_IF</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 - Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">통계분석팀 (R-04)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">D+1 (시즌 중)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">분석팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">14개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">P_ID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 ID (정수)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">SECTION_CD</span></td><td><span class="col-std">section_cd</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">구간 코드 (SEASON: 1=정규시즌, 2=포스트시즌 / SITUATION: 1=타자투타, 2=투수피투타, 3=아웃수별, 4=이닝별, 5=주자상황별, 6=카운트별, 7=상대투타별)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">SITUATION_IF</span></td><td><span class="col-std">situation_if</span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">상황 구분값 (아웃수 0~3, 이닝 4~12, 주자상태 12/13/23/123, 볼카운트 0-0~3-2, 투타 R/L/RO/LO/RU 등 복합)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">AB_CN</span></td><td><span class="col-std">ab_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">HIT_CN</span></td><td><span class="col-std">hit_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타 수</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">H2_CN</span></td><td><span class="col-std">h2b_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2루타 수</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">H3_CN</span></td><td><span class="col-std">h3b_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">3루타 수</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HR_CN</span></td><td><span class="col-std">hr_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런 수</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">RBI_CN</span></td><td><span class="col-std">rbi_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타점</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">BB_CN</span></td><td><span class="col-std">bb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷 수</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">HP_CN</span></td><td><span class="col-std">hbp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">사구 수</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">KK_CN</span></td><td><span class="col-std">so_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진 수</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">GD_CN</span></td><td><span class="col-std">gidp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">병살타 수</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">4개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>SEASON_ID</code><span class="code-desc"> &mdash; 시즌 ID</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>P_ID</code><span class="code-desc"> &mdash; 선수 ID</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>SECTION_CD</code><span class="code-desc"> &mdash; 구간 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>4</td><td>96,664</td></tr>
<tr><td>6</td><td>89,827</td></tr>
<tr><td>3</td><td>64,106</td></tr>
<tr><td>7</td><td>55,507</td></tr>
<tr><td>5</td><td>27,871</td></tr>
<tr><td>1</td><td>26,650</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>SITUATION_IF</code><span class="code-desc"> &mdash; 상황 구분값</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>2</td><td>32,102</td></tr>
<tr><td>1</td><td>30,109</td></tr>
<tr><td>3</td><td>20,217</td></tr>
<tr><td>0</td><td>18,639</td></tr>
<tr><td>9</td><td>16,424</td></tr>
<tr><td>8</td><td>16,375</td></tr>
<tr><td>7</td><td>16,023</td></tr>
<tr><td>6</td><td>15,256</td></tr>
<tr><td>5</td><td>14,395</td></tr>
<tr><td>4</td><td>12,738</td></tr>
<tr><td>12</td><td>11,408</td></tr>
<tr><td>RO</td><td>9,512</td></tr>
<tr><td>2-1</td><td>8,941</td></tr>
<tr><td>LO</td><td>8,861</td></tr>
<tr><td>2-2</td><td>8,778</td></tr>
<tr><td>0-0</td><td>8,584</td></tr>
<tr><td>2-3</td><td>8,514</td></tr>
<tr><td>2-0</td><td>8,507</td></tr>
<tr><td>1-0</td><td>8,313</td></tr>
<tr><td>1-1</td><td>8,253</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>SEASON_ID</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>P_ID</td><td>10005</td><td>10005</td><td>10005</td></tr>
<tr><td>SECTION_CD</td><td>1</td><td>1</td><td>3</td></tr>
<tr><td>SITUATION_IF</td><td>LO</td><td>RO</td><td>0</td></tr>
<tr><td>AB_CN</td><td>55</td><td>227</td><td>192</td></tr>
<tr><td>HIT_CN</td><td>11</td><td>62</td><td>53</td></tr>
<tr><td>H2_CN</td><td>1</td><td>8</td><td>7</td></tr>
<tr><td>H3_CN</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>HR_CN</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>RBI_CN</td><td>0</td><td>12</td><td>1</td></tr>
<tr><td>BB_CN</td><td>8</td><td>23</td><td>17</td></tr>
<tr><td>HP_CN</td><td>0</td><td>3</td><td>2</td></tr>
<tr><td>KK_CN</td><td>4</td><td>16</td><td>15</td></tr>
<tr><td>GD_CN</td><td>0</td><td>3</td><td>0</td></tr>
</tbody></table>
</div>

</div>
