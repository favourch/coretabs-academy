import Vue from 'vue'
import VueYoutube from 'vue-youtube'
Vue.use(VueYoutube)

export default {
  name: 'HomeComponent',
  data() {
    return {
      videoId: '1wgiLnGl0JU',
      playerVars: {
        showinfo: 0,
        rel: 0
      }
    }
  },
  methods: {
    setIntroVideoHeight() {
      var vDiv = document.querySelector('#introductory-video')
      if (vDiv) {
        var vDivHeight = (vDiv.clientWidth * 75) / 100
        vDiv.setAttribute('style', 'height: ' + vDivHeight + 'px !important')
      }
    },
    play() {
      let modal = document.querySelector('.video-modal')
      modal.classList.add('open')
      modal.classList.remove('close')
      this.$refs.youtube.player.playVideo()
    },
    closeModal() {
      let modal = document.querySelector('.video-modal')
      modal.classList.add('close')
      modal.classList.remove('open')
      this.$refs.youtube.player.pauseVideo()       
    }
  },
  computed: {
    i18n() { return this.$store.state.i18n.home }
  },
  created() {
    if (this.$store.getters.isLogin) {
      if (this.$store.getters.account('track')) {
        this.$router.push(`/classroom/${this.$store.getters.account('track')}/`)
      } else if(!this.$store.getters.user('batch_status')) {
        this.$router.push('/batch-not-started')
      } else {
        this.$router.push('/select-track')
      }
    }
  },
  mounted() {
    window.addEventListener('resize', this.setIntroVideoHeight)
    this.$nextTick(function() { this.setIntroVideoHeight() })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
