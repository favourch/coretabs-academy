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
    isLogin: false,
    githubFileURL: '',
    user: {},
    progress: {
      size: 0,
      width: 0,
      pageText: '',
      lessonText: ''
    },
    css: {
      workshops: {
        drawerWidth: ''
      }
    }
  },
  mutations: {
    getGithubFileURL(state, params) {
      params.owner = params.owner === undefined ? 'coretabs-academy' : params.owner
      state.githubFileURL = `https://raw.githubusercontent.com/${params.owner}/${params.repo}/master/${params.path}`
    },
    isLogin(state, boolean) {
      state.isLogin = boolean
    },
    user(state, payload) {
      if (payload.prop === null) {
        state.user = payload.data
      } else {
        state.user[payload.prop] = payload.data
      }
    },
    profile(state, payload) {
      state.user.profile[payload.prop] = payload.data
    }
  },
  actions: {
    getImgUrl(state, img) {
      return require(`@/assets/multimedia/${img}`)
    },
    isLogin(context, boolean) {
      context.commit('isLogin', boolean)
    },
    user: ({commit}, payload) => {
      return new Promise((resolve, reject) => {
        commit('user', payload)
        resolve(true)
      })
    },
    profile(context, payload) {
      context.commit('profile', payload)
    }
  },
  getters: {
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
