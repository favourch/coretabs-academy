/* eslint-disable */
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
    },
    'quiz.questions': {
      handler: function (after, before) {
        let questions = after
        let count = 0
        questions.forEach((q) => { if (q.success) count++ })

        if(questions.length === count) {
          if (!this.$parent.current.lesson.is_shown) {
            this.$parent.current.lesson.is_shown = this.$auth.showLesson(this.endpoint, this.$store)
          }
        }
      },
      deep: true
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
              this.quiz.questions = response.data
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
