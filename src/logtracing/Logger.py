import traceback
from typing import Optional, Union
from pymysql import DatabaseError

from db.models.log import Log
from db.models.main import BaseModel
from abstract_logger import AbstractLogger
from base_classes import LogTracingOptions, LoggingOptions, LogAttributes, LogType


class Logger(AbstractLogger):
    def __init__(
        self,
        flow: str,
        options: Optional[LogTracingOptions]=None
    ) -> None:
        super().__init__(flow)
        self.options = options
        self._slack_integration = False

        if options and options.slack_integration:
            self._slack_integration = options.slack_integration

    @property
    def slack_integrations(self) -> bool:
        return self._slack_integration

    def trace(
        self,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            return self.save(LogType.types['TRACE'], content, opts)
        except RuntimeError as error:
            print(f'An error has occurred while saving the trace log: {error}')
            traceback.print_exc()

    def debug(
        self,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            return self.save(LogType.types['DEBUG'], content, opts)
        except RuntimeError as error:
            print(f'An error has occurred while saving the debug log: {error}')
            traceback.print_exc()

    def info(
        self,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            return self.save(LogType.types['INFO'], content, opts)
        except RuntimeError as error:
            print(f'An error has occurred while saving the info log: {error}')
            traceback.print_exc()

    def warn(
        self,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            return self.save(LogType.types['WARN'], content, opts)
        except RuntimeError as error:
            print(f'An error has occurred while saving the warning log: {error}')
            traceback.print_exc()

    def error(
        self,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            return self.save(LogType.types['ERROR'], content, opts)
        except RuntimeError as error:
            print(f'An error has occurred while saving the error log: {error}')
            traceback.print_exc()

    def fatal(
        self,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            return self.save(LogType.types['FATAL'], content, opts)
        except RuntimeError as error:
            print(f'An error has occurred while saving the fatal log: {error}')
            traceback.print_exc()

    def save(
        self,
        level: str,
        content: str,
        opts: Union[LoggingOptions, None]
    ) -> Log:
        try:
            log = ''
            database = BaseModel._meta.database

            data: LogAttributes = {
                'level': level,
                'flow': self.flow,
                'content': content
            }

            # TODO refactor the condition
            # if opts and opts.group:
            #     data.log_group_id = opts.group.id

            with database.atomic():
                log = Log.create(
                    level=data['level'],
                    flow=data['flow'],
                    content=data['content']
                )

            return log
        except DatabaseError as error:
            print(f'An error has occurred while saving the log: {error}')
            traceback.print_exc()

