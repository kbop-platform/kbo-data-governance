# 통계/집계 테이블 사전

| 테이블 | 컬럼 수 | 행 수 | PK | 스키마 |
|--------|--------|-------|-----|--------|
| [BatTotal](./BatTotal.md) | 23 | 13,616 | PCODE, GYEAR, SEC | legacy |
| [PitTotal](./PitTotal.md) | 22 | 9,377 | PCODE, GYEAR, SEC | legacy |
| [TeamRank](./TeamRank.md) | 30 | 373 | GYEAR, SEC, TEAM | unknown |
| [KBO_BATRESULT](./KBO_BATRESULT.md) | 90 | 424,921 | GMKEY, GDAY, PCODE | legacy |
| [KBO_PITRESULT](./KBO_PITRESULT.md) | 23 | 134,292 | GMKEY, GDAY, PCODE | legacy |
| [KBO_ETCGAME](./KBO_ETCGAME.md) | 5 | 122,762 | GMKEY, GDAY, SEQ | legacy |
| [SEASON_PLAYER_HITTER](./SEASON_PLAYER_HITTER.md) | 43 | 19,747 | SEASON_ID, P_ID, SECTION_CD, GROUP_IF | new |
| [SEASON_PLAYER_PITCHER](./SEASON_PLAYER_PITCHER.md) | 54 | 13,306 | SEASON_ID, P_ID, SECTION_CD, GROUP_IF | new |
| [SEASON_PLAYER_HITTER_SITUATION](./SEASON_PLAYER_HITTER_SITUATION.md) | 14 | 360,625 | SEASON_ID, P_ID, SECTION_CD, SITUATION_IF | new |
| [SEASON_PLAYER_PITCHER_SITUATION](./SEASON_PLAYER_PITCHER_SITUATION.md) | 14 | 301,375 | SEASON_ID, P_ID, SECTION_CD, SITUATION_IF | new |
