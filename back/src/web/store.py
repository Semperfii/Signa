import json
import redis

from .config import config


class Store:
    def __init__(self):
        self.redis_db = redis.StrictRedis(host=config['redis'].get('host', 'localhost'), port=6379, db=0)

    def set_subjects(self, user_id, subjects):
        self.redis_db.set('subjects_{}'.format(user_id), json.dumps(subjects))

    def get_subjects(self, user_id):
        subjects = self.redis_db.get('subjects_{}'.format(user_id))
        if subjects is not None:
            return json.loads(subjects)
        else:
            return None

    def remove_subjects(self, user_id):
        self.redis_db.delete('subjects_{}'.format(user_id))