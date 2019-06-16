import Siema from 'siema'
import Countdown from './../countdown/countdown.vue'

let carouselTransitionT
let carouselTransitionM

export default {
  name: 'FrontendComponent',
  components: {
    Countdown
  },
  data: () => ({
    sectionsImages: [],
    testimonialsImages: [],
    quotationIcon: '',
    starState: {
      active: '',
      inactive: ''
    },
    navigation: {
      left: '',
      right: ''
    },
    currentSlide: 0,
    testimonialsSiema: {
      perPage: ''
    },
    perPage: 1,
    activeProjectItem: 0,
    projectImage: require('../../assets/multimedia/images/track/backend/atm.gif'),
    projects: [
      {
        title: 'تطوير تطبيق صراف آلي ATM',
        imgSrc: require('../../assets/multimedia/images/track/backend/atm.gif')
      },
      {
        title: 'تطوير تطبيق مشابه للفيسبوك',
        imgSrc: require('../../assets/multimedia/images/track/backend/posty.png'),
        url: 'https://demos.coretabs.net/server/facebook-like-app/'
      }
    ]
  }),
  computed: {
    i18n() { return this.$store.state.i18n.about }
  },
  methods: {
    showTestimonials(i, e) {
      let children = e.currentTarget.parentElement.children
      for (let i = 0; i < children.length; i++) {
        children[i].classList.remove('active')
      }
      e.currentTarget.classList.add('active')
      this.testimonialsSiema.goTo(i)
    },
    calc(i, j) {
      return i <= j ? this.starState.active : this.starState.inactive
    },
    stopTSiema() {
      clearInterval(carouselTransitionT)
    },
    playTSiema() {
      carouselTransitionT = setInterval(() => { this.testimonialsSiema.prev() }, 4000)
    },
    stopMSiema() {
      clearInterval(carouselTransitionM)
    },
    scrollTo(sectionName) {
      let pricingSection = document.getElementById(sectionName)
      let offset = pricingSection.offsetTop
      window.scrollTo(0, offset)
    },
    showProject(project, index) {
      this.activeProjectItem = index
      this.projectImage = project.imgSrc
    },
    showDemo(url) {
      window.open(url, '_blank')
    }
  },
  created() {   
    for (let testimonial of this.i18n.testimonials.carousel) {
      this.$store.dispatch('getImgUrl', `images/testimonials/${testimonial.img}`).then(img => {
        this.testimonialsImages.push(img)
      }).catch(error => {
        throw new Error(error.message)
      })
    }

    this.$store.dispatch('getImgUrl', 'images/quotation.svg').then(img => {
      this.quotationIcon = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'images/star_active.svg').then(img => {
      this.starState.active = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'images/star_inactive.svg').then(img => {
      this.starState.inactive = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'images/left.svg').then(img => {
      this.navigation.left = img
    }).catch(error => {
      throw new Error(error.message)
    })

    this.$store.dispatch('getImgUrl', 'images/right.svg').then(img => {
      this.navigation.right = img
    }).catch(error => {
      throw new Error(error.message)
    })
  },
  mounted() {
    this.testimonialsSiema = new Siema({
      selector: '.testimonials-carousel',
      duration: 500,
      easing: 'ease-out',
      perPage: 1,
      startIndex: 0,
      draggable: true,
      multipleDrag: true,
      threshold: 20,
      loop: true,
      rtl: true,
      onInit: changeCurrentSlideT,
      onChange: changeCurrentSlideT
    })

    function changeCurrentSlideT() {
      const slideT = document.querySelector('.t')
      if (slideT) {
        var children = slideT.children
        for (var i = 0; i < children.length; i++) {
          children[i].classList.remove('active')
        }
        children[this.currentSlide].classList.add('active')
      }
    }

    let childrenT = this.$refs.controlsT.children
    for (let i = 0; i < childrenT.length; i++) {
      childrenT[i].classList.remove('active')
    }
    childrenT[0].classList.add('active')
  },
  beforeDestroy() {
    clearInterval(carouselTransitionT)
    clearInterval(carouselTransitionM)
  }
}
