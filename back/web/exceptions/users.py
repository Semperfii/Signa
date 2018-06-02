from ..config import logger


class UserError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        logger.critical('User error : {}'.format(message))

    def to_dict(self):
        return {'error': self.message}


class UserAlreadyRegistered(UserError):
    def __init__(self):
        UserError.__init__(self, 'This user is already registered.')


class UserNotExisting(UserError):
    def __init__(self):
        UserError.__init__(self, 'This user is not existing.')


class BadEmail(UserError):
    def __init__(self):
        UserError.__init__(self, 'This email is not correct.')


class UserNotAdmin(UserError):
    def __init__(self):
        UserError.__init__(self, 'This user has no right to do this.', 403)


class NotConnected(UserError):
    def __init__(self):
        UserError.__init__(self, 'You are not connected', 403)
