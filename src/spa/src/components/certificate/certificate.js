export default {
  name: 'certificate',
  data: () => ({
    shareDialog: false,
    certificateLink: '',
    isCopied: false,
    manualCopy: false
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
    }
  }
}
