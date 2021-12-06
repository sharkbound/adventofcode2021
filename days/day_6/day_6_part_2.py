from collections import deque
from itertools import count

from icecream import ic

from day import Day
import re
import numpy as np
import utils


class Day6Part2(Day):
    day = 6
    part = 2

    def get_sample_input(self):
        return '3,4,3,1,2'

    def parse_input(self):
        return tuple(map(int, self.input_sample.split(',')))

    def preload_counts(self, data):
        counts = deque([0] * 9)
        for phase in data:
            counts[phase] += 1
        return counts

    def advance_phases(self, counts: deque):
        phase_0_count = counts[0]
        counts[0] = 0
        counts.rotate(-1)
        counts[8] = phase_0_count
        counts[6] += phase_0_count

    def solve(self):
        counts = self.preload_counts(self.parse_input())
        for _ in range(256):
            self.advance_phases(counts)
        self.print_answer(sum(counts))


"""
So, suppose you have a lanternfish with an internal timer value of 3:

day:
    1) its internal timer would become 2.
    2) its internal timer would become 1.
    3) its internal timer would become 0.
    4) its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
    5) the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.

A lanternfish that creates a new fish resets its timer to 6, not 7 
(because 0 is included as a valid timer value). 
The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, 
while each other number decreases by 1 if it was present at the start of the day.
"""
