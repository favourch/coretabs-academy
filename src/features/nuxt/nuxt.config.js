module.exports = {
  /*
   ** Headers of the page
   */
  head: {
    title: 'أكاديمية Coretabs',
    meta: [{
      charset: 'utf-8'
    }, {
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    }, {
      hid: 'description',
      name: 'description',
      content: 'Coretabs Academy is the first step that will transform your career as a developer. Start talking the future language, select your track, we will make you READY to work'
    }, {
      'http-equiv': 'X-UA-Compatible',
      content: 'IE=edge'
    }],
    link: [{
      rel: 'icon',
      type: 'image/x-icon',
      href: '/favicon.ico'
    }]
  },
  css: ['~/assets/styles/index.scss'],
  plugins: [
    '~/plugins/vuetify.js',
    '~/plugins/api/index.js', {
      src: '~/plugins/vue-video-player.js',
      ssr: false
    }
  ],
  loading: '~/components/loading/loading.vue',
  cache: {
    max: 1000,
    maxAge: 900000
  },
  // Nuxt.js lets you create environment variables that will be shared for the client and server-side.
  env: {},
  mode: 'universal',
  router: {
    mode: 'history',
    linkActiveClass: 'active-link',
    linkExactActiveClass: 'exact-active-link'
    // ,
    // middleware: ''
  },
  render: {
    bundleRenderer: {
      shouldPreload: (file, type) => {
        return ['script', 'style', 'font'].includes(type)
      }
    }
  },

  /*
   ** Build configuration
   */
  build: {
    analyze: true,
    extractCSS: true,
    cssSourceMap: false,
    vendor: [
      'axios',
      'vuetify'
    ],
    /*
     ** Run ESLint on save
     */
    extend(config, {
      isDev,
      isClient
    }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
