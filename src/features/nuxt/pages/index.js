export default {
  layout: 'index/index',
  asyncData(nuxt) {
    // called every time before loading the component
    let i18n = nuxt.app.store.state.i18n
    nuxt.app.store.state.progress.width = 5
    nuxt.app.store.state.progress.size = 80
    nuxt.app.store.state.direction = i18n.direction
    nuxt.app.store.state.css.workshops.drawerWidth = 350
    nuxt.app.store.state.rev_direction = i18n.rev_direction
    nuxt.app.store.state.progress.pageText = i18n.app.progress.pageText
    nuxt.app.store.state.progress.lessonText = i18n.app.progress.lessonText
    return {
      i18n: i18n.home,
      playerOptions: {
        autoplay: false,
        sources: [{
          type: 'video/mp4',
          src: 'https://www.w3schools.com/html/mov_bbb.mp4'
        }]
      }
    }
  },
  created() {},
  mounted() {
    window.addEventListener('resize', this.setIntroVideoHeight)
    this.$nextTick(function() {
      this.setIntroVideoHeight()
    })
    this.vPlayer.on('fullscreenchange', () => {
      this.exit(this.vPlayer)
    })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  },
  methods: {
    setIntroVideoHeight() {
      let vDiv = document.querySelector('#introductory-video')
      if (vDiv) {
        let vDivHeight = (vDiv.clientWidth * 75) / 100
        vDiv.setAttribute('style', 'height: ' + vDivHeight + 'px !important')
      }
    },
    play(vPlayer) {
      let player = document.getElementById('player')
      player.style.display = 'block'
      vPlayer.requestFullscreen()
      vPlayer.play()
    },
    pause(vPlayer) {
      vPlayer.pause()
    },
    ended(vPlayer) {
      vPlayer.exitFullscreen()
      let player = document.getElementById('player')
      player.style.display = 'none'
    },
    exit(vPlayer) {
      if (vPlayer.isFullscreen() === false) {
        this.pause(vPlayer)
        this.ended(vPlayer)
      }
    }
  }
}
