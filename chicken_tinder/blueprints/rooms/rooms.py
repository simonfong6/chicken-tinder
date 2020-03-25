import json

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file
from flask import url_for


rooms = Blueprint(
    'rooms',
    __name__,
    template_folder='templates')


@rooms.route('/create', methods=['POST'])
def create():
    room = request.form['room']

    return redirect(url_for('rooms.show', room=room))


@rooms.route('/<room>')
def show(room):
    with open('blueprints/rooms/restaurants.json') as f:
        restaurants = json.load(f)

    context = {
        'room': room,
        'restaurants': restaurants['restaurants']
    }
    return render_template('room.html.jinja', **context)


@rooms.route('/restaurants')
def restaurants():

    return send_file('blueprints/rooms/restaurants.json')
