import ModulesNavComponent from '../modules-nav/modules-nav.vue'
export default {
  name: 'WorkshopComponent',
  components: {
    ModulesNavComponent
  },
  data: () => ({
    loaded: false,
    workshop: {},
    interval: {},
    progressValue: 0
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
    getContinueURL() {
      let module = this.$store.getters.account('last_opened_module_slug')
      let lesson = this.$store.getters.account('last_opened_lesson_slug')
      let workshop = this.$store.getters.account('last_opened_workshop_slug')
      let track = this.$store.getters.account('track')
      this.$router.push(`/classroom/${track}/${workshop}/${module}/${lesson}`)
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
    this.interval = setInterval(() => {
      if (this.progressValue > this.workshop.shown_percentage && this.progressValue >= 0) {
        this.progressValue--
      }
      if (this.progressValue < this.workshop.shown_percentage && this.progressValue <= 100) {
        this.progressValue++
      }
      return this.progressValue
    }, 4)
  },
  beforeDestroy() {
    clearInterval(this.interval)
    window.removeEventListener('resize', this.onResize)
  }
}
