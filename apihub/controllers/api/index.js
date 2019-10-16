const userInfo = (ctx, next) => {
    ctx.type = 'text/html'
    ctx.body = 'userInfo Controller'
    next()
}
module.exports = {userInfo}