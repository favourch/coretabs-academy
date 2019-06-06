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
      if (isAbout || isTracks) {
        if (window.scrollY >= 100) {
          header.classList.add('fixed-header')
          this.setProperty(brandLogo, 'margin', '10px')
        } else {
          header.classList.remove('fixed-header')
          this.setProperty(brandLogo, 'margin', '25px 10px 10px 20px')
        }
      } else {
        header.classList.remove('fixed-header')
        this.setProperty(brandLogo, 'margin', '25px 10px 10px 20px')
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
  mounted() {
    window.addEventListener('scroll', this.updateHeader)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onResize)
  }
}
