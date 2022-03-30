import argparse


class ProfilerArgs:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--work_date", type=str, help="work date YYYY-MM-DD. "
                                                          "\n Empty for previous date. 'renew' to create new working date.",
                            default="")
        parser.add_argument("--data_source", type=str, help="stock, db, downloaded. choose one", default="downloaded")
        parser.add_argument("--from_date", type=str, help="for stock & db. query start date in YYYY-MM-DD", default="2022-02-01")
        parser.add_argument("--to_date", type=str, help="for stock & db. query start date in YYYY-MM-DD", default="2022-02-28")
        parser.add_argument("--uid", type=str, help="for stock & db. person id", default="")
        parser.add_argument("--pool_file", type=str, help="for stock & db. csv pool file name", default="high_sample.csv")
        parser.add_argument("--query", type=str, help="if db. custom query", default="")
        self.args = parser.parse_args()

    def get_working_date(self) -> str:
        return self.args.work_date

    def get_query_info(self) -> dict:
        query_info = {'from_date': self.args.from_date,
                      'to_date': self.args.to_date,
                      'uid': self.args.uid,
                      'pool_file': self.args.pool_file,
                      'custom_q': self.args.query}

        return query_info

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




