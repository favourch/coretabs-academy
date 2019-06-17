export default {
  name: 'ManageProjectsComponent',
  data: () => ({
    reader: null,
    project_img: '',
    alert: {
      success: false,
      error: false,
      message: ''
    },
    isAdd: false,
    validImage: {
      valid: false,
      imageData: ''
    },
    waiting: false,
    editProjectId: null,
    valid: false,
    vs: {
      v1: false,
    },
    project_name: '',
    repo_link: '',
    demo_link: '',
    dialog: false,
    deleteDialog: false,
    projects: null
  }),
  watch: {
    'validImage.valid': function() {
      this.chackValid()
    }
  },
  computed: {
    i18n() { return this.$store.state.i18n.account.manage_projects },
    form() { return this.$store.state.i18n.form }
  },
  methods: {
    previewImage(event) {
      let input = event.target
      this.reader = new FileReader()
      if (input.files && input.files[0]) {
        const img = new Image()
        img.src = window.URL.createObjectURL(input.files[0])
        img.onload = () => {
          window.URL.revokeObjectURL(img.src)
          this.validImage.valid = true
          this.validImage.imageData = input.files[0]
          this.reader.onload = (e) => {
            this.project_img = e.target.result
          }
          this.reader.readAsDataURL(input.files[0])
        }
      }
    },
    chackValid() {
      let root = this
      root.vs.v1 = true

      root.pnRules.forEach((rule) => { if (rule(root.project_name) !== true) { root.vs.v1 = false } })
      root.valid = root.vs.v1 && (root.repo_link || root.demo_link) && root.validImage.valid
    },
    async fetchProjects() {
      let root = this

      await axios.get('/api/v1/profile', {
        withCredentials: true
      }).then(async (response) => {
        await root.$auth.storeProfile(root.$store, response.data)
      }).catch()
      this.projects = await this.$store.getters.profile('projects').reverse()
    },
    addProject() {
      this.isAdd = true
      this.$refs.form.reset()
      this.validImage.valid = false

      this.alert = {
        success: false,
        error: false,
        message: ''
      }

      this.project_name =  ''
      this.project_img = ''
      this.repo_link =  ''
      this.demo_link =  ''
      this.dialog = true
    },
    editProject(id) {
      this.isAdd = false
      this.editProjectId = id

      this.alert = {
        success: false,
        error: false,
        message: ''
      }

      this.valid = false
      let project = this.projects.filter(e => e.id === id)[0]

      this.project_name = project.description
      this.project_img = project.photo
      this.repo_link = project.github_link
      this.demo_link = project.live_demo_link

      this.dialog = true
    },
    openDeleteDialog(id) {
      this.editProjectId = id
      let project = this.projects.filter(e => e.id === id)[0]
      this.project_name = project.description
      this.deleteDialog = true
    },
    async deleteProject() {
      let root = this
      root.waiting = true

      this.deleteDialog = true
      root.waiting = await this.$profiles.deleteProject(root)
      
      if (!root.waiting) {
        this.deleteDialog = false
        this.fetchProjects()
        this.alert = {
          success: false,
          error: false,
          message: ''
        }
      }
    },
    async submit() {
      if (this.valid) {
        let root = this
        root.waiting = true
        
        // is the user will add new project
        if (this.isAdd || this.$route.params.isAddFromRoute) {
          root.waiting = await this.$profiles.createProject(root)

          if (!root.waiting && !this.alert.error) {
            this.fetchProjects()
            this.dialog = false
          }
        }
        
        // is the user will edit instead of add
        if (!this.isAdd) {
          root.waiting = true
          root.waiting = await this.$profiles.changeProjectInfo(root)
            
          if (!root.waiting) {
            this.fetchProjects()
          }
        }
      }
    }
  },
  async created() {
    if (this.$route.params.isAddFromRoute) {
      this.dialog = true
    }

    this.fetchProjects()

    this.pnRules = [
      v => !!v || '',
      v => (v && v.length <= 20) || this.form.projectname_length_error
    ]

  },
  updated() {
    this.chackValid()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
  