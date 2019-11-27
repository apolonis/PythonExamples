from aiohttp import web
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

routes = web.RouteTableDef()
engine = create_engine('sqlite:///test1.db')
session = sessionmaker(bind=engine)()
Base = declarative_base()

class Person(Base):

    __tablename__ = "person"

    name = Column(String, primary_key=True)
    lastname = Column(String)

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

@routes.get('/')
async def handler(request):
    return web.Response(text="Web server is running")

@routes.post("/path/{name}/{lastname}")
async def greet_user(request: web.Request) -> web.Response:

    # PATH VARIABLE
    person = Person((request.match_info.get("name","")),(request.match_info.get("lastname","")))

    person1 = Person("Some1","Other1")

    my_data = {"name": person.name, "lastname": person.lastname}
    my_data1 = {"name": person1.name, "lastname": person1.lastname}
    list = []
    list.append(my_data)
    list.append(my_data1)

    session.add(person)
    session.add(person1)
    session.commit()
    return web.json_response(list)

@routes.post("/postReq")
async def postReq(request):

    # REQUEST BODY
    data =await request.json()
    print(data)

    name = data["name"]
    lastname = data["lastname"]

    person = Person(name,lastname)

    my_data = {"name": person.name, "lastname": person.lastname}
    print(type(my_data))

    list_ = []
    list_.append(my_data)
    print(list_)

    session.add(person)

    session.commit()

    return web.json_response(list_)

async def init_app() -> web.Application:

    app = web.Application()
    app.add_routes(routes)

    return app
Base.metadata.create_all(engine)
web.run_app(init_app())