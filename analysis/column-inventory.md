# 전체 컬럼 인벤토리

> 분석 일시: 2026-02-23
> 대상: 19개 DB, 52종 테이블

## 1. 테이블별 컬럼 상세

### 1.1 GAMEINFO (경기 기본 정보) - 27컬럼
| # | 컬럼 | 타입 | 의미 | 비고 |
|---|------|------|------|------|
| 1 | GMKEY | char(13) | 경기 고유키 | PK 일부 |
| 2 | GDAY | char(8)/int | 경기 일자 (YYYYMMDD) | DB마다 타입 다름 |
| 3 | DBHD | char(1)/tinyint | 더블헤더 번호 | 0=단일 |
| 4 | STADIUM | varchar(10) | 구장명 (한글) | |
| 5 | VTEAM | char(2) | 원정팀 코드 | 2자 영문 |
| 6 | HTEAM | char(2) | 홈팀 코드 | 2자 영문 |
| 7 | STTM | char(4)/varchar | 시작시간 (HHMM) | |
| 8 | ENTM | char(4)/varchar | 종료시간 (HHMM) | |
| 9 | DLTM | char(3)/varchar | 지연시간 (분) | |
| 10 | GMTM | char(3)/varchar | 경기시간 (분) | |
| 11 | STAD | char(2) | 구장 코드 (영문) | |
| 12 | UMPC | varchar(10) | 주심 | |
| 13 | UMP1 | varchar(10) | 1루심 | |
| 14 | UMP2 | varchar(10) | 2루심 | |
| 15 | UMP3 | varchar(10) | 3루심 | |
| 16 | UMPL | varchar(10) | 좌선심 | |
| 17 | UMPR | varchar(10) | 우선심 | |
| 18 | SCOA | varchar(10) | 기록원 A | |
| 19 | SCOB | varchar(10) | 기록원 B | |
| 20 | TEMP | varchar(4) | 기온 (×10, 예: 251=25.1°C) | |
| 21 | MOIS | varchar(3) | 습도 (%) | |
| 22 | WEATH | char(1) | 날씨 코드 | C=맑음, R=비 |
| 23 | WIND | varchar(4) | 풍향 | |
| 24 | WINS | varchar(3) | 풍속 | |
| 25 | GWEEK | varchar(3) | 요일 | EUC-KR 한글 |
| 26 | CROWD | varchar(6) | 관중수 | |
| 27 | CHAJUN | varchar(3) | 차전(라운드) | |

### 1.2 GAMECONTAPP (경기 진행 내역) - 29컬럼
| # | 컬럼 | 타입 | 의미 | 비고 |
|---|------|------|------|------|
| 1 | GMKEY | char(13) | 경기키 | PK |
| 2 | GYEAR | smallint | 시즌 연도 | PK |
| 3 | GDAY | char(8) | 경기일자 | |
| 4 | SERNO | smallint | 이벤트 순번 | PK |
| 5 | TURN | char(2) | 타순 | |
| 6 | INN | tinyint | 이닝 | 1~25 |
| 7 | TB | char(1) | 팀구분 | T/B |
| 8 | INN2 | char(1) | 이닝 세부 | |
| 9 | OCOUNT | char(1) | 아웃 카운트 | 0/1/2/4 |
| 10 | BCOUNT | varchar(30) | 볼카운트 상세 | |
| 11 | RTURN | char(2) | 주자 타순? | |
| 12 | HOW | char(2) | 결과 코드 | 49종 |
| 13 | FIELD | varchar(25) | 수비 상세 | |
| 14 | PLACE | char(1) | 타구 방향 | 0~9,A~S |
| 15 | HITTER | varchar(10) | 타자 코드 | |
| 16 | HITNAME | varchar(20) | 타자명 | |
| 17 | PITNAME | varchar(20) | 투수명 | |
| 18 | PITCHER | varchar(10) | 투수 코드 | |
| 19 | CATNAME | varchar(20) | 포수명 | |
| 20 | CATCHER | varchar(10) | 포수 코드 | |
| 21 | BCNT | char(3) | 볼카운트 요약 | |
| 22 | TSCORE | smallint | 원정팀 점수 | |
| 23 | BSCORE | smallint | 홈팀 점수 | |
| 24 | BASE1B | char(2) | 1루 주자(이전) | 타순번호 |
| 25 | BASE2B | char(2) | 2루 주자(이전) | |
| 26 | BASE3B | char(2) | 3루 주자(이전) | |
| 27 | BASE1A | char(2) | 1루 주자(이후) | |
| 28 | BASE2A | char(2) | 2루 주자(이후) | |
| 29 | BASE3A | char(2) | 3루 주자(이후) | |

### 1.3 Hitter (타자 경기 기록) - 26컬럼
| # | 컬럼 | 타입 | 의미 |
|---|------|------|------|
| 1 | GMKEY | char(13) | 경기키 |
| 2 | GDAY | char(8)/int | 경기일자 |
| 3 | TB | char(1) | 팀구분 (T/B) |
| 4 | NAME | varchar(15) | 선수명 |
| 5 | PCODE | varchar(10) | 선수코드 |
| 6 | TURN | char(2) | 타순 |
| 7 | ONETURN | int/smallint | 고유 타석순번 |
| 8 | PA | smallint | 타석 |
| 9 | AB | smallint | 타수 |
| 10 | RBI | smallint | 타점 |
| 11 | RUN | smallint | 득점 |
| 12 | HIT | smallint | 안타 |
| 13 | H2 | smallint | 2루타 |
| 14 | H3 | smallint | 3루타 |
| 15 | HR | smallint | 홈런 |
| 16 | SB | smallint | 도루 |
| 17 | CS | smallint | 도루실패 |
| 18 | SH | smallint | 희생번트 |
| 19 | SF | smallint | 희생플라이 |
| 20 | BB | smallint | 볼넷 |
| 21 | IB | smallint | 고의사구 |
| 22 | HP | smallint | 사구 |
| 23 | KK | smallint | 삼진 |
| 24 | GD | smallint | 병살타 |
| 25 | ERR | smallint | 실책 |
| 26 | LOB | smallint | 잔루 |

### 1.4 Pitcher (투수 경기 기록) - 36컬럼
| # | 컬럼 | 타입 | 의미 |
|---|------|------|------|
| 1 | GMKEY | char(13) | 경기키 |
| 2 | GDAY | char(8)/int | 경기일자 |
| 3 | TB | char(1) | 팀구분 |
| 4 | NAME | varchar(15) | 선수명 |
| 5 | PCODE | varchar(10) | 선수코드 |
| 6 | POS | char(1)/varchar | 등판 순서 |
| 7 | START | varchar(5) | 선발 여부/이닝 |
| 8 | QUIT | varchar(5) | 강판 이닝 |
| 9 | CG | smallint | 완투 |
| 10 | SHO | smallint | 완봉 |
| 11 | WLS | char(1) | 승패세 (W/L/S) |
| 12 | HOLD | smallint | 홀드 |
| 13 | INN | varchar(7) | 이닝 (예: "8 1/3") |
| 14 | INN2 | varchar(4) | 아웃수 환산 |
| 15 | BF | smallint | 타자수(BF) |
| 16 | PA | smallint | 타석수 |
| 17 | AB | smallint | 타수(피) |
| 18 | HIT | smallint | 피안타 |
| 19 | H2 | smallint | 피2루타 |
| 20 | H3 | smallint | 피3루타 |
| 21 | HR | smallint | 피홈런 |
| 22 | SB | smallint | 피도루 |
| 23 | CS | smallint | 도루저지 |
| 24 | SH | smallint | 피희생번트 |
| 25 | SF | smallint | 피희생플라이 |
| 26 | BB | smallint | 피볼넷 |
| 27 | IB | smallint | 피고의사구 |
| 28 | HP | smallint | 피사구 |
| 29 | KK | smallint | 탈삼진 |
| 30 | GD | smallint | 유도병살 |
| 31 | WP | smallint | 폭투 |
| 32 | BK | smallint | 보크 |
| 33 | ERR | smallint | 실책 |
| 34 | R | smallint | 실점 |
| 35 | ER | smallint | 자책점 |
| 36 | BS | smallint | 블론세이브 |

### 1.5 Score (이닝별 스코어) - 60컬럼
| # | 컬럼 | 타입 | 의미 |
|---|------|------|------|
| 1 | GMKEY | char(13) | 경기키 |
| 2 | GDAY | char(8)/int | 경기일자 |
| 3~52 | `{N}T`, `{N}B` | smallint | N이닝 원정(T)/홈(B) 점수 |
| | | | N = 1~25 (최대 25이닝) |
| | | | -1 = 미진행 이닝 |
| 53 | TPOINT | smallint | 원정팀 총점 |
| 54 | BPOINT | smallint | 홈팀 총점 |
| 55 | THIT | smallint | 원정팀 안타수 |
| 56 | BHIT | smallint | 홈팀 안타수 |
| 57 | TERR | smallint | 원정팀 실책수 |
| 58 | BERR | smallint | 홈팀 실책수 |
| 59 | TBBHP | smallint | 원정팀 볼넷+사구 |
| 60 | BBBHP | smallint | 홈팀 볼넷+사구 |

### 1.6 KBO_BATRESULT (타격 결과 상세) - 90컬럼 (1군) / 65컬럼 (2군)
| # | 컬럼 | 타입 | 의미 |
|---|------|------|------|
| 1 | GMKEY | char(13) | 경기키 |
| 2 | GDAY | char(8)/int | 경기일자 |
| 3 | TB | char(1) | 팀구분 |
| 4 | NAME | varchar(15) | 선수명 |
| 5 | PCODE | varchar(10) | 선수코드 |
| 6 | TURN | char(2) | 타순 |
| 7 | ONETURN | smallint | 고유 타석순번 |
| 8 | POSITION | varchar(5) | 포지션 (한글 약어) |
| 9 | CHANGEINN | tinyint | 교체 이닝 |
| 10~84 | INN{N}, IL{N}, INN{N}_3 | varchar | 이닝별 타격결과 (1~25이닝) |
| | | | INN{N}: 결과 텍스트 |
| | | | IL{N}: 상세 |
| | | | INN{N}_3: 추가정보 |
| 85 | AB | tinyint | 타수 합계 |
| 86 | RUN | tinyint | 득점 합계 |
| 87 | HIT | tinyint | 안타 합계 |
| 88 | RBI | tinyint | 타점 합계 |
| 89 | AVGS | varchar(10) | 시즌 타율 |
| 90 | AVG5 | varchar(10) | 최근5경기 타율 |

### 1.7 person (선수 마스터) - 20컬럼
| # | 컬럼 | 타입 | 의미 |
|---|------|------|------|
| 1 | GYEAR | varchar(4) | 시즌 연도 |
| 2 | PCODE | varchar(10) | 선수 코드 |
| 3 | NAME | varchar(20) | 선수명 (한글) |
| 4 | TEAM | varchar(10) | 팀명/코드 |
| 5 | T_ID | varchar(4) | 팀 코드 (2자) |
| 6 | POS | varchar(2) | 포지션 코드 |
| 7 | POSITION | varchar(10) | 포지션명 (한글) |
| 8 | BACKNUM | varchar(4) | 등번호 |
| 9 | ENGNAME | varchar(50) | 영문명 |
| 10 | CNAME | varchar(30) | 한자명 |
| 11 | HITTYPE | varchar(20) | 투타유형 (한글) |
| 12 | BIRTH | varchar(8) | 생년월일 (YYYYMMDD) |
| 13 | HEIGHT | varchar(4) | 신장 (cm) |
| 14 | WEIGHT | varchar(4) | 체중 (kg) |
| 15 | INDATE | varchar(10) | 입단일 |
| 16 | PROMISE | varchar(20) | 계약금 |
| 17 | MONEY | varchar(20) | 연봉 |
| 18 | CAREER | nvarchar(200) | 경력 |
| 19 | DRAFT | varchar(50) | 드래프트 정보 |
| 20 | REG_DT | datetime | 등록일시 |

### 1.8 KBO_schedule (경기 일정) - 22컬럼
| # | 컬럼 | 타입 | 의미 | 비고 |
|---|------|------|------|------|
| 1 | gmkey | varchar(13) | 경기키 | **소문자** |
| 2 | game_flag | tinyint | 경기유형 | |
| 3 | end_flag | tinyint | 종료플래그 | |
| 4 | gamedate | char(8) | 경기일자 | |
| 5 | gyear | smallint | 시즌연도 | |
| 6 | gmonth | tinyint | 월 | |
| 7 | gday | tinyint | 일 | |
| 8 | gweek | varchar(3) | 요일 | |
| 9 | home | varchar(10) | 홈팀명 | |
| 10 | home_key | char(2) | 홈팀코드 | |
| 11 | visit | varchar(10) | 원정팀명 | |
| 12 | visit_key | char(2) | 원정팀코드 | |
| 13 | stadium | varchar(10) | 구장명 | |
| 14 | stadium_key | char(2) | 구장코드 | |
| 15 | dheader | tinyint | 더블헤더 | |
| 16 | hpcode | varchar(10) | 홈선발투수코드 | |
| 17 | vpcode | varchar(10) | 원정선발투수코드 | |
| 18 | gtime | varchar(5) | 경기시작시간 | |
| 19 | hscore | tinyint | 홈팀점수 | |
| 20 | vscore | tinyint | 원정팀점수 | |
| 21 | cancel_flag | bit | 취소여부 | |
| 22 | suspended_flag | bit | 서스펜디드여부 | |

---

## 2. 테이블 유형별 분류

### 2.1 경기 기록 (핵심)
| 테이블 | 컬럼수 | 존재 DB수 | 핵심 PK |
|--------|--------|----------|---------|
| GAMEINFO | 27 | 12 | GMKEY |
| GAMECONTAPP | 29 | 12 | GMKEY+GYEAR+SERNO |
| Hitter | 26 | 12 | GMKEY+GDAY+TB+PCODE |
| Pitcher | 36 | 12 | GMKEY+GDAY+TB+PCODE |
| Score | 60 | 12 | GMKEY+GDAY |
| ENTRY | 11~12 | 12 | GMKEY+GYEAR+TURN+PCODE+POSI |
| DEFEN | 12 | 2 | (없음-비정규) |
| BatTotal | 22~23 | 12 | GYEAR+PCODE+SEC |
| PitTotal | 21~22 | 12 | GYEAR+PCODE+SEC |
| TeamRank | 29~30 | 12 | TEAM+GYEAR |

### 2.2 상세 기록 (DB2 전용)
| 테이블 | 컬럼수 | 설명 |
|--------|--------|------|
| KBO_BATRESULT | 65~90 | 이닝별 타격결과 |
| KBO_PITRESULT | 23 | 투수 경기결과 |
| KBO_ETCGAME | 5 | 기타 경기기록 |
| PITCHCLOCK | 19 | 피치클락 위반 |
| GAMEINFO_WEATHER | 12 | 기상 상세 |
| GAME_HR | 15 | 홈런 상세 (신세대) |
| GAME_MEMO | 20 | 경기 메모 (신세대) |
| GAME_MEMO_PITCHCLOCK | 16 | 피치클락 메모 |

### 2.3 기록입력(IE) 시스템
| 테이블 | 컬럼수 | 설명 |
|--------|--------|------|
| IE_LiveText | 7 | 실시간 문자중계 |
| IE_BatterRecord | 25 | 타자 기록입력 |
| IE_PitcherRecord | 22 | 투수 기록입력 |
| IE_BallCount | 11 | 볼카운트 |
| IE_GameList | 6 | 경기 목록 |
| IE_GAMESTATE | 5 | 경기 상태 |
| IE_Scoreinning | 5 | 이닝별 스코어 |
| IE_ScoreRHEB | 7 | R/H/E/B 합산 |
| IE_log | 3 | 입력 로그 |

### 2.4 마스터/참조
| 테이블 | 컬럼수 | 설명 |
|--------|--------|------|
| person | 20 | 선수 마스터 (시즌별) |
| person2 | 17 | 선수 마스터 (보조) |
| PERSON (2군) | 16 | 2군 선수 마스터 |
| TEAM | 7 | 팀 마스터 (시즌별) |
| STADIUM | 3 | 구장 마스터 (시즌별) |
| PERSON_FA | 4 | FA 선수 |
| PERSON_BASE | 6 | 가을리그 선수 기본 |
| CANCEL_GAME | 6 | 취소 경기 |
| BROADCASTING_CD | 2 | 방송사 코드 |

### 2.5 시즌 통계
| 테이블 | 컬럼수 | 설명 |
|--------|--------|------|
| SEASON_PLAYER_HITTER | 43~46 | 시즌 타자 통계 |
| SEASON_PLAYER_PITCHER | 54~59 | 시즌 투수 통계 |
| SEASON_PLAYER_HITTER_SITUATION | 14 | 상황별 타자 |
| SEASON_PLAYER_PITCHER_SITUATION | 14 | 상황별 투수 |
| SEASON_TEAM_HITTER | 37 | 팀 타격 통계 |
| SEASON_TEAM_PITCHER | 38 | 팀 투구 통계 |

### 2.6 일정/중계
| 테이블 | 컬럼수 | 설명 |
|--------|--------|------|
| KBO_schedule | 15~22 | 경기 일정 |
| BROADCASTING_RATE | 23 | 시청률 |
| BROADCASTING_RATE_MINOR | 21 | 2군 시청률 |
| BROADCASTING_schedule | 22 | 중계 편성 |
| BROADCASTING_schedule_minor | 20 | 2군 중계 편성 |

### 2.7 가을리그 전용
| 테이블 | 컬럼수 | 설명 |
|--------|--------|------|
| GAME_KBO | 24 | 경기 정보 (신세대) |
| GAME_PLAYER_HITTER | 31 | 경기별 타자 |
| GAME_PLAYER_PITCHER | 38 | 경기별 투수 |
| GAME_TEAM_HITTER | 24 | 팀 타격 |
| GAME_TEAM_PITCHER | 24 | 팀 투구 |
| FALL_LEAGUE_RECORD | 20 | 가을리그 기록 |

---

## 3. 컬럼 유형별 분류

### 3.1 동일 의미 컬럼의 DB간 타입 차이
| 컬럼명 | DB2_BASEBALL | DB1_BASEBALL | DB2_MINOR | 비고 |
|--------|-------------|-------------|-----------|------|
| GDAY | int | int | char(8) | 타입 혼재 |
| GYEAR | smallint | smallint | smallint | 일관 |
| ONETURN | smallint | int | smallint | 타입 차이 |
| DBHD | tinyint | tinyint | char(1) | 타입 차이 |

### 3.2 공통 컬럼 출현 빈도 (상위 20개)
| 컬럼명 | 출현 테이블 수 | 의미 |
|--------|--------------|------|
| GMKEY/gmkey | 30+ | 경기키 |
| GDAY/gday | 20+ | 경기일자 |
| GYEAR/gyear | 15+ | 시즌연도 |
| PCODE | 15+ | 선수코드 |
| TB | 10+ | 팀구분 |
| NAME | 10+ | 선수명 |
| TEAM | 10+ | 팀명/코드 |
| HIT | 8+ | 안타 |
| HR | 8+ | 홈런 |
| BB | 8+ | 볼넷 |
| KK | 8+ | 삼진 |
| AB | 8+ | 타수 |
| RUN | 8+ | 득점 |
| RBI | 6+ | 타점 |
| INN | 6+ | 이닝 |
| SB | 6+ | 도루 |
| ERR | 6+ | 실책 |
| H2 | 6+ | 2루타 |
| H3 | 6+ | 3루타 |
| POSITION | 5+ | 포지션 |

---

## 4. 데이터 품질 이슈

1. **인코딩 혼재**: varchar 한글 = EUC-KR, nvarchar 한글 = Unicode
2. **타입 불일치**: 동일 컬럼이 DB마다 다른 타입 (int vs char, smallint vs tinyint)
3. **PK 부재**: 일부 테이블에 명시적 PK 없음 (DEFEN, GAMEINFO 일부)
4. **FK 미설정**: 테이블간 참조 무결성 제약 없음 (모든 DB)
5. **특수값 혼용**: PCODE에 'T'/'B' 사용 (합계행), 숫자 코드 체계와 혼재
6. **NULL vs 빈문자열**: 동일 의미로 혼용 (person.PROMISE 등)
