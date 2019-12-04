from aiohttp import web
from sqlalchemy.orm import sessionmaker
from Model import user

routes = web.RouteTableDef()
engine = user.dbCreate()
session = sessionmaker(bind=engine)()

# localhost:8080/
@routes.get('/')
async def handler(request):
    return web.Response(text="<h1 style ='color:blue;"
                             "text-align:center'> Server is running"
                             "</h1><br>"
                             "<div><a href="'http://localhost:8080/home'">home page</a><p>Click to go to youtube tutorial</div><br>"
                        ,content_type='text/html')

# home page
@routes.get('/home')
async def homePage(request):
    return web.Response(text="<h1 style='color:blue; text-align:center'>Home page </h1>"
                             "<body><div><p style='color:blue'>Home page</p></div>"
                             "<div><a href="'http://localhost:8080/getAll'">Get all persons</a><p>Click to get all persons</div></div></body>",
                        content_type='text/html')

# create user
@routes.post("/register")
async def register(request):

    data=await request.json()

    name = data['name']
    lastname = data['lastname']
    email = data['email']
    address = data['address']
    roles = data['roles']

    userObject = user.User(name,lastname,email,address,roles)

    my_data = {'name':userObject.name,
               'lastname':userObject.lastname,
               'email':userObject.email,
               'address':userObject.address,
               'roles':userObject.roles}
    myList = []
    myList.append(my_data)

    session.add(userObject)
    session.commit()
    return web.json_response(myList)

# get all mapping
@routes.get('/getAll')
async def getAll(request):

    result = [i for i in session.query(user.User).all()]
    myList = []
    for i in result:

        my_data = {"id":i.id,
                   "name":i.name,
                   "lastname":i.lastname,
                   "email":i.email,
                   "address":i.address,
                   "roles":i.roles}

        myList.append(my_data)

    return web.json_response(myList)

# get by id mapping
@routes.get("/id/{id}")
async def getById(request:web.Response) -> web.Response:
    result = [i for i in session.query(user.User).all()]
    id_ = request.match_info.get("id","")

    for i in result:
        if i.id == int(id_):
            myData = {"id":i.id,
                      "name":i.name,
                      "lastname":i.lastname,
                      "email":i.email,
                      "address":i.address,
                      "roles":i.roles}
    return web.json_response(myData)

# get by role mapping
@routes.get("/role/{roles}")
async def getByRole(request:web.Response) ->web.Response:
    result = [i for i in session.query(user.User).all()]
    roles_ = request.match_info.get("roles","")
    myList = []

    for i in result:
        if i.roles == roles_:

            myData = {"id":i.id,
                      "name":i.name,
                      "lastname":i.lastname,
                      "email":i.email,
                      "address":i.address,
                      "roles":i.roles}

            myList.append(myData)

    return web.json_response(myList)

# get by name mapping
@routes.get("/name/{name}")
async def getById(request:web.Response) -> web.Response:
    result = [i for i in session.query(user.User).all()]
    name_ = request.match_info.get("name","")

    for i in result:
        if i.name == name_:
            myData = {"id":i.id,
                      "name":i.name,
                      "lastname":i.lastname,
                      "email":i.email,
                      "address":i.address,
                      "roles":i.roles}
    return web.json_response(myData)

# delete by id mapping
@routes.delete("/deleteById/{id}")
async def getById(request:web.Response) -> web.Response:
    result = [i for i in session.query(user.User).all()]
    id_ = request.match_info.get("id","")

    for i in result:
        if i.id == int(id_):
            session.delete(i)
            session.commit()
    return web.Response(text=f"User with id: {id_}, has been deleted!")

async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app

web.run_app(init_app())