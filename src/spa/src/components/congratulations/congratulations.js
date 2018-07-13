export default {
  name: 'CongratulationsComponent',
  props: ['email'],
  data: () => ({
    alert: {
      success: false,
      error: false,
      message: ''
    },
    waiting: false,
    counter: 30
  }),
  computed: {
    i18n() { return this.$store.state.i18n.auth.congratulations }
  },
  methods: {
    async submit() {
      let root = this
      root.waiting = true
      root.waiting = await this.$auth.confirmation(root)
      setInterval(() => {
        if (this.counter > 0) {
          this.counter -= 1
        }
      }, 1000)
    },
    setSplashHeight() {
      let sDiv = document.querySelector('#splash')
      if (sDiv) {
        let sDivHeight
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
