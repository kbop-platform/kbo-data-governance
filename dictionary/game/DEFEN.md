---
title: DEFEN
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">DEFEN</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: </div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">846,736</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">12</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code></code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[약어 사전](../../standards/abbreviations.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">12개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">TB</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">팀 구분 (T=원정/Top, B=홈/Bottom)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">ONETURN</span></td><td><span class="col-std">one_turn_if</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">타순 (1~9)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">POSI</span></td><td><span class="col-std">position_cd</span></td><td><span class="col-type">varchar(5)</span></td><td></td><td></td><td><span class="col-desc">포지션 코드 (XY: X=교체순번, Y=포지션)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td></td><td></td><td><span class="col-desc">선수 코드 (5~6자리 숫자 문자열)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">PO</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">ASS</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">ERR</span></td><td><span class="col-std">err</span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc">실책</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">DP</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">PB</span></td><td><span class="col-std"></span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">INPUTTIME</span></td><td><span class="col-std">input_tm</span></td><td><span class="col-type">datetime</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">입력 시각</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">8개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>TB</code><span class="code-desc"> — 팀 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>423,738</td></tr>
<tr><td>T</td><td>422,998</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>POSI</code><span class="code-desc"> — 포지션 코드</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PO</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>ASS</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>594,550</td></tr>
<tr><td>1</td><td>123,439</td></tr>
<tr><td>2</td><td>58,894</td></tr>
<tr><td>3</td><td>34,571</td></tr>
<tr><td>4</td><td>19,185</td></tr>
<tr><td>5</td><td>9,616</td></tr>
<tr><td>6</td><td>4,160</td></tr>
<tr><td>7</td><td>1,559</td></tr>
<tr><td>8</td><td>521</td></tr>
<tr><td>9</td><td>172</td></tr>
<tr><td>10</td><td>53</td></tr>
<tr><td>11</td><td>12</td></tr>
<tr><td>12</td><td>4</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>ERR</code><span class="code-desc"> — 실책</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>812,870</td></tr>
<tr><td>1</td><td>32,303</td></tr>
<tr><td>2</td><td>1,506</td></tr>
<tr><td>3</td><td>54</td></tr>
<tr><td>4</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>DP</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>751,785</td></tr>
<tr><td>1</td><td>73,706</td></tr>
<tr><td>2</td><td>17,343</td></tr>
<tr><td>3</td><td>3,400</td></tr>
<tr><td>4</td><td>443</td></tr>
<tr><td>5</td><td>55</td></tr>
<tr><td>6</td><td>3</td></tr>
<tr><td>11</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>PB</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>843,501</td></tr>
<tr><td>1</td><td>3,138</td></tr>
<tr><td>2</td><td>90</td></tr>
<tr><td>3</td><td>7</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>19970915HHSB0</td><td>20050923LTHT0</td><td>20030710SKOB2</td></tr>
<tr><td>GDAY</td><td>19970915</td><td>20050923</td><td>20030710</td></tr>
<tr><td>TB</td><td>T</td><td>B</td><td>B</td></tr>
<tr><td>ONETURN</td><td>2</td><td>9</td><td>9</td></tr>
<tr><td>POSI</td><td>15</td><td>26</td><td>27</td></tr>
<tr><td>PCODE</td><td>93726</td><td>74605</td><td>73213</td></tr>
<tr><td>PO</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>ASS</td><td>0</td><td>2</td><td>2</td></tr>
<tr><td>ERR</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>DP</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>PB</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>INPUTTIME</td><td>2026-02-09 17:05:40.790000</td><td>2026-02-09 17:05:40.790000</td><td>2026-02-09 17:05:40.790000</td></tr>
</tbody></table>
</div>

</div>
