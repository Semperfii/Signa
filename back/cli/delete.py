import click

from .cli import cli


@cli.group()
def delete():
    pass


@delete.command()
@click.option('--id', prompt=True)
def match(id):
    from web.managers import MatchsManager
    manager = MatchsManager(user_id=0)
    manager.delete_matches(id)


@delete.command()
def matches():
    from web.managers import MatchsManager
    manager = MatchsManager(user_id=0)
    matches = manager.get_all()
    for match in matches:
        manager.delete_matches(match['id'])


@delete.command()
@click.option('--id', prompt=True)
def notification(id):
    from web.managers import NotificationManager
    manager = NotificationManager(user_id=0)
    manager.delete_notifications(id)
