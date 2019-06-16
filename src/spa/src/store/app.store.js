import Vue from 'vue'
import Vuex from 'vuex'
import i18n from '../i18n/ar/i18n'
import { countries as importedCountries } from './countries'

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
    notificationsCounter: 0,
    user: {},
    profile: {},
    countries: importedCountries,
    skills: [
      { value: 'html', text: 'HTML' },
      { value: 'css', text: 'CSS' },
      { value: 'js', text: 'Javascript' },
      { value: 'jquery', text: 'jQuery' },
      { value: 'vuejs', text: 'VueJS' },
      { value: 'python', text: 'Python' },
      { value: 'flask', text: 'Flask' },
      { value: 'django', text: 'Django' }
    ],
    unread: null,
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
    account(state, payload) {
      state.user.account[payload.prop] = payload.data
    },
    profile(state, payload) {
      if (payload.prop === null) {
        state.profile = payload.data
      } else {
        state.profile[payload.prop] = payload.data
      }
    },
    unread(state, payload) {
      state.unread = payload
    },
    progress(state, payload) {
      state.progress.error = payload.error
      if (payload.error === false) {
        state.progress.text = i18n.app.progress.loadingText
      } else {
        state.progress.text = i18n.app.progress.errorText
      }
    },
    notificationsCounter(state, payload) {
      state.notificationsCounter = payload
    }
  },
  actions: {
    getImgUrl(state, img) {
      return require(`../assets/multimedia/${img}`)
    },
    header: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        commit('header', payload)
        resolve(true)
      })
    },
    user: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        commit('user', payload)
        resolve(true)
      })
    },
    account: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        commit('account', payload)
        resolve(true)
      })
    },
    profile: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        commit('profile', payload)
        resolve(true)
      })
    },
    unread: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        commit('unread', payload)
        resolve(payload)
      })
    },
    progress(context, payload) {
      context.commit('progress', payload)
    },
    notificationsCounter({ commit }, payload) {
      commit('notificationsCounter', payload)
    }
  },
  getters: {
    header: state => {
      return state.header
    },
    notificationsCounter: state => {
      return state.notificationsCounter
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
    account: (state) => (prop) => {
      return state.user.account[prop]
    },
    profile: (state) => (prop) => {
      if (prop === null) {
        return state.profile
      } else {
        return state.profile[prop]
      }
    },
    countries: state => {
      return state.countries
    },
    skills: state => {
      return state.skills
    },
    unread: state => {
      return state.unread
    }
  }
})
