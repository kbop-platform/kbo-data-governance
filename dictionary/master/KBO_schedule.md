---
title: KBO_schedule
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-access">Public</span>
  </div>
  <div class="dict-hero-title">KBO_schedule</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gmkey, gamedate</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">27,340</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">22</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">시즌 전 일괄</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기운영팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gmkey, gamedate</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 - Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">경기운영팀 (R-05)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">시즌 전 일괄</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">전 시스템</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Public</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[일정 관리](../products/schedule.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [코드 사전](../../standards-dict/codes.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">22개</span></div>

<div class="dict-encoding-warn">`gweek`, `home`, `visit`, `stadium` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gmkey</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">game_flag</span></td><td><span class="col-std">game_type_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">경기 유형 코드 (0=정규시즌, 1=올스타전, 3=준플레이오프, 4=미확인, 5=플레이오프, 6=미확인, 7=한국시리즈, 8=와일드카드, 9=기타)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">end_flag</span></td><td><span class="col-std">end_if</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 종료 플래그 (1=종료, 0=미종료/진행중)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">gamedate</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">varchar(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">gyear</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">char(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">연도</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">gmonth</span></td><td><span class="col-std">game_mon</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 월</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">gday</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 일</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">gweek</span></td><td><span class="col-std">game_week_nm</span></td><td><span class="col-type">varchar(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">요일</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">home</span></td><td><span class="col-std">home_team_cd</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀명</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">home_key</span></td><td><span class="col-std">home_team_id</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 코드 (SS/LT/HT/OB/LG/HH/SK/WO/NC/KT, 국제: EA/WE/KR/JP 등)</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">visit</span></td><td><span class="col-std">away_team_cd</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">원정팀명</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">visit_key</span></td><td><span class="col-std">away_team_id</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">원정팀 코드 (SS/LT/HT/OB/LG/HH/SK/WO/NC/KT, 국제: EA/WE/KR/JP 등)</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">stadium</span></td><td><span class="col-std">stadium_nm</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">구장 코드 (JS=잠실, SJ=사직, DJ=대전, DG=대구, KC=고척, IC=인천 등)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">stadium_key</span></td><td><span class="col-std">stadium_id</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">구장 코드 (JS=잠실, SJ=사직, DJ=대전, DG=대구, MH=목동, SW=수원, KJ=광주, KC=고척, IC=인천 등 30개)</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">dheader</span></td><td><span class="col-std">doubleheader_no</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">더블헤더 번호 (0=일반, 1=1차전, 2=2차전)</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">hpcode</span></td><td><span class="col-std">home_pitcher_id</span></td><td><span class="col-type">char(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 선발투수 코드</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">vpcode</span></td><td><span class="col-std">away_pitcher_id</span></td><td><span class="col-type">char(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">원정팀 선발투수 코드</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">gtime</span></td><td><span class="col-std">game_tm</span></td><td><span class="col-type">char(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 시작 시각</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">hscore</span></td><td><span class="col-std">home_score</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 점수</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">vscore</span></td><td><span class="col-std">away_score</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">원정팀 점수</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">cancel_flag</span></td><td><span class="col-std">cancel_if</span></td><td><span class="col-type">bit</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 취소 여부 (True/False)</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">suspended_flag</span></td><td><span class="col-std">suspended_if</span></td><td><span class="col-type">bit</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">서스펜디드 여부 (True/False)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">21개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>game_flag</code><span class="code-desc"> &mdash; 경기 유형 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>25,313</td></tr>
<tr><td>1</td><td>1,376</td></tr>
<tr><td>7</td><td>240</td></tr>
<tr><td>5</td><td>186</td></tr>
<tr><td>3</td><td>121</td></tr>
<tr><td>9</td><td>48</td></tr>
<tr><td>8</td><td>38</td></tr>
<tr><td>4</td><td>16</td></tr>
<tr><td>6</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>end_flag</code><span class="code-desc"> &mdash; 경기 종료 플래그</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>25,372</td></tr>
<tr><td>0</td><td>1,968</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>gamedate</code><span class="code-desc"> &mdash; 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>gyear</code><span class="code-desc"> &mdash; 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>gmonth</code><span class="code-desc"> &mdash; 경기 월</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>05</td><td>4,627</td></tr>
<tr><td>06</td><td>4,265</td></tr>
<tr><td>08</td><td>4,260</td></tr>
<tr><td>04</td><td>3,906</td></tr>
<tr><td>07</td><td>3,749</td></tr>
<tr><td>09</td><td>3,589</td></tr>
<tr><td>03</td><td>1,614</td></tr>
<tr><td>10</td><td>1,251</td></tr>
<tr><td>11</td><td>75</td></tr>
<tr><td>3</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>gday</code><span class="code-desc"> &mdash; 경기 일</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>gweek</code><span class="code-desc"> &mdash; 요일</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>ÀÏ</td><td>4,709</td></tr>
<tr><td>Åä</td><td>4,706</td></tr>
<tr><td>¼ö</td><td>4,477</td></tr>
<tr><td>¸ñ</td><td>4,363</td></tr>
<tr><td>È­</td><td>4,246</td></tr>
<tr><td>±Ý</td><td>4,086</td></tr>
<tr><td>¿ù</td><td>752</td></tr>
<tr><td></td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>home</code><span class="code-desc"> &mdash; 홈팀명</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>»ï¼º</td><td>3,270</td></tr>
<tr><td>·Ôµ¥</td><td>3,246</td></tr>
<tr><td>LG</td><td>2,741</td></tr>
<tr><td>ÇÑÈ­</td><td>2,557</td></tr>
<tr><td>µÎ»ê</td><td>2,178</td></tr>
<tr><td>KIA</td><td>1,927</td></tr>
<tr><td>SK</td><td>1,646</td></tr>
<tr><td>NC</td><td>1,233</td></tr>
<tr><td>ÇØÅÂ</td><td>1,192</td></tr>
<tr><td>KT</td><td>1,036</td></tr>
<tr><td>OB</td><td>996</td></tr>
<tr><td>³Ø¼¾</td><td>863</td></tr>
<tr><td>Çö´ë</td><td>846</td></tr>
<tr><td>Å°¿ò</td><td>633</td></tr>
<tr><td>½Ö¹æ¿ï</td><td>575</td></tr>
<tr><td>SSG</td><td>514</td></tr>
<tr><td>ÅÂÆò¾ç</td><td>496</td></tr>
<tr><td>ºù±×·¹</td><td>487</td></tr>
<tr><td>MBC</td><td>419</td></tr>
<tr><td>Ã»º¸</td><td>163</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>home_key</code><span class="code-desc"> &mdash; 홈팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>SS</td><td>3,270</td></tr>
<tr><td>LT</td><td>3,246</td></tr>
<tr><td>HT</td><td>3,245</td></tr>
<tr><td>OB</td><td>3,174</td></tr>
<tr><td>LG</td><td>3,160</td></tr>
<tr><td>HH</td><td>3,044</td></tr>
<tr><td>SK</td><td>2,160</td></tr>
<tr><td>HD</td><td>1,645</td></tr>
<tr><td>WO</td><td>1,496</td></tr>
<tr><td>NC</td><td>1,233</td></tr>
<tr><td>KT</td><td>1,036</td></tr>
<tr><td>SB</td><td>575</td></tr>
<tr><td>EA</td><td>24</td></tr>
<tr><td>WE</td><td>21</td></tr>
<tr><td>KR</td><td>4</td></tr>
<tr><td>DR</td><td>2</td></tr>
<tr><td>JP</td><td>2</td></tr>
<tr><td>MA</td><td>1</td></tr>
<tr><td>CZ</td><td>1</td></tr>
<tr><td>AU</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>visit</code><span class="code-desc"> &mdash; 원정팀명</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>»ï¼º</td><td>3,230</td></tr>
<tr><td>·Ôµ¥</td><td>3,148</td></tr>
<tr><td>LG</td><td>2,853</td></tr>
<tr><td>ÇÑÈ­</td><td>2,470</td></tr>
<tr><td>µÎ»ê</td><td>2,332</td></tr>
<tr><td>KIA</td><td>1,870</td></tr>
<tr><td>SK</td><td>1,640</td></tr>
<tr><td>ÇØÅÂ</td><td>1,188</td></tr>
<tr><td>NC</td><td>1,170</td></tr>
<tr><td>KT</td><td>1,022</td></tr>
<tr><td>OB</td><td>994</td></tr>
<tr><td>³Ø¼¾</td><td>903</td></tr>
<tr><td>Çö´ë</td><td>838</td></tr>
<tr><td>Å°¿ò</td><td>708</td></tr>
<tr><td>½Ö¹æ¿ï</td><td>573</td></tr>
<tr><td>SSG</td><td>518</td></tr>
<tr><td>ÅÂÆò¾ç</td><td>495</td></tr>
<tr><td>ºù±×·¹</td><td>484</td></tr>
<tr><td>MBC</td><td>419</td></tr>
<tr><td>Ã»º¸</td><td>163</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>visit_key</code><span class="code-desc"> &mdash; 원정팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>OB</td><td>3,326</td></tr>
<tr><td>LG</td><td>3,272</td></tr>
<tr><td>SS</td><td>3,230</td></tr>
<tr><td>HT</td><td>3,183</td></tr>
<tr><td>LT</td><td>3,148</td></tr>
<tr><td>HH</td><td>2,954</td></tr>
<tr><td>SK</td><td>2,158</td></tr>
<tr><td>HD</td><td>1,636</td></tr>
<tr><td>WO</td><td>1,611</td></tr>
<tr><td>NC</td><td>1,170</td></tr>
<tr><td>KT</td><td>1,022</td></tr>
<tr><td>SB</td><td>573</td></tr>
<tr><td>WE</td><td>24</td></tr>
<tr><td>EA</td><td>21</td></tr>
<tr><td>KR</td><td>4</td></tr>
<tr><td>CZ</td><td>2</td></tr>
<tr><td>MA</td><td>2</td></tr>
<tr><td>DR</td><td>1</td></tr>
<tr><td>KI</td><td>1</td></tr>
<tr><td>TW</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>stadium</code><span class="code-desc"> &mdash; 구장 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>Àá½Ç</td><td>6,119</td></tr>
<tr><td>»çÁ÷</td><td>2,781</td></tr>
<tr><td>ÇÑ¹ç</td><td>2,655</td></tr>
<tr><td>½Ã¹Î</td><td>2,278</td></tr>
<tr><td>¹®ÇÐ</td><td>2,013</td></tr>
<tr><td>¹«µî</td><td>1,946</td></tr>
<tr><td>¼ö¿ø</td><td>1,711</td></tr>
<tr><td>±¤ÁÖ</td><td>1,172</td></tr>
<tr><td>ÀÎÃµ</td><td>1,076</td></tr>
<tr><td>´ë±¸</td><td>901</td></tr>
<tr><td>°íÃ´</td><td>893</td></tr>
<tr><td>¸¶»ê</td><td>734</td></tr>
<tr><td>Ã¢¿ø</td><td>690</td></tr>
<tr><td>¸ñµ¿</td><td>613</td></tr>
<tr><td>ÀüÁÖ</td><td>575</td></tr>
<tr><td>Ã»ÁÖ</td><td>363</td></tr>
<tr><td>±¸´ö</td><td>197</td></tr>
<tr><td>´ëÀü</td><td>167</td></tr>
<tr><td>±º»ê</td><td>117</td></tr>
<tr><td>µ¿´ë¹®</td><td>117</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>stadium_key</code><span class="code-desc"> &mdash; 구장 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>JS</td><td>6,119</td></tr>
<tr><td>SJ</td><td>2,780</td></tr>
<tr><td>DJ</td><td>2,655</td></tr>
<tr><td>DG</td><td>2,278</td></tr>
<tr><td>MH</td><td>2,013</td></tr>
<tr><td>SW</td><td>1,711</td></tr>
<tr><td>KJ</td><td>1,496</td></tr>
<tr><td>KC</td><td>1,134</td></tr>
<tr><td>IC</td><td>1,075</td></tr>
<tr><td>DK</td><td>901</td></tr>
<tr><td>GC</td><td>893</td></tr>
<tr><td>MS</td><td>734</td></tr>
<tr><td>CW</td><td>690</td></tr>
<tr><td>MD</td><td>609</td></tr>
<tr><td>JJ</td><td>582</td></tr>
<tr><td>GJ</td><td>488</td></tr>
<tr><td>CJ</td><td>363</td></tr>
<tr><td>KD</td><td>197</td></tr>
<tr><td>DN</td><td>167</td></tr>
<tr><td>DM</td><td>117</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>dheader</code><span class="code-desc"> &mdash; 더블헤더 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>25,817</td></tr>
<tr><td>1</td><td>771</td></tr>
<tr><td>2</td><td>752</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>hpcode</code><span class="code-desc"> &mdash; 홈팀 선발투수 코드</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>vpcode</code><span class="code-desc"> &mdash; 원정팀 선발투수 코드</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>gtime</code><span class="code-desc"> &mdash; 경기 시작 시각</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>18:30</td><td>14,000</td></tr>
<tr><td>14:00</td><td>3,522</td></tr>
<tr><td>17:00</td><td>2,958</td></tr>
<tr><td>18:00</td><td>1,206</td></tr>
<tr><td>13:00</td><td>1,202</td></tr>
<tr><td>18:31</td><td>611</td></tr>
<tr><td>15:00</td><td>436</td></tr>
<tr><td>14:01</td><td>391</td></tr>
<tr><td>18:29</td><td>306</td></tr>
<tr><td>18:20</td><td>250</td></tr>
<tr><td>19:00</td><td>246</td></tr>
<tr><td>18:32</td><td>135</td></tr>
<tr><td>14:02</td><td>115</td></tr>
<tr><td>13:59</td><td>113</td></tr>
<tr><td>18:01</td><td>101</td></tr>
<tr><td>15:01</td><td>88</td></tr>
<tr><td>16:00</td><td>87</td></tr>
<tr><td>18:02</td><td>53</td></tr>
<tr><td>18:59</td><td>52</td></tr>
<tr><td>12:59</td><td>51</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>hscore</code><span class="code-desc"> &mdash; 홈팀 점수</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>vscore</code><span class="code-desc"> &mdash; 원정팀 점수</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>cancel_flag</code><span class="code-desc"> &mdash; 경기 취소 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>False</td><td>26,121</td></tr>
<tr><td>True</td><td>1,219</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>suspended_flag</code><span class="code-desc"> &mdash; 서스펜디드 여부</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>False</td><td>27,328</td></tr>
<tr><td>True</td><td>12</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gmkey</td><td>19820327SSLG0</td><td>19820328HDSS0</td><td>19820328HTLT0</td></tr>
<tr><td>game_flag</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>end_flag</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>gamedate</td><td>19820327</td><td>19820328</td><td>19820328</td></tr>
<tr><td>gyear</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>gmonth</td><td>03</td><td>03</td><td>03</td></tr>
<tr><td>gday</td><td>27</td><td>28</td><td>28</td></tr>
<tr><td>gweek</td><td>Åä</td><td>ÀÏ</td><td>ÀÏ</td></tr>
<tr><td>home</td><td>MBC</td><td>»ï¼º</td><td>·Ôµ¥</td></tr>
<tr><td>home_key</td><td>LG</td><td>SS</td><td>LT</td></tr>
<tr><td>visit</td><td>»ï¼º</td><td>»ï¹Ì</td><td>ÇØÅÂ</td></tr>
<tr><td>visit_key</td><td>SS</td><td>HD</td><td>HT</td></tr>
<tr><td>stadium</td><td>µ¿´ë¹®</td><td>½Ã¹Î</td><td>±¸´ö</td></tr>
<tr><td>stadium_key</td><td>DM</td><td>DG</td><td>KD</td></tr>
<tr><td>dheader</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>hpcode</td><td>82122</td><td>80620</td><td>82571</td></tr>
<tr><td>vpcode</td><td>80620</td><td>82954</td><td>82700</td></tr>
<tr><td>gtime</td><td>14:30</td><td>14:02</td><td>14:05</td></tr>
<tr><td>hscore</td><td>11</td><td>3</td><td>14</td></tr>
<tr><td>vscore</td><td>7</td><td>5</td><td>2</td></tr>
<tr><td>cancel_flag</td><td>False</td><td>False</td><td>False</td></tr>
<tr><td>suspended_flag</td><td>False</td><td>False</td><td>False</td></tr>
</tbody></table>
</div>

</div>
