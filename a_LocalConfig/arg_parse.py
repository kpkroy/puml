import argparse


class DBDownloadArgs:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--from_date", type=str, help="query start date in YYYY-MM-DD", default="2022-02-01")
        parser.add_argument("--to_date", type=str, help=" query start date in YYYY-MM-DD", default="")
        parser.add_argument("--query", type=str, help="custom query", default="")
        parser.add_argument("--uid", type=str, help="person id. separate by comma",
                            default="5a7eba8617477c814f067302c7841c1e")
        parser.add_argument("--pool_file", type=str, help="csv pool file name", default="high_sample.csv")
        self.args = parser.parse_args()

    def get_query_info(self):
        return {'from_date': self.args.from_date,
                'to_date': self.args.to_date,
                'query': self.args.query}

    def get_pool_id_list(self):
        return self.args.uid.split(',')

    def get_pool_file(self):
        return self.args.pool_file

    def get_db_file_prefix(self) -> str:
        return f'{self.args.from_date}-{self.args.to_date}'

    '''
    def get_arg_parse() -> dict:
        parser = argparse.ArgumentParser()
        parser.add_argument("--shop_url", help="shop url to proceed. Use comma. all for all.", type=str, default="all")
        parser.add_argument("--vendor", type=str, help="Vendor. Use comma. all for all.", default="all")
        parser.add_argument("--cur", type=str, help="Currency. Use comma. all for all.", default='all')
        parser.add_argument("--lang", type=str, help="language. Use comma. all for all.", default='all')
        parser.add_argument('--is_cont', action="store_true", help='skips file already downloaded')
        parser.add_argument("--demo", type=str, default='Womens,Unisex,Mens',
                            help="valid demo. Use comma. all for all. Womens, Mens, Unisex, Infants, Kids, Maternity")
        parser.add_argument("--split", help='shopify split same product, different price', action="store_true")
        parser.add_argument("--remove_detail", action="store_true", help='removes detail in export format such as pattern')
        parser.add_argument("--send", action="store_true", help="send to server")
        '''




