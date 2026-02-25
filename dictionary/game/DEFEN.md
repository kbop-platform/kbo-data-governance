# DEFEN

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 846,736 |
| 컬럼 수 | 12 |
| PK | `` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 2 — Standard |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 기록팀 |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [약어 사전](../../standards/abbreviations.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GMKEY` | char | 13 | NN |  | 경기 고유키 (YYYYMMDDVVHH#, 13자리) | `game_id` |
| 2 | `GDAY` | int |  | NN |  | 경기 일자 (YYYYMMDD) | `game_dt` |
| 3 | `TB` | char | 1 |  |  | 팀 구분 (T=원정/Top, B=홈/Bottom) | `top_bottom_cd` |
| 4 | `ONETURN` | int |  |  |  | 타순 (1~9) | `one_turn_if` |
| 5 | `POSI` | varchar | 5 |  |  | 포지션 코드 (XY: X=교체순번, Y=포지션) | `position_cd` |
| 6 | `PCODE` | varchar | 10 |  |  | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 7 | `PO` | smallint |  |  |  | 자살 (Put Out) | `po` |
| 8 | `ASS` | smallint |  |  |  | 보살 (Assist) | `ast` |
| 9 | `ERR` | smallint |  |  |  | 실책 | `err` |
| 10 | `DP` | smallint |  |  |  | 병살 (Double Play) | `dp` |
| 11 | `PB` | smallint |  |  |  | 포일 (Passed Ball) | `pb` |
| 12 | `INPUTTIME` | datetime |  | NN |  | 입력 시각 | `input_tm` |

## 코드값 / 고유값


### `TB`

| 값 | 건수 |
|-----|------|
| `B` | 423,738 |
| `T` | 422,998 |



### `POSI`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `PO`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `ASS`

| 값 | 건수 |
|-----|------|
| `0` | 594,550 |
| `1` | 123,439 |
| `2` | 58,894 |
| `3` | 34,571 |
| `4` | 19,185 |

> 외 8건 — 전체 목록은 `raw/column-metadata.json` 참조



### `ERR`

| 값 | 건수 |
|-----|------|
| `0` | 812,870 |
| `1` | 32,303 |
| `2` | 1,506 |
| `3` | 54 |
| `4` | 3 |



### `DP`

| 값 | 건수 |
|-----|------|
| `0` | 751,785 |
| `1` | 73,706 |
| `2` | 17,343 |
| `3` | 3,400 |
| `4` | 443 |

> 외 3건 — 전체 목록은 `raw/column-metadata.json` 참조



### `PB`

| 값 | 건수 |
|-----|------|
| `0` | 843,501 |
| `1` | 3,138 |
| `2` | 90 |
| `3` | 7 |


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `19970915HHSB0`, `20050923LTHT0`, `20030710SKOB2` |
| `GDAY` | `19970915`, `20050923`, `20030710` |
| `TB` | `T`, `B`, `B` |
| `ONETURN` | `2`, `9`, `9` |
| `POSI` | `15`, `26`, `27` |
| `PCODE` | `93726`, `74605`, `73213` |
| `PO` | `0`, `1`, `0` |
| `ASS` | `0`, `2`, `2` |
| `ERR` | `0`, `0`, `0` |
| `DP` | `0`, `1`, `0` |
