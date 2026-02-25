---
title: IE_GameList
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">실시간</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">IE_GameList</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: gameID, GYEAR</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">15,908</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">6</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">실시간</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">S2i 운영</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>gameID, GYEAR</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 — Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">S2i 운영 (R-06)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">실시간 (&lt; 5초)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">앱 서비스</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[실시간 경기](../products/live-game.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">6개</span></div>

<div class="dict-encoding-warn">`HomeName`, `VisitName` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">gameID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (GMKEY와 동일 형식)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">HomeName</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(8)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">HomeMascot</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">VisitName</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(8)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">VisitMascot</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">3개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> — 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HomeName</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>»ï¼º</td><td>1,766</td></tr>
<tr><td>·Ôµ¥</td><td>1,761</td></tr>
<tr><td>ÇÑÈ­</td><td>1,751</td></tr>
<tr><td>µÎ»ê</td><td>1,716</td></tr>
<tr><td>LG</td><td>1,680</td></tr>
<tr><td>KIA</td><td>1,537</td></tr>
<tr><td>SK</td><td>1,293</td></tr>
<tr><td>NC</td><td>1,124</td></tr>
<tr><td>KT</td><td>949</td></tr>
<tr><td>³Ø¼¾</td><td>699</td></tr>
<tr><td>Å°¿ò</td><td>499</td></tr>
<tr><td>SSG</td><td>440</td></tr>
<tr><td>Çö´ë</td><td>267</td></tr>
<tr><td>±â¾Æ</td><td>210</td></tr>
<tr><td>¿ì¸®</td><td>196</td></tr>
<tr><td>³ª´®</td><td>5</td></tr>
<tr><td>µå¸²</td><td>3</td></tr>
<tr><td>´ëÇÑ¹Î±¹</td><td>3</td></tr>
<tr><td>¿þ½ºÅÏ</td><td>2</td></tr>
<tr><td>ÀÌ½ºÅÏ</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>VisitName</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>µÎ»ê</td><td>1,819</td></tr>
<tr><td>LG</td><td>1,791</td></tr>
<tr><td>»ï¼º</td><td>1,715</td></tr>
<tr><td>ÇÑÈ­</td><td>1,678</td></tr>
<tr><td>·Ôµ¥</td><td>1,662</td></tr>
<tr><td>KIA</td><td>1,497</td></tr>
<tr><td>SK</td><td>1,292</td></tr>
<tr><td>NC</td><td>1,080</td></tr>
<tr><td>KT</td><td>936</td></tr>
<tr><td>³Ø¼¾</td><td>712</td></tr>
<tr><td>Å°¿ò</td><td>564</td></tr>
<tr><td>SSG</td><td>445</td></tr>
<tr><td>Çö´ë</td><td>273</td></tr>
<tr><td>¿ì¸®</td><td>219</td></tr>
<tr><td>±â¾Æ</td><td>205</td></tr>
<tr><td>µå¸²</td><td>5</td></tr>
<tr><td>³ª´®</td><td>3</td></tr>
<tr><td>¼­±º</td><td>2</td></tr>
<tr><td>¿þ½ºÅÏ</td><td>2</td></tr>
<tr><td>ÀÌ½ºÅÏ</td><td>2</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>gameID</td><td>20040310LTSS0</td><td>20040313HDHH0</td><td>20040313LGSS0</td></tr>
<tr><td>GYEAR</td><td>2004</td><td>2004</td><td>2004</td></tr>
<tr><td>HomeName</td><td>»ï¼º</td><td>ÇÑÈ­</td><td>»ï¼º</td></tr>
<tr><td>HomeMascot</td><td>¶óÀÌ¿ÂÁî</td><td>ÀÌ±Û½º</td><td>¶óÀÌ¿ÂÁî</td></tr>
<tr><td>VisitName</td><td>·Ôµ¥</td><td>Çö´ë</td><td>LG</td></tr>
<tr><td>VisitMascot</td><td>ÀÚÀÌ¾ðÃ÷</td><td>À¯´ÏÄÜ½º</td><td>Æ®À©½º</td></tr>
</tbody></table>
</div>

</div>
