---
title: KBO_BATRESULT
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">KBO_BATRESULT</div>
  <div class="dict-hero-sub">DB2_BASEBALL &middot; PK: GMKEY, GDAY, PCODE</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">424,921</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">90</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY, PCODE</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">분석팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[코드 사전](../../standards/code-dictionary.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">90개</span></div>

<div class="dict-encoding-warn">`POSITION` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">TB</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 구분 (T=원정/Top, B=홈/Bottom)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(16)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선수명 (varchar=EUC-KR 깨짐 가능)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자 문자열)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">TURN</span></td><td><span class="col-std">turn_no</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타순</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">ONETURN</span></td><td><span class="col-std">one_turn_if</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타순 (1~9)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">POSITION</span></td><td><span class="col-std">position_nm</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">포지션</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">CHANGEINN</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">INN1</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">IL1</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">INN1_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">INN2</span></td><td><span class="col-std">inn_detail_no</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝 세부 (아웃수 환산 또는 연장 구분)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">IL2</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">INN2_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">INN3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">IL3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">INN3_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">INN4</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">IL4</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">INN4_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">INN5</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">IL5</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">INN5_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">INN6</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">IL6</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">INN6_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">INN7</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">IL7</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">30</td><td><span class="col-name">INN7_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">31</td><td><span class="col-name">INN8</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">32</td><td><span class="col-name">IL8</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">33</td><td><span class="col-name">INN8_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">34</td><td><span class="col-name">INN9</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">35</td><td><span class="col-name">IL9</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">36</td><td><span class="col-name">INN9_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">37</td><td><span class="col-name">INN10</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">38</td><td><span class="col-name">IL10</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">39</td><td><span class="col-name">INN10_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">40</td><td><span class="col-name">INN11</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">41</td><td><span class="col-name">IL11</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">42</td><td><span class="col-name">INN11_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">43</td><td><span class="col-name">INN12</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">44</td><td><span class="col-name">IL12</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">45</td><td><span class="col-name">INN12_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">46</td><td><span class="col-name">INN13</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">47</td><td><span class="col-name">IL13</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">48</td><td><span class="col-name">INN13_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">49</td><td><span class="col-name">INN14</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">50</td><td><span class="col-name">IL14</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">51</td><td><span class="col-name">INN14_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">52</td><td><span class="col-name">INN15</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">53</td><td><span class="col-name">IL15</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">54</td><td><span class="col-name">INN15_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">55</td><td><span class="col-name">INN16</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">56</td><td><span class="col-name">IL16</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">57</td><td><span class="col-name">INN16_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">58</td><td><span class="col-name">INN17</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">59</td><td><span class="col-name">IL17</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">60</td><td><span class="col-name">INN17_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">61</td><td><span class="col-name">INN18</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">62</td><td><span class="col-name">IL18</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">63</td><td><span class="col-name">INN18_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">64</td><td><span class="col-name">INN19</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">65</td><td><span class="col-name">IL19</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">66</td><td><span class="col-name">INN19_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">67</td><td><span class="col-name">INN20</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">68</td><td><span class="col-name">IL20</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">69</td><td><span class="col-name">INN20_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">70</td><td><span class="col-name">INN21</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">71</td><td><span class="col-name">IL21</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">72</td><td><span class="col-name">INN21_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">73</td><td><span class="col-name">INN22</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">74</td><td><span class="col-name">IL22</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">75</td><td><span class="col-name">INN22_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">76</td><td><span class="col-name">INN23</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">77</td><td><span class="col-name">IL23</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">78</td><td><span class="col-name">INN23_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">79</td><td><span class="col-name">INN24</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">80</td><td><span class="col-name">IL24</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">81</td><td><span class="col-name">INN24_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">82</td><td><span class="col-name">INN25</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">83</td><td><span class="col-name">IL25</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">84</td><td><span class="col-name">INN25_3</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">85</td><td><span class="col-name">AB</span></td><td><span class="col-std">ab</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수 (At Bat)</span></td></tr>
<tr><td class="col-num">86</td><td><span class="col-name">RUN</span></td><td><span class="col-std">run</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">87</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">88</td><td><span class="col-name">RBI</span></td><td><span class="col-std">rbi</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타점</span></td></tr>
<tr><td class="col-num">89</td><td><span class="col-name">AVGS</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">90</td><td><span class="col-name">AVG5</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">88개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> — 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB</code><span class="code-desc"> — 팀 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>212,502</td></tr>
<tr><td>T</td><td>212,419</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TURN</code><span class="code-desc"> — 타순</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>ONETURN</code><span class="code-desc"> — 타순</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>8</td><td>50,344</td></tr>
<tr><td>9</td><td>49,664</td></tr>
<tr><td>7</td><td>45,012</td></tr>
<tr><td>6</td><td>43,392</td></tr>
<tr><td>5</td><td>42,403</td></tr>
<tr><td>2</td><td>42,382</td></tr>
<tr><td>4</td><td>41,207</td></tr>
<tr><td>1</td><td>39,788</td></tr>
<tr><td>3</td><td>39,786</td></tr>
<tr><td></td><td>30,943</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>POSITION</code><span class="code-desc"> — 포지션</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>Æ÷</td><td>42,442</td></tr>
<tr><td>ì£</td><td>35,608</td></tr>
<tr><td>À¯</td><td>34,904</td></tr>
<tr><td>ß²</td><td>34,139</td></tr>
<tr><td>ÁÂ</td><td>33,955</td></tr>
<tr><td>ìé</td><td>33,555</td></tr>
<tr><td>¿ì</td><td>32,709</td></tr>
<tr><td>Áß</td><td>31,879</td></tr>
<tr><td></td><td>30,943</td></tr>
<tr><td>Áö</td><td>30,028</td></tr>
<tr><td>Å¸</td><td>24,620</td></tr>
<tr><td>ÁÖ</td><td>7,691</td></tr>
<tr><td>Åõ</td><td>3,275</td></tr>
<tr><td>Å¸ÁÂ</td><td>2,976</td></tr>
<tr><td>Å¸¿ì</td><td>2,471</td></tr>
<tr><td>Å¸ìé</td><td>2,452</td></tr>
<tr><td>Å¸Æ÷</td><td>2,250</td></tr>
<tr><td>Å¸ì£</td><td>2,076</td></tr>
<tr><td>ÁÖÁÂ</td><td>2,019</td></tr>
<tr><td>ÁÖì£</td><td>1,917</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>CHANGEINN</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 16종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INN1</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>287,636</td></tr>
<tr><td>»ïÁø</td><td>22,633</td></tr>
<tr><td>4±¸</td><td>13,839</td></tr>
<tr><td>À¯¶¥</td><td>7,753</td></tr>
<tr><td>2¶¥</td><td>7,543</td></tr>
<tr><td>Áßºñ</td><td>7,512</td></tr>
<tr><td>Áß¾È</td><td>6,755</td></tr>
<tr><td>ÁÂºñ</td><td>6,313</td></tr>
<tr><td>ÁÂ¾È</td><td>6,161</td></tr>
<tr><td>¿ìºñ</td><td>5,883</td></tr>
<tr><td>¿ì¾È</td><td>5,688</td></tr>
<tr><td>3¶¥</td><td>4,344</td></tr>
<tr><td>1¶¥</td><td>3,985</td></tr>
<tr><td>Åõ¶¥</td><td>2,783</td></tr>
<tr><td>À¯ºñ</td><td>1,927</td></tr>
<tr><td>»ç±¸</td><td>1,904</td></tr>
<tr><td>ÁÂ2</td><td>1,825</td></tr>
<tr><td>2ºñ</td><td>1,694</td></tr>
<tr><td>¿ì2</td><td>1,377</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,193</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL1</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,492</td></tr>
<tr><td>»ïÁø</td><td>49</td></tr>
<tr><td>4±¸</td><td>38</td></tr>
<tr><td>ÁÂ¾È</td><td>31</td></tr>
<tr><td>2¶¥</td><td>30</td></tr>
<tr><td>ÁÂºñ</td><td>26</td></tr>
<tr><td>¿ì¾È</td><td>23</td></tr>
<tr><td>1¶¥</td><td>22</td></tr>
<tr><td>Áßºñ</td><td>22</td></tr>
<tr><td>À¯¶¥</td><td>21</td></tr>
<tr><td>3¶¥</td><td>19</td></tr>
<tr><td>Áß¾È</td><td>19</td></tr>
<tr><td>¿ìºñ</td><td>15</td></tr>
<tr><td>ÁÂ2</td><td>12</td></tr>
<tr><td>»ç±¸</td><td>10</td></tr>
<tr><td>À¯ºñ</td><td>10</td></tr>
<tr><td>Åõ¶¥</td><td>9</td></tr>
<tr><td>¿ì2</td><td>7</td></tr>
<tr><td>¿ìÁß2</td><td>7</td></tr>
<tr><td>À¯Á÷</td><td>6</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN1_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN2</code><span class="code-desc"> — 이닝 세부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>292,139</td></tr>
<tr><td>»ïÁø</td><td>23,316</td></tr>
<tr><td>4±¸</td><td>11,177</td></tr>
<tr><td>À¯¶¥</td><td>8,182</td></tr>
<tr><td>Áßºñ</td><td>7,234</td></tr>
<tr><td>2¶¥</td><td>6,549</td></tr>
<tr><td>Áß¾È</td><td>6,393</td></tr>
<tr><td>¿ìºñ</td><td>6,221</td></tr>
<tr><td>ÁÂ¾È</td><td>6,087</td></tr>
<tr><td>ÁÂºñ</td><td>5,597</td></tr>
<tr><td>¿ì¾È</td><td>5,263</td></tr>
<tr><td>3¶¥</td><td>5,262</td></tr>
<tr><td>1¶¥</td><td>3,212</td></tr>
<tr><td>Åõ¶¥</td><td>2,635</td></tr>
<tr><td>À¯ºñ</td><td>1,887</td></tr>
<tr><td>2ºñ</td><td>1,875</td></tr>
<tr><td>»ç±¸</td><td>1,869</td></tr>
<tr><td>ÁÂ2</td><td>1,803</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,389</td></tr>
<tr><td>¿ì2</td><td>1,209</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL2</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,495</td></tr>
<tr><td>»ïÁø</td><td>66</td></tr>
<tr><td>À¯¶¥</td><td>34</td></tr>
<tr><td>4±¸</td><td>33</td></tr>
<tr><td>ÁÂ¾È</td><td>26</td></tr>
<tr><td>Áßºñ</td><td>26</td></tr>
<tr><td>Áß¾È</td><td>26</td></tr>
<tr><td>2¶¥</td><td>23</td></tr>
<tr><td>ÁÂºñ</td><td>21</td></tr>
<tr><td>¿ìºñ</td><td>19</td></tr>
<tr><td>¿ì¾È</td><td>17</td></tr>
<tr><td>3¶¥</td><td>13</td></tr>
<tr><td>1¶¥</td><td>12</td></tr>
<tr><td>À¯ºñ</td><td>11</td></tr>
<tr><td>ÁÂÈ¨</td><td>10</td></tr>
<tr><td>ÁÂ2</td><td>9</td></tr>
<tr><td>2ºñ</td><td>7</td></tr>
<tr><td>1ÆÄ</td><td>5</td></tr>
<tr><td>1ºñ</td><td>5</td></tr>
<tr><td>ÁßÈ¨</td><td>5</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN2_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>289,111</td></tr>
<tr><td>»ïÁø</td><td>21,374</td></tr>
<tr><td>4±¸</td><td>11,851</td></tr>
<tr><td>À¯¶¥</td><td>8,203</td></tr>
<tr><td>Áßºñ</td><td>7,541</td></tr>
<tr><td>2¶¥</td><td>7,119</td></tr>
<tr><td>Áß¾È</td><td>6,587</td></tr>
<tr><td>ÁÂ¾È</td><td>6,392</td></tr>
<tr><td>¿ìºñ</td><td>6,194</td></tr>
<tr><td>ÁÂºñ</td><td>5,942</td></tr>
<tr><td>¿ì¾È</td><td>5,673</td></tr>
<tr><td>3¶¥</td><td>5,021</td></tr>
<tr><td>1¶¥</td><td>3,764</td></tr>
<tr><td>Åõ¶¥</td><td>2,825</td></tr>
<tr><td>À¯ºñ</td><td>1,940</td></tr>
<tr><td>»ç±¸</td><td>1,908</td></tr>
<tr><td>ÁÂ2</td><td>1,866</td></tr>
<tr><td>2ºñ</td><td>1,747</td></tr>
<tr><td>¿ì2</td><td>1,419</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,368</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,405</td></tr>
<tr><td>»ïÁø</td><td>74</td></tr>
<tr><td>4±¸</td><td>47</td></tr>
<tr><td>À¯¶¥</td><td>34</td></tr>
<tr><td>Áß¾È</td><td>32</td></tr>
<tr><td>¿ì¾È</td><td>27</td></tr>
<tr><td>ÁÂ¾È</td><td>26</td></tr>
<tr><td>Áßºñ</td><td>26</td></tr>
<tr><td>¿ìºñ</td><td>25</td></tr>
<tr><td>2¶¥</td><td>24</td></tr>
<tr><td>ÁÂºñ</td><td>24</td></tr>
<tr><td>1¶¥</td><td>17</td></tr>
<tr><td>3¶¥</td><td>14</td></tr>
<tr><td>Åõ¶¥</td><td>14</td></tr>
<tr><td>»ç±¸</td><td>12</td></tr>
<tr><td>2ºñ</td><td>11</td></tr>
<tr><td>ÁÂ2</td><td>9</td></tr>
<tr><td>¿ì2</td><td>7</td></tr>
<tr><td>ÁÂÁß2</td><td>7</td></tr>
<tr><td>¿ìÁß¾È</td><td>6</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN3_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,919</td></tr>
<tr><td>Áß2</td><td>1</td></tr>
<tr><td>ÁÂºñ</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN4</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>289,566</td></tr>
<tr><td>»ïÁø</td><td>21,801</td></tr>
<tr><td>4±¸</td><td>11,756</td></tr>
<tr><td>À¯¶¥</td><td>8,111</td></tr>
<tr><td>Áßºñ</td><td>7,769</td></tr>
<tr><td>¿ìºñ</td><td>6,532</td></tr>
<tr><td>2¶¥</td><td>6,486</td></tr>
<tr><td>Áß¾È</td><td>6,439</td></tr>
<tr><td>ÁÂ¾È</td><td>6,417</td></tr>
<tr><td>ÁÂºñ</td><td>5,880</td></tr>
<tr><td>¿ì¾È</td><td>5,358</td></tr>
<tr><td>3¶¥</td><td>5,170</td></tr>
<tr><td>1¶¥</td><td>3,498</td></tr>
<tr><td>Åõ¶¥</td><td>2,755</td></tr>
<tr><td>ÁÂ2</td><td>1,994</td></tr>
<tr><td>»ç±¸</td><td>1,940</td></tr>
<tr><td>À¯ºñ</td><td>1,842</td></tr>
<tr><td>2ºñ</td><td>1,830</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,500</td></tr>
<tr><td>¿ì2</td><td>1,377</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL4</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,444</td></tr>
<tr><td>»ïÁø</td><td>82</td></tr>
<tr><td>4±¸</td><td>46</td></tr>
<tr><td>Áßºñ</td><td>40</td></tr>
<tr><td>À¯¶¥</td><td>32</td></tr>
<tr><td>Áß¾È</td><td>23</td></tr>
<tr><td>¿ì¾È</td><td>22</td></tr>
<tr><td>3¶¥</td><td>22</td></tr>
<tr><td>2¶¥</td><td>22</td></tr>
<tr><td>ÁÂ¾È</td><td>20</td></tr>
<tr><td>1¶¥</td><td>17</td></tr>
<tr><td>¿ìºñ</td><td>17</td></tr>
<tr><td>ÁÂºñ</td><td>17</td></tr>
<tr><td>ÁÂÁß2</td><td>11</td></tr>
<tr><td>À¯ºñ</td><td>9</td></tr>
<tr><td>2ºñ</td><td>7</td></tr>
<tr><td>1ÆÄ</td><td>6</td></tr>
<tr><td>1ºñ</td><td>6</td></tr>
<tr><td>¿ì2</td><td>6</td></tr>
<tr><td>»ç±¸</td><td>6</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN4_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN5</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>289,352</td></tr>
<tr><td>»ïÁø</td><td>21,912</td></tr>
<tr><td>4±¸</td><td>11,529</td></tr>
<tr><td>À¯¶¥</td><td>8,210</td></tr>
<tr><td>Áßºñ</td><td>7,620</td></tr>
<tr><td>2¶¥</td><td>6,868</td></tr>
<tr><td>Áß¾È</td><td>6,628</td></tr>
<tr><td>¿ìºñ</td><td>6,391</td></tr>
<tr><td>ÁÂ¾È</td><td>6,332</td></tr>
<tr><td>ÁÂºñ</td><td>5,990</td></tr>
<tr><td>¿ì¾È</td><td>5,528</td></tr>
<tr><td>3¶¥</td><td>4,948</td></tr>
<tr><td>1¶¥</td><td>3,489</td></tr>
<tr><td>Åõ¶¥</td><td>2,837</td></tr>
<tr><td>ÁÂ2</td><td>1,903</td></tr>
<tr><td>À¯ºñ</td><td>1,892</td></tr>
<tr><td>»ç±¸</td><td>1,794</td></tr>
<tr><td>2ºñ</td><td>1,739</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,362</td></tr>
<tr><td>¿ì2</td><td>1,351</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL5</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,421</td></tr>
<tr><td>»ïÁø</td><td>78</td></tr>
<tr><td>4±¸</td><td>48</td></tr>
<tr><td>¿ìºñ</td><td>30</td></tr>
<tr><td>Áßºñ</td><td>28</td></tr>
<tr><td>2¶¥</td><td>26</td></tr>
<tr><td>À¯¶¥</td><td>26</td></tr>
<tr><td>ÁÂ¾È</td><td>26</td></tr>
<tr><td>Áß¾È</td><td>25</td></tr>
<tr><td>¿ì¾È</td><td>24</td></tr>
<tr><td>3¶¥</td><td>21</td></tr>
<tr><td>ÁÂºñ</td><td>20</td></tr>
<tr><td>1¶¥</td><td>12</td></tr>
<tr><td>Åõ¶¥</td><td>10</td></tr>
<tr><td>2ºñ</td><td>8</td></tr>
<tr><td>1ÆÄ</td><td>8</td></tr>
<tr><td>»ç±¸</td><td>8</td></tr>
<tr><td>3ºñ</td><td>7</td></tr>
<tr><td>¿ìÁß2</td><td>7</td></tr>
<tr><td>Æ÷ÆÄ</td><td>6</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN5_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN6</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>289,554</td></tr>
<tr><td>»ïÁø</td><td>22,944</td></tr>
<tr><td>4±¸</td><td>12,238</td></tr>
<tr><td>À¯¶¥</td><td>8,051</td></tr>
<tr><td>Áßºñ</td><td>7,531</td></tr>
<tr><td>2¶¥</td><td>6,705</td></tr>
<tr><td>Áß¾È</td><td>6,291</td></tr>
<tr><td>¿ìºñ</td><td>6,283</td></tr>
<tr><td>ÁÂ¾È</td><td>6,261</td></tr>
<tr><td>ÁÂºñ</td><td>5,764</td></tr>
<tr><td>¿ì¾È</td><td>5,383</td></tr>
<tr><td>3¶¥</td><td>4,920</td></tr>
<tr><td>1¶¥</td><td>3,395</td></tr>
<tr><td>Åõ¶¥</td><td>2,718</td></tr>
<tr><td>»ç±¸</td><td>1,931</td></tr>
<tr><td>ÁÂ2</td><td>1,845</td></tr>
<tr><td>À¯ºñ</td><td>1,843</td></tr>
<tr><td>2ºñ</td><td>1,727</td></tr>
<tr><td>¿ì2</td><td>1,335</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,317</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL6</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,461</td></tr>
<tr><td>»ïÁø</td><td>85</td></tr>
<tr><td>4±¸</td><td>33</td></tr>
<tr><td>À¯¶¥</td><td>31</td></tr>
<tr><td>2¶¥</td><td>28</td></tr>
<tr><td>Áßºñ</td><td>25</td></tr>
<tr><td>3¶¥</td><td>21</td></tr>
<tr><td>¿ìºñ</td><td>20</td></tr>
<tr><td>Áß¾È</td><td>18</td></tr>
<tr><td>ÁÂºñ</td><td>17</td></tr>
<tr><td>ÁÂ¾È</td><td>17</td></tr>
<tr><td>¿ì¾È</td><td>16</td></tr>
<tr><td>1¶¥</td><td>13</td></tr>
<tr><td>À¯ºñ</td><td>13</td></tr>
<tr><td>ÁÂ2</td><td>9</td></tr>
<tr><td>»ç±¸</td><td>8</td></tr>
<tr><td>Åõ¶¥</td><td>8</td></tr>
<tr><td>1ÆÄ</td><td>7</td></tr>
<tr><td>2ºñ</td><td>7</td></tr>
<tr><td>ÁÂÁß2</td><td>5</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN6_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN7</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>289,675</td></tr>
<tr><td>»ïÁø</td><td>24,022</td></tr>
<tr><td>4±¸</td><td>12,234</td></tr>
<tr><td>À¯¶¥</td><td>7,931</td></tr>
<tr><td>Áßºñ</td><td>7,173</td></tr>
<tr><td>2¶¥</td><td>6,784</td></tr>
<tr><td>¿ìºñ</td><td>6,256</td></tr>
<tr><td>Áß¾È</td><td>6,209</td></tr>
<tr><td>ÁÂ¾È</td><td>6,204</td></tr>
<tr><td>ÁÂºñ</td><td>5,755</td></tr>
<tr><td>¿ì¾È</td><td>5,379</td></tr>
<tr><td>3¶¥</td><td>4,665</td></tr>
<tr><td>1¶¥</td><td>3,212</td></tr>
<tr><td>Åõ¶¥</td><td>2,765</td></tr>
<tr><td>»ç±¸</td><td>2,017</td></tr>
<tr><td>À¯ºñ</td><td>1,856</td></tr>
<tr><td>2ºñ</td><td>1,782</td></tr>
<tr><td>ÁÂ2</td><td>1,759</td></tr>
<tr><td>¿ì2</td><td>1,260</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,231</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL7</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,375</td></tr>
<tr><td>»ïÁø</td><td>86</td></tr>
<tr><td>4±¸</td><td>35</td></tr>
<tr><td>Áß¾È</td><td>34</td></tr>
<tr><td>Áßºñ</td><td>33</td></tr>
<tr><td>ÁÂºñ</td><td>32</td></tr>
<tr><td>À¯¶¥</td><td>28</td></tr>
<tr><td>2¶¥</td><td>27</td></tr>
<tr><td>¿ìºñ</td><td>26</td></tr>
<tr><td>¿ì¾È</td><td>24</td></tr>
<tr><td>3¶¥</td><td>22</td></tr>
<tr><td>1¶¥</td><td>20</td></tr>
<tr><td>ÁÂ¾È</td><td>20</td></tr>
<tr><td>À¯ºñ</td><td>12</td></tr>
<tr><td>¿ì2</td><td>9</td></tr>
<tr><td>»ç±¸</td><td>9</td></tr>
<tr><td>1ºñ</td><td>9</td></tr>
<tr><td>ÁÂ2</td><td>9</td></tr>
<tr><td>ÁÂÁß¾È</td><td>9</td></tr>
<tr><td>Åõ¶¥</td><td>8</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN7_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN8</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>289,387</td></tr>
<tr><td>»ïÁø</td><td>24,470</td></tr>
<tr><td>4±¸</td><td>12,210</td></tr>
<tr><td>À¯¶¥</td><td>7,627</td></tr>
<tr><td>Áßºñ</td><td>7,368</td></tr>
<tr><td>2¶¥</td><td>6,579</td></tr>
<tr><td>Áß¾È</td><td>6,233</td></tr>
<tr><td>¿ìºñ</td><td>6,209</td></tr>
<tr><td>ÁÂ¾È</td><td>5,993</td></tr>
<tr><td>ÁÂºñ</td><td>5,809</td></tr>
<tr><td>¿ì¾È</td><td>5,325</td></tr>
<tr><td>3¶¥</td><td>4,554</td></tr>
<tr><td>1¶¥</td><td>3,371</td></tr>
<tr><td>Åõ¶¥</td><td>2,632</td></tr>
<tr><td>»ç±¸</td><td>2,049</td></tr>
<tr><td>À¯ºñ</td><td>1,900</td></tr>
<tr><td>ÁÂ2</td><td>1,837</td></tr>
<tr><td>2ºñ</td><td>1,782</td></tr>
<tr><td>ÁÂÈ¨</td><td>1,294</td></tr>
<tr><td>¿ì2</td><td>1,293</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL8</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,382</td></tr>
<tr><td>»ïÁø</td><td>79</td></tr>
<tr><td>4±¸</td><td>46</td></tr>
<tr><td>Áßºñ</td><td>35</td></tr>
<tr><td>Áß¾È</td><td>33</td></tr>
<tr><td>2¶¥</td><td>31</td></tr>
<tr><td>¿ìºñ</td><td>29</td></tr>
<tr><td>¿ì¾È</td><td>25</td></tr>
<tr><td>À¯¶¥</td><td>25</td></tr>
<tr><td>ÁÂºñ</td><td>25</td></tr>
<tr><td>ÁÂ¾È</td><td>25</td></tr>
<tr><td>3¶¥</td><td>23</td></tr>
<tr><td>1¶¥</td><td>15</td></tr>
<tr><td>ÁÂÈ¨</td><td>11</td></tr>
<tr><td>2ºñ</td><td>9</td></tr>
<tr><td>»ç±¸</td><td>9</td></tr>
<tr><td>¿ì2</td><td>9</td></tr>
<tr><td>ÁÂ2</td><td>9</td></tr>
<tr><td>3ºñ</td><td>8</td></tr>
<tr><td>À¯ºñ</td><td>7</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN8_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN9</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>322,858</td></tr>
<tr><td>»ïÁø</td><td>20,262</td></tr>
<tr><td>4±¸</td><td>8,061</td></tr>
<tr><td>À¯¶¥</td><td>5,762</td></tr>
<tr><td>Áßºñ</td><td>5,712</td></tr>
<tr><td>2¶¥</td><td>4,983</td></tr>
<tr><td>¿ìºñ</td><td>4,699</td></tr>
<tr><td>Áß¾È</td><td>4,673</td></tr>
<tr><td>ÁÂºñ</td><td>4,601</td></tr>
<tr><td>ÁÂ¾È</td><td>4,355</td></tr>
<tr><td>¿ì¾È</td><td>4,048</td></tr>
<tr><td>3¶¥</td><td>3,248</td></tr>
<tr><td>1¶¥</td><td>2,581</td></tr>
<tr><td>Åõ¶¥</td><td>2,051</td></tr>
<tr><td>À¯ºñ</td><td>1,492</td></tr>
<tr><td>2ºñ</td><td>1,394</td></tr>
<tr><td>»ç±¸</td><td>1,305</td></tr>
<tr><td>ÁÂ2</td><td>1,211</td></tr>
<tr><td>¿ì2</td><td>969</td></tr>
<tr><td>ÁÂÈ¨</td><td>874</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL9</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,688</td></tr>
<tr><td>»ïÁø</td><td>41</td></tr>
<tr><td>4±¸</td><td>22</td></tr>
<tr><td>Áß¾È</td><td>18</td></tr>
<tr><td>Áßºñ</td><td>15</td></tr>
<tr><td>À¯¶¥</td><td>12</td></tr>
<tr><td>ÁÂºñ</td><td>11</td></tr>
<tr><td>¿ì¾È</td><td>10</td></tr>
<tr><td>¿ìºñ</td><td>10</td></tr>
<tr><td>3¶¥</td><td>9</td></tr>
<tr><td>»ç±¸</td><td>7</td></tr>
<tr><td>2¶¥</td><td>7</td></tr>
<tr><td>À¯ºñ</td><td>6</td></tr>
<tr><td>ÁÂ2</td><td>6</td></tr>
<tr><td>ÁÂ¾È</td><td>6</td></tr>
<tr><td>1¶¥</td><td>5</td></tr>
<tr><td>Åõ¶¥</td><td>4</td></tr>
<tr><td>2ºñ</td><td>3</td></tr>
<tr><td>1ºñ</td><td>3</td></tr>
<tr><td>3Á÷</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN9_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN10</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>414,697</td></tr>
<tr><td>»ïÁø</td><td>2,017</td></tr>
<tr><td>4±¸</td><td>968</td></tr>
<tr><td>À¯¶¥</td><td>529</td></tr>
<tr><td>Áßºñ</td><td>493</td></tr>
<tr><td>2¶¥</td><td>469</td></tr>
<tr><td>Áß¾È</td><td>445</td></tr>
<tr><td>¿ìºñ</td><td>439</td></tr>
<tr><td>¿ì¾È</td><td>425</td></tr>
<tr><td>ÁÂ¾È</td><td>413</td></tr>
<tr><td>ÁÂºñ</td><td>397</td></tr>
<tr><td>°í4</td><td>306</td></tr>
<tr><td>3¶¥</td><td>255</td></tr>
<tr><td>1¶¥</td><td>242</td></tr>
<tr><td>Åõ¶¥</td><td>178</td></tr>
<tr><td>ÅõÈñ¹ø</td><td>158</td></tr>
<tr><td>»ç±¸</td><td>135</td></tr>
<tr><td>À¯ºñ</td><td>135</td></tr>
<tr><td>ÁÂ2</td><td>127</td></tr>
<tr><td>2ºñ</td><td>112</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL10</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,898</td></tr>
<tr><td>Áßºñ</td><td>3</td></tr>
<tr><td>ÁÂºñ</td><td>3</td></tr>
<tr><td>»ïÁø</td><td>3</td></tr>
<tr><td>À¯¶¥</td><td>3</td></tr>
<tr><td>2¶¥</td><td>2</td></tr>
<tr><td>1¶¥</td><td>2</td></tr>
<tr><td>4±¸</td><td>2</td></tr>
<tr><td>ÁÂ2</td><td>1</td></tr>
<tr><td>¿ìºñ</td><td>1</td></tr>
<tr><td>»ç±¸</td><td>1</td></tr>
<tr><td>3ÆÄ</td><td>1</td></tr>
<tr><td>2¾È</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN10_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN11</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>419,362</td></tr>
<tr><td>»ïÁø</td><td>1,010</td></tr>
<tr><td>4±¸</td><td>549</td></tr>
<tr><td>Áßºñ</td><td>288</td></tr>
<tr><td>À¯¶¥</td><td>277</td></tr>
<tr><td>2¶¥</td><td>262</td></tr>
<tr><td>¿ìºñ</td><td>255</td></tr>
<tr><td>ÁÂºñ</td><td>240</td></tr>
<tr><td>ÁÂ¾È</td><td>222</td></tr>
<tr><td>¿ì¾È</td><td>213</td></tr>
<tr><td>Áß¾È</td><td>211</td></tr>
<tr><td>°í4</td><td>182</td></tr>
<tr><td>3¶¥</td><td>137</td></tr>
<tr><td>1¶¥</td><td>115</td></tr>
<tr><td>Åõ¶¥</td><td>111</td></tr>
<tr><td>ÅõÈñ¹ø</td><td>111</td></tr>
<tr><td>»ç±¸</td><td>96</td></tr>
<tr><td>À¯ºñ</td><td>85</td></tr>
<tr><td>2ºñ</td><td>72</td></tr>
<tr><td>ÁÂ2</td><td>60</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>IL11</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,905</td></tr>
<tr><td>Áß¾È</td><td>4</td></tr>
<tr><td>»ïÁø</td><td>3</td></tr>
<tr><td>Åõ¶¥</td><td>1</td></tr>
<tr><td>4±¸</td><td>1</td></tr>
<tr><td>Áß2</td><td>1</td></tr>
<tr><td>À¯ºñ</td><td>1</td></tr>
<tr><td>À¯¶¥</td><td>1</td></tr>
<tr><td>¿ìÈ¨</td><td>1</td></tr>
<tr><td>¿ì¾È</td><td>1</td></tr>
<tr><td>¿ìºñ</td><td>1</td></tr>
<tr><td>¿ì2</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN11_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN12</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>422,107</td></tr>
<tr><td>»ïÁø</td><td>539</td></tr>
<tr><td>4±¸</td><td>264</td></tr>
<tr><td>À¯¶¥</td><td>152</td></tr>
<tr><td>Áßºñ</td><td>141</td></tr>
<tr><td>2¶¥</td><td>131</td></tr>
<tr><td>Áß¾È</td><td>122</td></tr>
<tr><td>¿ìºñ</td><td>121</td></tr>
<tr><td>ÁÂ¾È</td><td>114</td></tr>
<tr><td>ÁÂºñ</td><td>113</td></tr>
<tr><td>¿ì¾È</td><td>100</td></tr>
<tr><td>3¶¥</td><td>95</td></tr>
<tr><td>°í4</td><td>84</td></tr>
<tr><td>Åõ¶¥</td><td>61</td></tr>
<tr><td>1¶¥</td><td>54</td></tr>
<tr><td>ÅõÈñ¹ø</td><td>49</td></tr>
<tr><td>»ç±¸</td><td>44</td></tr>
<tr><td>À¯ºñ</td><td>32</td></tr>
<tr><td>ÁÂ2</td><td>31</td></tr>
<tr><td>¿ì2</td><td>26</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL12</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,913</td></tr>
<tr><td>»ïÁø</td><td>2</td></tr>
<tr><td>»ç±¸</td><td>1</td></tr>
<tr><td>2ºñ</td><td>1</td></tr>
<tr><td>Áßºñ</td><td>1</td></tr>
<tr><td>ÁÂÈ¨</td><td>1</td></tr>
<tr><td>¿ìÁß¾È</td><td>1</td></tr>
<tr><td>¿ìºñ</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN12_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN13</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,813</td></tr>
<tr><td>»ïÁø</td><td>19</td></tr>
<tr><td>4±¸</td><td>11</td></tr>
<tr><td>¿ìºñ</td><td>5</td></tr>
<tr><td>À¯¶¥</td><td>5</td></tr>
<tr><td>¿ìÈñ¹ø</td><td>5</td></tr>
<tr><td>2¶¥</td><td>5</td></tr>
<tr><td>ÁÂ¾È</td><td>5</td></tr>
<tr><td>Áß¾È</td><td>5</td></tr>
<tr><td>1¶¥</td><td>4</td></tr>
<tr><td>Åõ¶¥</td><td>4</td></tr>
<tr><td>¿ì¾È</td><td>3</td></tr>
<tr><td>1ÆÄ</td><td>3</td></tr>
<tr><td>2À¯º´</td><td>3</td></tr>
<tr><td>ÁßÈñ¹ø</td><td>3</td></tr>
<tr><td>3¶¥</td><td>2</td></tr>
<tr><td>»ç±¸</td><td>2</td></tr>
<tr><td>°í4</td><td>2</td></tr>
<tr><td>ÁÂºñ</td><td>2</td></tr>
<tr><td>ÁÂÈ¨</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL13</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN13_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN14</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,852</td></tr>
<tr><td>»ïÁø</td><td>7</td></tr>
<tr><td>4±¸</td><td>7</td></tr>
<tr><td>1¶¥</td><td>6</td></tr>
<tr><td>2¶¥</td><td>6</td></tr>
<tr><td>3¶¥</td><td>4</td></tr>
<tr><td>ÁÂ¾È</td><td>4</td></tr>
<tr><td>Áßºñ</td><td>4</td></tr>
<tr><td>À¯¶¥</td><td>3</td></tr>
<tr><td>°í4</td><td>3</td></tr>
<tr><td>Åõ¶¥</td><td>3</td></tr>
<tr><td>¿ì¾È</td><td>2</td></tr>
<tr><td>ÁÂºñ</td><td>2</td></tr>
<tr><td>ÁÂ2</td><td>2</td></tr>
<tr><td>Áß¾È</td><td>2</td></tr>
<tr><td>ÅõÈñ¹ø</td><td>2</td></tr>
<tr><td>ÁÂÁß2</td><td>1</td></tr>
<tr><td>¿ìÆÄ</td><td>1</td></tr>
<tr><td>¿ìÁß¾È</td><td>1</td></tr>
<tr><td>À¯¾È</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL14</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN14_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN15</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,879</td></tr>
<tr><td>2¶¥</td><td>5</td></tr>
<tr><td>»ïÁø</td><td>5</td></tr>
<tr><td>Áßºñ</td><td>5</td></tr>
<tr><td>¿ì¾È</td><td>3</td></tr>
<tr><td>°í4</td><td>3</td></tr>
<tr><td>4±¸</td><td>3</td></tr>
<tr><td>3¶¥</td><td>2</td></tr>
<tr><td>ÁÂºñ</td><td>2</td></tr>
<tr><td>Åõ¶¥</td><td>2</td></tr>
<tr><td>Áß¾È</td><td>2</td></tr>
<tr><td>À¯¶¥</td><td>2</td></tr>
<tr><td>ÅõÈñ¹ø</td><td>1</td></tr>
<tr><td>Åõ¹ø</td><td>1</td></tr>
<tr><td>ÁÂ¾È</td><td>1</td></tr>
<tr><td>À¯½Ç</td><td>1</td></tr>
<tr><td>»ç±¸</td><td>1</td></tr>
<tr><td>3ÆÄ</td><td>1</td></tr>
<tr><td>2¾È</td><td>1</td></tr>
<tr><td>1Á÷</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL15</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN15_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN16</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,915</td></tr>
<tr><td>»ïÁø</td><td>3</td></tr>
<tr><td>¿ìºñ</td><td>1</td></tr>
<tr><td>2ºñ</td><td>1</td></tr>
<tr><td>1¶¥</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL16</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN16_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN17</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,914</td></tr>
<tr><td>Åõ¶¥</td><td>2</td></tr>
<tr><td>ÁÂºñ</td><td>1</td></tr>
<tr><td>À¯¶¥</td><td>1</td></tr>
<tr><td>»ïÁø</td><td>1</td></tr>
<tr><td>4±¸</td><td>1</td></tr>
<tr><td>2ºñ</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL17</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN17_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN18</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,912</td></tr>
<tr><td>4±¸</td><td>3</td></tr>
<tr><td>»ïÁø</td><td>3</td></tr>
<tr><td>Áßºñ</td><td>1</td></tr>
<tr><td>¿ìºñ</td><td>1</td></tr>
<tr><td>°í4</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL18</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN18_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN19</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL19</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN19_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN20</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL20</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN20_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN21</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL21</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN21_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN22</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL22</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN22_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN23</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL23</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN23_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN24</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL24</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN24_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN25</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>IL25</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN25_3</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>424,921</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>AB</code><span class="code-desc"> — 타수</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>RUN</code><span class="code-desc"> — 득점</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HIT</code><span class="code-desc"> — 안타</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>RBI</code><span class="code-desc"> — 타점</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>AVGS</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>AVG5</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>20010405HHSS0</td><td>20010405HHSS0</td><td>20010405HHSS0</td></tr>
<tr><td>GDAY</td><td>20010405</td><td>20010405</td><td>20010405</td></tr>
<tr><td>TB</td><td>B</td><td>T</td><td>B</td></tr>
<tr><td>NAME</td><td>¹ÚÁ¤È¯</td><td>ÀÌ¹üÈ£</td><td>¸¶¸£Æ¼³×</td></tr>
<tr><td>PCODE</td><td>70408</td><td>70756</td><td>71419</td></tr>
<tr><td>TURN</td><td>39</td><td>39</td><td>16</td></tr>
<tr><td>ONETURN</td><td>9</td><td>9</td><td>6</td></tr>
<tr><td>POSITION</td><td>À¯</td><td>ì£</td><td>Áß</td></tr>
<tr><td>CHANGEINN</td><td>8</td><td>5</td><td></td></tr>
<tr><td>INN1</td><td></td><td></td><td>Áßºñ</td></tr>
<tr><td>IL1</td><td></td><td></td><td></td></tr>
<tr><td>INN1_3</td><td></td><td></td><td></td></tr>
<tr><td>INN2</td><td></td><td></td><td></td></tr>
<tr><td>IL2</td><td></td><td></td><td></td></tr>
<tr><td>INN2_3</td><td></td><td></td><td></td></tr>
<tr><td>INN3</td><td></td><td></td><td></td></tr>
<tr><td>IL3</td><td></td><td></td><td></td></tr>
<tr><td>INN3_3</td><td></td><td></td><td></td></tr>
<tr><td>INN4</td><td></td><td></td><td>¿ìºñ</td></tr>
<tr><td>IL4</td><td></td><td></td><td></td></tr>
<tr><td>INN4_3</td><td></td><td></td><td></td></tr>
<tr><td>INN5</td><td></td><td></td><td></td></tr>
<tr><td>IL5</td><td></td><td></td><td></td></tr>
<tr><td>INN5_3</td><td></td><td></td><td></td></tr>
<tr><td>INN6</td><td></td><td></td><td>»ïÁø</td></tr>
<tr><td>IL6</td><td></td><td></td><td></td></tr>
<tr><td>INN6_3</td><td></td><td></td><td></td></tr>
<tr><td>INN7</td><td></td><td>ÁÂ¾È</td><td></td></tr>
<tr><td>IL7</td><td></td><td></td><td></td></tr>
<tr><td>INN7_3</td><td></td><td></td><td></td></tr>
<tr><td>INN8</td><td>2¶¥</td><td></td><td>ÁÂÈ¨</td></tr>
<tr><td>IL8</td><td></td><td></td><td></td></tr>
<tr><td>INN8_3</td><td></td><td></td><td></td></tr>
<tr><td>INN9</td><td></td><td>À¯¶¥</td><td></td></tr>
<tr><td>IL9</td><td></td><td></td><td></td></tr>
<tr><td>INN9_3</td><td></td><td></td><td></td></tr>
<tr><td>INN10</td><td></td><td></td><td></td></tr>
<tr><td>IL10</td><td></td><td></td><td></td></tr>
<tr><td>INN10_3</td><td></td><td></td><td></td></tr>
<tr><td>INN11</td><td></td><td></td><td></td></tr>
<tr><td>IL11</td><td></td><td></td><td></td></tr>
<tr><td>INN11_3</td><td></td><td></td><td></td></tr>
<tr><td>INN12</td><td></td><td></td><td></td></tr>
<tr><td>IL12</td><td></td><td></td><td></td></tr>
<tr><td>INN12_3</td><td></td><td></td><td></td></tr>
<tr><td>INN13</td><td></td><td></td><td></td></tr>
<tr><td>IL13</td><td></td><td></td><td></td></tr>
<tr><td>INN13_3</td><td></td><td></td><td></td></tr>
<tr><td>INN14</td><td></td><td></td><td></td></tr>
<tr><td>IL14</td><td></td><td></td><td></td></tr>
<tr><td>INN14_3</td><td></td><td></td><td></td></tr>
<tr><td>INN15</td><td></td><td></td><td></td></tr>
<tr><td>IL15</td><td></td><td></td><td></td></tr>
<tr><td>INN15_3</td><td></td><td></td><td></td></tr>
<tr><td>INN16</td><td></td><td></td><td></td></tr>
<tr><td>IL16</td><td></td><td></td><td></td></tr>
<tr><td>INN16_3</td><td></td><td></td><td></td></tr>
<tr><td>INN17</td><td></td><td></td><td></td></tr>
<tr><td>IL17</td><td></td><td></td><td></td></tr>
<tr><td>INN17_3</td><td></td><td></td><td></td></tr>
<tr><td>INN18</td><td></td><td></td><td></td></tr>
<tr><td>IL18</td><td></td><td></td><td></td></tr>
<tr><td>INN18_3</td><td></td><td></td><td></td></tr>
<tr><td>INN19</td><td></td><td></td><td></td></tr>
<tr><td>IL19</td><td></td><td></td><td></td></tr>
<tr><td>INN19_3</td><td></td><td></td><td></td></tr>
<tr><td>INN20</td><td></td><td></td><td></td></tr>
<tr><td>IL20</td><td></td><td></td><td></td></tr>
<tr><td>INN20_3</td><td></td><td></td><td></td></tr>
<tr><td>INN21</td><td></td><td></td><td></td></tr>
<tr><td>IL21</td><td></td><td></td><td></td></tr>
<tr><td>INN21_3</td><td></td><td></td><td></td></tr>
<tr><td>INN22</td><td></td><td></td><td></td></tr>
<tr><td>IL22</td><td></td><td></td><td></td></tr>
<tr><td>INN22_3</td><td></td><td></td><td></td></tr>
<tr><td>INN23</td><td></td><td></td><td></td></tr>
<tr><td>IL23</td><td></td><td></td><td></td></tr>
<tr><td>INN23_3</td><td></td><td></td><td></td></tr>
<tr><td>INN24</td><td></td><td></td><td></td></tr>
<tr><td>IL24</td><td></td><td></td><td></td></tr>
<tr><td>INN24_3</td><td></td><td></td><td></td></tr>
<tr><td>INN25</td><td></td><td></td><td></td></tr>
<tr><td>IL25</td><td></td><td></td><td></td></tr>
<tr><td>INN25_3</td><td></td><td></td><td></td></tr>
<tr><td>AB</td><td>1</td><td>2</td><td>4</td></tr>
<tr><td>RUN</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>HIT</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>RBI</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>AVGS</td><td>0.000</td><td>0.500</td><td>0.250</td></tr>
<tr><td>AVG5</td><td>0.000</td><td>0.500</td><td>0.250</td></tr>
</tbody></table>
</div>

</div>
