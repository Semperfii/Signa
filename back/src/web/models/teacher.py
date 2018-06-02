from peewee import *
from ..database import db


class Teacher:
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    subject = CharField()

    def get_data(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "subject": self.subject}

    class Meta:
        database = db