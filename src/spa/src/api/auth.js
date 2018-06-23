/* eslint-disable */
import Vue from 'vue'
import Cookies from 'js-cookie'

const AuthAPI = {
  registration(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/registration/', {
      username: root.username,
      name: root.fullname,
      password1: root.password,
      password2: root.password,
      email: root.email
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
        }
        if (error.response.status === 500) {
          root.alert.message = 'Oops! Please Try again later!'
        }
      }
    })
  },
  confirmation(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/confirmation/', {
      email: root.email
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.success_message_text
    }).catch(() => {
      root.alert.error = true
      root.alert.message = root.i18n.error_message_text
    })
  },
  verifyEmail(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/registration/verify-email/', {
      key: root.$route.params.key
    }).then((response) => {
      this.storeUser(root.$store, response.data)
      root.$router.push('/account-confirmed')
    }).catch((error) => {
      if (error.response) {
        if (error.response.status === 404) {
          root.$router.push('/404')
        }
      }
    })
  },
  requestReset(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/password/reset/', {
      email: root.email
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.success_message_text
    }).catch(() => {
      root.alert.error = true
      root.alert.message = root.i18n.error_message_text
    })
  },
  resetConfirm(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/password/reset/confirm/', {
      new_password1: root.password,
      new_password2: root.password,
      uid: root.$route.params.uid,
      key: root.$route.params.key
    }).then((response) => {
      root.$router.push('/signin')
    })
  },
  login(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/login/', {
      email: root.email,
      password: root.password
    }).then((response) => {
      this.storeUser(root.$store, response.data)
      if (root.$route.query.next) {
        root.$router.push(root.$route.query.next)
      } else {
        root.$router.push('/')
      }
    }).catch((error) => {
      if (error.response) {
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.error = true
            root.alert.message = error.response.data[err][0]
            break
          }
        }
        if (error.response.status === 403) {
          root.$router.push({
            name: 'congratulations',
            params: {
                email: root.email
            }
          })
        }
      }
    })
  },
  get_notifications(root) {
    axios.get('https://forums.coretabs.net/notifications.json?api_key=e0545b44febdf89e6cc92e16b34a4e8fb63d72587487ff12b799ab792c8da252&api_username=' + root.$store.getters.user('username'))
    .then((response) => {
      for (var notification in response.data.notifications.slice(0, 5)) {
        if (!notification.read) {
          root.unread = true
          break
        }
      }
      root.notifications = response.data
    })
  },
  async checkUser(store) {
    await axios.get('/api/v1/auth/user/').then(async () => {
      await this.storeUser(store)
    }).catch(async () => {
      await this.removeUser(store)
    })    
  },
  changeInfo(root) {
    let formData = new FormData()
    formData.append('name', root.fullname)
    formData.append('email', root.email)
    formData.append('username', root.username)
    formData.append('avatar', root.validImage.imageData)

    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.patch('/api/v1/auth/user/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }).then((response) => {
      root.alert.success = true
      if (root.$store.getters.user('email') === root.email) {
        root.alert.message = root.i18n.success_message
        root.$store.dispatch('user', { prop: 'name', data: root.fullname })
        root.$store.dispatch('user', { prop: 'username', data: root.username })
        if (root.$store.getters.user('avatar_url') !== root.avatar_url) {
          root.$store.dispatch('user', { prop: 'avatar_url', data: '/media/avatars/' + root.username + '/resized/80/' + root.validImage.imageData.name })
        }
        this.updateUser(root.$store)
      } else {
        root.alert.message = root.i18n.logout_message
        setTimeout(() => {
          this.logout(root)
        }, 3000)
      }
    }).catch((error) => {
      if (error.response) {
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.error = true
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          console.log(error.response.status + ': ' + error.response.data)
        }
      }
    })
  },
  logout(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/logout/').then((response) => {
      this.removeUser(root.$store)
      root.$router.push('/')
    })
  },
  getTracks() {
    return axios.get('/api/v1/tracks/').then((response) => {
      return response.data
    })
  },
  selectTrack(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    return axios.patch('/api/v1/auth/user/', {
      profile: {
        track: root.track_selected
      }
    }).then((response) => {
      root.$store.dispatch('profile', { prop: 'track', data: response.data.profile.track })
      root.$store.dispatch('profile', { prop: 'track_slug', data: response.data.profile.track_slug })
      this.updateUser(root.$store)
      return true
    })
  },
  changePassword(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/password/change/', {
      old_password: root.old_password,
      new_password1: root.new_password1,
      new_password2: root.new_password2
    }).then((response) => {
      root.alert.success = true
      root.alert.message = response.data
    }).catch((error) => {
      if (error.response) {
        for (var err in error.response.data) {
          root.alert.error = true
          root.alert.message = error.response.data[err][0]
          break
        }
      }
    })
  },
  contact(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/contact/', {
      name: root.fullname,
      email: root.email,
      body: root.message
    }).then((response) => {
      root.alert.success = true
      root.alert.message = response.data.detail
    }).catch((error) => {
      if (error.response) {
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.error = true
            root.alert.message = error.response.data[err][0]
            break
          }
        }
      }
    })
  },
  storeUser(store, data = null) {
    store.dispatch('isLogin', true)
    if (data !== null) {
      window.localStorage.setItem('token', Vue.prototype.$encryption.b64EncodeUnicode(data.key))
      window.localStorage.setItem('user', Vue.prototype.$encryption.b64EncodeUnicode(JSON.stringify(data.user)))
      return store.dispatch('user', { prop: null, data: data.user })
      .then((response) => {
        return response
      })
    } else {
      return store.dispatch('user', { prop: null, data: JSON.parse(Vue.prototype.$encryption.b64DecodeUnicode(window.localStorage.getItem('user'))) })
      .then((response) => {
        return response
      })
    }
  },
  updateUser(store) {
    window.localStorage.setItem('user', Vue.prototype.$encryption.b64EncodeUnicode(JSON.stringify(store.getters.user(null))))
  },
  removeUser(store) {
    window.localStorage.removeItem('token')
    window.localStorage.removeItem('user')
    store.dispatch('isLogin', false)
    return store.dispatch('user', { prop: null, data: 'empty' })
    .then((response) => {
      return response
    })
  }
}

export default AuthAPI
