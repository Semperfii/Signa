from web.exceptions import UsersError
from ..config import logger


class TeacherError(UsersError):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        logger.critical('Teacher error : {}'.format(message))

    def to_dict(self):
        return {'error': self.message}


class TeacherAlreadyRegistered(TeacherError):
    def __init__(self):
        TeacherError.__init__(self, 'This teacher is already registered.')


class TeacherNotExisting(TeacherError):
    def __init__(self):
        TeacherError.__init__(self, 'This teacher does not exist.')


class NotATeacher(TeacherError):
    def __init__(self):
        TeacherError.__init__(self, 'Vous n\'êtes pas un prof !')
