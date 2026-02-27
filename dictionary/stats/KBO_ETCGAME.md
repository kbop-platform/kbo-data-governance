---
title: KBO_ETCGAME
---

<div class="dict-detail-page" markdown>

<div class="dict-hero">
  <div class="dict-as-is-banner">현행 시스템(As-Is) 데이터 사전</div>
  <div class="dict-hero-badges">
    <span class="dict-badge badge-domain">통계</span>
    <span class="dict-badge badge-tier tier-3">Tier 3</span>
    <span class="dict-badge badge-access">Internal</span>
  </div>
  <div class="dict-hero-title">KBO_ETCGAME</div>
  <div class="dict-hero-sub">DB2_BASEBALL &middot; PK: GMKEY, GDAY, SEQ</div>
</div>

<div class="dict-quick-stats">
  <div class="dict-qs"><div class="dict-qs-val">122,762</div><div class="dict-qs-label">행 수</div></div>
  <div class="dict-qs"><div class="dict-qs-val">5</div><div class="dict-qs-label">컬럼</div></div>
  <div class="dict-qs"><div class="dict-qs-val">경기 당일</div><div class="dict-qs-label">갱신 주기</div></div>
  <div class="dict-qs"><div class="dict-qs-val">기록위원회</div><div class="dict-qs-label">오너</div></div>
</div>

<div class="dict-info-grid">
  <div class="dict-info-item"><span class="dict-info-label">대표 DB</span><span class="dict-info-value"><code>DB2_BASEBALL_220328</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">PK</span><span class="dict-info-value"><code>GMKEY, GDAY, SEQ</code></span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 티어</span><span class="dict-info-value">Tier 3 - Reference</span></div>
  <div class="dict-info-item"><span class="dict-info-label">데이터 오너</span><span class="dict-info-value">기록위원회 (R-03)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">갱신 주기</span><span class="dict-info-value">경기 당일 (S2i 전송)</span></div>
  <div class="dict-info-item"><span class="dict-info-label">소비자</span><span class="dict-info-value">기록팀</span></div>
  <div class="dict-info-item"><span class="dict-info-label">접근 수준</span><span class="dict-info-value">Internal</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">데이터 프로덕트</span><span class="dict-info-value">[시즌 통계](../products/season-stats.md)</span></div>
  <div class="dict-info-item full"><span class="dict-info-label">관련 표준</span><span class="dict-info-value">[도메인 타입](../../standards-dict/domains.md)</span></div>
</div>

<div class="dict-section-hdr"><h2>컬럼 상세</h2><span class="dict-section-count">5개</span></div>

<div class="dict-encoding-warn">`HOW`, `RESULT` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.</div>

<div style="overflow-x:auto">
<table class="dict-col-table"><thead>
<tr><th class="col-num">#</th><th>컬럼명</th><th>표준명(안)</th><th>타입</th><th>NULL</th><th>PK</th><th>설명</th></tr>
</thead><tbody>
<tr><td class="col-num">1</td><td><span class="col-name">GMKEY</span></td><td><span class="col-std">game_id</span></td><td><span class="col-type">char(13)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 고유키 (YYYYMMDDVVHH#)</span></td></tr>
<tr><td class="col-num">2</td><td><span class="col-name">GDAY</span></td><td><span class="col-std">game_dt</span></td><td><span class="col-type">char(8)</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">경기 일자 (YYYYMMDD)</span></td></tr>
<tr><td class="col-num">3</td><td><span class="col-name">SEQ</span></td><td><span class="col-std">seq_no</span></td><td><span class="col-type">tinyint</span></td><td><span class="nn-mark">NN</span></td><td><span class="pk-badge">PK</span></td><td><span class="col-desc">순번</span></td></tr>
<tr><td class="col-num">4</td><td><span class="col-name">HOW</span></td><td><span class="col-std">how_cd</span></td><td><span class="col-type">varchar(16)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">플레이 결과 코드 (H1=안타, H2=2루타, H3=3루타, HR=홈런, BB=볼넷, KK=삼진헛스윙, KN=삼진, GR=땅볼, FL=플라이, GD=병살타, SB=도루, HP=사구, SH=희생번트, SF=희생플라이, ER=실책 등 49종)</span></td></tr>
<tr><td class="col-num">5</td><td><span class="col-name">RESULT</span></td><td><span class="col-std">result_cd</span></td><td><span class="col-type">varchar(255)</span></td><td><span class="nn-mark">NN</span></td><td></td><td><span class="col-desc">결과 (KBO_ETCGAME: 선수명+회차 텍스트, EUC-KR / 기타 테이블: 결과 코드)</span></td></tr>
</tbody></table>
</div>

<div class="dict-section-hdr"><h2>코드값 / 고유값</h2><span class="dict-section-count">4개 컬럼</span></div>

<div class="dict-codes-section">
<details class="dict-code-group">
<summary><code>GDAY</code><span class="code-desc"> &mdash; 경기 일자</span></summary>
<div class="code-ref">고유값 20종 이상 - 상세 분포는 `raw/column-metadata.json` 참조</div>
</details>
<details class="dict-code-group">
<summary><code>SEQ</code><span class="code-desc"> &mdash; 순번</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>16</td><td>15,473</td></tr>
<tr><td>1</td><td>15,473</td></tr>
<tr><td>4</td><td>14,659</td></tr>
<tr><td>10</td><td>12,315</td></tr>
<tr><td>6</td><td>11,354</td></tr>
<tr><td>2</td><td>11,199</td></tr>
<tr><td>5</td><td>10,639</td></tr>
<tr><td>12</td><td>8,412</td></tr>
<tr><td>8</td><td>7,545</td></tr>
<tr><td>7</td><td>7,545</td></tr>
<tr><td>3</td><td>3,833</td></tr>
<tr><td>11</td><td>1,882</td></tr>
<tr><td>9</td><td>1,600</td></tr>
<tr><td>13</td><td>833</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>HOW</code><span class="code-desc"> &mdash; 플레이 결과 코드</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>½ÉÆÇ</td><td>15,473</td></tr>
<tr><td>°á½ÂÅ¸</td><td>15,473</td></tr>
<tr><td>2·çÅ¸</td><td>14,659</td></tr>
<tr><td>º´»ìÅ¸</td><td>12,315</td></tr>
<tr><td>µµ·ç</td><td>11,354</td></tr>
<tr><td>È¨·±</td><td>11,199</td></tr>
<tr><td>½ÇÃ¥</td><td>10,639</td></tr>
<tr><td>ÆøÅõ</td><td>8,412</td></tr>
<tr><td>ÁÖ·ç»ç</td><td>7,545</td></tr>
<tr><td>µµ·çÀÚ</td><td>7,545</td></tr>
<tr><td>3·çÅ¸</td><td>3,833</td></tr>
<tr><td>Æ÷ÀÏ</td><td>1,882</td></tr>
<tr><td>°ßÁ¦»ç</td><td>1,600</td></tr>
<tr><td>º¸Å©</td><td>833</td></tr>
</tbody></table>
</div>
</details>
<details class="dict-code-group">
<summary><code>RESULT</code><span class="code-desc"> &mdash; 결과</span></summary>
<div class="code-body">
<table class="dict-code-table"><thead><tr><th>값</th><th>건수</th></tr></thead><tbody>
<tr><td>¾øÀ½</td><td>2,207</td></tr>
<tr><td>±èÁÖÂù(1È¸)</td><td>72</td></tr>
<tr><td>ÀÌ´ëÇü(1È¸)</td><td>69</td></tr>
<tr><td>ÀÌ¿ë±Ô(1È¸)</td><td>67</td></tr>
<tr><td>¹ÚÇØ¹Î(1È¸)</td><td>62</td></tr>
<tr><td>Á¤±Ù¿ì(1È¸)</td><td>55</td></tr>
<tr><td>¹Ú¹Î¿ì(1È¸)</td><td>53</td></tr>
<tr><td>¿ÀÁöÈ¯(4È¸)</td><td>52</td></tr>
<tr><td>°­¹ÎÈ£(2È¸)</td><td>51</td></tr>
<tr><td>¹ÚÇÑÀÌ(1È¸)</td><td>50</td></tr>
<tr><td>¿ÀÁöÈ¯(6È¸)</td><td>46</td></tr>
<tr><td>¼Õ¾Æ¼·(1È¸)</td><td>46</td></tr>
<tr><td>±¸ÀÚ¿í(1È¸)</td><td>45</td></tr>
<tr><td>¹Ú¿ëÅÃ(1È¸)</td><td>45</td></tr>
<tr><td>ÀÌ¿ë±Ô(3È¸)</td><td>44</td></tr>
<tr><td>°­¹ÎÈ£(1È¸)</td><td>43</td></tr>
<tr><td>¹ÚÇØ¹Î(3È¸)</td><td>43</td></tr>
<tr><td>±è»ó¼ö(5È¸)</td><td>41</td></tr>
<tr><td>°­¹ÎÈ£(6È¸)</td><td>41</td></tr>
<tr><td>ÀÌ´ëÇü(3È¸)</td><td>40</td></tr>
</tbody></table>
</div>
</details>
</div>

<div class="dict-section-hdr"><h2>샘플 데이터</h2><span class="dict-section-count">상위 3건</span></div>

<div class="dict-sample-section">
<table class="dict-sample-table"><thead>
<tr><th>컬럼</th><th>값 1</th><th>값 2</th><th>값 3</th></tr>
</thead><tbody>
<tr><td>GMKEY</td><td>20010405HHSS0</td><td>20010405HHSS0</td><td>20010405HHSS0</td></tr>
<tr><td>GDAY</td><td>20010405</td><td>20010405</td><td>20010405</td></tr>
<tr><td>SEQ</td><td>1</td><td>3</td><td>4</td></tr>
<tr><td>HOW</td><td>°á½ÂÅ¸</td><td>3·çÅ¸</td><td>2·çÅ¸</td></tr>
<tr><td>RESULT</td><td>¾øÀ½</td><td>±è±âÅÂ(1È¸) ±è¼ö¿¬(6È¸)</td><td>µ¥ÀÌºñ½º(1È¸) ½ÉÀçÀ±(4È¸) ±èÁ¾¼®(9È¸)</td></tr>
</tbody></table>
</div>

</div>
