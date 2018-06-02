from peewee import *
from ..database import db


class ResultQuizz:
    id_student = IntegerField()
    id_question = IntegerField()
    outcome = BooleanField()

    class Meta:
        database = db