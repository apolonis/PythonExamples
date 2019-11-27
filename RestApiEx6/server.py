from aiohttp import web

async def handler(request):
    return web.Response(text="Hello world")

async def handler1(request):
    return web.Response(text="Hello world 2")

async def init_app() -> web.Application:
    app=web.Application()
    app.add_routes([web.get("/",handler)])
    app.add_routes([web.get("/handler1",handler1)])
    app.add_routes([web.get("/{username}",greet_user)])
    return app
#
# app = web.Application()
# app.add_routes([web.get('/',handler)],)
# app.add_routes([web.get('/handler1',handler1)])

async def greet_user(request: web.Request) -> web.Response:
    user = request.match_info.get("username", "")
    return web.Response(text=f"Hello, {user}")

web.run_app(init_app())
