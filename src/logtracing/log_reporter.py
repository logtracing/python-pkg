from typing import List
from datetime import datetime
from logger import LogModel, LogGroupModel
from base_classes import LogReporterOptions

class LogReporter:

    def __init__(
        self,
        flow: str
    ):
        self.flow = flow
        self._default_limit = 50
        self._default_offset = 0

    def get_basic_logs(
            self,
            options: LogReporterOptions = LogReporterOptions()
        ) -> List[str]:

        options = options or {}


        offset = getattr(options, 'offset', self._default_offset) or self._default_offset
        limit = getattr(options, 'limit', self._default_limit) or self._default_limit

        query = (
            LogModel
                .select()
                .where(LogModel.flow == self.flow)
                .order_by(LogModel.created_at.desc())
                .paginate(
                    offset,
                    limit
                )
        )

        if 'level' in options:
            query = query.where(LogModel.level == options['level'])

        if 'group_name' in options:
            query = (
                query
                .join(LogGroupModel, on=(LogModel.log_group == LogGroupModel.id))
                .where(LogGroupModel.name == options['group_name'].name.lower())
            )

        data = query.execute()

        return [self._format(log, {'group': options.get('group_name')}) for log in data]


    def _format(self, log, segments=None):
        segments = segments or {}

        level_segment = f"[{log.level.ljust(5)}]"
        date_segment = f"[{self._format_date(log.created_at)}]"
        segments_format = [level_segment, date_segment]

        for _, value in segments.items():
            if value:
                segments_format.append(f"[{value}]")

        return f"{''.join(segments_format)}: {log.content}"

    def _format_date(self, date: datetime) -> str:
        return date.strftime('%Y-%m-%d %H:%M:%S')
