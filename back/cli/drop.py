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


@drop.command()
def matches():
    from web.managers import MatchsManager
    manager = MatchsManager()
    if click.confirm('Caution, dropping a table. Continue ?'):
        manager.delete_matches_table()


@drop.command()
def notifications():
    from web.managers import NotificationManager
    manager = NotificationManager()
    if click.confirm('Caution, dropping a table. Continue ?'):
        manager.delete_notifications_tables()
