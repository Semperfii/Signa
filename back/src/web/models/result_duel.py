from peewee import *
from ..database import db


class ResultDuel:
    id_student_1 = IntegerField()
    id_student_2 = IntegerField()
    score_1 = IntegerField()
    score_2 = IntegerField()

    class Meta:
        database = db
