from .main import BaseModel
from .execution_details import ExecutionDetails
from peewee import CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ExecutionArguments(BaseModel):
    argument = CharField(null=True)
    execution_details = ForeignKeyField(column_name='executionDetailsId', field='id', model=ExecutionDetails, null=True)

    class Meta:
        table_name = 'executionArguments'
