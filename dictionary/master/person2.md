---
title: person2
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-access">Restricted</span>
  </div>
  <div class="dict-hero-title">person2</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: GYEAR, PCODE, NAME</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">91,891</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">17</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">시즌 전 갱신</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GYEAR, PCODE, NAME</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 - Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">시즌 전 갱신</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Restricted</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[선수 프로필](../products/player-profile.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-note">
**관련 테이블**: person 계열 구버전. [person](./person.md)(20컬럼) 대비 ENGNAME, DRAFT, REG_DT 없고 PK에 NAME 포함.
신규 시스템에서는 [person](./person.md) 기준으로 통합 권고.
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">17개</span></div>

<div class="dict-encoding-warn">`TEAM`, `POSITION`, `HITTYPE` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(20)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수명</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">TEAM</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">varchar(8)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 코드 (HH=한화, LG, SK, HT=KIA, LT=롯데, OB=두산, SS=삼성, WO=키움, NC, KT 등 2자리)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">T_ID</span></td><td><span class="col-std">team_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">팀 코드 (2자리)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">POS</span></td><td><span class="col-std">position_cd</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">포지션 코드 (1=투수, 2=포수, 3=1루, 4=2루, 5=3루, 6=유격, 7=좌익, 8=중견, 9=우익, 0=미분류)</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">POSITION</span></td><td><span class="col-std">position_nm</span></td><td><span class="col-type">varchar(4)</span></td><td></td><td></td><td><span class="col-desc">포지션명 (EUC-KR: 투수/포수/1루수/2루수/3루수/유격수/좌익수/중견수/우익수/지명타자 등)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">BACKNUM</span></td><td><span class="col-std">back_no</span></td><td><span class="col-type">varchar(50)</span></td><td></td><td></td><td><span class="col-desc">등번호</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">CNAME</span></td><td><span class="col-std">player_hanja_nm</span></td><td><span class="col-type">varchar(30)</span></td><td></td><td></td><td><span class="col-desc">한자 이름</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">HITTYPE</span></td><td><span class="col-std">bat_throw_cd</span></td><td><span class="col-type">varchar(8)</span></td><td></td><td></td><td><span class="col-desc">투타 유형 (우투우타/좌투좌타/우투좌타/우언우타/우투양타 등, EUC-KR)</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">BIRTH</span></td><td><span class="col-std">birth_dt</span></td><td><span class="col-type">varchar(8)</span></td><td></td><td></td><td><span class="col-desc">생년월일</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HEIGHT</span></td><td><span class="col-std">height_va</span></td><td><span class="col-type">varchar(3)</span></td><td></td><td></td><td><span class="col-desc">키 (cm)</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">WEIGHT</span></td><td><span class="col-std">weight_va</span></td><td><span class="col-type">varchar(3)</span></td><td></td><td></td><td><span class="col-desc">몸무게 (kg)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">INDATE</span></td><td><span class="col-std">join_dt</span></td><td><span class="col-type">varchar(8)</span></td><td></td><td></td><td><span class="col-desc">입단일</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">PROMISE</span></td><td><span class="col-std">signing_bonus_va</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">계약금</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">MONEY</span></td><td><span class="col-std">salary_va</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">연봉</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">CAREER</span></td><td><span class="col-std">career_nm</span></td><td><span class="col-type">varchar(70)</span></td><td></td><td></td><td><span class="col-desc">경력</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">11개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> &mdash; 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TEAM</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-ref">팀 식별자 - [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>T_ID</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-ref">팀 식별자 - [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>POS</code><span class="code-desc"> &mdash; 포지션 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>31,012</td></tr>
<tr><td>0</td><td>9,857</td></tr>
<tr><td>7</td><td>7,334</td></tr>
<tr><td>3</td><td>5,977</td></tr>
<tr><td>2</td><td>5,263</td></tr>
<tr><td>4</td><td>2,799</td></tr>
<tr><td>9</td><td>2,686</td></tr>
<tr><td>5</td><td>2,544</td></tr>
<tr><td>6</td><td>2,057</td></tr>
<tr><td>8</td><td>1,844</td></tr>
<tr><td></td><td>58</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>POSITION</code><span class="code-desc"> &mdash; 포지션명</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>Åõ</td><td>33,509</td></tr>
<tr><td>³»</td><td>17,058</td></tr>
<tr><td>¿Ü</td><td>15,340</td></tr>
<tr><td></td><td>9,166</td></tr>
<tr><td>ÄÚÄ¡</td><td>9,016</td></tr>
<tr><td>Æ÷</td><td>5,917</td></tr>
<tr><td>°¨µ¶</td><td>708</td></tr>
<tr><td>0</td><td>16</td></tr>
<tr><td>Áö</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>HITTYPE</code><span class="code-desc"> &mdash; 투타 유형</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>¿ìÅõ¿ìÅ¸</td><td>57,810</td></tr>
<tr><td>ÁÂÅõÁÂÅ¸</td><td>14,655</td></tr>
<tr><td></td><td>9,588</td></tr>
<tr><td>¿ìÅõÁÂÅ¸</td><td>5,421</td></tr>
<tr><td>¿ì¾ð¿ìÅ¸</td><td>2,132</td></tr>
<tr><td>¿ìÅõ¾çÅ¸</td><td>951</td></tr>
<tr><td>ÁÂÅõ¿ìÅ¸</td><td>165</td></tr>
<tr><td>¿ì¾ðÁÂÅ¸</td><td>121</td></tr>
<tr><td>ÁÂ¾ðÁÂÅ¸</td><td>83</td></tr>
<tr><td>¿ì¾ð¾çÅ¸</td><td>24</td></tr>
<tr><td>ÁÂÅõ¾çÅ¸</td><td>2</td></tr>
<tr><td>¿ìÅõ¿ìÆ¼</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>BIRTH</code><span class="code-desc"> &mdash; 생년월일</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HEIGHT</code><span class="code-desc"> &mdash; 키</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>WEIGHT</code><span class="code-desc"> &mdash; 몸무게</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INDATE</code><span class="code-desc"> &mdash; 입단일</span></summary>
<div class="code-ref">연속값 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GYEAR</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>PCODE</td><td>10005</td><td>10082</td><td>30003</td></tr>
<tr><td>NAME</td><td>Â÷¿µÈ­</td><td>È²ÅÂÈ¯</td><td>¼Õ»ó´ë</td></tr>
<tr><td>TEAM</td><td>ÇØÅÂ</td><td>OB</td><td>»ï¼º</td></tr>
<tr><td>T_ID</td><td>HT</td><td>OB</td><td>SS</td></tr>
<tr><td>POS</td><td>4</td><td>1</td><td>2</td></tr>
<tr><td>POSITION</td><td>³»</td><td>Åõ</td><td>Æ÷</td></tr>
<tr><td>BACKNUM</td><td>82</td><td></td><td>80</td></tr>
<tr><td>CNAME</td><td>(ó³ç´ü¤)</td><td>(üÜ÷Áüº)</td><td>(áÝßÓÓÞ)</td></tr>
<tr><td>HITTYPE</td><td>¿ìÅõ¿ìÅ¸</td><td>ÁÂÅõÁÂÅ¸</td><td>¿ìÅõ¿ìÅ¸</td></tr>
<tr><td>BIRTH</td><td>19570627</td><td>19520806</td><td>19541020</td></tr>
<tr><td>HEIGHT</td><td>178</td><td></td><td>178</td></tr>
<tr><td>WEIGHT</td><td>82</td><td></td><td>82</td></tr>
<tr><td>INDATE</td><td>198202</td><td>198202</td><td>198202</td></tr>
<tr><td>PROMISE</td><td></td><td></td><td></td></tr>
<tr><td>MONEY</td><td>3000¸¸¿ø</td><td></td><td></td></tr>
<tr><td>CAREER</td><td>¼­¸²ÃÊ-Àü³²Áß-±¤ÁÖÁ¦ÀÏ°í-µ¿½ÅÀü¹®´ë-ÇØÅÂ</td><td>ÇÑ¾ç´ë</td><td>°æºÏ°í-ÇÑ¾ç´ë-»ï¼º</td></tr>
</tbody></table>
</div>

</div>
