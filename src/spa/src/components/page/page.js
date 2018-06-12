export default {
  name: 'PageComponent',
  computed: {
    i18n() { return this.$store.state.i18n.page }
  }
}
