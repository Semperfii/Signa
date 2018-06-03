import re
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from ..database import db
from ..exceptions import *
from ..models import Teacher


class TeachersManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)

    def __del__(self):
        self.db.close()

    def get_all(self, search=None, max=None):
        teachers = []
        if search is None or search == '':
            query = Teacher.select()
        else:
            query = Teacher.select().where(
                (Teacher.first_name.contains(search)) |
                (Teacher.last_name.contains(search))
            )
        for teacher in query:
            teachers.append(model_to_dict(teacher))
        logger.debug('Get all teachers from db. Number of teachers : {}'.format(len(teachers)))
        if max is not None:
            teachers = teachers[:min([len(teachers), int(max)])]
        return teachers

    def get(self, teacher_id):
        try:
            teacher = Teacher.get(Teacher.id == teacher_id)
            logger.debug('Get the {}th teacher. Response : {}'.format(teacher_id, teacher))
            return teacher.get_data()
        except DoesNotExist:
            raise TeacherNotExisting

    def add_teacher(self, email, password, first_name, last_name, subject, classes, admin=False):
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email) is None:
            raise BadEmail
        with self.db.atomic():
            try:
                teacher = Teacher.create(first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         password=password,
                                         subject=subject)
                return teacher
            except IntegrityError:
                raise TeacherAlreadyRegistered

    def del_teacher_table(self):
        with self.db.atomic():
            Teacher.drop_table()

    def check_user_auth(self, email, password):
        with self.db.transaction():
            teachers = Teacher.select().where(Teacher.email == email, Teacher.password == password)
            if len(teachers) > 0:
                return teachers[0].get_data()
            else:
                return None





