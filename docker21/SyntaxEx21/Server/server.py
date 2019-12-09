from aiohttp import web
from sqlalchemy.orm import sessionmaker
from Model import driver,car

routes = web.RouteTableDef()
engine = driver.dbCreate()
session = sessionmaker(bind=engine)()

# /
@routes.get('/')
async def handler(request):
    return web.Response(text="<h1 style ='color:blue;"
                             "text-align:center'> Server is running"
                             "</h1><br>"
                             "<div><a href="'http://localhost:8080/home'">home page</a><p>Click to go to youtube tutorial</div><br>"
                        ,content_type='text/html')

# Create driver
@routes.post("/createDriver")
async def createDriver(request):
    data = await request.json()
    fullname = data['fullname']
    driverObject = driver.Driver(fullname)
    session.add(driverObject)
    session.commit()
    driverDict = {'fullname':driverObject.fullname}
    return web.json_response(driverDict)

# Create car
@routes.post("/createCar")
async def createCar(request):
    data = await request.json()
    model = data['model']
    driver_id = data['driver_id']
    carObject = car.Car(model, int(driver_id))
    session.add(carObject)
    session.commit()
    carDict = {'model':carObject.model}
    return web.json_response(carDict)

# get all drivers
@routes.get("/allDrivers")
async def getAllDrivers(request:web.Response)->web.Response:
    result = [i for i in session.query(driver.Driver).all()]
    myList = []
    for i in result:
        driverDict = {"id":i.id,
                      "fullname":i.fullname}
        myList.append(driverDict)
    return web.json_response(myList)

# get all cars
@routes.get("/allCars")
async def getAllCars(request:web.Response)->web.Response:
    result = [i for i in session.query(car.Car).all()]
    myList = []
    for i in result:
        carDict = {"id":i.id,
                      "model":i.model,
                      "driver_id":i.driver_id}
        myList.append(carDict)
    return web.json_response(myList)

# get all cars for a driver
@routes.get("/fullname/{fullname}")
async def getAllCarsByDriver(request : web.Response)->web.Response:
    resultDriver = [i for i in session.query(driver.Driver).all()]
    name_ = request.match_info.get("fullname","")
    resultCar = [j for j in session.query(car.Car).all()]
    myList = []
    for i in resultDriver:
        if i.fullname == name_.lower():
            for j in resultCar:
                if j.driver_id == i.id:
                    carDict = {"id":j.id,
                               "model":j.model,
                               "driver_id":j.driver_id}
                    myList.append(carDict)
    return web.json_response(myList)

# get all drivers by car model
@routes.get("/model/{model}")
async def getAllDriversByCar(request : web.Response)->web.Response:
    resultDriver = [i for i in session.query(driver.Driver).all()]
    resultCar = [j for j in session.query(car.Car).all()]
    model_ = request.match_info.get("model","")
    myList = []
    for i in resultCar:
        if i.model == model_.lower():
            for j in resultDriver:
                if j.id == i.driver_id:
                    driverDict = {"id":j.id,
                               "fullname":j.fullname}
                    myList.append(driverDict)
    return web.json_response(myList)

# update driver by id
@routes.put("/updateDriverById/{id}")
async def updateDriverById(request:web.Response)->web.Response:
    result = [i for i in session.query(driver.Driver).all()]
    id_ = request.match_info.get("id","")
    data = await request.json()
    fullname_ = data['fullname']
    myDict={}
    for i in result:
        if int(id_) == i.id:
            i.fullname = fullname_
            myDict = {"id":i.id,
                      "fullname":i.fullname}
    return web.json_response(myDict)

# delete car by id
@routes.delete("/deleteCarById/{id}")
async def deleteCarById(request:web.Response)->web.Response:
    result = [i for i in session.query(car.Car).all()]
    id_ = request.match_info.get("id","")
    for i in result:
        if i.id == int(id_):
            session.delete(i)
            session.commit()
    return web.Response(text=f"Car with id: {id_}, has been deleted")

# delete driver by id
@routes.delete("/deleteDriverById/{id}")
async def deleteDriverById(request:web.Response)->web.Response:
    result = [i for i in session.query(driver.Driver).all()]
    result1 = [j for j in session.query(car.Car).all()]
    id_ = request.match_info.get("id","")
    for i in result:
        if i.id == int(id_):
            for j in result1:
                if i.id == j.driver_id:
                    session.delete(j)
                    session.commit()
                    session.delete(i)
                    session.commit()
    return web.Response(text=f"Driver with id:{id_}, has been deleted!")

async def initApp()->web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app

web.run_app(initApp())