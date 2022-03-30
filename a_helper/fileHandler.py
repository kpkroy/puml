import os
import csv
import shutil
import time
import gzip


def get_valid_file_list(dir_path, file_has_string):
    if file_has_string:
        return [y for y in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, y))
                and file_has_string in y]
    else:
        return [y for y in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, y))]


def generate_from_csv(dir_path: str, file_name: str):
    file_path = os.path.join(dir_path, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as handler:
            for row in csv.DictReader(handler):
                yield row
    except:
        return []


def unzip_file(file_path, file_name, extender):
    new_name = file_name.split('.zip')[0] + '.' + extender
    with gzip.open(os.path.join(file_path, file_name), 'rb') as f_in:
        with open(os.path.join(file_path, new_name), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    time.sleep(1)
    return new_name


def export_csv_local(dir_path, file_name, export_data: [dict], opt='w+', file_field=None):
    if not export_data:
        return
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if file_field is None:
        file_field = export_data[0].keys()

    file_path = os.path.join(dir_path, file_name)
    file_exists = os.path.isfile(file_path)
    with open(file_path, opt, newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=file_field, quoting=csv.QUOTE_ALL)
        if file_exists and opt == 'a+':
            pass
        else:
            writer.writeheader()
        for data in export_data:
            writer.writerow(data)

