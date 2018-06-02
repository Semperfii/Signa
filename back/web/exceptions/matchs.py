from ..config import logger


class MatchError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        logger.critical('Match error : {}'.format(message))

    def to_dict(self):
        return {'error': self.message}
