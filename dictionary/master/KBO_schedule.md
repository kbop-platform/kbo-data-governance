# KBO_schedule

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 27,340 |
| 컬럼 수 | 22 |
| PK | `gmkey, gamedate` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 경기운영팀 (R-05) |
| 갱신 주기 | 시즌 전 일괄 |
| 소비자 | 전 시스템 |
| 데이터 프로덕트 | [일정 관리](../products/schedule.md) |
| 접근 수준 | Public |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `gmkey` | char | 13 | NN | PK | 경기 고유키 | `game_id` |
| 2 | `game_flag` | char | 1 |  |  | 경기 유형 코드 (0~9, 불리언 아님) | `game_type_cd` |
| 3 | `end_flag` | char | 1 | NN |  | 종료 여부 (0/1) | `end_if` |
| 4 | `gamedate` | varchar | 8 | NN | PK | 경기 일자 | `game_dt` |
| 5 | `gyear` | char | 4 | NN |  | 연도 | `season_yr` |
| 6 | `gmonth` | char | 2 | NN |  | 경기 월 | `game_mon` |
| 7 | `gday` | char | 2 | NN |  | 경기 일 | `game_dt` |
| 8 | `gweek` | varchar | 2 | NN |  | 요일 | `game_week_nm` |
| 9 | `home` | varchar | 10 | NN |  | 홈팀명 | `home_team_cd` |
| 10 | `home_key` | char | 2 | NN |  | 홈팀 코드 | `home_team_id` |
| 11 | `visit` | varchar | 10 | NN |  | 원정팀명 | `away_team_cd` |
| 12 | `visit_key` | char | 2 | NN |  | 원정팀 코드 | `away_team_id` |
| 13 | `stadium` | varchar | 10 | NN |  | 구장 코드 | `stadium_nm` |
| 14 | `stadium_key` | char | 2 | NN |  | 구장 코드 | `stadium_id` |
| 15 | `dheader` | char | 1 | NN |  | 더블헤더 번호 | `doubleheader_no` |
| 16 | `hpcode` | char | 5 | NN |  | 홈팀 선발투수 코드 | `home_pitcher_id` |
| 17 | `vpcode` | char | 5 | NN |  | 원정팀 선발투수 코드 | `away_pitcher_id` |
| 18 | `gtime` | char | 5 | NN |  | 경기 시작 시각 | `game_tm` |
| 19 | `hscore` | tinyint |  | NN |  | 홈팀 점수 | `home_score` |
| 20 | `vscore` | tinyint |  | NN |  | 원정팀 점수 | `away_score` |
| 21 | `cancel_flag` | bit |  | NN |  | 취소 여부 (0/1) | `cancel_if` |
| 22 | `suspended_flag` | bit |  | NN |  | 서스펜디드 여부 (0/1) | `suspended_if` |

## 코드값 / 고유값

> **EUC-KR 참고**: `gweek`, `home`, `visit`, `stadium` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `game_flag`

| 값 | 건수 |
|-----|------|
| `0` | 25,313 |
| `1` | 1,376 |
| `7` | 240 |
| `5` | 186 |
| `3` | 121 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `end_flag`

| 값 | 건수 |
|-----|------|
| `1` | 25,372 |
| `0` | 1,968 |



### `gamedate`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `gyear`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `gmonth`

| 값 | 건수 |
|-----|------|
| `05` | 4,627 |
| `06` | 4,265 |
| `08` | 4,260 |
| `04` | 3,906 |
| `07` | 3,749 |

> 외 5건 — 전체 목록은 `raw/column-metadata.json` 참조



### `gday`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `gweek`

| 값 | 건수 |
|-----|------|
| `ÀÏ` | 4,709 |
| `Åä` | 4,706 |
| `¼ö` | 4,477 |
| `¸ñ` | 4,363 |
| `È­` | 4,246 |

> 외 3건 — 전체 목록은 `raw/column-metadata.json` 참조



### `home`

| 값 | 건수 |
|-----|------|
| `»ï¼º` | 3,270 |
| `·Ôµ¥` | 3,246 |
| `LG` | 2,741 |
| `ÇÑÈ­` | 2,557 |
| `µÎ»ê` | 2,178 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `home_key`

| 값 | 건수 |
|-----|------|
| `SS` | 3,270 |
| `LT` | 3,246 |
| `HT` | 3,245 |
| `OB` | 3,174 |
| `LG` | 3,160 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `visit`

| 값 | 건수 |
|-----|------|
| `»ï¼º` | 3,230 |
| `·Ôµ¥` | 3,148 |
| `LG` | 2,853 |
| `ÇÑÈ­` | 2,470 |
| `µÎ»ê` | 2,332 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `visit_key`

| 값 | 건수 |
|-----|------|
| `OB` | 3,326 |
| `LG` | 3,272 |
| `SS` | 3,230 |
| `HT` | 3,183 |
| `LT` | 3,148 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `stadium`

| 값 | 건수 |
|-----|------|
| `Àá½Ç` | 6,119 |
| `»çÁ÷` | 2,781 |
| `ÇÑ¹ç` | 2,655 |
| `½Ã¹Î` | 2,278 |
| `¹®ÇÐ` | 2,013 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `stadium_key`

| 값 | 건수 |
|-----|------|
| `JS` | 6,119 |
| `SJ` | 2,780 |
| `DJ` | 2,655 |
| `DG` | 2,278 |
| `MH` | 2,013 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `dheader`

| 값 | 건수 |
|-----|------|
| `0` | 25,817 |
| `1` | 771 |
| `2` | 752 |



### `hpcode`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `vpcode`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `gtime`

| 값 | 건수 |
|-----|------|
| `18:30` | 14,000 |
| `14:00` | 3,522 |
| `17:00` | 2,958 |
| `18:00` | 1,206 |
| `13:00` | 1,202 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `hscore`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `vscore`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `cancel_flag`

| 값 | 건수 |
|-----|------|
| `False` | 26,121 |
| `True` | 1,219 |



### `suspended_flag`

| 값 | 건수 |
|-----|------|
| `False` | 27,328 |
| `True` | 12 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gmkey` | `19820327SSLG0`, `19820328HDSS0`, `19820328HTLT0` |
| `game_flag` | `0`, `0`, `0` |
| `end_flag` | `1`, `1`, `1` |
| `gamedate` | `19820327`, `19820328`, `19820328` |
| `gyear` | `1982`, `1982`, `1982` |
| `gmonth` | `03`, `03`, `03` |
| `gday` | `27`, `28`, `28` |
| `gweek` | `Åä`, `ÀÏ`, `ÀÏ` |
| `home` | `MBC`, `»ï¼º`, `·Ôµ¥` |
| `home_key` | `LG`, `SS`, `LT` |
