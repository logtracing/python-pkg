import os
import sys
import json
import time
import psutil
import logging
import platform
import traceback
from typing import Union
from abstract_logger import AbstractLogger

class ExceptionLogger(AbstractLogger):
    def __init__(
      self,
      flow: str
    ) -> None:
        super().__init__(flow)
        self.prepare_stack_trace = traceback.extract_stack
        self.err_stack = []
        self.os_vars = None
        self.python_vars = None
        self.env_vars = None
        self.extra_vars = {}
        self.code_lines_limit = 5

    def add_extra(
        self,
        identifier: str,
        extra: Union[dict, str]
    ) -> None:
        if not isinstance(extra, (dict, str)):
            raise ValueError('<extra> must be dict or str')

        value = json.dumps(extra) if isinstance(extra, dict) else extra
        self.extra_vars[identifier] = value

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
        except AttributeError:
            pass
        except OSError as error:
            logging.error('OS error in ExceptionLogger at load_os_vars: %s', error)
        except Exception as error:
            logging.error('Unexpected error in ExceptionLogger at load_os_vars: %s', error)

    def get_cpus_info(
        self
    ) -> list:
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
        except AttributeError:
            pass
        except FileNotFoundError:
            pass
        except psutil.AccessDenied as error:
            logging.error('Permission denied in ExceptionLogger at get_cpus_info: %s', error)
        except psutil.TimeoutExpired as error:
            logging.error('Timeout expires and process still alive in ExceptionLogger at get_cpus_info: %s', error)
        except Exception as error:
            logging.error('Unexpected error in ExceptionLogger at get_cpus_info: %s', error)

    def load_python_vars(self) -> None:
        try:
            self.python_vars = {
                "version": sys.version,
                "args": sys.argv,
                "datetime": int(time.time())
            }
        except Exception as error:
            logging.error('Unexpected error in ExceptionLogger at load_python_vars: %s', error)

    def load_env_vars(self) -> None:
        self.env_vars = os.environ
