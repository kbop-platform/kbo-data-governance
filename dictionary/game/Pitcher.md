# Pitcher

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 223,624 |
| 컬럼 수 | 36 |
| PK | `GMKEY, GDAY, PCODE` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 경기 당일 (S2i 전송) |
| 소비자 | 기록팀, 통계팀, 외부 API |
| 데이터 프로덕트 | [경기 요약](../products/game-summary.md) |
| 접근 수준 | Internal |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [약어 사전](../../standards/abbreviations.md) |

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GMKEY` | char | 13 | NN | PK | 경기 고유키 (YYYYMMDDVVHH#, 13자리) | `game_id` |
| 2 | `GDAY` | char | 8 | NN | PK | 경기 일자 (YYYYMMDD) | `game_dt` |
| 3 | `TB` | char | 1 |  |  | 팀 구분 (T=원정/Top, B=홈/Bottom) | `top_bottom_cd` |
| 4 | `NAME` | varchar | 20 |  |  | 선수명 (varchar=EUC-KR 깨짐 가능) | `player_nm` |
| 5 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 6 | `POS` | varchar | 10 |  |  | 등판 순서 (S=선발, R=구원) | `position_cd` |
| 7 | `START` | char | 1 |  |  | 선발 여부 | `start_if` |
| 8 | `QUIT` | char | 1 |  |  | 종료 여부 | `quit` |
| 9 | `CG` | int |  | NN |  | 완투 | `cg` |
| 10 | `SHO` | int |  | NN |  | 완봉 | `sho` |
| 11 | `WLS` | char | 1 |  |  | 승패세 (W=승, L=패, S=세이브) | `wls_cd` |
| 12 | `HOLD` | smallint |  | NN |  | 홀드 | `hld` |
| 13 | `INN` | varchar | 10 |  |  | 이닝 번호 | `ip` |
| 14 | `INN2` | int |  | NN |  | 이닝 세부 (아웃수 환산 또는 연장 구분) | `inn_2_score` |
| 15 | `BF` | int |  | NN |  | 상대타자수 | `bf` |
| 16 | `PA` | int |  | NN |  | 타석 (Plate Appearance) | `pa` |
| 17 | `AB` | int |  | NN |  | 타수 (At Bat) | `ab` |
| 18 | `HIT` | int |  | NN |  | 안타 | `hit` |
| 19 | `H2` | int |  | NN |  | 2루타 | `h2b` |
| 20 | `H3` | int |  | NN |  | 3루타 | `h3b` |
| 21 | `HR` | int |  | NN |  | 홈런 | `hr` |
| 22 | `SB` | int |  | NN |  | 도루 | `sb` |
| 23 | `CS` | int |  | NN |  | 도루실패 | `cs` |
| 24 | `SH` | int |  | NN |  | 희생번트 | `sh` |
| 25 | `SF` | int |  | NN |  | 희생플라이 | `sf` |
| 26 | `BB` | int |  | NN |  | 볼넷 | `bb` |
| 27 | `IB` | int |  | NN |  | 고의사구 (Intentional BB) | `ibb` |
| 28 | `HP` | int |  | NN |  | 사구 (Hit by Pitch) | `hbp` |
| 29 | `KK` | int |  | NN |  | 삼진 | `so` |
| 30 | `GD` | int |  | NN |  | 병살타 | `gidp` |
| 31 | `WP` | int |  | NN |  | 폭투 | `wp` |
| 32 | `BK` | int |  | NN |  | 보크 | `bk` |
| 33 | `ERR` | int |  | NN |  | 실책 | `err` |
| 34 | `R` | int |  | NN |  | 실점 | `runs_cn` |
| 35 | `ER` | int |  | NN |  | 자책점 | `er` |
| 36 | `BS` | int |  |  |  | 블론세이브 (Blown Save) | `bs` |

## 코드값 / 고유값


### `GDAY`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TB`

| 값 | 건수 |
|-----|------|
| `B` | 113,318 |
| `T` | 110,306 |



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `POS`

| 값 | 건수 |
|-----|------|
| `11` | 47,158 |
| `21` | 43,635 |
| `31` | 35,837 |
| `41` | 25,695 |
| `51` | 14,683 |

> 외 8건 — 전체 목록은 `raw/column-metadata.json` 참조



### `START`

| 값 | 건수 |
|-----|------|
| `1` | 47,158 |



### `QUIT`

| 값 | 건수 |
|-----|------|
| `1` | 47,158 |
| `0` | 2,757 |



### `WLS`

| 값 | 건수 |
|-----|------|
| `` | 116,107 |
| `L` | 46,130 |
| `W` | 46,130 |
| `S` | 10,707 |
| `0` | 2,494 |

> 외 1건 — 전체 목록은 `raw/column-metadata.json` 참조



### `HOLD`

| 값 | 건수 |
|-----|------|
| `0` | 203,351 |
| `1` | 16,915 |
| `2` | 2,426 |
| `3` | 786 |
| `4` | 126 |

> 외 2건 — 전체 목록은 `raw/column-metadata.json` 참조



### `INN`

| 값 | 건수 |
|-----|------|
| `1` | 41,256 |
| `9` | 34,662 |
| `0 1/3` | 18,581 |
| `0 2/3` | 17,488 |
| `8` | 12,673 |

> 외 15건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `19820327SSLG0`, `19820327SSLG0`, `19820327SSLG0` |
| `GDAY` | `19820327`, `19820327`, `19820327` |
| `TB` | `T`, `B`, `B` |
| `NAME` | `È²±ÔºÀ`, `ÀÌ±æÈ¯`, `À¯Á¾°â` |
| `PCODE` | `80620`, `82122`, `82175` |
| `POS` | `11`, `11`, `21` |
| `START` | `1`, `1`, `1` |
| `QUIT` | `1`, `1`, `1` |
| `CG` | `0`, `0`, `0` |
| `SHO` | `0`, `0`, `0` |
