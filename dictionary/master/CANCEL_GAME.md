---
title: CANCEL_GAME
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-access">Public</span>
  </div>
  <div class="dict-hero-title">CANCEL_GAME</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: LE_ID, SR_ID, G_ID</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">1,290</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">6</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">발생 즉시</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기운영팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>LE_ID, SR_ID, G_ID</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 - Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">경기운영팀 (R-05)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">발생 즉시</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">운영팀, 방송팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Public</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[일정 관리](../products/schedule.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">6개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">LE_ID</span></td><td><span class="col-std">league_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">리그 ID (1=1군)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">SR_ID</span></td><td><span class="col-std">series_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시리즈 ID (0=정규시즌, 1=올스타전, 3=준플레이오프, 4=미확인, 5=플레이오프, 6=미확인, 7=한국시리즈, 8=와일드카드, 9=기타)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">G_ID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (YYYYMMDDVVHH# 형식)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">CANCEL_SC_NM</span></td><td><span class="col-std">cancel_sc_nm</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">경기 취소 사유명</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">REG_DT</span></td><td><span class="col-std">reg_dt</span></td><td><span class="col-type">datetime</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">등록 일시</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">4개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>LE_ID</code><span class="code-desc"> &mdash; 리그 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>1,290</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SR_ID</code><span class="code-desc"> &mdash; 시리즈 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>1,120</td></tr>
<tr><td>1</td><td>157</td></tr>
<tr><td>5</td><td>4</td></tr>
<tr><td>3</td><td>4</td></tr>
<tr><td>7</td><td>3</td></tr>
<tr><td>4</td><td>1</td></tr>
<tr><td>9</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>SEASON_ID</code><span class="code-desc"> &mdash; 시즌 ID</span></summary>
<div class="code-ref">고유값 16종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>G_ID</code><span class="code-desc"> &mdash; 경기 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>20100427SSLG0</td><td>1</td></tr>
<tr><td>20100421SKOB0</td><td>1</td></tr>
<tr><td>20100421LGWO0</td><td>1</td></tr>
<tr><td>20100418LGHT0</td><td>1</td></tr>
<tr><td>20100414OBHT0</td><td>1</td></tr>
<tr><td>20100401SSHT0</td><td>1</td></tr>
<tr><td>20100401SKLG0</td><td>1</td></tr>
<tr><td>20100401OBWO0</td><td>1</td></tr>
<tr><td>20100401LTHH0</td><td>1</td></tr>
<tr><td>20100331SKLG0</td><td>1</td></tr>
<tr><td>20100331OBWO0</td><td>1</td></tr>
<tr><td>20100331LTHH0</td><td>1</td></tr>
<tr><td>20100320HTLG0</td><td>1</td></tr>
<tr><td>20100320HHSK0</td><td>1</td></tr>
<tr><td>20100318HHLG0</td><td>1</td></tr>
<tr><td>20100317WOHH0</td><td>1</td></tr>
<tr><td>20100311LTSK0</td><td>1</td></tr>
<tr><td>20100310OBWO0</td><td>1</td></tr>
<tr><td>20100310LTSS0</td><td>1</td></tr>
<tr><td>20100310LGSK0</td><td>1</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>LE_ID</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>SR_ID</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SEASON_ID</td><td>2010</td><td>2010</td><td>2010</td></tr>
<tr><td>G_ID</td><td>20100331LTHH0</td><td>20100331OBWO0</td><td>20100331SKLG0</td></tr>
<tr><td>CANCEL_SC_NM</td><td>¿ìÃµÃë¼Ò</td><td>¿ìÃµÃë¼Ò</td><td>¿ìÃµÃë¼Ò</td></tr>
<tr><td>REG_DT</td><td>2025-09-01 14:04:52.060000</td><td>2025-09-01 14:04:52.060000</td><td>2025-09-01 14:04:52.060000</td></tr>
</tbody></table>
</div>

</div>
