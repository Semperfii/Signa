from peewee import *


class Result:
    id_student = IntegerField()
    id_question = IntegerField()
    outcome = BooleanField()
    time = TimeField()
