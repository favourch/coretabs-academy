export default {
  name: 'ChangePasswordComponent',
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    pw: true,
    old_password: '',
    new_password1: '',
    new_password2: '',
    waiting: false,
    valid: false,
    vs: {
      v1: false,
      v2: false,
      v3: false,
      v4: false
    }
  }),
  computed: {
    i18n() { return this.$store.state.i18n.profile.change_password },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    chackValid() {
      let root = this
      root.vs.v1 = true
      root.vs.v2 = true
      root.vs.v3 = true
      root.vs.v4 = true

      root.pwRules.forEach((rule) => { if (rule(root.old_password) !== true) { root.vs.v1 = false } })
      root.pwRules.forEach((rule) => { if (rule(root.new_password1) !== true) { root.vs.v2 = false } })
      root.pwRules.forEach((rule) => { if (rule(root.new_password2) !== true) { root.vs.v3 = false } })
      if (root.new_password1 !== root.new_password2) { root.vs.v4 = false }

      root.valid = root.vs.v1 && root.vs.v2 && root.vs.v3 && root.vs.v4
    },
    async submit() {
      if (this.valid) {
        let root = this
        root.waiting = true
        root.waiting = await this.$auth.changePassword(root)
      }
    }
  },
  created() {
    this.pwRules = [
      v => !!v || '',
      v => (v && v.length >= 8) || this.form.password_length_error
    ]
  },
  updated() {
    this.chackValid()
  }
}
