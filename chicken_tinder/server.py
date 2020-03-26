#!/usr/bin/env python3
"""
Handles matching swipes.
"""
from collections import Counter


from flask import Flask
from flask import render_template
from flask_socketio import emit
from flask_socketio import join_room
from flask_socketio import SocketIO


from chicken_tinder.blueprints.rooms.rooms import rooms


app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'


app.register_blueprint(rooms, url_prefix='/rooms')

socketio = SocketIO(app)


connected_count = 0

restaurant_counts = Counter()


@app.route('/')
def index():
    return render_template('index.html.jinja')


@socketio.on('joined', namespace='/matches')
def joined(message):
    """When someone joins a room."""
    global connected_count
    connected_count += 1

    room = message['room']
    join_room(room)
    emit('status', {'msg': f'Joined the room: {room} Count: {connected_count}'}, room=room)


@socketio.on('disconnect', namespace='/matches')
def disconnect():
    """When someone leaves a room."""
    global connected_count
    connected_count -= 1


@socketio.on('accept', namespace='/matches')
def accept(message):
    """When someone leaves a room."""
    global connected_count
    global restaurant_counts

    room = message['room']
    restaurant_id = message['id']

    # Update restaurant accept count.
    restaurant_counts[restaurant_id] += 1

    restaurant_count = restaurant_counts[restaurant_id]

    # Check if the count is accepted by all members.
    if restaurant_count == connected_count:
        # We found a restaurant that everyone agrees on, tell everyone.
        emit('match-found', {'matched': restaurant_id}, room=room)


def main(args):

    socketio.run(
        app,
        host='0.0.0.0',
        debug=args.debug,
        port=args.port
    )


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-p', '--port',
                        help="Port that the server will run on.",
                        type=int,
                        default=7777)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False,
                        action='store_true')

    args = parser.parse_args()
    main(args)
