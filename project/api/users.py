from flask import Blueprint, jsonify, request
from project.api.models import User
from project import db

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'hello': 'world',
    })


@users_blueprint.route('/post_user', methods=['POST'])
def post_user():
    post_data = request.get_json()
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')

    db.session.add(User(username=username, email=email, password=password))
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': f'{username} was added!'
    }
    return jsonify(response_object), 201
