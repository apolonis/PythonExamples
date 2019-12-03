from aiohttp import web
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Model import user

routes = web.RouteTableDef()
engine = user.dbCreate()
session = sessionmaker(bind=engine)()
Base = declarative_base()

@routes.get('/')
async def handler(request):
    return web.Response(text="<h1 style ='color:blue;"
                             "text-align:center'> Server is running"
                             "</h1><br>"
                             "<div><a href="'http://localhost:8080/home'">home page</a><p>Click to go to youtube tutorial</div><br>"
                        ,content_type='text/html')

@routes.post("/signup")
async def signup(request):

    data=await request.json()

    username = data["username"]
    password = data["password"]
    roles = data["roles"]
    userObject = user.User(username,password,roles)

    my_data = {"username":userObject.username,
               "password":userObject.password,
               "roles":userObject.roles}
    list_ = []
    list_.append(my_data)

    session.add(userObject)
    session.commit()
    return web.json_response(list_)

@routes.get("/getAll")
async def getAll(request):

    result = [i for i in session.query(user.User).all()]
    list_ = []
    for i in result:
        my_data = {"id":i.id,
                   "username":i.username,
                   "password":i.password,
                   "roles":i.roles}
        list_.append(my_data)

    return web.json_response(list_)

@routes.get("/login")
async def login(request):
    result = [i for i in session.query(user.User).all()]
    data = await request.json()

    username = data["username"]
    password = data["password"]

    for i in result:
        if i.username == username:
            if i.username == password:
                my_data = {"id":i.id,"username":i.username,"roles":i.roles}
                return web.json_response(my_data)
            else:
                return web.Response(text="Invalid credentials, try again!!!")

@routes.get("/get/{username}")
async def getByUsername(request: web.Request) -> web.Response:
    result = [i for i in session.query(user.User).all()]
    username_ = request.match_info.get("username","")

    for i in result:
        if i.username == username_:
            my_data = {"id":i.id,"username":i.username,"roles":i.roles}
    return web.json_response(my_data)

@routes.get("/getByRoles/{roles}")
async def getByRoles(request:web.Request) -> web.Response:
    result = [i for i in session.query(user.User).all()]
    roles_ = request.match_info.get("roles","")
    list_ = []

    for i in result:
        if i.roles == roles_:
            my_data = {"id":i.id,
                       "username":i.username,
                       "roles":i.roles}
            list_.append(my_data)

    return web.json_response(list_)

@routes.get("/getById/{id}")
async def getById(request:web.Response) -> web.Response:
    result = [i for i in session.query(user.User).all()]
    id_ = request.match_info.get("id","")

    for i in result:
        if i.id == int(id_):
            my_data = {"id": i.id,
                       "username": i.username,
                       "roles": i.roles}

    return web.json_response(my_data)




@routes.get('/home')
async def handler(request):
    return web.Response(text="<h1 style='color:blue; text-align:center'>Home page </h1>"
                             "<body><div><p style='color:blue'>This is a home page for aiohttp example</p></div>"
                             "<div><a href="'https://www.youtube.com/watch?v=OxzVApXKWYM'">youtube link</a><p>Click to go to youtube tutorial</div><br>"
                             "<div><a href="'https://aiohttp.readthedocs.io/en/stable/'">aiohttp official</a><p>Click to go to official tutorial</div><br>"
                             "<div><a href="'http://localhost:8080/getAll'">Get all persons</a><p>Click to get all persons</div></div></body>",
                        content_type='text/html')

async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app

Base.metadata.create_all(engine)
web.run_app(init_app())