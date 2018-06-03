from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request

from web.managers import StudentsManager
from web.managers.questions import QuestionsManager
from ..store import Store


class Question(Resource):
    @jwt_required
    def get(self):
        me = get_jwt_identity()["id"]
        student = StudentsManager().get(me)
        subject = request.args.get('subject', None)
        questionsManager = QuestionsManager()
        question = questionsManager.allocate_question(student, subject)
        return question


class Questions(Resource):

    @jwt_required
    def get(self, question_id):
        me = get_jwt_identity()["id"]
        student = StudentsManager().get(me)

        store = Store()
        if store.get_subjects(me) is None:
            scores = student['score']
            subjects_header = [0]
            for i in range(len(subjects_header)):
                if subjects_header[i] != 0:
                    scores[i] = 1 / scores[i]
            total = len(subjects_header)

            proportions = []
            for key in scores.keys():
                proportions.append(1 / scores[key] * total)
            proportions = [proportion * (20 / sum(proportions)) for proportion in proportions]

            subjects = []
            for i, proportion in enumerate(proportions):
                for _ in range(round(proportion)):
                    subjects.append(i)

            store.set_subjects(me, subjects)

        subjects = store.get_subjects(me)
        subject = subjects[int(question_id)]

        questionsManager = QuestionsManager()
        question = questionsManager.allocate_question(student, subject)

        if question_id == 19:
            store.remove_subjects(me)

        return question
