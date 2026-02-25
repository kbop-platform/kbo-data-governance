---
title: PERSON
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Restricted</span>
  </div>
  <div class="dict-hero-title">PERSON</div>
  <div class="dict-hero-sub">DB2_MINOR_BASEBALL &middot; PK: GYEAR, PCODE</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">13,902</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">16</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">시즌 전 갱신</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_MINOR_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GYEAR, PCODE</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 — Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">시즌 전 갱신</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Restricted</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[선수 프로필](../products/player-profile.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-note">
**관련 테이블**: [person](./person.md)(1군, 20컬럼)의 2군 버전. T_ID/ENGNAME/DRAFT/REG_DT 없음.
1군 [person](./person.md)과 스키마 거의 동일하나 DB가 분리되어 있음 (MINOR_BASEBALL).
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">16개</span></div>

<div class="dict-encoding-warn">`TEAM`, `POSITION`, `HITTYPE` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자 문자열)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선수명 (varchar=EUC-KR 깨짐 가능)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">TEAM</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">varchar(8)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 코드 (2자리, HH=키움, HT=KIA 등)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">POS</span></td><td><span class="col-std">position_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">포지션 코드</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">POSITION</span></td><td><span class="col-std">position_nm</span></td><td><span class="col-type">varchar(4)</span></td><td></td><td></td><td><span class="col-desc">포지션</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">BACKNUM</span></td><td><span class="col-std">back_no</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">등번호</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">CNAME</span></td><td><span class="col-std">player_hanja_nm</span></td><td><span class="col-type">varchar(30)</span></td><td></td><td></td><td><span class="col-desc">한자 이름</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">HITTYPE</span></td><td><span class="col-std">bat_throw_cd</span></td><td><span class="col-type">varchar(8)</span></td><td></td><td></td><td><span class="col-desc">타석 방향</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">BIRTH</span></td><td><span class="col-std">birth_dt</span></td><td><span class="col-type">varchar(8)</span></td><td></td><td></td><td><span class="col-desc">생년월일</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">HEIGHT</span></td><td><span class="col-std">height_va</span></td><td><span class="col-type">varchar(3)</span></td><td></td><td></td><td><span class="col-desc">키</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">WEIGHT</span></td><td><span class="col-std">weight_va</span></td><td><span class="col-type">varchar(3)</span></td><td></td><td></td><td><span class="col-desc">몸무게</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">INDATE</span></td><td><span class="col-std">join_dt</span></td><td><span class="col-type">varchar(8)</span></td><td></td><td></td><td><span class="col-desc">입단일</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">PROMISE</span></td><td><span class="col-std">signing_bonus_va</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">계약금</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">MONEY</span></td><td><span class="col-std">salary_va</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">연봉</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">CAREER</span></td><td><span class="col-std">career_nm</span></td><td><span class="col-type">varchar(255)</span></td><td></td><td></td><td><span class="col-desc">경력</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">10개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> — 시즌 연도</span></summary>
<div class="code-ref">고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TEAM</code><span class="code-desc"> — 팀 코드</span></summary>
<div class="code-ref">팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>POS</code><span class="code-desc"> — 포지션 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>6,898</td></tr>
<tr><td>3</td><td>1,423</td></tr>
<tr><td>7</td><td>1,358</td></tr>
<tr><td>2</td><td>1,287</td></tr>
<tr><td>4</td><td>645</td></tr>
<tr><td>9</td><td>597</td></tr>
<tr><td>5</td><td>569</td></tr>
<tr><td>6</td><td>566</td></tr>
<tr><td>8</td><td>538</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>POSITION</code><span class="code-desc"> — 포지션</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>Åõ</td><td>6,898</td></tr>
<tr><td>³»</td><td>3,213</td></tr>
<tr><td>¿Ü</td><td>2,504</td></tr>
<tr><td>Æ÷</td><td>1,287</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>HITTYPE</code><span class="code-desc"> — 타석 방향</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>¿ìÅõ¿ìÅ¸</td><td>8,351</td></tr>
<tr><td>ÁÂÅõÁÂÅ¸</td><td>2,446</td></tr>
<tr><td>¿ìÅõÁÂÅ¸</td><td>2,245</td></tr>
<tr><td>¿ì¾ð¿ìÅ¸</td><td>591</td></tr>
<tr><td>¿ìÅõ¾çÅ¸</td><td>151</td></tr>
<tr><td>ÁÂÅõ¿ìÅ¸</td><td>49</td></tr>
<tr><td>¿ì¾ðÁÂÅ¸</td><td>37</td></tr>
<tr><td>¿ì¾ð¾çÅ¸</td><td>18</td></tr>
<tr><td>ÁÂ¾ðÁÂÅ¸</td><td>10</td></tr>
<tr><td>ÁÂÅõ¾çÅ¸</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>BIRTH</code><span class="code-desc"> — 생년월일</span></summary>
<div class="code-ref">연속값 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HEIGHT</code><span class="code-desc"> — 키</span></summary>
<div class="code-ref">연속값 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>WEIGHT</code><span class="code-desc"> — 몸무게</span></summary>
<div class="code-ref">연속값 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INDATE</code><span class="code-desc"> — 입단일</span></summary>
<div class="code-ref">연속값 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GYEAR</td><td>2010</td><td>2010</td><td>2010</td></tr>
<tr><td>PCODE</td><td>60100</td><td>60102</td><td>60105</td></tr>
<tr><td>NAME</td><td>±è¹ÎÇõ</td><td>°íÁ¾¿í</td><td>¹èÀçÈ¯</td></tr>
<tr><td>TEAM</td><td>KT</td><td>SSG</td><td>»ó¹«</td></tr>
<tr><td>POS</td><td>7</td><td>7</td><td>1</td></tr>
<tr><td>POSITION</td><td>¿Ü</td><td>¿Ü</td><td>Åõ</td></tr>
<tr><td>BACKNUM</td><td>53</td><td>38</td><td>61</td></tr>
<tr><td>CNAME</td><td>(ÑÑÚÂúÒ)</td><td>(ÍÔðóéô)</td><td>(ÛÑî¥üº)</td></tr>
<tr><td>HITTYPE</td><td>¿ìÅõÁÂÅ¸</td><td>¿ìÅõÁÂÅ¸</td><td>¿ìÅõ¿ìÅ¸</td></tr>
<tr><td>BIRTH</td><td>19951121</td><td>19890111</td><td>19950224</td></tr>
<tr><td>HEIGHT</td><td>181</td><td>184</td><td>186</td></tr>
<tr><td>WEIGHT</td><td>71</td><td>83</td><td>105</td></tr>
<tr><td>INDATE</td><td>201401</td><td>201101</td><td>201401</td></tr>
<tr><td>PROMISE</td><td>6000¸¸¿ø</td><td>8000¸¸¿ø</td><td>15000¸¸¿ø</td></tr>
<tr><td>MONEY</td><td>6500¸¸¿ø</td><td>11000¸¸¿ø</td><td>9000¸¸¿ø</td></tr>
<tr><td>CAREER</td><td>±¤ÁÖ¼­¼®ÃÊ-¹èÀçÁß-¹èÀç°í-KT-»ó¹«</td><td>¿ª»ïÃÊ-´ëÄ¡Áß-°æ±â°í-ÇÑ¾ç´ë-³Ø¼¾-»ó¹«-³Ø¼¾-SK</td><td>°¡µ¿ÃÊ-Àá½ÅÁß-¼­¿ï°í-NC-»ó¹«</td></tr>
</tbody></table>
</div>

</div>
