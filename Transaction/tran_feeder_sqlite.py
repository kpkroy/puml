from Transaction.query_helper_sqlite import QueryHelper
import sqlite3
from a_LocalConfig.log_handler import LogHandler
from Transaction.adapted_tran import AdaptedTran
import os


class TransactionFeeder:
    def __init__(self,
                 from_date,
                 to_date,
                 table_name,
                 uid_list: list,
                 source_path, source_file, lha=None):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)
        self.query_info = {'from_date': from_date,
                           'to_date': to_date,
                           'table_name': table_name}
        self.uid_list = uid_list
        self.source_path = source_path
        self.source_file = source_file
        self.qh = QueryHelper()
        self.query = ''

    def generate(self) -> [AdaptedTran]:
        conn = sqlite3.connect(os.path.join(self.source_path, self.source_file))
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        query_list = self.qh.create_query_list_by_month(self.query_info, self.uid_list)
        for query in query_list:
            self.logger.info(f'> Fetching : {query}')
            cur.execute(query)
            fetch_result = cur.fetchall()
            self.logger.info(f'> Fetched : {len(fetch_result)}')
            for transaction in fetch_result:
                yield AdaptedTran(dict(transaction))


if __name__ == '__main__':
    uid = '000033dca27df2a32a04692394f164de'
    f_date = '2021-01-01'
    t_date = '2021-03-01'
    table = 'transactions'

    tf = TransactionFeeder(f_date,
                           t_date,
                           table,
                           [uid],
                           r'C:\Users\runqu\PycharmProjects\ProfileData\downloadedDb',
                           'syrup-part1.db')
    for i in tf.generate():
        print(i.get_ori())
    print('a')

