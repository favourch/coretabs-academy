import InnerHeaderComponent from '../inner-header/inner-header.vue'
export default {
  name: 'ProfileSettingsComponent',
  components: {
    InnerHeaderComponent
  },
  data: () => ({
    header: '',
    drawer: {
      isOpen: null,
      isRight: false
    }
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
        case 'change-track':
          this.header = this.i18n.change_track
          break
        case 'change-password':
          this.header = this.i18n.change_password
          break
      }
    }
  },
  created() {
    this.$on('toggle-drawer', function(data) {
      this.drawer.isOpen = !this.drawer.isOpen
    })
    this.drawer.isRight = this.$store.state.direction === 'rtl'
  },
  mounted() {
    this.setHeaderTitle(this.$route.name)
    this.$nextTick(() => { this.initMenu() })
  }
}
