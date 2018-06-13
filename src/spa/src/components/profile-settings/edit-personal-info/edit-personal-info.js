export default {
  name: 'EditPersonalInfoComponent',
  data: () => ({
    reader: null,
    avatar_url: '',
    validImage: {
      valid: 1,
      imageData: ''
    },
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
    fullname: '',
    email: '',
    username: ''
  }),
  computed: {
    i18n() { return this.$store.state.i18n.profile.personal_info },
    form() { return this.$store.state.i18n.form }
  },
  watch: {
    'validImage.valid': function() {
      this.chackValid()
    }
  },
  methods: {
    previewImage(event) {
      let input = event.target
      this.reader = new FileReader()
      if (input.files && input.files[0]) {
        const img = new Image()
        img.src = window.URL.createObjectURL(input.files[0])
        img.onload = () => {
          window.URL.revokeObjectURL(img.src)

          this.validImage.valid = 1
          this.validImage.imageData = input.files[0]
          this.reader.onload = (e) => {
            this.avatar_url = e.target.result
          }
          this.reader.readAsDataURL(input.files[0])
        }
      }
    },
    chackValid() {
      var root = this
      root.vs.v1 = 1
      root.vs.v2 = 1
      root.vs.v3 = 1

      root.fnRules.forEach((rule) => { if (rule(root.fullname) !== true) { root.vs.v1 = 0 } })
      root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v2 = 0 } })
      root.unRules.forEach((rule) => { if (rule(root.username) !== true) { root.vs.v3 = 0 } })

      root.valid = root.vs.v1 + root.vs.v2 + root.vs.v3 + root.validImage.valid
    },
    submit() {
      var root = this
      this.$auth.changeInfo(root)
    }
  },
  created() {
    this.fullname = this.$store.getters.user('name')
    this.email = this.$store.getters.user('email')
    this.username = this.$store.getters.user('username')
    this.avatar_url = this.$store.getters.user('avatar_url')

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
  },
  mounted() {
    window.addEventListener('resize', this.setAvatarsHeight)
  },
  updated() {
    this.chackValid()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
