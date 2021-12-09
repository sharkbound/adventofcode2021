import statistics

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

    # old graphing code prior to optimization
    # def graph(self, data):
    #     import plotly.subplots
    #     fig = plotly.subplots.make_subplots(rows=2, cols=1)
    #     fig.add_trace(plotly.graph_objs.Scatter(x=data, y=[0] * len(data), mode='markers', name='starting positions'), row=1, col=1)
    #     fig.add_trace(plotly.graph_objs.Scatter(x=self.array_dist(data), y=[1] * (len(data) - 1), mode='markers', name='distance from next'),
    #                   row=2, col=1)
    #     fig.show()

    def solve(self):
        data = self.parse_input()
        # old solution via brute-force with a range
        # best_fuel_total = min(sum(abs(value - submarine) for submarine in data) for value in data)
        median = statistics.median(data)
        best_fuel_total = int(sum(abs(median - submarine) for submarine in data))
        self.print_answer(best_fuel_total)
