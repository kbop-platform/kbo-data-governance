# 전체 DB 스키마 요약

추출 일시: 2026-02-23
DB 수: 19개

## DB별 테이블 수
| DB | 테이블 수 | 총 컬럼 수 | 총 행 수 |
|-----|----------|-----------|---------|
| DB1_BASEBALL_220328 | 13 | 327 | 5,237,679 |
| DB1_BASEBALL_2_220328 | 4 | 125 | 695,053 |
| DB2_BASEBALL_220328 | 18 | 477 | 874,166 |
| DB2_BASEBALL_2_220328 | 5 | 132 | 470,448 |
| DB2_BASEBALL_NEW_220328 | 15 | 163 | 9,942,740 |
| DB2_POSTSEASON | 21 | 490 | 297,976 |
| DB2_ALLSTAR | 20 | 468 | 25,119 |
| DB2_EXHIBITION | 24 | 593 | 852,751 |
| DB2_INTERNATIONAL | 21 | 488 | 30,697 |
| DB1_MINOR_BASEBALL_220328 | 9 | 262 | 1,676,024 |
| DB1_MINOR_SO_BASEBALL | 9 | 262 | 25,796 |
| DB2_MINOR_BASEBALL_220328 | 17 | 415 | 491,954 |
| DB2_MINOR_BASEBALL_NEW_220328 | 8 | 88 | 5,034,305 |
| DB2_MINOR_POSTSEASON | 21 | 487 | 2,568 |
| DB2_MINOR_SO_BASEBALL | 15 | 393 | 16,025 |
| DB2_MINOR_SO_BASEBALL_NEW | 8 | 88 | 8,746 |
| BROADCAST_BASEBALL | 5 | 88 | 3,195 |
| DB2_OTHER_GAME | 20 | 468 | 9,658 |
| FALL_LEAGUE_BASEBALL | 11 | 347 | 8,257 |

## 고유 테이블 유형: 52종
| 테이블명 | 존재하는 DB 수 | 컬럼수 범위 |
|---------|--------------|-----------|
| BatTotal | 12 | 22~23 |
| BROADCASTING_CD | 1 | 2 |
| BROADCASTING_RATE | 1 | 23 |
| BROADCASTING_RATE_MINOR | 1 | 21 |
| BROADCASTING_schedule | 1 | 22 |
| BROADCASTING_schedule_minor  | 1 | 20 |
| CANCEL_GAME | 1 | 6 |
| DEFEN | 2 | 12 |
| ENTRY | 12 | 11~12 |
| FALL_LEAGUE_RECORD | 1 | 20 |
| GAMECONTAPP | 12 | 29 |
| GAMEINFO | 12 | 27 |
| GAMEINFO_WEATHER | 1 | 12 |
| GAME_HR | 2 | 15 |
| GAME_KBO | 1 | 24 |
| GAME_MEMO | 2 | 20 |
| GAME_MEMO_PITCHCLOCK | 2 | 16 |
| GAME_PLAYER_HITTER | 1 | 31 |
| GAME_PLAYER_PITCHER | 1 | 38 |
| GAME_TEAM_HITTER | 1 | 24 |
| GAME_TEAM_PITCHER | 1 | 24 |
| Hitter | 12 | 26 |
| IE_BallCount | 9 | 11 |
| IE_BatterRecord | 9 | 25 |
| IE_GameList | 9 | 6 |
| IE_GAMESTATE | 9 | 5 |
| IE_LiveText | 9 | 7 |
| IE_log | 1 | 3 |
| IE_PitcherRecord | 9 | 22 |
| IE_Scoreinning | 9 | 5 |
| IE_ScoreRHEB | 9 | 7 |
| KBO_BATRESULT | 9 | 65~90 |
| KBO_ETCGAME | 9 | 5 |
| KBO_PITRESULT | 9 | 23 |
| KBO_schedule | 3 | 15~22 |
| person | 4 | 16~20 |
| person2 | 1 | 17 |
| PERSON_BASE | 1 | 6 |
| PERSON_FA | 1 | 4 |
| PITCHCLOCK | 4 | 19 |
| Pitcher | 12 | 36 |
| PitTotal | 12 | 21~22 |
| Score | 12 | 60 |
| SEASON_PLAYER_HITTER | 4 | 43~46 |
| SEASON_PLAYER_HITTER_SITUATION | 3 | 14 |
| SEASON_PLAYER_PITCHER | 4 | 54~59 |
| SEASON_PLAYER_PITCHER_SITUATION | 3 | 14 |
| SEASON_TEAM_HITTER | 1 | 37 |
| SEASON_TEAM_PITCHER | 1 | 38 |
| STADIUM | 2 | 3 |
| TEAM | 3 | 7 |
| TeamRank | 12 | 29~30 |
