from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request

from web.managers import StudentsManager
from web.managers.questions import QuestionsManager
from web.managers.results_quizz import QuizzResultsManager


class Results(Resource):

    @jwt_required
    def post(self):
        studentsManager = StudentsManager()
        me = get_jwt_identity()["id"]
        outcome = request.json['outcome']
        question_id = request.json['question_id']

        results_manager = QuizzResultsManager()
        result = results_manager.add_result(me, question_id, outcome)

        bonus = QuestionsManager().eval_question(result)
        subject = result.question.subject
        xp = QuestionsManager().xp_question(result)

        new_score = studentsManager.update_score(me, bonus, subject)
        new_xp = studentsManager.update_xp(me, xp)

        return {'msg': 'success', 'xp': new_xp, 'score': new_score}
