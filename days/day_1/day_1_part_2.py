from day import Day
import re
import numpy as np
import utils


class Day1Part1(Day):
    day = 1
    part = 2

    def get_sample_input(self):
        return ('199\n'
                '200\n'
                '208\n'
                '210\n'
                '200\n'
                '207\n'
                '240\n'
                '269\n'
                '260\n'
                '263')

    def parse_input(self):
        return tuple(map(int, self.input_text_lines))

    def sliding_window(self, window_size, collection):
        for i in range(0, len(collection) - window_size + 1):
            yield collection[i:i + window_size]

    def solve(self):
        data = self.parse_input()
        prev = None
        total = 0

        for window in self.sliding_window(3, data):
            sum_ = sum(window)

            if prev is None:
                prev = sum_
                continue

            if sum_ > prev:
                total += 1

            prev = sum_
        print(f'day 1 part 2 answer: {total}')
