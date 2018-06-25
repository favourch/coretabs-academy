export default {
  data: () => ({
    loading: false
  }),
  methods: {
    start() {
      this.loading = true
    },
    finish() {
      this.loading = false
    },
    fail() {
      this.$store.state.progress.classList = 'progress-error'
      this.$store.state.progress.pageText = this.$store.state.i18n.app.progress.pageTextError
    }
  }
}
