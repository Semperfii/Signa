from flask import Blueprint
from flask_restful import Api

from .me import me
from .users import Users, User
from .matchs import Matchs, Match
from .notifications import Notifications, Notification
from ..config import logger

api_bp = Blueprint('api', __name__)


def register_api(app):
    api = Api(api_bp)
    api.add_resource(Users, '/users')
    api.add_resource(User, '/users/<user_id>')
    api.add_resource(Matchs, '/matchs')
    api.add_resource(Match, '/matchs/<match_id>')
    api.add_resource(Notifications, '/notifications')
    api.add_resource(Notification, '/notifications/<notification_id>')
    api_bp.add_url_rule('/me', 'me', me)

    app.register_blueprint(api_bp, url_prefix="/api/v1")

    logger.debug('Blueprints successfully registered.')
