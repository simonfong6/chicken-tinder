from flask import Blueprint
from flask import jsonify
from flask import send_file

rooms = Blueprint(
    'rooms',
    __name__,
    template_folder='templates')

@rooms.route('/<room>')
def show(room):
    return room

@rooms.route('/restaurants')
def restaurants():

    return send_file('blueprints/rooms/restaurants.json')
