import store from '../../store/app.store'

export default { 
  name: 'maintenanceComponent',
  methods: {
   setSplashHeight() {
     var sDiv = document.querySelector('#splash')
     if (sDiv) {
       var sDivHeight = sDiv.clientWidth - 20
       sDiv.setAttribute('style', 'height: ' + sDivHeight + 'px !important')
     }
   }
  },
  mounted() {
     window.addEventListener('resize', this.setSplashHeight)
     this.$nextTick(function() { this.setSplashHeight() })
     store.dispatch('header', false)
   },
   beforeDestroy() {
     window.removeEventListener('resize', this.onResize)
  },
  computed: {
   i18n() { return this.$store.state.i18n.maintenance }
 }
}
