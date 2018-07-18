import Vue from 'vue'
import axios from 'axios'
import App from './app.vue'
import Vuetify from 'vuetify'
import router from './router'
import store from './store/app.store'
import Raven from 'raven-js'
import RavenVue from 'raven-js/plugins/vue'

Raven
    .config('https://5134f66568be4bb090819995c88110eb@sentry.io/1222814')
    .addPlugin(RavenVue, Vue)
    .install()

axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL
window.axios = axios

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

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
