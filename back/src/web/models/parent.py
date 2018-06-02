from peewee import *

from .student import Student


class Parent:
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()

    def get_data(self):
        return {"id": self.id, "name": self.name, "surname": self.surname}