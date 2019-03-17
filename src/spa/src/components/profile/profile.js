import InnerHeaderComponent from '../inner-header/inner-header.vue'
export default {
  name: 'ProfileComponent',
  components: {
    InnerHeaderComponent
  },
  data() {
    return {
      tabs: [
        { name: 'about', text: 'حول', path: 'about' },
        { name: 'certificates', text: 'الشهادات', path: 'certificates' }
      ]
    }
  }
}