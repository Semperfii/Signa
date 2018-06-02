from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request

from ..managers import NotificationManager
from ..config import logger


class Notifications(Resource):
    """
    Manage the notifications in the database
    """

    @jwt_required
    def get(self):
        me_id = get_jwt_identity()['id']
        match_manager = NotificationManager(me_id)
        logger.debug('Get on /notifications called.')
        return match_manager.get()


class Notification(Resource):
    """
    Manage an notification in the database
    """

    @jwt_required
    def delete(self, notification_id):
        me_id = get_jwt_identity()['id']
        match_manager = NotificationManager(me_id)
        logger.debug('Delete on /notification/:id called.')
        return match_manager.delete_notifications(notification_id)
