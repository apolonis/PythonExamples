import zmq
import time

def connectingToServer():
    context = zmq.Context()
    print("Client is trying to connect to server...")
    time.sleep(2)
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    print("Succesfully connected to server!")
    time.sleep(2)
    return socket

def sendingMessage(myjson, socket):
    while True:
        print("Clien is trying to send a message...")
        time.sleep(2)
        socket.send_string(myjson)
        print("Message sent!")
        time.sleep(2)
        flag = 1
        if flag == 1:
            print("Client is trying to recive a message...")
            time.sleep(2)
            message = socket.recv()
            flag = 0
            print("Message recived: ",message)
