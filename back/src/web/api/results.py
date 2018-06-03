from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request

from web.managers import StudentsManager
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

        studentsManager.update_score(me, result)
        studentsManager.update_xp(me, result)

        return {'msg': 'success'}
