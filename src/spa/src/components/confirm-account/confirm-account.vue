<script>
export default {
  name: 'ConfirmAccountComponent',
  mounted() {
    var root = this
    this.$auth.verifyEmail(root)
  }
}
</script>
