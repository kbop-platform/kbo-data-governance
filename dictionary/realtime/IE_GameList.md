# IE_GameList

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 15,908 |
| 컬럼 수 | 6 |
| PK | `gameID, GYEAR` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 3 — Reference |
| 데이터 오너 | S2i 운영 (R-06) |
| 갱신 주기 | 실시간 (< 5초) |
| 소비자 | 앱 서비스 |
| 데이터 프로덕트 | [실시간 경기](../products/live-game.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `gameID` | char | 13 | NN | PK | 경기 ID (GMKEY와 동일 형식) | `game_id` |
| 2 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `HomeName` | varchar | 8 | NN |  | 홈팀명 | `home_team_nm` |
| 4 | `HomeMascot` | varchar | 20 | NN |  | 홈팀 마스코트명 | `home_mascot_nm` |
| 5 | `VisitName` | varchar | 8 | NN |  | 원정팀명 | `away_team_nm` |
| 6 | `VisitMascot` | varchar | 20 | NN |  | 원정팀 마스코트명 | `away_mascot_nm` |

## 코드값 / 고유값

> **EUC-KR 참고**: `HomeName`, `VisitName` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HomeName`

| 값 | 건수 |
|-----|------|
| `»ï¼º` | 1,766 |
| `·Ôµ¥` | 1,761 |
| `ÇÑÈ­` | 1,751 |
| `µÎ»ê` | 1,716 |
| `LG` | 1,680 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `VisitName`

| 값 | 건수 |
|-----|------|
| `µÎ»ê` | 1,819 |
| `LG` | 1,791 |
| `»ï¼º` | 1,715 |
| `ÇÑÈ­` | 1,678 |
| `·Ôµ¥` | 1,662 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gameID` | `20040310LTSS0`, `20040313HDHH0`, `20040313LGSS0` |
| `GYEAR` | `2004`, `2004`, `2004` |
| `HomeName` | `»ï¼º`, `ÇÑÈ­`, `»ï¼º` |
| `HomeMascot` | `¶óÀÌ¿ÂÁî`, `ÀÌ±Û½º`, `¶óÀÌ¿ÂÁî` |
| `VisitName` | `·Ôµ¥`, `Çö´ë`, `LG` |
| `VisitMascot` | `ÀÚÀÌ¾ðÃ÷`, `À¯´ÏÄÜ½º`, `Æ®À©½º` |
