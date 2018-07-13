<script>
export default {
  name: 'ConfirmAccountComponent',
  mounted() {
    let root = this
    this.$auth.verifyEmail(root)
  }
}
</script>
