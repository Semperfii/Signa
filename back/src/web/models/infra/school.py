from peewee import *

from web.database import db


class School(Model):
    id = PrimaryKeyField()
    name = CharField()

    def get_data(self):
        return {"id": self.id, "name": self.name}

    class Meta:
        database = db


School.create_table(fail_silently=True)
