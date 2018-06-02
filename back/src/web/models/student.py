from peewee import *

from .classe import Classe


class Student:
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    classe = ForeignKeyField(Classe)

    def get_data(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "class": self.classe.get_data()}


