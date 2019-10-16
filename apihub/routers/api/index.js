const koaRouter = require('koa-router')
const router = koaRouter()
const controller = require('../../controllers/api')

router.get('/userinfo', controller.userInfo)

module.exports = router