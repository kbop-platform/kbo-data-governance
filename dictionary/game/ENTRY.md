---
title: ENTRY
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">ENTRY</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GMKEY, GDAY, TURN, PCODE, POSI</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">854,280</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">11</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY, TURN, PCODE, POSI</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 - Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀, 방송팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[코드 사전](../../standards-dict/codes.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">11개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">TURN</span></td><td><span class="col-std">turn_no</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">타순</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(15)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선수명</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">TEAM</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 코드 (HH=한화, LG, SK, HT=KIA, LT=롯데, OB=두산, SS=삼성, WO=키움, NC, KT 등 2자리)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">POSI</span></td><td><span class="col-std">position_cd</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">수비 포지션 코드 (XY 형식: X=타순, Y=포지션번호 1~9, 예: 11=1번타순 투수, 35=3번타순 3루수)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">CHIN</span></td><td><span class="col-std">change_inning_no</span></td><td><span class="col-type">varchar(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">교체 이닝</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">CHTURN</span></td><td><span class="col-std">change_turn_no</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">교체 타순</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">CHBCNT</span></td><td><span class="col-std">change_ball_count_cd</span></td><td><span class="col-type">varchar(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">교체 시점 볼카운트</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">CHIN2</span></td><td><span class="col-std">change_inning2_no</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">교체 이닝 세부</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">9개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> &mdash; 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TURN</code><span class="code-desc"> &mdash; 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> &mdash; 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>TEAM</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-ref">팀 식별자 - [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>POSI</code><span class="code-desc"> &mdash; 수비 포지션 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>11</td><td>47,384</td></tr>
<tr><td>19</td><td>47,158</td></tr>
<tr><td>18</td><td>47,158</td></tr>
<tr><td>17</td><td>47,158</td></tr>
<tr><td>16</td><td>47,158</td></tr>
<tr><td>15</td><td>47,158</td></tr>
<tr><td>14</td><td>47,158</td></tr>
<tr><td>13</td><td>47,158</td></tr>
<tr><td>12</td><td>47,158</td></tr>
<tr><td>1D</td><td>47,151</td></tr>
<tr><td>21</td><td>44,277</td></tr>
<tr><td>31</td><td>36,726</td></tr>
<tr><td>1H</td><td>33,428</td></tr>
<tr><td>41</td><td>26,717</td></tr>
<tr><td>2H</td><td>21,826</td></tr>
<tr><td>22</td><td>20,182</td></tr>
<tr><td>1R</td><td>19,610</td></tr>
<tr><td>27</td><td>19,564</td></tr>
<tr><td>29</td><td>17,619</td></tr>
<tr><td>24</td><td>17,183</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>CHIN</code><span class="code-desc"> &mdash; 교체 이닝</span></summary>
<div class="code-ref">고유값 16종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>CHTURN</code><span class="code-desc"> &mdash; 교체 타순</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>471,566</td></tr>
<tr><td>9</td><td>47,939</td></tr>
<tr><td>8</td><td>47,255</td></tr>
<tr><td>7</td><td>44,468</td></tr>
<tr><td>6</td><td>42,567</td></tr>
<tr><td>1</td><td>41,971</td></tr>
<tr><td>5</td><td>41,460</td></tr>
<tr><td>2</td><td>39,813</td></tr>
<tr><td>3</td><td>38,685</td></tr>
<tr><td>4</td><td>38,555</td></tr>
<tr><td></td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>CHBCNT</code><span class="code-desc"> &mdash; 교체 시점 볼카운트</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>849,347</td></tr>
<tr><td>1</td><td>2,483</td></tr>
<tr><td>2</td><td>1,220</td></tr>
<tr><td>3</td><td>622</td></tr>
<tr><td>4</td><td>310</td></tr>
<tr><td>5</td><td>170</td></tr>
<tr><td>6</td><td>76</td></tr>
<tr><td>7</td><td>39</td></tr>
<tr><td>8</td><td>7</td></tr>
<tr><td>11</td><td>4</td></tr>
<tr><td>9</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>CHIN2</code><span class="code-desc"> &mdash; 교체 이닝 세부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>852,852</td></tr>
<tr><td>1</td><td>756</td></tr>
<tr><td>2</td><td>629</td></tr>
<tr><td></td><td>40</td></tr>
<tr><td>3</td><td>2</td></tr>
<tr><td>4</td><td>1</td></tr>
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
<tr><td>TURN</td><td>10</td><td>10</td><td>11</td></tr>
<tr><td>NAME</td><td>ÀüÁØ¿ì</td><td>ÇÑµ¿Èñ</td><td>¹Ú°Ç¿ì</td></tr>
<tr><td>PCODE</td><td>80620</td><td>82122</td><td>40002</td></tr>
<tr><td>TEAM</td><td>B</td><td>B</td><td>T</td></tr>
<tr><td>POSI</td><td>11</td><td>11</td><td>15</td></tr>
<tr><td>CHIN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>CHTURN</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>CHBCNT</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>CHIN2</td><td>0</td><td>0</td><td>0</td></tr>
</tbody></table>
</div>

</div>
