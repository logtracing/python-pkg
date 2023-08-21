from typing import Union
from db.models.log_group import LogGroup

class AbstractLogger:
    def __init__(self, flow: str):
        if not flow:
            raise ValueError('Flow argument is missing')

        self._flow = flow

    @property
    def flow(self) -> str:
        return self._flow

    async def get_or_create_group(self, name: str) -> Union[LogGroup, None]:
        try:
            group_name = name.lower()

            group, _ = await LogGroup.get_or_create(name=group_name)

            return group
        except Exception as err:
            print(err)
            return None
