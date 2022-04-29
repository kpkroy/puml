from a_LocalConfig.local_config import LocalConfig
from Transaction.query_helper_sqlite import QueryHelper
from a_helper.db_connection import DbConnection
from a_LocalConfig.arg_parse import DBDownloadArgs
from Transaction.pool import Pool
from a_LocalConfig.log_handler import LogHandler


class DownloadFromDB:
    def __init__(self, f_path, f_name, lha=None):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)
        self.tran_file_name = f_name
        self.tran_file_path = f_path

    def download(self, query_info, pool_id_list):
        qh = QueryHelper()
        query_list = qh.create_query_list_by_month(query_info, pool_id_list)
        db = DbConnection(self.lh)
        db.connect()
        db.save_to_local_sql(query_list, self.tran_file_path, self.tran_file_name)
        db.close()


if __name__ == '__main__':
    lc = LocalConfig()
    conf = lc.configure_all()
    date = conf['prefix']['date']

    args = DBDownloadArgs()
    file_name = f'{args.get_db_file_prefix()}-{date}.db'
    file_path = conf['path']['tempDb']

    downloader = DownloadFromDB(file_path, file_name)
    pm = Pool(args.get_pool_id_list(), conf['path']['pool'], args.get_pool_file())
    downloader.download(args.get_query_info(), pm.get_user_id_list())

