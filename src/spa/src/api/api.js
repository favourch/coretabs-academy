/* eslint-disable */
import AuthAPI from './auth'
import DateAPI from './date'
import MarkdownAPI from './markdown'
import WorkshopsAPI from './workshops'
import ProfilesAPI from './profiles'
import CertificatesAPI from './profiles'

export default {
   install: (Vue) => {
      Vue.prototype.$date = DateAPI
      Vue.prototype.$auth = AuthAPI
      Vue.prototype.$api = WorkshopsAPI
      Vue.prototype.$markdown = MarkdownAPI
      Vue.prototype.$profiles = ProfilesAPI
      Vue.prototype.$certificates = CertificatesAPI
      Vue.prototype.$util = {
         prettyDigit(n) {
            return (n < 10) ? `0${n}` : n
         }
      }
   }
}
