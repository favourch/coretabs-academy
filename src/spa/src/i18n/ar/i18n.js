import page from './page'
import auth from './auth'
import about from './about'
import workshop from './workshop'
import lesson from './lesson'

var i18n = `{
  "app": {
    "lang": "ar",
    "direction": "rtl",
    "rev_direction": "ltr",
    "progress": {
      "loadingText": "يُرجى الانتظار قليلًا",
      "errorText": "خطأ.. حاول مرة أخرى!"
    }
  },
  "header": {
    "default_navs": [
      "تسجيل الدخول",
      "عن الأكاديمية"
    ],
    "user_navs": [
      "الصف الدراسي",
      "عن الأكاديمية"
    ],
    "admin_navs": []
  },
  "inner_header": {
    "profile_settings_btn_text": "إعدادات الحساب",
    "logout_btn_text": "تسجيل خروج"
  },
  "home": {
    "heading_text": "إن تعلم البرمجة شيء رائع!",
    "description_text_1": "الأروع من ذلك أن أكاديمية Coretabs ستقوم بتوجيهك لبدأ تعلمها عبر عمل تطبيقات من أول يوم.",
    "description_text_2": "مستعد لتغيير حياتك وتعلم مهارات جديدة؟",
    "yes_btn_text": "نعم، اكتشف ميولي",
    "no_btn_text": "لا، أنا لست مستعداً"
  },
  "not_ready": {
    "heading_text": [
      "البرمجة لغة المستقبل",
      "هل أنت مستعد لهذه التجربة؟"
    ],
    "description_text": [
      "تعتبر البرمجة من أكثر المجالات طلباً في سوق العمل، فمن يوم لأخر تصبح العديد من المجالات أكثر اعتماداً عليها بشكل أساسي لهذا أصبحت لا تقل أهمية عن لغاتنا نحن البشر بل أنها تعتبر لغة المستقبل.",
      "لا يُتطلب منك أن تكون خارق الذكاء، كل ما ستحتاج إليه هو كمبيوتر، اتصال بالإنترنت وهدف تسعى لتحقيقه ونحن سنأخذ بيدك لتعلم البرمجة بأسلوب مبسط وتطبيقي."
    ],
    "source_text": "الإحصائيات التالية من استطلاع قام به أكثر من 100,000 مبرمج من أنحاء العالم في العام 2018 استناداً لموقع <a href='https://insights.stackoverflow.com/survey/2018/' target='_blank'>Stack Overflow</a>",
    "statistics": [{
      "desc": "تعلموا البرمجة تعليم ذاتي، بعيداً عن التعليم الجامعي",
      "value": "90%"
    }, {
      "desc": "حاصلين على وظيفة أو يعملون بدوام جزئي إما في شركات أو كعمل حر",
      "value": "90%"
    }, {
      "desc": "متوسط الدخل الشهري للفرد أي بمعدل 56000 دولار سنوياً",
      "value": "$4666"
    }, {
      "desc": "يعملون في قطاعات أخرى غير قطاع تقنية المعلومات",
      "value": "46%"
    }],
    "yes_btn_text": "نعم، اكتشف ميولي"
  },
  "about": ${JSON.stringify(about)},
  "workshops": {
    "title": "قائمة ورش العمل"
  },
  "workshop": ${JSON.stringify(workshop)},
  "lesson": ${JSON.stringify(lesson)},
  "form": {
    "fullname_label": "اسمك الكامل",
    "fullname_length_error": "اسم المستخدم لا يجب أن يتجاوز 20 حرفًا",
    "email_label": "البريد الإلكتروني",
    "email_validator_error": "البريد الإلكتروني غير صالح",
    "username_label": "اسم المستخدم",
    "username_length_error": "اسم المستخدم لا يجب أن يتجاوز 20 حرفًا",
    "password_label": "كلمة السر",
    "new_password_label": "كلمة المرور الجديدة",
    "password_length_error": "كلمة السر يجب أن تتكون من 8 أحرف على الأقل",
    "message_label": "أدخل رسالتك هنا",
    "message_length_error": "الرسالة قصيرة جدًا"
  },
  "contact": {
    "forums_text": "تذكر في حال احتجت إلى مساعدة بإمكانك بدء نقاش مع زملائك والموجهين من خلال المنتدى <a href='http://forums.coretabs.net' target='_blank'>من هنا</a>",
    "heading_title_text": "اتصل بنا",
    "description_text": "للتواصل معنا قم باستخدام النموذج التالي أو بإمكانك مراسلتنا مباشرة على العنوان <a href='mailto:info@coretabs.com'>info@coretabs.com</a>",
    "submit_btn_text": "إرسال"
  },
  "page": ${JSON.stringify(page)},
  "auth": ${JSON.stringify(auth)},
  "select_track": {
    "track_1_text_en": "BACK-END TRACK",
    "track_1_text_ar": "مسار تطوير نظم خلفية",
    "track_2_text_en": "FRONT-END TRACK",
    "track_2_text_ar": "مسار تطوير واجهات الويب",
    "submit_btn_text": "ابدأ المسار"
  },
  "profile": {
    "titles": {
      "settings": "إعدادات الحساب",
      "personal_info": "المعلومات الشخصية",
      "change_track": "تغيير المسار",
      "change_password": "تغيير كلمة السر"
    },
    "personal_info": {
      "success_message": "تم تغيير بياناتك الشخصية بنجاح",
      "logout_message": "يُرجى تأكيد بريدك الإلكتروني الجديد",
      "submit_btn_text": "حفظ التغييرات"
    },
    "change_track": {
      "success_message": "تم تغيير المسار بنجاح.",
      "heading_text": "اختر المسار المطلوب",
      "select_text": "اختر",
      "hint_text": "بإمكانك العودة للمسار الحالي لاحقاُ للإكمال من حيث توقفت",
      "submit_btn_text": "حفظ التغييرات"
    },
    "change_password": {
      "old_password": "كلمة المرور الحالية",
      "new_password": "كلمة المرور الجديدة",
      "re_new_password": "تأكيد كلمة المرور الجديدة",
      "submit_btn_text": "حفظ التغيرات"
    }
  }
}`

export default JSON.parse(i18n)
