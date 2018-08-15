const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const FaviconsWebpackPlugin = require('favicons-webpack-plugin')
const CompressionPlugin = require('compression-webpack-plugin')
const webpack = require('webpack')
const path = require('path')

console.log('========= ENV', process.env.NODE_ENV)

var config = {
  mode: 'development',
  entry: './src/client-entry.js',
  output: {
    publicPath: '/',
    filename: 'js/app.[hash].js'
  },
  optimization: {
    minimize: true
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: [
          {
            loader: 'vue-loader',
            options: {
              loaders: {
                scss: [
                  'vue-style-loader',
                  process.env.NODE_ENV === 'production' ? MiniCssExtractPlugin.loader : '',
                  'css-loader',
                  'sass-loader'
                ]
              }
            }
          }
        ]
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: 'images/[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(ttf|woff2)$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]?[hash]'
        }
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      vue$: 'vue/dist/vue.esm.js'
    }
  },
  devtool: '#source-map',
  devServer: {
    publicPath: '/',
    clientLogLevel: 'none',
    compress: true,
    historyApiFallback: true
  },
  plugins: [
    new webpack.EnvironmentPlugin({
      NODE_ENV: '',
      API_BASE_URL: '',
      MAINTENANCE_MODE: 'false'
    }),
    new HtmlWebpackPlugin({
      template: './public/index.html'
    })
  ]
}
if (process.env.NODE_ENV === 'production') {
  config.mode = 'production'
  config.output.path = path.resolve(__dirname, './static')
  config.output.publicPath = '/static/'
  config.output.filename = 'js/app.[chunkhash].js'
  config.plugins.push(
    new CleanWebpackPlugin(path.resolve(__dirname, './static')),
    new MiniCssExtractPlugin({
      filename: 'css/app.[chunkhash].css'
    }),
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
    }),
    new CompressionPlugin({
      asset: '[path].gz[query]',
      algorithm: 'gzip',
      test: /\.js$|\.css$|\.html$/,
      threshold: 10240,
      minRatio: 0.8,
      deleteOriginalAssets: true
    })
  )
}

module.exports = config
