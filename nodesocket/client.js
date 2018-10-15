// socket client subscribe in the port 5556 to
// listen event message

var zeromq = require('zeromq');

// run socket client
console.log("Node socket client listening socket server on 5556 (PUBLISHER)");

// Socket to talk to server
var subscriber = zeromq.socket('sub');

// get message from publisher event
subscriber.on('message', function(topic, data=null) {
  // parse event name to string
  const eventName = topic.toString();
  // parse data object is exists
  const dataObj = data ? JSON.parse(data) : {};

  // print
  console.log('Message from publisher received:')
  console.log('Event:', eventName);
  console.log('Data:', dataObj);
  console.log('----');
});

// conect to publisher
subscriber.connect(`tcp://0.0.0.0:5556`);
// subscribe to event
subscriber.subscribe('message');