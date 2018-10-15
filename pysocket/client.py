# socket client. Receive a input from the user
# and send to the socket server

import zmq
import sys

# push json to the server with event name
def push(event, json_data=None):
    # get context
    context = zmq.Context()

    # socket to send message
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://0.0.0.0:5555")

    # set initial send dict
    data_dict = {
        'event': event
    }

    # if provide data
    if json_data is not None:
        data_dict['data'] = json_data

    # send json to server
    sender.send_json(data_dict)

# get message from promt to send to socket server
def get_message():
    print('Python socket client started')
    while True:
        # get message from user
        print('Enter message. enter exit() to close:')
        line = sys.stdin.readline().rstrip()

        # if user enter 'exit()' exit from loop
        if line == 'exit()':
            break

        # send event to socket server
        push('message', { 'data': line })

get_message()
