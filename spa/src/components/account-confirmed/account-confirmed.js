export default {
  name: 'AccountConfirmedComponent',
  computed: {
    i18n() { return this.$store.state.i18n.auth.account_confirmed }
  },
  methods: {
    start() { },
    dismiss() { },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight = sDiv.clientWidth / 2
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  mounted() {
    window.addEventListener('resize', this.setSplashHeight)
    this.$nextTick(function() { this.setSplashHeight() })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
