# -*- coding: utf-8 -*-
"""Builds site/quiz.html from tools/questions.py"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from questions import Q

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
KEYS = "ABCDEFGH"

CH_TITLES = {
    1: ("Chapter 1 — Introduction to Ethical Hacking", "الفصل الأول — مقدمة في الاختراق الأخلاقي"),
    2: ("Chapter 2 — Reconnaissance &amp; Footprinting", "الفصل الثاني — الاستطلاع وجمع المعلومات"),
    3: ("Chapter 3 — Scanning &amp; Enumeration", "الفصل الثالث — الفحص والتعداد"),
    4: ("Chapter 4 — Network Sniffing", "الفصل الرابع — التنصت على الشبكة"),
}

HEAD = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Expected Exam Questions | الأسئلة المتوقعة في الاختبار</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="index.html"><span class="logo">⚡</span><span>Ethical Hacking<small>الاختراق الأخلاقي — Study Pack</small></span></a>
    <nav class="nav">
      <a href="index.html">Home</a><a href="ch1.html">Ch 1</a><a href="ch2.html">Ch 2</a>
      <a href="ch3.html">Ch 3</a><a href="ch4.html">Ch 4</a><a href="predicted.html">Predicted Models</a><a href="exam.html">Solved Sample</a><a href="quiz.html">Question Bank</a><a href="cheatsheet.html">Cheat Sheet</a>
    </nav>
  </div>
</header>

<main class="wrap narrow">
  <div class="page-head">
    <span class="kicker">Exam Preparation · التحضير للاختبار</span>
    <h1>%(N)d Expected Exam Questions</h1>
    <p class="h1-ar">%(N)d سؤالاً متوقعاً في الاختبار</p>
    <p class="lede">Every question below is built <strong>only</strong> from facts that appear in the four lecture PDFs — nothing invented.
    Each one shows the exact <strong>slide reference</strong> so you can check it yourself. The exam is in <strong>English</strong>;
    the Arabic translation is only to help you understand the question.</p>
    <p class="lede lede-ar">كل سؤال هنا مبني <strong>حصراً</strong> على معلومات وردت في ملفات المحاضرات الأربعة — لا شيء مُختلَق.
    ويظهر مع كل سؤال <strong>رقم الشريحة</strong> لتتأكدي بنفسك. الاختبار باللغة <strong>الإنجليزية</strong>،
    والترجمة العربية فقط لمساعدتك على الفهم.</p>
  </div>

  <div class="note no-print">
    <div class="en"><b>How to use:</b> click an option to answer — the correct answer turns green instantly and the explanation appears.
      For True/False and short-answer questions, press “Show answer”. Use the filter to revise one chapter at a time.
      When you print, <b>all answers are shown automatically</b>.</div>
    <div class="ar"><b>طريقة الاستخدام:</b> اضغطي على الخيار للإجابة — تتحول الإجابة الصحيحة إلى اللون الأخضر فوراً ويظهر الشرح.
      وفي أسئلة صح/خطأ والإجابات القصيرة اضغطي «إظهار الإجابة». استخدمي الفلتر لمراجعة فصل واحد في كل مرة.
      وعند الطباعة <b>تظهر جميع الإجابات تلقائياً</b>.</div>
  </div>

  <div class="quiz-tools no-print">
    <label>Chapter · الفصل:
      <select id="chFilter">
        <option value="all">All chapters · كل الفصول (%(N)d)</option>
        <option value="1">Ch 1 · الفصل الأول (%(C1)d)</option>
        <option value="2">Ch 2 · الفصل الثاني (%(C2)d)</option>
        <option value="3">Ch 3 · الفصل الثالث (%(C3)d)</option>
        <option value="4">Ch 4 · الفصل الرابع (%(C4)d)</option>
      </select>
    </label>
    <label>Language:
      <select id="langSel">
        <option value="both">Both · الاثنان</option>
        <option value="en">English only</option>
        <option value="ar">العربية فقط</option>
      </select>
    </label>
    <button class="btn" onclick="revealAll()">Reveal all · إظهار الكل</button>
    <button class="btn" onclick="resetQuiz()">Reset · إعادة</button>
    <button class="btn primary" data-print>Print / PDF</button>
    <span class="score" id="score"></span>
  </div>
"""

FOOT = """
  <div class="pager no-print">
    <a class="btn" href="ch4.html">← Chapter 4 · الفصل الرابع</a>
    <a class="btn primary" href="cheatsheet.html">Cheat Sheet → الملخص</a>
  </div>
</main>

<footer>Expected exam questions · built from Chapters 1–4 · Eng. Zahra Rajeh, M.Sc.
  <div class="ar">الأسئلة المتوقعة · مبنية على الفصول ١–٤ · م. زهراء راجح</div></footer>

<script src="js/app.js"></script>
</body>
</html>
"""


def build():
    counts = {c: sum(1 for q in Q if q[1] == c) for c in (1, 2, 3, 4)}
    out = [HEAD % {"N": len(Q), "C1": counts[1], "C2": counts[2], "C3": counts[3], "C4": counts[4]}]

    n = 0
    cur_ch = None
    for item in Q:
        kind, ch, ref = item[0], item[1], item[2]
        if ch != cur_ch:
            cur_ch = ch
            te, ta = CH_TITLES[ch]
            out.append(f'\n  <div class="qsec" data-ch="{ch}"><h2>{te}</h2>'
                       f'<div class="ar">{ta}</div></div>\n')
        n += 1
        if kind == "mcq":
            _, _, _, qe, qa, opts, ci, ee, ea = item
            out.append(f'  <div class="q" data-ch="{ch}" data-done="">\n')
            out.append(f'    <div class="qhead"><span class="qn">Q{n}</span><span class="tag mcq">MCQ</span>'
                       f'<span class="qtext">{qe}</span></div>\n')
            out.append(f'    <div class="qtext-ar">{qa}</div>\n')
            out.append('    <div class="opts">\n')
            for i, (oe, oa) in enumerate(opts):
                corr = "1" if i == ci else "0"
                out.append(
                    f'      <div class="opt" data-correct="{corr}" '
                    f'onclick="pickOption(this,\'q{n}\',{"true" if i == ci else "false"})">'
                    f'<span class="k">{KEYS[i]}</span>'
                    f'<span class="txt"><span class="en">{oe}</span><span class="ar">{oa}</span></span></div>\n')
            out.append('    </div>\n')
            out.append(f'    <div class="row"><button class="btn ghost no-print" data-toggle-ans '
                       f'onclick="toggleAnswer(this)">Show answer / إظهار الإجابة</button>'
                       f'<span class="srcref">📄 {ref}</span></div>\n')
            out.append(f'    <div class="answer"><div class="lab">✔ Correct answer: {KEYS[ci]}) {opts[ci][0]}</div>'
                       f'<div class="en">{ee}</div><div class="ar">{ea}</div></div>\n')
            out.append('  </div>\n')
        elif kind == "tf":
            _, _, _, qe, qa, ans, ee, ea = item
            a_en = "TRUE" if ans else "FALSE"
            a_ar = "صحيح" if ans else "خطأ"
            out.append(f'  <div class="q" data-ch="{ch}" data-done="">\n')
            out.append(f'    <div class="qhead"><span class="qn">Q{n}</span><span class="tag tf">True / False</span>'
                       f'<span class="qtext">{qe}</span></div>\n')
            out.append(f'    <div class="qtext-ar">{qa}</div>\n')
            out.append('    <div class="opts">\n')
            for i, (oe, oa, val) in enumerate([("True", "صحيح", True), ("False", "خطأ", False)]):
                corr = "1" if val == ans else "0"
                out.append(
                    f'      <div class="opt" data-correct="{corr}" '
                    f'onclick="pickOption(this,\'q{n}\',{"true" if val == ans else "false"})">'
                    f'<span class="k">{KEYS[i]}</span>'
                    f'<span class="txt"><span class="en">{oe}</span><span class="ar">{oa}</span></span></div>\n')
            out.append('    </div>\n')
            out.append(f'    <div class="row"><button class="btn ghost no-print" data-toggle-ans '
                       f'onclick="toggleAnswer(this)">Show answer / إظهار الإجابة</button>'
                       f'<span class="srcref">📄 {ref}</span></div>\n')
            out.append(f'    <div class="answer"><div class="lab">✔ Correct answer: {a_en} · {a_ar}</div>'
                       f'<div class="en">{ee}</div><div class="ar">{ea}</div></div>\n')
            out.append('  </div>\n')
        else:  # short
            _, _, _, qe, qa, ae, aa = item
            out.append(f'  <div class="q" data-ch="{ch}" data-done="">\n')
            out.append(f'    <div class="qhead"><span class="qn">Q{n}</span><span class="tag short">Short answer</span>'
                       f'<span class="qtext">{qe}</span></div>\n')
            out.append(f'    <div class="qtext-ar">{qa}</div>\n')
            out.append(f'    <div class="row"><button class="btn ghost no-print" data-toggle-ans '
                       f'onclick="toggleAnswer(this)">Show answer / إظهار الإجابة</button>'
                       f'<span class="srcref">📄 {ref}</span></div>\n')
            out.append(f'    <div class="answer"><div class="lab">✔ Model answer · الإجابة النموذجية</div>'
                       f'<div class="en">{ae}</div><div class="ar">{aa}</div></div>\n')
            out.append('  </div>\n')

    out.append(FOOT)
    path = os.path.join(ROOT, "quiz.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"wrote {path}  ({len(Q)} questions: "
          f"ch1={counts[1]} ch2={counts[2]} ch3={counts[3]} ch4={counts[4]})")


if __name__ == "__main__":
    build()
