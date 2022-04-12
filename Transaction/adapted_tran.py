from abc import ABC


class AdaptedTran(ABC):
    def __init__(self, tran: dict):
        self.tran = tran
        self.person_id = tran.get('person_id', '')
        self.id = tran.get('id', '')
        self.pay_date = tran.get('pay_date', '')
        self.pay_hour = tran.get('pay_hour', '')
        self.pay_hour_itv = tran.get('pay_hour_itv', '')
        self.amount = tran.get('ori_amount', '')
        self.currency_code = tran.get('currency_code')
        self.dw_type = tran.get('dw_type')
        self.canceled_match = tran.get('is_cancel_matched')
        self.keyword = tran.get('keyword_search', '')
        self.company_name = tran.get('company_name', '')
        self.franchise_name = tran.get('franchise_name', '')
        self.cate_lid = tran.get('ori_category_large_id', '')
        self.cate_mid = tran.get('ori_category_medium_id', '')
        self.cate_sid = tran.get('ori_category_small_id', '')
        self.cate_code = self.cate_lid + self.cate_mid + self.cate_sid
        self.use_category = self.check_category_code()

    def get_ori_data(self):
        return self.tran

    def get_person_id(self):
        return self.person_id

    def get_tran_id(self):
        return self.id

    def get_pay_date(self):
        return self.pay_date

    def get_pay_hour(self):
        return self.pay_hour

    def get_pay_hour_itv(self):
        return self.pay_hour_itv

    def get_amount(self):
        try:
            float_amount = float(self.amount)
        except Exception as e:
            float_amount = 0
        return float_amount

    def get_currency(self):
        return self.currency_code

    def get_dw_type(self):
        return self.dw_type

    def is_canceled_match(self):
        return self.canceled_match

    def get_keyword(self):
        return self.keyword

    def get_company_name(self):
        return self.company_name

    def get_franchise_name(self):
        return self.franchise_name

    def get_merged_keyword(self):
        return ' '.join([self.keyword, self.company_name, self.franchise_name])

    def check_category_code(self):
        if self.cate_code in {'101010', '841010'}:
            # category code for not found,
            # category code for withdrawl
            return False
        elif self.cate_code == '':
            return False
        else:
            return True

    def get_cate_code(self):
        return self.cate_code

    @staticmethod
    def adapt_hour_itv(hour: int) -> int:
        return int(hour/3) + 1

