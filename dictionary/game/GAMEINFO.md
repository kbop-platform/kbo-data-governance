# GAMEINFO

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 23,579 |
| 컬럼 수 | 27 |
| PK | `GMKEY, GDAY` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 기록팀, 방송팀, 통계팀, 외부 API |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GMKEY` | char | 15 | NN | PK | 경기 고유키 (YYYYMMDDVVHH#, 유효 13자리; 현행 DB char(15), 표준 char(13) 전환 대상) | `game_id` |
| 2 | `GDAY` | char | 8 | NN | PK | 경기 일자 (YYYYMMDD) | `game_dt` |
| 3 | `DBHD` | char | 10 | NN |  | 더블헤더 번호 (0=일반, 1=1차, 2=2차) | `doubleheader_no` |
| 4 | `STADIUM` | nvarchar | 40 |  |  | 구장 | `stadium_nm` |
| 5 | `VTEAM` | nvarchar | 4 | NN |  | 원정팀 코드 | `away_team_cd` |
| 6 | `HTEAM` | nvarchar | 4 | NN |  | 홈팀 코드 | `home_team_cd` |
| 7 | `STTM` | char | 4 |  |  | 경기 시작 시각 (HHMM) | `start_tm` |
| 8 | `ENTM` | nvarchar | 8 |  |  | 경기 종료 시각 (HHMM) | `end_tm` |
| 9 | `DLTM` | nvarchar | 8 |  |  | 지연 시간 (분) | `delay_tm` |
| 10 | `GMTM` | nvarchar | 8 |  |  | 경기 소요 시간 (분) | `game_duration_tm` |
| 11 | `STAD` | nvarchar | 16 |  |  | 구장 코드 | `stadium_cd` |
| 12 | `UMPC` | nvarchar | 16 |  |  | 주심 이름 | `umpire_chief_nm` |
| 13 | `UMP1` | nvarchar | 16 |  |  | 1루심 이름 | `umpire_1b_nm` |
| 14 | `UMP2` | nvarchar | 16 |  |  | 2루심 이름 | `umpire_2b_nm` |
| 15 | `UMP3` | nvarchar | 16 |  |  | 3루심 이름 | `umpire_3b_nm` |
| 16 | `UMPL` | nvarchar | 16 |  |  | 좌측 외야심 이름 | `umpire_lf_nm` |
| 17 | `UMPR` | nvarchar | 16 |  |  | 우측 외야심 이름 | `umpire_rf_nm` |
| 18 | `SCOA` | nvarchar | 16 |  |  | 기록원 A 이름 | `scorer_a_nm` |
| 19 | `SCOB` | nvarchar | 16 |  |  | 기록원 B 이름 | `scorer_b_nm` |
| 20 | `TEMP` | nvarchar | 6 |  |  | 기온 (×10, 예: 270=27.0℃) | `temperature_va` |
| 21 | `MOIS` | nvarchar | 6 |  |  | 습도 (%) | `humidity_va` |
| 22 | `WEATH` | nvarchar | 4 |  |  | 날씨 코드 (F=맑음, C=흐림, R=비) | `weather_cd` |
| 23 | `WIND` | nvarchar | 6 |  |  | 풍향 (16방위) | `wind_dir_cd` |
| 24 | `WINS` | nvarchar | 10 |  |  | 풍속 (m/s) | `wind_speed_va` |
| 25 | `GWEEK` | varchar | 12 |  |  | 요일 (EUC-KR 인코딩) | `game_week_nm` |
| 26 | `CROWD` | int |  |  |  | 관중수 | `crowd_cn` |
| 27 | `CHAJUN` | char | 10 |  |  | 차전 (라운드 번호) | `round_no` |

## 코드값 / 고유값

> **EUC-KR 참고**: `GWEEK` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨 (예: `¸ñ`=목). nvarchar 전환은 마이그레이션 시 처리.


### `GDAY`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `DBHD`

| 값 | 건수 |
|-----|------|
| `0` | 22,076 |
| `1` | 754 |
| `2` | 749 |



### `VTEAM`

| 값 | 건수 |
|-----|------|
| `HT` | 2,819 |
| `SS` | 2,818 |
| `LG` | 2,818 |
| `LT` | 2,816 |
| `OB` | 2,816 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `HTEAM`

| 값 | 건수 |
|-----|------|
| `LT` | 2,819 |
| `OB` | 2,819 |
| `SS` | 2,816 |
| `LG` | 2,816 |
| `HT` | 2,816 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `STTM`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `ENTM`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `DLTM`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `GMTM`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `TEMP`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `MOIS`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `WEATH`

| 값 | 건수 |
|-----|------|
| `F` | 13,299 |
| `C` | 9,153 |
| `R` | 905 |
| `` | 137 |
| `CR` | 29 |

> 외 9건 — 전체 목록은 `raw/column-metadata.json` 참조



### `WIND`

| 값 | 건수 |
|-----|------|
| `W` | 3,604 |
| `SW` | 2,720 |
| `WNW` | 1,973 |
| `NW` | 1,851 |
| `WSW` | 1,648 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `WINS`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `CHAJUN`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `19820327SSLG0`, `19820328HDSS0`, `19820328HTLT0` |
| `GDAY` | `19820327`, `19820328`, `19820328` |
| `DBHD` | `0`, `0`, `0` |
| `STADIUM` | `한밭`, `수원`, `고척` |
| `VTEAM` | `OB`, `SK`, `SS` |
| `HTEAM` | `HH`, `KT`, `WO` |
| `STTM` | `1830`, `1829`, `1830` |
| `ENTM` | `2127`, `2145`, `2112` |
| `DLTM` | `0`, `0`, `0` |
| `GMTM` | `257`, `316`, `242` |
