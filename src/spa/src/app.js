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
      updateHeader() {
         var isAbout = document.querySelector('#about')
         var header = document.querySelector('header')
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
   },
   created() {
      if (window.localStorage.getItem('token') !== null && typeof window.localStorage.getItem('user') !== null) {
         this.$auth.storeUser(this.$store, {
            key: window.localStorage.getItem('token'),
            user: window.localStorage.getItem('user')
         })
      }
      this.$store.state.direction = this.i18n.direction
      this.$store.state.rev_direction = this.i18n.rev_direction
      this.$store.state.progress = {
         width: 5,
         size: 80,
         pageText: this.i18n.progress.pageText,
         lessonText: this.i18n.progress.lessonText
      }

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
      document.querySelector('html').setAttribute('lang', this.i18n.lang)
      document.querySelector('html').setAttribute('dir', this.i18n.direction)
   },
   mounted() {
      window.addEventListener('scroll', this.updateHeader)
   },
   beforeDestroy() {
      window.removeEventListener('scroll', this.onResize)
   }
}
