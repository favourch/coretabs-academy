const CompressionPlugin = require('compression-webpack-plugin')
const FaviconsWebpackPlugin = require('favicons-webpack-plugin')
const path = require('path')
var config = {
  outputDir: 'public_html',
  configureWebpack: {
    output: {
      publicPath: '/',
      path: path.resolve(__dirname, './public_html')
    },
    plugins: [
      new FaviconsWebpackPlugin({
        logo: './src/assets/multimedia/icons/icon.png',
        prefix: 'icons/',
        persistentCache: true,
        inject: true,
        background: '#fff',
        title: 'Coretabs Academy',
        icons: {
            android: true,
            appleIcon: true,
            appleStartup: true,
            coast: false,
            favicons: true,
            firefox: true,
            opengraph: true,
            twitter: true,
            yandex: true,
            windows: true
        }
      })
    ]
  }
}

if (process.env.NODE_ENV === 'production') {
  config.configureWebpack.plugins.push(new CompressionPlugin({
    asset: '[path].gz[query]',
    algorithm: 'gzip',
    test: /\.js$|\.css$|\.html$/,
    threshold: 10240,
    minRatio: 0.8,
    deleteOriginalAssets: true
  }))
}

module.exports = config
