export default {
  name: 'ChangeTrackComponent',
  data: () => ({
    alert: {
      success: false,
      message: ''
    },
    waiting: false,
    track_selected: null,
    tracks: []
  }),
  computed: {
    i18n() { return this.$store.state.i18n.profile.change_track }
  },
  methods: {
    async getTracks() {
      this.track_selected = this.$store.getters.profile('track')
      this.tracks = await this.$auth.getTracks()
    },
    async submit() {
      let root = this
      root.waiting = true
      root.waiting = await this.$auth.selectTrack(root)
    }
  },
  mounted() {
    this.getTracks()
  }
}
