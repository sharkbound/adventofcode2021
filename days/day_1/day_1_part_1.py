from day import Day
import re
import numpy as np
import utils


class Day1Part1(Day):
    day = 1
    part = 1

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
        return map(int, self.input_text_lines)

    def solve(self):
        data = self.parse_input()
        prev = next(data)
        total = 0
        for val in data:
            if val > prev:
                total += 1
            prev = val
        print(f'day 1 part 1 answer: {total}')
