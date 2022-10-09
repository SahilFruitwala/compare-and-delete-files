from datetime import datetime
from os import path, rmdir, remove, walk
from time import time, ctime


def convert_to_datetime(timestamp: float) -> str:
    """ take timestamp as float and returns full date and time """
    return ctime(timestamp)


def measure_run_time(func):
    """ decorate to time given function """
    def timeit_wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f"--- {end_time - start_time} seconds ---")

    return timeit_wrapper


def write_list_to_file(file_list: list):
    """ write filename from list of filenames """
    today = datetime.today().strftime('%Y-%m-%d')
    with open(f'{today} - Deletion Error.txt', 'w', encoding="UTF-8") as file:
        for filename in file_list:
            file.write(f"{filename}\n")
    print(f'Added list of files failed to delete are saved in "{today} - Deletion Error.txt"')


def remove_empty_directories(root_dir: str) -> None:
    """ Generate list of all directory and subdirectory, and remove the empty ones"""
    all_dirs = []
    for (dir_path, dir_names, _) in walk(root_dir):
        for dirname in dir_names:
            all_dirs.append(path.join(dir_path, dirname))

    error_file_list = []
    for i in range(len(all_dirs) - 1, -1, -1):
        temp_path = path.join(all_dirs[i], '.DS_Store')
        if path.exists(temp_path):
            try:
                remove(temp_path)
            except:
                print(temp_path)
        try:
            rmdir(all_dirs[i])
        except:
            error_file_list.append(all_dirs[i])

    if len(error_file_list) > 0:
        write_list_to_file(error_file_list)


def extract_files(root_dir: str) -> list[(str, str, str)]:
    """
    Go through every directory and subdirectory and return list of tuples
    tuple contains filename, file's parent directory, file's absolute path
    """
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
