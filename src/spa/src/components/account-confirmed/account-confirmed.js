export default {
  name: 'AccountConfirmedComponent',
  computed: {
    i18n() { return this.$store.state.i18n.auth.account_confirmed }
  },
  methods: {
    start() { },
    setSplashHeight() {
      let sDiv = document.querySelector('#splash')
      if (sDiv) {
        let sDivHeight
        if (sDiv.clientWidth < 250) { sDivHeight = sDiv.clientWidth * 1.25 } else { sDivHeight = sDiv.clientWidth / 1.25 }
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
