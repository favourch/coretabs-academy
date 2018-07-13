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
    valid: 0,
    vs: {
      v1: 0,
      v2: 0,
      v3: 0,
      v4: 0
    }
  }),
  computed: {
    i18n() { return this.$store.state.i18n.profile.change_password },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    chackValid() {
      let root = this
      root.vs.v1 = 1
      root.vs.v2 = 1
      root.vs.v3 = 1
      root.vs.v4 = 1

      root.pwRules.forEach((rule) => { if (rule(root.old_password) !== true) { root.vs.v1 = 0 } })
      root.pwRules.forEach((rule) => { if (rule(root.new_password1) !== true) { root.vs.v2 = 0 } })
      root.pwRules.forEach((rule) => { if (rule(root.new_password2) !== true) { root.vs.v3 = 0 } })
      if (root.new_password1 !== root.new_password2) { root.vs.v4 = 0 }

      root.valid = root.vs.v1 + root.vs.v2 + root.vs.v3 + root.vs.v4
    },
    async submit() {
      let root = this
      root.waiting = true
      root.waiting = await this.$auth.changePassword(root)
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
