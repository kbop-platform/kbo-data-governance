/* === KBO DataHub - Login Gate === */
/* 계정 변경: python3 -c "import hashlib; print(hashlib.sha256(b'아이디:비밀번호').hexdigest())" */

(function () {
  var HASH = '31f5fb453a215d6cb849a0c7d34238f25b33d9309cb3a159527ea3287b22370e';
  var KEY = 'kbo-ds-auth';
  var authenticated = sessionStorage.getItem(KEY) === HASH;

  if (authenticated) {
    document.documentElement.setAttribute('data-authed', '');
  }

  async function sha256(msg) {
    var buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(msg));
    return Array.from(new Uint8Array(buf)).map(function (b) { return b.toString(16).padStart(2, '0'); }).join('');
  }

  function getBaseUrl() {
    var scripts = document.getElementsByTagName('script');
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].src || '';
      var idx = src.indexOf('assets/js/auth.js');
      if (idx !== -1) return src.substring(0, idx);
    }
    return './';
  }

  function addLogoutButton() {
    var header = document.querySelector('.md-header__inner');
    if (!header) return;

    /* DataHub 타이틀 클릭 → 홈 이동 */
    var titleEl = document.querySelector('.md-header__title');
    if (titleEl) {
      titleEl.style.cursor = 'pointer';
      titleEl.addEventListener('click', function () {
        window.location.href = getBaseUrl();
      });
    }

    /* 로그아웃 버튼 */
    var btn = document.createElement('button');
    btn.className = 'md-header__button logout-btn';
    btn.title = 'Logout';
    btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"/></svg>';
    btn.addEventListener('click', function () {
      sessionStorage.removeItem(KEY);
      location.reload();
    });

    /* 팔레트 토글(다크/라이트)을 검색과 로그아웃 사이에 배치 */
    var paletteForm = document.querySelector('[data-md-component="palette"]');
    if (paletteForm) {
      header.appendChild(paletteForm);
    }
    header.appendChild(btn);
  }

  function showLogin() {
    var overlay = document.createElement('div');
    overlay.id = 'auth-overlay';
    var personIcon = '<svg class="auth-field-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>';
    var lockIcon = '<svg class="auth-field-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>';

    overlay.innerHTML = [
      '<div class="auth-card">',
      '  <img class="auth-logo-img" src="' + getBaseUrl() + 'assets/images/kbo-logo.png" alt="KBO">',
      '  <h1 class="auth-title">KBO DataHub</h1>',
      '  <p class="auth-subtitle">Data Catalog &amp; Governance Platform</p>',
      '  <form id="auth-form">',
      '    <div class="auth-field">',
      '      <input type="text" id="auth-id" placeholder="ID" autocomplete="off" autofocus>',
      '      ' + personIcon,
      '    </div>',
      '    <div class="auth-field">',
      '      <input type="password" id="auth-pw" placeholder="Password" autocomplete="off">',
      '      ' + lockIcon,
      '    </div>',
      '    <button type="submit" class="auth-btn">Sign In</button>',
      '    <p id="auth-error" class="auth-error"></p>',
      '  </form>',
      '  <div class="auth-footer">',
      '    <p class="auth-footer-label">Authorized personnel only</p>',
      '    <p class="auth-footer-copy">&copy; 2026 KBOP Data Biz Team</p>',
      '  </div>',
      '</div>'
    ].join('\n');

    document.body.innerHTML = '';
    document.body.appendChild(overlay);
    document.documentElement.style.visibility = 'visible';

    document.getElementById('auth-form').addEventListener('submit', async function (e) {
      e.preventDefault();
      var id = document.getElementById('auth-id').value;
      var pw = document.getElementById('auth-pw').value;
      var hash = await sha256(id + ':' + pw);
      if (hash === HASH) {
        sessionStorage.setItem(KEY, HASH);
        location.reload();
      } else {
        var err = document.getElementById('auth-error');
        err.textContent = 'ID 또는 비밀번호가 올바르지 않습니다.';
        document.getElementById('auth-pw').value = '';
        document.getElementById('auth-pw').focus();
        err.classList.add('shake');
        setTimeout(function () { err.classList.remove('shake'); }, 500);
      }
    });
  }

  window.addEventListener('DOMContentLoaded', function () {
    if (authenticated) {
      addLogoutButton();
    } else {
      showLogin();
    }
  });
})();
