import zmq
import time

def connect():
    context = zmq.Context()
    print("Client is trying to connect to server...")
    time.sleep(2)

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print("Client succesfully connected to server!")
    time.sleep(2)
    return socket

def send(myjson, socket):
    while True:
        print("Client is trying to send a message...")
        time.sleep(2)
        socket.send_string(myjson)
        print("Message sent!")
        time.sleep(2)
        print("Client is trying to recive a message...")
        time.sleep(2)
        message = socket.recv()
        print("Message recived: ",message)

