from peewee import *

from web.database import db


class ResultDuel:
    id_student_1 = IntegerField()
    id_student_2 = IntegerField()
    score_1 = IntegerField()
    score_2 = IntegerField()
    id_question = IntegerField()

    class Meta:
        database = db
