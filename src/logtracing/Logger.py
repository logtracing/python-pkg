import os
import sys
import json
import time
import psutil
import platform
import traceback
from typing import Union
from Types import CodeLine, ErrorStack, PythonVars, OsVars, PrepareStackTrace


class Logger:
    def __init__(self, flow: str):
        if not flow:
            raise ValueError('Flow argument is missing')

        self._flow = flow
        self.prepare_stack_trace: PrepareStackTrace = traceback.extract_stack
        self.err_stack: Union[ErrorStack, None] = None
        self.os_vars: Union[OsVars, None] = None
        self.python_vars: Union[PythonVars, None] = None
        self.env_vars: Union[os.environ, None] = None
        self.extra_vars = {}
        self.code_lines_limit: int = 5

    @property
    def flow(self) -> str:
        return self._flow

    def track_error(self, err) -> None:
        if not err:
            raise ValueError('Error argument is missing')

    def report(self) -> None:
        try:
            self.load_os_vars()
            self.load_python_vars()
            self.load_env_vars()
        except Exception as error:
            print(f"An error occurred while loading variables: {error}")
            return

        print(self.err_stack)
        print(self.os_vars)
        print(self.env_vars)
        print(self.python_vars)
        print(self.extra_vars)

    def add_extra(self, identifier: str, extra) -> None:
        if not identifier:
            raise ValueError('Identifier must not be empty')
        if not isinstance(extra, (dict, str)):
            raise ValueError('Extra must be dict or str')

        extra = json.dumps(extra) if isinstance(extra, dict) else extra
        self.extra_vars[identifier] = extra

    def read_line(self, file_path: str, start: int, end: int) -> CodeLine:
        pass

    def use_custom_prepare_stack_trace(self) -> None:
        pass

    def restore_prepare_stack_trace(self) -> None:
        traceback.extract_stack = self.prepare_stack_trace

    def load_os_vars(self) -> None:
        try:
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
        except Exception as error:
            raise RuntimeError(f"An error occurred while loading OS variables: {error}") from error

    def get_cpus_info(self) -> list:
        try:
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
        except Exception as error:
            raise RuntimeError(f"An error occurred while getting CPU info: {error}") from error

    def load_python_vars(self) -> None:
        try:    
            self.python_vars = {
                "version": sys.version,
                "args": sys.argv,
                "datetime": int(time.time())
            }
        except Exception as error:
            raise RuntimeError(f"An error occurred while loading Python variables: {error}") from error

    def load_env_vars(self) -> None:
        try:
            self.env_vars = os.environ
        except Exception as error:
            raise RuntimeError(f"An error occurred while loading environment variables: {error}") from error
