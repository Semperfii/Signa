from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from web.managers import StudentsManager


@jwt_required
def me():
    me_id = get_jwt_identity()['id']
    students_manager = StudentsManager()
    me = students_manager.get(me_id)
    return jsonify(me)
