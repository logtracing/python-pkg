from .main import BaseModel
from .error_exception import ErrorException
from peewee import IntegerField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ExtraDetails(BaseModel):
    name = CharField(null=True)
    value = CharField(null=True)
    is_json = IntegerField(column_name='isJson', null=True)
    error_exception = ForeignKeyField(
        column_name='errorExceptionId',
        field='id',
        model=ErrorException,
        on_delete='CASCADE',
        null=True
    )

    class Meta:
        table_name = 'extraDetails'
