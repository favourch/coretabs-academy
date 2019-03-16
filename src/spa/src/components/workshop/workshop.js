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
    },
    durationUnit() {
      let duration = this.workshop.duration
      if (duration > 1 && duration < 11) {
        return this.i18n.card1.duration.hours
      }
      else {
        return this.i18n.card1.duration.hour
      }
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
    getAuthorAvatar(url) {
      if (url.slice(0, 4) !== 'http') {
        url = `${process.env.API_BASE_URL || ''}${url}`
      }
      return url
    },
    getContinueURL(workshop) {
      let module = this.$store.getters.account('last_opened_module_slug')
      let lesson = this.$store.getters.account('last_opened_lesson_slug')

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
