const Koa = require('koa')
const routers = require('./routers')
const app = new Koa()

app.use(routers.routes(), routers.allowedMethods())
app.listen(3000)
console.log("demo in run")