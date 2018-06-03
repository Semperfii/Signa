from peewee import *

from web.database import db


class Question(Model):
    id = PrimaryKeyField()
    subject = CharField()
    difficulty = IntegerField()
    content = CharField()
    propositions_1 = CharField()
    propositions_2 = CharField()
    propositions_3 = CharField()
    propositions_4 = CharField()

    class Meta:
        database = db


Question.create_table(fail_silently=True)
