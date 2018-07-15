import ModulesNavComponent from '../modules-nav/modules-nav.vue'
import InnerHeaderComponent from '../inner-header/inner-header.vue'
export default {
  name: 'ModulesComponent',
  components: {
    ModulesNavComponent,
    InnerHeaderComponent
  },
  data: () => ({
    height: 0,
    modules: [],
    loaded: false,
    drawer: {
      isOpen: true,
      isRight: false
    },
    current: {
      lesson: {},
      workshop: {}
    }
  }),
  created() {
    this.$on('toggle-drawer', function(data) {
      this.drawer.isOpen = !this.drawer.isOpen
    })
    this.drawer.isRight = this.$store.state.direction === 'rtl'

    this.current.workshop.URL = {
      name: 'workshop',
      params: {
        workshop: this.$route.params.workshop
      }
    }

    let modulesData = this.$route.params.modules
    if (typeof modulesData === 'undefined') {
      this.getModules()
    } else {
      this.current.workshop.title = this.$route.params._workshop.title
      this.current.workshop.forums = this.$route.params._workshop.forums

      this.modules = modulesData
      this.getCurrentLesson(this.$api.getModuleId(this.modules).lessons)
      this.loaded = true
    }
  },
  watch: {
    $route() {
      this.current.lesson = this.$api.getLessonId(this.$api.getModuleId(this.modules).lessons)
    }
  },
  methods: {
    getModules() {
      this.$api.getWorkshop(`/api/v1/tracks/${this.$route.params.track}/workshops/${this.$route.params.workshop}`)
        .then(workshop => {
          this.current.workshop.title = workshop.title
          this.current.workshop.forums = workshop.workshop_forums_url

          this.modules = workshop.modules
          let module = this.$api.getModuleId(this.modules)
          if (typeof module !== 'undefined') {
            this.getCurrentLesson(module.lessons)
            this.loaded = true
          } else {
            this.$router.push('/404')
          }
        }).catch(() => {
          this.$store.dispatch('progress', { error: true })
        })
    },
    getCurrentLesson(lessons) {
      if (typeof this.$route.params.lesson !== 'undefined') {
        this.current.lesson = this.$api.getLessonId(lessons)
      } else {
        this.current.lesson = lessons[0]
        this.$router.push({
          name: 'lessons',
          params: {
            lesson: this.current.lesson.url.params.lesson
          },
          query: this.current.lesson.url.query
        })
      }
    },
    onResize() {
      let selector = '.modules >.inner-header >.toolbar'
      if (document.querySelector(selector) !== null) {
        this.height = window.innerHeight - document.querySelector(selector).offsetHeight
      } else {
        let self = this
        setTimeout(() => {
          self.height = window.innerHeight - document.querySelector(selector).offsetHeight
        }, 100)
      }
    }
  }
}
