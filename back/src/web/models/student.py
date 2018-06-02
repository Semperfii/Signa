from peewee import *

from ..models import User
from .classe import Classe


class Student(User):
    classe = ForeignKeyField(Classe)
    score = FloatField()
    xp = FloatField()

    type = 0

    def get_data(self):
        dict = super.get_data()
        dict["class"] = self.classe
        return dict



