import traceback
from datetime import datetime
from typing import List, Union, Optional, Any, Dict
from db.models.log_group import LogGroup

# Error Exception
class PrepareStackTrace:
    def __init__(
        self,
        prepare_stack_trace: Union[BaseException, List[traceback.FrameSummary], Any]
    ) -> None:
        self.prepare_stack_trace = prepare_stack_trace


class CodeLine:
    def __init__(
        self,
        line: int,
        content: str,
        current_line: Optional[int]=None
    ) -> None:
        self.line = line
        self.content = content
        self.current_line = current_line


class ErrorStack:
    def __init__(
        self,
        error_name: str,
        error_message: str,
        error_stack: str,
        function_name: str,
        file_name: str,
        line_number: int,
        column_number: int,
        code: List[CodeLine]
    ) -> None:
        self.error_name = error_name
        self.error_message = error_message
        self.error_stack = error_stack
        self.function_name = function_name
        self.file_name = file_name
        self.line_number = line_number
        self.column_number = column_number
        self.code = code


class OsUser:
    def __init__(
        self,
        username: str,
        uid: int,
        gid: int
    ) -> None:
        self.username = username
        self.uid = uid
        self.gid = gid


class OsCpuTime:
    def __init__(
        self,
        user: int,
        nice: int,
        sys: int,
        idle: int,
        irq: int
    ) -> None:
        self.user = user
        self.nice = nice
        self.sys = sys
        self.idle = idle
        self.irq = irq


class OsCpu:
    def __init__(
        self,
        model: str,
        speed: int,
        times: OsCpuTime
    ) -> None:
        self.model = model
        self.speed = speed
        self.times = times


class OsVars:
    def __init__(
        self,
        arch: str,
        cpus: List[OsCpu],
        hostname: str,
        machine: str,
        platform: str,
        release: str,
        version: str,
        user: OsUser
    ) -> None:
        self.arch = arch
        self.cpus = cpus
        self.hostname = hostname
        self.machine = machine
        self.platform = platform
        self.release = release
        self.version = version
        self.user = user


class PythonVars:
    def __init__(
        self,
        version: str,
        args: List[str],
        date_time: int
    ) -> None:
        self.version = version
        self.args = args
        self.date_time = date_time


# Slack
class SlackMessageSectionField:
    def __init__(
        self,
        msg_type: str,
        msg_text: str
    ) -> None:
        self.msg_type = msg_type
        self.msg_text = msg_text


class SlackMessageSection:
    def __init__(
        self,
        msg_type: str,
        fields: List[SlackMessageSectionField]
    ) -> None:
        self.msg_type = msg_type
        self.fields = fields


# General
class LoggingOptions:
    def __init__(
        self,
        group: Optional[List],
        slack_message_extra_sections: Optional[List[SlackMessageSection]]
    ) -> None:
        self.group = group
        self.slack_message_extra_sections = slack_message_extra_sections


class LogTracingOptions:
    def __init__(
        self,
        slack_integration: Optional[bool]
    ) -> None:
        self.slack_integration = slack_integration


# Logger
class LogType:
    types = {
        'TRACE': 'TRACE',
        'DEBUG': 'DEBUG',
        'INFO': 'INFO',
        'WARN': 'WARN',
        'ERROR': 'ERROR',
        'FATAL': 'FATAL',
    }


# Models
class LogAttributes:
    def __init__(
        self,
        level: str,
        flow: str,
        content: str,
        log_group_id: Optional[int]=None,
        created_at: Optional[datetime]=None,
        updated_at: Optional[datetime]=None
    ) -> None:
        self.level = level
        self.flow = flow
        self.content = content
        self.log_group_id = log_group_id
        self.created_at = created_at
        self.updated_at = updated_at


class ErrorExceptionAttributes: 
    def __init__(
        self,
        package: str,
        flow: str,
        name: str,
        message: str,
        stack_str: str,
        log_group_id: Optional[int]=None,
        created_at: Optional[datetime]=None,
        updated_at: Optional[datetime]=None
    ) -> None:
        self.package = package
        self.flow = flow
        self.name = name
        self.message = message
        self.stack_str = stack_str
        self.log_group_id = log_group_id
        self.created_at = created_at
        self.updated_at = updated_at


class StackAttributes:
    def __init__(
        self,
        file: str,
        function: str,
        line: int,
        column: int,
        error_exception_id: int
    ) -> None:
        self.file = file
        self.function = function
        self.line = line
        self.column = column
        self.error_exception_id = error_exception_id


class CodeLineAttributes:
    def __init__(
        self,
        line: int,
        content: str,
        is_error_line: bool,
        stack_id: int
    ) -> None:
        self.line = line
        self.content = content
        self.is_error_line = is_error_line
        self.stack_id = stack_id


class SystemDetailsAttributes:
    def __init__(
        self,
        arch: str,
        processor: str,
        hostname: str,
        platform: str,
        platform_release: str,
        platform_version: str,
        user: str,
        error_exception_id: int
    ) -> None:
        self.arch = arch
        self.processor = processor
        self.hostname = hostname
        self.platform = platform
        self.platform_release = platform_release
        self.platform_version = platform_version
        self.user = user
        self.error_exception_id = error_exception_id


class ExecutionDetailsAttributes:
    def __init__(
        self,
        language: str,
        version: str,
        execution_finish_time: datetime,
        error_exception_id: int
    ) -> None:
        self.language = language
        self.version = version
        self.execution_finish_time = execution_finish_time
        self.error_exception_id = error_exception_id


class ExecutionArgumentAttributes:
    def __init__(
        self,
        argument: str,
        execution_details_id: int
    ) -> None:
        self.argument = argument
        self.execution_details_id = execution_details_id


class EnvironmentDetailsAttributes:
    def __init__(
        self,
        name: str,
        value: str,
        error_exception_id: int
    ) -> None:
        self.name = name
        self.value = value
        self.error_exception_id = error_exception_id


class ExtraDetailsAttributes:
    def __init__(
        self,
        name: str,
        value: str,
        is_json: bool,
        error_exception_id: int
    ) -> None:
        self.name = name
        self.value = value
        self.is_json = is_json
        self.error_exception_id = error_exception_id


class ModelSearchQuery:
    def __init__(
        self,
        limit: int,
        offset: int,
        where: Optional[Dict[str, Any]]=None,
        order: Optional[List[List[str]]]=None,
        include: Optional[List[Dict[str, Any]]]=None,
    ) -> None:
        self.limit = limit
        self.offset = offset
        self.where = where
        self.order = order
        self.include = include

class LogReporterOptions:
    def __init__(
        self,
        limit: Optional[int]=None,
        offset: Optional[int]=None,
        level: Optional[LogType]=None,
        group_name: Optional[LogGroup]=None,
    ) -> None:
        self.limit = limit
        self.offset = offset
        self.level = level
        self.group_name = group_name

class LogReporterSegments:
    def __init__(
        self,
        identifier: List[str]=None
    ) -> None:
        self.identifier = identifier

class LogReporterObject:
    def __init__(
        self,
        flow: str,
        datetime: str,
        level: LogType,
        content: str,
        group: Optional[LogGroup]=None,
    ) -> None:
        self.flow = flow
        self.datetime = datetime
        self.level = level
        self.content = content
        self.group = group
