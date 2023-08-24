import datetime
from .main import BaseModel
from peewee import DateTimeField, CharField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class LogGroup(BaseModel):
    name = CharField(null=True, unique=True)
    created_at = DateTimeField(column_name='createdAt', default=datetime.datetime.now)
    updated_at = DateTimeField(column_name='updatedAt', default=datetime.datetime.now)

    class Meta:
        table_name = 'logGroups'
