from abc import ABC
from abc import abstractmethod
from a_LocalConfig.log_handler import LogHandler


class QueryHelper(ABC):
    def __init__(self, lh=None):
        if lh:
            self.lh = lh
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)

        self.default_columns = ['*']

    @abstractmethod
    def create_query_list_by_month(self, query_info: dict, person_id_list: list):
        pass
