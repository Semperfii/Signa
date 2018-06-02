from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from ..managers import StudentsManager
from ..config import logger


class Students(Resource):
    """
    Manage the students in the database
    """

    @jwt_required
    def get(self):
        """
        Get the list of students in signa
        :return: list of students
        """
        search = request.args.get('search', None)
        studentsManager = StudentsManager()
        students = studentsManager.get_all(search=search, max=max)
        logger.debug('Get on /students called. Search : {}.'.format(search))
        return students


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
        logger.debug('Get on /students/:id called.')
        userManager = StudentsManager()
        return userManager.get(user_id)
