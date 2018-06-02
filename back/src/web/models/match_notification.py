from peewee import *

from .user import User
from .match import Match
from ..database import db


class MatchNotification(Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User, backref='notifications')
    match = ForeignKeyField(Match, backref='notifications')

    class Meta:
        database = db
