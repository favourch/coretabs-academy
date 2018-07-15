/* eslint-disable */
export default {
  name: 'LessonComponent',
  data: () => ({
    loaded: false,
    content: {
      video: null,
      markdown: null
    },
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
  computed: {
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
    }
  },
  created() {
    this.getLesson()
  },
  methods: {
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
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              }
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
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              }
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
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
              }
              this.loaded = true
            }).catch(() => {
              this.$store.dispatch('progress', { error: true })
            })
          break
        case '3':
          axios.get(lesson.markdown)
            .then(response => {
              this.content.markdown = response.data
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
              if (!this.$parent.current.lesson.is_shown) {
                this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
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
    parser() {
      document.querySelectorAll('.lesson-markdown img').forEach((img) => {
        let src = img.src.replace(/^.*[\\/]/, '')
        src = `${this.$parent.current.lesson.markdown.replace(/[a-zA-Z-]+\.txt/, '')}${src}`
        img.src = src
      })
  
      document.querySelectorAll('.lesson-markdown pre code').forEach((code) => {
        hljs.highlightBlock(code)
      })
    },
    chooseAnswer(questions, question, answer) {
      if (question.correct.length === 1) {
        question.choose = []
        if (!question.choose.includes(answer)) {
          question.choose.push(answer)
        }
        this.checkAnswers(questions, question)
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
    checkAnswers(questions, question) {
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
      
      let count = 0
      questions.forEach((q) => {
        if (q.true) count++
      })
      if(questions.length === count) {
        if (!this.$parent.current.lesson.is_shown) {
          this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
        }
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
