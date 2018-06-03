from playhouse.shortcuts import model_to_dict, dict_to_model

from web.database import db
from ..managers import StudentsManager
from ..models import Question
from ..models import ResultQuizz


class QuestionsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)

    def __del__(self):
        self.db.close()

    def score_question(self, id_question, score_function):
        with self.db.transaction():
            positives = ResultQuizz.select().where(ResultQuizz.id_question == id_question, ResultQuizz.outcome)
            negatives = ResultQuizz.select().where(ResultQuizz.id_question == id_question, not ResultQuizz.outcome)
            return score_function(len(positives), len(negatives))

    def allocate_question(self, student, subject):
        with self.db.transaction():
            s = student['score'][str(subject)]
            questions = Question.select().where(Question.subject == subject)
            questions = list(map(lambda x: model_to_dict(x), questions))
            r = questions.index(min([abs(question["difficulty"] - s) for question in questions]))
            return dict_to_model(Question, r)

    def eval_question(self, result_solo, eval_function):
        with self.db.transaction():
            student = StudentsManager().get(result_solo.id_student)
            question = result_solo.question
            score = student.score[question.subject]
            return result_solo.outcome * (eval_function(score, question.difficulty))

    def xp_question(self, result_solo, xp_function):
        with self.db.transaction():
            if result_solo.outcome:
                student = StudentsManager().get(result_solo.id_student)
                question = result_solo.question
                xp = student.xp
                return xp_function(question.difficulty, xp)
