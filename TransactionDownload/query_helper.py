from a_helper import fileHandler as fh


class QueryHelper:
    def __init__(self, query_info, pool_path):
        self.default_query = f"SELECT person_id, id, pay_date, pay_hour, amount, keyword_search, company_name," \
                             f" franchise_name, category_large_id, category_medium_id, category_small_id" \
                             f" FROM public.transactions"

        self.f_date = query_info.get('from_date')
        self.t_date = query_info.get('to_date')
        self.customary_query = query_info.get('customary_q')
        self.person_id = query_info.get('uid')
        self.pool_file = query_info.get('pool_file')
        self.pool_path = pool_path

    def create_query_list(self):
        if self.person_id:
            return [self.create_default_query(self.f_date, self.t_date, self.person_id)]
        else:
            person_id_list = fh.generate_from_csv(self.pool_path, self.pool_file)
            for p in person_id_list:
                person_id = p.get('person_id')
                yield self.create_default_query(self.f_date, self.t_date, person_id)

    def create_default_query(self, from_date, to_date, user_id):
        query = self.default_query + f" WHERE person_id = '{user_id}' AND pay_date >= '{from_date}' AND pay_date <= '{to_date}'"
        return query

    def create_custom_query(self, from_date, to_date, user_id):
        query = self.customary_query + f" WHERE person_id = '{user_id}' AND pay_date >= '{from_date}' AND pay_date <= '{to_date}'"
        return query

