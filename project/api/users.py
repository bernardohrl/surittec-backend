from flask import Blueprint, jsonify, request
from project.api.models import User
from project import db
from sqlalchemy import exc
import psycopg2


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'hello': 'world',
    })


@users_blueprint.route('/post_user', methods=['POST'])
def post_user():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid payload.'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    try:
        user = User.query.filter_by(username=username).first()

        if not user:
            db.session.add(User(username=username, email=email, password=password))
            db.session.commit()
            return jsonify({ 'message': f'{username} was added!' }), 201
        else:
            return jsonify({ 'message': 'Sorry. That username already exists.' }), 400

    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify({'message': 'Invalid payload.', 'error': str(e)}), 400



@users_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({ 'message': 'User does not exist.' }), 404

        response_object = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        return jsonify(response_object), 200

    except exc.DataError as e:
        return jsonify({ 'message': 'User does not exist.', 'error': str(e) }), 404



@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    return jsonify( [user.to_json() for user in User.query.all()] ), 200
