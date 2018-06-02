import re

from peewee import IntegrityError, DoesNotExist
from playhouse.shortcuts import model_to_dict

from ..exceptions import *
from ..models import User
from ..database import db


class UsersManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)
        User.create_table(fail_silently=True)

    def __del__(self):
        self.db.close()

    def get_all(self, search=None, max=None):
        user_list = []
        if search is None or search == '':
            query = User.select()
        else:
            query = User.select().where(
                (User.first_name.contains(search)) |
                (User.last_name.contains(search))
            )
        for user in query:
            user_list.append(model_to_dict(user))
        logger.debug('Get all users from db. Number of users : {}'.format(len(user_list)))
        if max is not None:
            user_list = user_list[:min([len(user_list), int(max)])]
        return user_list

    def get(self, id):
        with self.db.transaction():
            try:
                user = User.get(User.id == id)
                logger.debug('Get {} user. Response : {}'.format(id, user))
                return user.get_data()
            except DoesNotExist:
                raise UserNotExisting

    def create_user(self, email, first_name, last_name, admin=False):
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email) is None:
            raise BadEmail
        with self.db.atomic():
            try:
                user = User.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    admin=admin
                )
                return user
            except IntegrityError:
                raise UserAlreadyRegistered

    def delete_users_table(self):
        with self.db.atomic():
            User.drop_table()
