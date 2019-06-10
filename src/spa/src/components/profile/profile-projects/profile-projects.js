export default {
  name: 'profile-projects',
  data() {
    return {
      loaded: false,
      projects: null
    }
  },
  created() {
    this.$parent.getProfileData()
    .then(profile => {
      this.loaded = true
      this.projects = profile.projects;
      document.title = `${profile.name} - ${document.title}`
    })
  },
  watch: {
    $route() {
      this.$parent.getProfileData()
      .then(profile => {
        this.loaded = true
        this.projects = profile.projects
      })
    }
  }
}
