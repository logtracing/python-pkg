import logging
from typing import Optional, Union
from pymysql import DatabaseError

from logtracing.db.models.main import BaseModel
from logtracing.db.models.log import Log as LogModel
from logtracing.abstract_logger import AbstractLogger
from logtracing.base_classes import LogTracingOptions, LoggingOptions, LogAttributes, LogType
from logtracing.slack_message_sender import SlackMessageSender


class Logger(AbstractLogger):
    def __init__(
        self,
        flow: str,
        options: Optional[LogTracingOptions]=None
    ) -> None:
        super().__init__(flow)
        self.options = options
        self._slack_integration = False

        if options\
            and isinstance(options, dict) \
            and options.get('slack_integration'):
            self._slack_integration = options['slack_integration']

    @property
    def slack_integrations(self) -> bool:
        return self._slack_integration

    def trace(
        self,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            return self.save(LogType.types['TRACE'], content, options)
        except Exception as error:
            logging.error('An error has occurred while saving the trace log: %s', error)

    def debug(
        self,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            return self.save(LogType.types['DEBUG'], content, options)
        except Exception as error:
            logging.error('An error has occurred while saving the debug log: %s', error)

    def info(
        self,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            return self.save(LogType.types['INFO'], content, options)
        except Exception as error:
            logging.error('An error has occurred while saving the info log: %s', error)

    def warn(
        self,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            return self.save(LogType.types['WARN'], content, options)
        except Exception as error:
            logging.error('An error has occurred while saving the warn log: %s', error)

    def error(
        self,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            return self.save(LogType.types['ERROR'], content, options)
        except Exception as error:
            logging.error('An error has occurred while saving the error log: %s', error)

    def fatal(
        self,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            return self.save(LogType.types['FATAL'], content, options)
        except Exception as error:
            logging.error('An error has occurred while saving the fatal log: %s', error)

    def save(
        self,
        level: str,
        content: str,
        options: Union[LoggingOptions, None]=None
    ) -> LogModel:
        try:
            log = None
            database = BaseModel._meta.database

            data: LogAttributes = {
                'level': level,
                'flow': self.flow,
                'content': content
            }

            if options\
                and isinstance(options, dict)\
                and options.get('group'):
                data['log_group_id'] = options['group'].id

            with database.atomic():
                log = LogModel.create(
                    level=data['level'],
                    flow=data['flow'],
                    content=data['content'],
                    log_group=data.get('log_group_id')
                )

            if self._slack_integration:
                slack_sender = SlackMessageSender.get_instance()
                message = slack_sender.get_base_message_template(
                    title = self.flow,
                    log = log
                )

                if options\
                    and isinstance(options, dict)\
                    and options.get('slack_message_extra_sections'):
                    message['blocks'].append(options['slack_message_extra_sections'])

                slack_sender.publish_message(message)

            return log
        except DatabaseError as error:
            logging.error('Database error in Logger at save: %s', error)
        except Exception as error:
            logging.error('Unexpected error in Logger at save: %s', error)
