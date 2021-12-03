import requests

from utils import ask_int, create_day_input_file_path

ADVENT_OF_CODE_URL = 'https://www.adventofcode.com/'
ADVENT_OF_CODE_INPUT_URL = f'{ADVENT_OF_CODE_URL}/2021/day/{{day}}/input'


def read_session():
    with open('./secrets/session.txt', 'r') as file:
        return file.read().strip()


def get(day):
    return requests.get(
        ADVENT_OF_CODE_INPUT_URL.format(day=day),
        cookies={
            'User-Agent': 'advent-of-code-input-fetcher',
            'session': read_session()
        }
    )


day = ask_int('enter day to fetch input for: ')
# data = get(day)
# data.raise_for_status()

# create_day_input_file_path(day).write_text(data.text)
print(f'\n\n***\ndone getting input for day: {day}\n\nit was dumped to file: {create_day_input_file_path(day)!s}\n***')
