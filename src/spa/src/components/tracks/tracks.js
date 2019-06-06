export default {
  name: 'TracksComponent',
  data() {
    return {
      backendImg: '',
      frontendImg: ''
    }
  },
  created() {
    this.$store.dispatch('getImgUrl', 'images/tracks/backend.png').then(img => {
      this.backendImg = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'images/tracks/frontend.png').then(img => {
      this.frontendImg = img
    }).catch(error => {
      throw new Error(error.message)
    })
  },
  methods: {
    toDetails(path) {
      this.$router.push(path)
    }
  },
  computed: {
    tracks() { return this.$store.state.i18n.tracks }
  }
}
