from peewee import *

from ..database import db
from .user import User


class Match(Model):
    id = PrimaryKeyField()
    playerA = ForeignKeyField(User)
    playerB = ForeignKeyField(User)
    playerC = ForeignKeyField(User)
    playerD = ForeignKeyField(User)
    scoreAB = IntegerField()
    scoreCD = IntegerField()
    issuer = ForeignKeyField(User)
    date = DateTimeField()
    contested = BooleanField()

    class Meta:
        database = db

