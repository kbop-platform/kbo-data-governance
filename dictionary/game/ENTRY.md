# ENTRY

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 854,280 |
| 컬럼 수 | 11 |
| PK | `GMKEY, GDAY, TURN, PCODE, POSI` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 기록팀, 방송팀 |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [코드 사전](../../standards/code-dictionary.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GMKEY` | char | 13 | NN | PK | 경기 고유키 (YYYYMMDDVVHH#, 13자리) | `game_id` |
| 2 | `GDAY` | char | 8 | NN | PK | 경기 일자 (YYYYMMDD) | `game_dt` |
| 3 | `TURN` | char | 2 | NN | PK | 타순 | `turn_no` |
| 4 | `NAME` | varchar | 15 | NN |  | 선수명 (varchar=EUC-KR 깨짐 가능) | `player_nm` |
| 5 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 6 | `TEAM` | char | 1 | NN |  | 팀 코드 (2자리, HH=키움, HT=KIA 등) | `team_cd` |
| 7 | `POSI` | char | 2 | NN | PK | 포지션 코드 (XY: X=교체순번, Y=포지션) | `position_cd` |
| 8 | `CHIN` | varchar | 2 | NN |  | 교체 이닝 | `change_inning_no` |
| 9 | `CHTURN` | char | 1 | NN |  | 교체 타순 | `change_turn_no` |
| 10 | `CHBCNT` | varchar | 2 | NN |  | 교체 시점 볼카운트 | `change_ball_count_cd` |
| 11 | `CHIN2` | char | 1 | NN |  | 교체 이닝 세부 | `change_inning2_no` |

## 코드값 / 고유값


### `GDAY`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TURN`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `TEAM`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `POSI`

| 값 | 건수 |
|-----|------|
| `11` | 47,384 |
| `19` | 47,158 |
| `18` | 47,158 |
| `17` | 47,158 |
| `16` | 47,158 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조



### `CHIN`

→ 고유값 16종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `CHTURN`

| 값 | 건수 |
|-----|------|
| `0` | 471,566 |
| `9` | 47,939 |
| `8` | 47,255 |
| `7` | 44,468 |
| `6` | 42,567 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `CHBCNT`

| 값 | 건수 |
|-----|------|
| `0` | 849,347 |
| `1` | 2,483 |
| `2` | 1,220 |
| `3` | 622 |
| `4` | 310 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조



### `CHIN2`

| 값 | 건수 |
|-----|------|
| `0` | 852,852 |
| `1` | 756 |
| `2` | 629 |
| `` | 40 |
| `3` | 2 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `19820327SSLG0`, `19820327SSLG0`, `19820327SSLG0` |
| `GDAY` | `19820327`, `19820327`, `19820327` |
| `TURN` | `10`, `10`, `11` |
| `NAME` | `ÀüÁØ¿ì`, `ÇÑµ¿Èñ`, `¹Ú°Ç¿ì` |
| `PCODE` | `80620`, `82122`, `40002` |
| `TEAM` | `B`, `B`, `T` |
| `POSI` | `11`, `11`, `15` |
| `CHIN` | `0`, `0`, `0` |
| `CHTURN` | `0`, `0`, `0` |
| `CHBCNT` | `0`, `0`, `0` |
