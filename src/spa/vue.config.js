const CompressionPlugin = require('compression-webpack-plugin')
const FaviconsWebpackPlugin = require('favicons-webpack-plugin')
const webpack = require('webpack')
const path = require('path')
var config = {
  outputDir: 'static',
  configureWebpack: {
    entry: './src/client-entry.js',
    output: {
      path: path.resolve(__dirname, './static'),
      publicPath: '/'
    },
    plugins: [
      new webpack.EnvironmentPlugin(['API_BASE_URL', 'MAINTENANCE_MODE']),
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
    minRatio: 0.8
  }))
}

module.exports = config
