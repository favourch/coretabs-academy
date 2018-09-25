/* eslint-disable */
import Vue from 'vue'
import Cookies from 'js-cookie'

const AuthAPI = {
  async registration(root) {
    root.alert.error = false
    return await axios.post('/api/v1/auth/registration/', {
      username: root.username,
      name: root.fullname,
      password1: root.password,
      password2: root.password,
      email: root.email
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      root.$router.push({ name: 'congratulations', params: { email: root.email } })
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  async confirmation(root) {
    root.alert.success = false
    root.alert.error = false
    return await axios.post('/api/v1/auth/confirmation/', {
      email: root.email
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.success_message_text
      root.counter = 60
      return false
    }).catch(() => {
      root.alert.error = true
      root.alert.message = root.i18n.error_message_text
      root.counter = 60
      return false
    })
  },
  verifyEmail(root) {
    axios.post('/api/v1/auth/registration/verify-email/', {
      key: root.$route.params.key
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then(() => {
      root.$router.push('/application-submitted')
    }).catch(() => {
      root.$router.push('/404')
    })
  },
  async requestReset(root) {
    root.alert.success = false
    root.alert.error = false
    return await axios.post('/api/v1/auth/password/reset/', {
      email: root.email
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.success_message_text
      return false
    }).catch(() => {
      root.alert.error = true
      if (error.response.status === 400) {
        root.alert.message = error.response.data.email
      } else {
        root.alert.message = root.i18n.error_message_text
      }
      return false
    })
  },
  async resetConfirm(root) {
    root.alert.success = false
    root.alert.error = false
    return await axios.post('/api/v1/auth/password/reset/confirm/', {
      new_password1: root.password,
      new_password2: root.password,
      uid: root.$route.params.uid,
      key: root.$route.params.key
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.success_message_text
      setTimeout(() => {
        root.$router.push('/signin')
      }, 3000)
    }).catch(() => {
      root.alert.error = true
      root.alert.message = root.i18n.error_message_text
      return false
    })
  },
  async login(root) {
    root.alert.error = false
    return await axios.post('/api/v1/auth/login/', {
      email: root.email,
      password: root.password
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      this.storeUser(root.$store, response.data)
      if (root.$route.query.next) {
        window.location = root.$route.query.next
      } else {
        if (root.$store.getters.profile('track')) {
          root.$router.push(`/classroom/${root.$store.getters.profile('track')}/`)
        } else {
          root.$router.push('/select-track')
        }
      }
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        }
        else if (error.response.status === 403) {
          if (error.response.data.detail === 'not verified') {
            root.$router.push({
              name: 'congratulations',
              params: {
                email: root.email
              }
            })
          } else {
            root.alert.message = root.form.message_endpoint_error
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  async get_notifications(root) {
    return await axios.get(`/api/v1/auth/user/notifications/`,
      { withCredentials: true })
      .then(async (response) => {
        let unread = root.$store.getters.unread
        let notifications = response.data.notifications.slice(0, 5)
        notifications.forEach(async (notification) => {
          if (!notification.read) {
            await root.$store.dispatch('unread', true)
          }
        })

        if(unread === false || notifications[0].id === response.data.seen_notification_id) {
          await root.$store.dispatch('unread', false)
        }

        root.notifications = notifications
        return root.$store.getters.unread
      })
  },
  async checkUser(store) {
    await store.dispatch('header', false)
    return await axios.get('/api/v1/auth/user/', {
      withCredentials: true
    }).then(async (response) => {
      await store.dispatch('header', true)
      await this.storeUser(store, response.data)
    }).catch(async () => {
      await store.dispatch('header', true)
      await this.removeUser(store)
    })
  },
  async changeInfo(root) {
    root.alert.success = false
    root.alert.error = false
    let formData = new FormData()
    formData.append('name', root.fullname)
    formData.append('username', root.username)
    formData.append('avatar', root.validImage.imageData)

    return await axios.patch('/api/v1/auth/user/', formData, {
      withCredentials: true,
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        'Content-Type': 'multipart/form-data'
      }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.success_message
      root.$store.dispatch('user', { prop: 'name', data: root.fullname })
      root.$store.dispatch('user', { prop: 'username', data: root.username })
      if (root.$store.getters.user('avatar_url') !== root.avatar_url) {
        root.$store.dispatch('user', { prop: 'avatar_url', data: '/media/avatars/' + root.username + '/resized/80/' + root.validImage.imageData.name })
      }
      return false
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  getTracks() {
    return axios.get('/api/v1/tracks/').then((response) => {
      return response.data
    })
  },
  async selectTrack(root) {
    return await axios.patch('/api/v1/auth/user/', {
      profile: {
        track: root.track_selected
      }
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      return root.$store.dispatch('profile', { prop: 'track', data: response.data.profile.track })
        .then((response) => {
          return response
        })
    }).catch(() => {
      return false
    })
  },
  async changePassword(root) {
    root.alert.success = false
    root.alert.error = false
    return await axios.post('/api/v1/auth/password/change/', {
      old_password: root.old_password,
      new_password1: root.new_password1,
      new_password2: root.new_password2
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = response.data.detail
      return false
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  logout(root) {
    axios.post('/api/v1/auth/logout/', {}, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      this.removeUser(root.$store)
      root.$router.push('/')
    })
  },
  async contact(root) {
    root.alert.success = false
    root.alert.error = false
    return await axios.post('/api/v1/contact/', {
      name: root.fullname,
      email: root.email,
      body: root.message
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = response.data.detail
      return false
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  storeUser(store, data) {
    if (data !== null) {
      if (data.key) {
        window.localStorage.setItem('token', data.key)
        return store.dispatch('user', { prop: null, data: data.user })
          .then((response) => {
            return response
          })
      } else {
        return store.dispatch('user', { prop: null, data: data })
          .then((response) => {
            return response
          })
      }
    }
  },
  removeUser(store) {
    window.localStorage.removeItem('token')
    return store.dispatch('user', { prop: null, data: null })
      .then((response) => {
        return response
      })
  },
  showLesson(endpoint, store) {
    return axios.put(endpoint, {
      is_shown: true
    }, {
      withCredentials: true,
      headers: { 'X-CSRFToken': Cookies.get('csrftoken') }
    }).then(async () => {
      if (await this.checkUser(store)) {
        return true
      }
    })
  }
}

export default AuthAPI
