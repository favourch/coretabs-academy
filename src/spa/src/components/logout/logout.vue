<script>
export default {
  name: 'LogoutComponent',
  mounted() {
    var root = this
    this.$auth.logout(root)
  }
}
</script>
