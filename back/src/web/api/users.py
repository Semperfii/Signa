from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from ..managers import UsersManager
from ..config import logger


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
        userManager = UsersManager()
        users = userManager.get_all(search=search, max=max)
        logger.debug('Get on /users called. Search : {}.'.format(search))
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
