# IE_BallCount

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 15,482 |
| 컬럼 수 | 11 |
| PK | `gameID, GYEAR` |
| 스키마 세대 | unknown |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | S2i 운영 (R-06) |
| 갱신 주기 | 실시간 (< 5초) |
| 소비자 | 방송팀, 앱 서비스 |
| 데이터 프로덕트 | [실시간 경기](../products/live-game.md) |
| 접근 수준 | Internal |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `gameID` | char | 13 | NN | PK | 경기 ID (GMKEY와 동일 형식) | `game_id` |
| 2 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 3 | `strike` | tinyint |  | NN |  | 스트라이크 카운트 | `strike_cn` |
| 4 | `ball` | tinyint |  | NN |  | 볼 카운트 | `ball_cn` |
| 5 | `out` | tinyint |  | NN |  | 아웃 카운트 | `out_cn` |
| 6 | `base1` | tinyint |  | NN |  | 1루 주자 여부 | `base_1b_id` |
| 7 | `base2` | tinyint |  | NN |  | 2루 주자 여부 | `base_2b_id` |
| 8 | `base3` | tinyint |  | NN |  | 3루 주자 여부 | `base_3b_id` |
| 9 | `pitcher` | varchar | 10 | NN |  | 투수 선수 코드 | `pitcher_id` |
| 10 | `batter` | varchar | 10 | NN |  | 타자 선수 코드 | `batter_id` |
| 11 | `batResult` | varchar | 50 | NN |  | 타격 결과 텍스트 | `bat_result_cd` |

## 코드값 / 고유값


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `strike`

| 값 | 건수 |
|-----|------|
| `0` | 5,621 |
| `3` | 3,883 |
| `2` | 3,207 |
| `1` | 2,771 |



### `ball`

| 값 | 건수 |
|-----|------|
| `0` | 6,701 |
| `1` | 4,272 |
| `2` | 2,996 |
| `3` | 1,513 |



### `out`

| 값 | 건수 |
|-----|------|
| `3` | 12,327 |
| `0` | 2,253 |
| `2` | 462 |
| `1` | 440 |



### `base1`

| 값 | 건수 |
|-----|------|
| `0` | 9,616 |
| `6` | 693 |
| `8` | 674 |
| `7` | 656 |
| `9` | 649 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



### `base2`

| 값 | 건수 |
|-----|------|
| `0` | 11,185 |
| `1` | 538 |
| `6` | 511 |
| `4` | 495 |
| `8` | 494 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `base3`

| 값 | 건수 |
|-----|------|
| `0` | 13,080 |
| `5` | 291 |
| `6` | 289 |
| `4` | 274 |
| `1` | 271 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `pitcher`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `batter`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gameID` | `20040310LTSS0`, `20040313HDHH0`, `20040313LGSS0` |
| `GYEAR` | `2004`, `2004`, `2004` |
| `strike` | `0`, `0`, `0` |
| `ball` | `0`, `0`, `0` |
| `out` | `1`, `0`, `0` |
| `base1` | `0`, `0`, `0` |
| `base2` | `0`, `0`, `0` |
| `base3` | `0`, `0`, `0` |
| `pitcher` | `94526`, `96720`, `93453` |
| `batter` | `94539`, `98742`, `93112` |
