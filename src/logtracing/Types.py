import traceback
from typing import List, Union


class PrepareStackTrace:
    """Represents a prepared stack trace."""
    def __init__(self, prepare_stack_trace: Union[BaseException, List[traceback.FrameSummary], None]):
        """Initialize with the given stack trace."""
        self.prepare_stack_trace = prepare_stack_trace


class CodeLine:
    """Represents a line of code within a stack trace."""
    def __init__(self, line: int, content: str, current_line: Union[int, None]):
        """Initialize with line number, content, and an optional marker for the current line."""
        self.line = line
        self.content = content
        self.current_line = current_line


class ErrorStack:
    """Encapsulates details of an error, including error name, message, stack, and code context."""
    def __init__(self, error_name: str, error_message: str, error_stack: str, function_name: str, file_name: str, line_number: int, column_number: int, code: List[CodeLine]):
        """Initialize with error details."""
        self.error_name = error_name
        self.error_message = error_message
        self.error_stack = error_stack
        self.function_name = function_name
        self.file_name = file_name
        self.line_number = line_number
        self.column_number = column_number
        self.code = code


class OsUser:
    """Represents an OS user, including username, user ID, and group ID."""
    def __init__(self, username: str, uid: int, gid: int):
        """Initialize with user details."""
        self.username = username
        self.uid = uid
        self.gid = gid


class OsCpuTime:
    """Encapsulates CPU time usage details."""
    def __init__(self, user: int, nice: int, sys: int, idle: int, irq: int):
        """Initialize with CPU times."""
        self.user = user
        self.nice = nice
        self.sys = sys
        self.idle = idle
        self.irq = irq


class OsCpu:
    """Represents details of a CPU, including model, speed, and times."""
    def __init__(self, model: str, speed: int, times: OsCpuTime):
        """Initialize with CPU details."""
        self.model = model
        self.speed = speed
        self.times = times


class OsVars:
    """Collects various OS-level details."""
    def __init__(self, arch: str, cpus: List[OsCpu], hostname: str, machine: str, platform: str, release: str, version: str, user: OsUser):
        """Initialize with OS-level details."""
        self.arch = arch
        self.cpus = cpus
        self.hostname = hostname
        self.machine = machine
        self.platform = platform
        self.release = release
        self.version = version
        self.user = user


class PythonVars:
    """Encapsulates Python-related variables."""
    def __init__(self, version: str, args: List[str], datetime: int):
        """Initialize with Python version, arguments, and a timestamp."""
        self.version = version
        self.args = args
        self.datetime = datetime
