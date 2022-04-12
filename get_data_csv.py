from a_LocalConfig.local_config import LocalConfig
import gzip
import os
import pandas
import sqlite3


def get_valid_file_list(dir_path, file_has_string):
    if file_has_string:
        return [y for y in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, y))
                and file_has_string in y]
    else:
        return [y for y in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, y))]


if __name__ == '__main__':
    lc = LocalConfig()
    conf = lc.configure_all()
    file_path = r'd:\temp'
    todo = ['syrup-part1', 'syrup-part2', 'syrup-part3', 'syrup-part4']
    for t in todo:
        file_list = get_valid_file_list(file_path, t)
        db_file_name = f"{t}.db"
        conn = sqlite3.connect(os.path.join(conf['path']['downloadedDb'], db_file_name))

        for f in file_list:
            print(f"starting : {f}")
            with gzip.open(os.path.join(file_path, f), 'rb') as f_in:
                x = pandas.read_csv(f_in,
                                    delimiter=",", quotechar='"', encoding='utf-8-sig',
                                    escapechar='\\',
                                    on_bad_lines='warn',
                                    low_memory=False)
                x.to_sql('transactions', conn, if_exists='append', index=False)
                print(f"Done")
