export default {
  name: 'SelectTrackComponent',
  data: () => ({
    track1: 'backend',
    track2: 'frontend',
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
  }
}
