from ..database import db
from ..models import ResultDuel


class DuelResultsManager:

    def __init__(self):
        self.db = db
        self.db.connect(reuse_if_open=True)
        ResultDuel.create_table(fail_silently=True)
