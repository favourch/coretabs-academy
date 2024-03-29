import HeaderComponent from './components/header/header.vue'
export default {
  name: 'app',
  components: {
    HeaderComponent
  },
  computed: {
    i18n() {
      return this.$store.state.i18n.app
    }
  },
  methods: {
    setProperty(element, prop, value) {
      element.style.setProperty(prop, value, 'important')
    },
    updateHeader() {
      let isAbout = document.querySelector('#about')
      let isTracks = document.querySelector('#track')
      let header = document.querySelector('header')
      let brandLogo = document.querySelector('.brand-logo')
      let burgerMenu = document.querySelector('.toolbar__side-icon')
      if (isAbout || isTracks) {
        let prevPosition = window.pageYOffset
        window.addEventListener('scroll', () => {
          let currentPosition = window.pageYOffset
          if (window.scrollY >= window.innerHeight && prevPosition > currentPosition) {
            header.classList.add('fixed-header')
            header.classList.add('slide-bottom')
            this.setProperty(brandLogo, 'margin', '10px')
            this.setProperty(burgerMenu, 'margin', '0 16px 4px 0')
          } else {
            header.classList.remove('fixed-header')
            header.classList.remove('slide-bottom')
            this.setProperty(brandLogo, 'margin', '25px 10px 10px 20px')
            this.setProperty(burgerMenu, 'margin', '13px 20px 29px 10px')
          }
          prevPosition = currentPosition
        })
      } else {
        header.classList.remove('fixed-header')
        header.classList.remove('slide-bottom')
        this.setProperty(brandLogo, 'margin', '25px 10px 10px 20px')
        this.setProperty(burgerMenu, 'margin', '13px 20px 29px 10px')
      }
    },
    triggerFixedHeader() {
      let fixedHeaderPages = ['frontend-track', 'backend-track', 'about']
      let currentRoutePath = this.$router.currentRoute.name
      if (fixedHeaderPages.includes(currentRoutePath)) {
        this.updateHeader()
      }
    }
  },
  created() {
    this.$store.state.direction = this.i18n.direction
    this.$store.state.rev_direction = this.i18n.rev_direction

    this.$store.dispatch('getImgUrl', 'icons/logo.png').then(img => {
      this.$store.state.logo = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'icons/icon.png').then(img => {
      this.$store.state.icon = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'icons/forums-logo.png').then(img => {
      this.$store.state.forumLogo = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.state.css.workshops.drawerWidth = 350
    if (typeof document !== 'undefined') {
      document.querySelector('html').setAttribute('lang', this.i18n.lang)
      document.querySelector('html').setAttribute('dir', this.i18n.direction)
    }
  },
  updated() {
    this.triggerFixedHeader()
  },
  mounted() {
    this.triggerFixedHeader()
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onResize)
  }
}
