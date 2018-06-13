export default {
  name: 'ForgotPasswordComponent',
  components: {},
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    valid: false,
    email: ''
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.forgot_password },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    submit() {
      var root = this
      this.$auth.requestReset(root)
    },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight
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
