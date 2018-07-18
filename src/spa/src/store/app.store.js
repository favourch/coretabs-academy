import Vue from 'vue'
import Vuex from 'vuex'
import i18n from '../i18n/ar/i18n'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    i18n: i18n,
    icon: '',
    direction: '',
    rev_direction: '',
    logo: '',
    forumLogo: '',
    maintenance: true,
    header: true,
    isLogin: false,
    user: {},
    progress: {
      width: 5,
      size: 80,
      error: null,
      text: ''
    },
    css: {
      workshops: {
        drawerWidth: ''
      }
    }
  },
  mutations: {
    header(state, payload) {
      state.header = payload
    },
    user(state, payload) {
      if (payload.prop === null) {
        state.user = payload.data

        if (payload.data === null) {
          state.isLogin = false
        } else {
          state.isLogin = true
        }
      } else {
        state.user[payload.prop] = payload.data
      }
    },
    profile(state, payload) {
      state.user.profile[payload.prop] = payload.data
    },
    progress(state, payload) {
      state.progress.error = payload.error
      if (payload.error === false) {
        state.progress.text = i18n.app.progress.loadingText
      } else {
        state.progress.text = i18n.app.progress.errorText
      }
    }
  },
  actions: {
    getImgUrl(state, img) {
      return require(`@/assets/multimedia/${img}`)
    },
    header: ({commit}, payload) => {
      return new Promise((resolve, reject) => {
        commit('header', payload)
        resolve(true)
      })
    },
    user: ({commit}, payload) => {
      return new Promise((resolve, reject) => {
        commit('user', payload)
        resolve(true)
      })
    },
    profile: ({commit}, payload) => {
      return new Promise((resolve, reject) => {
        commit('profile', payload)
        resolve(true)
      })
    },
    progress(context, payload) {
      context.commit('progress', payload)
    }
  },
  getters: {
    header: state => {
      return state.header
    },
    isLogin: state => {
      return state.isLogin
    },
    user: (state) => (prop) => {
      if (prop === null) {
        return state.user
      } else {
        return state.user[prop]
      }
    },
    profile: (state) => (prop) => {
      return state.user.profile[prop]
    }
  }
})
