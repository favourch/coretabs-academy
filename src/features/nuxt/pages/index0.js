
export default {
  name: 'HomeComponent',
  components: {
    videoPlayer
  },
  data: () => ({
    playerOptions: {
      autoplay: false,
      sources: [{
        type: 'video/mp4',
        src: 'https://www.w3schools.com/html/mov_bbb.mp4'
      }]
    }
  }),


}
