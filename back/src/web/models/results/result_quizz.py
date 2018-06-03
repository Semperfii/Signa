from peewee import *

from web.database import db
from ..questions import Question


class ResultQuizz(Model):
    id = PrimaryKeyField()
    id_student = IntegerField()
    question = ForeignKeyField(Question)
    outcome = BooleanField()

    class Meta:
        database = db


ResultQuizz.create_table(fail_silently=True)
