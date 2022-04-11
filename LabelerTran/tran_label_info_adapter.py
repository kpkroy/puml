from LocalConfig.log_handler import LogHandler


class AdapterTranLabelGS:
    def __init__(self, lha=None):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)

    def adapt(self, line_data) -> dict:
        label_adapted = {
                         'label_name': line_data.get('label_name'),
                         'keyword': line_data.get('keyword'),
                         'category_code': line_data.get('category_code'),
                         'amount_min': 0,
                         'amount_max': 0,
                         'amount_exact': False,
                         'is_ignore_amount': False,
                         'pay_at_min': 0,
                         'pay_at_max': 0,
                         'is_ignore_pay_at': False
                         }
        label_adapted.update(self.process_amount(line_data))
        label_adapted.update(self.process_pay_at(line_data))
        return label_adapted

    def process_amount(self, line_data) -> dict:
        amount_min = line_data.get('amount_min').replace(',', '')
        amount_max = line_data.get('amount_max').replace(',', '')
        is_ignore_amount = False
        amount_exact = 0
        float_amount_min = 0
        float_amount_max = 0

        if amount_min == "" and amount_max == "":
            is_ignore_amount = True
        else:
            try:
                float_amount_min = float(amount_min)
                float_amount_min = float(amount_max)
                if amount_min == amount_max:
                    amount_exact = float_amount_min
            except:
                self.logger.exception(f'>>amount conversion failed at {line_data.get("label_name")}: min[{amount_min}] | amount max [{amount_max}]')
                is_ignore_amount = True

        return {'amount_min': float_amount_min,
                'amount_max': float_amount_max,
                'amount_exact': amount_exact,
                'is_ignore_amount': is_ignore_amount}

    def process_pay_at(self, line_data):
        # line_data : each transaction label condition
        at_min = line_data.get('pay_at_min')
        at_max = line_data.get('pay_at_max')

        is_ignore_pay_at = False
        pay_at_min = 0
        pay_at_max = 0
        if at_min == "" and at_max == "":
            is_ignore_pay_at = True
        elif at_min == "0" and at_max == "24":
            is_ignore_pay_at = True
        else:
            try:
                pay_at_min = int(at_min)
                pay_at_max = int(at_max)
            except:
                self.logger.exception(f'>> at conversion failed at id {line_data.get("label_name")} : min[{at_min}] | max [{at_max}]')
                is_ignore_pay_at = True

        return {'pay_at_min': pay_at_min,
                'pay_at_max': pay_at_max,
                'is_ignore_pay_at': is_ignore_pay_at}
