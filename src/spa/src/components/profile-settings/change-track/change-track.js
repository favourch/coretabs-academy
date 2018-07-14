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
      root.alert.success = false
      root.alert.error = false
      root.waiting = true

      if (await this.$auth.selectTrack(root)) {
        root.alert.success = true
        root.alert.message = root.i18n.success_message
        root.waiting = false
      } else {
        root.alert.error = true
        root.alert.message = root.i18n.error_message
        root.waiting = false
      }
    }
  },
  mounted() {
    this.getTracks()
  }
}
