---
hide:
  - toc
---

<div class="sl-landing">

<!-- Dictionary Sub-Tabs -->
<div class="catalog-tabs">
  <a href="../standards-dict/glossary/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M1 2.828c.885-.37 2.154-.769 3.388-.893C5.33 1.827 6.16 1.882 6.84 2.28c.142.083.27.177.382.28.113-.103.24-.197.382-.28C8.283 1.882 9.114 1.827 10.056 1.935c1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687c-.935-.531-2.12-.603-3.213-.492C2.663 2.307 1.474 2.649.556 3v9.75A.5.5 0 0 1 0 12.5v-10a.5.5 0 0 1 .336-.472z"/></svg></span> 용어 사전 <span class="tab-count">134</span></a>
  <a href="../standards-dict/abbreviations/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H2zm1.5 3h2.104l1.573 4.636h.06L8.81 4h2.104v8H9.485V7.168h-.046L8.03 11.58H6.89L5.48 7.138h-.046V12H4.006V4H3.5z"/></svg></span> 약어 사전 <span class="tab-count">118</span></a>
  <a href="../standards-dict/domains/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8l3.147-3.146zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8l-3.147-3.146z"/></svg></span> 도메인 사전 <span class="tab-count">93</span></a>
  <a href="../standards-dict/codes/"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M8.39 12.648a1.32 1.32 0 0 0-.015.18c0 .305.21.508.5.508.266 0 .492-.172.555-.477l.554-2.703h1.204c.421 0 .617-.234.617-.547 0-.312-.188-.53-.617-.53h-.985l.516-2.524h1.265c.43 0 .618-.227.618-.547 0-.313-.188-.532-.618-.532h-1.046l.476-2.304a1.06 1.06 0 0 0 .016-.164.51.51 0 0 0-.516-.516.54.54 0 0 0-.539.43l-.523 2.554H7.617l.477-2.304c.008-.04.015-.118.015-.164a.512.512 0 0 0-.523-.516.539.539 0 0 0-.531.43L6.53 5.484H5.414c-.43 0-.617.22-.617.532 0 .312.187.539.617.539h.906l-.515 2.523H4.609c-.421 0-.609.219-.609.531 0 .313.188.547.61.547h.985l-.516 2.304c-.008.04-.015.118-.015.163 0 .305.21.508.5.508.266 0 .492-.172.554-.477l.555-2.498h2.078l-.555 2.492zm.508-3.649a1855.5 1855.5 0 0 1-.062.289h-2.078l.515-2.523h2.086l-.461 2.234z"/></svg></span> 코드 사전 <span class="tab-count">168</span></a>
  <a href="./" class="active"><span class="tab-icon"><svg width="12" height="12" viewBox="0 0 16 16" fill="currentColor"><path d="M3 4.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1zm0 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1z"/></svg></span> 사전 상세 <span class="tab-count">39</span></a>
</div>

<div class="sl-hero">
  <div class="sl-hero-title">데이터 사전</div>
  <div class="sl-hero-desc">KBO 운영 데이터베이스 39개 테이블, 787개 컬럼 정의서</div>
</div>

<div class="sl-group-title">경기 기록</div>

<div class="sl-cards">

  <a class="sl-card" href="game/GAMEINFO/">
    <div class="sl-card-head">
      <div class="sl-card-title">GAMEINFO</div>
      <span class="sl-card-type">경기 정보</span>
    </div>
    <p class="sl-card-desc">경기 기본 정보 (날짜, 구장, 팀, 관중, 심판 등). 전체 도메인의 기준 테이블.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">42컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/Hitter/">
    <div class="sl-card-head">
      <div class="sl-card-title">Hitter</div>
      <span class="sl-card-type">타자 기록</span>
    </div>
    <p class="sl-card-desc">경기별 타자 성적 (타수, 안타, 홈런, 타점, 도루 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + player_id</span>
      <span class="sl-card-tag">40컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/Pitcher/">
    <div class="sl-card-head">
      <div class="sl-card-title">Pitcher</div>
      <span class="sl-card-type">투수 기록</span>
    </div>
    <p class="sl-card-desc">경기별 투수 성적 (이닝, 피안타, 삼진, 자책점 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + player_id</span>
      <span class="sl-card-tag">40컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/Score/">
    <div class="sl-card-head">
      <div class="sl-card-title">Score</div>
      <span class="sl-card-type">이닝 스코어</span>
    </div>
    <p class="sl-card-desc">이닝별 득점 현황 (1~25회, R/H/E/B 포함).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + top_bottom</span>
      <span class="sl-card-tag">55컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/ENTRY/">
    <div class="sl-card-head">
      <div class="sl-card-title">ENTRY</div>
      <span class="sl-card-type">출전 엔트리</span>
    </div>
    <p class="sl-card-desc">경기 출전 선수 명단 (타순, 포지션, 교체 정보).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + player_id</span>
      <span class="sl-card-tag">11컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/DEFEN/">
    <div class="sl-card-head">
      <div class="sl-card-title">DEFEN</div>
      <span class="sl-card-type">수비 기록</span>
    </div>
    <p class="sl-card-desc">경기별 수비 기록 (자살, 병살, 실책 등 포지션별).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">12컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/GAMECONTAPP/">
    <div class="sl-card-head">
      <div class="sl-card-title">GAMECONTAPP</div>
      <span class="sl-card-type">경기 상세 기록</span>
    </div>
    <p class="sl-card-desc">투구 단위 상세 기록 (HOW, 주자 상황, 타구 방향 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + seq_no</span>
      <span class="sl-card-tag">29컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/GAME_HR/">
    <div class="sl-card-head">
      <div class="sl-card-title">GAME_HR</div>
      <span class="sl-card-type">홈런 기록</span>
    </div>
    <p class="sl-card-desc">홈런 상세 기록 (비거리, 발사각, 착지점 좌표 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">14컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/GAME_MEMO/">
    <div class="sl-card-head">
      <div class="sl-card-title">GAME_MEMO</div>
      <span class="sl-card-type">경기 메모</span>
    </div>
    <p class="sl-card-desc">경기 운영 메모 (선발 투수, 주심, 특이사항 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">17컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/GAME_MEMO_PITCHCLOCK/">
    <div class="sl-card-head">
      <div class="sl-card-title">GAME_MEMO_PITCHCLOCK</div>
      <span class="sl-card-type">피치클럭 메모</span>
    </div>
    <p class="sl-card-desc">피치클럭 위반 기록 (위반 선수, 팀, 판정 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + seq_no</span>
      <span class="sl-card-tag">14컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/PITCHCLOCK/">
    <div class="sl-card-head">
      <div class="sl-card-title">PITCHCLOCK</div>
      <span class="sl-card-type">피치클럭 설정</span>
    </div>
    <p class="sl-card-desc">시즌별 피치클럭 시간 기준 설정값.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">season_yr</span>
      <span class="sl-card-tag">10컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="game/GAMEINFO_WEATHER/">
    <div class="sl-card-head">
      <div class="sl-card-title">GAMEINFO_WEATHER</div>
      <span class="sl-card-type">경기 날씨</span>
    </div>
    <p class="sl-card-desc">경기 당일 기상 데이터 (기온, 습도, 풍향, 풍속 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">22컬럼</span>
    </div>
  </a>

</div>

<div class="sl-group-title">통계</div>

<div class="sl-cards">

  <a class="sl-card" href="stats/BatTotal/">
    <div class="sl-card-head">
      <div class="sl-card-title">BatTotal</div>
      <span class="sl-card-type">타격 합산</span>
    </div>
    <p class="sl-card-desc">시즌/통산 타격 합산 통계 (타율, OPS 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id + season_yr</span>
      <span class="sl-card-tag">31컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/PitTotal/">
    <div class="sl-card-head">
      <div class="sl-card-title">PitTotal</div>
      <span class="sl-card-type">투구 합산</span>
    </div>
    <p class="sl-card-desc">시즌/통산 투구 합산 통계 (ERA, WHIP 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id + season_yr</span>
      <span class="sl-card-tag">50컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/TeamRank/">
    <div class="sl-card-head">
      <div class="sl-card-title">TeamRank</div>
      <span class="sl-card-type">팀 순위</span>
    </div>
    <p class="sl-card-desc">시즌별 팀 순위, 승패, 승률, 게임차.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">team_cd + season_yr</span>
      <span class="sl-card-tag">16컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/KBO_BATRESULT/">
    <div class="sl-card-head">
      <div class="sl-card-title">KBO_BATRESULT</div>
      <span class="sl-card-type">이닝별 타격</span>
    </div>
    <p class="sl-card-desc">이닝 구간별 타격 세부 기록 (1~25회).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + player_id</span>
      <span class="sl-card-tag">251컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/KBO_PITRESULT/">
    <div class="sl-card-head">
      <div class="sl-card-title">KBO_PITRESULT</div>
      <span class="sl-card-type">이닝별 투구</span>
    </div>
    <p class="sl-card-desc">이닝 구간별 투구 세부 기록 (1~25회).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id + player_id</span>
      <span class="sl-card-tag">36컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/KBO_ETCGAME/">
    <div class="sl-card-head">
      <div class="sl-card-title">KBO_ETCGAME</div>
      <span class="sl-card-type">기타 경기 통계</span>
    </div>
    <p class="sl-card-desc">기타 경기 관련 통계 데이터.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">5컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/SEASON_PLAYER_HITTER/">
    <div class="sl-card-head">
      <div class="sl-card-title">SEASON_PLAYER_HITTER</div>
      <span class="sl-card-type">시즌 타자 통계</span>
    </div>
    <p class="sl-card-desc">시즌 타자 개인 통계 (경기수, 타석, 안타 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id + season_yr</span>
      <span class="sl-card-tag">16컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/SEASON_PLAYER_HITTER_SITUATION/">
    <div class="sl-card-head">
      <div class="sl-card-title">SEASON_PLAYER_HITTER_SITUATION</div>
      <span class="sl-card-type">상황별 타자</span>
    </div>
    <p class="sl-card-desc">상황별(주자, 아웃카운트 등) 타자 세부 통계.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id + section</span>
      <span class="sl-card-tag">8컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/SEASON_PLAYER_PITCHER/">
    <div class="sl-card-head">
      <div class="sl-card-title">SEASON_PLAYER_PITCHER</div>
      <span class="sl-card-type">시즌 투수 통계</span>
    </div>
    <p class="sl-card-desc">시즌 투수 개인 통계 (승패, 이닝, ERA 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id + season_yr</span>
      <span class="sl-card-tag">31컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="stats/SEASON_PLAYER_PITCHER_SITUATION/">
    <div class="sl-card-head">
      <div class="sl-card-title">SEASON_PLAYER_PITCHER_SITUATION</div>
      <span class="sl-card-type">상황별 투수</span>
    </div>
    <p class="sl-card-desc">상황별(주자, 아웃카운트 등) 투수 세부 통계.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id + section</span>
      <span class="sl-card-tag">8컬럼</span>
    </div>
  </a>

</div>

<div class="sl-group-title">실시간</div>

<div class="sl-cards">

  <a class="sl-card" href="realtime/IE_LiveText/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_LiveText</div>
      <span class="sl-card-type">문자 중계</span>
    </div>
    <p class="sl-card-desc">실시간 문자 중계 데이터 (투구, 타격, 주루 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID + seqNo</span>
      <span class="sl-card-tag">9컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_BallCount/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_BallCount</div>
      <span class="sl-card-type">볼카운트</span>
    </div>
    <p class="sl-card-desc">현재 볼/스트라이크/아웃 카운트 상태.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID</span>
      <span class="sl-card-tag">16컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_BatterRecord/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_BatterRecord</div>
      <span class="sl-card-type">타자 실시간</span>
    </div>
    <p class="sl-card-desc">경기 중 타자 누적 기록 (타수, 안타, 타율 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID + PlayerID</span>
      <span class="sl-card-tag">12컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_PitcherRecord/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_PitcherRecord</div>
      <span class="sl-card-type">투수 실시간</span>
    </div>
    <p class="sl-card-desc">경기 중 투수 누적 기록 (이닝, 투구수, ERA 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID + PlayerID</span>
      <span class="sl-card-tag">26컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_GAMESTATE/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_GAMESTATE</div>
      <span class="sl-card-type">경기 상태</span>
    </div>
    <p class="sl-card-desc">경기 진행 상태 (이닝, 공수, 점수 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">GAMEID</span>
      <span class="sl-card-tag">9컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_ScoreRHEB/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_ScoreRHEB</div>
      <span class="sl-card-type">R/H/E/B 요약</span>
    </div>
    <p class="sl-card-desc">팀별 득점/안타/실책/볼넷 요약 스코어.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID</span>
      <span class="sl-card-tag">9컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_Scoreinning/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_Scoreinning</div>
      <span class="sl-card-type">이닝 점수</span>
    </div>
    <p class="sl-card-desc">이닝별 점수 현황 (1~연장 이닝).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID + inn</span>
      <span class="sl-card-tag">5컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_GameList/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_GameList</div>
      <span class="sl-card-type">경기 목록</span>
    </div>
    <p class="sl-card-desc">당일 경기 목록 (시간, 구장, 팀 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">gameID</span>
      <span class="sl-card-tag">7컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="realtime/IE_log/">
    <div class="sl-card-head">
      <div class="sl-card-title">IE_log</div>
      <span class="sl-card-type">시스템 로그</span>
    </div>
    <p class="sl-card-desc">실시간 데이터 처리 시스템 로그.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">logDate</span>
      <span class="sl-card-tag">3컬럼</span>
    </div>
  </a>

</div>

<div class="sl-group-title">마스터</div>

<div class="sl-cards">

  <a class="sl-card" href="master/person/">
    <div class="sl-card-head">
      <div class="sl-card-title">person</div>
      <span class="sl-card-type">선수 마스터</span>
    </div>
    <p class="sl-card-desc">1군 선수 기본 정보 (이름, 생년월일, 포지션, 팀 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id</span>
      <span class="sl-card-tag">20컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/person2/">
    <div class="sl-card-head">
      <div class="sl-card-title">person2</div>
      <span class="sl-card-type">선수 마스터 (구버전)</span>
    </div>
    <p class="sl-card-desc">1군 선수 마스터 구버전. person 대비 ENGNAME/DRAFT/REG_DT 없음.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id</span>
      <span class="sl-card-tag">17컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/PERSON/">
    <div class="sl-card-head">
      <div class="sl-card-title">PERSON</div>
      <span class="sl-card-type">2군 선수 마스터</span>
    </div>
    <p class="sl-card-desc">2군(퓨처스리그) 선수 기본 정보.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id</span>
      <span class="sl-card-tag">16컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/PERSON_FA/">
    <div class="sl-card-head">
      <div class="sl-card-title">PERSON_FA</div>
      <span class="sl-card-type">FA 계약</span>
    </div>
    <p class="sl-card-desc">FA(자유계약) 선수 계약 정보.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">player_id</span>
      <span class="sl-card-tag">4컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/TEAM/">
    <div class="sl-card-head">
      <div class="sl-card-title">TEAM</div>
      <span class="sl-card-type">팀 마스터</span>
    </div>
    <p class="sl-card-desc">KBO 구단 기본 정보 (팀명, 연고지, 감독 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">team_cd + season_yr</span>
      <span class="sl-card-tag">13컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/STADIUM/">
    <div class="sl-card-head">
      <div class="sl-card-title">STADIUM</div>
      <span class="sl-card-type">구장 마스터</span>
    </div>
    <p class="sl-card-desc">야구장 기본 정보 (구장명, 소재지 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">stadium_cd</span>
      <span class="sl-card-tag">3컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/KBO_schedule/">
    <div class="sl-card-head">
      <div class="sl-card-title">KBO_schedule</div>
      <span class="sl-card-type">경기 일정</span>
    </div>
    <p class="sl-card-desc">시즌 경기 일정 (날짜, 시간, 구장, 대진 등).</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">39컬럼</span>
    </div>
  </a>

  <a class="sl-card" href="master/CANCEL_GAME/">
    <div class="sl-card-head">
      <div class="sl-card-title">CANCEL_GAME</div>
      <span class="sl-card-type">취소 경기</span>
    </div>
    <p class="sl-card-desc">우천/기타 사유로 취소된 경기 기록.</p>
    <div class="sl-card-meta">
      <span class="sl-card-tag">game_id</span>
      <span class="sl-card-tag">5컬럼</span>
    </div>
  </a>

</div>

---

<details class="dict-reference" markdown>
<summary>데이터 흐름도</summary>

```
                                                    경기 당일 전송
┌─────────────────┐                         ┌──────────────────┐
│  S2i 운영 DB     │ ─────────────────────→  │  DB2 (시즌 13개)  │
│  (Sports2i 외주) │                         │  시즌별 경기 데이터 │
└─────────────────┘                         └────────┬─────────┘
                                                     │ 확정 후 반영
                                                     ▼
                                             ┌──────────────────┐
                                             │  DB1 (영구 4개)    │
                                             │  누적/마스터 데이터 │
                                             └──────────────────┘
                                                    KBO 자체 구축
┌─────────────────┐                         ┌──────────────────┐
│  KBO 분석팀      │ ─────────────────────→  │  KBO 자체 DB      │
│  (내부)          │                         │  세이버/P-b-P 등   │
└─────────────────┘                         └──────────────────┘
```

- **DB2**: 경기 당일 S2i가 전송. 시즌 데이터
- **DB1**: DB2 확정 후 반영. 영구/누적
- **KBO 자체**: 세이버메트릭스, pitch-by-pitch 등 S2i 미제공 데이터

</details>

<details class="dict-reference" markdown>
<summary>테이블 간 주요 관계</summary>

**핵심 FK 관계**

```
GAME_INFO (game_id)
  ├── HITTER         (game_id, season_yr, player_id)
  ├── PITCHER         (game_id, season_yr, player_id)
  ├── SCORE           (game_id, season_yr, top_bottom_cd)
  ├── GAME_CONT_APP   (game_id, season_yr, seq_no)
  ├── ENTRY           (game_id, season_yr, turn_no, player_id, position_cd)
  ├── DEFEN           (game_id, season_yr)
  ├── GAME_HR         (game_id)
  └── GAME_MEMO       (game_id)

PERSON (player_id)
  ├── HITTER         (player_id)
  ├── PITCHER         (player_id)
  ├── ENTRY           (player_id)
  ├── BAT_TOTAL       (player_id)
  └── PIT_TOTAL       (player_id)

TEAM (team_id, season_id)
  ├── TEAM_RANK       (team_cd, season_yr)
  └── GAME_INFO       (home_team_cd, away_team_cd)
```

**실시간 테이블 관계**

실시간(IE_*) 테이블은 독립적으로 운영되며, `gameID`(=game_id)로 경기 기록 도메인과 연결.

```
IE_LIVE_TEXT (gameID) ← 실시간 문자 중계
IE_BALL_COUNT (gameID) ← 볼카운트 현재 상태
IE_BATTER_RECORD (gameID, PlayerID) ← 타자 누적
IE_PITCHER_RECORD (gameID, PlayerID) ← 투수 누적
IE_GAME_STATE (GAMEID) ← 경기 상태
IE_SCORE_RHEB (gameID) ← R/H/E/B 요약
IE_SCORE_INNING (gameID) ← 이닝 점수
IE_GAME_LIST (gameID) ← 당일 경기 목록
IE_LOG ← 시스템 로그 (FK 없음)
```

</details>

<details class="dict-reference" markdown>
<summary>참고 문서</summary>

- [데이터 프로덕트](products/game-summary.md): 비즈니스 단위별 데이터 구조
- [데이터 리니지](lineage.md): 데이터 흐름 추적, 영향도 분석
- [표준 명명 규칙](../standards/naming-rules.md): 레거시 → 표준 변환 규칙
- [ID 체계](../standards/id-system.md): game_id, player_id 등 6종 ID 정의
- [도메인 사전](../standards-dict/domains.md): 접미사별 MSSQL 타입 매핑
- [코드 사전](../standards-dict/codes.md): how_cd, place_cd 등 코드값
- [업무 용어 사전](../glossary/business-terms.md): 용어 정의 ~165개
- [컬럼 매핑](../migration/column-mapping.md): AS-IS → TO-BE 컬럼 전수 매핑

</details>

</div>
