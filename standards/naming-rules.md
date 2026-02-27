# 명명 규칙

> 최종수정: 2026-02-24 | 출처: analysis/naming-patterns.md, scripts/upgrade-dictionary.py
> 📋 문서 성격: 신규 시스템 표준(안)

## 1. 개요 및 적용 범위

KBO 신규 시스템의 모든 데이터 요소에 적용하는 명명 규칙을 정의한다.

**적용 대상** (RFP DAR-001):
- DB 컬럼 및 테이블
- REST API 필드
- Kafka 토픽 및 메시지 필드
- WebSocket 채널 및 메시지 필드

→ 참고: [약어 사전](../standards-dict/abbreviations.md) - 약어 정의 및 접미사 규칙
→ 참고: [도메인 사전](../standards-dict/domains.md) - 접미사별 데이터 타입 매핑
→ 참고: [ID 체계](./id-system.md) - ID 명명 및 GYEAR 이중 명명 (§2.5)

---

## 2. 4계층 명명 규칙 요약

| 계층 | 대상 | 컨벤션 | 예시 (경기ID) | 예시 (타율) |
|------|------|--------|-------------|-----------|
| DB | 테이블명 | UPPER_SNAKE_CASE | `GAME_INFO` | - |
| DB | 컬럼명 | lower_snake_case | `game_id` | `avg_rt` |
| API | URL 경로 | kebab-case | `/game-info/{gameId}` | - |
| API | 필드명 | camelCase | `gameId` | `avgRt` |
| Kafka | 토픽명 | dot.separated.lower | `kbo.game.play` | - |
| Kafka | 메시지 필드 | camelCase | `gameId` | `avgRt` |
| WebSocket | 채널 경로 | path/lower | `/ws/game/{gameId}` | - |
| WebSocket | 메시지 필드 | camelCase | `gameId` | `avgRt` |

---

## 3. DB 계층

### 3.1 테이블 명명

**규칙**: `UPPER_SNAKE_CASE`

| 원칙 | 설명 | 예시 |
|------|------|------|
| 단어 구분 | 언더스코어로 구분 | `GAME_INFO`, `BAT_TOTAL` |
| 접두사 유지 | 기존 도메인 접두사 보존 | `IE_LIVE_TEXT`, `KBO_SCHEDULE` |
| 약어 유지 | 야구 약어는 그대로 | `GAME_HR`, `GAME_MEMO` |

**레거시 → 표준 테이블명 예시**:

| 레거시 | 표준(안) | 변경 사유 |
|--------|---------|----------|
| `GAMEINFO` | `GAME_INFO` | 단어 구분 추가 |
| `GAMECONTAPP` | `GAME_CONT_APP` | 단어 구분 추가 (팀 논의 필요) |
| `BatTotal` | `BAT_TOTAL` | PascalCase → UPPER_SNAKE |
| `Hitter` | `HITTER` | PascalCase → UPPER |
| `Pitcher` | `PITCHER` | PascalCase → UPPER |
| `Score` | `SCORE` | PascalCase → UPPER |
| `TeamRank` | `TEAM_RANK` | PascalCase → UPPER_SNAKE |
| `PitTotal` | `PIT_TOTAL` | PascalCase → UPPER_SNAKE |
| `IE_LiveText` | `IE_LIVE_TEXT` | PascalCase → UPPER_SNAKE |
| `IE_BallCount` | `IE_BALL_COUNT` | PascalCase → UPPER_SNAKE |
| `person` | `PERSON` | lowercase → UPPER |
| `KBO_schedule` | `KBO_SCHEDULE` | 혼합 → UPPER |

> 기존 DB 테이블 물리 변경은 마이그레이션 단계에서 수행. 표준 문서는 **목표 상태**만 정의한다.

### 3.2 컬럼 명명

**규칙**: `lower_snake_case` + 접미사 필수

**구조**: `{의미어}_{접미사}`

접미사 목록: `_id`, `_nm`, `_cd`, `_sc`, `_cn`, `_rt`, `_if`, `_dt`, `_tm`, `_va`, `_no`

#### `_cd` vs `_sc` 구분 기준

| 접미사 | 용도 | 특징 | 예시 |
|--------|------|------|------|
| `_cd` | **참조 코드** - 마스터/코드 테이블의 고정 값 | 값이 드물게 변경됨, 별도 코드 테이블 관리 가능 | `team_cd`, `how_cd`, `place_cd`, `weather_cd`, `position_cd` |
| `_sc` | **상태/구분 코드** - 프로세스 상태나 이진/소수 구분 | 값 종류가 적고(2~5개), 프로세스 흐름에서 의미 가짐 | `top_bottom_sc`, `wls_sc`, `cancel_sc`, `game_sc`, `record_status_cd` |

> **간단 판별법**: "이 값이 마스터 테이블에 정의되는가?" → `_cd`. "프로세스 상태나 Y/N 구분인가?" → `_sc`.
> 경계가 모호한 경우 `_cd`를 기본으로 사용한다.

#### 접미사 생략 허용 케이스

| 케이스 | 조건 | 예시 |
|--------|------|------|
| 야구 기록 (경기 단위) | 국제 약어가 의미 충분 | `pa`, `ab`, `hit`, `hr`, `rbi`, `bb`, `so`, `sb`, `cs`, `sh`, `sf`, `err` |
| 야구 기록 (시즌 집계) | `_cn` 접미사 필수 | `pa_cn`, `ab_cn`, `hit_cn`, `hr_cn` |
| 비율/평균 | 항상 `_rt` 접미사 | `avg_rt`, `era_rt`, `obp_rt` |

**이유**: 경기 단위 테이블(Hitter, Pitcher)에서 `pa`, `ab` 등은 이미 명확한 국제 야구 약어이므로 `_cn`을 붙이면 오히려 가독성이 떨어진다. 시즌 집계(SEASON_PLAYER_*)에서는 다른 접미사 컬럼(`_rt`, `_if`)과 혼재하므로 `_cn`으로 통일한다.

**혼재 예시** - 경기 단위 테이블(Hitter)의 컬럼 패턴:

```
game_id       → _id 접미사 (식별자)
player_id     → _id 접미사 (식별자)
pa, ab, hit   → 접미사 없음 (국제 약어, 수량)
hr, rbi, bb   → 접미사 없음 (국제 약어, 수량)
avg_rt        → _rt 접미사 (비율 - 항상 필수)
obp_rt        → _rt 접미사 (비율 - 항상 필수)
```

> 하나의 테이블에서 접미사 있는 컬럼과 없는 컬럼이 혼재하는 것은 **정상**이다. 접미사 생략은 국제 야구 약어 수량 컬럼에만 허용되며, 비율(`_rt`), 식별자(`_id`), 날짜(`_dt`) 등은 항상 접미사를 유지한다.

#### GYEAR 이중 명명 (`season_id` vs `season_yr`)

레거시 `GYEAR`는 용도에 따라 표준명이 분기된다:

| 용도 | 표준명 | 예시 테이블 | 사유 |
|------|--------|-----------|------|
| PK/FK (엔티티 식별) | `season_id` | TEAM, SEASON_PLAYER_* | 시즌을 고유하게 식별하는 키 |
| 속성/필터 (조회 조건) | `season_yr` | BAT_TOTAL, PERSON, HITTER | 연도 속성으로 참조 |

> 물리 타입은 동일 (`smallint`). 의미적 역할만 다름.

### 3.3 레거시 → 표준 변환 5원칙

모든 레거시 컬럼의 표준명 변환은 아래 5원칙을 순서대로 적용한다.

| 순서 | 원칙 | 설명 | 예시 |
|------|------|------|------|
| 1 | **명시 매핑 우선** | STANDARD_MAP(462개)에 정의된 매핑을 최우선 적용 | `GMKEY` → `game_id` |
| 2 | **신세대 접미사 보존** | `_ID`, `_NM`, `_CD` 등 접미사가 있으면 소문자 변환만 | `TB_SC` → `top_bottom_sc` |
| 3 | **국제 약어 적용** | 레거시 UPPER_CASE 야구 약어를 소문자 국제 표준으로 | `AB` → `ab`, `ERA` → `era` |
| 4 | **KBO 비표준 교정** | KBO 고유 약어를 국제 표준으로 교체 | `KK` → `so`, `HP` → `hbp` |
| 5 | **이중 의미 분리** | 동일 약어가 다른 의미로 쓰이면 맥락별 구분 | `TB`(int) → `tb_cn`, `TB`(char) → `top_bottom_cd` |

> 권위 매핑: `scripts/upgrade-dictionary.py` STANDARD_MAP (462개)

**변환 예시** (원칙별 대표):

| 레거시 | 원칙 | 표준명(안) | 비고 |
|--------|------|-----------|------|
| `GMKEY` | 1 (명시) | `game_id` | |
| `PCODE` | 1 (명시) | `player_id` | |
| `TB_SC` | 2 (접미사) | `top_bottom_sc` | |
| `AB` | 3 (국제) | `ab` | |
| `KK` | 4 (비표준) | `so` | KK→SO |
| `HRA` | 4 (비표준) | `avg` | HRA→AVG |
| `TB` (int, 루타) | 5 (이중) | `tb_cn` | |
| `TB` (char, 팀구분) | 5 (이중) | `top_bottom_cd` | |

---

## 4. API 계층

### 4.1 URL 경로

**규칙**: kebab-case, 복수형 리소스

```
/api/v1/games/{gameId}
/api/v1/games/{gameId}/hitters
/api/v1/games/{gameId}/pitchers
/api/v1/players/{playerId}
/api/v1/seasons/{seasonId}/stats/hitters
/api/v1/teams/{teamId}
/api/v1/schedules
```

### 4.2 필드명

**규칙**: camelCase

변환: `snake_case` → `camelCase` (언더스코어 제거 + 다음 글자 대문자)

| DB (snake_case) | API (camelCase) |
|-----------------|-----------------|
| `game_id` | `gameId` |
| `player_id` | `playerId` |
| `avg_rt` | `avgRt` |
| `top_bottom_sc` | `topBottomSc` |
| `hr_distance_va` | `hrDistanceVa` |
| `home_team_cd` | `homeTeamCd` |

> **ID 케이싱**: `gameId` (O), `gameID` (X). `id`를 단어로 취급하여 camelCase 규칙을 일관 적용한다.

### 4.3 열거형 (Enum)

**규칙**: UPPER_SNAKE_CASE 문자열

```json
{
  "topBottomSc": "TOP",
  "wlsCd": "WIN",
  "weatherCd": "CLEAR"
}
```

### 4.4 Query Parameter

**규칙**: camelCase

```
GET /api/v1/games?seasonId=2025&teamId=HH&page=1&size=20
```

---

## 5. Kafka 계층

### 5.1 토픽명

**규칙**: `kbo.{도메인}.{이벤트}` (dot-separated lowercase)

| 토픽 | 용도 |
|------|------|
| `kbo.game.started` | 경기 시작 |
| `kbo.game.play` | 플레이 이벤트 (타석 결과) |
| `kbo.game.score` | 점수 변동 |
| `kbo.game.ended` | 경기 종료 |
| `kbo.game.cancelled` | 경기 취소 |
| `kbo.stats.hitter.updated` | 타자 통계 갱신 |
| `kbo.stats.pitcher.updated` | 투수 통계 갱신 |
| `kbo.schedule.changed` | 일정 변경 |
| `kbo.lineup.changed` | 라인업 변경 |

### 5.2 메시지 구조

- **Key**: `gameId` (경기별 파티셔닝)
- **Value**: JSON, camelCase 필드명 (API 계층과 동일)
- **스키마**: JSON Schema 또는 Avro (camelCase 필드명)

```json
{
  "gameId": "20250322HHKT0",
  "seasonId": 2025,
  "eventType": "PLAY_RESULT",
  "inningNo": 3,
  "topBottomSc": "TOP",
  "howCd": "HR",
  "batterId": 75847,
  "pitcherId": 67263,
  "timestamp": "2025-03-22T19:30:00+09:00"
}
```

---

## 6. WebSocket 계층

### 6.1 채널 경로

**규칙**: `/ws/{도메인}/{식별자}/{이벤트}`

| 채널 | 용도 |
|------|------|
| `/ws/game/{gameId}/live` | 실시간 경기 중계 |
| `/ws/game/{gameId}/score` | 실시간 스코어보드 |
| `/ws/schedule/today` | 오늘 경기 일정 |

### 6.2 메시지 구조

- JSON 포맷, camelCase 필드명 (API/Kafka와 동일)
- `eventType` 필드: UPPER_SNAKE_CASE 이벤트 유형

```json
{
  "eventType": "LIVE_TEXT",
  "gameId": "20250322HHKT0",
  "inningNo": 5,
  "topBottomSc": "BOTTOM",
  "liveText": "이정후 좌전 안타",
  "timestamp": "2025-03-22T20:15:30+09:00"
}
```

---

## 7. 계층 간 변환 규칙

```
DB (snake_case)
    │
    ├──→ API (camelCase)
    │        │
    │        ├──→ Kafka message (camelCase, 동일)
    │        │
    │        └──→ WebSocket message (camelCase, 동일)
    │
    └──→ Kafka topic (dot.separated)
```

### 자동 변환 함수

```python
# snake_case → camelCase
def to_camel(name: str) -> str:
    parts = name.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

# camelCase → snake_case
def to_snake(name: str) -> str:
    import re
    return re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', name).lower()
```

### 변환 시 주의사항

| 항목 | 규칙 | 예시 |
|------|------|------|
| 2글자 약어 (id, nm, cd) | 단어로 취급 (대문자화 안 함) | `game_id` → `gameId` (O), `gameID` (X) |
| 야구 약어 (hr, rbi) | 그대로 유지 | `hr` → `hr` (변환 없음) |
| 숫자 포함 | 숫자 앞뒤 언더스코어 유지 | `inn_1_score` → `inn1Score` |
| 연속 대문자 없음 | camelCase에서 연속 대문자 금지 | `opp_obp_rt` → `oppObpRt` (O), `oppOBPRt` (X) |

### 날짜/시간 직렬화 규칙 (API / Kafka / WebSocket 공통)

모든 비-DB 계층에서 날짜·시간 필드는 **ISO 8601** 형식을 사용한다.

| DB 도메인 | DB 저장 형식 | API/Kafka/WS 직렬화 | 예시 |
|-----------|-------------|---------------------|------|
| `_dt` (날짜) | `char(8)` YYYYMMDD | `"YYYY-MM-DD"` | `"2025-03-22"` |
| `_dt` (일시) | `datetime2` | `"YYYY-MM-DDTHH:mm:ss+09:00"` | `"2025-03-22T18:30:00+09:00"` |
| `_tm` (시각) | `char(4)` HHMM | `"HH:MM"` | `"18:30"` |
| `_tm` (시간량) | `int` (분) | 정수 (분 단위) | `257` |
| `timestamp` | - | `"YYYY-MM-DDTHH:mm:ss.SSS+09:00"` | `"2025-03-22T19:30:00.123+09:00"` |

> 타임존: KST (`+09:00`) 고정. UTC 변환은 클라이언트 책임.

---

## 8. Do / Don't 예시

| 계층 | Do | Don't | 사유 |
|------|-----|-------|------|
| DB 테이블 | `GAME_INFO` | `GAMEINFO`, `GameInfo` | UPPER_SNAKE 통일 |
| DB 테이블 | `BAT_TOTAL` | `BatTotal`, `BATTOTAL` | 단어 구분 명확 |
| DB 테이블 | `IE_LIVE_TEXT` | `IE_LiveText` | UPPER_SNAKE 통일 |
| DB 컬럼 | `game_id` | `GMKEY`, `G_ID` | 표준 식별자 |
| DB 컬럼 | `so` | `KK` | 국제 표준 (삼진) |
| DB 컬럼 | `avg_rt` | `HRA`, `HRA_RT` | 국제 표준 (타율) |
| DB 컬럼 | `top_bottom_cd` | `TB` (char) | 이중 의미 해소 |
| DB 컬럼 | `stadium_nm` | `STADIUM` | 접미사로 타입 명시 |
| API | `gameId` | `game_id`, `gameID` | camelCase 통일 |
| API | `avgRt` | `avg_rt`, `AVG_RT` | camelCase 통일 |
| Kafka | `kbo.game.play` | `KBO.Game.Play`, `kbo_game_play` | dot.lower 통일 |
| Kafka | `kbo.stats.hitter.updated` | `kbo.stats.HITTER.updated` | 소문자 통일 |

---

## 9. KBO 비표준 약어 주의사항

KBO 레거시 시스템(Sports2i)에서 국제 표준과 다르게 사용하는 약어. 표준명(안)은 국제 표준 기준으로 정의했다.

| KBO 레거시 | 국제 표준 | 표준명(안) | 한글 | 비고 |
|-----------|----------|-----------|------|------|
| `KK` | SO (Strikeout) | `so` | 삼진 | K/SO가 국제 표준 |
| `HP` | HBP (Hit by Pitch) | `hbp` | 사구 | |
| `IB` | IBB (Intentional BB) | `ibb` | 고의사구 | |
| `HRA` | AVG / BA | `avg` | 타율 | HRA는 KBO 고유. 국제적으로 HR Average와 혼동 |
| `GD` | GIDP | `gidp` | 병살타 | Grounded into Double Play |
| `ASS` | AST (Assist) | `ast` | 보살 | S2i 고유 약어 |
| `INN` | IP (Innings Pitched) | `ip` | 이닝 | IP가 국제 표준 |
| `WRA` | wRC (Weighted Runs Created) | `wrc` | 가중득점생산 | |
| `BRA` | BA (Batting Average) | `bat_avg` | 팀 타율 | 확인 필요 |
| `LRA` | - | `left_avg` | 좌타자 타율? | 의미 확인 필요 |

### 이중 의미 약어

| 약어 | 의미 1 | 의미 2 | 구분 방법 |
|------|--------|--------|----------|
| `TB` | Total Bases (루타, int) | Top/Bottom (팀구분, char) | 타입으로 구분: int=루타, char(1)=팀구분 |
| | 표준: `tb_cn` | 표준: `top_bottom_cd` / `top_bottom_sc` | |
| `R` | Runs Allowed (실점) | Runs Scored (득점) | 맥락으로 구분: 투수=실점, Score=실점행 |
| | 표준: `runs_cn` | | |
| `INN` | Innings Pitched (투구 이닝) | Inning Score (이닝별 점수) | INN 단독=투구, INN1~INN25=이닝 점수 |
| | 표준: `ip` | 표준: `inn_{N}_score` | |

→ 참고: [약어 사전](../standards-dict/abbreviations.md) - 전체 약어 목록 및 레거시 ↔ 표준 매핑
