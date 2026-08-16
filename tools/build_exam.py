# -*- coding: utf-8 -*-
"""Build the high-confidence exam-format revision page from the photographed paper."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"
LETTERS = "ABCD"

mcqs = [
    ("Which of the following correctly defines ethical hacking?",
     "أي مما يلي يعرّف الاختراق الأخلاقي تعريفاً صحيحاً؟",
     [("Hacking without permission to test security", "الاختراق دون إذن لاختبار الأمن"),
      ("Authorized testing of systems to identify security weaknesses", "اختبار الأنظمة بتصريح لتحديد نقاط الضعف الأمنية"),
      ("Hacking for personal financial gain", "الاختراق لتحقيق مكسب مالي شخصي"),
      ("Breaking into systems to steal data", "اقتحام الأنظمة لسرقة البيانات")], 1, "Ch 1 · Slide 5",
     "Ethical hacking is authorized testing. Permission is what separates it from criminal hacking.",
     "الاختراق الأخلاقي اختبار مُصرّح به، والإذن هو ما يميّزه عن الاختراق الإجرامي."),
    ("The three components of the Security Triangle are:",
     "ما المكونات الثلاثة لمثلث الأمن؟",
     [("Confidentiality, Integrity, Availability", "السرية، السلامة، التوافر"),
      ("Security, Functionality, Usability", "الأمن، الوظيفية، سهولة الاستخدام"),
      ("Prevention, Detection, Correction", "المنع، الكشف، التصحيح"),
      ("Hardware, Software, Network", "الأجهزة، البرمجيات، الشبكة")], 1, "Ch 1 · Slide 11",
     "Do not confuse the Security Triangle with the CIA triad. Here the answer is Security, Functionality, and Usability.",
     "لا تخلط بين مثلث الأمن وثالوث CIA. الجواب هنا: الأمن والوظيفية وسهولة الاستخدام."),
    ("Which footprinting method involves direct interaction with the target’s systems?",
     "أي أسلوب بصمة يتضمن تفاعلاً مباشراً مع أنظمة الهدف؟",
     [("Passive footprinting", "البصمة السلبية"), ("OSINT", "استخبارات المصادر المفتوحة"),
      ("Active footprinting", "البصمة النشطة"), ("Social media intelligence", "استخبارات وسائل التواصل")], 2, "Ch 2 · Slides 3, 8–9",
     "Active footprinting directly interacts with the target and therefore has a greater chance of detection.",
     "البصمة النشطة تتفاعل مباشرة مع الهدف، ولذلك احتمال اكتشافها أكبر."),
    ('What does the Google Dork <code>intitle:"index of" /backup</code> search for?',
     "عمّ يبحث أمر Google Dork الظاهر؟",
     [("Websites with the word backup in the URL", "مواقع فيها كلمة backup في الرابط"),
      ("Exposed directory listings containing backup files", "قوائم مجلدات مكشوفة تحتوي ملفات نسخ احتياطية"),
      ("PDF documents", "مستندات PDF"), ("Login pages", "صفحات تسجيل الدخول")], 1, "Ch 2 · Slide 22",
     "The <code>intitle:\"index of\"</code> pattern finds exposed directory listings; adding backup targets backup directories/files.",
     "النمط <code>intitle:\"index of\"</code> يجد قوائم المجلدات المكشوفة، وإضافة backup تستهدف النسخ الاحتياطية."),
    ("Which type of penetration testing simulates an outside attacker with no knowledge of the internal network?",
     "أي نوع اختبار اختراق يحاكي مهاجماً خارجياً لا يعرف شيئاً عن الشبكة الداخلية؟",
     [("White-box testing", "الصندوق الأبيض"), ("Gray-box testing", "الصندوق الرمادي"),
      ("Black-box testing", "الصندوق الأسود"), ("Clear-box testing", "الصندوق الشفاف")], 2, "Ch 1 · Slide 30",
     "Black-box means no prior knowledge of the target. White-box means full knowledge; gray-box means partial knowledge.",
     "الصندوق الأسود يعني عدم وجود معرفة مسبقة. الأبيض معرفة كاملة، والرمادي معرفة جزئية."),
    ("In the TCP three-way handshake, what does the server send in Step 2?",
     "في المصافحة الثلاثية لـ TCP، ماذا يرسل الخادم في الخطوة الثانية؟",
     [("SYN", "SYN"), ("ACK", "ACK"), ("SYN-ACK", "SYN-ACK"), ("RST", "RST")], 2, "Ch 3 · Slide 10",
     "The sequence is SYN → SYN-ACK → ACK.", "التسلسل هو: SYN ثم SYN-ACK ثم ACK."),
    ("Which active sniffing technique involves forging ARP messages to associate the attacker’s MAC address with another device’s IP?",
     "أي تقنية تنصت نشط تزوّر رسائل ARP لربط MAC المهاجم بعنوان IP لجهاز آخر؟",
     [("MAC flooding", "إغراق MAC"), ("ARP spoofing", "انتحال ARP"),
      ("Port mirroring", "نسخ المنافذ"), ("DHCP starvation", "تجويع DHCP")], 1, "Ch 4 · Slide 24",
     "ARP spoofing/poisoning creates the false IP-to-MAC association and can enable a man-in-the-middle attack.",
     "انتحال/تسميم ARP ينشئ ربطاً مزيفاً بين IP وMAC وقد يتيح هجوم الوسيط."),
    ("Which DNS record is used to identify mail servers for a domain?",
     "أي سجل DNS يُستخدم لتحديد خوادم البريد الخاصة بنطاق؟",
     [("A record", "A record"), ("CNAME record", "CNAME record"),
      ("MX record", "MX record"), ("NS record", "NS record")], 2, "Ch 2 · DNS Footprinting",
     "MX stands for Mail Exchange and identifies the domain’s mail servers.",
     "MX اختصار Mail Exchange، ويحدد خوادم البريد الخاصة بالنطاق."),
]

tfs = [
    ("Passive footprinting is more likely to be detected than active footprinting.", "البصمة السلبية أكثر عرضة للاكتشاف من البصمة النشطة.", False, "Ch 2 · Slides 8–9", "Passive footprinting has no direct target contact and a low detection risk; active footprinting is more detectable.", "البصمة السلبية لا تتصل مباشرة بالهدف وخطر اكتشافها منخفض؛ النشطة هي الأكثر عرضة للاكتشاف."),
    ("The main goal of ethical hacking is to find vulnerabilities before malicious attackers do.", "الهدف الأساسي من الاختراق الأخلاقي هو اكتشاف الثغرات قبل المهاجمين الخبيثين.", True, "Ch 1 · Slides 5, 7", "Ethical hackers identify and help fix weaknesses before hostile attackers exploit them.", "يكتشف المخترق الأخلاقي نقاط الضعف ويساعد على إصلاحها قبل استغلالها."),
    ("The RST flag is used to force termination of a TCP connection.", "يُستخدم علم RST لفرض إنهاء اتصال TCP.", True, "Ch 3 · Slide 9", "RST forces termination in both directions; FIN indicates an orderly close.", "RST يفرض الإنهاء في الاتجاهين، أما FIN فيشير إلى إغلاق منظم."),
    ("Shodan searches for internet-connected devices such as routers, webcams, and servers.", "يبحث Shodan عن الأجهزة المتصلة بالإنترنت مثل الموجّهات والكاميرات والخوادم.", True, "Ch 2 · Slide 28", "Unlike Google, which searches websites and documents, Shodan indexes internet-connected devices.", "على عكس Google الذي يبحث في المواقع والمستندات، يفهرس Shodan الأجهزة المتصلة بالإنترنت."),
    ("An XMAS scan sends packets with FIN, PSH, and URG flags set.", "يرسل فحص XMAS حزماً مع تفعيل أعلام FIN وPSH وURG.", True, "Ch 3 · Slide 29", "XMAS = FIN + PSH + URG. NULL sends no flags; FIN scan sends FIN only.", "XMAS = FIN + PSH + URG. أما NULL فدون أعلام، وFIN يرسل FIN فقط."),
    ("NetBIOS enumeration can reveal computer names and shared resources.", "يمكن لتعداد NetBIOS كشف أسماء الحواسيب والموارد المشتركة.", True, "Ch 3 · Slides 54, 62", "Enumeration can reveal names, users, workgroups/domains, MAC addresses, and shared resources.", "يمكن للتعداد كشف الأسماء والمستخدمين ومجموعات العمل/النطاقات وعناوين MAC والموارد المشتركة."),
    ("Wireshark is a command-line packet analyzer used only on Linux.", "Wireshark محلل حزم يعمل بسطر الأوامر وعلى Linux فقط.", False, "Ch 4 · Slides 29, 32", "Wireshark is a graphical, cross-platform protocol analyzer. Tcpdump is the command-line analyzer commonly used on Linux/Unix.", "Wireshark محلل بروتوكولات رسومي ومتعدد المنصات. Tcpdump هو أداة سطر الأوامر الشائعة على Linux/Unix."),
    ("The default port for SSH is 22.", "المنفذ الافتراضي لـ SSH هو 22.", True, "Ch 3 · Slide 15", "SSH uses port 22; Telnet uses port 23.", "يستخدم SSH المنفذ 22، بينما يستخدم Telnet المنفذ 23."),
]

reserve = [
    ("In an inverse FIN/NULL/XMAS scan, an open port usually gives…", "في فحص FIN/NULL/XMAS العكسي، المنفذ المفتوح يعطي عادةً…", "No response", "لا استجابة", "Ch 3 · Slide 29"),
    ("Which Nmap option performs a stealth SYN scan?", "أي خيار Nmap ينفذ فحص SYN خفياً؟", "<code>-sS</code>", "<code>-sS</code>", "Ch 3 · Slide 36"),
    ("Which Nmap option detects the operating system?", "أي خيار Nmap يكشف نظام التشغيل؟", "<code>-O</code>", "<code>-O</code>", "Ch 3 · Slide 36"),
    ("Which ICMP types are Echo Request and Echo Reply?", "ما نوعا ICMP لطلب الصدى ورد الصدى؟", "Type 8 = Request; Type 0 = Reply", "النوع 8 = طلب؛ النوع 0 = رد", "Ch 3 · Slide 22"),
    ("What are the default SNMP read and read/write strings?", "ما سلسلتا SNMP الافتراضيتان للقراءة وللقراءة/الكتابة؟", "public / private", "public / private", "Ch 3 · Slide 65"),
    ("What happens when a switch CAM table becomes full?", "ماذا يحدث عندما يمتلئ جدول CAM؟", "Unknown frames are flooded to all ports; the switch behaves like a hub.", "تُبث الإطارات المجهولة لكل المنافذ ويتصرف المحوّل كالـHub.", "Ch 4 · Slides 22–23"),
    ("ARP Request uses what delivery type, and ARP Reply uses what type?", "ما نوع إرسال طلب ARP ورد ARP؟", "Request = broadcast; Reply = unicast", "الطلب = بث؛ الرد = أحادي البث", "Ch 4 · Slide 13"),
    ("Name the three principal scan-evasion techniques.", "اذكر تقنيات التهرب الرئيسية الثلاث.", "Packet fragmentation, IP spoofing, proxy servers", "تجزئة الحزم، انتحال IP، الخوادم الوسيطة", "Ch 3 · Slide 44"),
]


def qcard(n, qe, qa, opts, correct, ref, ee, ea, tag="MCQ", tagcls="mcq"):
    out = [f'<div class="q" data-done=""><div class="qhead"><span class="qn">{n}</span><span class="tag {tagcls}">{tag}</span><span class="qtext">{qe}</span></div><div class="qtext-ar">{qa}</div><div class="opts">']
    for i, (oe, oa) in enumerate(opts):
        ok = i == correct
        out.append(f'<div class="opt" data-correct="{1 if ok else 0}" onclick="pickOption(this,\'exam-{n}\',{str(ok).lower()})"><span class="k">{LETTERS[i]}</span><span class="txt"><span class="en">{oe}</span><span class="ar">{oa}</span></span></div>')
    out.append(f'</div><div class="row"><button class="btn ghost no-print" data-toggle-ans onclick="toggleAnswer(this)">Show answer / إظهار الإجابة</button><span class="srcref">📄 {ref}</span></div><div class="answer"><div class="lab">✔ Correct answer: {LETTERS[correct]}) {opts[correct][0]}</div><div class="en">{ee}</div><div class="ar">{ea}</div></div></div>')
    return "".join(out)


def short_card(n, qe, qa, ae, aa, ref):
    return f'''<div class="q scenario-q"><div class="qhead"><span class="qn">{n}</span><span class="tag short">Scenario</span><span class="qtext">{qe}</span></div><div class="qtext-ar">{qa}</div><div class="row"><button class="btn ghost no-print" data-toggle-ans onclick="toggleAnswer(this)">Show model answer / إظهار الحل النموذجي</button><span class="srcref">📄 {ref}</span></div><div class="answer"><div class="lab">✔ Model answer · الإجابة النموذجية</div><div class="en">{ae}</div><div class="ar">{aa}</div></div></div>'''


def build():
    nav = '<a href="index.html">Home</a><a href="ch1.html">Ch 1</a><a href="ch2.html">Ch 2</a><a href="ch3.html">Ch 3</a><a href="ch4.html">Ch 4</a><a href="predicted.html">Predicted Models</a><a href="exam.html">Solved Sample</a><a href="quiz.html">Question Bank</a><a href="cheatsheet.html">Cheat Sheet</a>'
    out = [f'''<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>High-Confidence Predicted Exam | نموذج الاختبار المتوقع</title><link rel="stylesheet" href="css/style.css"></head><body>
<header class="topbar"><div class="topbar-in"><a class="brand" href="index.html"><span class="logo">⚡</span><span>Ethical Hacking<small>الاختراق الأخلاقي — Study Pack</small></span></a><nav class="nav">{nav}</nav></div></header>
<main class="wrap narrow"><div class="page-head"><span class="kicker">Today’s Exam · مراجعة عاجلة</span><h1>High-Confidence Predicted Exam</h1><p class="h1-ar">نموذج الاختبار الأقرب إلى الورقة المصوّرة — مع الحل الكامل</p><p class="lede">This page reconstructs the photographed exam format exactly: <b>8 MCQs, 8 True/False statements, and a three-part scenario</b>. It prioritizes the same facts and wording style. No prediction can honestly guarantee the lecturer’s exact paper, so memorize the bold ideas and then review the reserve list.</p><p class="lede lede-ar">تعيد هذه الصفحة بناء تنسيق الاختبار المصوّر: <b>٨ اختيارات، ٨ صح/خطأ، وسيناريو من ثلاثة أجزاء</b>. لا يمكن ضمان ورقة المدرّسة حرفياً، لذلك احفظ الأفكار المكتوبة بالخط العريض ثم راجع قائمة الاحتياط.</p></div>
<div class="exam-route no-print"><a href="#q1">1 · MCQ</a><a href="#q2">2 · True/False</a><a href="#q3">3 · Scenario</a><a href="#reserve">⚡ Reserve</a><button class="btn" onclick="revealAll()">Reveal all · إظهار الحلول</button><button class="btn primary" data-print>Print / PDF</button><span class="score" id="score"></span></div>
<div class="note"><div class="en"><b>Fastest plan (25–35 min):</b> Answer this page once without revealing solutions. Then memorize the eight reserve answers and the bold keywords in the scenario model answers.</div><div class="ar"><b>أسرع خطة (٢٥–٣٥ دقيقة):</b> حل الصفحة مرة دون إظهار الحل، ثم احفظ أجوبة الاحتياط الثمانية والكلمات الغامقة في حلول السيناريو.</div></div>
<div class="qsec" id="q1"><h2>Q1 · Circle the best answer (8)</h2><div class="ar">س١ · اختر أفضل إجابة (٨)</div></div>''']
    for i, q in enumerate(mcqs, 1): out.append(qcard(f"Q1.{i}", *q))
    out.append('<div class="qsec" id="q2"><h2>Q2 · True or False (8)</h2><div class="ar">س٢ · صح أم خطأ (٨)</div></div>')
    for i, (qe, qa, ans, ref, ee, ea) in enumerate(tfs, 1):
        opts = [("True", "صحيح"), ("False", "خطأ")]
        out.append(qcard(f"Q2.{i}", qe, qa, opts, 0 if ans else 1, ref, ee, ea, "True / False", "tf"))
    out.append('<div class="qsec" id="q3"><h2>Q3 · Scenario</h2><div class="ar">س٣ · السيناريو</div></div>')
    out.append('''<div class="scenario-stem"><div class="en"><b>Scenario:</b> “MediTrust” is a healthcare provider that stores electronic health records for more than 50,000 patients. It needs a penetration test to comply with healthcare data-protection regulations. You begin with Shodan searches to understand what information is publicly exposed.</div><div class="ar"><b>السيناريو:</b> شركة “MediTrust” للرعاية الصحية تخزّن سجلات صحية إلكترونية لأكثر من ٥٠ ألف مريض، وتحتاج اختبار اختراق للامتثال لأنظمة حماية البيانات. تبدأ باستخدام Shodan لمعرفة المعلومات المكشوفة للعامة.</div></div>''')
    out.append(short_card("Q3", "What is Shodan, why is it particularly dangerous for IoT devices, and what information about the organization’s devices might an attacker find?", "ما هو Shodan، ولماذا يُعد خطراً خصوصاً على أجهزة IoT، وما المعلومات التي قد يجدها المهاجم عن أجهزة المؤسسة؟", "<b>Shodan is a specialized search engine for internet-connected devices</b>, rather than ordinary web pages. It is dangerous for IoT because many devices are publicly reachable, poorly configured, use default credentials, or run outdated vulnerable software. An attacker may find <b>public IP addresses, open ports, running services and banners, device type/model, software/firmware versions, location, and exposed webcams, routers, servers, medical or industrial devices</b>. This information helps select vulnerable targets without first scanning the organization directly.", "<b>Shodan محرك بحث متخصص للأجهزة المتصلة بالإنترنت</b> وليس لصفحات الويب العادية. خطورته على IoT أن كثيراً من الأجهزة مكشوفة للعامة أو سيئة الإعداد أو تستخدم بيانات افتراضية أو برمجيات قديمة. قد يجد المهاجم <b>عناوين IP العامة، المنافذ المفتوحة، الخدمات واللافتات، نوع الجهاز وطرازه، إصدار البرنامج/البرنامج الثابت، الموقع، والكاميرات والموجّهات والخوادم والأجهزة الطبية أو الصناعية المكشوفة</b>. تساعد هذه البيانات في اختيار هدف ضعيف دون فحص المؤسسة مباشرة.", "Ch 2 · Slides 28–30"))
    out.append(short_card("Q3.A", "You perform passive reconnaissance by examining the company’s website and social media. Why is passive reconnaissance important, and what useful non-technical information might you gather?", "تنفذ استطلاعاً سلبياً بفحص موقع الشركة ووسائل التواصل. لماذا هو مهم، وما المعلومات غير التقنية المفيدة التي قد تجمعها؟", "Passive reconnaissance is important because it gathers useful intelligence <b>without directly interacting with the target</b>, so it creates no obvious target traffic and has a <b>low risk of detection</b>. Useful non-technical data includes <b>employee names, job titles and responsibilities; organizational structure; office locations and physical-security details; working hours, routines and travel; phone numbers and e-mail patterns; suppliers, partners, current projects and job vacancies</b>. Later, this can support social engineering and more focused authorized testing.", "الاستطلاع السلبي مهم لأنه يجمع معلومات <b>دون تفاعل مباشر مع الهدف</b>، فلا يولّد حركة واضحة واحتمال اكتشافه <b>منخفض</b>. تشمل المعلومات غير التقنية: <b>أسماء الموظفين ومناصبهم ومسؤولياتهم، الهيكل التنظيمي، مواقع المكاتب والأمن المادي، ساعات العمل والروتين والسفر، الهواتف وأنماط البريد، الموردين والشركاء والمشاريع وإعلانات الوظائف</b>. ويمكن استخدامها لاحقاً في الهندسة الاجتماعية وتركيز الاختبار المصرّح.", "Ch 2 · Slides 6, 8, 14–17"))
    out.append(short_card("Q3.B", "During active scanning, you need to avoid detection by the organization’s IDS. Name three scan-evasion techniques and explain how each helps avoid detection.", "أثناء الفحص النشط تريد تجنب اكتشاف IDS. اذكر ثلاث تقنيات للتهرب واشرح كيف تساعد كل واحدة.", "<ol><li><b>Packet fragmentation:</b> split packets into small fragments. The destination reassembles them, while an IDS/firewall may fail to inspect the complete probe correctly.</li><li><b>IP address spoofing:</b> place a fake source IP in packets to hide the scanner’s true identity; replies may not return to the attacker.</li><li><b>Proxy servers / proxy chains:</b> send scanning traffic through one or more real intermediary servers. The target sees the proxy IP, hiding the tester’s identity and location; each proxy in a chain knows only the previous and next hop.</li></ol>", "<ol><li><b>تجزئة الحزم:</b> تقسيم الحزمة إلى أجزاء صغيرة؛ تعيد الوجهة تجميعها، وقد يعجز IDS/الجدار الناري عن فحص الطلب كاملاً.</li><li><b>انتحال عنوان IP:</b> وضع عنوان مصدر مزيف لإخفاء هوية الفاحص الحقيقية، وقد لا تعود الردود إليه.</li><li><b>الخوادم/السلاسل الوسيطة:</b> تمرير حركة الفحص عبر وسيط أو أكثر؛ يرى الهدف IP الوسيط فتُخفى الهوية والموقع، وكل وسيط في السلسلة يعرف القفزة السابقة والتالية فقط.</li></ol>", "Ch 3 · Slides 44–48"))
    out.append('<div class="qsec" id="reserve"><h2>⚡ Highest-probability reserve</h2><div class="ar">احتياط عالي الاحتمال — احفظه</div></div><div class="reserve-grid">')
    for i, (qe, qa, ae, aa, ref) in enumerate(reserve, 1):
        out.append(f'<div class="reserve-card"><span class="reserve-n">R{i}</span><div class="en"><b>{qe}</b><p>{ae}</p></div><div class="ar"><b>{qa}</b><p>{aa}</p></div><small>📄 {ref}</small></div>')
    out.append('''</div><div class="pager no-print"><a class="btn" href="cheatsheet.html">← Last-minute Cheat Sheet</a><a class="btn primary" href="quiz.html">Full 214-question bank →</a></div></main><footer>High-confidence exam-format revision · answers verified against Chapters 1–4<div class="ar">مراجعة بتنسيق الاختبار · الحلول مراجعة على الفصول ١–٤</div></footer><script src="js/app.js"></script></body></html>''')
    (ROOT / "exam.html").write_text("".join(out), encoding="utf-8")
    print("wrote", ROOT / "exam.html")

if __name__ == "__main__": build()
