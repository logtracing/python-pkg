from main import BaseModel
from error_exception import ErrorExceptions
from peewee import DateTimeField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ExecutionDetails(BaseModel):
    error_exception = ForeignKeyField(column_name='errorExceptionId', field='id', model=ErrorExceptions, null=True)
    execution_finish_time = DateTimeField(column_name='executionFinishTime', null=True)
    language = CharField(null=True)
    version = CharField(null=True)

    class Meta:
        table_name = 'executionDetails'