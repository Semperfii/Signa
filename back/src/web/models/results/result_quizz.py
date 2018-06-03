from peewee import *

from web.database import db


class ResultQuizz(Model):
    id_student = IntegerField()
    id_question = IntegerField()
    outcome = BooleanField()

    class Meta:
        database = db


ResultQuizz.create_table(fail_silently=True)
