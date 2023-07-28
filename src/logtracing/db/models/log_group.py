from main import BaseModel
from peewee import DateTimeField, CharField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class LogGroup(BaseModel):
    name = CharField(null=True, unique=True)
    created_at = DateTimeField(column_name='createdAt')
    updated_at = DateTimeField(column_name='updatedAt')

    class Meta:
        table_name = 'logGroups'
