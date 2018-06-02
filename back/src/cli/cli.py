import click


@click.group()
def cli():
    click.echo(click.style('== Signa CLI ==', bold=True))
