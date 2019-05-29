export default {
  name: 'SignUpComponent',
  data: () => ({
    alert: {
      error: false,
      message: ''
    },
    waiting: false,
    valid: false,
    vs: {
      v1: false,
      v2: false,
      v3: false,
      v4: false
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
      let root = this
      root.vs.v1 = true
      root.vs.v2 = true
      root.vs.v3 = true
      root.vs.v4 = true

      root.fnRules.forEach((rule) => { if (rule(root.fullname) !== true) { root.vs.v1 = false } })
      root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v2 = false } })
      root.unRules.forEach((rule) => { if (rule(root.username) !== true) { root.vs.v3 = false } })
      root.pwRules.forEach((rule) => { if (rule(root.password) !== true) { root.vs.v4 = false } })
      root.valid = root.vs.v1 && root.vs.v2 && root.vs.v3 && root.vs.v4
    },
    async submit() {
      if (this.valid) {
        let root = this
        root.waiting = true
        root.waiting = await this.$auth.registration(root)
      }
    },
    setAvatarsHeight() {
      let aDiv = document.querySelector('#avatars')
      if (aDiv) {
        let aDivHeight = aDiv.clientWidth
        aDiv.setAttribute('style', 'height: ' + aDivHeight + 'px !important')

        let vDiv = document.querySelector('#avatar')
        let vDivX = (aDiv.clientWidth / 7.5) * 2

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
      v => /^([\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z-.]+[ ]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z-_.]*)+$/.test(v.trim()) || this.form.fullname_format_error,
      v => (v && v.trim().length <= 20) || this.form.fullname_length_error
    ]

    this.emRules = [
      v => !!v || '',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v.trim()) || this.form.email_validator_error
    ]

    this.unRules = [
      v => !!v || '',
      v => (v && v.trim().length <= 20) || this.form.username_length_error,
      v => /^([A-Za-z0-9\-_.])+$/.test(v.trim()) || this.form.userName_format_error
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
