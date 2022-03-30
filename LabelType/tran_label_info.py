from Adapters.tran_adapter import TranAdapter


class TranLabelInfo:
    def __init__(self, label_adapted):
        self.label_name = label_adapted.get('label_name')
        self.amount_min = label_adapted.get('amount_min')
        self.amount_max = label_adapted.get('amount_max')
        self.amount_exact = label_adapted.get('amount_exact')
        self.is_ignore_amount = label_adapted.get('is_ignore_amount')
        self.pay_at_min = label_adapted.get('pay_at_min')
        self.pay_at_max = label_adapted.get('pay_at_max')
        self.is_ignore_pay_at = label_adapted.get('is_ignore_pay_at')

    def test_amount(self, t) -> bool:
        if self.is_ignore_amount:
            return True
        else:
            if self.amount_exact:
                if self.amount_min == t.get_amount():
                    return True
                else:
                    return False
            else:
                if self.amount_min <= t.get_amount() <= self.amount_max:
                    pass
                else:
                    return False
        return True

    def test_pay_at(self, t) -> bool:
        if self.is_ignore_pay_at:
            return True
        else:
            if self.pay_at_min <= t.get_pay_interval() <= self.pay_at_max:
                return True
            else:
                return False

    def test_currency(self, t) -> bool:
        pass

    def check_conditions(self, t: TranAdapter) -> bool:
        if self.test_amount(t) is False:
            return False
        if self.test_pay_at(t) is False:
            return False
        if self.test_currency(t) is False:
            return False
        return True

    def get_name(self):
        return self.label_name
