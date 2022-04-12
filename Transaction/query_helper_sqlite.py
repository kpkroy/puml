from Transaction.query_helper import QueryHelper
import datetime
from dateutil import relativedelta


class QueryHelperSQLite(QueryHelper):
    def __init__(self, lh=None):
        super().__init__(lh)
        self.default_columns = ['person_id', 'id', 'pay_year', 'pay_month', 'pay_hour',
                                'pay_day_of_week', 'ori_amount', 'installment_count',
                                'keyword_sms', 'currency_code', 'dw_type', 'fin_id', 'is_cancel_matched',
                                'person_gender', 'person_age',
                                'ori_pay_type', 'ori_pay_subtype', 'ori_pay_brand',
                                'company_id', 'company_name', 'company_address_si', 'company_address_gu',
                                'franchise_id', 'franchise_name', 'is_deleted', 'create_date']

    @staticmethod
    def get_query_pay_month(fd, td) -> []:
        from_date = datetime.datetime.strptime(fd, '%Y-%m-%d')

        if not td:
            return [from_date.strftime('%Y-%m-%d')]
        else:
            to_date = datetime.datetime.strptime(td, '%Y-%m-%d')

        if from_date == to_date:
            return [from_date.strftime('%Y-%m-%d')]
        else:
            # get interval months
            next_month = from_date
            result = []
            while next_month <= to_date:
                result.append(next_month)
                next_month = next_month + relativedelta.relativedelta(months=1)
            query_month = [x.strftime('%Y-%m-%d') for x in result]
        return query_month

    def create_query_list_by_month(self, query_info, person_id_list):
        pay_month = self.get_query_pay_month(query_info.get('from_date'), query_info.get('to_date'))
        table_name = query_info.get('table_name')
        if not table_name:
            table_name = 'public.transactions'

        for pm in pay_month:
            if person_id_list:
                for person_id in person_id_list:
                    yield 'SELECT ' + ', '.join(self.default_columns) + ' FROM ' + table_name + f" WHERE person_id = '{person_id}' AND pay_month = '{pay_month}' "
            else:
                yield 'SELECT ' + ', '.join(self.default_columns) + ' FROM ' + table_name + f" WHERE pay_month = '{pm}' limit 3000"


