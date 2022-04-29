from abc import ABC
from abc import abstractmethod
import datetime
from dateutil import relativedelta
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

    @staticmethod
    def generate_pay_period(fd, td):
        from_date = datetime.datetime.strptime(fd, '%Y-%m-%d')
        to_date = datetime.datetime.strptime(td, '%Y-%m-%d')

        if from_date == to_date:
            return [from_date.strftime('%Y-%m-%d')]
        else:
            next_month = from_date
            result = []
            while next_month <= to_date:
                result.append(next_month)
                next_month = next_month + relativedelta.relativedelta(months=1)
            query_month = [x.strftime('%Y-%m-%d') for x in result]
        return query_month

    '''
    def generate_pay_period(self, fd, td):
        from_date = datetime.datetime.strptime(fd, '%Y-%m-%d')
        try:
            to_date = datetime.datetime.strptime(td, '%Y-%m-%d')
        except Exception as e:
            self.logger.info('{0} - {1}: {2}'.format(fd, td, e))
            to_date = None
        if from_date == to_date:
            return [from_date.strftime('%Y-%m-%d')]
        else:
            next_month = from_date
            result = []
            while next_month <= to_date:
                result.append(next_month)
                next_month = next_month + relativedelta.relativedelta(months=1)
            query_month = [x.strftime('%Y-%m-%d') for x in result]
        return query_month
    '''