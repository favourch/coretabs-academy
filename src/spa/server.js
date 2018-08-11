const history = require('connect-history-api-fallback')
const express = require('express')
const server = express()
const fs = require('fs')
const path = require('path')

const template = fs.readFileSync(path.resolve(__dirname, './static/index.html'), 'utf-8')

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

server.use(express.static(path.join(__dirname, './static'), { maxAge: '356d' }))
server.use(history({
  disableDotRule: true,
  verbose: true
}))

server.get('*', (req, res) => {
  res.write(template)
  res.end()
})

const port = process.env.PORT || 3000
server.listen(port, () => {
   console.log(`server started as http://localhost:${port}`)
})
