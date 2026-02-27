---
title: GAME_MEMO_PITCHCLOCK
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">경기 기록</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">GAME_MEMO_PITCHCLOCK</div>
  <div class="dict-hero-sub">DB1_BASEBALL &middot; PK: LE_ID, SR_ID, G_ID, SEQ_NO</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">237</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">16</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB1_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>LE_ID, SR_ID, G_ID, SEQ_NO</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 - Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[경기 요약](../products/game-summary.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">16개</span></div>

<div class="dict-encoding-warn">`PIT_RESULT_SC` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">LE_ID</span></td><td><span class="col-std">league_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">리그 ID (1=1군)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">SR_ID</span></td><td><span class="col-std">series_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">시리즈 ID (0=정규시즌, 1=올스타전, 3=준플레이오프, 4=미확인, 5=플레이오프, 6=미확인, 7=한국시리즈, 8=와일드카드, 9=기타)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEASON_ID</span></td><td><span class="col-std">season_id</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">시즌 ID (연도)</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">G_ID</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 ID (YYYYMMDDVVHH# 형식)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">INN_NO</span></td><td><span class="col-std">inning_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">이닝 번호</span></td></tr>
<tr><td class="col-num">6</td><td><span class="col-name">BAT_ORDER_NO</span></td><td><span class="col-std">bat_order_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타순 번호</span></td></tr>
<tr><td class="col-num">7</td><td><span class="col-name">BAT_AROUND_NO</span></td><td><span class="col-std">bat_around_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 회전 번호</span></td></tr>
<tr><td class="col-num">8</td><td><span class="col-name">TB_SC</span></td><td><span class="col-std">top_bottom_sc</span></td><td><span class="col-type">char(1)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">팀 구분 코드 (T=원정, B=홈)</span></td></tr>
<tr><td class="col-num">9</td><td><span class="col-name">PA_PIT_NO</span></td><td><span class="col-std">pa_pitch_no</span></td><td><span class="col-type">smallint</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">타석 투구 번호</span></td></tr>
<tr><td class="col-num">10</td><td><span class="col-name">GAME_PIT_NO</span></td><td><span class="col-std">game_pitch_no</span></td><td><span class="col-type">smallint</span></td><td></td><td></td><td><span class="col-desc">경기 투구 번호</span></td></tr>
<tr><td class="col-num">11</td><td><span class="col-name">T_ID</span></td><td><span class="col-std">team_id</span></td><td><span class="col-type">char(2)</span></td><td></td><td></td><td><span class="col-desc">팀 코드 (2자리)</span></td></tr>
<tr><td class="col-num">12</td><td><span class="col-name">P_ID</span></td><td><span class="col-std">player_id</span></td><td><span class="col-type">int</span></td><td></td><td></td><td><span class="col-desc">선수 ID (정수)</span></td></tr>
<tr><td class="col-num">13</td><td><span class="col-name">PIT_RESULT_SC</span></td><td><span class="col-std">pit_result_sc</span></td><td><span class="col-type">varchar(20)</span></td><td></td><td></td><td><span class="col-desc">투구 결과 상태코드 (S=스트라이크, B=볼, F=파울, T=파울팁, H=타격 등)</span></td></tr>
<tr><td class="col-num">14</td><td><span class="col-name">ETC_ME</span></td><td><span class="col-std">etc_memo</span></td><td><span class="col-type">varchar(400)</span></td><td></td><td></td><td><span class="col-desc">기타 메모</span></td></tr>
<tr><td class="col-num">15</td><td><span class="col-name">SEQ_NO</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">int</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">순번</span></td></tr>
<tr><td class="col-num">16</td><td><span class="col-name">REG_DT</span></td><td><span class="col-std">reg_dt</span></td><td><span class="col-type">datetime</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">등록 일시</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">13개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group" open>
<summary><code>LE_ID</code><span class="code-desc"> &mdash; 리그 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>237</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SR_ID</code><span class="code-desc"> &mdash; 시리즈 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>215</td></tr>
<tr><td>1</td><td>17</td></tr>
<tr><td>8</td><td>3</td></tr>
<tr><td>5</td><td>1</td></tr>
<tr><td>3</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>SEASON_ID</code><span class="code-desc"> &mdash; 시즌 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>2025</td><td>237</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>G_ID</code><span class="code-desc"> &mdash; 경기 ID</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>20250328HTHH0</td><td>3</td></tr>
<tr><td>20250317LTWO0</td><td>2</td></tr>
<tr><td>20250310HHSK0</td><td>2</td></tr>
<tr><td>20250325LTSK0</td><td>2</td></tr>
<tr><td>20250323WOSS0</td><td>2</td></tr>
<tr><td>20250325WOHT0</td><td>2</td></tr>
<tr><td>20250327OBKT0</td><td>2</td></tr>
<tr><td>20250329HTHH0</td><td>2</td></tr>
<tr><td>20250330SSOB0</td><td>2</td></tr>
<tr><td>20250406OBLT0</td><td>2</td></tr>
<tr><td>20250411LTNC0</td><td>2</td></tr>
<tr><td>20250412WOHH0</td><td>2</td></tr>
<tr><td>20250417HHSK0</td><td>2</td></tr>
<tr><td>20250429SSSK0</td><td>2</td></tr>
<tr><td>20250430KTOB0</td><td>2</td></tr>
<tr><td>20250506HTWO0</td><td>2</td></tr>
<tr><td>20250510LGSS2</td><td>2</td></tr>
<tr><td>20250515LTHT0</td><td>2</td></tr>
<tr><td>20250518OBHT0</td><td>2</td></tr>
<tr><td>20250525NCOB0</td><td>2</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>INN_NO</code><span class="code-desc"> &mdash; 이닝 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>7</td><td>37</td></tr>
<tr><td>3</td><td>29</td></tr>
<tr><td>8</td><td>29</td></tr>
<tr><td>1</td><td>27</td></tr>
<tr><td>5</td><td>26</td></tr>
<tr><td>9</td><td>25</td></tr>
<tr><td>6</td><td>23</td></tr>
<tr><td>4</td><td>19</td></tr>
<tr><td>2</td><td>19</td></tr>
<tr><td>10</td><td>2</td></tr>
<tr><td>11</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>BAT_ORDER_NO</code><span class="code-desc"> &mdash; 타순 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>3</td><td>39</td></tr>
<tr><td>6</td><td>34</td></tr>
<tr><td>1</td><td>30</td></tr>
<tr><td>7</td><td>29</td></tr>
<tr><td>5</td><td>23</td></tr>
<tr><td>4</td><td>22</td></tr>
<tr><td>8</td><td>22</td></tr>
<tr><td>9</td><td>20</td></tr>
<tr><td>2</td><td>18</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>BAT_AROUND_NO</code><span class="code-desc"> &mdash; 타석 회전 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>0</td><td>237</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>TB_SC</code><span class="code-desc"> &mdash; 팀 구분 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>B</td><td>123</td></tr>
<tr><td>T</td><td>114</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group" open>
<summary><code>PA_PIT_NO</code><span class="code-desc"> &mdash; 타석 투구 번호</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>1</td><td>177</td></tr>
<tr><td>4</td><td>23</td></tr>
<tr><td>3</td><td>15</td></tr>
<tr><td>5</td><td>10</td></tr>
<tr><td>2</td><td>4</td></tr>
<tr><td>7</td><td>3</td></tr>
<tr><td>6</td><td>2</td></tr>
<tr><td>8</td><td>2</td></tr>
<tr><td>9</td><td>1</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>GAME_PIT_NO</code><span class="code-desc"> &mdash; 경기 투구 번호</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>T_ID</code><span class="code-desc"> &mdash; 팀 코드</span></summary>
<div class="code-ref">팀 식별자 - [팀 마스터(TEAM)](../master/TEAM.md) 참조</div>
</details>
<details class="dict-code-group">
<summary><code>P_ID</code><span class="code-desc"> &mdash; 선수 ID</span></summary>
<div class="code-ref">선수 식별자 - [선수 마스터(person)](../master/person.md) 참조</div>
</details>
<details class="dict-code-group" open>
<summary><code>PIT_RESULT_SC</code><span class="code-desc"> &mdash; 투구 결과 상태코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>C</td><td>170</td></tr>
<tr><td>P</td><td>66</td></tr>
<tr><td>Q</td><td>1</td></tr>
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
<tr><td>SEASON_ID</td><td>2025</td><td>2025</td><td>2025</td></tr>
<tr><td>G_ID</td><td>20250322HHKT0</td><td>20250323WOSS0</td><td>20250323WOSS0</td></tr>
<tr><td>INN_NO</td><td>3</td><td>1</td><td>7</td></tr>
<tr><td>BAT_ORDER_NO</td><td>6</td><td>1</td><td>8</td></tr>
<tr><td>BAT_AROUND_NO</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>TB_SC</td><td>B</td><td>B</td><td>B</td></tr>
<tr><td>PA_PIT_NO</td><td>1</td><td>3</td><td>4</td></tr>
<tr><td>GAME_PIT_NO</td><td>109</td><td>22</td><td>266</td></tr>
<tr><td>T_ID</td><td>HH</td><td>WO</td><td>WO</td></tr>
<tr><td>P_ID</td><td>55730</td><td>64350</td><td>66018</td></tr>
<tr><td>PIT_RESULT_SC</td><td>C</td><td>C</td><td>C</td></tr>
<tr><td>ETC_ME</td><td>3È¸¸» 6¹øÅ¸¼ø ÃÊ±¸ Àü ÇÇÄ¡Å¬¶ô Åõ¼öÀ§¹Ý : ÇÑÈ­ Æù¼¼</td><td>1È¸¸» 1¹øÅ¸¼ø 2±¸ ÈÄ ÇÇÄ¡Å¬¶ô Åõ¼öÀ§¹Ý : Å°¿ò ÇÏ¿µ¹Î</td><td>7È¸¸» 8¹øÅ¸¼ø 3±¸ ÈÄ ÇÇÄ¡Å¬¶ô Åõ¼öÀ§¹Ý : Å°¿ò ±è¼±±â</td></tr>
<tr><td>SEQ_NO</td><td>1430</td><td>270</td><td>3690</td></tr>
<tr><td>REG_DT</td><td>2025-09-12 17:17:04.833000</td><td>2025-09-12 17:17:04.833000</td><td>2025-09-12 17:17:04.833000</td></tr>
</tbody></table>
</div>

</div>
