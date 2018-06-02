from peewee import IntegrityError, DoesNotExist
from playhouse.shortcuts import model_to_dict

from ..exceptions import *
from ..models import MatchNotification
from ..database import db


class NotificationManager:

    def __init__(self, user_id=None):
        self.db = db
        self.db.connect(reuse_if_open=True)
        MatchNotification.create_table(fail_silently=True)
        self.user_id = user_id

    def __del__(self):
        self.db.close()

    def get(self):
        match_notifications = []
        for notification in MatchNotification.select().where(MatchNotification.user == self.user_id):
            match_notifications.append(model_to_dict(notification))
        logger.debug('Get user {} notifications. Number of it : {}'.format(self.user_id, len(match_notifications)))
        return match_notifications

    def create_match_notification(self, match_id, players):
        with self.db.atomic():
            for player in players:
                try:
                    MatchNotification.create(user_id=player, match_id=match_id)
                except IntegrityError:
                    logger.critical('Notification for user {} for match {} already exists.'.format(player, match_id))

    def delete_notifications_tables(self):
        with self.db.atomic():
            MatchNotification.drop_table()

    def delete_notifications(self, notification_id):
        with self.db.atomic():
            try:
                match_notification = MatchNotification.get(MatchNotification.id == notification_id)
                logger.debug('Get notification {}. Response : {}'.format(id, match_notification))
                if match_notification.user_id != self.user_id:
                    raise MatchError('This notification is not for you.')
                match_notification.delete_instance()
            except DoesNotExist:
                raise MatchError('Can\'t delete notification.')
