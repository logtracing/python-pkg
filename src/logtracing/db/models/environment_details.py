from main import BaseModel
from error_exception import ErrorException
from peewee import TextField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class EnvironmentDetails(BaseModel):
    error_exception = ForeignKeyField(column_name='errorExceptionId', field='id', model=ErrorException, null=True)
    name = CharField(null=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'environmentDetails'
