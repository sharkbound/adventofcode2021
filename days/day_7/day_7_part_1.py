import numpy as np
import plotly.express as px

import utils.iterator
from day import Day


class Day7Part1(Day):
    day = 7
    part = 1

    def get_sample_input(self):
        return '16,1,2,0,4,2,7,1,2,14'

    def parse_input(self):
        return list(utils.get_all_ints(self.input_sample))

    def solve(self):
        data = self.parse_input()
        plt = px.scatter(x=data, y=[0] * len(data))
        plt.show()
        print(np.mean(data, dtype=int))
