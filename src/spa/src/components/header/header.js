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
      }
    ],
    user_navs: [
      {
        url: '/classroom/tour/',
        radius: true
      }, {
        url: '/about',
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
    this.drawer.width = window.innerWidth
    this.drawer.isRight = this.$store.state.direction === 'rtl'
    this.i18n = this.$store.state.i18n.header[this.role]
  },
  watch: {
    role() { this.i18n = this.$store.state.i18n.header[this.role] },
    $route() {
      this.setHeader()
      let el = document.querySelector('main.content')
      el.className = ''
      el.classList.add('content')
      el.classList.add(this.currentClass)
    }
  },
  mounted() {
    let el = document.querySelector('main.content')
    el.className = ''
    el.classList.add('content')
    el.classList.add(this.currentClass)
  },
  methods: {
    setHeader() {
      this.$store.dispatch('progress', { error: false })
      this.currentClass = `${this.$route.name}-main-content`

      switch (this.$route.name) {
        case 'personal-info':
        case 'change-track':
        case 'change-password':
        case 'lessons':
        case 'modules':
        case 'workshop':
        case 'workshops':
          this.show = false
          break
        default:
          this.show = true
          this.role = 'default_navs'
          this.navs = this.default_navs
          if (this.$store.getters.isLogin) {
            this.role = 'user_navs'
            this.navs = this.user_navs
            if (this.$store.getters.profile('track')) {
              this.user_navs[0].url = `/classroom/${this.$store.getters.profile('track')}/`
            }
          }
          break
      }
    },
    toggleDrawer() {
      this.drawer.isOpen = !this.drawer.isOpen
    }
  }
}
