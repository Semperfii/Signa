from ..models import ResultQuizz
from playhouse.shortcuts import model_to_dict, dict_to_model
from ..models import Question
from ..managers import StudentsManager


class QuestionsManager:

    def __init__(self):
        pass

    def score_question(self, id_question, score_function):
        with ResultQuizz.db.transaction():
            positives = ResultQuizz.select().where(ResultQuizz.id_question == id_question, ResultQuizz.outcome)
            negatives = ResultQuizz.select().where(ResultQuizz.id_question == id_question, not ResultQuizz.outcome)
        return score_function(len(positives), len(negatives))

    def allocate_question(self, student, subject):
        s = student.score[subject]
        questions = Question.select().where(Question.subject == subject)
        questions = map(lambda x: model_to_dict(x), questions)
        r = questions.index(min([abs(question["difficulty"]-s) for question in questions]))
        return dict_to_model(Question, r)

    def eval_question(self, result_solo, eval_function):
        student = StudentsManager.get(result_solo.id_student)
        question = result_solo.question
        score = student.score[question.subject]
        return result_solo.outcome * (eval_function(score, question.difficulty))

    def xp_question(self, result_solo, xp_function):
        if result_solo.outcome:
            student = StudentsManager.get(result_solo.id_student)
            question = result_solo.question
            xp = student.xp
            return xp_function(question.difficulty, xp)

