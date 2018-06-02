from peewee import *

from .classe import Classe


class Student:
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    classe = ForeignKeyField(Classe)

