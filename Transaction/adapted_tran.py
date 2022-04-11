from a_helper import tran_value_adapter as tva


class AdaptedTran:
    def __init__(self, tran: dict):
        self.tran = tran
        self.person_id = tran.get('person_id')
        self.id = tran.get('id')
        self.pay_date = tran.get('pay_date')
        self.pay_hour = tran.get('pay_hour')
        self.pay_hour_itv = tran.get('pay_hour_itv')
        self.amount = tran.get('amount')
        self.keyword_search = tran.get('keyword_search')
        self.company_name = tran.get('company_name')
        self.franchise_name = tran.get('franchise_name')
        self.cate_lid = tran.get('category_large_id')
        self.cate_mid = tran.get('category_medium_id')
        self.cate_sid = tran.get('category_small_id')
        self.has_category = self.check_category_code()

    def get_ori(self):
        return self.tran

    def check_category_code(self):
        if self.get_category_code in {'101010', '841010'}:
            # category code for not found,
            # category code for withdrawl
            return False
        else:
            return True

    def get_merged_keyword(self):
        if self.has_category:
            return ' '.join([self.keyword_search, self.company_name, self.franchise_name])
        else:
            return self.keyword_search

    def get_category_code(self):
        if self.has_category:
            return self.cate_lid + self.cate_mid + self.cate_sid
        else:
            return ''

    def get_pay_interval(self):
        if self.pay_hour_itv:
            return self.pay_hour_itv
        else:
            return tva.hour_adapter(int(self.pay_hour))

    def get_amount(self):
        try:
            float_amount = float(self.amount)
        except Exception as e:
            float_amount = 0
        return float_amount
