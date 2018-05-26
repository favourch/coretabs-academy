export default {
  name: 'SelectTrackComponent',
  components: {},
  data: () => ({
    track_selected: '0'
  }),
  computed: {
    i18n() { return this.$store.state.i18n.select_track }
  },
  methods: {
    select(track) { this.track_selected = track },
    submit() { }
  }
}
