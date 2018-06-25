/* eslint-disable */
import AuthAPI from './auth'
import DateAPI from './date'
import UtilAPI from './util'
// import MarkdownAPI from './markdown'
// import WorkshopsAPI from './workshops'
import EncryptionAPI from './encryption'

export default {
  install: (Vue) => {
    Vue.prototype.$date = DateAPI
    Vue.prototype.$auth = AuthAPI
    Vue.prototype.$util = UtilAPI
    // Vue.prototype.$markdown = MarkdownAPI
    // Vue.prototype.$workshop = WorkshopsAPI
    Vue.prototype.$encryption = EncryptionAPI
  }
}
