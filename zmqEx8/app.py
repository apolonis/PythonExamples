import json
from model import user
from client import client

userObj = user.User("David","Beckham","Bang it like Beckham")

myDict = {"name":userObj.name,
            "lastname":userObj.lastname,
            "message":userObj.message}
myjson = json.dumps(myDict)

socket = client.connecting()

client.sendingMessage(myjson,socket)