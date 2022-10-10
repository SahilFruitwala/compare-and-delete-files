from os import remove
from os.path import getsize, getmtime

from config import BASE_DIR, BACKUP_DIR
from model import File
from utils import extract_files, measure_run_time, remove_empty_directories


def generate_file_objects(dir_path: str):
    all_files = []
    for file in extract_files(dir_path):
        all_files.append(
            File(
                name=file[0],
                extension=file[1],
                parent_directory=file[2],
                root_directory=dir_path,
                full_path=file[3],
                size=getsize(file[3]),
                updated_at=getmtime(file[3]),
            ),
        )
    return all_files


def remove_similar_files(base_dir: str, backup_dir: str):
    all_base_files = generate_file_objects(base_dir)
    all_backup_files = generate_file_objects(backup_dir)

    for (f1, f2) in zip(all_base_files, all_backup_files):
        if f1 == f2:
            remove(f2.full_path)


@measure_run_time
def main():
    remove_similar_files(BASE_DIR, BACKUP_DIR)
    remove_empty_directories(BACKUP_DIR)


if __name__ == "__main__":
    main()
