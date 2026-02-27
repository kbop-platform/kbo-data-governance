---
title: PITCHCLOCK
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">PITCHCLOCK</div>
  <div class="dict-hero-sub">DB2_BASEBALL &middot; PK: GMKEY, GYEAR, GDAY, LIVETEXT</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">215</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">19</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GYEAR, GDAY, LIVETEXT</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 - Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">19개</span></div>

<div class="dict-encoding-warn">`RUNNER` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">STADIUM</span></td><td><span class="col-std">stadium_nm</span></td><td><span class="col-type">nvarchar(40)</span></td><td></td><td></td><td><span class="col-desc">구장명</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">VTEAM</span></td><td><span class="col-std">away_team_cd</span></td><td><span class="col-type">nvarchar(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">원정팀 코드</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">HTEAM</span></td><td><span class="col-std">home_team_cd</span></td><td><span class="col-type">nvarchar(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 코드</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">HITNAME</span></td><td><span class="col-std">hitter_nm</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">타자 이름 (EUC-KR)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">HITTER</span></td><td><span class="col-std">hitter_nm</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">타자 선수 코드</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">PITNAME</span></td><td><span class="col-std">pitcher_nm</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">투수 이름 (EUC-KR)</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">PITCHER</span></td><td><span class="col-std">pitcher_nm</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">투수 선수 코드</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">CATNAME</span></td><td><span class="col-std">catcher_nm</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">포수 이름 (EUC-KR)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">CATCHER</span></td><td><span class="col-std">catcher_id</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">포수 선수 코드</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">TEAM</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">nvarchar(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 코드 (HH=한화, LG, SK, HT=KIA, LT=롯데, OB=두산, SS=삼성, WO=키움, NC, KT 등 2자리)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">선수명</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">선수 코드 (5~6자리 숫자)</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">PITCHCLOCK</span></td><td><span class="col-std">pitch_clock_cd</span></td><td><span class="col-type">varchar(15)</span></td><td></td><td></td><td><span class="col-desc">피치클락 위반 코드 (타자위반/투수위반/포수위반, EUC-KR)</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">LIVETEXT</span></td><td><span class="col-std">live_text</span></td><td><span class="col-type">varchar(200)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">실시간 문자 중계 텍스트</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">RUNNER</span></td><td><span class="col-std">runner_cd</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">주자 상태 코드 (X=무주자, 1=1루, 2=2루, 3=3루, 12=1·2루, 13=1·3루, 23=2·3루, 123=만루)</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">DETAIL</span></td><td><span class="col-std">detail_nm</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">상세 내용</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">6개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>2025</td><td>215</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> &mdash; 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>VTEAM</code><span class="code-desc"> &mdash; 원정팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>WO</td><td>31</td></tr>
<tr><td>HT</td><td>28</td></tr>
<tr><td>OB</td><td>26</td></tr>
<tr><td>LT</td><td>26</td></tr>
<tr><td>HH</td><td>25</td></tr>
<tr><td>SS</td><td>17</td></tr>
<tr><td>SK</td><td>17</td></tr>
<tr><td>NC</td><td>16</td></tr>
<tr><td>LG</td><td>14</td></tr>
<tr><td>KT</td><td>14</td></tr>
<tr><td>키움</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>HTEAM</code><span class="code-desc"> &mdash; 홈팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>SK</td><td>29</td></tr>
<tr><td>HT</td><td>26</td></tr>
<tr><td>LT</td><td>24</td></tr>
<tr><td>OB</td><td>23</td></tr>
<tr><td>WO</td><td>23</td></tr>
<tr><td>SS</td><td>20</td></tr>
<tr><td>KT</td><td>19</td></tr>
<tr><td>HH</td><td>19</td></tr>
<tr><td>NC</td><td>16</td></tr>
<tr><td>LG</td><td>16</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>TEAM</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-ref">팀 식별자 - [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>RUNNER</code><span class="code-desc"> &mdash; 주자 상태 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>X</td><td>70</td></tr>
<tr><td>1</td><td>48</td></tr>
<tr><td>12</td><td>37</td></tr>
<tr><td>2</td><td>27</td></tr>
<tr><td>123</td><td>12</td></tr>
<tr><td>3</td><td>11</td></tr>
<tr><td>23</td><td>7</td></tr>
<tr><td>13</td><td>3</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>20250322HHKT0</td><td>20250323WOSS0</td><td>20250323WOSS0</td></tr>
<tr><td>GYEAR</td><td>2025</td><td>2025</td><td>2025</td></tr>
<tr><td>GDAY</td><td>20250322</td><td>20250323</td><td>20250323</td></tr>
<tr><td>STADIUM</td><td>수원</td><td>대구</td><td>대구</td></tr>
<tr><td>VTEAM</td><td>HH</td><td>WO</td><td>WO</td></tr>
<tr><td>HTEAM</td><td>KT</td><td>SS</td><td>SS</td></tr>
<tr><td>HITNAME</td><td>¹®»óÃ¶</td><td>±èÁöÂù</td><td>±è¿µ¿õ</td></tr>
<tr><td>HITTER</td><td>64007</td><td>50458</td><td>52430</td></tr>
<tr><td>PITNAME</td><td>Æù¼¼</td><td>ÇÏ¿µ¹Î</td><td>±è¼±±â</td></tr>
<tr><td>PITCHER</td><td>55730</td><td>64350</td><td>66018</td></tr>
<tr><td>CATNAME</td><td>ÃÖÀçÈÆ</td><td>±èµ¿Çå</td><td>±èµ¿Çå</td></tr>
<tr><td>CATCHER</td><td>78288</td><td>53344</td><td>53344</td></tr>
<tr><td>TEAM</td><td>HH</td><td>WO</td><td>WO</td></tr>
<tr><td>NAME</td><td>Æù¼¼</td><td>ÇÏ¿µ¹Î</td><td>±è¼±±â</td></tr>
<tr><td>PCODE</td><td>55730</td><td>64350</td><td>66018</td></tr>
<tr><td>PITCHCLOCK</td><td>Åõ¼ö À§¹Ý</td><td>Åõ¼ö À§¹Ý</td><td>Åõ¼ö À§¹Ý</td></tr>
<tr><td>LIVETEXT</td><td>3È¸¸» 6¹øÅ¸¼ø ÃÊ±¸ Àü ÇÇÄ¡Å¬¶ô Åõ¼öÀ§¹Ý : ÇÑÈ­ Æù¼¼</td><td>1È¸¸» 1¹øÅ¸¼ø 2±¸ ÈÄ ÇÇÄ¡Å¬¶ô Åõ¼öÀ§¹Ý : Å°¿ò ÇÏ¿µ¹Î</td><td>7È¸¸» 8¹øÅ¸¼ø 3±¸ ÈÄ ÇÇÄ¡Å¬¶ô Åõ¼öÀ§¹Ý : Å°¿ò ±è¼±±â</td></tr>
<tr><td>RUNNER</td><td>12</td><td>X</td><td>X</td></tr>
<tr><td>DETAIL</td><td>Å¸¼®°£ 33ÃÊ</td><td>Åõ±¸°£(ÁÖÀÚX) 20ÃÊ</td><td>Åõ±¸°£(ÁÖÀÚX) 20ÃÊ</td></tr>
</tbody></table>
</div>

</div>
