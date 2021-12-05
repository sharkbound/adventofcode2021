from collections import deque
from dataclasses import dataclass

import numpy as np

import utils
from day import Day


class LineType:
    BOARD_LINE = 'BOARD_LINE'
    HEADER = 'HEADER'
    SEPARATOR = 'SEPARATOR'


@dataclass
class Board:
    grid: np.ndarray
    number_locations: dict[int, tuple[int, int]] = None
    flattened: np.ndarray = None

    def __post_init__(self):
        self.number_locations = {value: index for index, value in np.ndenumerate(self.grid)}
        self.flattened = np.ravel(self.grid)

    def active_indexes_from_numbers(self, active_numbers):
        return [index for number, index in self.number_locations.items() if number in active_numbers]


class Day4Part1(Day):
    day = 4
    part = 2

    def get_sample_input(self):
        return ('7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n'
                '\n'
                '22 13 17 11  0\n'
                ' 8  2 23  4 24\n'
                '21  9 14 16  7\n'
                ' 6 10  3 18  5\n'
                ' 1 12 20 15 19\n'
                '\n'
                ' 3 15  0  2 22\n'
                ' 9 18 13 17  5\n'
                '19  8  7 25 23\n'
                '20 11 10 24  4\n'
                '14 21 16 12  6\n'
                '\n'
                '14 21 17 24  4\n'
                '10 16 15  9 19\n'
                '18  8 23 26 20\n'
                '22 11 13  6  5\n'
                ' 2  0 12  3  7')

    def parse_input(self):
        drawing_numbers = deque()
        buffer = []
        boards = []

        def _trans(x):
            if ',' in x:
                return x, LineType.HEADER
            if x:
                return x, LineType.BOARD_LINE
            return LineType.SEPARATOR

        for pair in utils.iter_with_terminator(self.input_text_lines, transform=_trans, end_marker=LineType.SEPARATOR):
            match pair:
                case (x, LineType.HEADER):
                    drawing_numbers.extend(map(int, x.split(',')))
                case (x, LineType.BOARD_LINE):
                    buffer.append([int(x) for x in x.split()])
                case LineType.SEPARATOR if buffer:
                    boards.append(buffer)
                    buffer = []

        return drawing_numbers, [Board(np.array(b)) for b in boards]

    def check_win(self, board: Board, drawn_numbers: set[int]):
        for y, x in board.active_indexes_from_numbers(drawn_numbers):
            if all(val in drawn_numbers for val in board.grid[y, :]) or all(val in drawn_numbers for val in board.grid[:, x]):
                return True
        return False

    def solve(self):
        numbers, boards = self.parse_input()
        drawn = set()
        last_draw = None
        last_board = None

        while boards:
            last_draw = numbers.popleft()
            drawn.add(last_draw)
            boards = [b for b in boards if not self.check_win(b, drawn)]
            if boards:
                last_board = boards[-1]

        print(sum(set(last_board.flattened) - drawn) * last_draw)
