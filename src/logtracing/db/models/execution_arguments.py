from peewee import CharField, ForeignKeyField
from logtracing.db.models.main import BaseModel
from logtracing.db.models.execution_details import ExecutionDetails


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ExecutionArguments(BaseModel):
    argument = CharField(null=True)
    execution_details = ForeignKeyField(
        column_name='executionDetailsId',
        field='id',
        model=ExecutionDetails,
        on_delete='CASCADE',
        null=True
    )

    class Meta:
        table_name = 'executionArguments'
