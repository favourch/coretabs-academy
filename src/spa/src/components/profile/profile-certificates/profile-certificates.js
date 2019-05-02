export default {
  name: 'ProfileCertificatesComponent',
  data() {
    return {
      loaded: false,
      certificates: null
    }
  },
  created() {
    this.$parent.getProfileData()
    .then(profile => {
      this.loaded = true;
      this.certificates = profile.certificates;
      document.title = `${profile.name} - ${document.title}`
    })
  },
  watch: {
    $route() {
      this.$parent.getProfileData()
      .then(profile => {
        this.loaded = true;
        this.certificates = profile.certificates;
      });
    }
  }
}
