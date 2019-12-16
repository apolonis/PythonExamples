import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

count = 0

while True:
    while True:
        my_dict = {count:count}
        my_json = json.dumps(my_dict)
        print("Client is trying to send a message...")
        time.sleep(2)
        socket.send_string(my_json)
        print("Message sent!")
        time.sleep(2)
        print("Client is trying to recive a message...")
        time.sleep(2)
        message = socket.recv()
        print("Message recived: ",message)
        count = count + 1