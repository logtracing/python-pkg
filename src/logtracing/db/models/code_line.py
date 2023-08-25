from .main import BaseModel
from .stack import Stack
from peewee import IntegerField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class CodeLine(BaseModel):
    content = CharField(null=True)
    line = IntegerField(null=True)
    is_error_line = IntegerField(column_name='isErrorLine', null=True)
    stack = ForeignKeyField(
        column_name='stackId',
        field='id',
        model=Stack,
        on_delete='CASCADE',
        null=True
    )

    class Meta:
        table_name = 'codeLines'
