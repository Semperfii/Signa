from peewee import *

from web.models import User
from .student import Student


class Parent(User):

    type = 2

    pass
