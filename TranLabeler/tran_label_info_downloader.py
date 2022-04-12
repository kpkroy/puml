import requests
import csv
from io import StringIO


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



