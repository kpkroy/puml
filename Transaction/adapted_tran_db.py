from Transaction.adapted_tran import AdaptedTran


class AdaptedTranDb(AdaptedTran):
    def __init__(self, tran: dict):
        super().__init__(tran)
        self.pay_date = tran.get('pay_month')
        self.keyword = tran.get('keyword_sms', '')

    def get_pay_hour_itv(self):
        if self.pay_hour_itv:
            return self.pay_hour_itv
        else:
            return self.adapt_hour_itv(int(self.pay_hour))


