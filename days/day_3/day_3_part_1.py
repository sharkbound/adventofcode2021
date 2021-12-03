from collections import Counter

from icecream import ic

from day import Day
import re
import numpy as np
import utils

"""

You need to use the binary numbers in the 
diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 

The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

"""


class Day3Part1(Day):
    day = 3
    part = 1

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
        return self.input_text_lines

    def most_and_least_common_at(self, index, data):
        counts = Counter((binary[index] for binary in data))
        return [pair[0] for pair in counts.most_common()]

    def solve(self):
        data = self.parse_input()
        bits = [self.most_and_least_common_at(i, data) for i in range(len(data[0]))]

        epsilon_rate = int(''.join(pair[0] for pair in bits), 2)
        gamma_rate = int(''.join(pair[1] for pair in bits), 2)

        print(f'day 3 part 2 answer: {epsilon_rate * gamma_rate}')
