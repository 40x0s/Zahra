/* Ethical Hacking Study Pack — shared behaviour
   لغة العرض + التمرير + الطباعة */
(function () {
  var KEY = 'eh-lang-mode';

  function applyMode(m) {
    document.body.classList.remove('only-en', 'only-ar');
    if (m === 'en') document.body.classList.add('only-en');
    if (m === 'ar') document.body.classList.add('only-ar');
    document.querySelectorAll('[data-lang-btn]').forEach(function (b) {
      b.classList.toggle('primary', b.getAttribute('data-lang-btn') === m);
    });
    var sel = document.getElementById('langSel');
    if (sel) sel.value = m;
  }

  window.setLangMode = function (m) {
    try { localStorage.setItem(KEY, m); } catch (e) {}
    applyMode(m);
  };

  document.addEventListener('DOMContentLoaded', function () {
    var saved = 'both';
    try { saved = localStorage.getItem(KEY) || 'both'; } catch (e) {}
    applyMode(saved);

    document.querySelectorAll('[data-lang-btn]').forEach(function (b) {
      b.addEventListener('click', function () { window.setLangMode(b.getAttribute('data-lang-btn')); });
    });
    var sel = document.getElementById('langSel');
    if (sel) sel.addEventListener('change', function () { window.setLangMode(sel.value); });

    document.querySelectorAll('[data-print]').forEach(function (b) {
      b.addEventListener('click', function () { window.print(); });
    });

    // highlight current nav link
    var here = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav a').forEach(function (a) {
      if (a.getAttribute('href') === here) a.classList.add('active');
    });

    // side-nav scroll spy
    var links = Array.prototype.slice.call(document.querySelectorAll('.sidenav a[href^="#"]'));
    if (links.length) {
      var targets = links.map(function (a) { return document.querySelector(a.getAttribute('href')); }).filter(Boolean);
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            links.forEach(function (l) { l.style.background = ''; l.style.color = ''; });
            var act = links.find(function (l) { return l.getAttribute('href') === '#' + en.target.id; });
            if (act) { act.style.background = 'var(--panel-2)'; act.style.color = 'var(--txt)'; }
          }
        });
      }, { rootMargin: '-90px 0px -70% 0px' });
      targets.forEach(function (t) { io.observe(t); });
    }
  });
})();

/* ---------------- Quiz engine ---------------- */
(function () {
  var answered = {}, total = 0;

  function updateScore() {
    var el = document.getElementById('score');
    if (!el) return;
    var keys = Object.keys(answered);
    var right = keys.filter(function (k) { return answered[k]; }).length;
    el.innerHTML = 'Score / النتيجة: <b>' + right + '</b> / ' + keys.length +
      ' <span style="opacity:.6">(of ' + total + ')</span>';
  }

  window.pickOption = function (optEl, qid, isCorrect) {
    var q = optEl.closest('.q');
    if (q.dataset.done === '1') return;
    q.dataset.done = '1';
    q.querySelectorAll('.opt').forEach(function (o) {
      o.classList.add('disabled');
      if (o.dataset.correct === '1') o.classList.add('correct');
    });
    if (!isCorrect) optEl.classList.add('wrong');
    q.querySelector('.answer').classList.add('show');
    answered[qid] = !!isCorrect;
    updateScore();
  };

  window.toggleAnswer = function (btn) {
    var a = btn.closest('.q').querySelector('.answer');
    a.classList.toggle('show');
    btn.textContent = a.classList.contains('show') ? 'Hide answer / إخفاء الإجابة' : 'Show answer / إظهار الإجابة';
  };

  window.revealAll = function () {
    document.querySelectorAll('.q').forEach(function (q) {
      q.querySelector('.answer').classList.add('show');
      q.querySelectorAll('.opt[data-correct="1"]').forEach(function (o) { o.classList.add('correct'); });
    });
  };

  window.resetQuiz = function () {
    answered = {};
    document.querySelectorAll('.q').forEach(function (q) {
      q.dataset.done = '';
      q.querySelector('.answer').classList.remove('show');
      q.querySelectorAll('.opt').forEach(function (o) {
        o.classList.remove('correct', 'wrong', 'disabled');
      });
      var b = q.querySelector('[data-toggle-ans]');
      if (b) b.textContent = 'Show answer / إظهار الإجابة';
    });
    updateScore();
  };

  window.filterQuiz = function (val) {
    document.querySelectorAll('.q').forEach(function (q) {
      q.classList.toggle('hidden', !(val === 'all' || q.dataset.ch === val));
    });
    document.querySelectorAll('.qsec').forEach(function (s) {
      s.classList.toggle('hidden', !(val === 'all' || s.dataset.ch === val));
    });
  };

  document.addEventListener('DOMContentLoaded', function () {
    // Only multiple-choice / True-False cards are auto-gradable.
    // Short-answer and scenario cards still reveal model answers but do not inflate the score denominator.
    total = Array.prototype.filter.call(document.querySelectorAll('.q'), function (q) {
      return !!q.querySelector('.opts');
    }).length;
    var t = document.getElementById('qTotal');
    if (t) t.textContent = total;
    updateScore();
    var f = document.getElementById('chFilter');
    if (f) f.addEventListener('change', function () { window.filterQuiz(f.value); });
  });
})();
