from datetime import datetime
from peewee import DateTimeField, CharField
from logtracing.db.models.main import BaseModel


class UnknownField(object):
    def __init__(self, *_, **__): pass


class LogGroup(BaseModel):
    name = CharField(null=True, unique=True)
    updated_at = DateTimeField(column_name='updatedAt', default=datetime.now)
    created_at = DateTimeField(column_name='createdAt', default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(LogGroup, self).save(*args, **kwargs)

    class Meta:
        table_name = 'logGroups'
