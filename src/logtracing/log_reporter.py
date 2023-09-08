from peewee import *
from datetime import datetime
from typing import List, Dict, Optional, Any
from db.models.log_group import LogGroup
from logger import LogModel
from base_classes import ModelSearchQuery, LogType, SlackMessageSection, LogReporterOptions, LogReporterSegments, LogReporterObject

class LogReporter:

    def __init__(
        self,
        flow: str):
        self.flow = flow
        DEFAULT_LIMIT = 50
        DEFAULT_OFFSET = 0

    def get_basic_logs(
        self,
        options: LogReporterOptions = {}
        ) -> List[str]:
        QUERY: ModelSearchQuery = 
        return

    def get_logs(
        self,
        options: LogReporterOptions = {}
        ) -> List[str]:
        return

    def _format(self,
        log: LogModel,
        segments: LogReporterSegments = Dict
        ) -> str:
        new_Segments = [
            f'{log["level"]}'.ljust(5),
            f'[{self._format_date(log["created_at"])}]'
        ]

        for segment in segments:
            if segments[segment]:
                new_Segments.append(f'[{segment}]')

        return ''.join(new_Segments) + ': ' + log['content']
    
    def _format_date(self,
        date: datetime
        ) -> str:
        date_str = date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        date_str = date_str[:19].replace('T', ' ')
        return date_str
    