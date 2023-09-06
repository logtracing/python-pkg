from datetime import datetime
from peewee import DateTimeField, CharField, ForeignKeyField, TextField
from logtracing.db.models.main import BaseModel
from logtracing.db.models.log_group import LogGroup


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ErrorException(BaseModel):
    flow = CharField(null=True)
    name = CharField(null=True)
    package = CharField(null=True)
    message = CharField(null=True)
    stack_str = TextField(column_name='stackStr', null=True)
    created_at = DateTimeField(column_name='createdAt', default=datetime.now)
    updated_at = DateTimeField(column_name='updatedAt', default=datetime.now)
    log_group = ForeignKeyField(
        column_name='logGroupId',
        field='id',
        model=LogGroup,
        on_delete='CASCADE',
        null=True
    )

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(ErrorException, self).save(*args, **kwargs)

    class Meta:
        table_name = 'errorExceptions'
