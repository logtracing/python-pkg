import os
import traceback
from typing import Union
from Types import PrepareStackTrace, CodeLine, ErrorStack, OsVars, PythonVars


class Logger:
    def __init__(self, flow: str):
      self._flow = flow;
      self.prepare_stack_trace: PrepareStackTrace = traceback.extract_stack
      self.err_stack = None;
      self.os_vars: Union[OsVars, None] = None;
      self.python_vars: Union[PythonVars, None] = None;
      self.env_vars: Union[os.environ, None] = None;
      self.extra_vars = {};
      self.code_lines_limit: int = 5;

    @property
    def flow(self):
        return self._flow
