import InnerHeaderComponent from '../inner-header/inner-header.vue'
import NavigatorDrawerComponent from '../navigator-drawer/navigator-drawer.vue'
export default {
  name: 'ProfileSettingsComponent',
  components: {
    InnerHeaderComponent,
    NavigatorDrawerComponent
  },
  data: () => ({
    height: 0,
    header: '',
    currentRoute: 'personal-info',
    drawer: {
      isOpen: null,
      isRight: false
    },
    items: [
      { title: 'Classrome', icon: 'dashboard' },
      { title: 'About', icon: 'question_answer' }
    ],
    navDrawer: [
      {
        name: 'personal-info',
        text: '',
        icon: 'settings',
        route: '/profile/personal-info'
      },
      {
        name: 'profile-info',
        text: '',
        icon: 'person',
        route: '/profile/profile-info'
      },
      {
        name: 'manage-projects',
        text: '',
        icon: 'business_center',
        route: '/profile/manage-projects'
      },
      {
        name: 'change-track',
        text: '',
        icon: 'compare_arrows',
        route: '/profile/change-track'
      },
      {
        name: 'change-password',
        text: '',
        icon: 'lock',
        route: '/profile/change-password'
      }
    ],
    mini: true
  }),
  computed: {
    i18n() { return this.$store.state.i18n.account.titles }
  },
  watch: {
    $route(to, from) {
      this.setHeaderTitle(to.name)
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
    setHeaderTitle(name) {
      switch (name) {
        case 'personal-info':
          this.header = this.i18n.personal_info
          break
        case 'profile-info':
          this.header = this.i18n.profile_info
          break
        case 'change-track':
          this.header = this.i18n.change_track
          break
        case 'change-password':
          this.header = this.i18n.change_password
          break
        case 'manage-projects':
          this.header = this.i18n.manage_projects
          break
      }
    },
    onResize() {
      let selector = '.settings .inner-header .toolbar'
      if (document.querySelector(selector) !== null) {
        this.height = window.innerHeight - document.querySelector(selector).offsetHeight
      } else {
        let self = this
        this.timeout = setTimeout(() => {
          self.height = window.innerHeight - document.querySelector(selector).offsetHeight
        }, 100)
      }
    },
    setCurrentRoute(route) {
      this.currentRoute = route
    }
  },
  created() {
    this.$on('toggle-drawer', function(data) {
      this.drawer.isOpen = !this.drawer.isOpen
    })
    this.drawer.isRight = this.$store.state.direction === 'rtl'
    this.navDrawer[0].text = this.i18n.personal_info
    this.navDrawer[1].text = this.i18n.profile_info
    this.navDrawer[2].text = this.i18n.manage_projects
    this.navDrawer[3].text = this.i18n.change_track
    this.navDrawer[4].text = this.i18n.change_password
  },
  mounted() {
    this.setHeaderTitle(this.$route.name)
    this.$nextTick(() => { this.initMenu() })
  }
}
