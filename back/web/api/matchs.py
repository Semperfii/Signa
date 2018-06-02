from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request

from ..managers.matchs import MatchsManager
from ..config import logger


class Matchs(Resource):
    """
    Manage the matchs in the database
    """

    @jwt_required
    def get(self):
        """
        Get the list of matchs in signa
        :return: list of matchs
        """
        me_id = get_jwt_identity()['id']
        match_manager = MatchsManager(me_id)
        logger.debug('Get on /matchs called.')
        return match_manager.get_all()

    @jwt_required
    def put(self):
        """
        Put a in signa
        :return: message
        """
        me_id = get_jwt_identity()['id']
        match_manager = MatchsManager(me_id)
        body = request.get_json()
        match_manager.add_match(body)
        logger.debug('Put on /matchs called. Body : {}'.format(body))
        return {'msg': 'success'}


class Match(Resource):
    """
    Manage an match in the database
    """

    @jwt_required
    def get(self, match_id):
        """
        Get an match by its id
        :return: the match demanded
        """
        me_id = get_jwt_identity()['id']
        match_manager = MatchsManager(me_id)
        logger.debug('Get on /matchs/:id called.')
        return match_manager.get(match_id)

    @jwt_required
    def post(self, match_id):
        """
        Get an match by its id
        :return: the match demanded
        """
        me_id = get_jwt_identity()['id']
        match_manager = MatchsManager(me_id)
        body = request.get_json()
        if body is None:
            return {'msg': 'no action'}, 400
        contestation = body.get('contestation', False)
        logger.debug('Post on /matchs/:id called. Contestation : {}'.format(contestation))
        if contestation:
            return match_manager.contest_match(match_id)
        else:
            return {'msg': 'nothing to do'}
