from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from back.web.exceptions import *
from back.web.models import Teacher
from ..database import db


class TeachersManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)
        Teacher.create_table(fail_silently=True)

    def __del__(self):
        self.db.close()

    def get_all(self, search=None, max=None):
        teachers = []
        if search is None or search == '':
            query = Teacher.select()
        else:
            query = Teacher.select().where(
                (Teacher.name.contains(search)) |
                (Teacher.surname.contains(search))
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

    def add_teacher(self, name, surname, subject, classes, admin=False):
        with self.db.atomic():
            try:
                teacher = Teacher.create(name=name, surname=surname, subject=subject)
                return teacher
            except IntegrityError:
                raise TeacherAlreadyRegistered

    def del_teacher(self):
        pass

    def del_teacher_table(self):
        with self.db.atomic():
            Teacher.drop_table()

    def get_classes(self):
        pass




