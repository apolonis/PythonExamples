from aiohttp import web
from Model import Person
routes = web.RouteTableDef()

@routes.get('/')
async def handler(request):
    return web.Response(text="Hello world")

@routes.post("/path/{name}/{lastname}")
async def greet_user(request: web.Request) -> web.Response:

    # PATH VARIABLE
    person = Person.Person((request.match_info.get("name","")),(request.match_info.get("lastname","")))

    person1 = Person.Person("Some","Other")

    my_data = {"name": person.name, "lastname": person.lastname}
    my_data1 = {"name": person1.name, "lastname": person1.lastname}
    list = []
    list.append(my_data)
    list.append(my_data1)

    return web.json_response(list)

@routes.post("/postReq")
async def postReq(request):

    # REQUEST BODY
    data =await request.json()
    print(data)

    name = data["name"]
    lastname = data["lastname"]

    person = Person.Person(name,lastname)

    my_data = {"name": person.name, "lastname": person.lastname}
    print(type(my_data))

    list_ = []
    list_.append(my_data)
    print(list_)

    return web.json_response(list_)

async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    # app.add_routes([web.get('/path1', get_1),
    #                 web.get('/path2', get_2),
    #                 web.post('/path2', post_2),
    #                 web.post('/path1', post_1)]

    return app

web.run_app(init_app())

