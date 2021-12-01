from pathlib import Path

INPUT_FILES_PATH = Path('./inputs/')
DAY_FILES_PATH = Path('./days/')


def create_day_folder_path(day_number):
    return Path(DAY_FILES_PATH / f'day_{day_number}')


def create_day_input_path(day_number):
    return Path(INPUT_FILES_PATH / f'day_{day_number}.txt')


def ask_int(prompt):
    while True:
        day = input(prompt)
        if not day.isnumeric():
            continue
        return int(day)


class CreateMode:
    FOLDER = 'FOLDER'
    FILE = 'FILE'


def create_if_not_exists(path: Path, type: str):
    if path.exists():
        return

    if type == CreateMode.FOLDER:
        path.mkdir(parents=True, exist_ok=True)

    elif type == CreateMode.FILE:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)


day = ask_int('enter day number >>> ')
day_input_file_path = create_day_input_path(day)
day_folder_path = create_day_folder_path(day)

create_if_not_exists(day_input_file_path, CreateMode.FILE)
create_if_not_exists(day_folder_path / f'day_{day}_part_1.py', CreateMode.FILE)
create_if_not_exists(day_folder_path / f'day_{day}_part_2.py', CreateMode.FILE)

print(f'done! created input and folder for day {day}!\n{day_input_file_path!s}\n{day_folder_path!s}')
