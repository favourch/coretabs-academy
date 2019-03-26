import Vue from 'vue'
import VueHtml2Canvas from 'vue-html2canvas'
Vue.use(VueHtml2Canvas)

export default {
  name: 'certificate',
  props: ['certificateId'],
  data: () => ({
    shareDialog: false,
    certificateLink: '',
    isCopied: false,
    manualCopy: false,
    output: null,
    loading: false,
    certificate: {},
    firstName: ''
  }),
  methods: {
    shareCertificate() {
      this.shareDialog = true
      this.certificateLink = window.location.href
    },
    closeDialog() {
      this.shareDialog = false
    },
    copyToClipboard() {
      let link = document.querySelector('#link-holder')
      link.setAttribute('type', 'text') 
      link.select()
      try {
        document.execCommand('copy')
        this.isCopied = true
        setTimeout(() => {
          this.isCopied = false
        }, 2000)
      } catch (err) {
        this.isCopied = true
        this.manualCopy = true
        setTimeout(() => {
          this.isCopied = false
        }, 2000)
      }
      link.setAttribute('type', 'hidden')
      window.getSelection().removeAllRanges()
    },
    async download() {
      this.loading = true
      let ribbon = document.querySelector('#certificate-ribbon')
      ribbon.style.top = '0px'
      const el = this.$refs.download
      const options = {
        type: 'dataURL'
      }
      this.output = await this.$html2canvas(el, options)
      this.loading = false
      console.log(this.output)

      var link = document.createElement('a')
      link.download = this.output
      link.href = this.output
      link.click()
    }
  },
  created() {
    this.$profiles.getCertificate(`/api/v1/certificates/${this.certificateId}`)
    .then(response => {
      this.certificate = response
      this.firstName = response.full_name.split(' ')[0]
    })
    .catch(err => {
      console.log(err)
    })
  }
}
