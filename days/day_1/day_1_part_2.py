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

    def solve(self):
        data = self.parse_input()
        prev = None
        total = 0
        
        for start in range(len(data) - 2):
            slice_ = data[start:start + 3]

            sum_ = sum(slice_)
            if prev is None:
                prev = sum_
                continue

            if sum_ > prev:
                total += 1

            prev = sum_
        print(f'day 1 part 2 answer: {total}')
