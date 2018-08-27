const path = require('path')
const merge = require('webpack-merge')
const VueSSRServerPlugin = require('vue-server-renderer/server-plugin')
let VueConfig = require('./client.config')

delete VueConfig.module

let ServerConfig = merge(VueConfig, {
  target: 'node',
  entry: {
    app: './src/server-entry.js'
  },
  output: {
    path: path.resolve(__dirname, './static'),
    filename: 'js/server.app.js',
    libraryTarget: 'commonjs2'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg|ttf|woff2)$/,
        loader: 'file-loader',
        options: {
          emitFile: false
        }
      }
    ]
  },
  externals: Object.keys(require('./package.json').dependencies)
})

ServerConfig.plugins = [
  ServerConfig.plugins.shift(),
  new VueSSRServerPlugin()
]
module.exports = ServerConfig
