/* === KBO Data Standards — Password Gate === */
/* 비밀번호 변경: python3 -c "import hashlib; print(hashlib.sha256(b'새비밀번호').hexdigest())" */

(function () {
  var HASH = '8b4640a8317afd3cec39a4f6aa7571dc1cb091f66da8eb6a6ad08e2d7194307a';
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
      '  <p class="auth-desc">문서 열람을 위해 비밀번호를 입력하세요.</p>',
      '  <form id="auth-form">',
      '    <div class="auth-input-wrap">',
      '      <input type="password" id="auth-pw" placeholder="Password" autocomplete="off" autofocus>',
      '    </div>',
      '    <button type="submit" class="auth-btn">Enter</button>',
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
      var pw = document.getElementById('auth-pw').value;
      var hash = await sha256(pw);
      if (hash === HASH) {
        sessionStorage.setItem(KEY, HASH);
        location.reload();
      } else {
        var err = document.getElementById('auth-error');
        err.textContent = '비밀번호가 올바르지 않습니다.';
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
