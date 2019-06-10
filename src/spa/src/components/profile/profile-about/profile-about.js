export default {
  name: 'ProfileAboutComponent',
  data() {
    return {
      profile: {},
      loaded: false
    }
  },
  computed: {
    bio() {
      if (this.profile && this.profile.bio === '') {
        return 'أنا شخص غامض قليلاً ولا يوجد شي لكي تعرفه عني الآن. ولكن ربما عندما تعود لاحقاَ سأكون قد أضفت نبذة عني';
      } else {
        return this.profile.bio;
      }
    },
    links() {
      if (this.profile) {
        return [
          {
            name: 'website',
            url: this.profile.website_link
          },
          {
            name: 'github',
            url: this.profile.github_link
          },
          {
            name: 'linkedin',
            url: this.profile.linkedin_link
          },
          {
            name: 'twitter',
            url: this.profile.twitter_link
          },
          {
            name: 'facebook',
            url: this.profile.facebook_link
          }
        ].filter(link => link.url)
      }
    },
  },
  async created() {
    await this.$parent.getProfileData()
    .then(profile => {
      this.loaded = true;
      this.profile = profile;
    });
  },
  watch: {
    $route() {
      this.$parent.getProfileData()
      .then(profile => {
        this.loaded = true
        this.profile = profile
      })
    }
  }
}
