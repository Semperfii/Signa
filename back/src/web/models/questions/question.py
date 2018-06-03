from peewee import *

from web.database import db


class Question(Model):
    id = PrimaryKeyField()
    subject = CharField()
    difficulty = IntegerField()
    content = CharField()
    proposition_1 = CharField()
    proposition_2 = CharField()
    proposition_3 = CharField()
    proposition_4 = CharField()

    class Meta:
        database = db


Question.create_table(fail_silently=True)
