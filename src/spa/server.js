const express = require('express')
const server = express()
const fs = require('fs')
const path = require('path')

const template = fs.readFileSync(path.resolve(__dirname, './static/index.html'), 'utf-8')
const bundle = require('./static/js/server.app.js')
const renderer = require('vue-server-renderer').createRenderer(bundle)

server.get('*.js', (req, res, next) => {
  req.url = req.url + '.gz'
  res.set('Content-Encoding', 'gzip')
  res.set('Content-Type', 'text/javascript')
  next()
})

server.get('*.css', (req, res, next) => {
  req.url = req.url + '.gz'
  res.set('Content-Encoding', 'gzip')
  res.set('Content-Type', 'text/css')
  next()
})

server.use('/static', express.static(path.join(__dirname, './static'), { maxAge: '356d' }))

server.get('*', (req, res) => {
  bundle.default({url: req.url}).then((app) => {
    renderer.renderToString(app, (err, html) => {
      if (err) {
        if (err.code === 404) {
          res.status(404).end('Page not found')
        } else {
          console.log('err', err)
          res.status(500).end('Internal Server Error')
        }
      } else {
        html = template.replace('{{ APP }}', html)
        res.write(html)
        res.end()
      }
    })
  }, (err) => {
    console.log(err)
  })
})

const port = process.env.PORT || 3000
server.listen(port, () => {
   console.log(`server started as http://localhost:${port}`)
})
