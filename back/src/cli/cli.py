import click


@click.group()
def cli():
    click.echo(click.style('== Signa CLI ==', bold=True))


@cli.group()
def reset():
    pass


@reset.command()
@click.option('--student_id', prompt=True)
def student(student_id):
    from web.managers import StudentsManager
    manager = StudentsManager()
    manager.reset_student(student_id)
