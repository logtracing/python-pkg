import logging
import traceback
from typing import Union
from pymysql import DatabaseError
from db.models.log_group import LogGroup

class AbstractLogger:
    def __init__(self, flow: str):
        if not flow:
            raise ValueError('Flow argument is missing')

        self._flow = flow

    @property
    def flow(self) -> str:
        return self._flow

    def get_or_create_group(
        self,
        name: str
    ) -> Union[LogGroup, None]:
        try:
            group_name = name.lower()
            group, _ = LogGroup.get_or_create(name=group_name)

            return group
        except DatabaseError as error:
            logging.error('An error occurred while trying to get or create a group: %s', error)
        except Exception as error:
            logging.error('Unexpected error in AbstractLogger at get_or_create_group: %s', error)
            return None
