from TransactionDownload.query_helper import QueryHelper
from TransactionDownload.db_connection import DbConnection
import a_helper.fileHandler as fh
from LocalConfig.log_handler import LogHandler


class TransactionFeeder:
    def __init__(self, date_path, transaction_file_name, lha=None):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)
        self.date_path = date_path
        self.tran_file_name = transaction_file_name

    def prepare_transaction(self, query_info, pool_path):
        qh = QueryHelper(query_info, pool_path)
        query_list = qh.create_query_list()
        db = DbConnection(self.lh)
        db.connect()
        for each_person in query_list:
            fh.export_csv_local(self.date_path, self.tran_file_name, db.fetch(each_person), opt='a+')

    def transaction_file_exists(self) -> bool:
        if self.tran_file_name in fh.get_valid_file_list(self.date_path, ""):
            return True
        else:
            return False

    def yield_from_file(self):
        return fh.generate_from_csv(self.date_path, self.tran_file_name)


if __name__ == '__main__':
    uid = '5a7eba8617477c814f067302c7841c1e'
    f_date = '2022-02-01'
    t_date = '2022-02-28'

    q_info ={'from_date': f_date,
             'to_date': t_date,
             'uid': uid}

    tf = TransactionFeeder('date_path', 'tran_file_name')
    print(tf.yield_from_file())
