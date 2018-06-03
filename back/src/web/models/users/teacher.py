from peewee import *

from .user import User


class Teacher(User):
    subject = CharField()

    type = 1

    def get_data(self):
        dict = super(Teacher, self).get_data()
        dict["subject"] = self.subject
        return dict


Teacher.create_table(fail_silently=True)
