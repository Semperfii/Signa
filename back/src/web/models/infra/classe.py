from peewee import *

from .school import School
from web.database import db


class Classe(Model):
    id = PrimaryKeyField()
    name = CharField()
    school = ForeignKeyField(School)

    def get_data(self):
        return {"id": self.id, "name": self.name, "school": self.school.get_data()}

    class Meta:
        database = db

Classe.create_table(fail_silently=True)
