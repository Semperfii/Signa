from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from ..managers import UsersManager, MatchsManager
from ..config import logger
from ..compute.scoring import compute_scoring


class Users(Resource):
    """
    Manage the users in the database
    """

    @jwt_required
    def get(self):
        """
        Get the list of users in signa
        :return: list of users
        """
        search = request.args.get('search', None)
        score = request.args.get('score', False)
        max = request.args.get('max', None)
        userManager = UsersManager()
        users = userManager.get_all(search=search, max=max)
        if score:
            match_manager = MatchsManager()
            users = compute_scoring(users, match_manager.get_all())
        logger.debug('Get on /users called. Search : {}. Score : {}'.format(search, score))
        return users


class User(Resource):
    """
    Manage an user in the database
    """

    @jwt_required
    def get(self, user_id):
        """
        Get an user by its id
        :return: the user demanded
        """
        logger.debug('Get on /users/:id called.')
        userManager = UsersManager()
        return userManager.get(user_id)
