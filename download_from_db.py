from LocalConfig.arg_parse import DBDownloadArgs
from LocalConfig.local_config import LocalConfig
from TransactionDownload.query_helper import QueryHelper
from TransactionDownload.db_connection import DbConnection
from LocalConfig.log_handler import LogHandler


class DownloadFromDB:
    def __init__(self, f_path, f_name, lha=None):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)
        self.tran_file_name = f_name
        self.tran_file_path = f_path

    def download(self, query_info, p_path, p_file_name):
        qh = QueryHelper()
        query_list = qh.create_query_list(query_info, p_path, p_file_name)
        db = DbConnection(self.lh)
        db.connect()
        db.save_to_local_sql(query_list, self.tran_file_path, self.tran_file_name)
        db.close()
        return p_file_name


if __name__ == '__main__':
    lc = LocalConfig()
    conf = lc.configure_all()
    date = conf['prefix']['date']

    args = DBDownloadArgs()
    file_name = f'{args.get_db_file_prefix()}-{date}.db'
    file_path = conf['path']['tempDb']

    tf = DownloadFromDB(file_path, file_name)
    pool_path = conf['path']['pool']
    pool_file_name = args.get_pool_file()

    tf.download(args.get_query_info(), pool_path, pool_file_name)

