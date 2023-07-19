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
            raise Exception('Flow argument is missing')

        self._flow = flow
        self.prepare_stack_trace: PrepareStackTrace = traceback.extract_stack
        self.err_stack: Union[ErrorStack, None] = None
        self.os_vars: Union[OsVars, None] = None
        self.python_vars: Union[PythonVars, None] = None
        self.env_vars: Union[os.environ, None] = None
        self.extra_vars = {}
        self.code_lines_limit: int = 5

    @property
    def flow(self):
        return self._flow

    def track_error(self, err) -> None:
        if not err:
            raise Exception('Error argument is missing')

    def report(self) -> None:
        self.load_os_vars()
        self.load_python_vars()
        self.load_env_vars()
        self.use_custom_prepare_stack_trace()

        #print(self.err_stack)
        #print(self.os_vars)
        #print(self.env_vars)
        print(self.python_vars)
        #print(self.extra_vars)

    def add_extra(self, identifier: str, extra) -> None:
        if not isinstance(extra, dict) and not isinstance(extra, str):
            raise Exception('extra must be dict or str')

        extra = json.dumps(extra) if isinstance(extra, dict) else extra
        self.extra_vars[identifier] = extra

    def read_lines(self, file_path: str, start: int, end: int) -> CodeLine:
        lines = []
       
        with open(file_path, 'r') as file:
            file_content = file.readlines()

            for i in range(start -1, end):
                line_number = i+1
                line_content = file_content[i].rstrip('\n')
                lines.append({
                   'line': line_number,
                   'content': line_content
                })

        return lines


    def use_custom_prepare_stack_trace(self) -> None:
        [traceback_string] = traceback.format_tb(e.__traceback__)
        print(traceback_string)
        file, line_number, line_content = traceback_string.split(',')
        file_path = file.split('"')[1]
        line_number = line_number.strip().split(' ')[1]
        line_content = line_content.split('>')[1].strip()
        code = []

        if file_path: 
            code = self.read_lines(file_path, int(line_number) - self.code_lines_limit, int(line_number) + self.code_lines_limit)

        obj = {
            "file_path": file_path,
            "line_number": line_number,
            "line_content": line_content,
            "code": code,
        }

        print(obj)

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

# Testing code
if __name__ == '__main__':
    logger = Logger('OH')
    logger.add_extra('test_extra_var', {
        "algo": 0
    })

    try:
        res1 = 10+2
        res2 = 10/0
        res3 = 10/5
    except Exception as e:
        # logger.add_extra('one_more_extra_vars', 'test')

        # This is throw in an expection
        # logger.add_extra('one_more_extra_vars', 0)
        # logger.track_error('')
        logger.report()
