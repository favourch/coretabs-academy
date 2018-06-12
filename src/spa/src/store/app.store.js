import Vue from 'vue'
import Vuex from 'vuex'
import i18n from '../i18n/ar/i18n'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    i18n: i18n,
    icon: '',
    direction: '',
    logo: '',
    forumLogo: '',
    isLogin: false,
    githubFileURL: '',
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
    }
  },
  actions: {
    getImgUrl(state, img) {
      return require(`@/assets/multimedia/${img}`)
    }
  }
})
