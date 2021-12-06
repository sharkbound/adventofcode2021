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
        return tuple(map(int, self.input_text.split(',')))

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
