#!/usr/bin/env python3
"""
Handles matching swipes.
"""

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


@app.route('/')
def index():
    return render_template('index.html.jinja')


@socketio.on('joined', namespace='/matches')
def joined(message):
    """When someone joins a room."""
    room = message['room']
    join_room(room)
    emit('status', {'msg': f'Joined the room: {room}'}, room=room)


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
