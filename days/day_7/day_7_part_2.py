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

    def calculate_movement_cost(self, target, position):
        return sum(range(1, abs(target - position) + 1))

    def solve(self):
        data = self.parse_input()
        # i really don't like this brute-force approach, but i will revisit it later...
        best_fuel_total = min(
            (sum(self.calculate_movement_cost(pos, submarine) for submarine in data)
             for pos in range(min(data), max(data))), key=lambda x: x[0]
        )
        self.print_answer(best_fuel_total)
        # (96864235, 462)
