export default {
  name: 'SignInComponent',
  data: () => ({
    alert: {
      error: false,
      message: ''
    },
    valid: 0,
    vs: {
      v1: 0,
      v2: 0
    },
    email: '',
    password: '',
    pw: true
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.signin },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    chackValid() {
      var root = this
      root.vs.v1 = 1
      root.vs.v2 = 1

      root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v1 = 0 } })
      root.pwRules.forEach((rule) => { if (rule(root.password) !== true) { root.vs.v2 = 0 } })
      root.valid = root.vs.v1 + root.vs.v2
    },
    submit() {
      var root = this
      this.$auth.login(root)
    },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight = sDiv.clientWidth - 20
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  created() {
    this.emRules = [
      v => !!v || '',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || this.form.email_validator_error
    ]

    this.pwRules = [
      v => !!v || ''
    ]
  },
  mounted() {
    window.addEventListener('resize', this.setSplashHeight)
    this.$nextTick(function() { this.setSplashHeight() })
  },
  updated() {
    this.chackValid()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  },

}
