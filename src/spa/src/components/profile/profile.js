import InnerHeaderComponent from '../inner-header/inner-header.vue'
export default {
  name: 'ProfileComponent',
  components: {
    InnerHeaderComponent
  },
  data() {
    return {
      certificates: {},
      tabs: [
        { name: 'about', text: 'حول', path: 'about' },
        { name: 'certificates', text: 'الشهادات', path: 'certificates' }
      ]
    }
  },
  created() {
    this.$profiles.getProfile(`/api/v1/profile`)
    .then(profile => {
      document.title = `${profile.name} - ${document.title}`
      this.certificates = profile.certificates
    })
  }
}