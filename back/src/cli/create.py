import click

from .cli import cli


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

