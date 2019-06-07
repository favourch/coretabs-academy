import Siema from 'siema'

let carouselTransitionT
let carouselTransitionM
let mentorsSiema

export default {
  name: 'AboutComponent',
  data: () => ({
    sectionsImages: [],
    testimonialsImages: [],
    teamImages: [],
    contributorsImages: [],
    mentorsImages: [],
    quotationIcon: '',
    starState: {
      active: '',
      inactive: ''
    },
    icons: {
      github: '',
      stackoverflow: '',
      website: '',
      linkedin: '',
      twitter: '',
      facebook: '',
      LH: ''
    },
    navigation: {
      left: '',
      right: ''
    },
    currentSlide: 0,
    testimonialsSiema: {
      perPage: ''
    },
    perPage: 1
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
    showMentors(i, e) {
      let children = e.currentTarget.parentElement.children
      for (let i = 0; i < children.length; i++) {
        children[i].classList.remove('active')
      }
      e.currentTarget.classList.add('active')
      mentorsSiema.goTo(i * this.perPage)
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
    playMSiema() {
      carouselTransitionM = setInterval(() => {
        if (mentorsSiema.currentSlide + mentorsSiema.perPage >= this.i18n.mentors.members.length) {
          mentorsSiema.prev(this.i18n.mentors.members.length)
        } else {
          mentorsSiema.next(mentorsSiema.perPage)
        }
      }, 5000)
    },
    mentorsSliderCount() {
      return Math.ceil(this.i18n.mentors.members.length / this.perPage)
    },
    prev() {
      var index = mentorsSiema.currentSlide / mentorsSiema.perPage
      if (mentorsSiema.currentSlide % mentorsSiema.perPage === 0) {
        const slideM = document.querySelector('.m')
        if (slideM) {
          var children = slideM.children
          for (var i = 0; i < children.length; i++) {
            children[i].classList.remove('active')
          }
          index = Math.ceil(index)
          children[index].classList.add('active')
        }
      }
      mentorsSiema.prev(mentorsSiema.perPage)
    },
    next() {
      var index = mentorsSiema.currentSlide / mentorsSiema.perPage
      if (mentorsSiema.currentSlide % mentorsSiema.perPage === 0) {
        const slideM = document.querySelector('.m')
        if (slideM) {
          var children = slideM.children
          for (var i = 0; i < children.length; i++) {
            children[i].classList.remove('active')
          }
          index = Math.ceil(index)
          children[index].classList.add('active')
        }
      }
      mentorsSiema.next(mentorsSiema.perPage)
    }
  },
  created() {
    for (let section of this.i18n.sections) {
      this.$store.dispatch('getImgUrl', `images/${section.src}.svg`).then(img => {
        this.sectionsImages.push(img)
      }).catch(error => {
        throw new Error(error.message)
      })
    }

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

    for (let icon in this.icons) {
      this.$store.dispatch('getImgUrl', `icons/social-icons/${icon !== 'LH' ? icon + '.svg' : icon + '.png'}`).then(img => {
        this.icons[icon] = img
      }).catch(error => {
        throw new Error(error.message)
      })
    }

    for (let member of this.i18n.team.members) {
      this.$store.dispatch('getImgUrl', `images/${member.src}`).then(img => {
        this.teamImages.push(img)
      }).catch(error => {
        throw new Error(error.message)
      })
    }

    for (let member of this.i18n.contributors.members) {
      this.$store.dispatch('getImgUrl', `images/${member.src}`).then(img => {
        this.contributorsImages.push(img)
      }).catch(error => {
        throw new Error(error.message)
      })
    }

    for (let member of this.i18n.mentors.members) {
      this.$store.dispatch('getImgUrl', `images/${member.src}`).then(img => {
        this.mentorsImages.push(img)
      }).catch(error => {
        throw new Error(error.message)
      })
    }

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

    this.playTSiema()

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

    let root = this

    mentorsSiema = new Siema({
      selector: '.mentors-carousel',
      duration: 1000,
      easing: 'ease-out',
      perPage: {
        1150: 4,
        900: 3,
        650: 2,
        520: 3,
        0: 2
      },
      startIndex: 0,
      draggable: true,
      multipleDrag: true,
      threshold: 20,
      loop: false,
      rtl: false,
      onInit: changeCurrentSlideM,
      onChange: changeCurrentSlideM
    })

    this.playMSiema()

    function changeCurrentSlideM() {
      var index = this.currentSlide / this.perPage
      if (this.currentSlide % this.perPage === 0 || index + 1 === root.mentors.members.length / this.perPage) {
        const slideM = document.querySelector('.m')
        if (slideM) {
          var children = slideM.children
          for (var i = 0; i < children.length; i++) {
            children[i].classList.remove('active')
          }
          index = Math.ceil(index)
          children[index].classList.add('active')
        }
      }
    }

    addEventListener('resize', function() {
      root.perPage = mentorsSiema.perPage
      const slideM = document.querySelector('.m')
      if (slideM) {
        var children = slideM.children
        for (var i = 0; i < children.length; i++) {
          children[i].classList.remove('active')
        }
        children[0].classList.add('active')
        mentorsSiema.currentSlide = 0
      }
    }, false)

    let childrenM = this.$refs.controlsT.children
    for (let i = 0; i < childrenM.length; i++) {
      childrenM[i].classList.remove('active')
    }
    childrenM[0].classList.add('active')

    this.perPage = mentorsSiema.perPage
  },
  beforeDestroy() {
    clearInterval(carouselTransitionT)
    clearInterval(carouselTransitionM)
  }
}
