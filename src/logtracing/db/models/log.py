from main import BaseModel
from log_group import LogGroups
from peewee import SQL, Check, TextField, DateTimeField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class Logs(BaseModel):
    content = TextField(null=True)
    created_at = DateTimeField(column_name='createdAt')
    flow = CharField(null=True)
    level = CharField(constraints=[Check("level IN ('TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL')")], default='INFO', null=True)
    log_group = ForeignKeyField(column_name='logGroupId', field='id', model=LogGroups, null=True)
    updated_at = DateTimeField(column_name='updatedAt')

    class Meta:
        table_name = 'logs'
