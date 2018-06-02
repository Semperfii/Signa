from flask import Blueprint
from flask_restful import Api

from .me import me
from .users import Users, User
from ..config import logger

api_bp = Blueprint('api', __name__)


def register_api(app):
    api = Api(api_bp)
    api.add_resource(Users, '/users')
    api.add_resource(User, '/users/<user_id>')
    api_bp.add_url_rule('/me', 'me', me)

    app.register_blueprint(api_bp, url_prefix="/api/v1")

    logger.debug('Blueprints successfully registered.')
