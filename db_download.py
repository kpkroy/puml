import argparse
from TransactionDownload.db_connection import DbConnection
from TransactionDownload.query_helper import QueryHelper


class DownloadFromDb:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--from_date", type=str, default="2021-02-01")
        parser.add_argument("--to_date", type=str, default="2021-02-28")
        parser.add_argument("--pool_file", type=str, default="")
        parser.add_argument("--uid", type=str, default='5a7eba8617477c814f067302c7841c1e')
        parser.add_argument("--query", type=str, default="")


