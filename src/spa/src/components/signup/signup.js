export default {
  name: 'SignUpComponent',
  data: () => ({
    alert: {
      error: false,
      message: ''
    },
    valid: 0,
    vs: {
      v1: 0,
      v2: 0,
      v3: 0,
      v4: 0
    },
    fullname: '',
    email: '',
    username: '',
    password: '',
    pw: true
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.signup },
    form() { return this.$store.state.i18n.form }
  },
  watch: {
    fullname: function(val) {
      if (val[0] !== undefined) {
        document.querySelector('#avatar').setAttribute('data-before', val[0])
      } else { document.querySelector('#avatar').setAttribute('data-before', '') }
    }
  },
  methods: {
    chackValid() {
      var root = this
      root.vs.v1 = 1
      root.vs.v2 = 1
      root.vs.v3 = 1
      root.vs.v4 = 1

      root.fnRules.forEach((rule) => { if (rule(root.fullname) !== true) { root.vs.v1 = 0 } })
      root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v2 = 0 } })
      root.unRules.forEach((rule) => { if (rule(root.username) !== true) { root.vs.v3 = 0 } })
      root.pwRules.forEach((rule) => { if (rule(root.password) !== true) { root.vs.v4 = 0 } })
      root.valid = root.vs.v1 + root.vs.v2 + root.vs.v3 + root.vs.v4
    },
    submit() {
      var root = this
      this.$auth.registration(root)
    },
    setAvatarsHeight() {
      var aDiv = document.querySelector('#avatars')
      if (aDiv) {
        var aDivHeight = aDiv.clientWidth
        aDiv.setAttribute('style', 'height: ' + aDivHeight + 'px !important')

        var vDiv = document.querySelector('#avatar')
        var vDivX = (aDiv.clientWidth / 7.5) * 2

        vDiv.setAttribute('style', `
          height: ${vDivX}px !important;
          width: ${vDivX}px !important;
          max-width: ${vDivX}px !important;
          line-height: ${vDivX}px !important;
          font-size: ${vDivX / 2}px !important;
        `)
      }
    }
  },
  created() {
    this.fnRules = [
      v => !!v || '',
      v => (v && v.length <= 20) || this.form.fullname_length_error
    ]

    this.emRules = [
      v => !!v || '',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || this.form.email_validator_error
    ]

    this.unRules = [
      v => !!v || '',
      v => (v && v.length <= 20) || this.form.username_length_error
    ]

    this.pwRules = [
      v => !!v || '',
      v => (v && v.length >= 8) || this.form.password_length_error
    ]
  },
  mounted() {
    window.addEventListener('resize', this.setAvatarsHeight)
    this.$nextTick(function() { this.setAvatarsHeight() })
  },
  updated() {
    this.chackValid()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
