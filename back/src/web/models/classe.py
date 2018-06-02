from peewee import *

from .school import School


class Classe:
    id = PrimaryKeyField()
    grade = IntegerField()
    school = ForeignKeyField(School)
