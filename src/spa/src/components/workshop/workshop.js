import ModulesNavComponent from '../modules-nav/modules-nav.vue'
export default {
  name: 'WorkshopComponent',
  components: {
    ModulesNavComponent
  },
  data: () => ({
    loaded: false,
    workshop: {}
  }),
  computed: {
    i18n() {
      return this.$store.state.i18n.workshop
    }
  },
  watch: {
    $route() {
      this.loaded = false
      this.getWorkshop()
    }
  },
  created() {
    this.getWorkshop()
  },
  methods: {
    getWorkshop() {
      this.$api.getWorkshop(`/api/v1/tracks/${this.$route.params.track}/workshops/${this.$route.params.workshop}`)
        .then(workshop => {
          document.title = `${workshop.title} - ${document.title}`
          this.workshop = workshop
          this.loaded = true
        }).catch(() => {
          this.$store.dispatch('progress', { error: true })
        })
    },
    getContinueURL(workshop) {
      let module = this.$store.getters.profile('last_opened_module_slug')
      let lesson = this.$store.getters.profile('last_opened_lesson_slug')

      workshop.modules.forEach((m) => {
        if (m.url.params.module === module) {
          m.lessons.forEach((l) => {
            if (l.url.params.lesson === lesson) {
              this.$router.push(l.url)
            }
          })
        }
      })
    },
    toggleAvatar() {
      var isBreak = false
      document.querySelectorAll('.author').forEach((author) => {
        if (author.querySelector('.info').clientWidth >= (author.clientWidth - 58)) {
          document.querySelectorAll('.avatar').forEach((avatar) => {
            avatar.style.display = 'none'
          })
          isBreak = true
        } else {
          if (!isBreak) {
            document.querySelectorAll('.avatar').forEach((avatar) => {
              avatar.style.display = 'inline-flex'
            })
          }
        }
      })
    }
  },
  mounted() {
    window.addEventListener('resize', this.toggleAvatar)

    this.$nextTick(function() {
      this.toggleAvatar()
    })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
