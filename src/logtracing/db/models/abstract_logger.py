import traceback
from typing import Union
from db.models.log_group import LogGroups

class AbstractLogger:
    def __init__(self, flow: str):
        if not flow:
            raise ValueError('Flow argument is missing')

        self._flow = flow

    @property
    def flow(self) -> str:
        return self._flow

    def get_or_create_group(self, name: str) -> Union[LogGroups, None]:
        try:
            group_name = name.lower()

            group, _ = LogGroups.get_or_create(name=group_name)

            return group
        except:
            traceback.print_exc()
            return None
