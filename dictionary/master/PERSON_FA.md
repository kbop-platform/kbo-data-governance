---
title: PERSON_FA
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">마스터</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-access">Restricted</span>
  </div>
  <div class="dict-hero-title">PERSON_FA</div>
  <div class="dict-hero-sub">DB2_BASEBALL_NEW &middot; PK: </div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">228</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">4</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">FA 발생 시 수시</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_NEW_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code></code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 - Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">FA 발생 시 수시</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀, 인사팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Restricted</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[선수 프로필](../products/player-profile.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-note">
**관련 테이블**: [person](./person.md)의 보조 테이블. FA(자유계약) 선수의 연봉·옵션 관리.
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">4개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선수 코드 (5~6자리 숫자)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">MONEY</span></td><td><span class="col-std">salary_va</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">연봉</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">OPTION</span></td><td><span class="col-std">option_cd</span></td><td><span class="col-type">varchar(12)</span></td><td></td><td></td><td><span class="col-desc">FA 옵션</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">2개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>2023</td><td>81</td></tr>
<tr><td>2024</td><td>79</td></tr>
<tr><td>2025</td><td>68</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> &mdash; 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GYEAR</td><td>2025</td><td>2025</td><td>2025</td></tr>
<tr><td>PCODE</td><td>54640</td><td>77637</td><td>55633</td></tr>
<tr><td>MONEY</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>OPTION</td><td>170000´Þ·¯</td><td>80000¸¸¿ø</td><td>175000´Þ·¯</td></tr>
</tbody></table>
</div>

</div>
