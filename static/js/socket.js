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


/*
setInterval(function() {
    socket.send("hello");
    socket.emit('my event', {data: 'I\'m connected!'});
}, 3000);
*/

//send a message on button click
document.getElementById("send").onclick = function() {
    socket.send("hello");
}

document.getElementById("emit").onclick = function() {
    socket.emit('json', {data: 'button pressed'});
}


