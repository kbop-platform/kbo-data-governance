# PERSON (2군)

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_MINOR_BASEBALL_220328` |
| 행 수 | 13,902 |
| 컬럼 수 | 16 |
| PK | `GYEAR, PCODE` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 3 — Reference |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 시즌 전 갱신 |
| 소비자 | 기록팀 |
| 데이터 프로덕트 | [선수 프로필](../products/player-profile.md) |
| 접근 수준 | Restricted |
| 관련 표준 | [도메인 타입](../../standards/domain-types.md) |

> **관련 테이블**: [person](./person.md)(1군, 20컬럼)의 2군 버전. T_ID/ENGNAME/DRAFT/REG_DT 없음.
> 1군 [person](./person.md)과 스키마 거의 동일하나 DB가 분리되어 있음 (MINOR_BASEBALL).

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 2 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 3 | `NAME` | varchar | 20 | NN |  | 선수명 (varchar=EUC-KR 깨짐 가능) | `player_nm` |
| 4 | `TEAM` | varchar | 8 | NN |  | 팀 코드 (2자리, HH=키움, HT=KIA 등) | `team_cd` |
| 5 | `POS` | char | 1 |  |  | 포지션 코드 | `position_cd` |
| 6 | `POSITION` | varchar | 4 |  |  | 포지션 | `position_nm` |
| 7 | `BACKNUM` | varchar | 50 |  |  | 등번호 | `back_no` |
| 8 | `CNAME` | varchar | 30 |  |  | 한자 이름 | `player_hanja_nm` |
| 9 | `HITTYPE` | varchar | 8 |  |  | 타석 방향 | `bat_throw_cd` |
| 10 | `BIRTH` | varchar | 8 |  |  | 생년월일 | `birth_dt` |
| 11 | `HEIGHT` | varchar | 3 |  |  | 키 | `height_va` |
| 12 | `WEIGHT` | varchar | 3 |  |  | 몸무게 | `weight_va` |
| 13 | `INDATE` | varchar | 8 |  |  | 입단일 | `join_dt` |
| 14 | `PROMISE` | varchar | 12 |  |  | 계약금 | `signing_bonus_va` |
| 15 | `MONEY` | varchar | 12 |  |  | 연봉 | `salary_va` |
| 16 | `CAREER` | varchar | 255 |  |  | 경력 | `career_nm` |

## 코드값 / 고유값

> **EUC-KR 참고**: `TEAM`, `POSITION`, `HITTYPE` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `GYEAR`

→ 고유값 17종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `TEAM`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `POS`

| 값 | 건수 |
|-----|------|
| `1` | 6,898 |
| `3` | 1,423 |
| `7` | 1,358 |
| `2` | 1,287 |
| `4` | 645 |

> 외 4건 — 전체 목록은 `raw/column-metadata.json` 참조



### `POSITION`

| 값 | 건수 |
|-----|------|
| `Åõ` | 6,898 |
| `³»` | 3,213 |
| `¿Ü` | 2,504 |
| `Æ÷` | 1,287 |



### `HITTYPE`

| 값 | 건수 |
|-----|------|
| `¿ìÅõ¿ìÅ¸` | 8,351 |
| `ÁÂÅõÁÂÅ¸` | 2,446 |
| `¿ìÅõÁÂÅ¸` | 2,245 |
| `¿ì¾ð¿ìÅ¸` | 591 |
| `¿ìÅõ¾çÅ¸` | 151 |

> 외 5건 — 전체 목록은 `raw/column-metadata.json` 참조



### `BIRTH`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `HEIGHT`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `WEIGHT`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조



### `INDATE`

→ 연속값 — 상세 분포는 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `GYEAR` | `2010`, `2010`, `2010` |
| `PCODE` | `60100`, `60102`, `60105` |
| `NAME` | `±è¹ÎÇõ`, `°íÁ¾¿í`, `¹èÀçÈ¯` |
| `TEAM` | `KT`, `SSG`, `»ó¹«` |
| `POS` | `7`, `7`, `1` |
| `POSITION` | `¿Ü`, `¿Ü`, `Åõ` |
| `BACKNUM` | `53`, `38`, `61` |
| `CNAME` | `(ÑÑÚÂúÒ)`, `(ÍÔðóéô)`, `(ÛÑî¥üº)` |
| `HITTYPE` | `¿ìÅõÁÂÅ¸`, `¿ìÅõÁÂÅ¸`, `¿ìÅõ¿ìÅ¸` |
| `BIRTH` | `19951121`, `19890111`, `19950224` |
