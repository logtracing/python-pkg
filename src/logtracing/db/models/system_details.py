from main import BaseModel
from error_exception import ErrorExceptions
from peewee import CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class SystemDetails(BaseModel):
    arch = CharField(null=True)
    error_exception = ForeignKeyField(column_name='errorExceptionId', field='id', model=ErrorExceptions, null=True)
    hostname = CharField(null=True)
    platform = CharField(null=True)
    platform_release = CharField(column_name='platformRelease', null=True)
    platform_version = CharField(column_name='platformVersion', null=True)
    processor = CharField(null=True)
    user = CharField(null=True)

    class Meta:
        table_name = 'systemDetails'
