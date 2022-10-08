import time
from os import path, rmdir, remove, walk


def convert_to_datetime(timestamp: float) -> str:
    """ take timestamp as float and returns full date and time """
    return time.ctime(timestamp)


def remove_empty_directories(root_dir: str) -> None:
    all_dirs = []
    for (dir_path, dir_names, _) in walk(root_dir):
        for dirname in dir_names:
            all_dirs.append(path.join(dir_path, dirname))
    for i in range(len(all_dirs) - 1, -1, -1):
        temp_path = path.join(all_dirs[i], '.DS_Store')
        if path.exists(temp_path):
            remove(temp_path)
        rmdir(all_dirs[i])


def extract_files(root_dir: str) -> list[(str, str, str)]:
    list_of_files = []
    for (dir_path, _, file_names) in walk(root_dir):
        list_of_files.extend(
            (
                filename,
                dir_path.split('/')[-1],
                path.join(dir_path, filename)
            ) for filename in file_names
        )

    return list_of_files
