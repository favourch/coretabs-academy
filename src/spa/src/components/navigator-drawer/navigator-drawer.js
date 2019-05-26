export default {
  name: 'NavigatorDrawerComponent',
  data: () => ({
    drawer: {
      isOpen: null,
      isRight: false
    },
    avatar: {
      open: null,
      close: null
    },
    items: [],
    mini: true,
  }),
  computed: {
    i18n() { return this.$store.state.i18n.navigation_drawer }
  },
  created() {
    this.drawer.isRight = this.$store.state.direction === 'rtl'

    this.$store.dispatch('getImgUrl', 'icons/icon.png').then(img => {
      this.avatar.close = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'icons/logo.png').then(img => {
      this.avatar.open = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.items.push({ route: `/classroom/${this.$store.getters.account('track')}/`, icon: 'school', title: this.i18n.classroom })
    this.items.push({ link: 'https://forums.coretabs.net', icon: 'forum', title: this.i18n.forum })
    this.items.push({ route: `/user/${this.$store.getters.user('username')}/`, icon: 'person', title: this.i18n.profile, separator: true })
    this.items.push({ route: '/profile', icon: 'settings', title: this.i18n.settings })
    this.items.push({ route: '/logout', icon: 'exit_to_app', title: this.i18n.logout })
  },
  methods: {
    toggleDrawer(event) {
      let target = event.target
      
      while (target) {
        if(target.parentNode.tagName === "ASIDE") {
          this.mini = false
          document.querySelector('main.content').classList.add('navigator-drawer-opened')
          return false
        } else {
          target = target.parentNode
          document.querySelector('main.content').classList.remove('navigator-drawer-opened')
          this.mini = true
        }
      }
    }
  }
}
