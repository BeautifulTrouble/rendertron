#!/usr/bin/env node

const http = require('http')
const https = require('https')

const hitCache = slug => {
  const req = http.request({
    hostname: 'localhost',
    port: 3000,
    path: `/render/https://beautifultrouble.org/toolbox/#/tool/${slug}`,
    method: 'GET'
  }, res => {
    res.on('end', () => process.stdout.write(`loaded\n`))
  })
}

const req = https.request({
  hostname: 'api.beautifulrising.org',
  port: 443,
  path: '/api/v1/modules',
  method: 'GET'
}, res => {
  let body = ""

  res.on('data', chunk => {
    body += chunk
  })
  res.on('end', () => {
    const tools = JSON.parse(body);
    tools.forEach(tool => {
      process.stdout.write(`Loading ${tool.slug}... `)
      hitCache(tool.slug)
    })
  })
})

req.end()
