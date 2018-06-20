import notifications from './notifications.json'
export default {
  name: 'InnerHeaderComponent',
  props: ['title'],
  data: () => ({
    menu: false,
    notifications: null
  }),
  methods: {
    notification_icon(type) {
      switch (type) {
        // case 1:
          // return 'alternate_email'
        case 2:
          return 'reply'
        case 4:
          return 'edit'
        case 5:
          return 'favorite'
        case 9:
          return 'reply'
        case 11:
          return 'link'
        default:
          return 'notifications'
      }
    }
  },
  created() {
    let selector = '.settings > .inner-header > .toolbar'
    if (document.querySelector(selector) !== null) {
      this.y = document.querySelector(selector).clientHeight
    } else {
      let self = this
      this.timeout = setTimeout(() => {
        self.y = document.querySelector(selector).clientHeight
      }, 100)
    }

    this.notifications = notifications
  },
  mounted() {
    // var root = this
    // this.$auth.get_notifications(root)
  }
}
