from peewee import IntegrityError

from ..database import db
from ..models import ResultDuel


class DuelResultsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)
        ResultDuel.create_table(fail_silently=True)

    def __del__(self):
        self.db.close()

    def add_result(self, id1, id2, score1, score2, id_question):
        with self.db.atomic():
            try:
                result = ResultDuel.create(
                    id_student_1=id1,
                    id_student_2=id2,
                    score_1=score1,
                    score_2=score2,
                    id_question=id_question
                )
                return result
            except IntegrityError:
                raise ResultAlreadyRegistered

    def del_result_table(self):
        with self.db.atomic():
            ResultDuel.drop_table()
