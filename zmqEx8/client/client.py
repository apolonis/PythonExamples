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
    for request in range(10):
        print("Sending request %s …" % request)
        socket.send_string(myjson)

        #  Get the reply.
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request, message))