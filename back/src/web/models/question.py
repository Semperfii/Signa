from peewee import *
from ..database import db


class Question:
    id = PrimaryKeyField()
    subject = CharField()
    difficulty = IntegerField()
    content = CharField()

    class Meta:
        database = db


