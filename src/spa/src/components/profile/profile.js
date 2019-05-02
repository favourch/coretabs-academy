import InnerHeaderComponent from '../inner-header/inner-header.vue'
export default {
  name: 'ProfileComponent',
  components: {
    InnerHeaderComponent
  },
  data() {
    return {
      loaded: false,
      profile: {},
      avatar_url: null,
      avatar_letter: null,
      tabs: [
        { name: 'profile-about', text: 'حول' },
        { name: 'profile-certificates', text: 'الشهادات' }
      ]
    }
  },
  methods: {
    getProfileData() {
      return this.$route.params.username === this.$store.getters.user('username') ? 
      this.$profiles.getProfile(`/api/v1/profile`) 
      :
      this.$profiles.getProfile(`/api/v1/profiles/${this.$route.params.username}`)
    }
  },
  created() {
    console.log(this.$route.params.username)
    this.getProfileData()
    .then(profile => {
      this.loaded = true;
      document.title = `${profile.name} - ${document.title}`
      this.profile = profile; 

      this.avatar_url = profile.avatar_url
      if (this.avatar_url.slice(0, 4) !== 'http') {
        this.avatar_url = `${process.env.API_BASE_URL || ''}${profile.avatar_url}`
      } else {
        if (this.avatar_url.search(/coretabs-academy-media/) === -1) {
          this.avatar_url = null
          this.avatar_letter = profile.name[0]
        }
      }
    });
  }
}