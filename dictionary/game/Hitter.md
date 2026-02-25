# Hitter

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB1_BASEBALL_220328` |
| 행 수 | 648,248 |
| 컬럼 수 | 26 |
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
| 3 | `TB` | char | 1 | NN |  | 팀 구분 (T=원정/Top, B=홈/Bottom) | `top_bottom_cd` |
| 4 | `NAME` | nvarchar | 15 |  |  | 선수명 (varchar=EUC-KR 깨짐 가능) | `player_nm` |
| 5 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 6 | `TURN` | char | 2 |  |  | 타순 | `turn_no` |
| 7 | `ONETURN` | char | 1 |  |  | 타순 (1~9) | `one_turn_if` |
| 8 | `PA` | int |  | NN |  | 타석 (Plate Appearance) | `pa` |
| 9 | `AB` | int |  | NN |  | 타수 (At Bat) | `ab` |
| 10 | `RBI` | int |  | NN |  | 타점 | `rbi` |
| 11 | `RUN` | int |  | NN |  | 득점 | `run` |
| 12 | `HIT` | int |  | NN |  | 안타 | `hit` |
| 13 | `H2` | int |  | NN |  | 2루타 | `h2b` |
| 14 | `H3` | int |  | NN |  | 3루타 | `h3b` |
| 15 | `HR` | int |  | NN |  | 홈런 | `hr` |
| 16 | `SB` | int |  | NN |  | 도루 | `sb` |
| 17 | `CS` | int |  | NN |  | 도루실패 | `cs` |
| 18 | `SH` | int |  | NN |  | 희생번트 | `sh` |
| 19 | `SF` | int |  | NN |  | 희생플라이 | `sf` |
| 20 | `BB` | int |  | NN |  | 볼넷 | `bb` |
| 21 | `IB` | int |  | NN |  | 고의사구 (Intentional BB) | `ibb` |
| 22 | `HP` | int |  | NN |  | 사구 (Hit by Pitch) | `hbp` |
| 23 | `KK` | int |  | NN |  | 삼진 | `so` |
| 24 | `GD` | int |  | NN |  | 병살타 | `gidp` |
| 25 | `ERR` | int |  | NN |  | 실책 | `err` |
| 26 | `LOB` | int |  | NN |  | 잔루 | `lob` |

## 코드값 / 고유값


### `GDAY`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `TB`

| 값 | 건수 |
|-----|------|
| `T` | 324,226 |
| `B` | 324,022 |



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `TURN`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `ONETURN`

| 값 | 건수 |
|-----|------|
| `8` | 77,112 |
| `9` | 75,520 |
| `7` | 69,259 |
| `6` | 66,550 |
| `2` | 65,620 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GMKEY` | `19820327SSLG0`, `19820327SSLG0`, `19820327SSLG0` |
| `GDAY` | `19820327`, `19820327`, `19820327` |
| `TB` | `T`, `B`, `B` |
| `NAME` | `천보성`, `최정우`, `김인식` |
| `PCODE` | `40002`, `40003`, `40006` |
| `TURN` | `11`, `29`, `11` |
| `ONETURN` | `1`, `9`, `1` |
| `PA` | `5`, `1`, `6` |
| `AB` | `3`, `1`, `5` |
| `RBI` | `0`, `0`, `0` |
