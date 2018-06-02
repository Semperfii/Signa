from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from web.managers import StudentsManager
from web.managers.questions import QuestionsManager


class Question(Resource):

    @jwt_required
    def get(self, student, subject):
        questionsManager = QuestionsManager()
        question = questionsManager.allocate_question(student, subject)
        return question


class Questions(Resource):

    @jwt_required
    def get(self):
        me = get_jwt_identity()["id"]
        student = StudentsManager.get(me)
        scores = student.score
        for i in range(len(scores.values)):
            if scores.values[i] != 0:
                scores[i] = 1/scores[i]
        total = sum(scores.values)
        proportions = []
        for key in scores.keys:
            proportions.append(1/scores[key]*total)
        proportions = proportions*20/sum(proportions)
        for i in range(len(proportions)):
            proportions[i] = round(proportions[i])
        questions = []
        for j in range(len(proportions)):
            for _ in range(proportions[j]):
                questions.append(Question.get(student, scores.keys[j]))
        return questions





