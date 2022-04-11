from LocalConfig.arg_parse import TranLabelerArgs
from LocalConfig.local_config import LocalConfig
from LocalConfig.log_handler import LogHandler
from Transaction.pool import Pool
from LabelerTran.creator import TranLabelerCreator
from Transaction.transaction_feeder import TransactionFeeder
from LabelerTran.labeler_tran import TranLabeler

import os
import time
import subprocess


def setup_environment():
    venv_path = os.path.join(os.getcwd(), 'venv', 'Scripts')
    if not os.path.isdir(venv_path):
        venv_path = os.path.join(os.getcwd(), 'venv', 'bin')
    subprocess.run([os.path.join(venv_path, 'pip'), 'install', '-r', 'requirements.txt'])
    time.sleep(1)


if __name__ == '__main__':
    pa = TranLabelerArgs()
    lc = LocalConfig('profiler')
    conf = lc.configure_all(use_date=pa.get_working_date())
    lh = LogHandler(conf['path']['date'])
    logger = lh.get_logger('profiler').info('> start profiling ')
    setup_environment()

    tran_label_url = 'https://docs.google.com/spreadsheets/d/17qBpAYLUT5YaujniLpxWKd9cPCW_xHQ8X-OPShjiEgs/edit#gid=0'
    tc = TranLabelerCreator()
    labeler = tc.create(tran_label_url, 'gs')
    labeler: TranLabeler

    pm = Pool(pa.get_pool_id_list(), conf['path']['pool'], pa.get_pool_file())

    source_path = conf['path'][pa.get_db_path()]
    source_file = pa.get_db_file()
    label_result = []
    tf = TransactionFeeder(pa.get_from_date(),
                           pa.get_to_date(),
                           pm.get_user_id_list(),
                           source_path,
                           source_file,
                           lh)

    for adt in tf.generate():
        labeled = labeler.find_labels(adt)
        print(labeled)
        label_result.append(labeled)
    print('temp')




