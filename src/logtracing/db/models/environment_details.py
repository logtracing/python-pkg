from peewee import TextField, CharField, ForeignKeyField
from logtracing.db.models.main import BaseModel
from logtracing.db.models.error_exception import ErrorException


class UnknownField(object):
    def __init__(self, *_, **__): pass


class EnvironmentDetails(BaseModel):
    name = CharField(null=True)
    value = TextField(null=True)
    error_exception = ForeignKeyField(
        column_name='errorExceptionId',
        field='id',
        model=ErrorException,
        on_delete='CASCADE',
        null=True
    )

    class Meta:
        table_name = 'environmentDetails'
