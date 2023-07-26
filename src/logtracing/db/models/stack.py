from main import BaseModel
from error_exception import ErrorExceptions
from peewee import IntegerField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class Stack(BaseModel):
    column = IntegerField(null=True)
    error_exception = ForeignKeyField(column_name='errorExceptionId', field='id', model=ErrorExceptions, null=True)
    file = CharField(null=True)
    function = CharField(null=True)
    line = IntegerField(null=True)

    class Meta:
        table_name = 'stack'
