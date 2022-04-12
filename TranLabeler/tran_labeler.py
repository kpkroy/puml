from Transaction.adapted_tran import AdaptedTran
from TranLabeler.tran_label_info import TranLabelInfo


class TranLabeler:
    def __init__(self):
        self.keyword_table = {}
        self.cate_table = {}
        self.label_id_table = {}
        self.label_count = 0

    def reset(self):
        self.keyword_table = {}
        self.cate_table = {}
        self.label_id_table = {}
        self.label_count = 0

    def get_label(self, label_id: int) -> TranLabelInfo:
        return self.label_id_table.get(label_id)

    def add_label(self, adapted_lc: dict):
        self.label_count += 1
        keyword = adapted_lc.get('keyword')
        category_code = adapted_lc.get('category_code')
        new_label = TranLabelInfo(adapted_lc)

        if keyword:
            if keyword in self.keyword_table:
                self.keyword_table[keyword].append(self.label_count)
            else:
                self.keyword_table[keyword] = [self.label_count]
        if category_code:
            if category_code in self.cate_table:
                self.cate_table[category_code].append(self.label_count)
            else:
                self.cate_table[category_code] = [self.label_count]
        if keyword or category_code:
            self.label_id_table[self.label_count] = new_label

    def find_cate_labels(self, t: AdaptedTran) -> list:
        found_cate = self.cate_table.get(t.get_category_code())
        if found_cate:
            return found_cate
        else:
            return []

    def find_keyword_labels(self, t: AdaptedTran) -> list:
        key_matching_list = []
        for (key, value) in self.keyword_table.items():
            if key in t.get_merged_keyword():
                key_matching_list.extend(value)
        return key_matching_list

    def sort_labels(self, initial_match, t: AdaptedTran) -> set:
        if not initial_match:
            return set()
        label_id_set = set(initial_match)
        found_label_name = set()
        for li in label_id_set:
            label_info = self.get_label(li)
            if label_info is None:
                print('temp')
            if label_info.get_name() in found_label_name:
                continue
            if label_info.check_conditions(t):
                found_label_name.add(label_info.get_name())
        return found_label_name

    def find_labels(self, t: AdaptedTran) -> set:
        initial_match = []
        initial_match.extend(self.find_cate_labels(t))
        initial_match.extend(self.find_keyword_labels(t))
        found = self.sort_labels(initial_match, t)
        return found

