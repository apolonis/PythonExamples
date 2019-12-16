import zmq
import json
import time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

while True:
    print("Server is trying to recive a message...")
    time.sleep(2)
    
    message = socket.recv()
    
    print(message)
    
    print("Server has recived a message!")
    time.sleep(2)
    print("Received message: ", message)

    myd = message.decode()
    result = json.loads(myd)
    time.sleep(2)
    socket.send(message)
    print("Server's result is: ",result)