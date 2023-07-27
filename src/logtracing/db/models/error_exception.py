from main import BaseModel
from log_group import LogGroup
from peewee import DateTimeField, CharField, ForeignKeyField, TextField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ErrorException(BaseModel):
    created_at = DateTimeField(column_name='createdAt')
    flow = CharField(null=True)
    log_group = ForeignKeyField(column_name='logGroupId', field='id', model=LogGroup, null=True)
    message = CharField(null=True)
    name = CharField(null=True)
    package = CharField(null=True)
    stack_str = TextField(column_name='stackStr', null=True)
    updated_at = DateTimeField(column_name='updatedAt')

    class Meta:
        table_name = 'errorExceptions'
