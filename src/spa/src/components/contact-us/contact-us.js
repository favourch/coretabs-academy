export default {
  name: 'ContactUsComponent',
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    valid: 0,
    vs: {
      v1: 0,
      v2: 0,
      v3: 0
    },
    forums_icon: '',
    fullname: '',
    email: '',
    message: ''
  }),
  computed: {
    i18n() { return this.$store.state.i18n.contact },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    chackValid() {
      var root = this

      root.vs.v1 = 1
      root.vs.v2 = 1
      root.vs.v3 = 1

      root.fnRules.forEach((rule) => { if (rule(root.fullname) !== true) { root.vs.v1 = 0 } })
      root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v2 = 0 } })
      root.meRules.forEach((rule) => { if (rule(root.message) !== true) { root.vs.v3 = 0 } })

      root.valid = root.vs.v1 + root.vs.v2 + root.vs.v3
    },
    submit() {
      var root = this
      this.$auth.contact(root)
    }
  },
  created() {
    this.fullname = this.$store.getters.user('name') || ''
    this.email = this.$store.getters.user('email') || ''

    this.fnRules = [
      v => !!v || '',
      v => (v && v.length <= 20) || this.form.fullname_length_error
    ]
    this.emRules = [
      v => !!v || '',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || this.form.email_validator_error
    ]
    this.meRules = [
      v => !!v || '',
      v => (v && v.length >= 10) || this.form.message_length_error
    ]

    this.$store.dispatch('getImgUrl', 'icons/forums-logo.png').then(img => {
      this.forums_icon = img
    }).catch(error => {
        throw new Error(error.message)
    })
  },
  updated() {
    this.chackValid()
  }
}
