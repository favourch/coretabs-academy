import { videoPlayer } from 'vue-video-player'
import '../../../node_modules/video.js/dist/video-js.css'

export default {
  name: 'HomeComponent',
  components: {
    videoPlayer
  },
  data: () => ({
    playerOptions: {
      autoplay: false,
      sources: [{
        type: 'video/mp4',
        src: 'https://www.w3schools.com/html/mov_bbb.mp4'
      }]
    }
  }),
  computed: {
    i18n() { return this.$store.state.i18n.home },
    vPlayer() { return this.$refs.videoPlayer.player }
  },
  methods: {
    setIntroVideoHeight() {
      var vDiv = document.querySelector('#introductory-video')
      if (vDiv) {
        var vDivHeight = (vDiv.clientWidth * 75) / 100
        vDiv.setAttribute('style', 'height: ' + vDivHeight + 'px !important')
      }
    },
    play(vPlayer) {
      var player = document.getElementById('player')
      player.style.display = 'block'
      vPlayer.requestFullscreen()
      vPlayer.play()
    },
    pause(vPlayer) {
      vPlayer.pause()
    },
    ended(vPlayer) {
      vPlayer.exitFullscreen()
      var player = document.getElementById('player')
      player.style.display = 'none'
    },
    exit(vPlayer) {
      if (vPlayer.isFullscreen() === false) {
        this.pause(vPlayer)
        this.ended(vPlayer)
      }
    }
  },
  mounted() {
    window.addEventListener('resize', this.setIntroVideoHeight)
    this.$nextTick(function() { this.setIntroVideoHeight() })
    this.vPlayer.on('fullscreenchange', () => { this.exit(this.vPlayer) })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
