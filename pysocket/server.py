# socket server. Receive a message from a sender client
# and broadcast the message to listener clients

# Binds PULL in tcp://*:5555
# Binds PUBLISHER in tcp://*:5556

import zmq
import json

def run():
    # get context of zeromq
    context = zmq.Context()

    # set receiver socket
    receiver = context.socket(zmq.PULL)
    receiver.bind('tcp://*:5555')

    # set publisher socket
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5556")

    print("Python socket server started in ports 5555 (receiver) and 5556 (publisher)")

    while True:
        #  Wait for next request from client
        # get dictionary of values key 'event', 'data'
        data_dict = receiver.recv_json()

        print("Received request: ", data_dict)

        # create string to return
        response = [data_dict['event'].encode()]

        # search data key in dictionary
        if 'data' in data_dict:
            response.append(json.dumps(data_dict['data'], ensure_ascii=False).encode())

        # broadcast event string message
        print("Broadcast event string message\n ---")
        publisher.send_multipart(response)

run()
