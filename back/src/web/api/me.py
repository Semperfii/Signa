from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..managers.users import UsersManager


@jwt_required
def me():
    me_id = get_jwt_identity()['id']
    manager = UsersManager()
    return jsonify(manager.get(me_id))
