import numpy as np
import plotly.express as px
from icecream import ic

import utils.iterator
from day import Day


class Day7Part1(Day):
    day = 7
    part = 1

    def get_sample_input(self):
        return '16,1,2,0,4,2,7,1,2,14'

    def parse_input(self):
        return utils.get_all_ints(self.input_text, transform=utils.partial(np.fromiter, dtype=np.int))

    def array_dist(self, numbers):
        if len(numbers) == 1:
            return np.array(numbers)
        return np.fromiter((abs(a - b) for a, b in zip(numbers[:-1], numbers[1:])), dtype=np.int, count=len(numbers) - 1)

    def split_mid(self, numbers):
        return numbers[:len(numbers) // 2], numbers[len(numbers) // 2:]

    def lesser_dist_array_from_split(self, data):
        a, b = self.split_mid(data)
        return a if self.array_dist(a).sum() < self.array_dist(b).sum() else b

    def solve(self):
        data = self.parse_input()
        working_copy = data
        while len(working_copy) > 1:
            working_copy = self.lesser_dist_array_from_split(working_copy)
            print(working_copy)
        self.print_answer(sum(abs(a - working_copy[0]) for a in data))
        # should be 336120 according to another solution, i will revisit this later, part 2 is 96864235 seemingly
