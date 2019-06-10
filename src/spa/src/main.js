import 'babel-polyfill'
import Vue from 'vue'
import axios from 'axios'
import App from './app.vue'
import Vuetify from 'vuetify'
import { createRouter } from './router'
import store from './store/app.store'

axios.defaults.baseURL = process.env.API_BASE_URL
if (typeof window !== 'undefined') { window.axios = axios }

Vue.use(require('./api/api').default)
Vue.use(Vuetify, {
  theme: {
    primary: '#4445e7',
    secondary: '#e0e0e0',
    accent: '#ff4081',
    error: '#f44336',
    warning: '#ffeb3b',
    info: '#2196f3',
    success: '#4caf50'
  }
})

Vue.config.productionTip = false
Vue.config.delimiters = ['[[', ']]']

export function createApp() {
  const router = createRouter()
  const app = new Vue({
    router,
    store,
    render: h => h(App)
  })

  return { app, router }
}
