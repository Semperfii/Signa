from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required
def me():
    me_id = get_jwt_identity()
    return jsonify(me_id)
