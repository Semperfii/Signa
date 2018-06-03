import json
import re
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from web.managers.questions import QuestionsManager
from ..database import db
from ..exceptions import *
from ..models import Student
from ..managers import QuizzResultsManager


class StudentsManager:
    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)

    def __del__(self):
        self.db.close()

    def get_all(self, search=None, max=None):
        students = []
        if search is None or search == '':
            query = Student.select()
        else:
            query = Student.select().where(
                (Student.first_name.contains(search)) |
                (Student.last_name.contains(search))
            )
        for student in query:
            students.append(model_to_dict(student))
        logger.debug('Get all students from db. Number of students : {}'.format(len(students)))
        if max is not None:
            students = students[:min([len(students), int(max)])]
        return students

    def get(self, id):
        with self.db.transaction():
            try:
                student = Student.get(Student.id == id)
                logger.debug('Get {} student. Response : {}'.format(id, student))
                return student.get_data()
            except DoesNotExist:
                raise StudentNotExisting

    def add_student(self, email, password, first_name, last_name, classe):
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email) is None:
            raise BadEmail
        with self.db.atomic():
            try:
                student = Student.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    classe=classe,
                    score=json.dumps({0: 0.2}),
                    xp=0.
                    )
                return student
            except IntegrityError:
                raise StudentAlreadyRegistered

    def del_student(self):
        pass

    def del_student_table(self):
        with self.db.atomic():
            Student.drop_table()

    def check_user_auth(self, email, password):
        with self.db.transaction():
            students = Student.select().where(Student.email == email, Student.password == password)
            if len(students) > 0:
                return students[0].get_data()
            else:
                return None

    def update_score(self, student_id, result):
        bonus = QuestionsManager().eval_question(result)
        student = StudentsManager().get(student_id)
        scores = json.loads(student.score)
        subject = result.question.subject
        new_score = scores[subject] + bonus
        if new_score < 0:
            scores[subject] = 0
            query = Student.update(scores=json.dumps(scores)).where(Student.id == student_id)
            query.execute()
        elif new_score > 1:
            scores[subject] = 1
            query = Student.update(scores=json.dumps(scores)).where(Student.id == student_id)
            query.execute()
        else:
            scores[subject] = new_score
            query = Student.update(scores=json.dumps(scores)).where(Student.id == student_id)
            query.execute()

    def update_xp(self, student_id, result):
        xp = QuestionsManager().xp_question(result)
        query = Student.update(xp = xp).where(Student.id == student_id)
        query.execute()



