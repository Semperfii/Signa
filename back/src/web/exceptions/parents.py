from ..config import logger


class ParentError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        logger.critical('Parent error : {}'.format(message))

    def to_dict(self):
        return {'error': self.message}


class ParentAlreadyRegistered(ParentError):
    def __init__(self):
        ParentError.__init__(self, 'This parent is already registered.')


class ParentNotExisting(ParentError):
    def __init__(self):
        ParentError.__init__(self, 'This parent does not exist.')