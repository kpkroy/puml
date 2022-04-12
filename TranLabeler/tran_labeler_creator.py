from Transaction.adapted_tran import AdaptedTran
from TranLabeler.tran_label_info_adapter import AdapterTranLabelProd
from TranLabeler.tran_label_info_downloader import LabelerInfoDownloader
from a_LocalConfig.local_config import LocalConfig
from a_LocalConfig.log_handler import LogHandler
from TranLabeler.tran_labeler import TranLabeler


class TranLabelerCreator:
    def __init__(self):
        self.adapter = {'prod': AdapterTranLabelProd}

    def create(self, url, adapter_type):
        lid = LabelerInfoDownloader()
        label_info = lid.download(url, adapter_type)

        adapter = self.adapter.get(adapter_type)()
        labeler = TranLabeler()

        for li in label_info:
            labeler.add_label(adapter.adapt(li))
        return labeler


if __name__ == '__main__':
    lc = LocalConfig('profiler')
    conf = lc.configure_all()
    lh = LogHandler(conf['path']['date'])
    logger = lh.get_logger('profiler').info('> start profiling ')

    prod_url = 'https://docs.google.com/spreadsheets/d/17qBpAYLUT5YaujniLpxWKd9cPCW_xHQ8X-OPShjiEgs/edit#gid=0'
    adapter_type = 'prod'
    tc = TranLabelerCreator()
    prod_labeler = tc.create(prod_url, adapter_type)
    prod_labeler: TranLabeler

    label_result = []
    test_data = {}
    adapted_transaction = AdaptedTran(test_data)
    result = prod_labeler.find_labels(adapted_transaction)



