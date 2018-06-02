import json
import logging
import os
from datetime import timedelta

from util import DateTimeEncoder

config = json.load(open(os.environ.get('CONFIG_FILE', './config/config.json')))


class FlaskConfig(object):
    DEBUG = config['flask'].get('debug', False)
    SECRET_KEY = config['flask'].get('oauth_secret', False)
    JWT_SECRET_KEY = config['flask'].get('jwt_secret', False)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=config['flask'].get('jwt_expiration', 900))
    RESTFUL_JSON = {'separators': (', ', ': '),
                    'indent': 2,
                    'cls': DateTimeEncoder}


flask_config = FlaskConfig

logger = logging.getLogger()
formatter = logging.Formatter('%(process)d %(asctime)s %(name)-12s %(levelname)-8s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

if not os.path.exists('../volumes/logs'):
    os.makedirs('../volumes//logs')
file_handler = logging.FileHandler('../volumes//logs/signa.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

log_level = config.get('log', 'INFO')
if log_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger = logging.getLogger('signa')

version = '0.1.0'
