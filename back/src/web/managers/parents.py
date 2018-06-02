from ..database import db
from ..models import Parent
from ..exceptions import *
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist, IntegrityError
import re


class ParentsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)

    def __del__(self):
        self.db.close()

    def get_all(self, search=None, max=None):
        parents = []
        if search is None or search == '':
            query = Parent.select()
        else:
            query = Parent.select().where(
                (Parent.first_name.contains(search)) |
                (Parent.last_name.contains(search))
            )
        for parent in query:
            parents.append(model_to_dict(parent))
        logger.debug('Get all parents from db. Number of parents : {}'.format(len(parents)))
        if max is not None:
            parents = parents[:min([len(parents), int(max)])]
        return parents

    def get(self, id):
        with self.db.transaction():
            try:
                parent = Parent.get(Parent.id == id)
                logger.debug('Get {} parent. Response : {}'.format(id, parent))
                return parent.get_data()
            except DoesNotExist:
                raise ParentNotExisting

    def add_parent(self, email, password, first_name, last_name):
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email) is None:
            raise BadEmail
        with self.db.atomic():
            try:
                parent = Parent.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                return parent
            except IntegrityError:
                raise ParentAlreadyRegistered

    def del_parent(self):
        pass

    def del_parent_table(self):
        with self.db.atomic():
            Parent.drop_table()

    def check_user_auth(self, email, password):
        with self.db.transaction():
            parents = Parent.select().where(Parent.email == email, Parent.password == password)
            if len(parents) > 0:
                return parents[0].get_data()
            else:
                return None
