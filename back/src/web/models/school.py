from peewee import *


class School(Model):
    id = PrimaryKeyField()
    name = CharField()

    def get_data(self):
        return {"id": self.id, "name": self.name}

