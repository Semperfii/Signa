import click


@click.group()
def cli():
    click.echo(click.style('== signa CLI ==', bold=True))
