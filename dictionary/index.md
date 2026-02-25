---
hide:
  - toc
---

<style>
.dict-landing { max-width: 1100px; margin: 0 auto; }
.dict-landing-header {
  text-align: center;
  padding: 32px 16px 24px;
}
.dict-landing-header h1 {
  font-size: 1.6rem;
  font-weight: 800;
  margin: 0 0 8px;
}
.dict-landing-header p {
  color: #777;
  font-size: 0.92rem;
  margin: 0;
}
[data-md-color-scheme="slate"] .dict-landing-header p { color: #aaa; }

/* 통계 바 */
.dict-landing-stats {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-bottom: 28px;
  flex-wrap: wrap;
}
.dict-landing-stat {
  text-align: center;
}
.dict-landing-stat .num {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--kbo-accent, #4A7BF7);
}
.dict-landing-stat .label {
  font-size: 0.75rem;
  color: #999;
  margin-top: 2px;
}

/* 도메인 카드 그리드 */
.domain-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-bottom: 28px;
}
@media (max-width: 720px) {
  .domain-cards { grid-template-columns: 1fr; }
}
.domain-card {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 20px 24px;
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.2s;
  display: block;
  background: #fff;
}
[data-md-color-scheme="slate"] .domain-card {
  border-color: #333;
  background: #1e1e1e;
}
.domain-card:hover {
  border-color: var(--kbo-accent, #4A7BF7);
  box-shadow: 0 4px 16px rgba(74, 123, 247, 0.12);
  transform: translateY(-2px);
}
.domain-card-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}
.domain-card-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}
.dc-game { background: #e8f0fe; color: #1a73e8; }
.dc-stats { background: #fce8e6; color: #d93025; }
.dc-realtime { background: #e6f4ea; color: #188038; }
.dc-master { background: #fef7e0; color: #e37400; }
[data-md-color-scheme="slate"] .dc-game { background: #1a3052; }
[data-md-color-scheme="slate"] .dc-stats { background: #3c1a1a; }
[data-md-color-scheme="slate"] .dc-realtime { background: #1a3424; }
[data-md-color-scheme="slate"] .dc-master { background: #3c2e0a; }

.domain-card-title {
  font-size: 1.05rem;
  font-weight: 700;
}
.domain-card-meta {
  font-size: 0.75rem;
  color: #999;
}
.domain-card-desc {
  font-size: 0.82rem;
  color: #666;
  margin-bottom: 12px;
  line-height: 1.5;
}
[data-md-color-scheme="slate"] .domain-card-desc { color: #aaa; }

.domain-card-tables {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}
.domain-card-tables code {
  font-size: 0.7rem;
  padding: 2px 7px;
  border-radius: 4px;
  background: #f3f4f6;
  color: #555;
  font-family: 'JetBrains Mono', monospace;
}
[data-md-color-scheme="slate"] .domain-card-tables code {
  background: #2a2a2a;
  color: #bbb;
}
</style>

<div class="dict-landing" markdown>

<div class="dict-landing-header">
  <h1>데이터 사전</h1>
  <p>KBO 운영 데이터베이스 39개 테이블 · 787개 컬럼 정의서</p>
</div>

<div class="dict-landing-stats">
  <div class="dict-landing-stat">
    <div class="num">39</div>
    <div class="label">테이블</div>
  </div>
  <div class="dict-landing-stat">
    <div class="num">787</div>
    <div class="label">컬럼</div>
  </div>
  <div class="dict-landing-stat">
    <div class="num">25.7M</div>
    <div class="label">총 행수</div>
  </div>
  <div class="dict-landing-stat">
    <div class="num">4</div>
    <div class="label">도메인</div>
  </div>
</div>

<div class="domain-cards">
  <a class="domain-card" href="game/GAMEINFO/">
    <div class="domain-card-head">
      <div class="domain-card-icon dc-game">&#9918;</div>
      <div>
        <div class="domain-card-title">경기 기록</div>
        <div class="domain-card-meta">12 테이블 · 284 컬럼 · Tier 1~2</div>
      </div>
    </div>
    <div class="domain-card-desc">경기 정보, 타자/투수 기록, 스코어, 수비, 엔트리, 홈런, 투구 메모 등 경기 당일 생성되는 핵심 기록 테이블</div>
    <div class="domain-card-tables">
      <code>GAMEINFO</code>
      <code>Hitter</code>
      <code>Pitcher</code>
      <code>Score</code>
      <code>ENTRY</code>
      <code>DEFEN</code>
      <code>GAMECONTAPP</code>
      <code>GAME_HR</code>
      <code>GAME_MEMO</code>
      <code>+3</code>
    </div>
  </a>

  <a class="domain-card" href="stats/BatTotal/">
    <div class="domain-card-head">
      <div class="domain-card-icon dc-stats">&#128202;</div>
      <div>
        <div class="domain-card-title">통계</div>
        <div class="domain-card-meta">10 테이블 · 318 컬럼 · Tier 1~2</div>
      </div>
    </div>
    <div class="domain-card-desc">타격·투구 합산, 팀 순위, 이닝별 타격, 시즌 타자/투수 통계 및 상황별 세분화 데이터</div>
    <div class="domain-card-tables">
      <code>BatTotal</code>
      <code>PitTotal</code>
      <code>TeamRank</code>
      <code>KBO_BATRESULT</code>
      <code>KBO_PITRESULT</code>
      <code>SEASON_PLAYER_HITTER</code>
      <code>+4</code>
    </div>
  </a>

  <a class="domain-card" href="realtime/IE_LiveText/">
    <div class="domain-card-head">
      <div class="domain-card-icon dc-realtime">&#9889;</div>
      <div>
        <div class="domain-card-title">실시간</div>
        <div class="domain-card-meta">9 테이블 · 96 컬럼 · IE_ 접두사</div>
      </div>
    </div>
    <div class="domain-card-desc">문자 중계, 볼카운트, 타자/투수 실시간 기록, 경기 목록·상태, 점수 요약/이닝, 시스템 로그</div>
    <div class="domain-card-tables">
      <code>IE_LiveText</code>
      <code>IE_BallCount</code>
      <code>IE_BatterRecord</code>
      <code>IE_PitcherRecord</code>
      <code>IE_GameList</code>
      <code>IE_GAMESTATE</code>
      <code>+3</code>
    </div>
  </a>

  <a class="domain-card" href="master/person/">
    <div class="domain-card-head">
      <div class="domain-card-icon dc-master">&#128100;</div>
      <div>
        <div class="domain-card-title">마스터</div>
        <div class="domain-card-meta">8 테이블 · 95 컬럼 · 참조 데이터</div>
      </div>
    </div>
    <div class="domain-card-desc">선수, 팀, 구장, 경기 일정, 취소 경기, FA 선수 등 다른 도메인에서 참조하는 기준 데이터</div>
    <div class="domain-card-tables">
      <code>person</code>
      <code>person2</code>
      <code>PERSON</code>
      <code>PERSON_FA</code>
      <code>TEAM</code>
      <code>STADIUM</code>
      <code>KBO_schedule</code>
      <code>CANCEL_GAME</code>
    </div>
  </a>
</div>

---

<details class="dict-reference" markdown>
<summary>데이터 흐름도</summary>

```
┌─────────────────┐     경기 당일 전송      ┌──────────────────┐
│  S2i 운영 DB     │ ──────────────────────→ │  DB2 (시즌 13개)  │
│  (Sports2i 외주) │                         │  시즌별 경기 데이터 │
└─────────────────┘                         └────────┬─────────┘
                                                     │ 확정 후 반영
                                                     ▼
                                             ┌──────────────────┐
                                             │  DB1 (영구 4개)    │
                                             │  누적/마스터 데이터 │
                                             └──────────────────┘

┌─────────────────┐     KBO 자체 구축       ┌──────────────────┐
│  KBO 분석팀      │ ──────────────────────→ │  KBO 자체 DB      │
│  (내부)          │                         │  세이버/P-b-P 등   │
└─────────────────┘                         └──────────────────┘
```

- **DB2**: 경기 당일 S2i가 전송. 시즌 데이터
- **DB1**: DB2 확정 후 반영. 영구/누적
- **KBO 자체**: 세이버메트릭스, pitch-by-pitch 등 S2i 미제공 데이터

</details>

<details class="dict-reference" markdown>
<summary>테이블 간 주요 관계</summary>

**핵심 FK 관계**

```
GAME_INFO (game_id)
  ├── HITTER         (game_id, season_yr, player_id)
  ├── PITCHER         (game_id, season_yr, player_id)
  ├── SCORE           (game_id, season_yr, top_bottom_cd)
  ├── GAME_CONT_APP   (game_id, season_yr, seq_no)
  ├── ENTRY           (game_id, season_yr, turn_no, player_id, position_cd)
  ├── DEFEN           (game_id, season_yr)
  ├── GAME_HR         (game_id)
  └── GAME_MEMO       (game_id)

PERSON (player_id)
  ├── HITTER         (player_id)
  ├── PITCHER         (player_id)
  ├── ENTRY           (player_id)
  ├── BAT_TOTAL       (player_id)
  └── PIT_TOTAL       (player_id)

TEAM (team_id, season_id)
  ├── TEAM_RANK       (team_cd, season_yr)
  └── GAME_INFO       (home_team_cd, away_team_cd)
```

**실시간 테이블 관계**

실시간(IE_*) 테이블은 독립적으로 운영되며, `gameID`(=game_id)로 경기 기록 도메인과 연결.

```
IE_LIVE_TEXT (gameID) ← 실시간 문자 중계
IE_BALL_COUNT (gameID) ← 볼카운트 현재 상태
IE_BATTER_RECORD (gameID, PlayerID) ← 타자 누적
IE_PITCHER_RECORD (gameID, PlayerID) ← 투수 누적
IE_GAME_STATE (GAMEID) ← 경기 상태
IE_SCORE_RHEB (gameID) ← R/H/E/B 요약
IE_SCORE_INNING (gameID) ← 이닝 점수
IE_GAME_LIST (gameID) ← 당일 경기 목록
IE_LOG ← 시스템 로그 (FK 없음)
```

</details>

<details class="dict-reference" markdown>
<summary>스키마 세대 분포</summary>

| 세대 | 식별 패턴 | 테이블 수 | 주요 특징 |
|------|----------|----------|----------|
| **구세대 (legacy)** | GMKEY/PCODE, camelCase·PascalCase 혼용 | 24종 | 1982년~ 축적 데이터. `varchar` 한글, `float` 비율 |
| **신세대 (new)** | G_ID/P_ID, `_CD`·`_CN`·`_SC` 접미사 | 6종 | 2022년~ 추가. `nvarchar`, 정수 ID |
| **미분류 (unknown)** | 양쪽 패턴 혼합 또는 판별 불가 | 9종 | IE_* 실시간 등. S2i 확인 필요 |

**구세대 → 신세대 전환 우선순위**:

1. GAME_INFO, HITTER, PITCHER — 핵심 경기 기록 (가장 많이 조회)
2. BAT_TOTAL, PIT_TOTAL — 통계 조회 빈도 높음
3. ENTRY, DEFEN, SCORE — 경기 부속 기록
4. IE_* — 실시간 테이블은 API/WebSocket 전환 시 함께

</details>

<details class="dict-reference" markdown>
<summary>참고 문서</summary>

- [데이터 프로덕트](products/game-summary.md) — 비즈니스 단위별 데이터 구조
- [데이터 리니지](lineage.md) — 데이터 흐름 추적, 영향도 분석
- [표준 명명 규칙](../standards/naming-rules.md) — 레거시→표준 변환 규칙
- [ID 체계](../standards/id-system.md) — game_id, player_id 등 6종 ID 정의
- [도메인 타입](../standards/domain-types.md) — 접미사별 MSSQL 타입 매핑
- [코드 사전](../standards/code-dictionary.md) — how_cd, place_cd 등 코드값
- [업무 용어 사전](../glossary/business-terms.md) — 용어 정의 ~165개
- [컬럼 매핑](../migration/column-mapping.md) — AS-IS→TO-BE 컬럼 전수 매핑

</details>

</div>
