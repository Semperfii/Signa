from peewee import *

from .student import Student


class Parent:
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
