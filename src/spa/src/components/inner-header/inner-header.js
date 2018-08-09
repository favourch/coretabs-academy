export default {
  name: 'InnerHeaderComponent',
  props: ['title'],
  data: () => ({
    avatar_url: null,
    avatar_letter: null,
    menu: false,
    notifications: null,
    unread: false
  }),
  watch: {
    $route() {
      var root = this
      this.$auth.get_notifications(root)
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
  mounted() {
    var root = this
    this.$auth.get_notifications(root)
  }
}
