from day import Day
import re
import numpy as np
import utils


class Day8Part1(Day):
    day = 8
    part = 1

    def get_sample_input(self):
        return 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |\n  ' \
               'cdfeb fcadb cdfeb cdbaf'

    def parse_input(self):
        return ''

    def solve(self):
        data = self.parse_input()
