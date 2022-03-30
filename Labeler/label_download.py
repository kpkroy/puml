import requests
from io import StringIO
import csv


class LabelerInfoDownloader:
    def __init__(self, tran_label_url=None):
        if tran_label_url is None:
            tran_label_url = 'https://docs.google.com/spreadsheets/d/1n30KN0i32guPJQnG8lpnKuxFt0NptZv-_R7OCzOZsBE' \
                             '/edit#gid=0'
        self.url = {'transaction': tran_label_url}

    def get_adapter(self, condition_type):
        x = self.adapter.get(condition_type)()
        return x

    def get_url(self, condition_type):
        ori_url = self.url.get(condition_type)
        replacee = 'edit#'
        replacer = 'gviz/tq?tqx=out:csv&'
        url = ori_url.replace(replacee, replacer)
        return url

    def get_label_conditions(self, condition_type) -> list:
        url = self.get_url(condition_type)
        req = requests.get(url)
        dict_reader = csv.DictReader(StringIO(req.text))
        return list(dict_reader)
