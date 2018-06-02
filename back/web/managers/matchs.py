import datetime
from peewee import IntegrityError, DoesNotExist

from ..exceptions import *
from ..models import Match
from .notifications import NotificationManager
from ..database import db


class MatchsManager:
    MANDATORY_FIELDS = ['playerA', 'playerB', 'playerC', 'playerD', 'scoreAB', 'scoreCD']

    def __init__(self, user_id=None):
        self.db = db
        self.db.connect(reuse_if_open=True)
        Match.create_table(fail_silently=True)
        self.user_id = user_id

    def __del__(self):
        self.db.close()

    def get_all(self):
        matchs_list = []
        for match in Match.select().dicts():
            matchs_list.append(match)
        logger.debug('Get all matchs from db. Number of matchs : {}'.format(len(matchs_list)))
        return matchs_list

    def get(self, id):
        try:
            match = Match.get(Match.id == id)
            logger.debug('Get {} match. Response : {}'.format(id, match))
            return match.get_data()
        except DoesNotExist:
            raise MatchError('Get not possible.')

    def add_match(self, body):
        for field in self.MANDATORY_FIELDS:
            if field not in body.keys():
                raise MatchError('{} is missing from body.'.format(field))

        if 'date' not in body.keys():
            body['date'] = datetime.datetime.now()
        with self.db.atomic():
            try:
                match = Match.create(
                    playerA=body['playerA'],
                    playerB=body['playerB'],
                    playerC=body['playerC'],
                    playerD=body['playerD'],
                    issuer=self.user_id,
                    scoreAB=body['scoreAB'],
                    scoreCD=body['scoreCD'],
                    contested=False,
                    date=body['date']
                )
                notication_manager = NotificationManager(user_id=self.user_id)
                players = [body['playerB'], body['playerC'], body['playerD']]
                notication_manager.create_match_notification(match.id, players)
                return match
            except IntegrityError:
                raise MatchError('Match already created.')

    def delete_matches_table(self):
        with self.db.atomic():
            Match.drop_table()

    def delete_matches(self, match_id):
        with self.db.atomic():
            try:
                match = Match.get(Match.id == match_id)
                logger.debug('Get match {}. Response : {}'.format(match_id, match))
                match.delete_instance()
            except DoesNotExist:
                raise MatchError('Can\'t delete match.')

    def contest_match(self, match_id):
        with self.db.atomic():
            try:
                match = Match.get(Match.id == match_id)
                logger.debug('Get match {}. Response : {}'.format(match_id, match))
                match.contested = True
                match.save()
            except DoesNotExist:
                raise MatchError('Can\'t contest match.')
