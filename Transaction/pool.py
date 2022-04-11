from a_helper import fileHandler as fh


class Pool:
    def __init__(self, uid_list: list, pool_path, pool_file_name):
        self.uid_set = set(uid_list)
        self.pool_path = pool_path
        self.pool_file = pool_file_name
        self.demo_info = None
        self.create_uid_list()

    def create_uid_list(self):
        try:
            temp = [x for x in fh.generate_from_csv(self.pool_path, self.pool_file)]
            for t in temp:
                self.uid_set.add(t.get('person_id'))
            self.uid_set.remove('')
        except:
            pass

    def get_user_id_list(self):
        return self.uid_set

    def update_demo_from_tran(self, demo: dict):
        pass

    def get_demo(self, uid):
        pass

