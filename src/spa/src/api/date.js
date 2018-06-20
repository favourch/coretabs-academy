/* eslint-disable */
import Vue from 'vue'

const DateAPI = {
   get(date) {
      return `${Vue.prototype.$util.prettyDigit(date.getDate())}/${Vue.prototype.$util.prettyDigit(date.getMonth())}/${date.getFullYear()}`
   }
}

export default DateAPI
