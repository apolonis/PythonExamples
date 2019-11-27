from aiohttp import web
import json
from Model import user
async def handle(request):
    response_obj = {'status':'succes'}
    return web.Response(text=json.dumps(response_obj),status=200)

async def new_user(request):
    try:

        user1 = user.User("David","Beckham")
        print("Creating a new user with name: ",user1.name)

        response_obj = {'status':'success','message':'user '+user1.name+' successfully created'}

        return web.Response(text = json.dumps(user1.__dict__), status=200)

    except Exception as e:
        response_obj = {'status':'failed','message':'Enter '+str(e)+' correctly'}
        return web.Response(text=json.dumps(response_obj),status=500)


app = web.Application()
app.router.add_get('/',handle)
app.router.add_post('/user',new_user)

web.run_app(app)
