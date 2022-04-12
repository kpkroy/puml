from abc import ABC


class TranFeeder(ABC):
    def __init__(self):
        self.query_info = {}
        self.uid_list = []
        self.source_path = ''
        self.source_file = ''
        self.qh = QueryHelper()
