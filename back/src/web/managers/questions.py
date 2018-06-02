from ..models import ResultQuizz
from playhouse.shortcuts import model_to_dict, dict_to_model
from ..models import Question


class QuestionsManager:

    def __init__(self):
        pass

    def score_question(self, question, score_function):
        with ResultQuizz.db.transaction():
            id = question.id_question
            positives = ResultQuizz.select().where(ResultQuizz.id_question == id, ResultQuizz.outcome)
            negatives = ResultQuizz.select().where(ResultQuizz.id_question == id, not ResultQuizz.outcome)
            question.difficulty = score_function(len(positives), len(negatives))

    def allocate_question(self, student):
        s = student.score
        questions = ResultQuizz.select()
        questions = map(lambda x: model_to_dict(x), questions)
        r = questions.index(min([abs(question["difficulty"]-s) for question in questions]))
        return dict_to_model(Question, r)
