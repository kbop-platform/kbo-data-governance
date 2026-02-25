# KBO_PITRESULT

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_220328` |
| 행 수 | 134,292 |
| 컬럼 수 | 23 |
| PK | `GMKEY, GDAY, PCODE` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 분석팀 |
| 데이터 프로덕트 | [시즌 통계](../products/season-stats.md) |
| 접근 수준 | Internal |
| 관련 표준 | [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GMKEY` | char | 13 | NN | PK | 경기 고유키 (YYYYMMDDVVHH#, 13자리) | `game_id` |
| 2 | `GDAY` | char | 8 | NN | PK | 경기 일자 (YYYYMMDD) | `game_dt` |
| 3 | `TB` | char | 1 | NN |  | 팀 구분 (T=원정/Top, B=홈/Bottom) | `top_bottom_cd` |
| 4 | `NAME` | varchar | 16 | NN |  | 선수명 (varchar=EUC-KR 깨짐 가능) | `player_nm` |
| 5 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 6 | `POS` | char | 2 | NN |  | 등판 순서 (S=선발, R=구원) | `position_cd` |
| 7 | `WLS` | varchar | 1 | NN |  | 승패세 (W=승, L=패, S=세이브) | `wls_cd` |
| 8 | `CHANGEINN` | varchar | 4 | NN |  | 교체 이닝 | `change_inn_no` |
| 9 | `GAME` | tinyint |  | NN |  | 경기 수 | `game_cn` |
| 10 | `W` | tinyint |  | NN |  | 승 | `win` |
| 11 | `L` | tinyint |  | NN |  | 패 | `loss` |
| 12 | `S` | tinyint |  | NN |  | 피안타 | `hits_cn` |
| 13 | `INN` | varchar | 5 | NN |  | 이닝 번호 | `ip` |
| 14 | `PA` | tinyint |  | NN |  | 타석 (Plate Appearance) | `pa` |
| 15 | `BF` | tinyint |  | NN |  | 상대타자수 | `bf` |
| 16 | `AB` | tinyint |  | NN |  | 타수 (At Bat) | `ab` |
| 17 | `HIT` | tinyint |  | NN |  | 안타 | `hit` |
| 18 | `HR` | tinyint |  | NN |  | 홈런 | `hr` |
| 19 | `BBHP` | tinyint |  | NN |  | 볼넷+사구 합계 | `bb_hbp` |
| 20 | `KK` | tinyint |  | NN |  | 삼진 | `so` |
| 21 | `R` | tinyint |  | NN |  | 실점 | `runs_cn` |
| 22 | `ER` | tinyint |  | NN |  | 자책점 | `er` |
| 23 | `ERA` | varchar | 6 | NN |  | 평균자책점 | `era` |

## 코드값 / 고유값

> **EUC-KR 참고**: 일부 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `GDAY`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TB`

| 값 | 건수 |
|-----|------|
| `B` | 68,661 |
| `T` | 65,631 |



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `POS`

| 값 | 건수 |
|-----|------|
| `11` | 30,980 |
| `21` | 30,434 |
| `31` | 28,280 |
| `41` | 22,157 |
| `51` | 13,366 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `WLS`

| 값 | 건수 |
|-----|------|
| `` | 84,075 |
| `L` | 15,165 |
| `W` | 15,165 |
| `H` | 11,903 |
| `S` | 7,334 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `CHANGEINN`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `GAME`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `W`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `L`

→ 고유값 19종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `S`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `INN`

| 값 | 건수 |
|-----|------|
| `1` | 36,985 |
| `0 ¨÷` | 15,587 |
| `0 ¨ø` | 15,026 |
| `1 ¨÷` | 9,603 |
| `2` | 8,162 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `PA`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `BF`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `AB`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HIT`

→ 고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `HR`

| 값 | 건수 |
|-----|------|
| `0` | 111,742 |
| `1` | 18,543 |
| `2` | 3,361 |
| `3` | 559 |
| `4` | 78 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BBHP`

| 값 | 건수 |
|-----|------|
| `0` | 64,869 |
| `1` | 36,986 |
| `2` | 17,088 |
| `3` | 8,396 |
| `4` | 4,081 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `KK`

→ 고유값 18종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `R`

→ 고유값 15종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `ER`

→ 고유값 15종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `ERA`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `20010405HHSS0`, `20010405HHSS0`, `20010405HHSS0` |
| `GDAY` | `20010405`, `20010405`, `20010405` |
| `TB` | `B`, `B`, `B` |
| `NAME` | `¹è¿µ¼ö`, `¸®º£¶ó`, `ÀÌ¼º¼ö` |
| `PCODE` | `70425`, `71414`, `71429` |
| `POS` | `41`, `61`, `31` |
| `WLS` | ``, `S`, `` |
| `CHANGEINN` | `8.4`, `9.9`, `7.2` |
| `GAME` | `1`, `1`, `1` |
| `W` | `0`, `0`, `0` |
