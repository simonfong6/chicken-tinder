#!/usr/bin/env python3
"""
Handles matching swipes.
"""
import logging
import sys
from collections import defaultdict


from flask import Flask
from flask import render_template
from flask import request
from flask_socketio import emit
from flask_socketio import join_room
from flask_socketio import SocketIO


from chicken_tinder.blueprints.rooms.rooms import rooms
from chicken_tinder.models.restaurant_room import RestaurantRoom


logger = logging.getLogger(__name__)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'


app.register_blueprint(rooms, url_prefix='/rooms')

socketio = SocketIO(app)


restaurant_rooms = defaultdict(RestaurantRoom)


@app.route('/')
def index():
    return render_template('index.html.jinja')


@socketio.on('joined', namespace='/matches')
def joined(message):
    """When someone joins a room."""
    room = message['room']

    join_room(room)

    emit('status', {'msg': f'Joined the room: {room}'}, room=room)

    reset(message)


@socketio.on('reset', namespace='/matches')
def reset(message):
    """Reset a room."""
    room = message['room']

    restaurant_room = restaurant_rooms[room]

    restaurant_room.reset()

    # Reset the other clients.
    emit('reset-client', room=room)

    emit('count-request', {}, room=room)

    logger.debug("Reset received")


@socketio.on('count', namespace='/matches')
def count(message):
    """Counts client in a room."""
    room = message['room']

    restaurant_room = restaurant_rooms[room]

    restaurant_room.increment_clients_count()

    emit(
        'client-count',
        {'client_count': restaurant_room.clients_count},
        room=room)

    logger.debug(f"Clients count: {restaurant_room.clients_count}")


@socketio.on('accept', namespace='/matches')
def accept(message):
    """When someone leaves a room."""
    room = message['room']
    restaurant_id = message['id']

    restaurant_room = restaurant_rooms[room]

     # Update restaurant accept count.
    restaurant_room.add_hit(restaurant_id)

    if restaurant_room.is_match(restaurant_id):
        emit('match-found', {'matched': restaurant_id}, room=room)


def main(args):

    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

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
