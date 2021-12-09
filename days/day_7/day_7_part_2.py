import numpy as np
import plotly.express as px
from icecream import ic

import utils.iterator
from day import Day


class Day7Part2(Day):
    day = 7
    part = 2

    def get_sample_input(self):
        return '16,1,2,0,4,2,7,1,2,14'

    def parse_input(self):
        return utils.get_all_ints(self.input_text, transform=utils.partial(np.fromiter, dtype=np.int))

    # i wanted to use these two functions to reduce complexity, but my approach did not work whatsoever...

    # def array_dist(self, numbers):
    #     if len(numbers) == 1:
    #         return np.array(numbers)
    #     return np.fromiter((abs(a - b) for a, b in zip(numbers[:-1], numbers[1:])), dtype=np.int, count=len(numbers) - 1)
    #
    # def split_mid(self, numbers):
    #     return numbers[:len(numbers) // 2], numbers[len(numbers) // 2:]

    # def graph(self, data):
    #     import plotly.subplots
    #     fig = plotly.subplots.make_subplots(rows=2, cols=1)
    #     fig.add_trace(plotly.graph_objs.Scatter(x=data, y=[0] * len(data), mode='markers', name='starting positions'), row=1, col=1)
    #     fig.add_trace(plotly.graph_objs.Scatter(x=self.array_dist(data), y=[1] * (len(data) - 1), mode='markers', name='distance from next'),
    #                   row=2, col=1)
    #     fig.show()

    def solve(self):
        data = self.parse_input()
        # i really don't like this brute-force approach, but i will revisit it later...
        best_fuel_total = min(sum(abs(value - submarine) for submarine in data) for value in data)
        self.print_answer(best_fuel_total)
        # should be 336120 according to another solution, i will revisit this later, part 2 is 96864235 seemingly
