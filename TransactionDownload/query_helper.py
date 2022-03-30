from a_helper import fileHandler as fh


class QueryHelper:
    def __init__(self):
        self.default_query = f"SELECT person_id, id, pay_date, pay_hour, amount, keyword_search, company_name," \
                             f" franchise_name, category_large_id, category_medium_id, category_small_id" \
                             f" FROM public.transactions"

    def create_query_list(self, query_info, pool_path, pool_file):
        person_id = query_info.get('uid')
        f_date = query_info.get('from_date')
        t_date = query_info.get('to_date')
        c_query = query_info.get('query')

        if person_id:
            person_id_list = [person_id]
        else:
            person_id_list = []
        if pool_path and pool_file:
            try:
                temp = [x for x in fh.generate_from_csv(pool_path, pool_file)]
                for t in temp:
                    person_id_list.append(t.get('person_id'))
            except:
                pass
        if person_id_list:
            for p in person_id_list:
                yield self.create_default_query(f_date, t_date, p)
        else:
            return [self.default_query + f"WHERE pay_date >= '{f_date}' AND pay_date <= '{t_date}"]

    def create_default_query(self, from_date, to_date, user_id):
        query = self.default_query + f" WHERE person_id = '{user_id}' AND pay_date >= '{from_date}' AND pay_date <= '{to_date}'"
        return query

    @staticmethod
    def create_custom_query(from_date, to_date, c_query, user_id):
        query = c_query + f" WHERE person_id = '{user_id}' AND pay_date >= '{from_date}' AND pay_date <= '{to_date}'"
        return query

