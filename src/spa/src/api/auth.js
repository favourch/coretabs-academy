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
      root.$router.push({name: 'congratulations', params: { email: root.email }})
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
          root.$router.push({name: 'congratulations', params: { email: root.email }})
        }
      }
    })
  },
  async checkUser(store) {
    await axios.get('/api/v1/auth/user/').then(async() => {
      await this.storeUser(store)
    }).catch(async() => {
      await this.removeUser(store)
    })
  },
  logout(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    axios.post('/api/v1/auth/logout/').then((response) => {
      this.removeUser(root.$store)
      root.$router.push('/')
    })
  },
  selectTrack(root) {
    axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
    return axios.patch('/api/v1/auth/user/', {
      profile: {
        track: root.track_selected
      }
    }).then((response) => {
      root.$store.dispatch('profile', { prop: 'track', data: root.track_selected })
      this.updateUser(root.$store)
      return true
    })
  },
  storeUser(store, data = null) {
    store.dispatch('isLogin', true)
    if (data !== null) {
      window.localStorage.setItem('token', data.key)
      window.localStorage.setItem('user', JSON.stringify(data.user))
      return store.dispatch('user', { prop: null, data: data.user })
      .then((response) => {
        return response
      })
    } else {
      return store.dispatch('user', { prop: null, data: JSON.parse(window.localStorage.getItem('user')) })
      .then((response) => {
        return response
      })
    }
  },
  updateUser(store) {
    window.localStorage.setItem('user', JSON.stringify(store.getters.user(null)))
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
