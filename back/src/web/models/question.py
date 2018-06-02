from peewee import *


class Question:
    id = PrimaryKeyField()
    subject = CharField()
    difficulty = IntegerField()
    content = CharField()


