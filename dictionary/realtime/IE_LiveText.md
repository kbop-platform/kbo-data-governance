# IE_LiveText

> 최종수정: 2026-02-25 | 버전: 2 | 출처: column-metadata.json

| 항목 | 값 |
|------|-----|
| 대표 DB | `DB2_BASEBALL_NEW_220328` |
| 행 수 | 8,005,079 |
| 컬럼 수 | 7 |
| PK | `gameID, GYEAR, SeqNO` |
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
| 3 | `LiveText` | varchar | 200 | NN |  | 실시간 문자 중계 텍스트 | `live_text` |
| 4 | `SeqNO` | smallint |  | NN | PK | 순번 | `seq_no` |
| 5 | `Inning` | tinyint |  | NN |  | 이닝 | `inning_no` |
| 6 | `bTop` | tinyint |  | NN |  | 초/말 구분 (1=초, 0=말) | `top_bottom_cd` |
| 7 | `textStyle` | tinyint |  | NN |  | 텍스트 스타일 코드 | `text_style_cd` |

## 코드값 / 고유값

> **EUC-KR 참고**: `textStyle` 등 varchar 컬럼의 한글 데이터가 EUC-KR 인코딩으로 깨져 표시됨. nvarchar 전환은 마이그레이션 시 처리.


### `GYEAR`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `SeqNO`

→ 고유값 20종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `Inning`

→ 고유값 19종 이상 — 상세 분포는 `raw/column-metadata.json` 참조



### `bTop`

| 값 | 건수 |
|-----|------|
| `1` | 4,045,213 |
| `0` | 3,958,252 |
| `99` | 1,614 |



### `textStyle`

| 값 | 건수 |
|-----|------|
| `1` | 4,525,865 |
| `8` | 1,181,293 |
| `13` | 1,059,661 |
| `14` | 278,278 |
| `2` | 276,181 |

> 외 6건 — 전체 목록은 `raw/column-metadata.json` 참조


## 샘플 데이터

| 컬럼 | 샘플 |
|------|------|
| `gameID` | `20040310LTSS0`, `20040310LTSS0`, `20040310LTSS0` |
| `GYEAR` | `2004`, `2004`, `2004` |
| `LiveText` | `1È¸ÃÊ ·Ôµ¥°ø°Ý`, `1¹øÅ¸ÀÚ ±è´ëÀÍ`, `1±¸ ½ºÆ®¶óÀÌÅ©` |
| `SeqNO` | `1`, `2`, `3` |
| `Inning` | `1`, `1`, `1` |
| `bTop` | `1`, `1`, `1` |
| `textStyle` | `0`, `8`, `1` |
