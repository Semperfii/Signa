from ..database import db
from ..models import ResultQuizz


class QuizzResultsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)
        ResultQuizz.create_table(fail_silently=True)

    def __del__(self):
        self.db.close()

