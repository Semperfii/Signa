from flask import Blueprint
from flask_restful import Api

from .me import me
from .students import Students, User
from .question import Questions
from ..config import logger

api_bp = Blueprint('api', __name__)


def register_api(app):
    api = Api(api_bp)
    api.add_resource(Students, '/students')
    api.add_resource(User, '/students/<user_id>')
    api.add_resource(Questions, '/questions/<question_id>')
    api_bp.add_url_rule('/me', 'me', me)

    app.register_blueprint(api_bp, url_prefix="/api/v1")

    logger.debug('Blueprints successfully registered.')
