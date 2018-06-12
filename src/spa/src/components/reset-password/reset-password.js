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
    i18n() { return this.$store.state.i18n.auth.forgot_password },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    submit() { },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight = sDiv.clientWidth / 2
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  created() {
    this.pwRules = [
      v => !!v || '',
      v => (v && v.length >= 10) || this.form.password_length_error
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
