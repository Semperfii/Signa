from playhouse.shortcuts import model_to_dict

from ..database import db
from ..models import ResultQuizz


class QuizzResultsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)

    def __del__(self):
        self.db.close()

    def add_result(self, id_student, id_question, outcome):
        with self.db.atomic():
            result = ResultQuizz.create(
                id_student=id_student,
                question=id_question,
                outcome=outcome
            )
            return result

    def get_results(self, id_student):
        with self.db.transaction():
            results = ResultQuizz.select().where(ResultQuizz.id_student == id_student)
            results_dict = [model_to_dict(result, recurse=True) for result in results]
        return results_dict

    def del_result_table(self):
        with self.db.atomic():
            ResultQuizz.drop_table()
