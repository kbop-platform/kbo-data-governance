# 데이터 사전 — 테이블 목록 조감도

> 최종수정: 2026-02-25 | KBO 데이터 표준 정의서 (RFP DAR-001)

## 1. 전체 현황 요약

| 항목 | 수치 |
|------|------|
| 데이터베이스 | 17개 (DB1 영구 4 + DB2 시즌 13) |
| 테이블 종류 | 39종 (인스턴스 252개) |
| 총 컬럼 수 | 787개 |
| 총 행 수 | ~25.7M |
| 스키마 세대 | 구세대(GMKEY/PCODE) 24종 + 신세대(G_ID/P_ID) 6종 + 미분류 9종 |

---

## 2. 데이터 흐름도

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

---

## 3. 도메인별 테이블 목록

### 3.1 경기 기록 (game/) — 12종

| # | 테이블명 | 표준명(안) | 컬럼 수 | 행 수 | PK | 세대 | 티어 | 오너 | 갱신 주기 | 설명 |
|---|----------|-----------|--------|-------|-----|------|------|------|----------|------|
| 1 | [GAMEINFO](game/GAMEINFO.md) | GAME_INFO | 27 | 23,579 | GMKEY, GDAY | legacy | Tier 1 | 기록위원회 | 경기 당일 | 경기 기본 정보 |
| 2 | [GAMEINFO_WEATHER](game/GAMEINFO_WEATHER.md) | GAME_INFO_WEATHER | 12 | 1,680 | code, tm | unknown | Tier 3 | 기록위원회 | 경기 당일 | 기상청 상세 날씨 |
| 3 | [GAMECONTAPP](game/GAMECONTAPP.md) | GAME_CONT_APP | 29 | 2,531,702 | GMKEY, GYEAR, SERNO | legacy | Tier 1 | 기록위원회 | 경기 당일 | 경기 이벤트 상세 |
| 4 | [ENTRY](game/ENTRY.md) | ENTRY | 11 | 854,280 | GMKEY, GDAY, TURN, PCODE, POSI | legacy | Tier 1 | 기록위원회 | 경기 당일 | 출전 엔트리 |
| 5 | [Hitter](game/Hitter.md) | HITTER | 26 | 648,248 | GMKEY, GDAY, PCODE | legacy | Tier 1 | 기록위원회 | 경기 당일 | 경기별 타자 기록 |
| 6 | [Pitcher](game/Pitcher.md) | PITCHER | 36 | 223,624 | GMKEY, GDAY, PCODE | legacy | Tier 1 | 기록위원회 | 경기 당일 | 경기별 투수 기록 |
| 7 | [Score](game/Score.md) | SCORE | 60 | 23,579 | GMKEY, GDAY | legacy | Tier 1 | 기록위원회 | 경기 당일 | 이닝별 스코어 |
| 8 | [DEFEN](game/DEFEN.md) | DEFEN | 12 | 846,736 | (없음) | legacy | Tier 2 | 기록위원회 | 경기 당일 | 수비 기록 |
| 9 | [GAME_HR](game/GAME_HR.md) | GAME_HR | 15 | 7,784 | LE_ID, SR_ID, G_ID, SEQ_NO | new | Tier 2 | 기록위원회 | 경기 당일 | 홈런 기록 상세 |
| 10 | [GAME_MEMO](game/GAME_MEMO.md) | GAME_MEMO | 20 | 54,544 | LE_ID, SR_ID, G_ID, INN_NO, ... | new | Tier 2 | 기록위원회 | 경기 당일 | 투구 단위 기록 메모 |
| 11 | [GAME_MEMO_PITCHCLOCK](game/GAME_MEMO_PITCHCLOCK.md) | GAME_MEMO_PITCHCLOCK | 16 | 237 | LE_ID, SR_ID, G_ID, SEQ_NO | new | Tier 3 | 기록위원회 | 경기 당일 | 피치클럭 위반 기록 |
| 12 | [PITCHCLOCK](game/PITCHCLOCK.md) | PITCHCLOCK | 19 | 215 | GMKEY, GYEAR, GDAY, LIVETEXT | legacy | Tier 3 | 기록위원회 | 경기 당일 | 피치클럭 이벤트 |

### 3.2 통계 (stats/) — 10종

| # | 테이블명 | 표준명(안) | 컬럼 수 | 행 수 | PK | 세대 | 티어 | 오너 | 갱신 주기 | 설명 |
|---|----------|-----------|--------|-------|-----|------|------|------|----------|------|
| 1 | [BatTotal](stats/BatTotal.md) | BAT_TOTAL | 23 | 13,616 | PCODE, GYEAR, SEC | legacy | Tier 2 | 통계분석팀 | D+1 | 타격 시즌/통산 합산 |
| 2 | [PitTotal](stats/PitTotal.md) | PIT_TOTAL | 22 | 9,377 | PCODE, GYEAR, SEC | legacy | Tier 2 | 통계분석팀 | D+1 | 투구 시즌/통산 합산 |
| 3 | [TeamRank](stats/TeamRank.md) | TEAM_RANK | 30 | 373 | GYEAR, SEC, TEAM | unknown | Tier 2 | 통계분석팀 | D+1 | 팀 순위 (시즌별) |
| 4 | [KBO_BATRESULT](stats/KBO_BATRESULT.md) | KBO_BAT_RESULT | 90 | 424,921 | GMKEY, GDAY, PCODE | legacy | Tier 2 | 기록위원회 | 경기 당일 | 이닝별 타격 결과 |
| 5 | [KBO_PITRESULT](stats/KBO_PITRESULT.md) | KBO_PIT_RESULT | 23 | 134,292 | GMKEY, GDAY, PCODE | legacy | Tier 2 | 기록위원회 | 경기 당일 | 투수 경기 결과 상세 |
| 6 | [KBO_ETCGAME](stats/KBO_ETCGAME.md) | KBO_ETC_GAME | 5 | 122,762 | GMKEY, GDAY, SEQ | legacy | Tier 3 | 기록위원회 | 경기 당일 | 기타 경기 이벤트 |
| 7 | [SEASON_PLAYER_HITTER](stats/SEASON_PLAYER_HITTER.md) | SEASON_PLAYER_HITTER | 43 | 19,747 | SEASON_ID, P_ID, SECTION_CD, GROUP_IF | new | Tier 2 | 통계분석팀 | D+1 | 시즌별 타자 통계 |
| 8 | [SEASON_PLAYER_HITTER_SITUATION](stats/SEASON_PLAYER_HITTER_SITUATION.md) | SEASON_PLAYER_HITTER_SITUATION | 14 | 360,625 | SEASON_ID, P_ID, SECTION_CD, SITUATION_IF | new | Tier 2 | 통계분석팀 | D+1 | 시즌 타자 상황별 통계 |
| 9 | [SEASON_PLAYER_PITCHER](stats/SEASON_PLAYER_PITCHER.md) | SEASON_PLAYER_PITCHER | 54 | 13,306 | SEASON_ID, P_ID, SECTION_CD, GROUP_IF | new | Tier 2 | 통계분석팀 | D+1 | 시즌별 투수 통계 |
| 10 | [SEASON_PLAYER_PITCHER_SITUATION](stats/SEASON_PLAYER_PITCHER_SITUATION.md) | SEASON_PLAYER_PITCHER_SITUATION | 14 | 301,375 | SEASON_ID, P_ID, SECTION_CD, SITUATION_IF | new | Tier 2 | 통계분석팀 | D+1 | 시즌 투수 상황별 통계 |

### 3.3 실시간 (realtime/) — 9종

| # | 테이블명 | 표준명(안) | 컬럼 수 | 행 수 | PK | 세대 | 티어 | 오너 | 갱신 주기 | 설명 |
|---|----------|-----------|--------|-------|-----|------|------|------|----------|------|
| 1 | [IE_LiveText](realtime/IE_LiveText.md) | IE_LIVE_TEXT | 7 | 8,005,079 | gameID, GYEAR, SeqNO | unknown | Tier 1 | S2i 운영 | 실시간 | 실시간 문자 중계 |
| 2 | [IE_BallCount](realtime/IE_BallCount.md) | IE_BALL_COUNT | 11 | 15,482 | gameID, GYEAR | unknown | Tier 1 | S2i 운영 | 실시간 | 현재 볼카운트 상태 |
| 3 | [IE_BatterRecord](realtime/IE_BatterRecord.md) | IE_BATTER_RECORD | 25 | 451,166 | gameID, GYEAR, BatOrder, PlayerID, SeqNO | unknown | Tier 2 | S2i 운영 | 실시간 | 타자 실시간 기록 |
| 4 | [IE_PitcherRecord](realtime/IE_PitcherRecord.md) | IE_PITCHER_RECORD | 22 | 134,388 | gameID, GYEAR, PlayerID | unknown | Tier 2 | S2i 운영 | 실시간 | 투수 실시간 기록 |
| 5 | [IE_GameList](realtime/IE_GameList.md) | IE_GAME_LIST | 6 | 15,908 | gameID, GYEAR | unknown | Tier 3 | S2i 운영 | 실시간 | 경기 목록 (일자별) |
| 6 | [IE_GAMESTATE](realtime/IE_GAMESTATE.md) | IE_GAME_STATE | 5 | 15,237 | GAMEID, GYEAR | unknown | Tier 1 | S2i 운영 | 실시간 | 경기 진행 상태 |
| 7 | [IE_ScoreRHEB](realtime/IE_ScoreRHEB.md) | IE_SCORE_RHEB | 7 | 30,860 | gameID, GYEAR, bHome | unknown | Tier 1 | S2i 운영 | 실시간 | 점수/안타/실책/볼넷 요약 |
| 8 | [IE_Scoreinning](realtime/IE_Scoreinning.md) | IE_SCORE_INNING | 5 | 267,166 | gameID, GYEAR, inning, bHome | unknown | Tier 1 | S2i 운영 | 실시간 | 이닝별 실시간 점수 |
| 9 | [IE_log](realtime/IE_log.md) | IE_LOG | 3 | 785,406 | (없음) | unknown | Tier 3 | S2i 운영 | 실시간 | 시스템 로그 |

### 3.4 마스터 (master/) — 8종

| # | 테이블명 | 표준명(안) | 컬럼 수 | 행 수 | PK | 세대 | 티어 | 오너 | 갱신 주기 | 설명 |
|---|----------|-----------|--------|-------|-----|------|------|------|----------|------|
| 1 | [person](master/person.md) | PERSON | 20 | 100,812 | GYEAR, PCODE | legacy | Tier 1 | 기록위원회 | 시즌 전 | 선수 마스터 |
| 2 | [person2](master/person2.md) | PERSON2 | 17 | 91,891 | GYEAR, PCODE, NAME | legacy | Tier 3 | 기록위원회 | 시즌 전 | 선수 마스터 2 |
| 3 | [PERSON](master/PERSON.md) | PERSON | 16 | 13,902 | GYEAR, PCODE | legacy | Tier 3 | 기록위원회 | 시즌 전 | 선수 마스터 (마이너) |
| 4 | [PERSON_FA](master/PERSON_FA.md) | PERSON_FA | 4 | 228 | (없음) | legacy | Tier 3 | 기록위원회 | FA 발생 시 | FA 선수 정보 |
| 5 | [TEAM](master/TEAM.md) | TEAM | 7 | 401 | SEASON_ID, T_ID | unknown | Tier 3 | 데이터 관리자 | 연 1회 | 팀 마스터 |
| 6 | [STADIUM](master/STADIUM.md) | STADIUM | 3 | 487 | gyear, stadium | unknown | Tier 3 | 데이터 관리자 | 연 1회 | 구장 마스터 |
| 7 | [KBO_schedule](master/KBO_schedule.md) | KBO_SCHEDULE | 22 | 27,340 | gmkey, gamedate | legacy | Tier 2 | 경기운영팀 | 시즌 전 | 경기 일정 |
| 8 | [CANCEL_GAME](master/CANCEL_GAME.md) | CANCEL_GAME | 6 | 1,290 | LE_ID, SR_ID, G_ID | new | Tier 2 | 경기운영팀 | 발생 즉시 | 취소/우천중단 경기 |

---

## 4. 테이블 간 주요 관계

### 4.1 핵심 FK 관계

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

### 4.2 실시간 테이블 관계

실시간(IE_*) 테이블은 독립적으로 운영되며, `gameID`(=game_id)로 경기 기록 도메인과 연결된다.

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

---

## 5. 스키마 세대 분포

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

---

## 6. 참고 문서

- [데이터 프로덕트](products/game-summary.md) — 비즈니스 단위별 데이터 구조
- [데이터 리니지](lineage.md) — 데이터 흐름 추적, 영향도 분석
- [표준 명명 규칙](../standards/naming-rules.md) — 레거시→표준 변환 규칙
- [ID 체계](../standards/id-system.md) — game_id, player_id 등 6종 ID 정의
- [도메인 타입](../standards/domain-types.md) — 접미사별 MSSQL 타입 매핑
- [코드 사전](../standards/code-dictionary.md) — how_cd, place_cd 등 코드값
- [업무 용어 사전](../glossary/business-terms.md) — 용어 정의 ~165개
- [컬럼 매핑](../migration/column-mapping.md) — AS-IS→TO-BE 컬럼 전수 매핑
