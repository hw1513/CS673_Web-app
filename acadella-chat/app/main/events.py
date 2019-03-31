import time
from flask import session, request
from flask_socketio import emit, join_room, leave_room
from collections import deque
from .. import socketio


#TODO: switch over to using database versus local memory
USERS = {}
ROOMS = {"Enterprise": deque([], maxlen=50)}


@socketio.on('joined')
def connection(message):
    """Message sent when a new member enters a room.
    This message is pushed out to all members in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('create channel')
def new_channel(data):
    if data['name'] in ROOMS:
        return False
    else:
        ROOMS[data['name']] = deque(maxlen=100)
        emit('create channel', {"name": data['name']}, broadcast=True)


@socketio.on('userdata')
def user_data(data):
    if 'username' in data:
        USERS[data['username']] = request.sid


@socketio.on('new msg')
def new_msg(data):
    """
    Sends a message in the channel with a time stamp.
    The message is sent out to all members of the channel.
    :param data:
    """
    if 'channel' in data:
        data['created_at'] = int(time.time())
        ROOMS[data['channel']].append(data)
        emit('msg', data, broadcast=True)


@socketio.on('get channels')
def get_channels():
    emit('channels', list(ROOMS.keys()))


@socketio.on('get msgs')
def get_msgs(data):
    if 'name' in data:
        emit('msgs', list(ROOMS[data['name']]))
