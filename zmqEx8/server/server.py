import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    # print("Recived request: %s" % message)
    time.sleep(1)
    socket.send(b"Server sent: message recived!")
   
    myDict = message.decode()
    # print(myDict)
    # print(type(myDict))

    res = json.loads(myDict)
    print(res)
    


    