from typing import List, Union
import traceback

class PrepareStackTrace:
  def __init__(self, prepare_stack_trace: Union[BaseException, List[traceback.FrameSummary], None]):
    self.prepare_stack_trace =  prepare_stack_trace

class CodeLine:
  def __init__(self, line: int, content: str, current_line: Union[int, None]):
    self.line = line
    self.content = content
    self.current_line = current_line

class ErrorStack:
  def __init__(self, err_message: str, function_name: str, file_name: str, line_number: int, column_number: int, code: List[CodeLine]):
    self.err_message = err_message,
    self.function_name = function_name
    self.file_name = file_name
    self.line_number = line_number
    self.column_number = column_number
    self.code = code


class OsUser:
  def __init__(self, username: str, uid: int, gid: int):
    self.username = username,
    self.uid = uid
    self.gid = gid

class OsCpuTime:
  def __init__(self, user: int, nice: int, sys: int, idle: int, irq: int):
    self.user = user
    self.nice = nice
    self.sys = sys
    self.idle = idle
    self.irq = irq

class OsCpu:
  def __init__(self, model: str, speed: int, times: OsCpuTime):
    self.model = model
    self.speed = speed
    self.times = times

class OsVars:
  def __init__(self, arch: str, cpus: List[OsCpu], hostname: str, machine: str, platform: str, release: str, version: str, user: OsUser):
    self.arch = arch
    self.cpus = cpus
    self.hostname = hostname
    self.machine = machine
    self.platform = platform
    self.release = release
    self.version = version
    self.user = user

class PythonVars:
  def __init__(self, version: str, args: List[str], datetime: int):
    self.version = version
    self.args = args
    self.datetime = datetime
