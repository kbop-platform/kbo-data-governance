/* === KBO Data Standards — Login Gate === */
/* 계정 변경: python3 -c "import hashlib; print(hashlib.sha256(b'아이디:비밀번호').hexdigest())" */

(function () {
  var HASH = '31f5fb453a215d6cb849a0c7d34238f25b33d9309cb3a159527ea3287b22370e';
  var KEY = 'kbo-ds-auth';

  if (sessionStorage.getItem(KEY) === HASH) return;

  /* ── 페이지 콘텐츠 숨기기 ── */
  document.documentElement.style.visibility = 'hidden';

  async function sha256(msg) {
    var buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(msg));
    return Array.from(new Uint8Array(buf)).map(function (b) { return b.toString(16).padStart(2, '0'); }).join('');
  }

  window.addEventListener('DOMContentLoaded', function () {
    document.documentElement.style.visibility = 'hidden';

    var overlay = document.createElement('div');
    overlay.id = 'auth-overlay';
    overlay.innerHTML = [
      '<div class="auth-card">',
      '  <div class="auth-logo">',
      '    <img src="' + getBaseUrl() + 'assets/images/kbo-logo.png" alt="KBO">',
      '  </div>',
      '  <h1 class="auth-title">Data Standards</h1>',
      '  <p class="auth-desc">문서 열람을 위해 로그인하세요.</p>',
      '  <form id="auth-form">',
      '    <div class="auth-input-wrap">',
      '      <input type="text" id="auth-id" placeholder="ID" autocomplete="off" autofocus>',
      '    </div>',
      '    <div class="auth-input-wrap">',
      '      <input type="password" id="auth-pw" placeholder="Password" autocomplete="off">',
      '    </div>',
      '    <button type="submit" class="auth-btn">Login</button>',
      '    <p id="auth-error" class="auth-error"></p>',
      '  </form>',
      '  <p class="auth-footer">&copy; 2026 KBOP Data Biz Team</p>',
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
  });

  function getBaseUrl() {
    var scripts = document.getElementsByTagName('script');
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].src || '';
      var idx = src.indexOf('assets/js/auth.js');
      if (idx !== -1) return src.substring(0, idx);
    }
    return './';
  }
})();
