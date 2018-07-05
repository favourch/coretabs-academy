export default {
  name: 'ResetPasswordComponent',
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    valid: false,
    password: '',
    pw: true
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.reset_password },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    submit() {
      var root = this
      this.$auth.resetConfirm(root)
    },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight
        if (sDiv.clientWidth < 250) { sDivHeight = sDiv.clientWidth / 1.25 } else { sDivHeight = sDiv.clientWidth / 2 }
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  created() {
    this.pwRules = [
      v => !!v || '',
      v => (v && v.length >= 8) || this.form.password_length_error
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
