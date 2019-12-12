import json
from client import client

my_dict = {"Message":"Hey from client"}

myjson = json.dumps(my_dict)

socket = client.connect()
client.send(myjson,socket)