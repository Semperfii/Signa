from peewee import *

from ..models.user import User


class Teacher(User):
    subject = CharField()

    def get_data(self):
        dict = super.get_data()
        dict["subject"] = self.subject
        return dict
