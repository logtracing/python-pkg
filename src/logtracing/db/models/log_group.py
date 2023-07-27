from main import BaseModel
from peewee import DateTimeField, CharField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class LogGroup(BaseModel):
    created_at = DateTimeField(column_name='createdAt')
    name = CharField(null=True, unique=True)
    updated_at = DateTimeField(column_name='updatedAt')

    class Meta:
        table_name = 'logGroups'
