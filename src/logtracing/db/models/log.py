from main import BaseModel
from log_group import LogGroup
from peewee import SQL, Check, TextField, DateTimeField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class Log(BaseModel):
    LEVEL_CHOICES = ('TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL')

    content = TextField(null=True)
    created_at = DateTimeField(column_name='createdAt')
    flow = CharField(null=True)
    level = CharField(constraints=[Check(f'level IN {LEVEL_CHOICES}'), SQL('DEFAULT "INFO"')], null=True)
    log_group = ForeignKeyField(column_name='logGroupId', field='id', model=LogGroup, null=True)
    updated_at = DateTimeField(column_name='updatedAt')

    class Meta:
        table_name = 'logs'
