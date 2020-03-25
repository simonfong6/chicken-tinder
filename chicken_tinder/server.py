#!/usr/bin/env python3
"""
Handles matching swipes.
"""

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import url_for


from chicken_tinder.blueprints.rooms.rooms import rooms


app = Flask(__name__)
app.register_blueprint(rooms)


@app.route('/')
def index():
    return render_template('index.html.jinja')


def main(args):

    app.run(
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
