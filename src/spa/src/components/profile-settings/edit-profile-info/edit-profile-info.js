import VAutocomplete from './VAutocomplete/VAutocomplete'

export default {
  components: {
    VAutocomplete
  },
  name: 'EditProfileInfoComponent',
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    waiting: false,
    description: '',
    bio: '',
    username: '',
    userCountry: {},
    userSkills: [],
    github_link: '',
    linkedin_link: '',
    facebook_link: '',
    twitter_link: '',
    website_link: '',
    countries: [],
    skills: []
  }),
  computed: {
    i18n() { return this.$store.state.i18n.account.personal_info },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    async submit() {
      let root = this
      root.waiting = true
      root.waiting = await this.$auth.changeProfile(root)
    }
  },
  async created() {
    let root = this
    await axios.get('/api/v1/profile', {
      withCredentials: true
    }).then(async (response) => {
      await root.$auth.storeProfile(root.$store, response.data)
    }).catch()

    this.description = await this.$store.getters.profile('description')
    this.bio = await this.$store.getters.profile('bio')
    this.userCountry = await this.$store.getters.profile('country')
    this.userSkills = await this.$store.getters.profile('skills')
    this.github_link = await this.$store.getters.profile('github_link')
    this.linkedin_link = await this.$store.getters.profile('linkedin_link')
    this.facebook_link = await this.$store.getters.profile('facebook_link')
    this.twitter_link = await this.$store.getters.profile('twitter_link')
    this.website_link = await this.$store.getters.profile('website_link')
    this.countries = await this.$store.getters.countries
    this.skills = await this.$store.getters.skills
  },
  mounted() {
    window.addEventListener('resize', this.setAvatarsHeight)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
