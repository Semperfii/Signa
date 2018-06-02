from peewee import *

from .school import School


class Classe(Model):
    id = PrimaryKeyField()
    grade = IntegerField()
    school = ForeignKeyField(School)

    def get_data(self):
        return {"id": self.id, "grade": self.grade, "school": self.school}
