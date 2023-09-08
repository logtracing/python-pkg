from peewee import CharField, ForeignKeyField
from logtracing.db.models.main import BaseModel
from logtracing.db.models.error_exception import ErrorException


class UnknownField(object):
    def __init__(self, *_, **__): pass


class SystemDetails(BaseModel):
    arch = CharField(null=True)
    user = CharField(null=True)
    hostname = CharField(null=True)
    platform = CharField(null=True)
    processor = CharField(null=True)
    platform_release = CharField(column_name='platformRelease', null=True)
    platform_version = CharField(column_name='platformVersion', null=True)
    error_exception = ForeignKeyField(
        column_name='errorExceptionId',
        field='id',
        model=ErrorException,
        on_delete='CASCADE',
        null=True
    )

    class Meta:
        table_name = 'systemDetails'
