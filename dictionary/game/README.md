# 경기 기록 테이블 사전

| 테이블 | 컬럼 수 | 행 수 | PK | 스키마 |
|--------|--------|-------|-----|--------|
| [GAMEINFO](./GAMEINFO.md) | 27 | 23,579 | GMKEY, GDAY | legacy |
| [GAMECONTAPP](./GAMECONTAPP.md) | 29 | 2,531,702 | GMKEY, GYEAR, SERNO | legacy |
| [ENTRY](./ENTRY.md) | 11 | 854,280 | GMKEY, GDAY, TURN, PCODE, POSI | legacy |
| [Hitter](./Hitter.md) | 26 | 648,248 | GMKEY, GDAY, PCODE | legacy |
| [Pitcher](./Pitcher.md) | 36 | 223,624 | GMKEY, GDAY, PCODE | legacy |
| [Score](./Score.md) | 60 | 23,579 | GMKEY, GDAY | legacy |
| [DEFEN](./DEFEN.md) | 12 | 846,736 |  | legacy |
| [GAME_HR](./GAME_HR.md) | 15 | 7,784 | LE_ID, SR_ID, G_ID, SEQ_NO | new |
| [GAME_MEMO](./GAME_MEMO.md) | 20 | 54,544 | LE_ID, SR_ID, G_ID, INN_NO, BAT_ORDER_NO, BAT_AROUND_NO, TB_SC, PA_PIT_NO, ORDER_NO | new |
| [GAME_MEMO_PITCHCLOCK](./GAME_MEMO_PITCHCLOCK.md) | 16 | 237 | LE_ID, SR_ID, G_ID, SEQ_NO | new |
| [GAMEINFO_WEATHER](./GAMEINFO_WEATHER.md) | 12 | 1,680 | code, tm | unknown |
| [PITCHCLOCK](./PITCHCLOCK.md) | 19 | 215 | GMKEY, GYEAR, GDAY, LIVETEXT | legacy |
