export default {
  name: 'CongratulationsComponent',
  data: () => ({
    counter: 30
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.congratulations }
  },
  methods: {
    submit() { },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight = sDiv.clientWidth / 2
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  mounted() {
    setInterval(() => {
      if (this.counter > 0) {
        this.counter -= 1
      }
    }, 1000)

    window.addEventListener('resize', this.setSplashHeight)
    this.$nextTick(function() { this.setSplashHeight() })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
