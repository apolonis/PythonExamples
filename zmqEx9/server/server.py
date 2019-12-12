import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    print("Server is trying to recive a message...")
    time.sleep(2)
    message = socket.recv()
    print("Server has recived a message!")
    time.sleep(2)

    socket.send(b"Server has responed with a message: 'message recived'")
    time.sleep(2)

    my_dict = message.decode()
    result = json.loads(my_dict)
    print("Server has recived result from client: ",result)