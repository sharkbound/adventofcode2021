from collections import namedtuple

from day import Day

"""

You need to use the binary numbers in the 
diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 

The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

"""

MOST_COMMON = object()
LEAST_COMMON = object()
FindBitResult = namedtuple('FindBitResult', 'bit count0 count1 data')


class Day3Part2(Day):
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
        return self.input_text_lines

    def get_column_values_at(self, index, data):
        return [row[index] for row in data]

    def find_bit(self, index, data, mode):
        values = self.get_column_values_at(index, data)
        count_0 = values.count('0')
        count_1 = values.count('1')

        if count_0 == count_1:
            return '1' if mode is MOST_COMMON else '0'
        elif mode is MOST_COMMON:
            return '0' if count_0 > count_1 else '1'
        else:
            return '0' if count_0 < count_1 else '1'

    def find_number(self, mode, data):
        valid = data.copy()
        for i in range(len(valid[0])):
            bit = self.find_bit(i, valid, mode)
            valid = [row for row in valid if row[i] == bit]
            if len(valid) == 1:
                return int(valid[0], 2)

    def solve(self):
        data = self.parse_input()

        print('day 3 part 2 answer is:', self.find_number(MOST_COMMON, data) * self.find_number(LEAST_COMMON, data))
