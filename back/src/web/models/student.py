from peewee import *

from ..models import User
from .classe import Classe


class Student(User):
    classe = ForeignKeyField(Classe)
    score = {"Maths": 0,
             "Histoire": 0,
             "Physique": 0}
    xp = FloatField()

    type = 0

    def get_data(self):
        dict = super(Student, self).get_data()
        dict["class"] = self.classe.get_data()
        return dict


Student.create_table(fail_silently=True)
