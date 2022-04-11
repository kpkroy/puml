import configparser
import os
import datetime
from pathlib import Path


class LocalConfig:
    def __init__(self, project_name='profiler', data_dir_name='ProfileData'):
        self.config_parser = configparser.ConfigParser()
        self.project_name = project_name
        self.data_dir_name = data_dir_name
        self.date = None
        self.work_path = None
        self.config_file_path = None
        self.root_path = None

    def configure_all(self, use_date="") -> configparser.ConfigParser():
        self.configure_parent_path()
        self.configure_date(use_date)
        self.configure_path()
        self.configure_file_name()
        self.create_output_folder()
        with open(self.config_file_path, 'w') as configfile:
            self.config_parser.write(configfile)
        return self.config_parser

    def configure_parent_path(self):
        # file path setting
        self.find_project_root_folder()
        config_path = os.path.join(self.root_path, 'LocalConfig')
        self.config_file_path = os.path.join(config_path, 'config_file.ini')
        parent_path = Path(self.root_path).parent
        self.work_path = os.path.join(parent_path, self.data_dir_name)

    def configure_date(self, use_date):
        # date for downloaded data to re-use.
        current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M')
        self.config_parser['prefix'] = {'date': current_time}
        if use_date == "":
            # use previously downloaded.
            try:
                prev_conf = configparser.ConfigParser()
                prev_conf.read(self.config_file_path)
                self.config_parser['prefix'] = {'date': prev_conf['prefix'].get('date')}
                current_time = prev_conf['prefix'].get('date')
            except Exception as e:
                pass
        elif use_date:
            self.config_parser['prefix'] = {'date': use_date}
            current_time = use_date
        self.date = current_time

    def configure_path(self):
        self.config_parser['path'] = {'work': self.work_path,
                                      'date': os.path.join(self.work_path, self.date),
                                      'pool': os.path.join(self.work_path, 'pool'),
                                      'log': os.path.join(self.work_path, 'log'),
                                      'downloadedDb': os.path.join(self.work_path, 'downloadedDb'),
                                      'visual': os.path.join(self.work_path, 'visual'),
                                      'tempDb': os.path.join(self.work_path, 'tempDb'),
                                      'demo_data': os.path.join(self.work_path, 'demo_data')
                                      }

    def configure_file_name(self):
        self.config_parser['file'] = {'labeled': 'transaction_label.csv',
                                      'profiled': 'profile_label.csv',
                                      }

    def create_output_folder(self):
        if not os.path.exists(self.work_path):
            os.mkdir(self.work_path)
        if not os.path.exists(os.path.join(self.work_path, self.date)):
            os.mkdir(os.path.join(self.work_path, self.date))

        for x in self.config_parser['path']:
            if not os.path.exists(self.config_parser['path'].get(x)):
                os.mkdir(self.config_parser['path'].get(x))

    def find_project_root_folder(self):
        max_search_count = 5
        count = 0
        is_found = True
        # returns the first prev_path when is_found turns False.
        current_path = os.getcwd()
        prev_path = os.getcwd()
        while count < max_search_count and is_found:
            count += 1
            if self.project_name in current_path:
                is_found = True
                prev_path = current_path
                current_path = os.path.abspath(Path(current_path).parent)
            else:
                is_found = False
        if is_found:
            self.root_path = os.getcwd()
        else:
            self.root_path = prev_path


if __name__ == '__main__':
    from LocalConfig.arg_parse import ProfilerArgs

    ap = ProfilerArgs()
    lc = LocalConfig()
    conf = lc.configure_all(use_date=ap.get_working_date())


