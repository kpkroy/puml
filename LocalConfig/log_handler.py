from LocalConfig.local_config import configparser
import os
import logging
logging.basicConfig(format='%(asctime)s %(message)s - {%(name)s} {%(funcName)s}', datefmt='%H:%M:%S')


class LogHandler:
    def __init__(self, output_path=None):
        if output_path is None:
            self.logger_output = os.getcwd()
        else:
            conf: configparser.ConfigParser()
            self.logger_output = output_path
        self.formatter = logging.Formatter('%(asctime)s %(message)s - (%(name)s || %(funcName)s)', datefmt='%H:%M:%S')
        self.logger = logging.getLogger('labeler')
        self.logger.setLevel('INFO')
        self.fh = self.create_fh()
        self.logger.addHandler(self.fh)

    def create_fh(self):
        fh = logging.FileHandler(os.path.join(self.logger_output, 'profiler_log'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        return fh

    def create_ch(self):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        return ch

    def get_fh(self):
        return self.fh

    def get_logger(self, name=None):
        if name is None:
            return self.logger
        else:
            return logging.getLogger('labeler.' + name)
