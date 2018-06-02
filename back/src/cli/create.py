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
@click.option('--admin/--no-admin', default=False)
def user(mail, password, firstname, lastname, admin):
    from web.managers import UsersManager, UserAlreadyRegistered
    manager = UsersManager()
    try:
        manager.create_user(mail, password, firstname, lastname, admin)
    except UserAlreadyRegistered:
        click.echo('User {} already registered'.format(mail))


@create.command()
@click.option('--playerA', prompt=True)
@click.option('--playerB', prompt=True)
@click.option('--playerC', prompt=True)
@click.option('--playerD', prompt=True)
@click.option('--scoreAB', prompt=True)
@click.option('--scoreCD', prompt=True)
def match(playerA, playerB, playerC, playerD, scoreAB, scoreCD):
    from web.managers import MatchsManager
    manager = MatchsManager(user_id=0)
    body = {
        'playerA': playerA,
        'playerB': playerB,
        'playerC': playerC,
        'playerD': playerD,
        'scoreAB': scoreAB,
        'scoreCD': scoreCD
    }
    manager.add_match(body)
