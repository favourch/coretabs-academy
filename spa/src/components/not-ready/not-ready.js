export default {
  name: 'NotReadyComponent',
  computed: {
    i18n() { return this.$store.state.i18n.not_ready }
  }
}
