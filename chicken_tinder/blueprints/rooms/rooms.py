from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import send_file

rooms = Blueprint(
    'rooms',
    __name__,
    template_folder='templates')

@rooms.route('/<room>')
def show(room):
    context = {
        'name': room
    }
    return render_template('room.html.jinja', **context)

@rooms.route('/restaurants')
def restaurants():

    return send_file('blueprints/rooms/restaurants.json')
