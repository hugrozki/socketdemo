## Socket Demo with zeromq


Console demo of a communication with sockets in two languages. Python client (emiter) send a message to a python server and this broadcast the message to javascript client (receiver).


### Installation

Install [zeromq](http://zeromq.org/). Nodesocket use [zeromq.js](https://github.com/zeromq/zeromq.js/) and pysocket use [pyzmq](https://github.com/zeromq/pyzmq) follow the instructions on each link to install the binders.


### Run demo

***Client (receiver)***

In console, go to nodesocket folder and run client.js

```
node client
```


***Socket server and client (emiter)***

In the console, go to pysocket and run server.py

```
python server.py
```


then run client.py

```
python client.py
```


In client window you see a message

```
Python socket client started
Enter message. enter exit() to close:
```

Enter a message and pulse Return key. The message is send to the python socket server and this broadcast to the listener clients. You can see in the javascript client window:

```
Message from publisher received:
Event: message
Data: { data: 'sendedmessage' }
----
```