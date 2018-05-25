export default {
  name: 'NotReadyComponent',
  components: {},
  data: () => ({
    heading_text: [
     'البرمجة لغة المستقبل',
      'هل أنت مستعد لهذه التجربة؟'
    ],
    description_text: [
      'تعتبر البرمجة من أكثر المجالات طلباً في سوق العمل، فمن يوم لأخر تصبح العديد من المجالات أكثر إعتماداً عليها بشكل أساسي لهذا أصبحت لا تقل أهمية عن لغاتنا نحن البشر بل أنها تعتبر لغة المستقبل.',
      ' لا يُتطلب منك أن تكون خارق الذكاء، كل ما ستحتاج إلية هو كمبيوتر، إتصال بالإنترنت وهدف تسعى لتحقيقة ونحن سنأخذ بيدك لتعلم البرمجة بأسلوب مبسط وتطبيقي.'
    ],
    source_text: 'الإحصائيات التالية من إستطلاع قام به أكثر من 100,000 مبرمج من أنحاء العالم في العام 2018 إستناداً لموقع <a href="https://insights.stackoverflow.com/survey/2018/" target="_blank">Stackoverflow</a>',
    statistics: [
      {
        imgUrl: '~@/assets/multimedia/images/not-ready/self-taught.svg',
        desc: 'تعلموا البرمجة تعليم ذاتي، بعيداً عن التعليم الجامعي',
        value: '90%',
        reverse: false
      },
      {
        imgUrl: '~@/assets/multimedia/images/not-ready/self-taught.svg',
        desc: 'حاصلين على وظيفة أو يعملون بدوام جزئي إما في شركات أو كعمل حر',
        value: '80%',
        reverse: true
      },
      {
        imgUrl: '~@/assets/multimedia/images/not-ready/self-taught.svg',
        desc: 'متوسط الدخل الشهري للفرد أي بمعدل 56000 دولار سنوياً',
        value: '$4666',
        reverse: false
      },
      {
        imgUrl: '~@/assets/multimedia/images/not-ready/self-taught.svg',
        desc: 'يعملون في قطاعات أخرى غير قطاع تقنية المعلومات ',
        value: '46%',
        reverse: true
      }
    ],
    button_text: 'نعم, إكتشف ميولي'
  })
}
