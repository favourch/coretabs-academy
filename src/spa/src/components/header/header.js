export default {
  name: 'HeaderComponent',
  data: () => ({
    navs: [],
    show: true,
    currentClass: '',
    role: 'default_navs',
    default_navs: [
      {
        url: '/signin',
        radius: true
      }, {
        url: '/about',
        dropdown: false
      }, {
        url: '/tracks',
        dropdown: false
      }
    ],
    user_navs: [
      {
        url: '/classroom/tour/',
        radius: true
      }, {
        url: '/about',
        dropdown: false
      }, {
        url: '/tracks',
        dropdown: false
      }
    ],
    admin_navs: [],
    fixed: false,
    drawer: {
      width: 0,
      isOpen: false,
      isRight: false
    },
    i18n: null
  }),
  created() {
    this.setHeader()
    if (typeof window !== 'undefined') { this.drawer.width = window.innerWidth }
    this.drawer.isRight = this.$store.state.direction === 'rtl'
    this.i18n = this.$store.state.i18n.header[this.role]

    if (this.$store.getters.isLogin) {
      if (this.$store.getters.account('track')) {
        if(this.$route.path.includes('classroom') && !this.$route.params.workshop) {
          this.$router.push(`/classroom/${this.$store.getters.account('track')}/`)
        }
      } else {
        if(!this.$store.getters.user('batch_status')) {
          this.$router.push('/batch-not-started')
        } else {
          this.$router.push('/select-track')
        }
      }
    }
  },
  watch: {
    $route() {
      this.setHeader()
      if (typeof document !== 'undefined') {
        let el = document.querySelector('main.content')
        el.className = ''
        el.classList.add('content')
        el.classList.add(this.currentClass)
      }
    }
  },
  mounted() {
    if (typeof document !== 'undefined') {
      let el = document.querySelector('main.content')
      el.className = ''
      el.classList.add('content')
      el.classList.add(this.currentClass)
    }
  },
  methods: {
    setHeader() {
      this.$store.dispatch('progress', { error: false })
      this.currentClass = `${this.$route.name}-main-content`

      switch (this.$route.name) {
        case 'personal-info':
        case 'profile-info':
        case 'change-track':
        case 'change-password':
        case 'profile-about':
        case 'profile-certificates':
        case 'lessons':
        case 'modules':
        case 'workshop':
        case 'workshops':
          this.show = false
          break
        default:
          this.show = true
          this.role = 'default_navs'
          this.i18n = this.$store.state.i18n.header[this.role]
          this.navs = this.default_navs
          if (this.$store.getters.isLogin) {
            this.role = 'user_navs'
            this.navs = this.user_navs
            if (this.$store.getters.account('track')) {
              this.user_navs[0].url = `/classroom/${this.$store.getters.account('track')}/`
            }
            if (!this.$store.getters.user('batch_status')) {
              this.user_navs[0].url = `/logout/`
              this.role = 'waiting_batch_navs'
            }
            this.i18n = this.$store.state.i18n.header[this.role]
          }
          break
      }
    },
    toggleDrawer() {
      this.drawer.isOpen = !this.drawer.isOpen
    }
  }
}
