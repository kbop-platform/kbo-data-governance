---
title: SEASON_PLAYER_PITCHER
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">SEASON_PLAYER_PITCHER</div>
  <div class="dict-hero-sub">DB1_BASEBALL_2 &middot; PK: SEASON_ID, P_ID, SECTION_CD, GROUP_IF</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">13,306</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">54</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">D+1</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">통계분석팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_2_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>SEASON_ID, P_ID, SECTION_CD, GROUP_IF</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 - Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">통계분석팀 (R-04)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">D+1 (시즌 중)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">54개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">P_ID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 ID (정수)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">SECTION_CD</span></td><td><span class="col-std">section_cd</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">구간 코드 (SEASON: 1=정규시즌, 2=포스트시즌 / SITUATION: 1=타자투타, 2=투수피투타, 3=아웃수별, 4=이닝별, 5=주자상황별, 6=카운트별, 7=상대투타별)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">GROUP_IF</span></td><td><span class="col-std">group_if</span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">그룹 구분 (팀코드(HH/LG/SK 등) 또는 시즌연도(2015~2025))</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">ERA_RT</span></td><td><span class="col-std">era_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">평균자책점 (ERA)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">GAME_CN</span></td><td><span class="col-std">game_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">출장 경기 수</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">START_CN</span></td><td><span class="col-std">start_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선발 등판 수</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">QUIT_CN</span></td><td><span class="col-std">quit_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">강판 횟수</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">W_CN</span></td><td><span class="col-std">win_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">승리 수</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">START_W_CN</span></td><td><span class="col-std">start_win_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선발승 수</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">RELIEF_W_CN</span></td><td><span class="col-std">relief_win_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">구원승 수</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">L_CN</span></td><td><span class="col-std">loss_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">패전 수</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">D_CN</span></td><td><span class="col-std">double_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">무승부 수</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">HOLD_CN</span></td><td><span class="col-std">hld_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홀드 수</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">SV_CN</span></td><td><span class="col-std">sv_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">세이브 수</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">SHO_CN</span></td><td><span class="col-std">sho_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">완봉 수</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">CG_CN</span></td><td><span class="col-std">cg_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">완투 수</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">INN2_CN</span></td><td><span class="col-std">ip_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">투구 이닝 수 (⅓이닝 단위)</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">WRA_RT</span></td><td><span class="col-std">wrc_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">승률</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">PA_CN</span></td><td><span class="col-std">pa_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 수</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">AB_CN</span></td><td><span class="col-std">ab_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수</span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">PIT_CN</span></td><td><span class="col-std">pitch_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">투구 수</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">R_CN</span></td><td><span class="col-std">runs_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실점 수</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">ER_CN</span></td><td><span class="col-std">er_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">자책점</span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">HIT_CN</span></td><td><span class="col-std">hit_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타 수</span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">H2_CN</span></td><td><span class="col-std">h2b_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2루타 수</span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">H3_CN</span></td><td><span class="col-std">h3b_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">3루타 수</span></td></tr>
<tr><td class="col-num">30</td><td><span class="col-name">HR_CN</span></td><td><span class="col-std">hr_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런 수</span></td></tr>
<tr><td class="col-num">31</td><td><span class="col-name">SH_CN</span></td><td><span class="col-std">sh_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생번트 수</span></td></tr>
<tr><td class="col-num">32</td><td><span class="col-name">SF_CN</span></td><td><span class="col-std">sf_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생플라이 수</span></td></tr>
<tr><td class="col-num">33</td><td><span class="col-name">BB_CN</span></td><td><span class="col-std">bb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷 수</span></td></tr>
<tr><td class="col-num">34</td><td><span class="col-name">IB_CN</span></td><td><span class="col-std">ibb_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">고의사구 수</span></td></tr>
<tr><td class="col-num">35</td><td><span class="col-name">HP_CN</span></td><td><span class="col-std">hbp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">사구 수</span></td></tr>
<tr><td class="col-num">36</td><td><span class="col-name">BBHP_CN</span></td><td><span class="col-std">bb_hbp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷+사구 합계</span></td></tr>
<tr><td class="col-num">37</td><td><span class="col-name">KK_CN</span></td><td><span class="col-std">so_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진 수</span></td></tr>
<tr><td class="col-num">38</td><td><span class="col-name">GD_CN</span></td><td><span class="col-std">gidp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">병살타 수</span></td></tr>
<tr><td class="col-num">39</td><td><span class="col-name">BK_CN</span></td><td><span class="col-std">bk_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">보크 수</span></td></tr>
<tr><td class="col-num">40</td><td><span class="col-name">WP_CN</span></td><td><span class="col-std">wp_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">폭투 수</span></td></tr>
<tr><td class="col-num">41</td><td><span class="col-name">GO_CN</span></td><td><span class="col-std">go_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">땅볼아웃 수</span></td></tr>
<tr><td class="col-num">42</td><td><span class="col-name">FO_CN</span></td><td><span class="col-std">fo_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">플라이아웃 수</span></td></tr>
<tr><td class="col-num">43</td><td><span class="col-name">FOGO_RT</span></td><td><span class="col-std">fo_go_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">플라이/땅볼 비율 (FO/GO)</span></td></tr>
<tr><td class="col-num">46</td><td><span class="col-name">BS_CN</span></td><td><span class="col-std">bs_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">블론세이브 수</span></td></tr>
<tr><td class="col-num">47</td><td><span class="col-name">QS_CN</span></td><td><span class="col-std">qs_cn</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">퀄리티스타트 수 (QS)</span></td></tr>
<tr><td class="col-num">48</td><td><span class="col-name">WHIP_RT</span></td><td><span class="col-std">whip_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">WHIP (이닝당 출루 허용률)</span></td></tr>
<tr><td class="col-num">49</td><td><span class="col-name">OAVG_RT</span></td><td><span class="col-std">opp_avg_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">피안타율</span></td></tr>
<tr><td class="col-num">50</td><td><span class="col-name">OOBP_RT</span></td><td><span class="col-std">opp_obp_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">피출루율</span></td></tr>
<tr><td class="col-num">51</td><td><span class="col-name">OSLG_RT</span></td><td><span class="col-std">opp_slg_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">피장타율</span></td></tr>
<tr><td class="col-num">52</td><td><span class="col-name">OOPS_RT</span></td><td><span class="col-std">opp_ops_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">피OPS</span></td></tr>
<tr><td class="col-num">53</td><td><span class="col-name">BABIP_RT</span></td><td><span class="col-std">babip_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">BABIP (인플레이 타구 피안타율)</span></td></tr>
<tr><td class="col-num">54</td><td><span class="col-name">GAME_KK_RT</span></td><td><span class="col-std">game_so_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">9이닝당 탈삼진</span></td></tr>
<tr><td class="col-num">55</td><td><span class="col-name">GAME_BB_RT</span></td><td><span class="col-std">game_bb_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">9이닝당 볼넷 허용</span></td></tr>
<tr><td class="col-num">56</td><td><span class="col-name">GAME_PIT_AVG_RT</span></td><td><span class="col-std">game_pitch_avg_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기당 평균 투구수</span></td></tr>
<tr><td class="col-num">57</td><td><span class="col-name">INN_PIT_AVG_RT</span></td><td><span class="col-std">inn_pitch_avg_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝당 평균 투구수</span></td></tr>
<tr><td class="col-num">58</td><td><span class="col-name">BB_KK_RT</span></td><td><span class="col-std">bb_so_rt</span></td><td><span class="col-type">float</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷/삼진 비율 (BB/K)</span></td></tr>
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
<tr><td>1</td><td>7,675</td></tr>
<tr><td>2</td><td>5,631</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>GROUP_IF</code><span class="code-desc"> &mdash; 그룹 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>LG</td><td>657</td></tr>
<tr><td>HH</td><td>652</td></tr>
<tr><td>HT</td><td>639</td></tr>
<tr><td>SK</td><td>617</td></tr>
<tr><td>LT</td><td>616</td></tr>
<tr><td>OB</td><td>616</td></tr>
<tr><td>SS</td><td>587</td></tr>
<tr><td>WO</td><td>461</td></tr>
<tr><td>NC</td><td>351</td></tr>
<tr><td>2021</td><td>308</td></tr>
<tr><td>2024</td><td>291</td></tr>
<tr><td>KT</td><td>289</td></tr>
<tr><td>2023</td><td>285</td></tr>
<tr><td>2020</td><td>283</td></tr>
<tr><td>2025</td><td>281</td></tr>
<tr><td>2022</td><td>281</td></tr>
<tr><td>2018</td><td>260</td></tr>
<tr><td>2019</td><td>257</td></tr>
<tr><td>2016</td><td>250</td></tr>
<tr><td>2015</td><td>244</td></tr>
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
<tr><td>P_ID</td><td>10082</td><td>80620</td><td>82003</td></tr>
<tr><td>SECTION_CD</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>GROUP_IF</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>ERA_RT</td><td>3.85714</td><td>2.46927</td><td>3.3913</td></tr>
<tr><td>GAME_CN</td><td>27</td><td>48</td><td>27</td></tr>
<tr><td>START_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>QUIT_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>W_CN</td><td>6</td><td>15</td><td>7</td></tr>
<tr><td>START_W_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>RELIEF_W_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>L_CN</td><td>5</td><td>11</td><td>6</td></tr>
<tr><td>D_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HOLD_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SV_CN</td><td>3</td><td>11</td><td>0</td></tr>
<tr><td>SHO_CN</td><td>0</td><td>2</td><td>1</td></tr>
<tr><td>CG_CN</td><td>2</td><td>8</td><td>6</td></tr>
<tr><td>INN2_CN</td><td>259</td><td>667</td><td>414</td></tr>
<tr><td>WRA_RT</td><td>0.5454545454545454</td><td>0.5769230769230769</td><td>0.5384615384615384</td></tr>
<tr><td>PA_CN</td><td>365</td><td>864</td><td>566</td></tr>
<tr><td>AB_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>PIT_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>R_CN</td><td>43</td><td>78</td><td>64</td></tr>
<tr><td>ER_CN</td><td>37</td><td>61</td><td>52</td></tr>
<tr><td>HIT_CN</td><td>76</td><td>189</td><td>139</td></tr>
<tr><td>H2_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>H3_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HR_CN</td><td>12</td><td>11</td><td>8</td></tr>
<tr><td>SH_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SF_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BB_CN</td><td>37</td><td>34</td><td>31</td></tr>
<tr><td>IB_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HP_CN</td><td>11</td><td>6</td><td>4</td></tr>
<tr><td>BBHP_CN</td><td>48</td><td>40</td><td>35</td></tr>
<tr><td>KK_CN</td><td>42</td><td>99</td><td>65</td></tr>
<tr><td>GD_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BK_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>WP_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>GO_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>FO_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>FOGO_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>BS_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>QS_CN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>WHIP_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>OAVG_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>OOBP_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>OSLG_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>OOPS_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>BABIP_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>GAME_KK_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>GAME_BB_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>GAME_PIT_AVG_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>INN_PIT_AVG_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
<tr><td>BB_KK_RT</td><td>0.0</td><td>0.0</td><td>0.0</td></tr>
</tbody></table>
</div>

</div>
