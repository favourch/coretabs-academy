export default {
  name: 'CongratulationsComponent',
  props: ['email'],
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    counter: 30
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.congratulations }
  },
  methods: {
    submit() {
      var root = this
      this.$auth.confirmation(root)
    },
    setSplashHeight() {
      var sDiv = document.querySelector('#splash')
      if (sDiv) {
        var sDivHeight
        if (sDiv.clientWidth < 250) { sDivHeight = sDiv.clientWidth * 1.25 } else { sDivHeight = sDiv.clientWidth / 1.5 }
        sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
      }
    }
  },
  mounted() {
    if (!this.email) { this.$router.push('/') }
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
