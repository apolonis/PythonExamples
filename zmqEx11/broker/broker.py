import zmq
import umsgpack
import json

context = zmq.Context()
frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

while True:
    
    message = frontend.recv_multipart()
    print(message)
                      
    backend.send_multipart(message)

    message = backend.recv_multipart()
    
    frontend.send_multipart(message)

# frontend.close()
# backend.close()
# context.term()

