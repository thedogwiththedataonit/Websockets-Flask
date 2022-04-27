from flask import Flask, render_template, redirect, request, url_for, jsonify
import pymongo
from pymongo import MongoClient
import certifi
import re
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit, join_room, leave_room, close_room, rooms, disconnect

application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application, cors_allowed_origins="*")
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'


@application.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    message = ('received message: ' + data)
    print("message")
    send(message, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print("connected")


@socketio.on('json')
def handle_json(json):
    message = ('received json: ' + str(json))
    print("json")
    send(message, broadcast=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    message = ('received json: ' + str(json))
    print("my event")
    send(message, broadcast=True)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    currentrooms = rooms()
    print(currentrooms)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


if __name__ == "__main__":
    socketio.run(application, debug=True, port=4000)