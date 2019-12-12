import json
from client import client

myDict = {"Message":"Hey from client"}

myjson = json.dumps(myDict)

socket = client.connectingToServer()
client.sendingMessage(myjson,socket)