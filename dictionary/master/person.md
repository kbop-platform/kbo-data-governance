# person

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 100,812 |
| 컬럼 수 | 20 |
| PK | `GYEAR, PCODE` |
| 스키마 세대 | legacy |
| 데이터 티어 | Tier 1 — Critical |
| 데이터 오너 | 기록위원회 (R-03) |
| 갱신 주기 | 시즌 전 갱신 |
| 소비자 | 전 시스템 |
| 데이터 프로덕트 | [선수 프로필](../products/player-profile.md) |
| 접근 수준 | Restricted |
| 관련 표준 | [ID 체계](../../standards/id-system.md), [도메인 타입](../../standards/domain-types.md) |

> **관련 테이블**: person 계열은 동일 스키마 패턴으로 DB별 분리 존재
> - `person` (이 파일) — **1군 선수 마스터** (DB2_BASEBALL_NEW, 20컬럼). ENGNAME, DRAFT, REG_DT, T_ID 포함
> - [person2](./person2.md) — **1군 선수 마스터 (구버전)**. 17컬럼, PK에 NAME 포함. person 대비 ENGNAME/DRAFT/REG_DT 없음
> - [PERSON](./PERSON.md) — **2군 선수 마스터** (DB2_MINOR_BASEBALL, 16컬럼). T_ID 없음
> - [PERSON_FA](./PERSON_FA.md) — **FA 계약 정보** (4컬럼, 228건). 보조 테이블

## 컬럼 상세

| # | 컬럼명 | 타입 | 길이 | NULL | PK | 설명 | 표준명(안) |
|---|--------|------|------|------|----|------|------|
| 1 | `GYEAR` | smallint |  | NN | PK | 시즌 연도 (4자리, "9999"=통산) | `season_yr` |
| 2 | `PCODE` | varchar | 10 | NN | PK | 선수 코드 (5~6자리 숫자 문자열) | `player_id` |
| 3 | `NAME` | varchar | 20 | NN |  | 선수명 (varchar=EUC-KR 깨짐 가능) | `player_nm` |
| 4 | `TEAM` | varchar | 20 | NN |  | 팀 코드 (2자리, HH=키움, HT=KIA 등) | `team_cd` |
| 5 | `T_ID` | char | 2 |  |  | 팀 코드 (2자리) | `team_id` |
| 6 | `POS` | char | 1 |  |  | 포지션 코드 | `position_cd` |
| 7 | `POSITION` | varchar | 4 |  |  | 포지션 | `position_nm` |
| 8 | `BACKNUM` | varchar | 50 |  |  | 등번호 | `back_no` |
| 9 | `ENGNAME` | nvarchar | 50 |  |  | 영문 이름 | `player_eng_nm` |
| 10 | `CNAME` | nvarchar | 30 |  |  | 한자 이름 | `player_hanja_nm` |
| 11 | `HITTYPE` | varchar | 8 |  |  | 타석 방향 | `bat_throw_cd` |
| 12 | `BIRTH` | varchar | 8 |  |  | 생년월일 | `birth_dt` |
| 13 | `HEIGHT` | varchar | 3 |  |  | 키 | `height_va` |
| 14 | `WEIGHT` | varchar | 3 |  |  | 몸무게 | `weight_va` |
| 15 | `INDATE` | varchar | 8 |  |  | 입단일 | `join_dt` |
| 16 | `PROMISE` | varchar | 12 |  |  | 계약금 | `signing_bonus_va` |
| 17 | `MONEY` | varchar | 12 |  |  | 연봉 | `salary_va` |
| 18 | `CAREER` | varchar | 255 |  |  | 경력 | `career_nm` |
| 19 | `DRAFT` | varchar | 70 |  |  | 드래프트 정보 | `draft_nm` |
| 20 | `REG_DT` | datetime |  | NN |  | 등록 일시 | `reg_dt` |

## 코드값 / 고유값

> **EUC-KR 참고**: `TEAM`, `POSITION`, `HITTYPE`, `CAREER` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `PCODE`

→ 선수 식별자 — [선수 마스터(person)](../master/person.md) 참조



### `TEAM`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `T_ID`

→ 팀 식별자 — [팀 마스터(TEAM)](../master/TEAM.md) 참조



### `POS`

| 값 | 건수 |
|-----|------|
| `1` | 36,997 |
| `0` | 10,694 |
| `7` | 8,520 |
| `3` | 7,128 |
| `2` | 6,629 |

> 외 5건 — 전체 목록은 `raw/column-metadata.json` 참조



### `POSITION`

| 값 | 건수 |
|-----|------|
| `Åõ` | 36,997 |
| `³»` | 18,789 |
| `¿Ü` | 16,901 |
| `ÄÚÄ¡` | 9,863 |
| `Æ÷` | 6,629 |

> 외 3건 — 전체 목록은 `raw/column-metadata.json` 참조



### `HITTYPE`

| 값 | 건수 |
|-----|------|
| `¿ìÅõ¿ìÅ¸` | 62,648 |
| `ÁÂÅõÁÂÅ¸` | 15,952 |
| `¿ìÅõÁÂÅ¸` | 6,479 |
| `¿ì¾ð¿ìÅ¸` | 2,515 |
| `¿ìÅõ¾çÅ¸` | 998 |

> 외 7건 — 전체 목록은 `raw/column-metadata.json` 참조



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
| `GYEAR` | `1982`, `1982`, `1982` |
| `PCODE` | `10005`, `10082`, `30003` |
| `NAME` | `Â÷¿µÈ­`, `È²ÅÂÈ¯`, `¼Õ»ó´ë` |
| `TEAM` | `ÇØÅÂ`, `OB`, `»ï¼º` |
| `T_ID` | `HT`, `OB`, `SS` |
| `POS` | `4`, `1`, `2` |
| `POSITION` | `³»`, `Åõ`, `Æ÷` |
| `BACKNUM` | ``, ``, `` |
| `ENGNAME` | `CHA Young Hwa`, `SON Sang Dae`, `YOO Ji Hwuon` |
| `CNAME` | `(車榮華)`, `(黃泰煥)`, `(孫相大)` |
