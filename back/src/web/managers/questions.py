from ..models import ResultQuizz


class QuestionsManager:

    def __init__(self):
        pass

    def score_question(self, id_question, score_function):
        with self.db.transaction():
            positives = ResultQuizz.select().where(ResultQuizz.id_question == id_question, ResultQuizz.outcome ==)
