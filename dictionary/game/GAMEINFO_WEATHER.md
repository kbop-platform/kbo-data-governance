# GAMEINFO_WEATHER

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_220328` |
| 행 수 | 1,680 |
| 컬럼 수 | 12 |
| PK | `code, tm` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 3 — Reference |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (기상청) |
| 소비자 | 방송팀 |
| 데이터 프로덕트 | [일정 관리](../products/schedule.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `code` | varchar | 10 | NN | PK | 관측 지점 코드 | `code_cd` |
| 2 | `area_wide` | nvarchar | 10 |  |  | 광역 지역명 | `area_wide_nm` |
| 3 | `area_city` | nvarchar | 10 |  |  | 시/군 지역명 | `area_city_nm` |
| 4 | `area_dong` | nvarchar | 10 |  |  | 동/읍/면 지역명 | `area_dong_nm` |
| 5 | `tm` | varchar | 10 | NN | PK | 관측 시각 | `team_cd` |
| 6 | `icon40` | nvarchar | 10 |  |  | 날씨 아이콘 코드 | `icon_40_cd` |
| 7 | `temp` | nvarchar | 10 |  |  | 기온 (℃) | `temperature_va` |
| 8 | `humi` | nvarchar | 10 |  |  | 습도 (%) | `humidity_va` |
| 9 | `rain` | nvarchar | 10 |  |  | 강수량 | `rain_if` |
| 10 | `snow` | nvarchar | 10 |  |  | 적설량 | `snow_if` |
| 11 | `wdirk` | nvarchar | 10 |  |  | 풍향 | `wind_dir_cd` |
| 12 | `wspeed` | nvarchar | 10 |  |  | 풍속 (m/s) | `wind_speed_va` |

## 코드값 / 고유값


### `code`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `area_wide`

| 값 | 건수 |
|-----|------|
| `경기도` | 280 |
| `경상북도` | 140 |
| `서울특별시` | 140 |
| `부산광역시` | 140 |
| `인천광역시` | 140 |

> 외 11건 — 전체 목록은 `raw/column-metadata.json` 참조



### `area_city`

| 값 | 건수 |
|-----|------|
| `이천시` | 140 |
| `김해시` | 70 |
| `구로구` | 70 |
| `동래구` | 70 |
| `고양시일산서구` | 70 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `area_dong`

| 값 | 건수 |
|-----|------|
| `-` | 210 |
| `부사동` | 70 |
| `임동` | 70 |
| `사직1동` | 70 |
| `백사면` | 70 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `tm`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `icon40`

| 값 | 건수 |
|-----|------|
| `04` | 422 |
| `03` | 384 |
| `01` | 308 |
| `02` | 248 |
| `10` | 192 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `temp`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `humi`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `rain`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `snow`

| 값 | 건수 |
|-----|------|
| `-` | 1,680 |



### `wdirk`

| 값 | 건수 |
|-----|------|
| `북동` | 170 |
| `서` | 147 |
| `서북서` | 142 |
| `동북동` | 137 |
| `서남서` | 131 |

> 외 11건 — 전체 목록은 `raw/column-metadata.json` 참조



### `wspeed`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `code` | `1038`, `1038`, `1038` |
| `area_wide` | `광주광역시`, `광주광역시`, `광주광역시` |
| `area_city` | `북구`, `북구`, `북구` |
| `area_dong` | `임동`, `임동`, `임동` |
| `tm` | `2025082209`, `2025082210`, `2025082212` |
| `icon40` | `02`, `02`, `03` |
| `temp` | `29.6`, `30.7`, `31.2` |
| `humi` | `74`, `67`, `64` |
| `rain` | `-`, `-`, `-` |
| `snow` | `-`, `-`, `-` |
