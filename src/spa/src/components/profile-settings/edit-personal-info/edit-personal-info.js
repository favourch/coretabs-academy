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
    waiting: false,
    valid: false,
    vs: {
      v1: false,
      // v2: false,
      v3: false
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
          this.validImage.valid = true
          this.validImage.imageData = input.files[0]
          this.reader.onload = (e) => {
            this.avatar_url = e.target.result
          }
          this.reader.readAsDataURL(input.files[0])
        }
      }
    },
    chackValid() {
      let root = this
      root.vs.v1 = true
      // root.vs.v2 = true
      root.vs.v3 = true
      root.fnRules.forEach((rule) => { if (rule(root.fullname) !== true) { root.vs.v1 = false } })
      // root.emRules.forEach((rule) => { if (rule(root.email) !== true) { root.vs.v2 = false } })
      root.unRules.forEach((rule) => { if (rule(root.username) !== true) { root.vs.v3 = false } })
      root.valid = root.vs.v1 && root.vs.v3 && root.validImage.valid
    },
    async submit() {
      if (this.valid) {
        let root = this
        root.waiting = true
        root.waiting = await this.$auth.changeInfo(root)
     }
    }
  },
  created() {
    this.fullname = this.$store.getters.user('name')
    this.email = this.$store.getters.user('email')
    this.username = this.$store.getters.user('username')
    this.avatar_url = this.$store.getters.user('avatar_url')
    if (this.avatar_url.slice(0, 4) !== 'http') {
      this.avatar_url = `${process.env.API_BASE_URL || ''}${this.$store.getters.user('avatar_url')}`
    } else {
      if (this.avatar_url.search(/coretabs-academy-media/) === -1) {
        this.avatar_url = null
      }
    }

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
