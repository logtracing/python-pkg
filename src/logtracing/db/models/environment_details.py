from main import BaseModel
from error_exception import ErrorExceptions
from peewee import TextField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class EnvironmentDetails(BaseModel):
    error_exception = ForeignKeyField(column_name='errorExceptionId', field='id', model=ErrorExceptions, null=True)
    name = CharField(null=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'environmentDetails'
