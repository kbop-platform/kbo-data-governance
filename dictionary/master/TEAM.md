# TEAM

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_2_220328` |
| 행 수 | 401 |
| 컬럼 수 | 7 |
| PK | `SEASON_ID, T_ID` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 3 — Reference |
| 데이터 오너 | 데이터 관리자 (R-01) |
| 갱신 주기 | 연 1회 (시즌 전) |
| 소비자 | 전 시스템 |
| 데이터 프로덕트 | [기준 데이터](../products/master-codes.md) |
| 접근 수준 | Public |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 2 | `SEASON_ID` | smallint |  | NN | PK | 시즌 ID (연도) | `season_id` |
| 3 | `T_ID` | char | 2 | NN | PK | 팀 코드 (2자리) | `team_id` |
| 4 | `FIRST_NM` | varchar | 50 | NN |  | FIRST 명칭 | `first_nm` |
| 5 | `LAST_NM` | varchar | 50 |  |  | LAST 명칭 | `last_nm` |
| 6 | `FIRST_ENG_NM` | varchar | 50 |  |  | FIRST_ENG 명칭 | `first_eng_nm` |
| 7 | `LAST_ENG_NM` | varchar | 50 |  |  | LAST_ENG 명칭 | `last_eng_nm` |
| 8 | `GROUP_SC` | varchar | 10 |  |  | GROUP 상태코드 | `group_sc` |

## 코드값 / 고유값

> **EUC-KR 참고**: `GROUP_SC` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `SEASON_ID`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `T_ID`

| 값 | 건수 |
|-----|------|
| `SS` | 45 |
| `LT` | 45 |
| `LG` | 45 |
| `OB` | 45 |
| `HT` | 45 |

> 외 9건 — 전체 목록은 `raw/column-metadata.json` 참조



### `GROUP_SC`

| 값 | 건수 |
|-----|------|
| `ALLSTAR` | 28 |
| `MAGIC` | 8 |
| `DREAM` | 8 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `SEASON_ID` | `1982`, `1982`, `1982` |
| `T_ID` | `HD`, `HT`, `LG` |
| `FIRST_NM` | `»ï¹Ì`, `ÇØÅÂ`, `MBC` |
| `LAST_NM` | `½´ÆÛ½ºÅ¸Áî`, `Å¸ÀÌ°ÅÁî`, `Ã»·æ` |
| `FIRST_ENG_NM` | `LOTTE`, `SAMSUNG`, `LOTTE` |
| `LAST_ENG_NM` | `GIANTS`, `LIONS`, `GIANTS` |
| `GROUP_SC` | `DREAM`, `MAGIC`, `DREAM` |
