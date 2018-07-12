/* eslint-disable */
export default {
  name: 'LessonComponent',
  components: {},
  data: () => ({
    type: '',
    loaded: false,
    notes_content: '',
    lesson_content: '',
    quiz: {
      result: '',
      status: {
        right: ''
      }
    },
    current: {
      quiz: 0,
      tab: null
    }
  }),
  created() {
    this.getLesson()
  },
  watch: {
    $route(to, from) {
      this.getLesson()
    }
  },
  computed: {
    i18n() {
      return this.$store.state.i18n.lesson
    }
  },
  updated() {
    document.querySelectorAll('#lesson-markdown img').forEach((img) => {
      let src = img.src.replace(/^.*[\\/]/, '')
      src = `${this.$encryption.b64DecodeUnicode(this.$route.query.url).replace(/[a-zA-Z-]+\.txt/, '')}/${src}`
      img.src = src
    })

    document.querySelectorAll('#lesson-markdown pre code').forEach((code) => {
      hljs.highlightBlock(code)
    })
  },
  methods: {
    getLesson() {
      let url = this.$encryption.b64DecodeUnicode(this.$route.query.url)
      this.type = this.$encryption.b64DecodeUnicode(this.$route.query.type)
      let notes = this.$encryption.b64DecodeUnicode(this.$route.query.notes)

      let track = this.$store.getters.profile('track')
      let workshop = this.$route.params.workshop
      let module = this.$route.params.module
      let lesson = this.$route.params.lesson
      let endpoint = `/api/v1/tracks/${track}/workshops/${workshop}/modules/${module}/lessons/${lesson}`

      switch (this.type) {
        case '0':
          this.lesson_content = url
          break
        case '1':
          let youtube = /(?:http?s?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)/g
          url = url.replace(youtube, 'http://www.youtube.com/embed/$1')
          this.lesson_content = url

          axios.get(notes)
            .then(response => {
              this.notes_content = this.previewMarkdowText(response.data)
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(endpoint, this.$store)
              }
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '2':
          axios.get(url)
            .then(response => {
              this.lesson_content = this.previewMarkdowText(response.data)
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(endpoint, this.$store)
              }
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '3':
          axios.get(url)
            .then(response => {
              this.lesson_content = response.data
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(endpoint, this.$store)
              }
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '4':
          axios.get(url)
            .then(response => {
              this.lesson_content = this.previewMarkdowText(response.data)
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(endpoint, this.$store)
              }
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
      }
    },
    previewMarkdowText(mdText) {
      return this.$markdown.render(mdText)
    },
    chooseAnswer(question, answer) {
      if (question.correct.length === 1) {
        question.choose = []
        if (!question.choose.includes(answer)) {
          question.choose.push(answer)
        }
        this.checkAnswers(question, answer)
      } else {
        if (this.quiz.status.right) {
          this.quiz.status.right = ''
        }
        if (question.choose.includes(answer)) {
          question.choose.splice(question.choose.indexOf(answer), 1)
        } else {
          question.choose.push(answer)
        }
      }
    },
    checkAnswers(question, answer) {
      question.choose.sort()
      if (question.choose.toString() === question.correct.toString()) {
        this.quiz.result = this.i18n.quiz.results_texts.success
        if (question.correct.length > 1) this.quiz.status.right = 'true_answer_checkbox'
        question.true = true
        question.wrong = false
      } else {
        this.quiz.result = this.i18n.quiz.results_texts.fail
        question.true = false
        question.wrong = true
      }
    },
    goNextAnswers() {
      this.current.quiz += 1
      this.quiz.result = ''
    },
    goPrevAnswers() {
      this.current.quiz -= 1
    }
  }
}
