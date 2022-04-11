from LabelerTran.labeler_tran import TranLabeler
from LabelerTran.tran_label_info_adapter import AdapterTranLabelGS
import requests
from io import StringIO
import csv


class TranLabelerCreator:
    def __init__(self):
        self.adapter = {'gs': AdapterTranLabelGS}

    def create(self, url, label_type):
        lid = LabelerInfoDownloader()
        label_info = lid.download(url, label_type)

        adapter = self.adapter.get(label_type)()
        labeler = TranLabeler()

        for li in label_info:
            labeler.add_label(adapter.adapt(li))
        return labeler


class LabelerInfoDownloader:
    def __init__(self):
        self.gs_replacee = 'edit#'
        self.gs_replacer = 'gviz/tq?tqx=out:csv&'

    def download(self, url, label_type) -> [dict]:
        if label_type == 'gs':
            new_url = url.replace(self.gs_replacee, self.gs_replacer)
            req = requests.get(new_url)
            dict_reader = csv.DictReader(StringIO(req.text))
            return list(dict_reader)
