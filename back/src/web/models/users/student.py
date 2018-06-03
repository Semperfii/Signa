import json
from peewee import *

from web.models.infra.classe import Classe
from .user import User


class Student(User):
    classe = ForeignKeyField(Classe)
    score = CharField()
    xp = FloatField()

    type = 0

    def get_data(self):
        dict = super(Student, self).get_data()
        dict["class"] = self.classe.get_data()
        dict["score"] = json.loads(self.score)
        return dict


Student.create_table(fail_silently=True)
