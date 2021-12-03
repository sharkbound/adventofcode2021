from pathlib import Path

INPUT_FILES_PATH = Path('./inputs/')
DAY_FILES_PATH = Path('./days/')


def create_day_input_file_path(day_number):
    return Path(INPUT_FILES_PATH / f'day_{day_number}.txt')


def create_day_folder_path(day_number):
    return Path(DAY_FILES_PATH / f'day_{day_number}')
