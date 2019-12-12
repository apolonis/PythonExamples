import json
from model import user
from client import client

userObj = user.User("David","Beckham","Bang it like Beckham")
# commented lines are to send 2nd user to server
 
# userObj1 = user.User("Viktorija","Beckham","Dave what up")

myDict = {"name":userObj.name,
            "lastname":userObj.lastname,
            "message":userObj.message}
# myDict1 = {"name":userObj1.name,
#             "lastname":userObj1.lastname,
#             "message":userObj1.message}

myjson = json.dumps(myDict)
# myjson1 = json.dumps(myDict1)

socket = client.connecting()

client.sendingMessage(myjson,socket)
# client.sendingMessage(myjson1,socket)


