from flask import Blueprint, jsonify

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'hello': 'world',
    })
