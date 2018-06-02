import click

from .cli import cli


@cli.group()
def get():
    pass


@get.command()
@click.option('--search')
@click.option('--max')
def users(search, max):
    from web.managers import UsersManager
    manager = UsersManager()
    click.echo(click.style('== Users ==', bold=True))
    click.echo(manager.get_all(search, max))


@get.command()
def matches():
    from web.managers import MatchsManager
    manager = MatchsManager()
    click.echo(click.style('== Matchs ==', bold=True))
    click.echo(manager.get_all())


@get.command()
@click.option('--id', prompt=True)
def notifications(id):
    from web.managers import NotificationManager
    manager = NotificationManager(user_id=id)
    click.echo(click.style('== Notifications ==', bold=True))
    click.echo(manager.get())
