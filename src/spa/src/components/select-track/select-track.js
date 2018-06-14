export default {
  name: 'SelectTrackComponent',
  data: () => ({
    track_selected: null
  }),
  computed: {
    i18n() { return this.$store.state.i18n.select_track }
  },
  methods: {
    select(track) { this.track_selected = track },
    async submit() {
      var root = this
      if (await this.$auth.selectTrack(root)) {
        this.$router.push('/')
      }
    }
  },
  created() {
    this.track_selected = (this.$store.getters.profile('track')) ? this.$store.getters.profile('track') : null
  }
}
