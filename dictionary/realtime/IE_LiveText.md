---
title: IE_LiveText
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">실시간</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">IE_LiveText</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gameID, GYEAR, SeqNO</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">8,005,079</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">7</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">실시간</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">S2i 운영</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gameID, GYEAR, SeqNO</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 - Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">S2i 운영 (R-06)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">실시간 (&lt; 5초)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀, 앱 서비스</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[실시간 경기](../products/live-game.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">7개</span></div>

<div class="dict-encoding-warn">`textStyle` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gameID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">LiveText</span></td><td><span class="col-std">live_text</span></td><td><span class="col-type">varchar(200)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실시간 문자 중계 텍스트</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">SeqNO</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">순번</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">Inning</span></td><td><span class="col-std">inning_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">bTop</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">초/말 구분 (1=초, 0=말)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">textStyle</span></td><td><span class="col-std">text_style_cd</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">텍스트 스타일 코드 (0=이닝시작, 1=일반, 2=타석시작, 7=교체, 8=투구상세, 13=투구결과, 14=타석결과, 23=득점, 24=주자이동, 44=피치클럭, 99=특수)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">5개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SeqNO</code><span class="code-desc"> &mdash; 순번</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Inning</code><span class="code-desc"> &mdash; 이닝</span></summary>
<div class="code-ref">고유값 19종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>bTop</code><span class="code-desc"> &mdash; 초/말 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>4,045,213</td></tr>
<tr><td>0</td><td>3,958,252</td></tr>
<tr><td>99</td><td>1,614</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>textStyle</code><span class="code-desc"> &mdash; 텍스트 스타일 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>4,525,865</td></tr>
<tr><td>8</td><td>1,181,293</td></tr>
<tr><td>13</td><td>1,059,661</td></tr>
<tr><td>14</td><td>278,278</td></tr>
<tr><td>2</td><td>276,181</td></tr>
<tr><td>0</td><td>268,080</td></tr>
<tr><td>24</td><td>174,729</td></tr>
<tr><td>23</td><td>110,533</td></tr>
<tr><td>99</td><td>72,739</td></tr>
<tr><td>7</td><td>57,355</td></tr>
<tr><td>44</td><td>365</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gameID</td><td>20040310LTSS0</td><td>20040310LTSS0</td><td>20040310LTSS0</td></tr>
<tr><td>GYEAR</td><td>2004</td><td>2004</td><td>2004</td></tr>
<tr><td>LiveText</td><td>1È¸ÃÊ ·Ôµ¥°ø°Ý</td><td>1¹øÅ¸ÀÚ ±è´ëÀÍ</td><td>1±¸ ½ºÆ®¶óÀÌÅ©</td></tr>
<tr><td>SeqNO</td><td>1</td><td>2</td><td>3</td></tr>
<tr><td>Inning</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>bTop</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>textStyle</td><td>0</td><td>8</td><td>1</td></tr>
</tbody></table>
</div>

</div>
