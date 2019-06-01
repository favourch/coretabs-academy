export default {
  name: 'JoinInviteComponent',
  data: () => ({
    isClosed: false
  }),
  computed: {
    i18n() { return this.$store.state.i18n.join_invite }
  },
  methods: {
    closeBanner() {
      this.isClosed = true;
    }
  }
}
