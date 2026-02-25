---
title: GAMEINFO_WEATHER
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-gen gen-unknown">미분류</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">GAMEINFO_WEATHER</div>
  <div class="dict-hero-sub">DB2_BASEBALL &middot; PK: code, tm</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">1,680</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">12</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>code, tm</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">unknown (미분류)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 — Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (기상청)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">방송팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[일정 관리](../products/schedule.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards/domain-types.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">12개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">code</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">area_wide</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">area_city</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">area_dong</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">tm</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">icon40</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">temp</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">humi</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">rain</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">snow</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">wdirk</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">wspeed</span></td><td><span class="col-std"></span></td><td><span class="col-type">nvarchar(10)</span></td><td></td><td></td><td><span class="col-desc"></span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">12개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>code</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>area_wide</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>경기도</td><td>280</td></tr>
<tr><td>경상북도</td><td>140</td></tr>
<tr><td>서울특별시</td><td>140</td></tr>
<tr><td>부산광역시</td><td>140</td></tr>
<tr><td>인천광역시</td><td>140</td></tr>
<tr><td>경상남도</td><td>140</td></tr>
<tr><td>울산광역시</td><td>70</td></tr>
<tr><td>광주광역시</td><td>70</td></tr>
<tr><td>대전광역시</td><td>70</td></tr>
<tr><td>충청남도</td><td>70</td></tr>
<tr><td>전라남도</td><td>70</td></tr>
<tr><td>강원특별자치도</td><td>70</td></tr>
<tr><td>전라북도</td><td>70</td></tr>
<tr><td>경삭북도</td><td>70</td></tr>
<tr><td>대구광역시</td><td>70</td></tr>
<tr><td>충청북도</td><td>70</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>area_city</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>이천시</td><td>140</td></tr>
<tr><td>김해시</td><td>70</td></tr>
<tr><td>구로구</td><td>70</td></tr>
<tr><td>동래구</td><td>70</td></tr>
<tr><td>고양시일산서구</td><td>70</td></tr>
<tr><td>중구</td><td>70</td></tr>
<tr><td>수원시장안구</td><td>70</td></tr>
<tr><td>강화군</td><td>70</td></tr>
<tr><td>송파구</td><td>70</td></tr>
<tr><td>수성구</td><td>70</td></tr>
<tr><td>북구</td><td>70</td></tr>
<tr><td>익산시</td><td>70</td></tr>
<tr><td>문경시</td><td>70</td></tr>
<tr><td>기장군</td><td>70</td></tr>
<tr><td>남구</td><td>70</td></tr>
<tr><td>함평군</td><td>70</td></tr>
<tr><td>미추홀구</td><td>70</td></tr>
<tr><td>포항시남구</td><td>70</td></tr>
<tr><td>춘천시</td><td>70</td></tr>
<tr><td>서산시</td><td>70</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>area_dong</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-</td><td>210</td></tr>
<tr><td>부사동</td><td>70</td></tr>
<tr><td>임동</td><td>70</td></tr>
<tr><td>사직1동</td><td>70</td></tr>
<tr><td>백사면</td><td>70</td></tr>
<tr><td>옥동</td><td>70</td></tr>
<tr><td>학교면</td><td>70</td></tr>
<tr><td>성연면</td><td>70</td></tr>
<tr><td>대화동</td><td>70</td></tr>
<tr><td>고척1동</td><td>70</td></tr>
<tr><td>일광면</td><td>70</td></tr>
<tr><td>상동면</td><td>70</td></tr>
<tr><td>문학동</td><td>70</td></tr>
<tr><td>양덕2동</td><td>70</td></tr>
<tr><td>영순면</td><td>70</td></tr>
<tr><td>대월면</td><td>70</td></tr>
<tr><td>조원1동</td><td>70</td></tr>
<tr><td>강남동</td><td>70</td></tr>
<tr><td>길상면</td><td>70</td></tr>
<tr><td>잠실2동</td><td>70</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>tm</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>icon40</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>04</td><td>422</td></tr>
<tr><td>03</td><td>384</td></tr>
<tr><td>01</td><td>308</td></tr>
<tr><td>02</td><td>248</td></tr>
<tr><td>10</td><td>192</td></tr>
<tr><td>15</td><td>98</td></tr>
<tr><td>39</td><td>13</td></tr>
<tr><td>40</td><td>12</td></tr>
<tr><td>07</td><td>3</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>temp</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>humi</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>rain</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>snow</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>-</td><td>1,680</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>wdirk</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>북동</td><td>170</td></tr>
<tr><td>서</td><td>147</td></tr>
<tr><td>서북서</td><td>142</td></tr>
<tr><td>동북동</td><td>137</td></tr>
<tr><td>서남서</td><td>131</td></tr>
<tr><td>동</td><td>123</td></tr>
<tr><td>남서</td><td>112</td></tr>
<tr><td>북서</td><td>112</td></tr>
<tr><td>동남동</td><td>105</td></tr>
<tr><td>남남서</td><td>98</td></tr>
<tr><td>남동</td><td>90</td></tr>
<tr><td>북북동</td><td>79</td></tr>
<tr><td>북북서</td><td>76</td></tr>
<tr><td>남남동</td><td>70</td></tr>
<tr><td>남</td><td>50</td></tr>
<tr><td>북</td><td>38</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>wspeed</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>code</td><td>1038</td><td>1038</td><td>1038</td></tr>
<tr><td>area_wide</td><td>광주광역시</td><td>광주광역시</td><td>광주광역시</td></tr>
<tr><td>area_city</td><td>북구</td><td>북구</td><td>북구</td></tr>
<tr><td>area_dong</td><td>임동</td><td>임동</td><td>임동</td></tr>
<tr><td>tm</td><td>2025082209</td><td>2025082210</td><td>2025082212</td></tr>
<tr><td>icon40</td><td>02</td><td>02</td><td>03</td></tr>
<tr><td>temp</td><td>29.6</td><td>30.7</td><td>31.2</td></tr>
<tr><td>humi</td><td>74</td><td>67</td><td>64</td></tr>
<tr><td>rain</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>snow</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wdirk</td><td>북</td><td>서북서</td><td>남</td></tr>
<tr><td>wspeed</td><td>1.1</td><td>0.6</td><td>1.4</td></tr>
</tbody></table>
</div>

</div>
