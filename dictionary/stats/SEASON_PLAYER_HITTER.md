---
title: SEASON_PLAYER_HITTER
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-new">신세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">SEASON_PLAYER_HITTER</div>
  <div class="dict-hero-sub">DB1_BASEBALL_2 &middot; PK: SEASON_ID, P_ID, SECTION_CD, GROUP_IF</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">19,747</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">43</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">D+1</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">통계분석팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_2_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>SEASON_ID, P_ID, SECTION_CD, GROUP_IF</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">new (신세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">통계분석팀 (R-04)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">D+1 (시즌 중)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">43개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">P_ID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 ID (정수)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">SECTION_CD</span></td><td><span class="col-std">section_cd</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">SECTION 코드</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">GROUP_IF</span></td><td><span class="col-std">group_if</span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">GROUP 여부 (Y/N)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">HRA_RT</span></td><td><span class="col-std">hra_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">HRA 비율</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">GAME_CN</span></td><td><span class="col-std">game_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">GAME 건수</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">PA_CN</span></td><td><span class="col-std">pa_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">PA 건수</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">AB_CN</span></td><td><span class="col-std">ab_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">AB 건수</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">RUN_CN</span></td><td><span class="col-std">run_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">RUN 건수</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HIT_CN</span></td><td><span class="col-std">hit_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">HIT 건수</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">H2_CN</span></td><td><span class="col-std">h2_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">H2 건수</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">H3_CN</span></td><td><span class="col-std">h3_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">H3 건수</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">HR_CN</span></td><td><span class="col-std">hr_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">HR 건수</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">XBH_CN</span></td><td><span class="col-std">xbh_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">XBH 건수</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">TB_CN</span></td><td><span class="col-std">tb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">TB 건수</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">MH_HITTER_CN</span></td><td><span class="col-std">mh_hitter_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">MH_HITTER 건수</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">RBI_CN</span></td><td><span class="col-std">rbi_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">RBI 건수</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">SB_CN</span></td><td><span class="col-std">sb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SB 건수</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">CS_CN</span></td><td><span class="col-std">cs_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">CS 건수</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">SB_RT</span></td><td><span class="col-std">sb_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SB 비율</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">RO_CN</span></td><td><span class="col-std">ro_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">RO 건수</span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">POFF_CN</span></td><td><span class="col-std">poff_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">POFF 건수</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">SH_CN</span></td><td><span class="col-std">sh_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SH 건수</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">SF_CN</span></td><td><span class="col-std">sf_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SF 건수</span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">BB_CN</span></td><td><span class="col-std">bb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">BB 건수</span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">IB_CN</span></td><td><span class="col-std">ib_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">IB 건수</span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">HP_CN</span></td><td><span class="col-std">hp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">HP 건수</span></td></tr>
<tr><td class="col-num">30</td><td><span class="col-name">BBHP_CN</span></td><td><span class="col-std">bbhp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">BBHP 건수</span></td></tr>
<tr><td class="col-num">31</td><td><span class="col-name">KK_CN</span></td><td><span class="col-std">kk_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">KK 건수</span></td></tr>
<tr><td class="col-num">32</td><td><span class="col-name">GD_CN</span></td><td><span class="col-std">gd_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">GD 건수</span></td></tr>
<tr><td class="col-num">33</td><td><span class="col-name">ERR_CN</span></td><td><span class="col-std">err_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">ERR 건수</span></td></tr>
<tr><td class="col-num">34</td><td><span class="col-name">WIN_HIT_CN</span></td><td><span class="col-std">win_hit_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">WIN_HIT 건수</span></td></tr>
<tr><td class="col-num">35</td><td><span class="col-name">GO_CN</span></td><td><span class="col-std">go_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">GO 건수</span></td></tr>
<tr><td class="col-num">36</td><td><span class="col-name">FO_CN</span></td><td><span class="col-std">fo_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">FO 건수</span></td></tr>
<tr><td class="col-num">37</td><td><span class="col-name">FOGO_RT</span></td><td><span class="col-std">fogo_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">FOGO 비율</span></td></tr>
<tr><td class="col-num">38</td><td><span class="col-name">PA_PIT_RT</span></td><td><span class="col-std">pa_pit_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">PA_PIT 비율</span></td></tr>
<tr><td class="col-num">39</td><td><span class="col-name">KK_BB_RT</span></td><td><span class="col-std">kk_bb_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">KK_BB 비율</span></td></tr>
<tr><td class="col-num">40</td><td><span class="col-name">SP_HRA_RT</span></td><td><span class="col-std">sp_hra_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SP_HRA 비율</span></td></tr>
<tr><td class="col-num">41</td><td><span class="col-name">PH_HRA_RT</span></td><td><span class="col-std">ph_hra_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">PH_HRA 비율</span></td></tr>
<tr><td class="col-num">42</td><td><span class="col-name">OBP_RT</span></td><td><span class="col-std">obp_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">OBP 비율</span></td></tr>
<tr><td class="col-num">43</td><td><span class="col-name">SLG_RT</span></td><td><span class="col-std">slg_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">SLG 비율</span></td></tr>
<tr><td class="col-num">44</td><td><span class="col-name">ISO_RT</span></td><td><span class="col-std">iso_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">ISO 비율</span></td></tr>
<tr><td class="col-num">45</td><td><span class="col-name">OPS_RT</span></td><td><span class="col-std">ops_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">OPS 비율</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">4개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>SEASON_ID</code><span class="code-desc"> — 시즌 ID</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>P_ID</code><span class="code-desc"> — 선수 ID</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>SECTION_CD</code><span class="code-desc"> — SECTION 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>11,632</td></tr>
<tr><td>2</td><td>8,115</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>GROUP_IF</code><span class="code-desc"> — GROUP 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>LG</td><td>950</td></tr>
<tr><td>HH</td><td>935</td></tr>
<tr><td>SK</td><td>911</td></tr>
<tr><td>HT</td><td>897</td></tr>
<tr><td>LT</td><td>885</td></tr>
<tr><td>OB</td><td>878</td></tr>
<tr><td>SS</td><td>844</td></tr>
<tr><td>WO</td><td>641</td></tr>
<tr><td>NC</td><td>517</td></tr>
<tr><td>KT</td><td>436</td></tr>
<tr><td>2025</td><td>398</td></tr>
<tr><td>2021</td><td>394</td></tr>
<tr><td>2024</td><td>386</td></tr>
<tr><td>2015</td><td>379</td></tr>
<tr><td>2016</td><td>378</td></tr>
<tr><td>2020</td><td>373</td></tr>
<tr><td>2023</td><td>366</td></tr>
<tr><td>2017</td><td>360</td></tr>
<tr><td>2022</td><td>356</td></tr>
<tr><td>2019</td><td>353</td></tr>
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
<tr><td>P_ID</td><td>10005</td><td>30003</td><td>30004</td></tr>
<tr><td>SECTION_CD</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>GROUP_IF</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>HRA_RT</td><td>0.25886523723602295</td><td>0.21052631735801697</td><td>0.25182482600212097</td></tr>
<tr><td>GAME_CN</td><td>76</td><td>12</td><td>80</td></tr>
<tr><td>PA_CN</td><td>323</td><td>22</td><td>299</td></tr>
<tr><td>AB_CN</td><td>282</td><td>19</td><td>274</td></tr>
<tr><td>RUN_CN</td><td>46</td><td>1</td><td>29</td></tr>
<tr><td>HIT_CN</td><td>73</td><td>4</td><td>69</td></tr>
<tr><td>H2_CN</td><td>9</td><td>0</td><td>14</td></tr>
<tr><td>H3_CN</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td>HR_CN</td><td>1</td><td>0</td><td>4</td></tr>
<tr><td>XBH_CN</td><td>11</td><td>0</td><td>20</td></tr>
<tr><td>TB_CN</td><td>87</td><td>4</td><td>99</td></tr>
<tr><td>MH_HITTER_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>RBI_CN</td><td>12</td><td>2</td><td>38</td></tr>
<tr><td>SB_CN</td><td>32</td><td>1</td><td>12</td></tr>
<tr><td>CS_CN</td><td>10</td><td>0</td><td>6</td></tr>
<tr><td>SB_RT</td><td>0.7619047619047619</td><td>1.0</td><td>0.6666666666666666</td></tr>
<tr><td>RO_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>POFF_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SH_CN</td><td>5</td><td>1</td><td>7</td></tr>
<tr><td>SF_CN</td><td>2</td><td>0</td><td>1</td></tr>
<tr><td>BB_CN</td><td>31</td><td>1</td><td>15</td></tr>
<tr><td>IB_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HP_CN</td><td>3</td><td>1</td><td>2</td></tr>
<tr><td>BBHP_CN</td><td>34</td><td>2</td><td>17</td></tr>
<tr><td>KK_CN</td><td>20</td><td>5</td><td>15</td></tr>
<tr><td>GD_CN</td><td>3</td><td>0</td><td>5</td></tr>
<tr><td>ERR_CN</td><td>5</td><td>1</td><td>25</td></tr>
<tr><td>WIN_HIT_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>GO_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>FO_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>FOGO_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>PA_PIT_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>KK_BB_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>SP_HRA_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>PH_HRA_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>OBP_RT</td><td>0.33860759493670883</td><td>0.2857142857142857</td><td>0.29553264604810997</td></tr>
<tr><td>SLG_RT</td><td>0.30851063829787234</td><td>0.21052631578947367</td><td>0.3613138686131387</td></tr>
<tr><td>ISO_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>OPS_RT</td><td>0.648</td><td>0.497</td><td>0.657</td></tr>
</tbody></table>
</div>

</div>
