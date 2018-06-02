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
