/* eslint-disable */
const hljs = require('highlight.js')
export default {
  name: 'LessonComponent',
  data: () => ({
    loaded: false,
    content: {
      video: null,
      markdown: null,
      tab: null
    },
    quiz: {
      currentQuestion: 1,
      questions: null
    }
  }),
  computed: {
    module() {
      return this.$parent.current.modules.find(module => {
        return module.url.params.module === this.$route.params.module
      })
    },
    lesson() {
      return this.module.lessons.find(lesson => {
        return lesson.slug === this.$route.params.lesson
      })
    },
    i18n() {
      return this.$store.state.i18n.lesson
    },
    endpoint() {
      let track = this.$store.getters.profile('track')
      let workshop = this.$route.params.workshop
      let module = this.$route.params.module
      let lesson = this.$route.params.lesson

      return `/api/v1/tracks/${track}/workshops/${workshop}/modules/${module}/lessons/${lesson}`
    }
  },
  watch: {
    $route() {
      this.getLesson()
      this.quiz.currentQuestion = 1
    },
    'quiz.questions': {
      handler: function (after, before) {
        let questions = after
        let count = 0
        questions.forEach((q) => { if (q.success) count++ })

        if(questions.length === count) {
          this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
        }
      },
      deep: true
    }
  },
  created() {
    this.getLesson()
  },
  methods: {
    goPrevLesson() {
      let module, lesson, link

      if(this.lesson.index > 1) {
        lesson = this.module.lessons[this.lesson.index - 2]
        link = this.module.url.params.module + '/' + lesson.slug
      } else {
        if (this.module.index > 1) {
          module = this.$parent.current.modules[this.module.index - 2]
          lesson = module.lessons[module.lessons.length - 1]
          link = module.url.params.module + '/' + lesson.slug
        } else {
          link = ''
        }
      }
      
      this.$router.push('/classroom/'+ this.$parent.current.workshop.URL.params.track +'/' + this.$parent.current.workshop.URL.params.workshop + '/' + link)
    },
    goNextLesson() {
      let module, lesson, link

      if(this.lesson.index < this.module.lessons.length) {
        lesson = this.module.lessons[this.lesson.index]
        link = this.module.url.params.module + '/' + lesson.slug
      } else {
        if (this.module.index < this.$parent.current.modules.length) {
          module = this.$parent.current.modules[this.module.index]
          lesson = module.lessons[0]
          link = module.url.params.module + '/' + lesson.slug
        } else {
          link = ''
        }
      }
      
      this.$router.push('/classroom/'+ this.$parent.current.workshop.URL.params.track +'/' + this.$parent.current.workshop.URL.params.workshop + '/' + link)
    },
    getLesson() {
      let lesson = this.$parent.current.lesson
      let workshop = this.$parent.current.workshop      
      document.title = `${lesson.title} - ${workshop.title}`
      
      switch (lesson.type) {
        case '0':
          let youtube = /(?:http?s?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)/g
          this.content.video = lesson.video.replace(youtube, 'https://www.youtube.com/embed/$1')
          
          axios.get(lesson.markdown)
            .then(response => {
              this.content.markdown = this.previewMarkdowText(response.data)
              setTimeout(() => { this.parser() }, 50)
              this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '1':
          this.content.video = lesson.video
          axios.get(lesson.markdown)
            .then(response => {
              this.content.markdown = this.previewMarkdowText(response.data)
              setTimeout(() => { this.parser() }, 50)
              this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '2':
          axios.get(lesson.markdown)
            .then(response => {
              this.content.markdown = this.previewMarkdowText(response.data)
              setTimeout(() => { this.parser() }, 50)
              this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '3':
          let version = lesson.markdown.replace('.md', '').substr(-2)
          version = (/^[0-9]+$/.test(version)) ? version : null
          
          axios.get(lesson.markdown)
            .then(async (response) => {
              this.quiz.questions = (version) ? await this.quizParser(response.data, version) : response.data
              setTimeout(() => { this.parser() }, 50)
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
            break
        case '4':
          axios.get(lesson.markdown)
            .then(response => {
              this.content.markdown = this.previewMarkdowText(response.data)
              setTimeout(() => { this.parser() }, 50)
              this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
      }
    },
    async quizParser(data, version) {
      if (version === '01') {
        let questions = []
        let question = {
          text: null,
          answers: {},
          correct: [],
          hint: null,
          choose: []
        }
        let property = null
        let index = null

        let lines = data.split('\n')
        lines.forEach((line, i) => {
          if (line.startsWith('^')) {
            property = 'text'
            index = 0
            question.text = line.substr(2)
          } else if (line.startsWith('*')) {
            property = 'answers'
            index += 1
            question.answers[index] = line.substr(2)

            if (line.startsWith('**')) {
              question.answers[index] = line.substr(3)
              question.correct.push(index.toString())
            }
          } else if (line.startsWith('$')) {
            property = 'hint'
            question.hint = line.substr(2)
          } else if (line && !line.startsWith('-')) {
            if (property === 'answers') {
              question.answers[index] += '\n' + line
            } else {
              question[property] += '\n' + line
            }
          }

          if (line.startsWith('-') || i === (lines.length - 1)) {
            questions.push(question)
            question = {
              text: null,
              answers: {},
              correct: [],
              hint: null,
              choose: []
            }
            property = null
          }
        })

        return await questions
      } else {
        this.$store.dispatch('progress', { error: true })
      }
    },
    previewMarkdowText(mdText) {
      return this.$markdown.render(mdText)
    },
    parser() {
      document.querySelectorAll('.lesson-markdown img').forEach((img) => {
        let src = img.src.replace(/^.*[\\/]/, 'assets/')
        src = `${this.$parent.current.lesson.markdown.replace(/[a-zA-Z-]+\.md/, '')}${src}`
        img.src = src
      })

      document.querySelectorAll('.lesson-markdown a').forEach((link) => {
        if(!link.getAttribute('target')) {
          link.setAttribute('target', '_blank')
        }
      })
  
      document.querySelectorAll('.lesson-markdown pre code, .lesson-quiz pre code').forEach((code) => {
        hljs.highlightBlock(code)
      })
    },
    chooseAnswer(question, answer) {
      if (question.correct.length === 1) {
        question.choose = []
        if (!question.choose.includes(answer)) {
          question.choose.push(answer)
        }
        this.checkAnswers(question)
      } else {
        if (question.status) {
          question.status = ''
        }
        if (question.choose.includes(answer)) {
          question.choose.splice(question.choose.indexOf(answer), 1)
        } else {
          question.choose.push(answer)
        }
      }
    },
    checkAnswers(question) {
      question.choose.sort()
      if (question.choose.toString() === question.correct.toString()) {
       question.result = this.i18n.quiz.results_texts.success
        if (question.correct.length > 1) question.status = 'true_answer_checkbox'
        question.success = true
      } else {
        question.result = this.i18n.quiz.results_texts.fail
        question.success = false
      }
    }
  }
}
