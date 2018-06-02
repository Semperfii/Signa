from peewee import PostgresqlDatabase

from .config import config

db = PostgresqlDatabase(
    'signa',
    user=config['database'].get('user', 'signa'),
    password=config['database'].get('password', 'signa'),
    host=config['database'].get('host', 'localhost')
)
