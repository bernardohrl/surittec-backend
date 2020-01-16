from flask import Blueprint, jsonify

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users/list', methods=['GET'])
def list_users():
    return jsonify({
        'lista': 'usuarios',
    })
