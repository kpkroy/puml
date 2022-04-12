from Transaction.tran_feeder import TransactionFeeder
from Transaction.query_helper_sqlite import QueryHelperSQLite
import sqlite3
from Transaction.adapted_tran import AdaptedTran
import os


class TransactionFeederSQLite(TransactionFeeder):
    def __init__(self,
                 from_date,
                 to_date,
                 table_name,
                 uid_list: list,
                 source_path, source_file, lha=None):

        super().__init__(lha)
        self.query_info = {'from_date': from_date,
                           'to_date': to_date,
                           'table_name': table_name}
        self.uid_list = uid_list
        self.source_path = source_path
        self.source_file = source_file
        self.qh = QueryHelperSQLite()

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

    tf = TransactionFeederSQLite(f_date, t_date, table, [uid], r'C:\Users\runqu\PycharmProjects\ProfileData'
                                                               r'\downloadedDb', 'syrup-part1.db')
    for i in tf.generate():
        print(i.get_ori_data())
    print('a')

