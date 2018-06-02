import click

from .cli import cli


@cli.group()
def drop():
    pass


@drop.command()
def users():
    from web.managers import UsersManager
    manager = UsersManager()
    if click.confirm('Caution, dropping a table. Continue ?'):
        manager.delete_users_table()
