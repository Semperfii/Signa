from ..database import db
from ..models import ResultQuizz
from peewee import IntegrityError


class QuizzResultsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)
        ResultQuizz.create_table(fail_silently=True)

    def __del__(self):
        self.db.close()

    def add_result(self, id_student, id_question, outcome):
        with self.db.atomic():
            try:
                result = ResultQuizz.create(
                    id_student=id_student,
                    id_question=id_question,
                    outcome=outcome
                )
                return result
            except IntegrityError:
                raise ResultAlreadyRegistered

    def del_result_table(self):
        with self.db.atomic():
            ResultQuizz.drop_table()