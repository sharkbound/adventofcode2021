from collections import Counter
from typing import Literal

from icecream import ic

from day import Day

"""

You need to use the binary numbers in the 
diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 

The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

"""


class Day3Part1(Day):
    day = 3
    part = 2

    def get_sample_input(self):
        return ('00100\n'
                '11110\n'
                '10110\n'
                '10111\n'
                '10101\n'
                '01111\n'
                '00111\n'
                '11100\n'
                '10000\n'
                '11001\n'
                '00010\n'
                '01010')

    def parse_input(self):
        return self.input_sample_lines

    def most_and_least_common_at(self, index, data):
        counts = Counter((binary[index] for binary in data))
        return counts.most_common()

    def _fix_pair(self, preference_index, pair):
        if pair[0][1] == pair[1][1]:
            return '1' if preference_index == 0 else '0'
        return pair[preference_index][0]

    def filter_by_bit_position(self, data, mode: Literal['most', 'least']):
        compare = [
            # self.most_and_least_common_at(i, data)[0 if mode == 'most' else 1][0]
            self._fix_pair(0 if mode == 'most' else 1, self.most_and_least_common_at(i, data))
            for i in range(len(data[0]))
        ]

        for i, bit in enumerate(compare):
            data = [v for v in data if v[i] == bit]
            print(data, mode, bit)
            if len(data) == 1:
                return data[0]

    def solve(self):
        data = self.parse_input()
        bits = [self.most_and_least_common_at(i, data) for i in range(len(data[0]))]

        # epsilon_rate = int(''.join(pair[0][0] for pair in bits), 2)
        # gamma_rate = int(''.join(pair[1][0] for pair in bits), 2)

        oxygen_rate = ic(int(ic(self.filter_by_bit_position(data, mode='most')), 2))
        c02_scrubber_rate = ic(int(self.filter_by_bit_position(data, mode='least'), 2))

        # print(f'day 3 part 2 answer: {epsilon_rate * gamma_rate}')
