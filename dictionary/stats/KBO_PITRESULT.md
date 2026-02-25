---
title: KBO_PITRESULT
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-2">Tier 2</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">KBO_PITRESULT</div>
  <div class="dict-hero-sub">DB2_BASEBALL &middot; PK: GMKEY, GDAY, PCODE</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">134,292</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">23</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY, PCODE</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 2 — Standard</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">분석팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[코드 사전](../../standards/code-dictionary.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">23개</span></div>

<div class="dict-encoding-warn">일부 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">TB</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 구분 (T=원정/Top, B=홈/Bottom)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">varchar(16)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">선수명 (varchar=EUC-KR 깨짐 가능)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자 문자열)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">POS</span></td><td><span class="col-std">position_cd</span></td><td><span class="col-type">char(2)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">포지션 코드</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">WLS</span></td><td><span class="col-std">wls_cd</span></td><td><span class="col-type">varchar(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">승패세 (W=승, L=패, S=세이브)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">CHANGEINN</span></td><td><span class="col-std"></span></td><td><span class="col-type">varchar(4)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">GAME</span></td><td><span class="col-std">game_cn</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">경기 수</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">W</span></td><td><span class="col-std">win_cn</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">승</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">L</span></td><td><span class="col-std">lose_cn</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">패</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">S</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">INN</span></td><td><span class="col-std">inn_no</span></td><td><span class="col-type">varchar(5)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝 번호</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">PA</span></td><td><span class="col-std">pa</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 (Plate Appearance)</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">BF</span></td><td><span class="col-std">bf</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">상대타자수</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">AB</span></td><td><span class="col-std">ab</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수 (At Bat)</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">BBHP</span></td><td><span class="col-std"></span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc"></span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">KK</span></td><td><span class="col-std">so</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">R</span></td><td><span class="col-std">r</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실점</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">ER</span></td><td><span class="col-std">er</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">자책점</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">ERA</span></td><td><span class="col-std">era</span></td><td><span class="col-type">varchar(6)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">평균자책점</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">21개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> — 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB</code><span class="code-desc"> — 팀 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>68,661</td></tr>
<tr><td>T</td><td>65,631</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>POS</code><span class="code-desc"> — 포지션 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>11</td><td>30,980</td></tr>
<tr><td>21</td><td>30,434</td></tr>
<tr><td>31</td><td>28,280</td></tr>
<tr><td>41</td><td>22,157</td></tr>
<tr><td>51</td><td>13,366</td></tr>
<tr><td>61</td><td>6,113</td></tr>
<tr><td>71</td><td>2,171</td></tr>
<tr><td>81</td><td>620</td></tr>
<tr><td>91</td><td>139</td></tr>
<tr><td>A1</td><td>26</td></tr>
<tr><td>B1</td><td>5</td></tr>
<tr><td>C1</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>WLS</code><span class="code-desc"> — 승패세</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td></td><td>84,075</td></tr>
<tr><td>L</td><td>15,165</td></tr>
<tr><td>W</td><td>15,165</td></tr>
<tr><td>H</td><td>11,903</td></tr>
<tr><td>S</td><td>7,334</td></tr>
<tr><td>D</td><td>650</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>CHANGEINN</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>GAME</code><span class="code-desc"> — 경기 수</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>W</code><span class="code-desc"> — 승</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>L</code><span class="code-desc"> — 패</span></summary>
<div class="code-ref">고유값 19종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>S</code><span class="code-desc"> — </span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>INN</code><span class="code-desc"> — 이닝 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>36,985</td></tr>
<tr><td>0 ¨÷</td><td>15,587</td></tr>
<tr><td>0 ¨ø</td><td>15,026</td></tr>
<tr><td>1 ¨÷</td><td>9,603</td></tr>
<tr><td>2</td><td>8,162</td></tr>
<tr><td>1 ¨ø</td><td>6,698</td></tr>
<tr><td>6</td><td>5,806</td></tr>
<tr><td>0</td><td>5,713</td></tr>
<tr><td>5</td><td>5,090</td></tr>
<tr><td>7</td><td>3,605</td></tr>
<tr><td>3</td><td>2,920</td></tr>
<tr><td>2 ¨÷</td><td>2,585</td></tr>
<tr><td>4</td><td>2,082</td></tr>
<tr><td>2 ¨ø</td><td>1,986</td></tr>
<tr><td>5 ¨÷</td><td>1,623</td></tr>
<tr><td>5 ¨ø</td><td>1,428</td></tr>
<tr><td>3 ¨÷</td><td>1,369</td></tr>
<tr><td>4 ¨÷</td><td>1,261</td></tr>
<tr><td>3 ¨ø</td><td>1,240</td></tr>
<tr><td>6 ¨÷</td><td>1,136</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PA</code><span class="code-desc"> — 타석</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>BF</code><span class="code-desc"> — 상대타자수</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>AB</code><span class="code-desc"> — 타수</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>HIT</code><span class="code-desc"> — 안타</span></summary>
<div class="code-ref">고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>HR</code><span class="code-desc"> — 홈런</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>111,742</td></tr>
<tr><td>1</td><td>18,543</td></tr>
<tr><td>2</td><td>3,361</td></tr>
<tr><td>3</td><td>559</td></tr>
<tr><td>4</td><td>78</td></tr>
<tr><td>5</td><td>9</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>BBHP</code><span class="code-desc"> — </span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>64,869</td></tr>
<tr><td>1</td><td>36,986</td></tr>
<tr><td>2</td><td>17,088</td></tr>
<tr><td>3</td><td>8,396</td></tr>
<tr><td>4</td><td>4,081</td></tr>
<tr><td>5</td><td>1,938</td></tr>
<tr><td>6</td><td>639</td></tr>
<tr><td>7</td><td>224</td></tr>
<tr><td>8</td><td>55</td></tr>
<tr><td>9</td><td>15</td></tr>
<tr><td>10</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>KK</code><span class="code-desc"> — 삼진</span></summary>
<div class="code-ref">고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>R</code><span class="code-desc"> — 실점</span></summary>
<div class="code-ref">고유값 15종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>ER</code><span class="code-desc"> — 자책점</span></summary>
<div class="code-ref">고유값 15종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>ERA</code><span class="code-desc"> — 평균자책점</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>20010405HHSS0</td><td>20010405HHSS0</td><td>20010405HHSS0</td></tr>
<tr><td>GDAY</td><td>20010405</td><td>20010405</td><td>20010405</td></tr>
<tr><td>TB</td><td>B</td><td>B</td><td>B</td></tr>
<tr><td>NAME</td><td>¹è¿µ¼ö</td><td>¸®º£¶ó</td><td>ÀÌ¼º¼ö</td></tr>
<tr><td>PCODE</td><td>70425</td><td>71414</td><td>71429</td></tr>
<tr><td>POS</td><td>41</td><td>61</td><td>31</td></tr>
<tr><td>WLS</td><td></td><td>S</td><td></td></tr>
<tr><td>CHANGEINN</td><td>8.4</td><td>9.9</td><td>7.2</td></tr>
<tr><td>GAME</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>W</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>L</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>S</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>INN</td><td>0 ¨ø</td><td>1</td><td>0 ¨÷</td></tr>
<tr><td>PA</td><td>4</td><td>4</td><td>2</td></tr>
<tr><td>BF</td><td>21</td><td>11</td><td>5</td></tr>
<tr><td>AB</td><td>2</td><td>4</td><td>2</td></tr>
<tr><td>HIT</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>HR</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BBHP</td><td>2</td><td>0</td><td>0</td></tr>
<tr><td>KK</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>R</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>ER</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>ERA</td><td>0.00</td><td>0.00</td><td>0.00</td></tr>
</tbody></table>
</div>

</div>
