import statistics

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
        # found this quicker way of solving in another solution
        # the steps it takes is this:
        # 1) diff = 4
        # 2) 4 * (4 + 1) // 2
        # 3) 4 * 5 // 2
        # 4) 20 // 2
        # 5) 10
        # same as sum(range(1, diff + 1)), but faster
        return (diff := abs(target - position)) * (diff + 1) // 2

    def solve(self):
        data = self.parse_input()
        # old brute-force solution
        # i really don't like this brute-force approach, but i will revisit it later...
        # best_fuel_total = min(
        #     sum(self.calculate_movement_cost(pos, submarine) for submarine in data)
        #     for pos in range(min(data), max(data))
        # )
        # best_fuel_total = min(
        #     sum(self.calculate_movement_cost(pos, submarine) for submarine in data)
        #     for pos in range(min(data), max(data))
        # )
        # optimized solution below:
        # found from a solution on reddit
        # link: https://www.reddit.com/r/adventofcode/comments/rar7ty/comment/hnsdcw3/?utm_source=share&utm_medium=web2x&context=3
        mean = statistics.mean(data)
        best_fuel_total = int(sum(self.calculate_movement_cost(mean, submarine) for submarine in data))
        self.print_answer(best_fuel_total)
        # (96864235, 462)
        # timing:
        #   1349388500 NS
        # 	1349.3885 MS
        # 	1.3493885 SECONDS
