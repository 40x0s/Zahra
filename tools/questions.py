# -*- coding: utf-8 -*-
"""
Question bank — every fact is taken verbatim from the four lecture PDFs.
بنك الأسئلة — كل معلومة مأخوذة حرفياً من ملفات المحاضرات الأربعة.

Format:
  ("mcq", ch, ref, q_en, q_ar, [(opt_en, opt_ar), ...], correct_index, exp_en, exp_ar)
  ("tf",  ch, ref, q_en, q_ar, True/False, exp_en, exp_ar)
  ("short", ch, ref, q_en, q_ar, ans_en, ans_ar)
"""

Q = []
def mcq(ch, ref, qe, qa, opts, ci, ee, ea): Q.append(("mcq", ch, ref, qe, qa, opts, ci, ee, ea))
def tf(ch, ref, qe, qa, ans, ee, ea):       Q.append(("tf", ch, ref, qe, qa, ans, ee, ea))
def sa(ch, ref, qe, qa, ae, aa):            Q.append(("short", ch, ref, qe, qa, ae, aa))

# ══════════════════════════════ CHAPTER 1 ══════════════════════════════
mcq(1, "Slide 5",
 "Ethical hacking is best defined as the ______ practice of testing systems, networks and applications to identify and fix security weaknesses.",
 "يُعرَّف الاختراق الأخلاقي بأنه الممارسة ______ لاختبار الأنظمة والشبكات والتطبيقات لاكتشاف نقاط الضعف وإصلاحها.",
 [("Authorized", "المصرَّح بها"), ("Anonymous", "المجهولة"), ("Automated", "الآلية"), ("Accidental", "العرضية")], 0,
 "Slide 5: ethical hacking is the <b>authorized</b> practice of testing systems … before malicious attackers exploit them.",
 "الشريحة ٥: الاختراق الأخلاقي هو الممارسة <b>المصرَّح بها</b> لاختبار الأنظمة قبل أن يستغلها المهاجمون الخبيثون.")

mcq(1, "Slide 6",
 "According to the estimates in the lecture, how much is cybercrime costing worldwide in 2025?",
 "حسب التقديرات الواردة في المحاضرة، كم تُكلّف الجرائم السيبرانية العالم في عام ٢٠٢٥؟",
 [("Almost 10.29 trillion U.S. dollars", "ما يقارب ١٠٫٢٩ تريليون دولار أمريكي"),
  ("Almost 16 trillion U.S. dollars", "ما يقارب ١٦ تريليون دولار"),
  ("Almost 1.29 trillion U.S. dollars", "ما يقارب ١٫٢٩ تريليون دولار"),
  ("Almost 6 billion U.S. dollars", "ما يقارب ٦ مليار دولار")], 0,
 "Slide 6: cybercrime costs almost <b>10.29 trillion USD in 2025</b>, projected to rise to ~16 trillion by 2029.",
 "الشريحة ٦: تكلفة الجرائم السيبرانية نحو <b>١٠٫٢٩ تريليون دولار في ٢٠٢٥</b>، ومن المتوقع ارتفاعها إلى ١٦ تريليون بحلول ٢٠٢٩.")

mcq(1, "Slide 6",
 "Cybercrime is projected to increase to approximately 16 trillion U.S. dollars by which year?",
 "من المتوقع أن ترتفع الجرائم السيبرانية إلى نحو ١٦ تريليون دولار بحلول أي عام؟",
 [("2029", "٢٠٢٩"), ("2025", "٢٠٢٥"), ("2030", "٢٠٣٠"), ("2027", "٢٠٢٧")], 0,
 "Slide 6: “projected to increase to approximately 16 trillion U.S. dollars <b>by 2029</b>.”",
 "الشريحة ٦: «من المتوقع أن ترتفع إلى نحو ١٦ تريليون دولار <b>بحلول ٢٠٢٩</b>».")

mcq(1, "Slide 7",
 "Which of the following is NOT one of the four aspects that keep ethical hacking structured, legal and focused?",
 "أي مما يلي ليس من الجوانب الأربعة التي تُبقي الاختراق الأخلاقي منظماً وقانونياً ومركّزاً؟",
 [("Anonymity", "إخفاء الهوية"), ("Permission-Based", "قائم على الإذن"),
  ("Methodology", "المنهجية"), ("Reporting", "إعداد التقارير")], 0,
 "Slide 7/8: the four aspects are <b>Permission-Based, Methodology, Objective, Reporting</b>. Anonymity is not one of them.",
 "الشريحة ٧/٨: الجوانب الأربعة هي <b>الإذن، المنهجية، الهدف، التقرير</b>. إخفاء الهوية ليس منها.")

mcq(1, "Slide 7",
 "Why is permission necessary in ethical hacking?",
 "لماذا يُعد الإذن ضرورياً في الاختراق الأخلاقي؟",
 [("To differentiate their job from criminal hacking jobs", "للتفريق بين عملهم وأعمال الاختراق الإجرامية"),
  ("To reduce the cost of the test", "لتقليل تكلفة الاختبار"),
  ("To make the scan faster", "لجعل الفحص أسرع"),
  ("To avoid using tools", "لتجنّب استخدام الأدوات")], 0,
 "Slide 7: “This permission becomes necessary to <b>differentiate their job from criminal hacking jobs</b>.”",
 "الشريحة ٧: «يصبح هذا الإذن ضرورياً <b>للتفريق بين عملهم وبين أعمال الاختراق الإجرامية</b>».")

mcq(1, "Slide 11",
 "The Security Triangle (the “Iron Triangle of Cybersecurity”) consists of:",
 "يتكوّن مثلث الأمن («المثلث الحديدي للأمن السيبراني») من:",
 [("Security, Functionality, Usability", "الأمن، الوظيفية، سهولة الاستخدام"),
  ("Confidentiality, Integrity, Availability", "السرية، السلامة، التوافر"),
  ("Preventative, Detective, Corrective", "وقائية، كاشفة، تصحيحية"),
  ("People, Process, Technology", "الأشخاص، العمليات، التقنية")], 0,
 "Slide 11: the triangle = <b>Security · Functionality · Usability</b>. (CIA is the separate IT-security triangle on slide 15.)",
 "الشريحة ١١: المثلث = <b>الأمن · الوظيفية · سهولة الاستخدام</b>. (أما CIA فهو مثلث أمن المعلومات في الشريحة ١٥.)")

mcq(1, "Slide 11",
 "In the Security Triangle, which element refers to “the ease with which users can navigate, learn, and utilize the system”?",
 "في مثلث الأمن، أي عنصر يشير إلى «سهولة تنقّل المستخدمين وتعلّمهم واستخدامهم للنظام»؟",
 [("Usability", "سهولة الاستخدام"), ("Functionality", "الوظيفية"),
  ("Security", "الأمن"), ("Availability", "التوافر")], 0,
 "Slide 11 defines <b>Usability</b> exactly this way.",
 "الشريحة ١١ تعرّف <b>سهولة الاستخدام</b> بهذه الصيغة تماماً.")

mcq(1, "Slide 11",
 "Which element of the Security Triangle means “the features, capabilities, and options a system offers to meet user needs”?",
 "أي عنصر من مثلث الأمن يعني «الميزات والقدرات والخيارات التي يوفرها النظام لتلبية احتياجات المستخدم»؟",
 [("Functionality", "الوظيفية"), ("Usability", "سهولة الاستخدام"),
  ("Security", "الأمن"), ("Integrity", "السلامة")], 0,
 "Slide 11: <b>Functionality</b>.", "الشريحة ١١: <b>الوظيفية</b>.")

mcq(1, "Slide 14",
 "Controls designed to be used AFTER an event to limit the extent of damage and aid swift recovery are called:",
 "الضوابط المصممة للاستخدام بعد وقوع الحدث للحد من الضرر والمساعدة على التعافي السريع تُسمى:",
 [("Corrective", "تصحيحية"), ("Preventative", "وقائية"),
  ("Detective", "كاشفة"), ("Administrative", "إدارية")], 0,
 "Slide 14: the three control types are <b>preventative</b> (before), <b>detective</b> (identify), <b>corrective</b> (after the event).",
 "الشريحة ١٤: أنواع الضوابط الثلاثة هي <b>وقائية</b> (قبل) و<b>كاشفة</b> (تكتشف) و<b>تصحيحية</b> (بعد الحدث).")

mcq(1, "Slide 14",
 "Controls put in place to prevent errors or incidents from occurring in the first place are:",
 "الضوابط الموضوعة لمنع وقوع الأخطاء أو الحوادث من الأساس هي:",
 [("Preventative", "وقائية"), ("Detective", "كاشفة"),
  ("Corrective", "تصحيحية"), ("Physical", "مادية")], 0,
 "Slide 14: <b>preventative</b> controls stop incidents from occurring in the first place.",
 "الشريحة ١٤: الضوابط <b>الوقائية</b> تمنع الحوادث من الوقوع أصلاً.")

mcq(1, "Slide 15",
 "“Ensuring data is only accessible to authorized individuals” is the definition of:",
 "«ضمان ألا يصل إلى البيانات إلا الأشخاص المصرّح لهم» هو تعريف:",
 [("Confidentiality", "السرية"), ("Integrity", "السلامة"),
  ("Availability", "التوافر"), ("Authentication", "المصادقة")], 0,
 "Slide 15: <b>Confidentiality</b>.", "الشريحة ١٥: <b>السرية</b>.")

mcq(1, "Slide 15",
 "“Protecting data from unauthorized alterations or corruption” refers to which CIA pillar?",
 "«حماية البيانات من التعديل أو التلف غير المصرّح به» يشير إلى أي ركيزة من CIA؟",
 [("Integrity", "السلامة/التكاملية"), ("Confidentiality", "السرية"),
  ("Availability", "التوافر"), ("Accountability", "المساءلة")], 0,
 "Slide 15: <b>Integrity</b>.", "الشريحة ١٥: <b>السلامة (Integrity)</b>.")

mcq(1, "Slide 15",
 "“Ensuring authorized users can access systems and data whenever needed” is:",
 "«ضمان تمكّن المستخدمين المصرّح لهم من الوصول إلى الأنظمة والبيانات وقت الحاجة» هو:",
 [("Availability", "التوافر"), ("Integrity", "السلامة"),
  ("Confidentiality", "السرية"), ("Usability", "سهولة الاستخدام")], 0,
 "Slide 15: <b>Availability</b>.", "الشريحة ١٥: <b>التوافر</b>.")

mcq(1, "Slide 18",
 "In which access control method is the security policy controlled by a security administrator, so users CANNOT set access controls themselves?",
 "في أي طريقة تحكم بالوصول تكون السياسة الأمنية تحت سيطرة مسؤول الأمن، بحيث لا يستطيع المستخدمون ضبط الصلاحيات بأنفسهم؟",
 [("Mandatory Access Control (MAC)", "التحكم الإلزامي (MAC)"),
  ("Discretionary Access Control (DAC)", "التحكم التقديري (DAC)"),
  ("Role-Based Access Control (RBAC)", "التحكم القائم على الأدوار"),
  ("Rule-Based Access Control", "التحكم القائم على القواعد")], 0,
 "Slide 18: <b>MAC</b> — the security administrator controls the policy; users can’t set access controls themselves.",
 "الشريحة ١٨: <b>MAC</b> — مسؤول الأمن يتحكم بالسياسة والمستخدمون لا يستطيعون ضبط الصلاحيات.")

mcq(1, "Slide 18",
 "Which access control method allows users to set access controls on the resources they own or control?",
 "أي طريقة تحكم بالوصول تسمح للمستخدمين بضبط صلاحيات الوصول على الموارد التي يملكونها؟",
 [("DAC", "التحكم التقديري DAC"), ("MAC", "التحكم الإلزامي MAC"),
  ("ACL only", "قوائم التحكم فقط"), ("Biometric control", "التحكم البيومتري")], 0,
 "Slide 18: <b>DAC</b> puts this power in the hands of the users themselves.",
 "الشريحة ١٨: <b>DAC</b> يضع هذه الصلاحية بين أيدي المستخدمين أنفسهم.")

mcq(1, "Slide 19",
 "Which security policy identifies the resources that need protection and the rules in place to control access to those resources?",
 "أي سياسة أمنية تحدد الموارد التي تحتاج حماية والقواعد للتحكم في الوصول إليها؟",
 [("Access Control Policy", "سياسة التحكم في الوصول"),
  ("Information Security Policy", "سياسة أمن المعلومات"),
  ("Password Policy", "سياسة كلمات المرور"),
  ("Information Audit Policy", "سياسة تدقيق المعلومات")], 0,
 "Slide 19: the <b>Access Control Policy</b>.", "الشريحة ١٩: <b>سياسة التحكم في الوصول</b>.")

mcq(1, "Slide 20",
 "Which policy defines information sensitivity levels, who has access to those levels, and how data is stored, transmitted and destroyed?",
 "أي سياسة تحدد مستويات حساسية المعلومات ومن يملك صلاحية الوصول إليها وكيفية تخزين البيانات ونقلها وإتلافها؟",
 [("Information Protection Policy", "سياسة حماية المعلومات"),
  ("Access Control Policy", "سياسة التحكم في الوصول"),
  ("E-mail Policy", "سياسة البريد الإلكتروني"),
  ("Password Policy", "سياسة كلمات المرور")], 0,
 "Slide 20: the <b>Information Protection Policy</b>.", "الشريحة ٢٠: <b>سياسة حماية المعلومات</b>.")

mcq(1, "Slide 20",
 "Length, complexity, maximum and minimum age, and reuse are all defined by which policy?",
 "الطول والتعقيد والحد الأقصى والأدنى للعمر وإعادة الاستخدام — كلها تحددها أي سياسة؟",
 [("Password Policy", "سياسة كلمات المرور"),
  ("Information Audit Policy", "سياسة تدقيق المعلومات"),
  ("Information Security Policy", "سياسة أمن المعلومات"),
  ("Access Control Policy", "سياسة التحكم في الوصول")], 0,
 "Slide 20: the <b>Password Policy</b>.", "الشريحة ٢٠: <b>سياسة كلمات المرور</b>.")

mcq(1, "Slide 20",
 "Which policy defines the framework for auditing security — when, where, how, how often, and sometimes who conducts the audits?",
 "أي سياسة تحدد إطار تدقيق الأمن: متى وأين وكيف وكم مرة وأحياناً مَن يقوم بالتدقيق؟",
 [("Information Audit Policy", "سياسة تدقيق المعلومات"),
  ("Information Protection Policy", "سياسة حماية المعلومات"),
  ("E-mail Policy", "سياسة البريد الإلكتروني"),
  ("Access Control Policy", "سياسة التحكم في الوصول")], 0,
 "Slide 20: the <b>Information Audit Policy</b>.", "الشريحة ٢٠: <b>سياسة تدقيق المعلومات</b>.")

mcq(1, "Slide 22",
 "Ethical hacking is also known as:",
 "يُعرف الاختراق الأخلاقي أيضاً باسم:",
 [("White-hat hacking or penetration testing", "اختراق القبعة البيضاء أو اختبار الاختراق"),
  ("Black-hat hacking", "اختراق القبعة السوداء"),
  ("Cracking", "التكسير (Cracking)"),
  ("Phreaking", "فريكينج")], 0,
 "Slide 22: “also known as <b>white-hat hacking</b> or <b>penetration testing</b>.”",
 "الشريحة ٢٢: «يُعرف أيضاً بـ<b>اختراق القبعة البيضاء</b> أو <b>اختبار الاختراق</b>».")

mcq(1, "Slide 23",
 "Which hacker classification describes crackers who illegally use their skills for personal gain or malicious intent?",
 "أي تصنيف للهاكرز يصف المخرّبين الذين يستخدمون مهاراتهم بشكل غير قانوني لمكسب شخصي أو بنية خبيثة؟",
 [("Black hats", "القبعات السوداء"), ("White hats", "القبعات البيضاء"),
  ("Gray hats", "القبعات الرمادية"), ("Blue hats", "القبعات الزرقاء")], 0,
 "Slide 23: <b>Black hats</b> — “the bad guys… the crackers.”",
 "الشريحة ٢٣: <b>القبعات السوداء</b> — «الأشرار… المخرّبون».")

mcq(1, "Slide 23",
 "According to slide 23, which group is “the hardest group to categorize” — neither good nor bad?",
 "حسب الشريحة ٢٣، أي مجموعة هي «الأصعب في التصنيف» — لا هي خيّرة ولا شريرة؟",
 [("Gray hats", "القبعات الرمادية"), ("Black hats", "القبعات السوداء"),
  ("White hats", "القبعات البيضاء"), ("Script kiddies", "الهواة (Script kiddies)")], 0,
 "Slide 23: <b>Gray hats</b> — two subsets: the merely curious, and those who feel it is their duty to demonstrate flaws with or without permission.",
 "الشريحة ٢٣: <b>القبعات الرمادية</b> — فئتان: الفضوليون، ومن يرون أن من واجبهم إظهار العيوب بإذن أو بدونه.")

mcq(1, "Slide 24",
 "An attack that targets the common mistake of accepting and leaving all the defaults when installing operating systems is called:",
 "الهجوم الذي يستهدف الخطأ الشائع بقبول جميع الإعدادات الافتراضية وتركها عند تثبيت أنظمة التشغيل يُسمّى:",
 [("Operating system (OS) attack", "هجوم نظام التشغيل"),
  ("Shrink-wrap code attack", "هجوم الشيفرة الجاهزة"),
  ("Application-level attack", "هجوم مستوى التطبيق"),
  ("Misconfiguration attack", "هجوم سوء الإعداد")], 0,
 "Slide 24: <b>OS attacks</b> target accepting/leaving all the defaults.",
 "الشريحة ٢٤: <b>هجمات نظام التشغيل</b> تستهدف قبول/ترك الإعدادات الافتراضية.")

mcq(1, "Slide 24",
 "Attacks that take advantage of the built-in code and scripts most off-the-shelf applications come with are:",
 "الهجمات التي تستغل الشيفرات والسكربتات المدمجة التي تأتي مع معظم التطبيقات الجاهزة هي:",
 [("Shrink-wrap code attacks", "هجمات الشيفرة الجاهزة"),
  ("Application-level attacks", "هجمات مستوى التطبيق"),
  ("Misconfiguration attacks", "هجمات سوء الإعداد"),
  ("OS attacks", "هجمات نظام التشغيل")], 0,
 "Slide 24: <b>Shrink-wrap code attacks</b>.", "الشريحة ٢٤: <b>هجمات الشيفرة الجاهزة (Shrink-wrap)</b>.")

mcq(1, "Slide 24",
 "Attacks on the actual programming code and software logic of an application are called:",
 "الهجمات على الشيفرة البرمجية ومنطق البرنامج الفعلي للتطبيق تُسمى:",
 [("Application-level attacks", "هجمات مستوى التطبيق"),
  ("OS attacks", "هجمات نظام التشغيل"),
  ("Shrink-wrap code attacks", "هجمات الشيفرة الجاهزة"),
  ("Misconfiguration attacks", "هجمات سوء الإعداد")], 0,
 "Slide 24: <b>Application-level attacks</b>.", "الشريحة ٢٤: <b>هجمات مستوى التطبيق</b>.")

mcq(1, "Slide 25",
 "Which organisation identified the hacking phases taught in this course?",
 "أي جهة حدّدت مراحل الاختراق التي تُدرَّس في هذا المقرر؟",
 [("EC-Council", "مجلس EC-Council"), ("ISO", "الأيزو"),
  ("NIST", "المعهد الوطني للمعايير NIST"), ("ISACA", "أيساكا")], 0,
 "Slide 25: “Hacking phases, as identified by <b>EC-Council</b>…”",
 "الشريحة ٢٥: «مراحل الاختراق كما حددها <b>مجلس EC-Council</b>».")

mcq(1, "Slide 25",
 "What is the correct order of the ethical hacking phases?",
 "ما الترتيب الصحيح لمراحل الاختراق الأخلاقي؟",
 [("Reconnaissance → Scanning and enumeration → Gaining access → Maintaining access → Covering tracks",
   "الاستطلاع ← الفحص والتعداد ← الحصول على الوصول ← الحفاظ على الوصول ← تغطية الآثار"),
  ("Scanning → Reconnaissance → Gaining access → Covering tracks → Maintaining access",
   "الفحص ← الاستطلاع ← الوصول ← تغطية الآثار ← الحفاظ على الوصول"),
  ("Reconnaissance → Gaining access → Scanning → Maintaining access → Covering tracks",
   "الاستطلاع ← الوصول ← الفحص ← الحفاظ على الوصول ← تغطية الآثار"),
  ("Footprinting → Exploiting → Reporting → Patching → Auditing",
   "البصمة ← الاستغلال ← التقرير ← الترقيع ← التدقيق")], 0,
 "Slide 25/26: the five phases in order are Reconnaissance, Scanning &amp; enumeration, Gaining access, Maintaining access, Covering tracks.",
 "الشريحة ٢٥/٢٦: المراحل الخمس بالترتيب: الاستطلاع، الفحص والتعداد، الحصول على الوصول، الحفاظ على الوصول، تغطية الآثار.")

mcq(1, "Slide 28",
 "In which phase does the attacker leave back doors open for future use?",
 "في أي مرحلة يترك المهاجم أبواباً خلفية مفتوحة للاستخدام المستقبلي؟",
 [("Maintaining access", "الحفاظ على الوصول"), ("Gaining access", "الحصول على الوصول"),
  ("Covering tracks", "تغطية الآثار"), ("Reconnaissance", "الاستطلاع")], 0,
 "Slide 28: in <b>maintaining access</b> hackers ensure a way back in; the attacker leaves back doors open.",
 "الشريحة ٢٨: في <b>الحفاظ على الوصول</b> يضمن المخترقون طريق العودة ويتركون أبواباً خلفية.")

mcq(1, "Slide 28",
 "Removing or altering log files, or hiding files with hidden attributes or directories, occurs in which phase?",
 "حذف أو تعديل ملفات السجل أو إخفاء الملفات بخصائص/مجلدات مخفية يحدث في أي مرحلة؟",
 [("Covering tracks", "تغطية الآثار"), ("Maintaining access", "الحفاظ على الوصول"),
  ("Scanning and enumeration", "الفحص والتعداد"), ("Gaining access", "الحصول على الوصول")], 0,
 "Slide 28: these are the steps of the final phase, <b>covering tracks</b>.",
 "الشريحة ٢٨: هذه خطوات المرحلة الأخيرة، <b>تغطية الآثار</b>.")

mcq(1, "Slide 30",
 "In which type of penetration testing does the ethical hacker have absolutely NO knowledge of the TOE (Target of Evaluation)?",
 "في أي نوع من اختبار الاختراق لا يملك المخترق الأخلاقي أي معرفة إطلاقاً بالهدف قيد التقييم (TOE)؟",
 [("Black-box testing", "اختبار الصندوق الأسود"), ("White-box testing", "اختبار الصندوق الأبيض"),
  ("Gray-box testing", "اختبار الصندوق الرمادي"), ("Blue-box testing", "اختبار الصندوق الأزرق")], 0,
 "Slide 30: in <b>black-box</b> testing the tester has absolutely no knowledge of the TOE; it takes the most time and is usually the most expensive.",
 "الشريحة ٣٠: في <b>الصندوق الأسود</b> لا يملك المختبِر أي معرفة بالهدف، ويستغرق أطول وقت وعادةً أغلى خيار.")

mcq(1, "Slide 30",
 "Which penetration test type is also known as “partial knowledge testing” and assumes the attacker is an insider?",
 "أي نوع من اختبار الاختراق يُعرف بـ«اختبار المعرفة الجزئية» ويفترض أن المهاجم من داخل المؤسسة؟",
 [("Gray-box testing", "اختبار الصندوق الرمادي"), ("Black-box testing", "الصندوق الأسود"),
  ("White-box testing", "الصندوق الأبيض"), ("Red-box testing", "الصندوق الأحمر")], 0,
 "Slide 30: <b>Gray-box</b> = partial knowledge; assumes the attacker is an insider and can demonstrate privilege escalation from a trusted employee.",
 "الشريحة ٣٠: <b>الرمادي</b> = معرفة جزئية، يفترض أن المهاجم من الداخل ويمكنه إظهار تصعيد الصلاحيات من موظف موثوق.")

mcq(1, "Slide 30",
 "Which penetration testing type takes the MOST amount of time and is usually by far the MOST expensive?",
 "أي نوع من اختبار الاختراق يستغرق أطول وقت وعادةً هو الأغلى بفارق كبير؟",
 [("Black-box", "الصندوق الأسود"), ("White-box", "الصندوق الأبيض"),
  ("Gray-box", "الصندوق الرمادي"), ("All are equal", "جميعها متساوية")], 0,
 "Slide 30: black-box “takes the most amount of time to complete and, usually, is by far the most expensive option.”",
 "الشريحة ٣٠: الصندوق الأسود «يستغرق أطول وقت وعادةً هو الخيار الأغلى بفارق كبير».")

mcq(1, "Slide 33",
 "According to the assessment policy, how many marks are allocated to the final exam (theory)?",
 "حسب سياسة التقييم، كم درجة مخصصة للاختبار النهائي (النظري)؟",
 [("50", "٥٠"), ("30", "٣٠"), ("10", "١٠"), ("20", "٢٠")], 0,
 "Slide 33: Assignments 5, Quizzes 5, Midterm 10, Lab 30, <b>Final exam 50</b> — total 100.",
 "الشريحة ٣٣: الواجبات ٥، الاختبارات القصيرة ٥، منتصف الفصل ١٠، المعمل ٣٠، <b>النهائي ٥٠</b> — المجموع ١٠٠.")

mcq(1, "Slide 33",
 "How many marks are allocated to the lab part?",
 "كم درجة مخصصة للجزء العملي (المعمل)؟",
 [("30", "٣٠"), ("50", "٥٠"), ("10", "١٠"), ("5", "٥")], 0,
 "Slide 33: the lab part is worth <b>30</b> marks.", "الشريحة ٣٣: الجزء العملي <b>٣٠</b> درجة.")

tf(1, "Slide 22",
 "Ethical hackers have the same skills and use the same tools and tactics as malicious hackers.",
 "يمتلك المخترقون الأخلاقيون المهارات نفسها ويستخدمون الأدوات والأساليب نفسها التي يستخدمها المخترقون الخبيثون.",
 True,
 "Slide 22 — true; but their goal is always to improve network security without harming the network or its users.",
 "الشريحة ٢٢ — صحيح؛ لكن هدفهم دائماً تحسين أمن الشبكة دون الإضرار بها أو بمستخدميها.")

tf(1, "Slide 30",
 "In white-box testing, pen testers have full knowledge of the network, system and infrastructure they are targeting.",
 "في اختبار الصندوق الأبيض يملك المختبِرون معرفة كاملة بالشبكة والنظام والبنية التحتية المستهدفة.",
 True,
 "Slide 30 — white-box is the exact opposite of black-box: full knowledge.",
 "الشريحة ٣٠ — الصندوق الأبيض هو النقيض التام للأسود: معرفة كاملة.")

tf(1, "Slide 29",
 "If the steps taken by the ethical hacker during a pen test do not adequately mirror what a “real” hacker would do, the test is doomed to failure.",
 "إذا لم تحاكِ خطوات المخترق الأخلاقي أثناء اختبار الاختراق ما سيفعله المخترق «الحقيقي» بشكل كافٍ، فإن الاختبار محكوم عليه بالفشل.",
 True,
 "Slide 29 states this literally.", "الشريحة ٢٩ تنص على ذلك حرفياً.")

sa(1, "Slide 12",
 "In risk management, what three things must an organisation identify to determine appropriate security countermeasures?",
 "في إدارة المخاطر، ما الأشياء الثلاثة التي يجب على المؤسسة تحديدها لاختيار الإجراءات المضادة المناسبة؟",
 "Organizational <b>assets</b>, the <b>threats</b> and the <b>vulnerabilities</b> that affect them (slide 12).",
 "<b>أصول</b> المؤسسة، و<b>التهديدات</b> و<b>الثغرات</b> التي تؤثر عليها (الشريحة ١٢).")

sa(1, "Slide 31",
 "Name any three laws mentioned in the lecture that an ethical hacker must be aware of.",
 "اذكر ثلاثة قوانين وردت في المحاضرة يجب على المخترق الأخلاقي معرفتها.",
 "Any three of: <b>FISMA</b>, Electronics Communications Privacy Act, <b>PATRIOT Act</b>, Privacy Act of 1974, <b>CISPA</b>, Consumer Data Security and Notification Act, Computer Security Act of 1987 (slide 31).",
 "أي ثلاثة من: <b>FISMA</b>، قانون خصوصية الاتصالات الإلكترونية، <b>قانون باتريوت</b>، قانون الخصوصية ١٩٧٤، <b>CISPA</b>، قانون أمن بيانات المستهلك والإخطار، قانون أمن الحاسوب ١٩٨٧ (الشريحة ٣١).")

sa(1, "Slide 5 / 7",
 "State the main objective of ethical hacking.",
 "اذكر الهدف الأساسي من الاختراق الأخلاقي.",
 "To <b>find the holes (security weaknesses) before hostile attackers can penetrate them</b>, and to fix them — strengthening cybersecurity and protecting digital assets (slides 5 &amp; 7).",
 "<b>إيجاد الثغرات قبل أن يتمكن المهاجمون المعادون من اختراقها</b> وإصلاحها — لتقوية الأمن السيبراني وحماية الأصول الرقمية (الشريحتان ٥ و٧).")

# ══════════════════════════════ CHAPTER 2 ══════════════════════════════
mcq(2, "Slide 3",
 "What is the FIRST step in ethical hacking?",
 "ما الخطوة الأولى في الاختراق الأخلاقي؟",
 [("Reconnaissance", "الاستطلاع"), ("Scanning", "الفحص"),
  ("Gaining access", "الحصول على الوصول"), ("Reporting", "إعداد التقرير")], 0,
 "Slide 3: “The first step in ethical hacking is <b>reconnaissance</b>, which means gathering information about the target.”",
 "الشريحة ٣: «الخطوة الأولى في الاختراق الأخلاقي هي <b>الاستطلاع</b>، ويعني جمع المعلومات عن الهدف».")

mcq(2, "Slide 3 / 8",
 "Which type of reconnaissance collects information WITHOUT directly interacting with the target, so the target does not know data has been gathered?",
 "أي نوع من الاستطلاع يجمع المعلومات دون التفاعل المباشر مع الهدف، بحيث لا يعلم الهدف بجمع البيانات؟",
 [("Passive reconnaissance", "الاستطلاع السلبي"), ("Active reconnaissance", "الاستطلاع النشط"),
  ("Aggressive scanning", "الفحص العدواني"), ("Enumeration", "التعداد")], 0,
 "Slide 3: <b>passive</b> reconnaissance = no direct interaction; low risk of detection.",
 "الشريحة ٣: الاستطلاع <b>السلبي</b> = لا تفاعل مباشر؛ خطر اكتشاف منخفض.")

mcq(2, "Slide 3 / 9",
 "Active reconnaissance provides more detailed information but carries which drawback?",
 "الاستطلاع النشط يوفر معلومات أكثر تفصيلاً لكنه يحمل أي عيب؟",
 [("A greater chance of being detected", "احتمالية أكبر للاكتشاف"),
  ("It is always illegal", "أنه غير قانوني دائماً"),
  ("It cannot find IP addresses", "أنه لا يجد عناوين IP"),
  ("It requires no tools", "أنه لا يحتاج أدوات")], 0,
 "Slides 3 &amp; 9: active methods increase the likelihood of detection by generating observable network traffic.",
 "الشريحتان ٣ و٩: الأساليب النشطة تزيد احتمال الاكتشاف لأنها تولّد حركة مرور ملحوظة.")

mcq(2, "Slide 9",
 "Which of the following is an example of ACTIVE footprinting?",
 "أي مما يلي مثال على البصمة النشطة؟",
 [("Performing a ping sweep or a port scan with Nmap", "تنفيذ مسح Ping أو فحص منافذ بأداة Nmap"),
  ("Examining an organization's website", "فحص موقع المؤسسة"),
  ("Reviewing employee profiles on social media", "مراجعة ملفات الموظفين على وسائل التواصل"),
  ("Searching public DNS records", "البحث في سجلات DNS العامة")], 0,
 "Slide 9: ping sweep, Nmap port scan, and service enumeration are active. The other three are passive examples (slide 8).",
 "الشريحة ٩: مسح Ping وفحص المنافذ بـ Nmap وتعداد الخدمات كلها نشطة. أما الخيارات الأخرى فهي أمثلة سلبية (الشريحة ٨).")

mcq(2, "Slide 8",
 "Which of the following is an example of PASSIVE footprinting?",
 "أي مما يلي مثال على البصمة السلبية؟",
 [("Collecting information from search engines", "جمع المعلومات من محركات البحث"),
  ("Port scanning with Nmap", "فحص المنافذ بـ Nmap"),
  ("Service enumeration", "تعداد الخدمات"),
  ("Performing a ping sweep", "تنفيذ مسح Ping")], 0,
 "Slide 8: examining the website, social-media profiles, public DNS records and search engines — all passive.",
 "الشريحة ٨: فحص الموقع وملفات التواصل وسجلات DNS العامة ومحركات البحث — كلها سلبية.")

mcq(2, "Slide 14",
 "According to the table on slide 14, which source is used to obtain WEB SERVER information?",
 "حسب جدول الشريحة ١٤، أي مصدر يُستخدم للحصول على معلومات خادم الويب؟",
 [("Netcraft", "نتكرافت (Netcraft)"), ("LinkedIn", "لينكدإن"),
  ("Google Maps", "خرائط جوجل"), ("WHOIS databases", "قواعد بيانات WHOIS")], 0,
 "Slide 14: Web server information → <b>Netcraft</b>.",
 "الشريحة ١٤: معلومات خادم الويب ← <b>Netcraft</b>.")

mcq(2, "Slide 14",
 "Which source is listed for obtaining employee names and positions?",
 "أي مصدر مذكور للحصول على أسماء الموظفين ومناصبهم؟",
 [("LinkedIn", "لينكدإن"), ("Netcraft", "نتكرافت"),
  ("Google Maps", "خرائط جوجل"), ("Shodan", "شودان")], 0,
 "Slide 14: Employee names and positions → <b>LinkedIn</b>.",
 "الشريحة ١٤: أسماء الموظفين ومناصبهم ← <b>لينكدإن</b>.")

mcq(2, "Slide 14",
 "Domain ownership information is obtained from:",
 "معلومات ملكية النطاق يتم الحصول عليها من:",
 [("WHOIS databases", "قواعد بيانات WHOIS"), ("Google Maps", "خرائط جوجل"),
  ("Netcraft", "نتكرافت"), ("LinkedIn", "لينكدإن")], 0,
 "Slide 14: Domain ownership information → <b>WHOIS databases</b>.",
 "الشريحة ١٤: معلومات ملكية النطاق ← <b>قواعد بيانات WHOIS</b>.")

mcq(2, "Slide 15",
 "Why are job advertisement platforms valuable during footprinting?",
 "لماذا تُعد منصات إعلانات الوظائف قيّمة أثناء مرحلة البصمة؟",
 [("Technical requirements can unintentionally reveal details about the organization's technology infrastructure",
   "لأن المتطلبات التقنية قد تكشف دون قصد تفاصيل عن البنية التقنية للمؤسسة"),
  ("They list employees' passwords", "لأنها تنشر كلمات مرور الموظفين"),
  ("They provide free vulnerability scanners", "لأنها توفر فاحصات ثغرات مجانية"),
  ("They allow direct access to the network", "لأنها تتيح الوصول المباشر للشبكة")], 0,
 "Slide 15: job postings may disclose OSs, databases, web technologies, cloud platforms, security solutions, languages, and network tools.",
 "الشريحة ١٥: قد تفصح الإعلانات عن أنظمة التشغيل وقواعد البيانات وتقنيات الويب والمنصات السحابية والحلول الأمنية واللغات وأدوات الشبكة.")

mcq(2, "Slide 17",
 "SOCMINT stands for:",
 "اختصار SOCMINT يعني:",
 [("Social Media Intelligence", "استخبارات وسائل التواصل الاجتماعي"),
  ("Social Contact Intelligence", "استخبارات الاتصال الاجتماعي"),
  ("Source Code Intelligence", "استخبارات الشيفرة المصدرية"),
  ("Society Control Intelligence", "استخبارات التحكم المجتمعي")], 0,
 "Slide 17: <b>Social Media Intelligence (SOCMINT)</b>.",
 "الشريحة ١٧: <b>استخبارات وسائل التواصل الاجتماعي (SOCMINT)</b>.")

mcq(2, "Slide 19",
 "The Google Hacking Database (GHDB) is:",
 "قاعدة بيانات اختراق جوجل (GHDB) هي:",
 [("A publicly available collection of advanced Google search commands", "مجموعة متاحة للعامة من أوامر البحث المتقدمة في جوجل"),
  ("A list of hacked Google accounts", "قائمة بحسابات جوجل المخترقة"),
  ("A malware repository", "مستودع برمجيات خبيثة"),
  ("A vulnerability scanner", "فاحص ثغرات")], 0,
 "Slide 19: GHDB is a publicly available collection of advanced Google search commands, often called “Google Dorks”. URL: exploit-db.com/google-hacking-database",
 "الشريحة ١٩: GHDB مجموعة عامة من أوامر البحث المتقدمة تُسمّى «Google Dorks»، على موقع exploit-db.")

mcq(2, "Slide 22",
 "Which Google operator would you use to find PDF documents on a company's website?",
 "أي معامل في جوجل تستخدمه لإيجاد مستندات PDF على موقع شركة؟",
 [("site:company.com filetype:pdf", "site:company.com filetype:pdf"),
  ("inurl:pdf company", "inurl:pdf company"),
  ("link:company.com pdf", "link:company.com pdf"),
  ("related:company.com pdf", "related:company.com pdf")], 0,
 "Slide 22: <code>filetype</code> → <code>site:company.com filetype:pdf</code>.",
 "الشريحة ٢٢: المعامل <code>filetype</code> ← <code>site:company.com filetype:pdf</code>.")

mcq(2, "Slide 22",
 "Which operator/query is used to search for exposed backup directories?",
 "أي معامل/استعلام يُستخدم للبحث عن مجلدات النسخ الاحتياطي المكشوفة؟",
 [("intitle:\"index of\" backup", "intitle:\"index of\" backup"),
  ("inurl:admin backup", "inurl:admin backup"),
  ("info:backup.com", "info:backup.com"),
  ("related:backup", "related:backup")], 0,
 "Slide 22: <code>index of</code> → <code>intitle:\"index of\" backup</code> searches for exposed backup directories.",
 "الشريحة ٢٢: <code>index of</code> ← <code>intitle:\"index of\" backup</code> للبحث عن مجلدات النسخ الاحتياطي المكشوفة.")

mcq(2, "Slide 22",
 "The operator <code>inurl:admin</code> is used to:",
 "المعامل <code>inurl:admin</code> يُستخدم لـ:",
 [("Locate administrative interfaces", "تحديد واجهات الإدارة"),
  ("Find login pages by title", "إيجاد صفحات الدخول عبر العنوان"),
  ("Identify pages linking to a website", "تحديد الصفحات المرتبطة بموقع"),
  ("View Google's information about a website", "عرض معلومات جوجل عن موقع")], 0,
 "Slide 22: <code>inurl</code> → locate administrative interfaces.",
 "الشريحة ٢٢: <code>inurl</code> ← تحديد واجهات الإدارة.")

mcq(2, "Slide 23",
 "Which operator searches for pages with MULTIPLE words in the title tag?",
 "أي معامل يبحث عن صفحات تحوي عدة كلمات في وسم العنوان؟",
 [("allintitle", "allintitle"), ("intitle", "intitle"),
  ("allinurl", "allinurl"), ("allintext", "allintext")], 0,
 "Slide 23: <code>allintitle:android google</code> — multiple words in the title tag.",
 "الشريحة ٢٣: <code>allintitle:android google</code> — عدة كلمات في وسم العنوان.")

mcq(2, "Slide 23",
 "<code>intext:apple</code> searches for:",
 "الأمر <code>intext:apple</code> يبحث عن:",
 [("Pages with a particular word in their content", "صفحات تحوي كلمة معينة في محتواها"),
  ("Pages with the word in the URL", "صفحات تحوي الكلمة في الرابط"),
  ("Pages with the word in the title", "صفحات تحوي الكلمة في العنوان"),
  ("Similar websites", "مواقع مشابهة")], 0,
 "Slide 23: <code>intext</code> = a particular word in the page content.",
 "الشريحة ٢٣: <code>intext</code> = كلمة معينة في محتوى الصفحة.")

mcq(2, "Slide 24",
 "In Google search syntax, what does the minus sign do — e.g. <code>windows -linux</code>?",
 "في صيغة بحث جوجل، ماذا تفعل إشارة الناقص — مثل <code>windows -linux</code>؟",
 [("Excludes pages containing the specified term", "تستبعد الصفحات التي تحوي المصطلح المحدد"),
  ("Requires both terms", "تشترط وجود المصطلحين معاً"),
  ("Searches a numeric range", "تبحث في نطاق رقمي"),
  ("Represents unknown words", "تمثّل كلمات مجهولة")], 0,
 "Slide 24: <code>-</code> (Minus) excludes pages containing the specified term.",
 "الشريحة ٢٤: إشارة الناقص تستبعد الصفحات التي تحوي المصطلح المحدد.")

mcq(2, "Slide 24",
 "What does the wildcard <code>*</code> represent in a Google search phrase such as <code>\"password * file\"</code>?",
 "ماذا يمثّل الرمز <code>*</code> في عبارة بحث مثل <code>\"password * file\"</code>؟",
 [("One or more unknown words within a search phrase", "كلمة أو أكثر مجهولة داخل عبارة البحث"),
  ("A numeric range", "نطاقاً رقمياً"),
  ("An excluded term", "مصطلحاً مستبعداً"),
  ("An exact phrase", "عبارة دقيقة")], 0,
 "Slide 24: <code>*</code> (Wildcard) represents one or more unknown words.",
 "الشريحة ٢٤: الرمز <code>*</code> يمثل كلمة أو أكثر مجهولة.")

mcq(2, "Slide 24",
 "Which symbol searches for values within a specified numeric range (e.g. <code>server 2016..2025</code>)?",
 "أي رمز يبحث عن قيم ضمن نطاق رقمي محدد (مثل <code>server 2016..2025</code>)؟",
 [(".. (Range)", ".. (النطاق)"), ("* (Wildcard)", "* (البدل)"),
  ("- (Minus)", "- (الناقص)"), ("\" \" (Quotes)", "\" \" (علامات الاقتباس)")], 0,
 "Slide 24: <code>..</code> is the range operator.",
 "الشريحة ٢٤: <code>..</code> هو معامل النطاق.")

mcq(2, "Slide 26",
 "What does the dork <code>filetype:sql \"INSERT INTO\"</code> expose?",
 "ماذا يكشف الأمر <code>filetype:sql \"INSERT INTO\"</code>؟",
 [("Database backups/schemas containing usernames, emails and hashed passwords",
   "نسخ قواعد البيانات الاحتياطية ومخططاتها التي تحوي أسماء مستخدمين وبُرد إلكترونية وكلمات مرور مُجزّأة"),
  ("Login pages only", "صفحات تسجيل الدخول فقط"),
  ("Remote access tools", "أدوات الوصول عن بُعد"),
  ("Satellite images", "صور الأقمار الصناعية")], 0,
 "Slide 26: “Exposes database backups/schemas… SQL dumps are frequently left in web roots; contains usernames, emails, hashed passwords.”",
 "الشريحة ٢٦: «يكشف نسخ قواعد البيانات ومخططاتها… غالباً تُترك ملفات SQL في جذور المواقع وتحوي أسماء مستخدمين وبُرداً وكلمات مرور مُجزّأة».")

mcq(2, "Slide 25",
 "The dork <code>allinurl:tsweb/default.htm</code> is used for finding:",
 "الأمر <code>allinurl:tsweb/default.htm</code> يُستخدم لإيجاد:",
 [("Web servers that have a specific remote access tool", "خوادم ويب تحتوي على أداة وصول عن بُعد محددة"),
  ("Exposed SQL databases", "قواعد بيانات SQL مكشوفة"),
  ("Employee e-mail addresses", "عناوين بريد الموظفين"),
  ("Company locations", "مواقع الشركات")], 0,
 "Slide 25 gives this exact example.", "الشريحة ٢٥ تعطي هذا المثال بالتحديد.")

mcq(2, "Slide 28",
 "Shodan is a specialized search engine that searches for:",
 "شودان محرك بحث متخصص يبحث عن:",
 [("Devices connected to the internet", "الأجهزة المتصلة بالإنترنت"),
  ("Websites and documents", "المواقع والمستندات"),
  ("Social media profiles", "ملفات وسائل التواصل"),
  ("E-mail headers", "ترويسات البريد الإلكتروني")], 0,
 "Slide 28: unlike Google (websites &amp; documents), Shodan searches for <b>devices connected to the internet</b>.",
 "الشريحة ٢٨: على عكس جوجل (المواقع والمستندات)، يبحث شودان عن <b>الأجهزة المتصلة بالإنترنت</b>.")

mcq(2, "Slide 28",
 "Which of the following is NOT listed as a device type found by Shodan?",
 "أي مما يلي لم يُذكر كنوع أجهزة يجدها شودان؟",
 [("Encrypted password vaults", "خزائن كلمات المرور المشفرة"),
  ("Webcams and security cameras", "كاميرات الويب وكاميرات المراقبة"),
  ("Industrial control systems (power plants, factories)", "أنظمة التحكم الصناعي (محطات الطاقة والمصانع)"),
  ("Smart home devices (thermostats, doorbells, refrigerators)", "أجهزة المنزل الذكي (منظمات الحرارة، أجراس الأبواب، الثلاجات)")], 0,
 "Slide 28 lists: computers and servers, routers and network equipment, webcams and security cameras, medical devices, industrial control systems, smart home devices.",
 "الشريحة ٢٨ تذكر: الحواسيب والخوادم، الموجّهات ومعدات الشبكة، الكاميرات، الأجهزة الطبية، أنظمة التحكم الصناعي، أجهزة المنزل الذكي.")

mcq(2, "Slide 31",
 "OSINT is best defined as the practice of:",
 "يُعرَّف OSINT بأنه ممارسة:",
 [("Collecting, analyzing, and synthesizing publicly available information to produce actionable intelligence",
   "جمع وتحليل وتركيب المعلومات المتاحة للعامة لإنتاج معلومات استخباراتية قابلة للتنفيذ"),
  ("Scanning networks with open-source tools only", "فحص الشبكات بأدوات مفتوحة المصدر فقط"),
  ("Publishing hacking tools as open source", "نشر أدوات الاختراق كمصدر مفتوح"),
  ("Breaking into open systems", "اقتحام الأنظمة المفتوحة")], 0,
 "Slide 31 gives this definition exactly.", "الشريحة ٣١ تعطي هذا التعريف حرفياً.")

mcq(2, "Slide 32",
 "Maigret is an open-source OSINT tool for Kali Linux that automates the collection of a target's digital footprint by:",
 "Maigret أداة OSINT مفتوحة المصدر لـ Kali Linux تقوم بأتمتة جمع البصمة الرقمية للهدف عن طريق:",
 [("Checking a username against thousands of sites", "فحص اسم مستخدم مقابل آلاف المواقع"),
  ("Scanning all open ports", "فحص جميع المنافذ المفتوحة"),
  ("Mirroring the target website", "نسخ موقع الهدف"),
  ("Reading e-mail headers", "قراءة ترويسات البريد")], 0,
 "Slide 32: Maigret checks a username against thousands of sites — discovering linked accounts, unmasking users, verifying identities.",
 "الشريحة ٣٢: تفحص Maigret اسم المستخدم مقابل آلاف المواقع لاكتشاف الحسابات المرتبطة وكشف الهويات والتحقق منها.")

mcq(2, "Slide 34",
 "Website footprinting is generally considered:",
 "تُعدّ بصمة المواقع الإلكترونية عموماً:",
 [("A passive reconnaissance technique", "تقنية استطلاع سلبية"),
  ("An active reconnaissance technique", "تقنية استطلاع نشطة"),
  ("An enumeration technique", "تقنية تعداد"),
  ("An exploitation technique", "تقنية استغلال")], 0,
 "Slide 34: “Website footprinting is generally considered a <b>passive reconnaissance technique</b>.”",
 "الشريحة ٣٤: «تُعدّ بصمة المواقع عموماً <b>تقنية استطلاع سلبية</b>».")

mcq(2, "Slide 35",
 "Which of the following may be found in a website's HTML source code?",
 "أي مما يلي قد يوجد في كود HTML المصدري للموقع؟",
 [("Hidden form fields, metadata, and developer comments", "حقول نماذج مخفية وبيانات وصفية وتعليقات المطورين"),
  ("Encrypted firewall rules", "قواعد جدار ناري مشفّرة"),
  ("Router CAM tables", "جداول CAM للموجّهات"),
  ("SNMP community strings", "سلاسل مجتمع SNMP")], 0,
 "Slide 35: hidden form fields, metadata and developer comments may reveal structure and technologies; comments may disclose usernames, file paths or configuration details.",
 "الشريحة ٣٥: الحقول المخفية والبيانات الوصفية وتعليقات المطورين قد تكشف البنية والتقنيات، وقد تفصح التعليقات عن أسماء مستخدمين ومسارات وإعدادات.")

mcq(2, "Slide 36",
 "Which of the following is a web mirroring tool listed in the lecture?",
 "أي مما يلي أداة نسخ مواقع مذكورة في المحاضرة؟",
 [("HTTrack", "HTTrack"), ("Nessus", "Nessus"),
  ("Wireshark", "Wireshark"), ("Snmp-check", "Snmp-check")], 0,
 "Slide 36 lists: HTTrack, Black Widow, WebRipper, Teleport Pro, GNU Wget, Backstreet Browser.",
 "الشريحة ٣٦ تذكر: HTTrack و Black Widow و WebRipper و Teleport Pro و GNU Wget و Backstreet Browser.")

mcq(2, "Slide 36",
 "Web mirroring is the process of:",
 "نسخ الموقع (Web mirroring) هو عملية:",
 [("Creating a complete local copy of a website", "إنشاء نسخة محلية كاملة من موقع إلكتروني"),
  ("Copying a switch's traffic to a monitoring port", "نسخ حركة المحوّل إلى منفذ مراقبة"),
  ("Duplicating DNS records", "تكرار سجلات DNS"),
  ("Cloning a MAC address", "استنساخ عنوان MAC")], 0,
 "Slide 36: an offline copy lets you explore structure in detail without repeatedly accessing the target site.",
 "الشريحة ٣٦: النسخة دون اتصال تتيح استكشاف البنية بتفصيل دون الوصول المتكرر للموقع المستهدف.")

mcq(2, "Slide 39",
 "An email header contains technical information that describes:",
 "تحتوي ترويسة البريد الإلكتروني على معلومات تقنية تصف:",
 [("How a message traveled from the sender to the recipient", "كيف انتقلت الرسالة من المرسِل إلى المستلِم"),
  ("The recipient's password", "كلمة مرور المستلِم"),
  ("The web server version", "إصدار خادم الويب"),
  ("The MAC address of the mail client", "عنوان MAC لبرنامج البريد")], 0,
 "Slide 39: headers describe the message's journey; they can be displayed and analyzed using most e-mail clients.",
 "الشريحة ٣٩: تصف الترويسة رحلة الرسالة، ويمكن إظهارها وتحليلها بمعظم برامج البريد.")

mcq(2, "Slide 38",
 "Which of the following may be revealed by e-mail communications?",
 "أي مما يلي قد تكشفه مراسلات البريد الإلكتروني؟",
 [("IP addresses, geographic location, e-mail server details, domain names and communication patterns",
   "عناوين IP والموقع الجغرافي وتفاصيل خادم البريد وأسماء النطاقات وأنماط التواصل"),
  ("Only the message body", "نص الرسالة فقط"),
  ("The firewall configuration", "إعدادات الجدار الناري"),
  ("The CAM table", "جدول CAM")], 0,
 "Slide 38 lists exactly these five items.", "الشريحة ٣٨ تذكر هذه العناصر الخمسة بالضبط.")

mcq(2, "Slide 41",
 "Each DNS server is responsible for managing records within a specific part of the DNS hierarchy, known as a:",
 "كل خادم DNS مسؤول عن إدارة السجلات ضمن جزء محدد من التسلسل الهرمي لـ DNS يُعرف باسم:",
 [("Namespace", "مساحة الأسماء (Namespace)"), ("Subnet", "الشبكة الفرعية"),
  ("Zone file only", "ملف المنطقة فقط"), ("Collision domain", "نطاق التصادم")], 0,
 "Slide 41: that part of the hierarchy is called a <b>namespace</b>.",
 "الشريحة ٤١: ذلك الجزء من التسلسل الهرمي يُسمّى <b>مساحة الأسماء</b>.")

mcq(2, "Slide 42",
 "Large DNS servers may manage top-level domains (TLDs) such as:",
 "قد تدير خوادم DNS الكبيرة نطاقات المستوى الأعلى (TLDs) مثل:",
 [(".com", ".com"), ("mheducation.com", "mheducation.com"),
  ("www.anyname.com", "www.anyname.com"), ("srv1.anyname.com", "srv1.anyname.com")], 0,
 "Slide 42: large servers manage TLDs such as <b>.com</b>, while lower-level servers manage specific domains such as mheducation.com.",
 "الشريحة ٤٢: الخوادم الكبيرة تدير نطاقات المستوى الأعلى مثل <b>.com</b>، والخوادم الأدنى تدير نطاقات محددة مثل mheducation.com.")

mcq(2, "Slide 43",
 "By examining DNS records, an attacker may identify all of the following EXCEPT:",
 "بفحص سجلات DNS قد يحدد المهاجم كل ما يلي ما عدا:",
 [("The users' passwords", "كلمات مرور المستخدمين"),
  ("The authoritative DNS servers", "خوادم DNS الموثوقة"),
  ("E-mail servers used by the organization", "خوادم البريد التي تستخدمها المؤسسة"),
  ("Public-facing web servers", "خوادم الويب العامة")], 0,
 "Slide 43 lists authoritative DNS servers, e-mail servers, public-facing web servers, and other important network resources — not passwords.",
 "الشريحة ٤٣ تذكر خوادم DNS الموثوقة وخوادم البريد وخوادم الويب العامة وموارد شبكية مهمة أخرى — وليس كلمات المرور.")

mcq(2, "Slide 44",
 "Whois queries the registries and returns information including:",
 "تستعلم أداة Whois من السجلات وتُرجع معلومات تشمل:",
 [("Domain ownership, addresses, locations and phone numbers", "ملكية النطاق والعناوين والمواقع وأرقام الهواتف"),
  ("Open ports and services", "المنافذ المفتوحة والخدمات"),
  ("Operating system versions", "إصدارات أنظمة التشغيل"),
  ("MAC addresses", "عناوين MAC")], 0,
 "Slide 44 states exactly this list.", "الشريحة ٤٤ تذكر هذه القائمة بالضبط.")

mcq(2, "Slide 47",
 "Network footprinting is the process of:",
 "بصمة الشبكة هي عملية:",
 [("Identifying and defining the IP address range used by a target organization", "تحديد وتعريف نطاق عناوين IP الذي تستخدمه المؤسسة المستهدفة"),
  ("Capturing packets on the LAN", "التقاط الحزم على الشبكة المحلية"),
  ("Mapping the DNS hierarchy", "رسم التسلسل الهرمي لـ DNS"),
  ("Mirroring a website", "نسخ موقع إلكتروني")], 0,
 "Slide 47: determining the network range reduces the time required for further reconnaissance.",
 "الشريحة ٤٧: تحديد نطاق الشبكة يقلل الوقت اللازم للاستطلاع اللاحق.")

mcq(2, "Slide 48",
 "ARIN stands for:",
 "اختصار ARIN يعني:",
 [("American Registry for Internet Numbers", "السجل الأمريكي لأرقام الإنترنت"),
  ("Advanced Router Identification Network", "شبكة تعريف الموجّهات المتقدمة"),
  ("Automated Registry of IP Names", "السجل الآلي لأسماء IP"),
  ("Association of Regional Internet Nodes", "رابطة عقد الإنترنت الإقليمية")], 0,
 "Slide 48: the <b>American Registry for Internet Numbers</b>, which maintains IP address allocations and network ownership.",
 "الشريحة ٤٨: <b>السجل الأمريكي لأرقام الإنترنت</b>، ويحتفظ بتخصيصات عناوين IP وملكية الشبكات.")

mcq(2, "Slide 48",
 "Which of the following can be obtained by searching an IP address in ARIN?",
 "أي مما يلي يمكن الحصول عليه بالبحث عن عنوان IP في ARIN؟",
 [("Network address range and the organization that owns the IP addresses", "نطاق عناوين الشبكة والمؤسسة المالكة لعناوين IP"),
  ("The web server banner", "لافتة خادم الويب"),
  ("The list of open ports", "قائمة المنافذ المفتوحة"),
  ("The SNMP community string", "سلسلة مجتمع SNMP")], 0,
 "Slide 48: network address range, owning organization, administrative contacts, technical contacts, additional registration details.",
 "الشريحة ٤٨: نطاق العناوين، المؤسسة المالكة، جهات الاتصال الإدارية والتقنية، تفاصيل تسجيل إضافية.")

mcq(2, "Slide 49",
 "Traceroute (tracert in Windows) is a command-line tool used to:",
 "أداة Traceroute (tracert في ويندوز) هي أداة سطر أوامر تُستخدم لـ:",
 [("Track the path that packets take across a network from source to destination", "تتبّع المسار الذي تسلكه الحزم عبر الشبكة من المصدر إلى الوجهة"),
  ("Capture and decode packets", "التقاط الحزم وفك ترميزها"),
  ("Enumerate SNMP devices", "تعداد أجهزة SNMP"),
  ("Mirror a website locally", "نسخ موقع محلياً")], 0,
 "Slide 49 defines traceroute exactly this way.", "الشريحة ٤٩ تعرّف الأداة بهذه الصيغة تماماً.")

mcq(2, "Slide 50",
 "How does traceroute discover the path to a destination?",
 "كيف تكتشف Traceroute المسار إلى الوجهة؟",
 [("By sending packets with gradually increasing TTL values", "بإرسال حزم ذات قيم TTL متزايدة تدريجياً"),
  ("By broadcasting ARP requests", "ببث طلبات ARP"),
  ("By flooding the switch's CAM table", "بإغراق جدول CAM في المحوّل"),
  ("By querying WHOIS repeatedly", "بالاستعلام المتكرر من WHOIS")], 0,
 "Slide 50: each router decrements the TTL by one; when TTL reaches zero the router responds, revealing each hop.",
 "الشريحة ٥٠: كل موجّه ينقص TTL بواحد، وعندما تصل للصفر يرد الموجّه فتظهر كل قفزة.")

mcq(2, "Slide 50",
 "In traceroute, when the TTL reaches zero, what happens?",
 "في Traceroute، ماذا يحدث عندما تصل قيمة TTL إلى الصفر؟",
 [("The router sends a response back to the source", "يرسل الموجّه رداً إلى المصدر"),
  ("The packet is silently discarded with no reply", "تُهمَل الحزمة بصمت دون رد"),
  ("The destination is reached", "يتم الوصول إلى الوجهة"),
  ("The TTL resets to 255", "تُعاد قيمة TTL إلى ٢٥٥")], 0,
 "Slide 50: “When the TTL reaches zero, the router sends a response back to the source.”",
 "الشريحة ٥٠: «عندما تصل TTL إلى الصفر يرسل الموجّه رداً إلى المصدر».")

mcq(2, "Slide 53",
 "Which tool's purpose is to perform OSINT investigations and obtain usernames, e-mail addresses, domains, phone numbers and online profiles?",
 "أي أداة غرضها إجراء تحقيقات OSINT والحصول على أسماء المستخدمين والبريد والنطاقات وأرقام الهواتف والملفات الشخصية؟",
 [("OSRFramework", "OSRFramework"), ("Maltego", "Maltego"),
  ("HTTrack", "HTTrack"), ("Netcraft", "Netcraft")], 0,
 "Slide 53: <b>OSRFramework</b> automates information gathering from multiple public sources.",
 "الشريحة ٥٣: <b>OSRFramework</b> يقوم بأتمتة جمع المعلومات من مصادر عامة متعددة.")

mcq(2, "Slide 55",
 "Which tool's purpose is to analyze and visualize relationships between entities?",
 "أي أداة غرضها تحليل وتصوير العلاقات بين الكيانات بصرياً؟",
 [("Maltego", "Maltego"), ("Web spiders", "عناكب الويب"),
  ("OSRFramework", "OSRFramework"), ("Shodan", "شودان")], 0,
 "Slide 55: <b>Maltego</b> helps correlate information and discover connections that may not be immediately visible.",
 "الشريحة ٥٥: <b>Maltego</b> يساعد على ربط المعلومات واكتشاف الصلات غير الظاهرة مباشرة.")

mcq(2, "Slide 54",
 "Web spiders are used in footprinting to:",
 "تُستخدم عناكب الويب في البصمة لـ:",
 [("Map website structure and identify hidden or forgotten content", "رسم بنية الموقع وتحديد المحتوى المخفي أو المنسي"),
  ("Poison the ARP cache", "تسميم ذاكرة ARP"),
  ("Scan for open TCP ports", "فحص منافذ TCP المفتوحة"),
  ("Read e-mail headers", "قراءة ترويسات البريد")], 0,
 "Slide 54: web spiders crawl websites, collecting web pages, directories, links and publicly accessible resources.",
 "الشريحة ٥٤: تزحف العناكب على المواقع فتجمع الصفحات والمجلدات والروابط والموارد المتاحة للعامة.")

tf(2, "Slide 8",
 "Since no direct contact is made with the target, passive footprinting generally presents a low risk of detection.",
 "لأنه لا يحدث اتصال مباشر بالهدف، فإن البصمة السلبية تمثل عموماً خطراً منخفضاً للاكتشاف.",
 True, "Slide 8 states this literally.", "الشريحة ٨ تنص على ذلك حرفياً.")

tf(2, "Slide 6",
 "Footprinting information must always be technical in nature.",
 "يجب أن تكون معلومات البصمة دائماً ذات طبيعة تقنية.",
 False,
 "Slide 6: “This information <b>does not have to be technical</b>” — useful data includes physical security measures and even employee routines.",
 "الشريحة ٦: «ليس شرطاً أن تكون هذه المعلومات <b>تقنية</b>» — فمن البيانات المفيدة إجراءات الأمن المادي وحتى روتين الموظفين.")

tf(2, "Slide 56",
 "Footprinting is probably the most important phase of hacking you’ll need to master.",
 "البصمة هي على الأرجح أهم مرحلة في الاختراق يجب أن تتقنها.",
 True,
 "Slide 56: spending time in this step drastically increases the odds of success later.",
 "الشريحة ٥٦: قضاء الوقت في هذه الخطوة يزيد بشكل هائل من فرص النجاح لاحقاً.")

sa(2, "Slide 11",
 "List the six footprinting methods and tools categories given in the lecture.",
 "اذكر فئات أساليب وأدوات البصمة الست الواردة في المحاضرة.",
 "<b>Search Engines · Google Hacking · Website Footprinting · Email Footprinting · DNS Footprinting · Network Footprinting</b> (slide 11).",
 "<b>محركات البحث · اختراق جوجل · بصمة المواقع · بصمة البريد · بصمة DNS · بصمة الشبكة</b> (الشريحة ١١).")

sa(2, "Slide 21",
 "Name four kinds of information that Google Dorking may discover.",
 "اذكر أربعة أنواع من المعلومات التي قد يكتشفها Google Dorking.",
 "Any four of: <b>public documents, e-mail addresses, login pages, directory listings, exposed configuration files, publicly accessible reports and presentations</b> (slide 21).",
 "أي أربعة من: <b>المستندات العامة، عناوين البريد، صفحات الدخول، قوائم المجلدات، ملفات الإعدادات المكشوفة، التقارير والعروض المتاحة للعامة</b> (الشريحة ٢١).")

sa(2, "Slide 34",
 "What five things can website analysis reveal?",
 "ما الأشياء الخمسة التي يمكن أن يكشفها تحليل الموقع الإلكتروني؟",
 "<b>Operating system information · Web server details · Software and applications in use · File and directory names · Contact information</b> (slide 34).",
 "<b>معلومات نظام التشغيل · تفاصيل خادم الويب · البرمجيات والتطبيقات المستخدمة · أسماء الملفات والمجلدات · معلومات الاتصال</b> (الشريحة ٣٤).")

# ══════════════════════════════ CHAPTER 3 ══════════════════════════════
mcq(3, "Slide 3",
 "Scanning is the process of:",
 "الفحص (Scanning) هو عملية:",
 [("Discovering systems on the network and looking at what open ports and applications may be running",
   "اكتشاف الأنظمة على الشبكة والاطلاع على المنافذ المفتوحة والتطبيقات التي قد تعمل"),
  ("Gathering public information without touching the target", "جمع معلومات عامة دون لمس الهدف"),
  ("Removing log files after an attack", "حذف ملفات السجل بعد الهجوم"),
  ("Writing the penetration test report", "كتابة تقرير اختبار الاختراق")], 0,
 "Slide 3: with footprinting we learn how big the network is; in scanning we go into the network and touch each device.",
 "الشريحة ٣: في البصمة نعرف حجم الشبكة، وفي الفحص ندخل الشبكة ونلمس كل جهاز.")

mcq(3, "Slide 6",
 "Which protocol establishes NO connection before data transmission (fire-and-forget)?",
 "أي بروتوكول لا يُنشئ أي اتصال قبل إرسال البيانات («أرسل وانسَ»)؟",
 [("UDP", "UDP"), ("TCP", "TCP"), ("ICMP", "ICMP"), ("ARP", "ARP")], 0,
 "Slide 6: UDP is connectionless — fast, low overhead, no guarantee of delivery/ordering/error recovery. Used by DNS, DHCP, VoIP.",
 "الشريحة ٦: UDP بلا اتصال — سريع وبأعباء منخفضة ولا يضمن التسليم أو الترتيب أو معالجة الأخطاء. يستخدمه DNS و DHCP و VoIP.")

mcq(3, "Slide 6",
 "Which of the following applications is given as an example of UDP usage?",
 "أي من التطبيقات التالية ذُكر كمثال على استخدام UDP؟",
 [("DNS, DHCP, VoIP", "DNS و DHCP و VoIP"), ("HTTP, HTTPS, FTP", "HTTP و HTTPS و FTP"),
  ("SSH and Telnet", "SSH و Telnet"), ("SMB and RDP", "SMB و RDP")], 0,
 "Slide 6: UDP is suitable where speed matters more than reliability — DNS, DHCP, VoIP.",
 "الشريحة ٦: UDP مناسب حيث السرعة أهم من الموثوقية — DNS و DHCP و VoIP.")

mcq(3, "Slide 7",
 "Which protocol uses the Three-Way Handshake and provides reliable, ordered, error-checked delivery?",
 "أي بروتوكول يستخدم المصافحة الثلاثية ويوفر تسليماً موثوقاً ومرتباً ومُتحقَّقاً من أخطائه؟",
 [("TCP", "TCP"), ("UDP", "UDP"), ("ICMP", "ICMP"), ("SNMP", "SNMP")], 0,
 "Slide 7: TCP is connection-oriented and suitable for HTTP, HTTPS, FTP, SSH.",
 "الشريحة ٧: TCP موجّه بالاتصال ومناسب لـ HTTP و HTTPS و FTP و SSH.")

mcq(3, "Slide 8",
 "How many flags does the TCP header contain?",
 "كم عَلَماً تحتوي عليه ترويسة TCP؟",
 [("Six", "ستة"), ("Four", "أربعة"), ("Eight", "ثمانية"), ("Two", "اثنان")], 0,
 "Slide 8: six flags — four (SYN, ACK, FIN, RST) govern the connection; two (PSH, URG) give instructions to the system.",
 "الشريحة ٨: ستة أعلام — أربعة (SYN و ACK و FIN و RST) تحكم الاتصال، واثنان (PSH و URG) يعطيان تعليمات للنظام.")

mcq(3, "Slide 8",
 "What is the size of each TCP flag?",
 "ما حجم كل عَلَم من أعلام TCP؟",
 [("1 bit", "بت واحد"), ("1 byte", "بايت واحد"),
  ("16 bits", "١٦ بت"), ("4 bits", "٤ بت")], 0,
 "Slide 8: “The size of each flag is <b>1 bit</b>. When a flag value is set to 1, that flag is turned on.”",
 "الشريحة ٨: «حجم كل عَلَم هو <b>بت واحد</b>، وعندما تُضبط قيمته على ١ يكون مُفعّلاً».")

mcq(3, "Slide 9",
 "Which TCP flag forces a termination of communications in BOTH directions?",
 "أي عَلَم في TCP يفرض إنهاء الاتصالات في كلا الاتجاهين؟",
 [("RST (Reset)", "RST (إعادة الضبط)"), ("FIN (Finish)", "FIN (الإنهاء)"),
  ("PSH (Push)", "PSH (الدفع)"), ("URG (Urgent)", "URG (العاجل)")], 0,
 "Slide 9: <b>RST</b> forces a termination in both directions; <b>FIN</b> signifies an ordered close.",
 "الشريحة ٩: <b>RST</b> يفرض الإنهاء في الاتجاهين، بينما <b>FIN</b> يشير إلى إغلاق منظّم.")

mcq(3, "Slide 9",
 "Which TCP flag signifies an ORDERED close to communications?",
 "أي عَلَم في TCP يشير إلى إغلاق منظّم للاتصالات؟",
 [("FIN", "FIN"), ("RST", "RST"), ("SYN", "SYN"), ("ACK", "ACK")], 0,
 "Slide 9: <b>FIN (Finish)</b>.", "الشريحة ٩: <b>FIN (الإنهاء)</b>.")

mcq(3, "Slide 9",
 "Which TCP flag forces the delivery of data without concern for any buffering?",
 "أي عَلَم في TCP يفرض تسليم البيانات دون الاهتمام بأي تخزين مؤقت؟",
 [("PSH (Push)", "PSH (الدفع)"), ("URG (Urgent)", "URG (العاجل)"),
  ("ACK", "ACK"), ("SYN", "SYN")], 0,
 "Slide 9: <b>PSH</b> — the receiving device need not wait for the buffer to fill up before processing the data.",
 "الشريحة ٩: <b>PSH</b> — لا يحتاج الجهاز المستقبِل لانتظار امتلاء المخزن المؤقت قبل المعالجة.")

mcq(3, "Slide 9",
 "Which TCP flag indicates that data is being sent OUT OF BAND (e.g. cancelling a message mid-stream)?",
 "أي عَلَم في TCP يشير إلى إرسال البيانات خارج النطاق (مثل إلغاء رسالة في منتصف البث)؟",
 [("URG (Urgent)", "URG (العاجل)"), ("PSH (Push)", "PSH (الدفع)"),
  ("RST (Reset)", "RST"), ("FIN (Finish)", "FIN")], 0,
 "Slide 9: <b>URG</b>.", "الشريحة ٩: <b>URG</b>.")

mcq(3, "Slide 10",
 "In the TCP three-way handshake, what does the server send in step 2?",
 "في المصافحة الثلاثية، ماذا يرسل الخادم في الخطوة الثانية؟",
 [("SYN, ACK — acknowledging Ack = x + 1 and sending its own Seq = y", "SYN, ACK — يُقرّ بـ Ack = x + 1 ويرسل Seq = y"),
  ("ACK only", "ACK فقط"), ("RST", "RST"), ("FIN, ACK", "FIN, ACK")], 0,
 "Slide 10: step 2 is <b>SYN-ACK</b>: the server accepts the request, acknowledges Ack = x + 1 and sends Seq = y.",
 "الشريحة ١٠: الخطوة الثانية <b>SYN-ACK</b>: يقبل الخادم الطلب ويُقرّ بـ Ack = x + 1 ويرسل Seq = y.")

mcq(3, "Slide 10",
 "In step 3 of the handshake, the client sends ACK with which value?",
 "في الخطوة الثالثة من المصافحة، يرسل العميل ACK بأي قيمة؟",
 [("Ack = y + 1", "Ack = y + 1"), ("Ack = x + 1", "Ack = x + 1"),
  ("Seq = x", "Seq = x"), ("Seq = 0", "Seq = 0")], 0,
 "Slide 10: the client acknowledges the server's sequence number with <b>Ack = y + 1</b>, completing the connection setup.",
 "الشريحة ١٠: يُقرّ العميل برقم تسلسل الخادم بـ <b>Ack = y + 1</b> فيكتمل إنشاء الاتصال.")

mcq(3, "Slide 13",
 "A port number is a logical identifier used by TCP and UDP to determine:",
 "رقم المنفذ معرّف منطقي يستخدمه TCP و UDP لتحديد:",
 [("Which application should receive incoming data", "أي تطبيق يجب أن يستقبل البيانات الواردة"),
  ("Which router forwards the packet", "أي موجّه يمرّر الحزمة"),
  ("The MAC address of the sender", "عنوان MAC للمرسِل"),
  ("The encryption algorithm", "خوارزمية التشفير")], 0,
 "Slide 13: the OS uses the destination port to deliver the packet to the correct application.",
 "الشريحة ١٣: يستخدم نظام التشغيل منفذ الوجهة لتسليم الحزمة إلى التطبيق الصحيح.")

mcq(3, "Slide 15",
 "Which port is used by SSH (Secure Remote Login)?",
 "أي منفذ يستخدمه SSH (الدخول الآمن عن بُعد)؟",
 [("22", "٢٢"), ("23", "٢٣"), ("25", "٢٥"), ("21", "٢١")], 0,
 "Slide 15: SSH = port <b>22</b>; Telnet = 23; SMTP = 25; FTP = 20/21.",
 "الشريحة ١٥: SSH = المنفذ <b>٢٢</b>، Telnet = ٢٣، SMTP = ٢٥، FTP = ٢٠/٢١.")

mcq(3, "Slide 15",
 "Which protocol uses ports 20/21?",
 "أي بروتوكول يستخدم المنفذين ٢٠/٢١؟",
 [("FTP", "FTP"), ("SSH", "SSH"), ("DHCP", "DHCP"), ("TFTP", "TFTP")], 0,
 "Slide 15: FTP (File Transfer Protocol) = <b>20/21</b>.",
 "الشريحة ١٥: بروتوكول نقل الملفات FTP = <b>٢٠/٢١</b>.")

mcq(3, "Slide 15",
 "Which port number does DNS use?",
 "أي رقم منفذ يستخدمه DNS؟",
 [("53", "٥٣"), ("69", "٦٩"), ("110", "١١٠"), ("161", "١٦١")], 0,
 "Slide 15: DNS (Domain Name Service) = port <b>53</b>.",
 "الشريحة ١٥: خدمة أسماء النطاقات DNS = المنفذ <b>٥٣</b>.")

mcq(3, "Slide 15",
 "SNMP (Network Management) uses which port?",
 "أي منفذ يستخدمه SNMP (إدارة الشبكة)؟",
 [("161", "١٦١"), ("143", "١٤٣"), ("389", "٣٨٩"), ("445", "٤٤٥")], 0,
 "Slide 15: SNMP = <b>161</b>; IMAP = 143; LDAP = 389; SMB = 445.",
 "الشريحة ١٥: SNMP = <b>١٦١</b>، IMAP = ١٤٣، LDAP = ٣٨٩، SMB = ٤٤٥.")

mcq(3, "Slide 15",
 "Which port is used for RDP (Remote Desktop)?",
 "أي منفذ يُستخدم لسطح المكتب البعيد RDP؟",
 [("3389", "٣٣٨٩"), ("445", "٤٤٥"), ("443", "٤٤٣"), ("389", "٣٨٩")], 0,
 "Slide 15: RDP = <b>3389</b>.", "الشريحة ١٥: RDP = <b>٣٣٨٩</b>.")

mcq(3, "Slide 15",
 "Windows File Sharing (SMB) uses which port?",
 "أي منفذ تستخدمه مشاركة ملفات ويندوز (SMB)؟",
 [("445", "٤٤٥"), ("139", "١٣٩"), ("443", "٤٤٣"), ("161", "١٦١")], 0,
 "Slide 15: SMB = <b>445</b>.", "الشريحة ١٥: SMB = <b>٤٤٥</b>.")

mcq(3, "Slide 15",
 "Which two ports are used by DHCP for automatic IP assignment?",
 "أي منفذين يستخدمهما DHCP لتعيين عناوين IP تلقائياً؟",
 [("67/68", "٦٧/٦٨"), ("20/21", "٢٠/٢١"), ("110/143", "١١٠/١٤٣"), ("137/139", "١٣٧/١٣٩")], 0,
 "Slide 15: DHCP = <b>67/68</b>.", "الشريحة ١٥: DHCP = <b>٦٧/٦٨</b>.")

mcq(3, "Slide 16",
 "Which port state means “Local host has closed the connection but waits for delayed packets before fully closing”?",
 "أي حالة منفذ تعني «الجهاز المحلي أغلق الاتصال لكنه ينتظر الحزم المتأخرة قبل الإغلاق التام»؟",
 [("TIME_WAIT", "TIME_WAIT"), ("CLOSE_WAIT", "CLOSE_WAIT"),
  ("ESTABLISHED", "ESTABLISHED"), ("LISTENING", "LISTENING")], 0,
 "Slide 16: <b>TIME_WAIT</b>. CLOSE_WAIT means the <i>remote</i> host has closed the connection.",
 "الشريحة ١٦: <b>TIME_WAIT</b>. أما CLOSE_WAIT فتعني أن الجهاز <i>البعيد</i> أغلق الاتصال.")

mcq(3, "Slide 16",
 "Which command is used to view port states in Windows?",
 "أي أمر يُستخدم لعرض حالات المنافذ في ويندوز؟",
 [("netstat -an", "netstat -an"), ("ipconfig /all", "ipconfig /all"),
  ("tracert -d", "tracert -d"), ("nmap -sS", "nmap -sS")], 0,
 "Slide 16: <code>cmd&gt;&gt; netstat -an</code>.", "الشريحة ١٦: <code>cmd&gt;&gt; netstat -an</code>.")

mcq(3, "Slide 17",
 "What is the FIRST step of the scanning methodology?",
 "ما الخطوة الأولى في منهجية الفحص؟",
 [("Check for live systems", "التحقق من الأنظمة النشطة"),
  ("Check for open ports", "التحقق من المنافذ المفتوحة"),
  ("Perform banner grabbing", "التقاط اللافتات"),
  ("Prepare proxies", "تجهيز الوسطاء")], 0,
 "Slide 17: step 1 — check for live systems (something as simple as a ping).",
 "الشريحة ١٧: الخطوة ١ — التحقق من الأنظمة النشطة (شيء بسيط مثل ping).")

mcq(3, "Slide 18",
 "What is the LAST (7th) step of the scanning methodology?",
 "ما الخطوة الأخيرة (السابعة) في منهجية الفحص؟",
 [("Prepare proxies", "تجهيز الوسطاء (Proxies)"),
  ("Draw network diagrams", "رسم مخططات الشبكة"),
  ("Scan for vulnerabilities", "فحص الثغرات"),
  ("Perform banner grabbing", "التقاط اللافتات")], 0,
 "Slide 18: step 7 — prepare proxies; “this obscures your efforts to keep you hidden”.",
 "الشريحة ١٨: الخطوة ٧ — تجهيز الوسطاء؛ «هذا يُخفي جهودك ويبقيك مستتراً».")

mcq(3, "Slide 18",
 "Which methodology step tells you what operating system is on the machines and which services they are running?",
 "أي خطوة في المنهجية تخبرك بنظام التشغيل على الأجهزة والخدمات التي تعمل عليها؟",
 [("Banner grabbing and OS fingerprinting", "التقاط اللافتات وبصمة نظام التشغيل"),
  ("Checking for live systems", "التحقق من الأنظمة النشطة"),
  ("Preparing proxies", "تجهيز الوسطاء"),
  ("Drawing network diagrams", "رسم مخططات الشبكة")], 0,
 "Slide 18: step 4 — perform banner grabbing.", "الشريحة ١٨: الخطوة ٤ — التقاط اللافتات.")

mcq(3, "Slide 20",
 "Host discovery is the process of identifying which devices on a network are online (alive) BEFORE:",
 "اكتشاف الأجهزة هو عملية تحديد الأجهزة المتصلة (النشطة) على الشبكة قبل:",
 [("Performing further scanning", "إجراء فحص إضافي"),
  ("Writing the report", "كتابة التقرير"),
  ("Gathering public information", "جمع المعلومات العامة"),
  ("Covering tracks", "تغطية الآثار")], 0,
 "Slide 20: it identifies active hosts, eliminates inactive IPs, reduces scanning time and focuses later scans on reachable systems.",
 "الشريحة ٢٠: يحدد الأجهزة النشطة ويستبعد غير النشطة ويقلل وقت الفحص ويركّز الفحوصات اللاحقة على الأنظمة المتاحة.")

mcq(3, "Slide 20",
 "Which of these is NOT listed as a common host discovery method?",
 "أي مما يلي لم يُذكر كطريقة شائعة لاكتشاف الأجهزة؟",
 [("SNMP Sweep", "مسح SNMP"), ("ICMP Ping", "ICMP Ping"),
  ("ARP Scan (Local networks)", "فحص ARP (الشبكات المحلية)"), ("TCP Ping", "TCP Ping")], 0,
 "Slide 20 lists ICMP Ping, ARP Scan, TCP Ping and UDP Ping.",
 "الشريحة ٢٠ تذكر ICMP Ping وفحص ARP و TCP Ping و UDP Ping.")

mcq(3, "Slide 21",
 "ICMP is a protocol operating at which OSI layer, used for error reporting, network diagnostics and connectivity testing?",
 "ICMP بروتوكول يعمل في أي طبقة، ويُستخدم للإبلاغ عن الأخطاء وتشخيص الشبكة واختبار الاتصال؟",
 [("Network Layer", "طبقة الشبكة"), ("Data Link Layer", "طبقة ربط البيانات"),
  ("Transport Layer", "طبقة النقل"), ("Application Layer", "طبقة التطبيق")], 0,
 "Slide 21: ICMP is a <b>Network Layer</b> protocol.",
 "الشريحة ٢١: ICMP بروتوكول في <b>طبقة الشبكة</b>.")

mcq(3, "Slide 22",
 "Which ICMP type number is the Echo REQUEST sent by the scanner?",
 "ما رقم نوع ICMP لطلب الصدى (Echo Request) الذي يرسله الفاحص؟",
 [("Type 8", "النوع ٨"), ("Type 0", "النوع ٠"),
  ("Type 3", "النوع ٣"), ("Type 11", "النوع ١١")], 0,
 "Slide 22: Type 8 = Echo Request; Type 0 = Echo Reply; Type 3 = Destination Unreachable.",
 "الشريحة ٢٢: النوع ٨ = طلب الصدى، النوع ٠ = رد الصدى، النوع ٣ = تعذّر الوصول للوجهة.")

mcq(3, "Slide 22",
 "If a host replies with ICMP Type 0 (Echo Reply), the host is considered:",
 "إذا رد الجهاز برسالة ICMP من النوع ٠ (رد الصدى)، فإنه يُعتبر:",
 [("Alive", "نشطاً/حيّاً"), ("Filtered", "مُرشَّحاً"),
  ("Closed", "مغلقاً"), ("Unreachable", "غير قابل للوصول")], 0,
 "Slide 22 NOTE: “If a host replies with Echo Reply (Type 0), it is considered <b>alive</b>.”",
 "ملاحظة الشريحة ٢٢: «إذا ردّ الجهاز بـ Echo Reply (النوع ٠) فإنه يُعتبر <b>نشطاً</b>».")

mcq(3, "Slide 22",
 "ICMP Type 3 means:",
 "ICMP من النوع ٣ يعني:",
 [("Destination Unreachable", "تعذّر الوصول إلى الوجهة"), ("Echo Reply", "رد الصدى"),
  ("Echo Request", "طلب الصدى"), ("Time Exceeded", "انتهاء الوقت")], 0,
 "Slide 22: Type 3 = Destination Unreachable (host or network cannot be reached).",
 "الشريحة ٢٢: النوع ٣ = تعذّر الوصول (لا يمكن الوصول إلى الجهاز أو الشبكة).")

mcq(3, "Slide 23",
 "Which of the following is a LIMITATION of a ping sweep?",
 "أي مما يلي يُعد قيداً على مسح Ping؟",
 [("Firewalls may block ICMP and many systems disable ping responses", "قد تحجب الجدران النارية ICMP وكثير من الأنظمة تعطّل الرد"),
  ("It is too slow to run", "أنه بطيء جداً"),
  ("It cannot be detected by IDS", "أنه لا يمكن لأنظمة IDS اكتشافه"),
  ("It only works on IPv6", "أنه يعمل على IPv6 فقط")], 0,
 "Slide 23: limitations — firewalls may block ICMP, systems disable ping responses, IDS/IPS may detect sweeps, less effective in some IPv6 environments.",
 "الشريحة ٢٣: القيود — حجب ICMP، تعطيل الرد، اكتشاف IDS/IPS، وأقل فعالية في بعض بيئات IPv6.")

mcq(3, "Slide 24",
 "According to the lecture, which is the MOST commonly used host discovery tool?",
 "حسب المحاضرة، ما أكثر أدوات اكتشاف الأجهزة استخداماً؟",
 [("Nmap", "Nmap"), ("SuperScan", "SuperScan"),
  ("Pinkie", "Pinkie"), ("OPUtils", "OPUtils")], 0,
 "Slide 24 NOTE: “<b>Nmap</b> is the most commonly used host discovery tool.”",
 "ملاحظة الشريحة ٢٤: «<b>Nmap</b> هي أكثر أدوات اكتشاف الأجهزة استخداماً».")

mcq(3, "Slide 26",
 "Port scanning determines which TCP/UDP ports are:",
 "فحص المنافذ يحدد أي منافذ TCP/UDP تكون:",
 [("Open, closed, or filtered", "مفتوحة أو مغلقة أو مُرشَّحة"),
  ("Encrypted or plain", "مشفّرة أو غير مشفّرة"),
  ("Wired or wireless", "سلكية أو لاسلكية"),
  ("Static or dynamic", "ثابتة أو ديناميكية")], 0,
 "Slide 26: a port scanner manipulates TCP flags and analyzes responses to determine each port's state.",
 "الشريحة ٢٦: يتلاعب الفاحص بأعلام TCP ويحلل الردود لتحديد حالة كل منفذ.")

mcq(3, "Slide 27",
 "Which scan type is also called the “Full Open Scan” because it completes the TCP three-way handshake?",
 "أي نوع فحص يُسمى أيضاً «الفحص المفتوح الكامل» لأنه يُكمل المصافحة الثلاثية؟",
 [("TCP Connect Scan", "فحص الاتصال الكامل TCP Connect"),
  ("SYN Scan", "فحص SYN"), ("XMAS Scan", "فحص XMAS"), ("Idle Scan", "الفحص الخامل")], 0,
 "Slide 27: TCP Connect Scan = Full Open Scan.",
 "الشريحة ٢٧: فحص TCP Connect = الفحص المفتوح الكامل.")

mcq(3, "Slide 27",
 "The SYN Scan is also called:",
 "فحص SYN يُسمى أيضاً:",
 [("Half-Open / Stealth Scan", "الفحص نصف المفتوح / الخفي"),
  ("Full Open Scan", "الفحص المفتوح الكامل"),
  ("Inverse TCP Flag Scan", "فحص الأعلام العكسية"),
  ("Zombie Scan", "فحص الزومبي")], 0,
 "Slide 27: SYN Scan = Half-Open / Stealth Scan; it stops before completing the handshake.",
 "الشريحة ٢٧: فحص SYN = نصف مفتوح/خفي، ويتوقف قبل إكمال المصافحة.")

mcq(3, "Slide 27",
 "The Idle Scan is also known as:",
 "الفحص الخامل يُعرف أيضاً باسم:",
 [("Zombie Scan", "فحص الزومبي"), ("Stealth Scan", "الفحص الخفي"),
  ("Window Scan", "فحص النافذة"), ("ACK Scan", "فحص ACK")], 0,
 "Slide 27: Idle Scan = Zombie Scan; it uses a third-party (idle) host to hide the attacker's IP.",
 "الشريحة ٢٧: الفحص الخامل = فحص الزومبي، يستخدم جهازاً خاملاً كطرف ثالث لإخفاء IP المهاجم.")

mcq(3, "Slide 29",
 "Which flags are sent in an XMAS scan?",
 "أي أعلام تُرسَل في فحص XMAS؟",
 [("FIN + PSH + URG", "FIN + PSH + URG"), ("SYN + ACK", "SYN + ACK"),
  ("No flags", "بدون أعلام"), ("FIN only", "FIN فقط")], 0,
 "Slide 29: FIN scan sends FIN; NULL scan sends no flags; XMAS sends <b>FIN + PSH + URG</b>.",
 "الشريحة ٢٩: فحص FIN يرسل FIN، وفحص NULL بدون أعلام، وXMAS يرسل <b>FIN + PSH + URG</b>.")

mcq(3, "Slide 29",
 "In an inverse TCP flag scan (FIN/NULL/XMAS), what response indicates the port is OPEN?",
 "في فحص الأعلام العكسية (FIN/NULL/XMAS)، أي رد يدل على أن المنفذ مفتوح؟",
 [("No response", "لا يوجد رد"), ("RST", "RST"),
  ("SYN/ACK", "SYN/ACK"), ("ICMP Type 3", "ICMP نوع ٣")], 0,
 "Slide 29: Open → <b>No Response</b>; Closed → <b>RST</b>.",
 "الشريحة ٢٩: مفتوح ← <b>لا يوجد رد</b>، مغلق ← <b>RST</b>.")

mcq(3, "Slide 29",
 "In a NULL scan, which flags are sent?",
 "في فحص NULL، أي أعلام تُرسَل؟",
 [("No flags", "بدون أعلام"), ("FIN", "FIN"),
  ("FIN + PSH + URG", "FIN + PSH + URG"), ("SYN", "SYN")], 0,
 "Slide 29: the NULL scan sends <b>no flags</b>.",
 "الشريحة ٢٩: فحص NULL يُرسَل <b>بدون أعلام</b>.")

mcq(3, "Slide 30",
 "In an idle (zombie) scan, what does the attacker observe to determine whether the target port is open or closed?",
 "في الفحص الخامل (الزومبي)، ماذا يراقب المهاجم لتحديد ما إذا كان منفذ الهدف مفتوحاً أم مغلقاً؟",
 [("Changes in the zombie's IP Identification (IPID) value", "التغيرات في قيمة معرّف IP (IPID) لدى الزومبي"),
  ("The target's TTL value", "قيمة TTL لدى الهدف"),
  ("The zombie's MAC address", "عنوان MAC للزومبي"),
  ("The banner returned by the service", "اللافتة التي تعيدها الخدمة")], 0,
 "Slide 30: identify an idle host, send spoofed packets using its IP, observe IPID changes.",
 "الشريحة ٣٠: تحديد جهاز خامل، إرسال حزم منتحَلة بعنوانه، ومراقبة تغيرات IPID.")

mcq(3, "Slide 36",
 "Which Nmap switch performs a TCP SYN (Stealth) Scan?",
 "أي خيار في Nmap ينفّذ فحص SYN (الخفي)؟",
 [("-sS", "-sS"), ("-sT", "-sT"), ("-sX", "-sX"), ("-sA", "-sA")], 0,
 "Slide 36: <code>-sS</code> = TCP SYN Scan (Stealth Scan).",
 "الشريحة ٣٦: <code>-sS</code> = فحص SYN الخفي.")

mcq(3, "Slide 36",
 "Which Nmap switch performs Operating System detection?",
 "أي خيار في Nmap ينفّذ كشف نظام التشغيل؟",
 [("-O", "-O"), ("-sV", "-sV"), ("-oN", "-oN"), ("-Pn", "-Pn")], 0,
 "Slide 36: <code>-O</code> = OS Detection; <code>-sV</code> = Service &amp; Version Detection.",
 "الشريحة ٣٦: <code>-O</code> = كشف نظام التشغيل، <code>-sV</code> = كشف الخدمة والإصدار.")

mcq(3, "Slide 36",
 "Which Nmap switch performs an Aggressive Scan (OS, Version, Scripts, Traceroute)?",
 "أي خيار في Nmap ينفّذ الفحص الشامل العدواني (نظام التشغيل، الإصدار، السكربتات، تتبع المسار)؟",
 [("-A", "-A"), ("-T4", "-T4"), ("-f", "-f"), ("-sW", "-sW")], 0,
 "Slide 36: <code>-A</code> = Aggressive Scan.",
 "الشريحة ٣٦: <code>-A</code> = الفحص العدواني الشامل.")

mcq(3, "Slide 36",
 "Which Nmap switch skips host discovery?",
 "أي خيار في Nmap يتخطى اكتشاف الأجهزة؟",
 [("-Pn", "-Pn"), ("-oN", "-oN"), ("-sI", "-sI"), ("-sF", "-sF")], 0,
 "Slide 36: <code>-Pn</code> = Skip Host Discovery.",
 "الشريحة ٣٦: <code>-Pn</code> = تخطّي اكتشاف الأجهزة.")

mcq(3, "Slide 36 / 45",
 "Which Nmap switch fragments packets for evasion?",
 "أي خيار في Nmap يجزّئ الحزم للتهرب من الكشف؟",
 [("-f", "-f"), ("-T4", "-T4"), ("-sA", "-sA"), ("-oN", "-oN")], 0,
 "Slide 36 &amp; 45: <code>-f</code> tells Nmap to send fragmented packets — e.g. <code>nmap -sS -A -f 172.17.15.12</code>.",
 "الشريحتان ٣٦ و٤٥: <code>-f</code> يخبر Nmap بإرسال حزم مجزّأة — مثل <code>nmap -sS -A -f 172.17.15.12</code>.")

mcq(3, "Slide 36",
 "Which Nmap switch is used for a Service &amp; Version Detection?",
 "أي خيار في Nmap يُستخدم لكشف الخدمة والإصدار؟",
 [("-sV", "-sV"), ("-O", "-O"), ("-sT", "-sT"), ("-sX", "-sX")], 0,
 "Slide 36: <code>-sV</code>.", "الشريحة ٣٦: <code>-sV</code>.")

mcq(3, "Slide 35",
 "What is the correct Nmap syntax given in the lecture?",
 "ما صيغة Nmap الصحيحة الواردة في المحاضرة؟",
 [("Nmap &lt;option&gt; &lt;Target IP address&gt;", "Nmap &lt;الخيار&gt; &lt;عنوان IP للهدف&gt;"),
  ("Nmap &lt;Target IP address&gt; only", "Nmap &lt;عنوان IP&gt; فقط"),
  ("Nmap --scan &lt;IP&gt;", "Nmap --scan &lt;IP&gt;"),
  ("Nmap -run &lt;IP&gt; -option", "Nmap -run &lt;IP&gt; -option")], 0,
 "Slide 35: <code>Nmap &lt;option&gt;&lt;Target IP address&gt;</code>.",
 "الشريحة ٣٥: <code>Nmap &lt;الخيار&gt;&lt;عنوان IP&gt;</code>.")

mcq(3, "Slide 38",
 "Hping3 is best described as:",
 "أفضل وصف لأداة Hping3 هو:",
 [("A command-line network scanning and packet crafting tool for TCP/IP", "أداة سطر أوامر لفحص الشبكة وصياغة الحزم لبروتوكول TCP/IP"),
  ("A graphical vulnerability scanner", "فاحص ثغرات رسومي"),
  ("A web mirroring tool", "أداة نسخ مواقع"),
  ("An IDS", "نظام كشف تسلل")], 0,
 "Slide 38: hping3 sends ICMP echo requests and supports TCP, UDP, ICMP and raw-IP; used for security auditing, firewall testing and remote OS fingerprinting.",
 "الشريحة ٣٨: hping3 يرسل طلبات ICMP ويدعم TCP و UDP و ICMP و raw-IP، ويُستخدم للتدقيق الأمني واختبار الجدران النارية وبصمة نظام التشغيل عن بُعد.")

mcq(3, "Slide 43",
 "The objective of scan evasion is:",
 "الهدف من التهرب أثناء الفحص هو:",
 [("Not to make scanning faster, but to make it harder to detect", "ليس جعل الفحص أسرع، بل جعله أصعب في الاكتشاف"),
  ("To make scanning faster", "جعل الفحص أسرع"),
  ("To increase the number of open ports", "زيادة عدد المنافذ المفتوحة"),
  ("To disable the target firewall", "تعطيل جدار الحماية لدى الهدف")], 0,
 "Slide 43 NOTE states exactly this.", "ملاحظة الشريحة ٤٣ تنص على ذلك تماماً.")

mcq(3, "Slide 44",
 "Which of the following are the three major evasion techniques listed?",
 "ما تقنيات التهرب الرئيسية الثلاث المذكورة؟",
 [("Packet Fragmentation, IP Address Spoofing, Proxy Servers", "تجزئة الحزم، انتحال عنوان IP، الخوادم الوسيطة"),
  ("Banner grabbing, NetBIOS, SNMP", "التقاط اللافتات، NetBIOS، SNMP"),
  ("MAC flooding, ARP spoofing, DHCP starvation", "إغراق MAC، تسميم ARP، تجويع DHCP"),
  ("Nessus, OpenVAS, Qualys", "Nessus، OpenVAS، Qualys")], 0,
 "Slide 44: Packet Fragmentation · IP Address Spoofing · Proxy Servers.",
 "الشريحة ٤٤: تجزئة الحزم · انتحال IP · الخوادم الوسيطة.")

mcq(3, "Slide 45",
 "In packet fragmentation, which device reassembles the fragments?",
 "في تجزئة الحزم، أي جهاز يعيد تجميع الأجزاء؟",
 [("The destination host", "الجهاز الوجهة"), ("The first router", "أول موجّه"),
  ("The IDS", "نظام كشف التسلل"), ("The proxy server", "الخادم الوسيط")], 0,
 "Slide 45: “The <b>destination host</b> reassembles the fragments.”",
 "الشريحة ٤٥: «<b>الجهاز الوجهة</b> يعيد تجميع الأجزاء».")

mcq(3, "Slide 46",
 "Which of the following tools is listed for IP address spoofing?",
 "أي من الأدوات التالية مذكورة لانتحال عنوان IP؟",
 [("Hping, Scapy, Nmap, Ettercap, Cain", "Hping و Scapy و Nmap و Ettercap و Cain"),
  ("Nessus, OpenVAS, Qualys", "Nessus و OpenVAS و Qualys"),
  ("HTTrack, Wget, Teleport Pro", "HTTrack و Wget و Teleport Pro"),
  ("Telnet, Netcat, Nmap", "Telnet و Netcat و Nmap")], 0,
 "Slide 46 lists Hping, Scapy, Nmap, Ettercap and Cain.",
 "الشريحة ٤٦ تذكر Hping و Scapy و Nmap و Ettercap و Cain.")

mcq(3, "Slide 47",
 "Which statement correctly distinguishes a proxy from IP spoofing?",
 "أي عبارة تميّز البروكسي عن انتحال IP بشكل صحيح؟",
 [("A proxy uses a real intermediary server and replies return through it; spoofing uses a fake source IP and may not receive replies",
   "البروكسي يستخدم خادماً وسيطاً حقيقياً وتعود الردود عبره، أما الانتحال فيستخدم IP مزيفاً وقد لا يستقبل الردود"),
  ("A proxy uses a fake source IP; spoofing uses a real server", "البروكسي يستخدم IP مزيفاً والانتحال يستخدم خادماً حقيقياً"),
  ("Both hide only the location", "كلاهما يُخفي الموقع فقط"),
  ("Neither hides the identity", "لا أحد منهما يُخفي الهوية")], 0,
 "Slide 47 table: spoofing → fake source IP, may not receive replies, hides identity. Proxy → real intermediary, replies return through it, hides identity <b>and</b> location.",
 "جدول الشريحة ٤٧: الانتحال ← IP مزيف وقد لا يستقبل ردوداً ويُخفي الهوية. البروكسي ← وسيط حقيقي وتعود الردود عبره ويُخفي الهوية <b>والموقع</b>.")

mcq(3, "Slide 48",
 "In a proxy chain, what does each proxy know?",
 "في سلسلة البروكسي، ماذا يعرف كل بروكسي؟",
 [("Only the previous and next hop", "القفزة السابقة والتالية فقط"),
  ("The full path", "المسار الكامل"),
  ("The attacker's real IP", "عنوان IP الحقيقي للمهاجم"),
  ("Nothing at all", "لا شيء إطلاقاً")], 0,
 "Slide 48: each proxy only knows the previous and next hop, making tracing the source more difficult.",
 "الشريحة ٤٨: كل بروكسي يعرف القفزة السابقة والتالية فقط، مما يصعّب تتبّع المصدر.")

mcq(3, "Slide 48",
 "Which is a LIMITATION of proxy chains?",
 "أي مما يلي يُعد قيداً على سلاسل البروكسي؟",
 [("Increased communication delay (latency)", "زيادة تأخير الاتصال (Latency)"),
  ("They reveal the attacker's IP", "أنها تكشف IP المهاجم"),
  ("They cannot hide identity", "أنها لا تستطيع إخفاء الهوية"),
  ("They only work with UDP", "أنها تعمل مع UDP فقط")], 0,
 "Slide 48: latency, dependence on each proxy's reliability, and some proxies may log user activity.",
 "الشريحة ٤٨: التأخير، والاعتماد على موثوقية كل بروكسي، وبعضها قد يسجّل نشاط المستخدم.")

mcq(3, "Slide 50",
 "Vulnerability scanning compares the target's configuration and software against:",
 "يقارن فحص الثغرات إعدادات الهدف وبرمجياته بـ:",
 [("A database of known vulnerabilities", "قاعدة بيانات للثغرات المعروفة"),
  ("The CAM table", "جدول CAM"),
  ("WHOIS registry records", "سجلات WHOIS"),
  ("The DNS namespace", "مساحة أسماء DNS")], 0,
 "Slide 50: it identifies known security weaknesses by comparing against a vulnerability database.",
 "الشريحة ٥٠: يحدد نقاط الضعف المعروفة بالمقارنة مع قاعدة بيانات الثغرات.")

mcq(3, "Slide 51",
 "How many steps does the vulnerability scanning process have?",
 "كم خطوة تتكون منها عملية فحص الثغرات؟",
 [("Five", "خمس"), ("Three", "ثلاث"), ("Seven", "سبع"), ("Four", "أربع")], 0,
 "Slide 51: “The process of vulnerability scanning has <b>five steps</b>.” (Identify Target → Collect System Information → Compare with Vulnerability Database → Detect Security Weaknesses → Generate Scan Report)",
 "الشريحة ٥١: «تتكون عملية فحص الثغرات من <b>خمس خطوات</b>»: تحديد الهدف ← جمع المعلومات ← المقارنة بقاعدة الثغرات ← كشف نقاط الضعف ← إنشاء التقرير.")

mcq(3, "Slide 51",
 "Which severity levels are listed in a typical vulnerability report?",
 "ما مستويات الخطورة المذكورة في تقرير الثغرات النموذجي؟",
 [("Critical, High, Medium, Low", "حرج، عالٍ، متوسط، منخفض"),
  ("Red, Orange, Yellow, Green", "أحمر، برتقالي، أصفر، أخضر"),
  ("Severe, Moderate, Minor", "شديد، معتدل، طفيف"),
  ("Level 1 to Level 5", "المستوى ١ إلى ٥")], 0,
 "Slide 51: severity level = Critical, High, Medium, Low.",
 "الشريحة ٥١: مستوى الخطورة = حرج، عالٍ، متوسط، منخفض.")

mcq(3, "Slide 52",
 "Which vulnerability scanner is described as “free and open-source with extensive scanning capabilities”?",
 "أي فاحص ثغرات يوصف بأنه «مجاني ومفتوح المصدر بقدرات فحص واسعة»؟",
 [("OpenVAS (Greenbone)", "OpenVAS (Greenbone)"), ("Nessus", "Nessus"),
  ("Qualys VMDR", "Qualys VMDR"), ("GFI LanGuard", "GFI LanGuard")], 0,
 "Slide 52: OpenVAS (Greenbone) is free and open source. Nessus is the widely used <i>commercial</i> scanner.",
 "الشريحة ٥٢: OpenVAS مجاني ومفتوح المصدر، بينما Nessus هو الفاحص <i>التجاري</i> واسع الاستخدام.")

mcq(3, "Slide 52",
 "Which tool is a legacy Microsoft tool for identifying missing Windows updates and security misconfigurations?",
 "أي أداة هي أداة مايكروسوفت القديمة لتحديد تحديثات ويندوز المفقودة وأخطاء الإعدادات الأمنية؟",
 [("MBSA", "MBSA"), ("Nessus", "Nessus"),
  ("OpenVAS", "OpenVAS"), ("Qualys VMDR", "Qualys VMDR")], 0,
 "Slide 52: Microsoft Baseline Security Analyzer (<b>MBSA</b>).",
 "الشريحة ٥٢: محلل أمان مايكروسوفت الأساسي (<b>MBSA</b>).")

mcq(3, "Slide 52",
 "Which vulnerability tool is described as a cloud-based vulnerability management and compliance platform?",
 "أي أداة ثغرات توصف بأنها منصة سحابية لإدارة الثغرات والامتثال؟",
 [("Qualys VMDR", "Qualys VMDR"), ("GFI LanGuard", "GFI LanGuard"),
  ("Nessus", "Nessus"), ("MBSA", "MBSA")], 0,
 "Slide 52: <b>Qualys VMDR</b>.", "الشريحة ٥٢: <b>Qualys VMDR</b>.")

mcq(3, "Slide 54",
 "Enumeration is the process of:",
 "التعداد (Enumeration) هو عملية:",
 [("Actively collecting detailed information from a target system", "جمع معلومات تفصيلية بشكل نشط من النظام المستهدف"),
  ("Passively browsing public web pages", "تصفح صفحات الويب العامة بشكل سلبي"),
  ("Deleting log files", "حذف ملفات السجل"),
  ("Encrypting network traffic", "تشفير حركة الشبكة")], 0,
 "Slide 54: it involves establishing connections with services and requesting specific information.",
 "الشريحة ٥٤: يتضمن إنشاء اتصالات مع الخدمات وطلب معلومات محددة.")

mcq(3, "Slide 55",
 "Which statement correctly compares scanning and enumeration?",
 "أي عبارة تقارن بين الفحص والتعداد بشكل صحيح؟",
 [("Scanning answers “What is available?” and enumeration answers “What information can be obtained?”",
   "الفحص يجيب «ما المتاح؟» والتعداد يجيب «ما المعلومات التي يمكن الحصول عليها؟»"),
  ("Scanning is more interactive than enumeration", "الفحص أكثر تفاعلية من التعداد"),
  ("Enumeration is performed before scanning", "التعداد يُنفَّذ قبل الفحص"),
  ("Both retrieve the same level of detail", "كلاهما يسترجع المستوى نفسه من التفاصيل")], 0,
 "Slide 55: scanning is less interactive and usually the first step; enumeration is more interactive and is performed after scanning.",
 "الشريحة ٥٥: الفحص أقل تفاعلية وهو عادةً الخطوة الأولى، والتعداد أكثر تفاعلية ويُنفَّذ بعد الفحص.")

mcq(3, "Slide 57",
 "Banner grabbing is classified as which kind of technique?",
 "التقاط اللافتات يُصنَّف كأي نوع من التقنيات؟",
 [("An active enumeration technique", "تقنية تعداد نشطة"),
  ("A passive footprinting technique", "تقنية بصمة سلبية"),
  ("An evasion technique", "تقنية تهرب"),
  ("A sniffing technique", "تقنية تنصت")], 0,
 "Slide 57: “Banner-grabbing is an <b>active enumeration technique</b>.”",
 "الشريحة ٥٧: «التقاط اللافتات <b>تقنية تعداد نشطة</b>».")

mcq(3, "Slide 58",
 "From the banner <code>HTTP/1.1 200 OK / Server: Microsoft-IIS/10.0</code>, what do we learn?",
 "من اللافتة <code>HTTP/1.1 200 OK / Server: Microsoft-IIS/10.0</code>، ماذا نعرف؟",
 [("Web server: Microsoft IIS, Version: 10.0", "خادم الويب: Microsoft IIS والإصدار: 10.0"),
  ("The OS is Ubuntu", "نظام التشغيل هو أوبونتو"),
  ("The port is closed", "المنفذ مغلق"),
  ("The MAC address of the server", "عنوان MAC للخادم")], 0,
 "Slide 58 gives exactly this interpretation.", "الشريحة ٥٨ تعطي هذا التفسير بالضبط.")

mcq(3, "Slide 60",
 "Which tool connects to a TCP port and displays service responses for banner grabbing?",
 "أي أداة تتصل بمنفذ TCP وتعرض ردود الخدمة لالتقاط اللافتات؟",
 [("Telnet", "Telnet"), ("Maltego", "Maltego"),
  ("HTTrack", "HTTrack"), ("Nessus", "Nessus")], 0,
 "Slide 60: Telnet, Netcat (nc) and Nmap are the three banner grabbing tools listed.",
 "الشريحة ٦٠: Telnet و Netcat و Nmap هي أدوات التقاط اللافتات الثلاث المذكورة.")

mcq(3, "Slide 62",
 "Which ports does NetBIOS use?",
 "أي منافذ يستخدمها NetBIOS؟",
 [("TCP/UDP 137, UDP 138, TCP 139", "TCP/UDP ١٣٧، UDP ١٣٨، TCP ١٣٩"),
  ("TCP 135, 445, 3389", "TCP ١٣٥ و٤٤٥ و٣٣٨٩"),
  ("UDP 161 and 162", "UDP ١٦١ و١٦٢"),
  ("TCP 20, 21, 22", "TCP ٢٠ و٢١ و٢٢")], 0,
 "Slide 62: NetBIOS uses TCP/UDP port <b>137</b>, UDP port <b>138</b>, TCP port <b>139</b>.",
 "الشريحة ٦٢: يستخدم NetBIOS المنفذ <b>١٣٧</b> على TCP/UDP، و<b>١٣٨</b> على UDP، و<b>١٣٩</b> على TCP.")

mcq(3, "Slide 62",
 "Why is NetBIOS considered FIRST for enumeration?",
 "لماذا يُعتبر NetBIOS الأول في التعداد؟",
 [("It extracts NetBIOS name, username, workgroup/domain name and MAC address, and is easy to exploit",
   "لأنه يستخرج اسم NetBIOS واسم المستخدم واسم مجموعة العمل/النطاق وعنوان MAC، وهو سهل الاستغلال"),
  ("It encrypts all data", "لأنه يشفّر كل البيانات"),
  ("It works only on Linux", "لأنه يعمل على لينكس فقط"),
  ("It is the newest protocol", "لأنه أحدث بروتوكول")], 0,
 "Slide 62: attackers target it because it is easy to exploit and runs on Windows systems even when not in use.",
 "الشريحة ٦٢: يستهدفه المهاجمون لأنه سهل الاستغلال ويعمل على ويندوز حتى عند عدم استخدامه.")

mcq(3, "Slide 65",
 "What is the DEFAULT SNMP read community string?",
 "ما سلسلة مجتمع SNMP الافتراضية للقراءة؟",
 [("public", "public"), ("private", "private"),
  ("admin", "admin"), ("snmp", "snmp")], 0,
 "Slide 65: the read community string is <b>‘public’</b> by default (view configuration); the read/write string is <b>‘private’</b> (remote editing).",
 "الشريحة ٦٥: سلسلة القراءة الافتراضية <b>‘public’</b> (لعرض الإعدادات)، وسلسلة القراءة/الكتابة <b>‘private’</b> (للتعديل عن بُعد).")

mcq(3, "Slide 65",
 "Which SNMP community string allows REMOTE EDITING of the configuration and is ‘private’ by default?",
 "أي سلسلة مجتمع SNMP تسمح بتعديل الإعدادات عن بُعد وقيمتها الافتراضية ‘private’؟",
 [("Read/write community string", "سلسلة القراءة والكتابة"),
  ("Read community string", "سلسلة القراءة"),
  ("Public community string", "سلسلة public"),
  ("Trap community string", "سلسلة trap")], 0,
 "Slide 65: the read/write community string (default ‘private’) allows remote editing of the configuration.",
 "الشريحة ٦٥: سلسلة القراءة/الكتابة (الافتراضية ‘private’) تسمح بتعديل الإعدادات عن بُعد.")

mcq(3, "Slide 64",
 "In SNMP, who installs the AGENT and where?",
 "في SNMP، من يثبّت الوكيل (Agent) وأين؟",
 [("Vendors install it in most network components (routers, switches, servers, firewalls, wireless APs)",
   "المصنّعون يثبّتونه في معظم مكونات الشبكة (الموجّهات والمحوّلات والخوادم والجدران النارية ونقاط الوصول)"),
  ("The network administrator installs it on a separate computer", "مسؤول الشبكة يثبّته على حاسوب منفصل"),
  ("The attacker installs it on the target", "المهاجم يثبّته على الهدف"),
  ("It is built into the OS kernel only", "إنه مدمج في نواة نظام التشغيل فقط")], 0,
 "Slide 64: the <b>agent</b> is installed by vendors in network components; the <b>manager</b> is installed by the administrator on a separate computer.",
 "الشريحة ٦٤: <b>الوكيل</b> يثبّته المصنّعون في مكونات الشبكة، و<b>المدير</b> يثبّته المسؤول على حاسوب منفصل.")

mcq(3, "Slide 66",
 "Snmp-check is a tool that:",
 "أداة Snmp-check هي أداة:",
 [("Enumerates SNMP devices and presents output in a user-friendly format", "تعدّد أجهزة SNMP وتعرض المخرجات بصيغة سهلة القراءة"),
  ("Mirrors websites", "تنسخ المواقع"),
  ("Cracks passwords", "تكسر كلمات المرور"),
  ("Captures packets", "تلتقط الحزم")], 0,
 "Slide 66: snmp-check (nothink.org) enumerates SNMP devices in a user-friendly format.",
 "الشريحة ٦٦: snmp-check تعدّد أجهزة SNMP وتعرض النتائج بصيغة سهلة.")

tf(3, "Slide 28",
 "The SYN scan is faster than the TCP Connect scan and more difficult to detect.",
 "فحص SYN أسرع من فحص TCP Connect وأصعب في الاكتشاف.",
 True,
 "Slide 28 — it is one of the most commonly used Nmap scan types.",
 "الشريحة ٢٨ — وهو من أكثر أنواع فحص Nmap استخداماً.")

tf(3, "Slide 8",
 "The four TCP flags SYN, ACK, FIN and RST govern the establishment, maintenance and termination of a connection.",
 "أعلام TCP الأربعة SYN و ACK و FIN و RST تحكم إنشاء الاتصال وصيانته وإنهاءه.",
 True, "Slide 8 states this literally.", "الشريحة ٨ تنص على ذلك حرفياً.")

sa(3, "Slide 26",
 "State the four objectives of port scanning.",
 "اذكر أهداف فحص المنافذ الأربعة.",
 "<b>Discover running services · Identify open ports · Detect operating systems and applications · Find potential attack entry points</b> (slide 26).",
 "<b>اكتشاف الخدمات العاملة · تحديد المنافذ المفتوحة · كشف أنظمة التشغيل والتطبيقات · إيجاد نقاط دخول محتملة للهجوم</b> (الشريحة ٢٦).")

sa(3, "Slide 54",
 "List the five categories of information that can be enumerated.",
 "اذكر الفئات الخمس للمعلومات التي يمكن تعدادها.",
 "<b>User accounts · Shared folders · Network resources · Running services · Group and permission</b> (slide 54).",
 "<b>حسابات المستخدمين · المجلدات المشتركة · موارد الشبكة · الخدمات العاملة · المجموعات والصلاحيات</b> (الشريحة ٥٤).")

sa(3, "Slide 57",
 "What five things may a banner reveal?",
 "ما الأشياء الخمسة التي قد تكشفها اللافتة (Banner)؟",
 "<b>Service name · Software version · Operating system information · Web server type · Mail server information</b> (slide 57).",
 "<b>اسم الخدمة · إصدار البرنامج · معلومات نظام التشغيل · نوع خادم الويب · معلومات خادم البريد</b> (الشريحة ٥٧).")

sa(3, "Slide 67",
 "Complete the closing sequence of Chapter 3: Discover → ______ → ______ → Access → Protect.",
 "أكمل تسلسل خاتمة الفصل الثالث: اكتشف ← ______ ← ______ ← اوصل ← احمِ.",
 "Discover → <b>Identify</b> → <b>Enumerate</b> → Access → Protect (slide 67).",
 "اكتشف ← <b>حدّد</b> ← <b>عدّد</b> ← اوصل ← احمِ (الشريحة ٦٧).")

# ══════════════════════════════ CHAPTER 4 ══════════════════════════════
mcq(4, "Slide 2",
 "Sniffing is the process of:",
 "التنصت (Sniffing) هو عملية:",
 [("Capturing and analyzing network traffic to understand how devices communicate and detect security issues",
   "التقاط وتحليل حركة الشبكة لفهم كيفية تواصل الأجهزة واكتشاف المشكلات الأمنية"),
  ("Scanning for open ports", "فحص المنافذ المفتوحة"),
  ("Gathering public information from search engines", "جمع المعلومات العامة من محركات البحث"),
  ("Deleting log files", "حذف ملفات السجل")], 0,
 "Slide 2 gives this definition.", "الشريحة ٢ تعطي هذا التعريف.")

mcq(4, "Slide 4",
 "Which of the following is a function of the NIC?",
 "أي مما يلي من وظائف بطاقة واجهة الشبكة (NIC)؟",
 [("Examines the destination MAC address of each incoming frame", "فحص عنوان MAC الوجهة لكل إطار وارد"),
  ("Assigns IP addresses to clients", "تخصيص عناوين IP للعملاء"),
  ("Resolves domain names", "تحليل أسماء النطاقات"),
  ("Encrypts all traffic", "تشفير كل حركة المرور")], 0,
 "Slide 4: connects the host, receives/transmits frames, examines the destination MAC address, passes valid frames to the OS.",
 "الشريحة ٤: توصيل الجهاز، استقبال وإرسال الإطارات، فحص عنوان MAC الوجهة، تمرير الإطارات الصالحة لنظام التشغيل.")

mcq(4, "Slide 5",
 "What is the length of a MAC address?",
 "ما طول عنوان MAC؟",
 [("48 bits (6 bytes)", "٤٨ بت (٦ بايت)"), ("32 bits (4 bytes)", "٣٢ بت (٤ بايت)"),
  ("64 bits (8 bytes)", "٦٤ بت (٨ بايت)"), ("128 bits (16 bytes)", "١٢٨ بت (١٦ بايت)")], 0,
 "Slide 5: 48 bits (6 bytes), represented as 12 hexadecimal digits — e.g. 00:1A:2B:3C:4D:5E.",
 "الشريحة ٥: ٤٨ بت (٦ بايت)، تُمثَّل بـ ١٢ رقماً ست عشرياً — مثل 00:1A:2B:3C:4D:5E.")

mcq(4, "Slide 5",
 "A MAC address is used for communication at which OSI layer?",
 "يُستخدم عنوان MAC للاتصال في أي طبقة من نموذج OSI؟",
 [("Data Link Layer (Layer 2)", "طبقة ربط البيانات (الطبقة الثانية)"),
  ("Network Layer (Layer 3)", "طبقة الشبكة (الثالثة)"),
  ("Transport Layer (Layer 4)", "طبقة النقل (الرابعة)"),
  ("Physical Layer (Layer 1)", "الطبقة المادية (الأولى)")], 0,
 "Slide 5: the Data Link Layer, Layer 2.", "الشريحة ٥: طبقة ربط البيانات، الطبقة الثانية.")

mcq(4, "Slide 5",
 "How many hexadecimal digits represent a MAC address?",
 "بكم رقماً ست عشرياً يُمثَّل عنوان MAC؟",
 [("12", "١٢"), ("6", "٦"), ("8", "٨"), ("16", "١٦")], 0,
 "Slide 5: 12 hexadecimal digits.", "الشريحة ٥: ١٢ رقماً ست عشرياً.")

mcq(4, "Slide 6",
 "A collision domain is:",
 "نطاق التصادم هو:",
 [("The logical and physical segment of the network where data packets can collide with one another",
   "الجزء المنطقي والمادي من الشبكة الذي يمكن أن تتصادم فيه حزم البيانات"),
  ("The range of IP addresses in a subnet", "نطاق عناوين IP في الشبكة الفرعية"),
  ("The area covered by a wireless AP", "المنطقة التي تغطيها نقطة الوصول اللاسلكية"),
  ("A table stored in a switch", "جدول مخزّن في المحوّل")], 0,
 "Slide 6: hosts sharing a common coaxial cable or repeater hub share a singular electrical bus.",
 "الشريحة ٦: الأجهزة التي تتشارك كابلاً محورياً أو Hub تتشارك ناقلاً كهربائياً واحداً.")

mcq(4, "Slide 6",
 "What happens when two nodes initiate simultaneous transmission on a shared electrical bus?",
 "ماذا يحدث عندما تبدأ عقدتان الإرسال في الوقت نفسه على ناقل كهربائي مشترك؟",
 [("A collision occurs and both frames become unintelligible", "يحدث تصادم ويصبح كلا الإطارين غير مفهومين"),
  ("The switch buffers both frames", "يخزّن المحوّل كلا الإطارين مؤقتاً"),
  ("The first frame wins and the second is queued", "يفوز الإطار الأول ويُصف الثاني في الطابور"),
  ("Nothing — modern hubs prevent this", "لا شيء — المُوزِّعات الحديثة تمنع ذلك")], 0,
 "Slide 6: the superposition of electrical signals — a collision — renders both frames unintelligible.",
 "الشريحة ٦: تراكب الإشارات الكهربائية — التصادم — يجعل كلا الإطارين غير مفهومين.")

mcq(4, "Slide 9",
 "Which protocol exposes “Usernames, passwords, transferred files” when sniffed?",
 "أي بروتوكول يكشف «أسماء المستخدمين وكلمات المرور والملفات المنقولة» عند التنصت عليه؟",
 [("FTP", "FTP"), ("SMTP", "SMTP"), ("HTTP", "HTTP"), ("POP3", "POP3")], 0,
 "Slide 9: FTP → usernames, passwords, transferred files.",
 "الشريحة ٩: FTP ← أسماء المستخدمين وكلمات المرور والملفات المنقولة.")

mcq(4, "Slide 9",
 "According to the table, HTTP exposes:",
 "حسب الجدول، يكشف HTTP عن:",
 [("Web pages, form data, cookies", "صفحات الويب وبيانات النماذج وملفات تعريف الارتباط"),
  ("Email messages", "رسائل البريد الإلكتروني"),
  ("Usernames, passwords, commands", "أسماء المستخدمين وكلمات المرور والأوامر"),
  ("Files transferred without encryption", "ملفات منقولة دون تشفير")], 0,
 "Slide 9: HTTP → web pages, form data, cookies.",
 "الشريحة ٩: HTTP ← صفحات الويب وبيانات النماذج وملفات تعريف الارتباط.")

mcq(4, "Slide 9",
 "Which protocol exposes “Usernames, passwords, commands”?",
 "أي بروتوكول يكشف «أسماء المستخدمين وكلمات المرور والأوامر»؟",
 [("Telnet", "Telnet"), ("TFTP", "TFTP"), ("SMTP", "SMTP"), ("HTTP", "HTTP")], 0,
 "Slide 9: Telnet → usernames, passwords, commands.",
 "الشريحة ٩: Telnet ← أسماء المستخدمين وكلمات المرور والأوامر.")

mcq(4, "Slide 9",
 "Which are the modern SECURE alternatives mentioned that encrypt transmitted data?",
 "ما البدائل الآمنة الحديثة المذكورة التي تشفّر البيانات المنقولة؟",
 [("HTTPS, SFTP, SSH", "HTTPS و SFTP و SSH"), ("HTTP, FTP, Telnet", "HTTP و FTP و Telnet"),
  ("SMTP, POP3, IMAP", "SMTP و POP3 و IMAP"), ("ARP, ICMP, DHCP", "ARP و ICMP و DHCP")], 0,
 "Slide 9 note: HTTPS, SFTP and SSH encrypt transmitted data and significantly reduce the risk of sniffing.",
 "ملاحظة الشريحة ٩: HTTPS و SFTP و SSH تشفّر البيانات وتقلل خطر التنصت بشكل كبير.")

mcq(4, "Slide 12",
 "ARP is a Data Link Layer protocol used to map:",
 "ARP بروتوكول في طبقة ربط البيانات يُستخدم لربط:",
 [("An IPv4 address to its corresponding MAC address within a local network", "عنوان IPv4 بعنوان MAC المقابل له داخل الشبكة المحلية"),
  ("A MAC address to a port number", "عنوان MAC برقم منفذ"),
  ("A domain name to an IP address", "اسم نطاق بعنوان IP"),
  ("An IP address to a hostname", "عنوان IP باسم مضيف")], 0,
 "Slide 12 gives exactly this definition.", "الشريحة ١٢ تعطي هذا التعريف بالضبط.")

mcq(4, "Slide 13",
 "An ARP Request is:",
 "طلب ARP هو:",
 [("A broadcast message sent to all devices, asking “Who has this IP address?”",
   "رسالة بث تُرسَل إلى جميع الأجهزة وتسأل «من يملك عنوان IP هذا؟»"),
  ("A unicast response containing a MAC address", "رد أحادي البث يحتوي على عنوان MAC"),
  ("A multicast DNS query", "استعلام DNS متعدد البث"),
  ("An ICMP echo request", "طلب صدى ICMP")], 0,
 "Slide 13: ARP Request = broadcast (“Who has this IP address?”); ARP Reply = unicast returning the MAC address.",
 "الشريحة ١٣: طلب ARP = بث («من يملك هذا العنوان؟»)، ورد ARP = أحادي البث ويعيد عنوان MAC.")

mcq(4, "Slide 13",
 "An ARP Reply is:",
 "رد ARP هو:",
 [("A unicast response sent by the device that owns the requested IP address", "رد أحادي البث يرسله الجهاز الذي يملك عنوان IP المطلوب"),
  ("A broadcast to all hosts", "بث إلى جميع الأجهزة"),
  ("An ICMP type 0 message", "رسالة ICMP نوع ٠"),
  ("A DHCP offer", "عرض DHCP")], 0,
 "Slide 13.", "الشريحة ١٣.")

mcq(4, "Slide 15 / 16",
 "Passive sniffing is commonly performed in which type of network?",
 "التنصت السلبي يُنفَّذ عادةً في أي نوع من الشبكات؟",
 [("Hub-based networks", "الشبكات القائمة على المُوزِّعات (Hubs)"),
  ("Switched networks", "الشبكات المُبدَّلة (Switches)"),
  ("Wireless mesh networks", "الشبكات اللاسلكية الشبكية"),
  ("Cloud networks", "الشبكات السحابية")], 0,
 "Slides 15 &amp; 16: passive sniffing is most effective in hub-based Ethernet networks where all connected devices receive the same traffic.",
 "الشريحتان ١٥ و١٦: التنصت السلبي أكثر فعالية في شبكات الإيثرنت القائمة على Hubs حيث تستقبل جميع الأجهزة نفس الحركة.")

mcq(4, "Slide 16",
 "Passive sniffing requires the attacker to be:",
 "يتطلب التنصت السلبي أن يكون المهاجم:",
 [("Within the same collision domain as the target", "داخل نطاق التصادم نفسه مع الهدف"),
  ("Connected to the target's router remotely", "متصلاً بموجّه الهدف عن بُعد"),
  ("An administrator on the switch", "مسؤولاً على المحوّل"),
  ("Using a proxy chain", "مستخدماً سلسلة بروكسي")], 0,
 "Slide 16.", "الشريحة ١٦.")

mcq(4, "Slide 16",
 "Which is a LIMITATION of passive sniffing?",
 "أي مما يلي يُعد قيداً على التنصت السلبي؟",
 [("Ineffective in modern switched Ethernet networks", "غير فعّال في شبكات الإيثرنت المُبدَّلة الحديثة"),
  ("It is easy to detect", "أنه سهل الاكتشاف"),
  ("It generates a lot of network traffic", "أنه يولّد حركة مرور كثيرة"),
  ("It requires administrative access", "أنه يتطلب صلاحيات إدارية")], 0,
 "Slide 16: it is difficult to detect and adds no traffic, but is ineffective in switched networks and limited to the local collision domain.",
 "الشريحة ١٦: يصعب اكتشافه ولا يضيف حركة، لكنه غير فعّال في الشبكات المُبدَّلة ومحدود بنطاق التصادم المحلي.")

mcq(4, "Slide 17",
 "Active sniffing is used when:",
 "يُستخدم التنصت النشط عندما:",
 [("Passive sniffing is not possible", "يكون التنصت السلبي غير ممكن"),
  ("The network uses hubs", "تستخدم الشبكة مُوزِّعات (Hubs)"),
  ("The attacker has no tools", "لا يملك المهاجم أدوات"),
  ("Traffic is already encrypted", "تكون الحركة مشفرة أصلاً")], 0,
 "Slide 17: it requires interaction with network devices or packet manipulation and is used in switch-based Ethernet networks.",
 "الشريحة ١٧: يتطلب التفاعل مع أجهزة الشبكة أو التلاعب بالحزم ويُستخدم في شبكات الإيثرنت المُبدَّلة.")

mcq(4, "Slide 21",
 "Why is passive sniffing usually ineffective in modern switched networks?",
 "لماذا يكون التنصت السلبي عادةً غير فعّال في الشبكات المُبدَّلة الحديثة؟",
 [("Switches forward frames only to the intended destination", "لأن المحوّلات تمرّر الإطارات إلى الوجهة المقصودة فقط"),
  ("Switches encrypt all frames", "لأن المحوّلات تشفّر جميع الإطارات"),
  ("Switches block all ICMP", "لأن المحوّلات تحجب ICMP"),
  ("Switches have no CAM table", "لأن المحوّلات ليس لديها جدول CAM")], 0,
 "Slide 21 states this literally.", "الشريحة ٢١ تنص على ذلك حرفياً.")

mcq(4, "Slide 21",
 "Which of the following is listed as an active sniffing technique on slide 21?",
 "أي مما يلي مذكور كتقنية تنصت نشط في الشريحة ٢١؟",
 [("DHCP Starvation", "تجويع DHCP"), ("Google Dorking", "Google Dorking"),
  ("Web mirroring", "نسخ المواقع"), ("Banner grabbing", "التقاط اللافتات")], 0,
 "Slide 21 lists MAC Flooding, ARP Spoofing (ARP Poisoning), Port Mirroring (SPAN Port) and DHCP Starvation.",
 "الشريحة ٢١ تذكر: إغراق MAC، تسميم ARP، نسخ المنافذ (SPAN)، وتجويع DHCP.")

mcq(4, "Slide 20",
 "Which sniffing tool's primary purpose is “Network monitoring and man-in-the-middle attacks”?",
 "أي أداة تنصت غرضها الأساسي «مراقبة الشبكة وهجمات الوسيط»؟",
 [("Ettercap", "Ettercap"), ("Wireshark", "Wireshark"),
  ("EtherPeek", "EtherPeek"), ("Snort", "Snort")], 0,
 "Slide 20: Ettercap. (Wireshark = packet capture and protocol analysis; EtherPeek = network traffic analysis; Snort = IDS with packet capture.)",
 "الشريحة ٢٠: Ettercap. (Wireshark = التقاط الحزم وتحليل البروتوكولات، EtherPeek = تحليل الحركة، Snort = نظام كشف تسلل.)")

mcq(4, "Slide 20",
 "Which tool is described as an Intrusion Detection System (IDS) with packet capture capabilities?",
 "أي أداة توصف بأنها نظام كشف تسلل (IDS) مع قدرات التقاط الحزم؟",
 [("Snort", "Snort"), ("Ettercap", "Ettercap"),
  ("Wireshark", "Wireshark"), ("Nessus", "Nessus")], 0,
 "Slide 20: <b>Snort</b>.", "الشريحة ٢٠: <b>Snort</b>.")

mcq(4, "Slide 22",
 "MAC Flooding works by:",
 "يعمل إغراق MAC عن طريق:",
 [("Transmitting thousands of frames with fake MAC addresses until the CAM table becomes full",
   "إرسال آلاف الإطارات بعناوين MAC مزيّفة حتى يمتلئ جدول CAM"),
  ("Sending forged ARP replies", "إرسال ردود ARP مزوّرة"),
  ("Exhausting the DHCP address pool", "استنفاد مجمّع عناوين DHCP"),
  ("Copying traffic to a monitoring port", "نسخ الحركة إلى منفذ مراقبة")], 0,
 "Slide 22: once the CAM table is full the switch can no longer learn new MAC addresses and unknown frames are flooded to all ports.",
 "الشريحة ٢٢: عند امتلاء جدول CAM لا يستطيع المحوّل تعلّم عناوين جديدة فتُبَث الإطارات المجهولة إلى كل المنافذ.")

mcq(4, "Slide 23",
 "A CAM table is a database maintained by an Ethernet switch to associate:",
 "جدول CAM قاعدة بيانات يحتفظ بها محوّل الإيثرنت لربط:",
 [("MAC addresses with switch ports", "عناوين MAC بمنافذ المحوّل"),
  ("IP addresses with domain names", "عناوين IP بأسماء النطاقات"),
  ("Port numbers with applications", "أرقام المنافذ بالتطبيقات"),
  ("Users with passwords", "المستخدمين بكلمات المرور")], 0,
 "Slide 23: this enables the switch to forward frames only to the intended destination.",
 "الشريحة ٢٣: هذا يمكّن المحوّل من تمرير الإطارات إلى الوجهة المقصودة فقط.")

mcq(4, "Slide 23",
 "When the CAM table is full, the switch behaves similarly to:",
 "عندما يمتلئ جدول CAM، يتصرف المحوّل بشكل مشابه لـ:",
 [("A hub", "المُوزِّع (Hub)"), ("A router", "الموجّه"),
  ("A firewall", "الجدار الناري"), ("A proxy server", "الخادم الوسيط")], 0,
 "Slide 23: “The switch floods these frames to all ports, behaving similarly to a <b>hub</b>”, so an attacker can capture traffic intended for other devices.",
 "الشريحة ٢٣: «يبث المحوّل هذه الإطارات إلى جميع المنافذ متصرّفاً كالـ<b>Hub</b>»، فيستطيع المهاجم التقاط حركة موجّهة لأجهزة أخرى.")

mcq(4, "Slide 24",
 "ARP Spoofing is a technique in which the attacker sends forged ARP messages to associate:",
 "انتحال ARP تقنية يرسل فيها المهاجم رسائل ARP مزوّرة لربط:",
 [("Their MAC address with the IP address of another device, such as the default gateway",
   "عنوان MAC الخاص به بعنوان IP لجهاز آخر مثل البوابة الافتراضية"),
  ("Their IP address with a fake domain name", "عنوان IP الخاص به باسم نطاق مزيف"),
  ("A switch port with a VLAN", "منفذ محوّل بشبكة VLAN"),
  ("A DHCP lease with a fake client", "عقد DHCP بعميل وهمي")], 0,
 "Slide 24 gives exactly this definition.", "الشريحة ٢٤ تعطي هذا التعريف بالضبط.")

mcq(4, "Slide 24",
 "What is the SECOND step of the ARP spoofing process?",
 "ما الخطوة الثانية في عملية انتحال ARP؟",
 [("Victims update their ARP cache with the forged MAC address", "يحدّث الضحايا ذاكرة ARP لديهم بعنوان MAC المزوّر"),
  ("The attacker broadcasts fake ARP Reply messages", "يبث المهاجم رسائل رد ARP مزيّفة"),
  ("Network traffic is redirected through the attacker's device", "تُعاد توجيه الحركة عبر جهاز المهاجم"),
  ("The attacker intercepts, modifies or forwards the traffic", "يعترض المهاجم الحركة أو يعدّلها أو يمرّرها")], 0,
 "Slide 24 order: (1) broadcast fake ARP Replies → (2) victims update their ARP cache → (3) traffic redirected → (4) intercept/modify/forward.",
 "ترتيب الشريحة ٢٤: (١) بث ردود ARP مزيّفة ← (٢) تحديث ذاكرة ARP لدى الضحايا ← (٣) إعادة توجيه الحركة ← (٤) الاعتراض/التعديل/التمرير.")

mcq(4, "Slide 25",
 "Which of the following is an impact of ARP spoofing?",
 "أي مما يلي من آثار انتحال ARP؟",
 [("It enables Man-in-the-Middle (MitM) attacks and may lead to data theft or session hijacking",
   "يمكّن من هجمات الوسيط وقد يؤدي إلى سرقة البيانات أو اختطاف الجلسات"),
  ("It exhausts the DHCP address pool", "يستنفد مجمّع عناوين DHCP"),
  ("It fills the CAM table", "يملأ جدول CAM"),
  ("It encrypts the victim's traffic", "يشفّر حركة الضحية")], 0,
 "Slide 25: enables MitM, allows packet sniffing in switched networks, may lead to data theft or session hijacking.",
 "الشريحة ٢٥: يمكّن من هجمات الوسيط، ويسمح بالتنصت في الشبكات المُبدَّلة، وقد يؤدي إلى سرقة البيانات أو اختطاف الجلسات.")

mcq(4, "Slide 26",
 "Port Mirroring is also known as:",
 "نسخ المنافذ يُعرف أيضاً باسم:",
 [("Switched Port Analyzer (SPAN)", "محلّل المنفذ المُبدَّل (SPAN)"),
  ("CAM Table Analyzer", "محلل جدول CAM"),
  ("Promiscuous Port", "المنفذ المختلط"),
  ("Trunk Port", "منفذ الجذع (Trunk)")], 0,
 "Slide 26: Port Mirroring = SPAN — a switch feature that copies traffic from one or more ports to a designated monitoring port.",
 "الشريحة ٢٦: نسخ المنافذ = SPAN — ميزة في المحوّل تنسخ الحركة من منفذ أو أكثر إلى منفذ مراقبة مخصص.")

mcq(4, "Slide 27",
 "A DHCP Starvation Attack is which kind of attack?",
 "هجوم تجويع DHCP هو أي نوع من الهجمات؟",
 [("A Denial-of-Service (DoS) attack", "هجوم حجب خدمة (DoS)"),
  ("A Man-in-the-Middle attack", "هجوم وسيط (MitM)"),
  ("A privilege escalation attack", "هجوم تصعيد صلاحيات"),
  ("A passive sniffing technique", "تقنية تنصت سلبي")], 0,
 "Slide 27: it is a DoS attack in which the attacker exhausts all available IP addresses in the DHCP server's address pool.",
 "الشريحة ٢٧: هجوم حجب خدمة يستنفد فيه المهاجم كل عناوين IP المتاحة في مجمّع خادم DHCP.")

mcq(4, "Slide 27",
 "What is the RESULT of a successful DHCP starvation attack?",
 "ما نتيجة نجاح هجوم تجويع DHCP؟",
 [("Legitimate users cannot obtain or renew IP addresses", "لا يستطيع المستخدمون الشرعيون الحصول على عناوين IP أو تجديدها"),
  ("The switch behaves like a hub", "يتصرف المحوّل كالـ Hub"),
  ("All traffic is routed through the attacker", "تمر كل الحركة عبر المهاجم"),
  ("The ARP cache is poisoned", "تُسمَّم ذاكرة ARP")], 0,
 "Slide 27: the address pool becomes exhausted, so legitimate users cannot obtain or renew IP addresses.",
 "الشريحة ٢٧: يُستنفَد مجمّع العناوين فلا يستطيع المستخدمون الشرعيون الحصول على العناوين أو تجديدها.")

mcq(4, "Slide 29",
 "Wireshark is best described as:",
 "أفضل وصف لأداة Wireshark هو:",
 [("An open-source network protocol analyzer used to capture, inspect and analyze traffic in real time",
   "محلل بروتوكولات شبكية مفتوح المصدر يلتقط ويفحص ويحلل الحركة في الوقت الفعلي"),
  ("A commercial vulnerability scanner", "فاحص ثغرات تجاري"),
  ("A web mirroring tool", "أداة نسخ مواقع"),
  ("An OSINT username checker", "أداة OSINT لفحص أسماء المستخدمين")], 0,
 "Slide 29: it is one of the most widely used packet sniffing tools for network administration, troubleshooting and security analysis.",
 "الشريحة ٢٩: هي من أكثر أدوات تنصت الحزم استخداماً في إدارة الشبكات واستكشاف الأعطال والتحليل الأمني.")

mcq(4, "Slide 30",
 "Which Wireshark filter displays Telnet traffic?",
 "أي مرشح في Wireshark يعرض حركة Telnet؟",
 [("tcp.port == 23", "tcp.port == 23"), ("tcp.port == 21", "tcp.port == 21"),
  ("http.request", "http.request"), ("dns", "dns")], 0,
 "Slide 30: <code>tcp.port == 23</code> → Telnet traffic (Telnet uses port 23).",
 "الشريحة ٣٠: <code>tcp.port == 23</code> ← حركة Telnet (المنفذ ٢٣).")

mcq(4, "Slide 30",
 "Which Wireshark filter displays packets associated with a specific IP?",
 "أي مرشح في Wireshark يعرض الحزم المرتبطة بعنوان IP محدد؟",
 [("ip.addr == 192.168.1.10", "ip.addr == 192.168.1.10"),
  ("tcp contains \"password\"", "tcp contains \"password\""),
  ("http.request", "http.request"), ("icmp", "icmp")], 0,
 "Slide 30.", "الشريحة ٣٠.")

mcq(4, "Slide 30",
 "Which Wireshark filter displays TCP packets containing a specific string?",
 "أي مرشح في Wireshark يعرض حزم TCP التي تحتوي نصاً معيّناً؟",
 [("tcp contains \"password\"", "tcp contains \"password\""),
  ("tcp.port == 23", "tcp.port == 23"),
  ("ip.addr == 192.168.1.10", "ip.addr == 192.168.1.10"),
  ("arp", "arp")], 0,
 "Slide 30.", "الشريحة ٣٠.")

mcq(4, "Slide 32",
 "Which tcpdump command SAVES captured packets to a file?",
 "أي أمر في tcpdump يحفظ الحزم الملتقطة في ملف؟",
 [("tcpdump -w capture.pcap", "tcpdump -w capture.pcap"),
  ("tcpdump -r capture.pcap", "tcpdump -r capture.pcap"),
  ("tcpdump -i eth0", "tcpdump -i eth0"),
  ("tcpdump -s 0", "tcpdump -s 0")], 0,
 "Slide 32: <code>-w</code> writes to a file, <code>-r</code> reads from a capture file, <code>-i</code> selects the interface.",
 "الشريحة ٣٢: <code>-w</code> للكتابة في ملف، و<code>-r</code> للقراءة من ملف، و<code>-i</code> لاختيار الواجهة.")

mcq(4, "Slide 32",
 "Which tcpdump command captures packets on interface eth0?",
 "أي أمر في tcpdump يلتقط الحزم على الواجهة eth0؟",
 [("tcpdump -i eth0", "tcpdump -i eth0"), ("tcpdump -w eth0", "tcpdump -w eth0"),
  ("tcpdump -r eth0", "tcpdump -r eth0"), ("tcpdump eth0 -all", "tcpdump eth0 -all")], 0,
 "Slide 32.", "الشريحة ٣٢.")

mcq(4, "Slide 32 / 33",
 "Tcpdump is a packet analyzer that is:",
 "Tcpdump محلل حزم يكون:",
 [("Command-line based, commonly used on Linux and Unix systems", "يعمل من سطر الأوامر ويُستخدم عادةً على أنظمة لينكس ويونكس"),
  ("Graphical, Windows-only", "رسومياً ولويندوز فقط"),
  ("A cloud service", "خدمة سحابية"),
  ("An intrusion prevention system", "نظام منع تسلل")], 0,
 "Slides 32–33: it captures packets from a specified interface, supports Boolean filtering, displays info in real time and saves packets for later analysis.",
 "الشريحتان ٣٢–٣٣: يلتقط الحزم من واجهة محددة، ويدعم التصفية المنطقية، ويعرض المعلومات فورياً، ويحفظ الحزم للتحليل لاحقاً.")

tf(4, "Slide 15",
 "Passive sniffing does not generate additional network traffic.",
 "التنصت السلبي لا يولّد حركة مرور إضافية على الشبكة.",
 True, "Slide 15 states this literally.", "الشريحة ١٥ تنص على ذلك حرفياً.")

tf(4, "Slide 17",
 "Active sniffing often requires administrative access or successful attack techniques.",
 "التنصت النشط غالباً يتطلب صلاحيات إدارية أو تقنيات هجوم ناجحة.",
 True, "Slide 17 — one of its limitations, along with higher complexity and detectable activity.",
 "الشريحة ١٧ — من قيوده، إلى جانب التعقيد الأعلى والنشاط القابل للاكتشاف.")

tf(4, "Slide 8",
 "Network protocols that transmit data in clear text are highly vulnerable to packet sniffing.",
 "بروتوكولات الشبكة التي تنقل البيانات كنص واضح عرضة بشدة لتنصت الحزم.",
 True, "Slide 8 states this literally.", "الشريحة ٨ تنص على ذلك حرفياً.")

sa(4, "Slide 18",
 "Name the three common techniques for active sniffing listed on slide 18.",
 "اذكر التقنيات الشائعة الثلاث للتنصت النشط المذكورة في الشريحة ١٨.",
 "<b>Port Mirroring (SPAN Port) · ARP Spoofing (ARP Poisoning) · MAC Flooding</b> (slide 18).",
 "<b>نسخ المنافذ (SPAN) · انتحال/تسميم ARP · إغراق MAC</b> (الشريحة ١٨).")

sa(4, "Slide 10",
 "What four kinds of information does the TCP transport layer provide for analysis?",
 "ما الأنواع الأربعة من المعلومات التي توفرها طبقة النقل TCP للتحليل؟",
 "<b>Source and destination port numbers · Sequence and acknowledgment numbers · Connection establishment and termination · Session tracking and analysis</b> (slide 10).",
 "<b>أرقام منافذ المصدر والوجهة · أرقام التسلسل والإقرار · إنشاء الاتصال وإنهاؤه · تتبع الجلسات وتحليلها</b> (الشريحة ١٠).")

sa(4, "Slide 22 / 23",
 "Explain in one sentence how MAC flooding allows an attacker to capture traffic intended for other devices.",
 "اشرح في جملة واحدة كيف يتيح إغراق MAC للمهاجم التقاط حركة موجّهة لأجهزة أخرى.",
 "The attacker floods the switch with thousands of fake MAC addresses until the <b>CAM table is full</b>; the switch can no longer learn new addresses and <b>floods unknown frames to all ports like a hub</b>, so the attacker sees traffic meant for others (slides 22–23).",
 "يُغرق المهاجم المحوّل بآلاف عناوين MAC المزيّفة حتى <b>يمتلئ جدول CAM</b>، فلا يعود المحوّل قادراً على تعلّم عناوين جديدة و<b>يبث الإطارات المجهولة إلى كل المنافذ كالـ Hub</b>، فيرى المهاجم حركة موجّهة لغيره (الشريحتان ٢٢–٢٣).")

sa(4, "Slide 26",
 "Describe the three steps of the port mirroring process.",
 "صف الخطوات الثلاث لعملية نسخ المنافذ.",
 "(1) The switch <b>duplicates packets from selected ports</b>; (2) the <b>copied traffic is sent to a monitoring device</b>; (3) <b>packet analyzers capture and inspect the mirrored traffic</b> (slide 26).",
 "(١) المحوّل <b>ينسخ الحزم من المنافذ المحددة</b>؛ (٢) تُرسَل <b>الحركة المنسوخة إلى جهاز المراقبة</b>؛ (٣) <b>محللات الحزم تلتقط وتفحص الحركة المنسوخة</b> (الشريحة ٢٦).")
