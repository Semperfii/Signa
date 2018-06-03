import click

from .cli import cli


@cli.group()
def drop():
    pass


@drop.command()
def students():
    from web.managers import StudentsManager
    manager = StudentsManager()
    if click.confirm('Caution, dropping a table. Continue ?'):
        manager.del_student_table()


@drop.command()
def questions():
    from web.models import Question
    from web.database import db
    if click.confirm('Caution, dropping a table. Continue ?'):
        with db.atomic():
            Question.drop_table()


@drop.command()
def results():
    from web.managers import QuizzResultsManager
    if click.confirm('Caution, dropping a table. Continue ?'):
        QuizzResultsManager().del_result_table()
