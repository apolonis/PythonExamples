from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def handler(request):
    return web.Response(text="Hello world")

@routes.get('/json')
async def get_json(request):
    my_data = {"name":"David Beckham"}
    return web.json_response(my_data)

@routes.post('/add_user')
async def add_user(request:web.Request) -> web.Response:

    data = await request.post()
    name = data.get("name")
    # add the user
    # ...
    return web.Response(text=f"{name} was added")

@routes.get("/{name}")
# @routes.post("{name}")
async def greet_user(request: web.Request) -> web.Response:
    user = request.match_info.get("name","")
    return web.Response(text=f"Hello, {user}")



async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app

web.run_app(init_app())
