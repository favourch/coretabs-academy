import InnerHeaderComponent from '../inner-header/inner-header.vue'
import NavigatorDrawerComponent from '../navigator-drawer/navigator-drawer.vue'
export default {
  name: 'WorkshopsComponent',
  components: {
    InnerHeaderComponent,
    NavigatorDrawerComponent
  },
  data: () => ({
    height: 0,
    loaded: false,
    timeout: null,
    workshops: [],
    drawer: {
      isOpen: null,
      isRight: false
    },
    current: {
      workshop: {}
    }
  }),
  computed: {
    i18n() {
      return this.$store.state.i18n.workshops
    }
  },
  watch: {
    $route() {
      this.getWorkshops()
    }
  },
  methods: {
    initMenu() {
      if (document.documentElement.clientWidth < 1264) {
        this.drawer.isOpen = false
      } else {
        this.drawer.isOpen = true
      }
    },
    onResize() {
      let selector = '.workshops .inner-header .toolbar'
      if (document.querySelector(selector) !== null) {
        this.height = window.innerHeight - document.querySelector(selector).offsetHeight
      } else {
        let self = this
        this.timeout = setTimeout(() => {
          self.height = window.innerHeight - document.querySelector(selector).offsetHeight
        }, 100)
      }
    },
    progress(percent) {
      let maxPercent = 100
      let increment = 360 / maxPercent
      let half = Math.round(maxPercent / 2)
      let gradient = ''
      if (percent < half) {
        let nextdeg = 90 + (increment * percent)
        gradient = `linear-gradient(90deg, var(--workshop-normal-state) 50%, transparent 50%, transparent),linear-gradient(${nextdeg}deg, var(--workshop-complete-state) 50%, var(--workshop-normal-state) 50%, var(--workshop-normal-state))`
      } else {
        let nextdeg = -90 + (increment * (percent - half))
        gradient = `linear-gradient(${nextdeg}deg, var(--workshop-complete-state) 50%, transparent 50%, transparent),linear-gradient(270deg, var(--workshop-complete-state) 50%, var(--workshop-normal-state) 50%, var(--workshop-normal-state))`
      }
      return gradient
    },
    getWorkshops() {
      this.$api.getWorkshops(`/api/v1/tracks/${this.$route.params.track}/workshops/`)
      .then(async(data) => {
        this.workshops = await data
        if (typeof this.$route.params.workshop === 'undefined') {
          this.$router.push({
            name: 'workshop',
            params: {
              workshop: this.workshops[0].url.params.workshop
            }
          })
        } else {
          this.current.workshop = this.$api.getWorkshopId(this.workshops)
        }
        this.loaded = true
      }).catch(() => {
        this.$store.dispatch('progress', { error: true })
      })
    }
  },
  created() {
    this.$on('toggle-drawer', function(data) {
      this.drawer.isOpen = !this.drawer.isOpen
    })
    this.$on('clearTimeout', function(data) {
      clearTimeout(this.timeout)
    })
    this.drawer.isRight = this.$store.state.direction === 'rtl'

    this.getWorkshops()
  },
  updated() {
    document.querySelectorAll('#sidenav .stepper__step__step').forEach((stepper, index) => {
      stepper.setAttribute('data-index', index + 1)
      if (this.workshops[index].shown_percentage !== 0 && this.workshops[index].shown_percentage !== 100) {
        stepper.style.background = this.progress(this.workshops[index].shown_percentage)
      }
    })
  },
  mounted() {
    this.$nextTick(() => {
      this.initMenu()
    })
  }
}
