export default {
  name: 'HeaderComponent',
  asyncData(context) {
    // console.log('context')
    // const admin_navs = []
    // const default_navs = [{
    //   url: '/signin',
    //   radius: true
    // }, {
    //   url: '/about',
    //   dropdown: false
    // }]
    // const user_navs = [{
    //   url: '/profile',
    //   radius: true
    // }, {
    //   url: '/logout',
    //   dropdown: false
    // }, {
    //   url: '/about',
    //   dropdown: false
    // }]
    // let nav = []
    // let role = ''
    // let show = false
    // let currentClass = `${$nuxt.$route.name}-main-content`
    // switch ($nuxt.$route.name) {
    //   case 'personal-info':
    //   case 'change-track':
    //   case 'change-password':
    //   case 'lessons':
    //   case 'modules':
    //   case 'workshop':
    //   case 'workshops':
    //     show = false
    //     break
    //   default:
    //     show = true
    //     role = 'default_navs'
    //     navs = default_navs
    //     if ($nuxt.$store.getters.isLogin) {
    //       role = 'user_navs'
    //       navs = user_navs
    //     }
    //     break
    // }
    // return {
    //   navs: navs,
    //   show: show,
    //   role: role,
    //   currentClass: currentClass,
    //   i18n: $nuxt.$store.state.i18n.header[this.role]
    // }
  },
  data: () => ({
    fixed: false,
    drawer: {
      width: 0,
      isOpen: false,
      isRight: false
    }
  }),
  created() {
    // console.log(this)
    this.setHeader()
    if (process.browser) {
      this.drawer.width = window.innerWidth
    }
    this.drawer.isRight = this.$store.state.direction === 'rtl'
    // this.i18n = this.$store.state.i18n.header[this.role]
  },
  watch: {
    role() {
      // this.i18n = this.$store.state.i18n.header[this.role]
    },
    $route(to, from) {
      // this.setHeader()
      // let el = document.querySelector('main.content')
      // el.className = ''
      // el.classList.add('content')
      // el.classList.add(this.currentClass)
    }
  },
  mounted() {
    // let el = document.querySelector('main.content')
    // el.className = ''
    // el.classList.add('content')
    // el.classList.add(this.currentClass)
    // window.addEventListener('scroll', this.updateHeader)
  },
  beforeDestroy() {
    // window.removeEventListener('scroll', this.onResize)
  },
  methods: {
    setHeader() {
      // this.currentClass = `${this.$route.name}-main-content`
      // switch (this.$route.name) {
      //   case 'personal-info':
      //   case 'change-track':
      //   case 'change-password':
      //   case 'lessons':
      //   case 'modules':
      //   case 'workshop':
      //   case 'workshops':
      //     this.show = false
      //     break
      //   default:
      //     this.show = true
      //     this.role = 'default_navs'
      //     this.navs = this.default_navs
      //     if (this.$store.getters.isLogin) {
      //       this.role = 'user_navs'
      //       this.navs = this.user_navs
      //     }
      //     break
      // }
    },
    toggleDrawer() {
      this.drawer.isOpen = !this.drawer.isOpen
    },
    updateHeader() {
      let isAbout = document.querySelector('#about')
      let header = document.querySelector('header')
      if (isAbout) {
        if (window.scrollY >= 100) {
          header.classList.add('fixed-header')
        } else {
          header.classList.remove('fixed-header')
        }
      } else {
        header.classList.remove('fixed-header')
      }
    }
  }
}
