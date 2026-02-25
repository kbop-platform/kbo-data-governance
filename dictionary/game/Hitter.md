---
title: Hitter
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-1">Tier 1</span>
    <span class="dict-badge badge-gen gen-legacy">구세대</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">Hitter</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: GMKEY, GDAY, PCODE</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">648,248</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">26</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY, PCODE</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">스키마 세대</span><span class="dict-info-value">legacy (구세대)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 1 — Critical</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀, 통계팀, 외부 API</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">26개</span></div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">TB</span></td><td><span class="col-std">top_bottom_cd</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 구분 (T=원정/Top, B=홈/Bottom)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">NAME</span></td><td><span class="col-std">player_nm</span></td><td><span class="col-type">nvarchar(15)</span></td><td></td><td></td><td><span class="col-desc">선수명 (varchar=EUC-KR 깨짐 가능)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">PCODE</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">varchar(10)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">선수 코드 (5~6자리 숫자 문자열)</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">TURN</span></td><td><span class="col-std">turn_no</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">타순</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">ONETURN</span></td><td><span class="col-std">one_turn_if</span></td><td><span class="col-type">char(1)</span></td><td></td><td></td><td><span class="col-desc">타순 (1~9)</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">PA</span></td><td><span class="col-std">pa</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 (Plate Appearance)</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">AB</span></td><td><span class="col-std">ab</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타수 (At Bat)</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">RBI</span></td><td><span class="col-std">rbi</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타점</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">RUN</span></td><td><span class="col-std">run</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">득점</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">HIT</span></td><td><span class="col-std">hit</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">안타</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">H2</span></td><td><span class="col-std">h2b</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">2루타</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">H3</span></td><td><span class="col-std">h3b</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">3루타</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">HR</span></td><td><span class="col-std">hr</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">홈런</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">SB</span></td><td><span class="col-std">sb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루</span></td></tr>
<tr><td class="col-num">17</td><td><span class="col-name">CS</span></td><td><span class="col-std">cs</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">도루실패</span></td></tr>
<tr><td class="col-num">18</td><td><span class="col-name">SH</span></td><td><span class="col-std">sh</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생번트</span></td></tr>
<tr><td class="col-num">19</td><td><span class="col-name">SF</span></td><td><span class="col-std">sf</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">희생플라이</span></td></tr>
<tr><td class="col-num">20</td><td><span class="col-name">BB</span></td><td><span class="col-std">bb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">볼넷</span></td></tr>
<tr><td class="col-num">21</td><td><span class="col-name">IB</span></td><td><span class="col-std">ibb</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">고의사구 (Intentional BB)</span></td></tr>
<tr><td class="col-num">22</td><td><span class="col-name">HP</span></td><td><span class="col-std">hbp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">사구 (Hit by Pitch)</span></td></tr>
<tr><td class="col-num">23</td><td><span class="col-name">KK</span></td><td><span class="col-std">so</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">삼진</span></td></tr>
<tr><td class="col-num">24</td><td><span class="col-name">GD</span></td><td><span class="col-std">gidp</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">병살타</span></td></tr>
<tr><td class="col-num">25</td><td><span class="col-name">ERR</span></td><td><span class="col-std">err</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">실책</span></td></tr>
<tr><td class="col-num">26</td><td><span class="col-name">LOB</span></td><td><span class="col-std">lob</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">잔루</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">5개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> — 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB</code><span class="code-desc"> — 팀 구분</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>T</td><td>324,226</td></tr>
<tr><td>B</td><td>324,022</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>PCODE</code><span class="code-desc"> — 선수 코드</span></summary>
<div class="code-ref">선수 식별자 — [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>TURN</code><span class="code-desc"> — 타순</span></summary>
<div class="code-ref">고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>ONETURN</code><span class="code-desc"> — 타순</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>8</td><td>77,112</td></tr>
<tr><td>9</td><td>75,520</td></tr>
<tr><td>7</td><td>69,259</td></tr>
<tr><td>6</td><td>66,550</td></tr>
<tr><td>2</td><td>65,620</td></tr>
<tr><td>5</td><td>64,738</td></tr>
<tr><td>4</td><td>61,844</td></tr>
<tr><td>3</td><td>60,350</td></tr>
<tr><td>1</td><td>60,097</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>19820327SSLG0</td><td>19820327SSLG0</td><td>19820327SSLG0</td></tr>
<tr><td>GDAY</td><td>19820327</td><td>19820327</td><td>19820327</td></tr>
<tr><td>TB</td><td>T</td><td>B</td><td>B</td></tr>
<tr><td>NAME</td><td>천보성</td><td>최정우</td><td>김인식</td></tr>
<tr><td>PCODE</td><td>40002</td><td>40003</td><td>40006</td></tr>
<tr><td>TURN</td><td>11</td><td>29</td><td>11</td></tr>
<tr><td>ONETURN</td><td>1</td><td>9</td><td>1</td></tr>
<tr><td>PA</td><td>5</td><td>1</td><td>6</td></tr>
<tr><td>AB</td><td>3</td><td>1</td><td>5</td></tr>
<tr><td>RBI</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>RUN</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>HIT</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td>H2</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>H3</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HR</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SB</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>CS</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>SH</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>SF</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>BB</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>IB</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>HP</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>KK</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>GD</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>ERR</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>LOB</td><td>0</td><td>0</td><td>0</td></tr>
</tbody></table>
</div>

</div>
