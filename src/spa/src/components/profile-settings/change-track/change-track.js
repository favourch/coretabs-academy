export default {
  name: 'ChangeTrackComponent',
  data: () => ({
    alert: {
      success: false,
      message: ''
    },
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
      var root = this
      if (await this.$auth.selectTrack(root)) {
        this.alert.success = true
        this.alert.message = this.i18n.success_message
      }
    }
  },
  mounted() {
    this.getTracks()
  }
}
