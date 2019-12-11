import zmq
import json

myDict = {"mykey":"myValue"}
myjson = json.dumps(myDict)

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Sending request %s …" % request)
    socket.send_string(myjson)

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))