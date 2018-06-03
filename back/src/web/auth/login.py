from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_refresh_token_required

from ..exceptions import *
from ..managers import TeachersManager, StudentsManager


def teacher_only(func):
    def success(user):
        me = get_jwt_identity()
        if me and me['admin']:
            return func(user)
        else:
            raise NotATeacher

    return success


def create_auth(app):
    jwt = JWTManager(app)
    auth_bp = Blueprint('login', __name__)

    @auth_bp.errorhandler(UsersError)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @auth_bp.route('/refresh', methods=['POST'])
    @jwt_refresh_token_required
    def refresh():
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token), 200

    @auth_bp.route('/login', methods=['POST'])
    def login():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)
        if not email:
            return jsonify({"msg": "Missing email parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        user = None

        teacher_manager = TeachersManager()
        teacher = teacher_manager.check_user_auth(email, password)
        if teacher is not None:
            user = teacher

        student_manager = StudentsManager()
        student = student_manager.check_user_auth(email, password)
        if student is not None:
            user = student

        if user is None:
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token), 200

    app.register_blueprint(auth_bp, url_prefix="/auth")
