---
title: GAMEINFO
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">GAMEINFO</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GMKEY, GDAY</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">23,579</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">27</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 - Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀, 방송팀, 통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [코드 사전](../../standards-dict/codes.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">27개</span></div>

<div class="dict-encoding-warn">`GWEEK` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨 (예: `¸ñ`=목). nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(15)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">DBHD</span></td><td><span class="col-std">doubleheader_no</span></td><td><span class="col-type">char(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">더블헤더 번호 (0=일반, 1=1차, 2=2차)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">STADIUM</span></td><td><span class="col-std">stadium_nm</span></td><td><span class="col-type">nvarchar(40)</span></td><td></td><td></td><td><span class="col-desc">구장명</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">VTEAM</span></td><td><span class="col-std">away_team_cd</span></td><td><span class="col-type">nvarchar(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">원정팀 코드</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">HTEAM</span></td><td><span class="col-std">home_team_cd</span></td><td><span class="col-type">nvarchar(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈팀 코드</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">STTM</span></td><td><span class="col-std">start_tm</span></td><td><span class="col-type">char(4)</span></td><td></td><td></td><td><span class="col-desc">경기 시작 시각 (HHMM)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">ENTM</span></td><td><span class="col-std">end_tm</span></td><td><span class="col-type">nvarchar(8)</span></td><td></td><td></td><td><span class="col-desc">경기 종료 시각 (HHMM)</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">DLTM</span></td><td><span class="col-std">delay_tm</span></td><td><span class="col-type">nvarchar(8)</span></td><td></td><td></td><td><span class="col-desc">지연 시간 (분)</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">GMTM</span></td><td><span class="col-std">game_duration_tm</span></td><td><span class="col-type">nvarchar(8)</span></td><td></td><td></td><td><span class="col-desc">경기 소요 시간 (분)</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">STAD</span></td><td><span class="col-std">stadium_cd</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">구장 코드 (JS=잠실, SJ=사직, DJ=대전, DG=대구, MH=목동, SW=수원, KJ=광주, KC=고척, IC=인천 등)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">UMPC</span></td><td><span class="col-std">umpire_chief_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">주심 이름</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">UMP1</span></td><td><span class="col-std">umpire_1b_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">1루심 이름</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">UMP2</span></td><td><span class="col-std">umpire_2b_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">2루심 이름</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">UMP3</span></td><td><span class="col-std">umpire_3b_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">3루심 이름</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">UMPL</span></td><td><span class="col-std">umpire_lf_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">좌측 외야심 이름</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">UMPR</span></td><td><span class="col-std">umpire_rf_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">우측 외야심 이름</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">SCOA</span></td><td><span class="col-std">scorer_a_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">기록원 A 이름</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">SCOB</span></td><td><span class="col-std">scorer_b_nm</span></td><td><span class="col-type">nvarchar(16)</span></td><td></td><td></td><td><span class="col-desc">기록원 B 이름</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">TEMP</span></td><td><span class="col-std">temperature_va</span></td><td><span class="col-type">nvarchar(6)</span></td><td></td><td></td><td><span class="col-desc">기온 (×10, 예: 270=27.0℃)</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">MOIS</span></td><td><span class="col-std">humidity_va</span></td><td><span class="col-type">nvarchar(6)</span></td><td></td><td></td><td><span class="col-desc">습도 (%)</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">WEATH</span></td><td><span class="col-std">weather_cd</span></td><td><span class="col-type">nvarchar(4)</span></td><td></td><td></td><td><span class="col-desc">날씨 코드 (F=맑음, C=흐림, R=비, S=눈, 복합: FC/CR/CF/RC 등)</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">WIND</span></td><td><span class="col-std">wind_dir_cd</span></td><td><span class="col-type">nvarchar(6)</span></td><td></td><td></td><td><span class="col-desc">풍향 (16방위)</span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">WINS</span></td><td><span class="col-std">wind_speed_va</span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc">풍속 (m/s)</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">GWEEK</span></td><td><span class="col-std">game_week_nm</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">요일 (EUC-KR 인코딩)</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">CROWD</span></td><td><span class="col-std">crowd_cn</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">관중수</span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">CHAJUN</span></td><td><span class="col-std">round_no</span></td><td><span class="col-type">char(10)</span></td><td></td><td></td><td><span class="col-desc">차전 (라운드 번호)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">14개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> &mdash; 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>DBHD</code><span class="code-desc"> &mdash; 더블헤더 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>22,076</td></tr>
<tr><td>1</td><td>754</td></tr>
<tr><td>2</td><td>749</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>VTEAM</code><span class="code-desc"> &mdash; 원정팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>HT</td><td>2,819</td></tr>
<tr><td>SS</td><td>2,818</td></tr>
<tr><td>LG</td><td>2,818</td></tr>
<tr><td>LT</td><td>2,816</td></tr>
<tr><td>OB</td><td>2,816</td></tr>
<tr><td>HH</td><td>2,621</td></tr>
<tr><td>SK</td><td>1,770</td></tr>
<tr><td>HD</td><td>1,569</td></tr>
<tr><td>WO</td><td>1,250</td></tr>
<tr><td>NC</td><td>921</td></tr>
<tr><td>KT</td><td>791</td></tr>
<tr><td>SB</td><td>570</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>HTEAM</code><span class="code-desc"> &mdash; 홈팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>LT</td><td>2,819</td></tr>
<tr><td>OB</td><td>2,819</td></tr>
<tr><td>SS</td><td>2,816</td></tr>
<tr><td>LG</td><td>2,816</td></tr>
<tr><td>HT</td><td>2,816</td></tr>
<tr><td>HH</td><td>2,624</td></tr>
<tr><td>SK</td><td>1,771</td></tr>
<tr><td>HD</td><td>1,568</td></tr>
<tr><td>WO</td><td>1,248</td></tr>
<tr><td>NC</td><td>919</td></tr>
<tr><td>KT</td><td>793</td></tr>
<tr><td>SB</td><td>570</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>STTM</code><span class="code-desc"> &mdash; 경기 시작 시각</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>ENTM</code><span class="code-desc"> &mdash; 경기 종료 시각</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>DLTM</code><span class="code-desc"> &mdash; 지연 시간</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>GMTM</code><span class="code-desc"> &mdash; 경기 소요 시간</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TEMP</code><span class="code-desc"> &mdash; 기온</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>MOIS</code><span class="code-desc"> &mdash; 습도</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>WEATH</code><span class="code-desc"> &mdash; 날씨 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>F</td><td>13,299</td></tr>
<tr><td>C</td><td>9,153</td></tr>
<tr><td>R</td><td>905</td></tr>
<tr><td></td><td>137</td></tr>
<tr><td>CR</td><td>29</td></tr>
<tr><td>FC</td><td>22</td></tr>
<tr><td>CF</td><td>8</td></tr>
<tr><td>RC</td><td>5</td></tr>
<tr><td>흐</td><td>1</td></tr>
<tr><td>FR</td><td>1</td></tr>
<tr><td>W</td><td>1</td></tr>
<tr><td>F</td><td>1</td></tr>
<tr><td>SE</td><td>1</td></tr>
<tr><td>S</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>WIND</code><span class="code-desc"> &mdash; 풍향</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>W</td><td>3,604</td></tr>
<tr><td>SW</td><td>2,720</td></tr>
<tr><td>WNW</td><td>1,973</td></tr>
<tr><td>NW</td><td>1,851</td></tr>
<tr><td>WSW</td><td>1,648</td></tr>
<tr><td>S</td><td>1,490</td></tr>
<tr><td>NE</td><td>1,347</td></tr>
<tr><td>E</td><td>1,211</td></tr>
<tr><td>SSW</td><td>1,137</td></tr>
<tr><td>SE</td><td>1,103</td></tr>
<tr><td>ENE</td><td>877</td></tr>
<tr><td></td><td>784</td></tr>
<tr><td>NNW</td><td>746</td></tr>
<tr><td>N</td><td>743</td></tr>
<tr><td>ESE</td><td>741</td></tr>
<tr><td>SSE</td><td>602</td></tr>
<tr><td>NNE</td><td>461</td></tr>
<tr><td>0</td><td>267</td></tr>
<tr><td>WW</td><td>31</td></tr>
<tr><td>WS</td><td>23</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>WINS</code><span class="code-desc"> &mdash; 풍속</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>CHAJUN</code><span class="code-desc"> &mdash; 차전</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>19820327SSLG0</td><td>19820328HDSS0</td><td>19820328HTLT0</td></tr>
<tr><td>GDAY</td><td>19820327</td><td>19820328</td><td>19820328</td></tr>
<tr><td>DBHD</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>STADIUM</td><td>한밭</td><td>수원</td><td>고척</td></tr>
<tr><td>VTEAM</td><td>OB</td><td>SK</td><td>SS</td></tr>
<tr><td>HTEAM</td><td>HH</td><td>KT</td><td>WO</td></tr>
<tr><td>STTM</td><td>1830</td><td>1829</td><td>1830</td></tr>
<tr><td>ENTM</td><td>2127</td><td>2145</td><td>2112</td></tr>
<tr><td>DLTM</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>GMTM</td><td>257</td><td>316</td><td>242</td></tr>
<tr><td>STAD</td><td>DJ</td><td>SW</td><td>GC</td></tr>
<tr><td>UMPC</td><td>차정구</td><td>박종철</td><td>이용혁</td></tr>
<tr><td>UMP1</td><td>유덕형</td><td>오훈규</td><td>이계성</td></tr>
<tr><td>UMP2</td><td>전일수</td><td>문동균</td><td>이민호</td></tr>
<tr><td>UMP3</td><td>권영철</td><td>나광남</td><td>문승훈</td></tr>
<tr><td>UMPL</td><td></td><td></td><td></td></tr>
<tr><td>UMPR</td><td></td><td></td><td></td></tr>
<tr><td>SCOA</td><td>이주헌</td><td>진철훈</td><td>한인희</td></tr>
<tr><td>SCOB</td><td>김형준</td><td>송형민</td><td>김영성</td></tr>
<tr><td>TEMP</td><td>245</td><td>161</td><td>160</td></tr>
<tr><td>MOIS</td><td>47</td><td>89</td><td>90</td></tr>
<tr><td>WEATH</td><td>F</td><td>C</td><td>C</td></tr>
<tr><td>WIND</td><td>NW</td><td>NW</td><td>W</td></tr>
<tr><td>WINS</td><td>1</td><td>3</td><td>2</td></tr>
<tr><td>GWEEK</td><td>¸ñ</td><td>¸ñ</td><td>¸ñ</td></tr>
<tr><td>CROWD</td><td>4122</td><td>4472</td><td>3918</td></tr>
<tr><td>CHAJUN</td><td>3</td><td>3</td><td>3</td></tr>
</tbody></table>
</div>

</div>
