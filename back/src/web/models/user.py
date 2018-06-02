from peewee import *

from ..database import db


class User(Model):
    id = PrimaryKeyField()
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True, index=True)
    password = CharField()

    type = None

    def get_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email,
                "type": self.type}

    def get_small_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name}

    class Meta:
        database = db
