const koaRouter = require('koa-router')
const router = koaRouter()

const api = require('./api')

router.get('/', async(ctx, next) => {
    ctx.type = 'text/html'
    ctx.body = 'root router'
})

router.get('/index', async (ctx, next) => {
    ctx.type = 'text/html'
    ctx.body = 'hello routers/index.js'
})

router.use('/api', api.routes())

module.exports = router