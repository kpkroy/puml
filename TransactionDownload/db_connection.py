import psycopg2
import pandas.io.sql as psql
import sqlite3
from psycopg2.extras import RealDictCursor
from LocalConfig.log_handler import LogHandler
import os


class DbConnection:
    def __init__(self, lha):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)
        self.config = {'dbname': 'tenqube',
                       'user': 'tenqube',
                       'pwd': 'Tenqube19',
                       'host': 'transaction.tenqube.kr',
                       'port': '5439'
                       }
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(dbname=self.config['dbname'],
                                     host=self.config['host'],
                                     port=self.config['port'],
                                     user=self.config['user'],
                                     password=self.config['pwd'])
        self.conn.autocommit = True

    def fetch(self, sql_query):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql_query)
        self.logger.info(f'> Fetching : {sql_query}')
        fetch_result = cur.fetchall()
        self.logger.info(f'> Fetched : {len(fetch_result)}')
        return fetch_result

    def save_to_local_sql(self, sql_query_list, file_path, file_name):
        conn = sqlite3.connect(os.path.join(file_path, file_name))

        for sql_query in sql_query_list:
            self.logger.info(f'> Fetching : {sql_query}')
            df = psql.read_sql(sql_query, self.conn)
            df.to_sql('transactions', conn, if_exists='append', index=False)
            print('temp')
        conn.close()

    def close(self):
        self.conn.close()

