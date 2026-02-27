---
title: GAMECONTAPP
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">GAMECONTAPP</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GMKEY, GYEAR, SERNO</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">2,531,702</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">29</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GYEAR, SERNO</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 - Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀, 분석팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[코드 사전](../../standards-dict/codes.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">29개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">SERNO</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">일련번호</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">TURN</span></td><td><span class="col-std">turn_no</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타순</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">INN</span></td><td><span class="col-std">ip</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">TB</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 구분 (T=원정, B=홈)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">INN2</span></td><td><span class="col-std">inn_2_score</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">2회 타격 결과 (HOW 코드, EUC-KR)</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">OCOUNT</span></td><td><span class="col-std">opp_count</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">아웃 카운트 (0=무사, 1=1사, 2=2사, 4=이닝종료/체인지)</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">BCOUNT</span></td><td><span class="col-std">ball_count_cd</span></td><td><span class="col-type">varchar(30)</span></td><td></td><td></td><td><span class="col-desc">투구 시퀀스 상세 (S/B/T/F/H 등)</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">RTURN</span></td><td><span class="col-std">real_turn_no</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">실제 타순 (교체 포함)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HOW</span></td><td><span class="col-std">how_cd</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">플레이 결과 코드 (H1=안타, H2=2루타, H3=3루타, HR=홈런, BB=볼넷, KK=삼진헛스윙, KN=삼진, GR=땅볼, FL=플라이, GD=병살타, SB=도루, HP=사구, SH=희생번트, SF=희생플라이, ER=실책 등 49종)</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">FIELD</span></td><td><span class="col-std">field_cd</span></td><td><span class="col-type">varchar(25)</span></td><td></td><td></td><td><span class="col-desc">수비 기록 코드 (복합: 포지션번호+동작코드, 예: F9=우익수플라이, 3N=1루수, 4 6B=2루수→유격수 병살 등)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">PLACE</span></td><td><span class="col-std">place_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">타구 방향 코드 (1~9=수비포지션 방향, A=공중, B=번트, C=중견방향, E=아웃/기타, R=우측, S=유격수, F=파울, H=홈, I=인필드)</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">HITTER</span></td><td><span class="col-std">hitter_nm</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">타자 선수 코드</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">HITNAME</span></td><td><span class="col-std">hitter_nm</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">타자 이름 (EUC-KR)</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">PITNAME</span></td><td><span class="col-std">pitcher_nm</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">투수 이름 (EUC-KR)</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">PITCHER</span></td><td><span class="col-std">pitcher_nm</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">투수 선수 코드</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">CATNAME</span></td><td><span class="col-std">catcher_nm</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">포수 이름 (EUC-KR)</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">CATCHER</span></td><td><span class="col-std">catcher_id</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">포수 선수 코드</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">BCNT</span></td><td><span class="col-std">ball_count_cd</span></td><td><span class="col-type">char(3)</span></td><td></td><td></td><td><span class="col-desc">볼카운트 (S-B 형식)</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">TSCORE</span></td><td><span class="col-std">total_score</span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc">원정팀 누적 득점</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">BSCORE</span></td><td><span class="col-std">bat_score</span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc">홈팀 누적 득점</span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">BASE1B</span></td><td><span class="col-std">base_1b_before_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">1루 주자 타순 (플레이 전)</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">BASE2B</span></td><td><span class="col-std">base_2b_before_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">2루 주자 타순 (플레이 전)</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">BASE3B</span></td><td><span class="col-std">base_3b_before_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">3루 주자 타순 (플레이 전)</span></td></tr>
<tr><td class="col-num">27</td><td><span class="col-name">BASE1A</span></td><td><span class="col-std">base_1b_after_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">1루 주자 타순 (플레이 후)</span></td></tr>
<tr><td class="col-num">28</td><td><span class="col-name">BASE2A</span></td><td><span class="col-std">base_2b_after_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">2루 주자 타순 (플레이 후)</span></td></tr>
<tr><td class="col-num">29</td><td><span class="col-name">BASE3A</span></td><td><span class="col-std">base_3b_after_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">3루 주자 타순 (플레이 후)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">23개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> &mdash; 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SERNO</code><span class="code-desc"> &mdash; 일련번호</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TURN</code><span class="code-desc"> &mdash; 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INN</code><span class="code-desc"> &mdash; 이닝</span></summary>
<div class="code-ref">고유값 18종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB</code><span class="code-desc"> &mdash; 팀 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>T</td><td>1,287,178</td></tr>
<tr><td>B</td><td>1,244,524</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>INN2</code><span class="code-desc"> &mdash; 2회 타격 결과</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>2,521,429</td></tr>
<tr><td>2</td><td>10,269</td></tr>
<tr><td>3</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>OCOUNT</code><span class="code-desc"> &mdash; 아웃 카운트</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>873,921</td></tr>
<tr><td>2</td><td>873,911</td></tr>
<tr><td>0</td><td>745,166</td></tr>
<tr><td>4</td><td>38,704</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>RTURN</code><span class="code-desc"> &mdash; 실제 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HOW</code><span class="code-desc"> &mdash; 플레이 결과 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>BH</td><td>484,156</td></tr>
<tr><td>GR</td><td>414,454</td></tr>
<tr><td>FL</td><td>342,069</td></tr>
<tr><td>KK</td><td>269,138</td></tr>
<tr><td>H1</td><td>268,791</td></tr>
<tr><td>BB</td><td>159,412</td></tr>
<tr><td>FO</td><td>81,843</td></tr>
<tr><td>H2</td><td>73,289</td></tr>
<tr><td>FF</td><td>47,609</td></tr>
<tr><td>HR</td><td>39,230</td></tr>
<tr><td>SB</td><td>36,023</td></tr>
<tr><td>GD</td><td>35,668</td></tr>
<tr><td>HI</td><td>30,275</td></tr>
<tr><td>LL</td><td>29,488</td></tr>
<tr><td>SH</td><td>26,743</td></tr>
<tr><td>HP</td><td>24,471</td></tr>
<tr><td>ER</td><td>24,148</td></tr>
<tr><td>CS</td><td>19,053</td></tr>
<tr><td>KN</td><td>18,929</td></tr>
<tr><td>TO</td><td>17,433</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PLACE</code><span class="code-desc"> &mdash; 타구 방향 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>A</td><td>566,292</td></tr>
<tr><td>1</td><td>420,424</td></tr>
<tr><td>2</td><td>419,622</td></tr>
<tr><td>3</td><td>418,858</td></tr>
<tr><td>B</td><td>316,534</td></tr>
<tr><td>E</td><td>191,604</td></tr>
<tr><td>C</td><td>168,459</td></tr>
<tr><td>R</td><td>15,130</td></tr>
<tr><td>S</td><td>6,791</td></tr>
<tr><td>F</td><td>6,767</td></tr>
<tr><td>0</td><td>619</td></tr>
<tr><td>H</td><td>577</td></tr>
<tr><td>I</td><td>22</td></tr>
<tr><td>4</td><td>2</td></tr>
<tr><td></td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>HITTER</code><span class="code-desc"> &mdash; 타자 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PITCHER</code><span class="code-desc"> &mdash; 투수 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>CATCHER</code><span class="code-desc"> &mdash; 포수 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BCNT</code><span class="code-desc"> &mdash; 볼카운트</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0-0</td><td>341,395</td></tr>
<tr><td>2-2</td><td>320,514</td></tr>
<tr><td>2-1</td><td>318,415</td></tr>
<tr><td>2-3</td><td>314,463</td></tr>
<tr><td>1-1</td><td>241,431</td></tr>
<tr><td>1-0</td><td>224,951</td></tr>
<tr><td>0-1</td><td>215,724</td></tr>
<tr><td>1-2</td><td>149,341</td></tr>
<tr><td>2-0</td><td>147,190</td></tr>
<tr><td>1-3</td><td>130,716</td></tr>
<tr><td>0-2</td><td>70,728</td></tr>
<tr><td>0-3</td><td>56,834</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>TSCORE</code><span class="code-desc"> &mdash; 원정팀 누적 득점</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BSCORE</code><span class="code-desc"> &mdash; 홈팀 누적 득점</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BASE1B</code><span class="code-desc"> &mdash; 1루 주자 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BASE2B</code><span class="code-desc"> &mdash; 2루 주자 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BASE3B</code><span class="code-desc"> &mdash; 3루 주자 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BASE1A</code><span class="code-desc"> &mdash; 1루 주자 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BASE2A</code><span class="code-desc"> &mdash; 2루 주자 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BASE3A</code><span class="code-desc"> &mdash; 3루 주자 타순</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>19820327SSLG0</td><td>19820327SSLG0</td><td>19820327SSLG0</td></tr>
<tr><td>GYEAR</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>GDAY</td><td>20250325</td><td>20250325</td><td>20250325</td></tr>
<tr><td>SERNO</td><td>10</td><td>20</td><td>30</td></tr>
<tr><td>TURN</td><td>14</td><td>14</td><td>16</td></tr>
<tr><td>INN</td><td>4</td><td>4</td><td>5</td></tr>
<tr><td>TB</td><td>B</td><td>B</td><td>T</td></tr>
<tr><td>INN2</td><td></td><td></td><td></td></tr>
<tr><td>OCOUNT</td><td>1</td><td>2</td><td>0</td></tr>
<tr><td>BCOUNT</td><td>SBT</td><td>BH</td><td>BBBTFT</td></tr>
<tr><td>RTURN</td><td>12</td><td></td><td></td></tr>
<tr><td>HOW</td><td>CS</td><td>GR</td><td>KK</td></tr>
<tr><td>FIELD</td><td>2 5T</td><td>1 3</td><td>2T</td></tr>
<tr><td>PLACE</td><td>2</td><td>3</td><td>1</td></tr>
<tr><td>HITTER</td><td>69102</td><td>69102</td><td>79608</td></tr>
<tr><td>HITNAME</td><td>¹®º¸°æ</td><td>¹®º¸°æ</td><td>¾ÈÄ¡È«</td></tr>
<tr><td>PITNAME</td><td>·ùÇöÁø</td><td>·ùÇöÁø</td><td>¿¡¸£³­µ¥½º</td></tr>
<tr><td>PITCHER</td><td>76715</td><td>76715</td><td>54119</td></tr>
<tr><td>CATNAME</td><td>ÃÖÀçÈÆ</td><td>ÃÖÀçÈÆ</td><td>¹Úµ¿¿ø</td></tr>
<tr><td>CATCHER</td><td>78288</td><td>78288</td><td>79365</td></tr>
<tr><td>BCNT</td><td>2-1</td><td>2-2</td><td>2-3</td></tr>
<tr><td>TSCORE</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BSCORE</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BASE1B</td><td></td><td></td><td></td></tr>
<tr><td>BASE2B</td><td>12</td><td></td><td></td></tr>
<tr><td>BASE3B</td><td></td><td></td><td></td></tr>
<tr><td>BASE1A</td><td></td><td></td><td></td></tr>
<tr><td>BASE2A</td><td></td><td></td><td></td></tr>
<tr><td>BASE3A</td><td></td><td></td><td></td></tr>
</tbody></table>
</div>

</div>
