from flask import Blueprint

rooms = Blueprint(
    'rooms',
    __name__,
    template_folder='templates')

@rooms.route('/<room>')
def show(room):
    return room
