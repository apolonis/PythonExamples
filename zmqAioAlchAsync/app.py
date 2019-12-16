import json
from model import user
from client import client

user_obj = user.User("David", "Beckham")

my_dict = {"name":user_obj.name,
            "lastname":user_obj.lastname}

my_json = json.dumps(my_dict)
socket = client.connect()
client.send(my_json,socket)

  