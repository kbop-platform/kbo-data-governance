---
title: PitTotal
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">PitTotal</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: PCODE, GYEAR, SEC</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">9,377</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">22</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">D+1</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">통계분석팀</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>PCODE, GYEAR, SEC</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 - Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">통계분석팀 (R-04)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">D+1 (전일 경기 반영)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [약어 사전](../../standards-dict/abbreviations.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">22개</span></div>

<div class="dict-encoding-warn">`Team` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨 (예: `·Ôµ¥`=롯데, `»ï¼º`=삼성). nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GYEAR</span></td><td><span class="col-std">season_yr</span></td><td><span class="col-type">char(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, &quot;9999&quot;=통산)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEC</span></td><td><span class="col-std">series_cd</span></td><td><span class="col-type">varchar(4)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시즌 연도 (4자리, 9999=통산)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">Team</span></td><td><span class="col-std">team_cd</span></td><td><span class="col-type">varchar(6)</span></td><td></td><td></td><td><span class="col-desc">팀 코드</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">ERA</span></td><td><span class="col-std">era</span></td><td><span class="col-type">float</span></td><td></td><td></td><td><span class="col-desc">평균자책점</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">GAMENUM</span></td><td><span class="col-std">game_cn</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 수</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">CG</span></td><td><span class="col-std">cg</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">완투</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">SHO</span></td><td><span class="col-std">sho</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">완봉</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">W</span></td><td><span class="col-std">win</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">승</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">L</span></td><td><span class="col-std">loss</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">패</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">SV</span></td><td><span class="col-std">sv</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">세이브</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">Hold</span></td><td><span class="col-std">hld</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홀드</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">BF</span></td><td><span class="col-std">bf</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">상대타자수</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">INN</span></td><td><span class="col-std">ip</span></td><td><span class="col-type">varchar(8)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">INN2</span></td><td><span class="col-std">inn_2_score</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2회 타격 결과 (HOW 코드, EUC-KR)</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">HP</span></td><td><span class="col-std">hbp</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">사구 (Hit by Pitch)</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">KK</span></td><td><span class="col-std">so</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">R</span></td><td><span class="col-std">runs_cn</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실점</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">ER</span></td><td><span class="col-std">er</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">자책점</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">21개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> &mdash; 선수 코드</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>GYEAR</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SEC</code><span class="code-desc"> &mdash; 시즌 연도</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Team</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>·Ôµ¥</td><td>897</td></tr>
<tr><td>»ï¼º</td><td>876</td></tr>
<tr><td>LG</td><td>857</td></tr>
<tr><td>ÇÑÈ­</td><td>760</td></tr>
<tr><td>µÎ»ê</td><td>643</td></tr>
<tr><td>±â¾Æ</td><td>628</td></tr>
<tr><td>1</td><td>549</td></tr>
<tr><td>SK</td><td>489</td></tr>
<tr><td>¿ì¸®</td><td>455</td></tr>
<tr><td>NC</td><td>341</td></tr>
<tr><td>KT</td><td>282</td></tr>
<tr><td>OB</td><td>259</td></tr>
<tr><td>ÇØÅÂ</td><td>249</td></tr>
<tr><td>Çö´ë</td><td>228</td></tr>
<tr><td>2</td><td>222</td></tr>
<tr><td>3</td><td>167</td></tr>
<tr><td>½Ö¹æ¿ï</td><td>167</td></tr>
<tr><td>4</td><td>147</td></tr>
<tr><td>ÅÂÆò¾ç</td><td>142</td></tr>
<tr><td>SSG</td><td>135</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>GAMENUM</code><span class="code-desc"> &mdash; 경기 수</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>CG</code><span class="code-desc"> &mdash; 완투</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SHO</code><span class="code-desc"> &mdash; 완봉</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>W</code><span class="code-desc"> &mdash; 승</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>L</code><span class="code-desc"> &mdash; 패</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SV</code><span class="code-desc"> &mdash; 세이브</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>Hold</code><span class="code-desc"> &mdash; 홀드</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BF</code><span class="code-desc"> &mdash; 상대타자수</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INN</code><span class="code-desc"> &mdash; 이닝</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>212</td></tr>
<tr><td>2</td><td>170</td></tr>
<tr><td>3</td><td>123</td></tr>
<tr><td>4</td><td>101</td></tr>
<tr><td>0 1/3</td><td>92</td></tr>
<tr><td>5</td><td>82</td></tr>
<tr><td>2 2/3</td><td>81</td></tr>
<tr><td>1 2/3</td><td>79</td></tr>
<tr><td>3 2/3</td><td>78</td></tr>
<tr><td>0 2/3</td><td>77</td></tr>
<tr><td>5 1/3</td><td>76</td></tr>
<tr><td>3 1/3</td><td>75</td></tr>
<tr><td>1 1/3</td><td>74</td></tr>
<tr><td>2 1/3</td><td>66</td></tr>
<tr><td>4 1/3</td><td>64</td></tr>
<tr><td>4 2/3</td><td>62</td></tr>
<tr><td>5 2/3</td><td>59</td></tr>
<tr><td>0</td><td>56</td></tr>
<tr><td>6 1/3</td><td>55</td></tr>
<tr><td>8 2/3</td><td>55</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN2</code><span class="code-desc"> &mdash; 2회 타격 결과</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HIT</code><span class="code-desc"> &mdash; 안타</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HR</code><span class="code-desc"> &mdash; 홈런</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BB</code><span class="code-desc"> &mdash; 볼넷</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HP</code><span class="code-desc"> &mdash; 사구</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>KK</code><span class="code-desc"> &mdash; 삼진</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>R</code><span class="code-desc"> &mdash; 실점</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>ER</code><span class="code-desc"> &mdash; 자책점</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>PCODE</td><td>10082</td><td>80620</td><td>82003</td></tr>
<tr><td>GYEAR</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>SEC</td><td>1982</td><td>1982</td><td>1982</td></tr>
<tr><td>Team</td><td>OB</td><td>»ï¼º</td><td>OB</td></tr>
<tr><td>ERA</td><td>3.86</td><td>2.47</td><td>3.39</td></tr>
<tr><td>GAMENUM</td><td>27</td><td>48</td><td>27</td></tr>
<tr><td>CG</td><td>2</td><td>8</td><td>6</td></tr>
<tr><td>SHO</td><td>0</td><td>2</td><td>1</td></tr>
<tr><td>W</td><td>6</td><td>15</td><td>7</td></tr>
<tr><td>L</td><td>5</td><td>11</td><td>6</td></tr>
<tr><td>SV</td><td>3</td><td>11</td><td>0</td></tr>
<tr><td>Hold</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BF</td><td>365</td><td>864</td><td>566</td></tr>
<tr><td>INN</td><td>86 1/3</td><td>222 1/3</td><td>138</td></tr>
<tr><td>INN2</td><td>259</td><td>667</td><td>414</td></tr>
<tr><td>HIT</td><td>76</td><td>189</td><td>139</td></tr>
<tr><td>HR</td><td>12</td><td>11</td><td>8</td></tr>
<tr><td>BB</td><td>37</td><td>34</td><td>31</td></tr>
<tr><td>HP</td><td>11</td><td>6</td><td>4</td></tr>
<tr><td>KK</td><td>42</td><td>99</td><td>65</td></tr>
<tr><td>R</td><td>43</td><td>78</td><td>64</td></tr>
<tr><td>ER</td><td>37</td><td>61</td><td>52</td></tr>
</tbody></table>
</div>

</div>
