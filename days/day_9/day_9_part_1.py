from day import Day
import re
import numpy as np
import utils


class Day9Part1(Day):
    day = 9
    part = 1

    def get_sample_input(self):
        return ('2199943210\n'
                '3987894921\n'
                '9856789892\n'
                '8767896789\n'
                '9899965678')

    def parse_input(self):
        return np.array(tuple(map(tuple, self.input_text_lines)), dtype='<u1')

    def index_or_none(self, data, y, x):
        if 0 <= y < data.shape[0] and 0 <= x < data.shape[1]:
            return data[y, x]
        return None

    def is_low_point(self, data, y, x):
        val_at_yx = data[y, x]
        for offy, offx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (val := self.index_or_none(data, y + offy, x + offx)) is not None and val <= val_at_yx:
                return False
        return True

    def solve(self):
        data = self.parse_input()
        self.print_answer(sum(val + 1 for (y, x), val in np.ndenumerate(data) if self.is_low_point(data, y, x)))
