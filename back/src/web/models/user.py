import hashlib

from peewee import *
from web.database import db


class User(Model):
    id = PrimaryKeyField()
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True, index=True)
    password = CharField()
    _admin = IntegerField()

    @property
    def admin(self):
        return bool(self._admin)

    @admin.setter
    def admin(self, val):
        self._admin = int(val)

    def get_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email,
                "admin": bool(self._admin)}

    def get_small_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name}

    class Meta:
        database = db

    def check_password(self, password):
        return self.password == hashlib.sha224(password.encode('utf-8')).hexdigest()


db.connect()
User.create_table(fail_silently=True)
db.close()
