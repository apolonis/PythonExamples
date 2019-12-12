import zmq
# import json

# import sys
# sys.path.append('...')

def connecting():
    context = zmq.Context()
    print("Connecting to hello world server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    return socket


def sendingMessage(myjson, socket):
    # for request in range(10):
    while True:
        # print("Sending request %s …" % request)
        socket.send_string(myjson)
        flag = 1
        if flag == 1: 
        #  Get the reply.
            message = socket.recv()
            flag = 0
            print(message)
        # print("Received reply %s [ %s ]" % (request, message))
        