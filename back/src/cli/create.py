import click
import json

from cli import cli


@cli.group()
def create():
    pass


@create.command()
@click.option('--mail', prompt=True)
@click.option('--password', prompt=True)
@click.option('--firstname', prompt=True)
@click.option('--lastname', prompt=True)
@click.option('--classe', prompt=True)
def student(mail, password, firstname, lastname, classe):
    from web.managers import StudentsManager
    from web.exceptions import StudentAlreadyRegistered
    manager = StudentsManager()
    try:
        manager.add_student(mail, password, firstname, lastname, classe)
    except StudentAlreadyRegistered:
        click.echo('Student {} already registered'.format(mail))


@create.command()
@click.option('--name', prompt=True)
def school(name):
    from web.models import School
    from web.database import db
    with db.transaction():
        School.create(name=name)


@create.command()
@click.option('--name', prompt=True)
@click.option('--school', prompt=True)
def classe(name, school):
    from web.models import Classe
    from web.database import db
    with db.transaction():
        Classe.create(name=name, school=school)


@create.command()
@click.option('--data_json', prompt=True)
@click.option('--subject', prompt=True)
def question(data_json, subject):
    from web.models import Question
    from web.database import db
    data = json.loads(data_json)
    with db.transaction():
        Question.create(subject=subject, content=data["question"],
                        difficulty=data["difficulty"],  propositions=json.dumps(data["propositions"]))
