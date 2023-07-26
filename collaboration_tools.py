```python
import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Collaboration Tools Service"

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send({"message": f"{username} has joined the room."}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send({"message": f"{username} has left the room."}, room=room)

@socketio.on('message')
def handle_message(data):
    send({"message": data['message']}, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
```