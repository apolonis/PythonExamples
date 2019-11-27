from aiohttp import web
from Model import Person
import sqlalchemy as db

routes = web.RouteTableDef()

def initDb():
    engine = db.create_engine('sqlite://census.sqlite')
    connection = engine.connect()

    metadata = db.MetaData()
    census = db.Table('census', metadata, autoload=True, autoload_with=engine)

@routes.get('/')
async def handler(request):
    return web.Response(text="Web server is running")

async def init_app() -> web.Application:
    initDb()
    app = web.Application()
    app.add_routes(routes)
    return app

web.run_app(init_app())