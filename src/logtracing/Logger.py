import os
import sys
import time
import psutil
import platform
import traceback
from typing import Union
from Types import PrepareStackTrace, CodeLine, ErrorStack, OsVars, PythonVars


class Logger:
    def __init__(self, flow: str):
        self._flow = flow
        self.prepare_stack_trace: PrepareStackTrace = traceback.extract_stack
        self.err_stack = None
        self.os_vars: Union[OsVars, None] = None
        self.python_vars: Union[PythonVars, None] = None
        self.env_vars: Union[os.environ, None] = None
        self.extra_vars = {}
        self.code_lines_limit: int = 5

    @property
    def flow(self):
        return self._flow

    def track_error(self, err) -> None:
        pass

    def report(self) -> None:
        pass

    def add_extra(self, identifier: str, extra) -> None:
        self.extra_vars[identifier] = extra

    def read_line(self, file_path: str, start: int, end: int) -> CodeLine:
        pass

    def use_custom_prepare_stack_trace(self) -> None:
        pass

    def restore_prepare_stack_trace(self) -> None:
        traceback.extract_stack = self.prepare_stack_trace

    def load_os_vars(self) -> None:
        self.os_vars = {
            "arch": platform.architecture(),
            "cpus": self.get_cpus_info(),
            "hostname": platform.node(),
            "machine": platform.machine(),
            "platform": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "user": {
                "username": psutil.users()[0].name,
                "uid": os.getuid(),
                "gid": os.getgid(),
            }
        }

    def get_cpus_info(self) -> list:
        cpus_info = []
        cpus = psutil.cpu_times(percpu=True)

        for cpu in cpus:
            cpu_data = {
                "model": platform.processor(),
                "speed": psutil.cpu_freq().current,
                "times": {
                    "user": cpu.user,
                    "nice": cpu.nice,
                    "sys": cpu.system,
                    "idle": cpu.idle,
                    "irq": cpu.irq
                }
            }

            cpus_info.append(cpu_data)

        return cpus_info

    def load_python_vars(self) -> None:
        self.python_vars = {
            "version": sys.version,
            "args": sys.argv,
            "datetime": int(time.time())
        }

    def load_env_vars(self) -> None:
        self.env_vars = os.environ
