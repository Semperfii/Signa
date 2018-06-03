from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request

from web.managers.results_quizz import QuizzResultsManager


class Results(Resource):

    @jwt_required
    def post(self):
        me = get_jwt_identity()["id"]

        outcome = request.json['outcome']
        question_id = request.json['question_id']

        results_manager = QuizzResultsManager()
        results_manager.add_result(me, question_id, outcome)

        return {'msg': 'success'}
