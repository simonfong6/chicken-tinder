#!/usr/bin/env python3
"""
Simple chat app.
"""

from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

socketio = SocketIO(app)


@app.route('/')
def index():
    return 'hello'


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
