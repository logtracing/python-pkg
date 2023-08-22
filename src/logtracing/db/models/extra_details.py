from main import BaseModel
from error_exception import ErrorException
from peewee import BooleanField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ExtraDetails(BaseModel):
    name = CharField(null=True)
    value = CharField(null=True)
    is_json = BooleanField(column_name='isJson', null=True)
    error_exception = ForeignKeyField(column_name='errorExceptionId', field='id', model=ErrorException, null=True)

    class Meta:
        table_name = 'extraDetails'
