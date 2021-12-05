from collections import namedtuple

from icecream import ic

from day import Day
import re
import numpy as np
import utils

Line = namedtuple('Line', 'x1 y1 x2 y2')


class Day5Part1(Day):
    day = 5
    part = 2

    def get_sample_input(self):
        return ('0,9 -> 5,9\n'
                '8,0 -> 0,8\n'
                '9,4 -> 3,4\n'
                '2,2 -> 2,1\n'
                '7,0 -> 7,4\n'
                '6,4 -> 2,0\n'
                '0,9 -> 2,9\n'
                '3,4 -> 1,4\n'
                '0,0 -> 8,8\n'
                '5,5 -> 8,2')

    def parse_input(self):
        def _trans(line: str):
            return Line(*map(int, re.findall(r'\d+', line)))

        yield from utils.iter_with_terminator(
            self.input_text_lines,
            # predicate=lambda p: p.x1 == p.x2 or p.y1 == p.y2,
            transform=_trans,
            include_end_marker=False
        )

    def expand_line(self, line):
        # both x's match, so the y changed
        if line.x1 == line.x2:
            return [(line.x1, y) for y in self.normalized_range(line.y1, line.y2)]
        # both y's match, so the x changed
        elif line.y1 == line.y2:
            return [(x, line.y1) for x in self.normalized_range(line.x1, line.x2)]
        # 45 degree lines
        else:
            return list(zip(self.normalized_range(line.x1, line.x2), self.normalized_range(line.y1, line.y2)))

    def normalized_range(self, a, b):
        if a < b:
            return range(a, b + 1)
        return range(a, b - 1, -1)

    def solve(self):
        data = tuple(self.parse_input())
        overlapping = set()
        seen = set()
        for pos in utils.iter_flatten(map(self.expand_line, data), depth=1):
            if pos in seen:
                overlapping.add(pos)
            seen.add(pos)
        self.print_answer(len(overlapping))
