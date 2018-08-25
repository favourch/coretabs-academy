export default {
  name: 'InnerHeaderComponent',
  props: ['title'],
  data: () => ({
    avatar_url: null,
    avatar_letter: null,
    menu: false,
    notifications: null,
    unread: null
  }),
  watch: {
    async $route() {
      var root = this
      this.unread = await this.$auth.get_notifications(root)
    },
    menu() {
      let lessonVideo = document.querySelector('.lesson-video')
      if (lessonVideo) {
        if (this.menu) {
          lessonVideo.classList.add('disabled')
        } else {
          lessonVideo.classList.remove('disabled')
        }
      }
    }
  },
  methods: {
    notification_icon(type) {
      switch (type) {
        case 1:
          return 'alternate_email'
        case 2:
          return 'reply'
        case 4:
          return 'edit'
        case 5:
          return 'favorite'
        case 6:
          return 'email'
        case 9:
          return 'reply'
        case 11:
          return 'link'
        default:
          return 'notifications'
      }
    },
    async set_unread() {
      this.unread = await this.$store.dispatch('unread', false)
    },
    mark_read(notification) {
      if (!notification.read) {
        notification.read = true
      }
    }
  },
  created() {
    this.avatar_url = this.$store.getters.user('avatar_url')
    if (this.avatar_url.slice(0, 4) !== 'http') {
      this.avatar_url = `${process.env.API_BASE_URL || ''}${this.$store.getters.user('avatar_url')}`
    } else {
      this.avatar_url = null
      this.avatar_letter = this.$store.getters.user('name')[0]
    }
  },
  async mounted() {
    var root = this
    this.unread = await this.$auth.get_notifications(root)
  }
}
