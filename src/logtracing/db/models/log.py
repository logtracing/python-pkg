from datetime import datetime
from .main import BaseModel
from .log_group import LogGroup
from peewee import SQL, Check, TextField, DateTimeField, CharField, ForeignKeyField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class Log(BaseModel):
    LEVEL_CHOICES = ('TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL')

    flow = CharField(null=True)
    content = TextField(null=True)
    created_at = DateTimeField(column_name='createdAt', default=datetime.now)
    updated_at = DateTimeField(column_name='updatedAt', default=datetime.now)
    level = CharField(
        constraints=[Check(f'level IN {LEVEL_CHOICES}'), SQL('DEFAULT "INFO"')],
        null=True
    )
    log_group = ForeignKeyField(
        column_name='logGroupId',
        field='id',
        model=LogGroup,
        on_delete='CASCADE',
        null=True
    )

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Log, self).save(*args, **kwargs)

    class Meta:
        table_name = 'logs'
