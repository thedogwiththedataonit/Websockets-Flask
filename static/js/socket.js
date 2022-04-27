var socket = io.connect("http://localhost:4000");
const testLabel = document.getElementById("testLabel");

socket.on('connect', function() {
        socket.emit('my event', {data: 'init connection'});

    });

socket.on('message', function(message) {
        console.log(message);
    });

socket.on("join", function(message) {
    console.log(message);
});

//every 3 seconds
/*
setInterval(function() {
    socket.send("hello");
    socket.emit('my event', {data: 'I\'m connected!'});
}, 3000);
*/



