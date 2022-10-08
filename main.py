from os import remove
from os.path import getsize, getmtime

from model import File
from utils import extract_files, remove_empty_directories

base_dir = '/Users/sahil/Code/Webstorm/gratitude.sahilfruitwala.com'
backup_dir = '/Users/sahil/Code/Pycharm/gratitude.sahilfruitwala.com'

all_base_files = []
for file in extract_files(base_dir):
    all_base_files.append(File(file[0], file[1], base_dir, file[2], getsize(file[2]), getmtime(file[2])))

all_backup_files = []
for file in extract_files(backup_dir):
    all_backup_files.append(File(file[0], file[1], backup_dir, file[2], getsize(file[2]), getmtime(file[2])))

for (f1, f2) in zip(all_base_files, all_backup_files):
    if f1 == f2:
        remove(f2.full_path)

remove_empty_directories(backup_dir)

