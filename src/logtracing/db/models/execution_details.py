from datetime import datetime
from .main import BaseModel
from .error_exception import ErrorException
from peewee import DateTimeField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ExecutionDetails(BaseModel):
    version = CharField(null=True)
    language = CharField(null=True)
    execution_finish_time = DateTimeField(column_name='executionFinishTime', default=datetime.now)
    error_exception = ForeignKeyField(
        column_name='errorExceptionId',
        field='id',
        model=ErrorException,
        on_delete='CASCADE',
        null=True
    )

    class Meta:
        table_name = 'executionDetails'
