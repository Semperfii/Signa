from peewee import *


class Teacher:
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    subject = CharField()
