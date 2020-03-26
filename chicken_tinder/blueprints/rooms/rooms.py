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

    empty_restaurant = {
        'id': -1,
        'name': 'No more restaurants near you :(',
        'image': 'https://image-share-public.s3-us-west-2.amazonaws.com/test/8f560335-16a1-4062-ad31-35046cf1fc5b.png'
    }

    context = {
        'room': room,
        'restaurants': restaurants['restaurants'],
        'empty_restaurant': empty_restaurant
    }
    return render_template('room.html.jinja', **context)


@rooms.route('/restaurants')
def restaurants():

    return send_file('blueprints/rooms/restaurants.json')
