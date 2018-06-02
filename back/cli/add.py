import click
import json

from .cli import cli


@cli.group()
def add():
    pass


@add.command()
@click.option('--file', prompt=True)
def users(file):
    from web.managers import UsersManager, UserAlreadyRegistered
    manager = UsersManager()
    with open(file) as f:
        for people in f:
            email, first_name, last_name = people.split('\t')
            try:
                manager.create_user(email, first_name, last_name)
            except UserAlreadyRegistered:
                click.echo('User already in database. Skipping.')
    click.echo('Import done.')


@add.command()
@click.option('--file', prompt=True)
def matches(file):
    from web.managers import MatchsManager
    manager = MatchsManager(user_id=0)
    with open(file) as f:
        data = json.load(f)
    for match in data:
        manager.add_match(match)
    click.echo('Import done.')
