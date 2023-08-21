# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class LogGroup(peewee.Model):
    name = CharField(max_length=255, null=True, unique=True)
    created_at = DateTimeField(column_name='createdAt')
    updated_at = DateTimeField(column_name='updatedAt')
    class Meta:
        table_name = "logGroups"


@snapshot.append
class ErrorException(peewee.Model):
    flow = CharField(max_length=255, null=True)
    name = CharField(max_length=255, null=True)
    package = CharField(max_length=255, null=True)
    message = CharField(max_length=255, null=True)
    created_at = DateTimeField(column_name='createdAt')
    updated_at = DateTimeField(column_name='updatedAt')
    stack_str = TextField(column_name='stackStr', null=True)
    log_group = snapshot.ForeignKeyField(column_name='logGroupId', index=True, model='loggroup', null=True)
    class Meta:
        table_name = "errorExceptions"


@snapshot.append
class Stack(peewee.Model):
    file = CharField(max_length=255, null=True)
    line = IntegerField(null=True)
    function = CharField(max_length=255, null=True)
    column = IntegerField(null=True)
    error_exception = snapshot.ForeignKeyField(column_name='errorExceptionId', index=True, model='errorexception', null=True)
    class Meta:
        table_name = "stack"


@snapshot.append
class CodeLine(peewee.Model):
    content = CharField(max_length=255, null=True)
    line = IntegerField(null=True)
    is_error_line = IntegerField(column_name='isErrorLine', null=True)
    stack = snapshot.ForeignKeyField(column_name='stackId', index=True, model='stack', null=True)
    class Meta:
        table_name = "codeLines"


@snapshot.append
class EnvironmentDetails(peewee.Model):
    name = CharField(max_length=255, null=True)
    value = TextField(null=True)
    error_exception = snapshot.ForeignKeyField(column_name='errorExceptionId', index=True, model='errorexception', null=True)
    class Meta:
        table_name = "environmentDetails"


@snapshot.append
class ExecutionDetails(peewee.Model):
    version = CharField(max_length=255, null=True)
    language = CharField(max_length=255, null=True)
    execution_finish_time = DateTimeField(column_name='executionFinishTime', null=True)
    error_exception = snapshot.ForeignKeyField(column_name='errorExceptionId', index=True, model='errorexception', null=True)
    class Meta:
        table_name = "executionDetails"


@snapshot.append
class ExecutionArguments(peewee.Model):
    argument = CharField(max_length=255, null=True)
    execution_details = snapshot.ForeignKeyField(column_name='executionDetailsId', index=True, model='executiondetails', null=True)
    class Meta:
        table_name = "executionArguments"


@snapshot.append
class ExtraDetails(peewee.Model):
    name = CharField(max_length=255, null=True)
    value = CharField(max_length=255, null=True)
    is_json = IntegerField(column_name='isJson', null=True)
    error_exception = snapshot.ForeignKeyField(column_name='errorExceptionId', index=True, model='errorexception', null=True)
    class Meta:
        table_name = "extraDetails"


@snapshot.append
class Log(peewee.Model):
    flow = CharField(max_length=255, null=True)
    content = TextField(null=True)
    created_at = DateTimeField(column_name='createdAt')
    updated_at = DateTimeField(column_name='updatedAt')
    log_group = snapshot.ForeignKeyField(column_name='logGroupId', index=True, model='loggroup', null=True)
    level = CharField(constraints=[SQL("CHECK (level IN ('TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'))"), SQL('DEFAULT "INFO"')], max_length=255, null=True)
    class Meta:
        table_name = "logs"


@snapshot.append
class SystemDetails(peewee.Model):
    arch = CharField(max_length=255, null=True)
    user = CharField(max_length=255, null=True)
    hostname = CharField(max_length=255, null=True)
    platform = CharField(max_length=255, null=True)
    processor = CharField(max_length=255, null=True)
    platform_release = CharField(column_name='platformRelease', max_length=255, null=True)
    platform_version = CharField(column_name='platformVersion', max_length=255, null=True)
    error_exception = snapshot.ForeignKeyField(column_name='errorExceptionId', index=True, model='errorexception', null=True)
    class Meta:
        table_name = "systemDetails"


