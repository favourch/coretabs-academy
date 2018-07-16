export default {
  name: 'ForgotPasswordComponent',
  components: {},
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    waiting: false,
    valid: false,
    email: ''
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.forgot_password },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    async submit() {
      if (this.valid) {
        let root = this
        root.waiting = true
        root.waiting = await this.$auth.requestReset(root)
      }
    },
    setSplashHeight() {
      let sDiv = document.querySelector('#splash')
      if (sDiv) {
        let sDivHeight
        if (sDiv.clientWidth < 250) { sDivHeight = sDiv.clientWidth } else { sDivHeight = sDiv.clientWidth / 1.5 }
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  created() {
    this.emRules = [
      v => !!v || '',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || this.form.email_validator_error
    ]
  },
  mounted() {
    window.addEventListener('resize', this.setSplashHeight)
    this.$nextTick(function() { this.setSplashHeight() })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
