from collections import namedtuple, Counter, defaultdict
from dataclasses import make_dataclass

from icecream import ic

from day import Day
import re
import numpy as np
import utils

LENGTH_TO_DIGIT = {
    2: '1',
    4: '4',
    3: '7',
    7: '8',
}


class Day8Part1(Day):
    day = 8
    part = 1

    def get_sample_input(self):
        return ('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n'
                'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n'
                'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n'
                'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n'
                'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n'
                'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n'
                'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n '
                'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n'
                'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n'
                'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce')

    def parse_input(self):
        return [
            utils.DotDict(
                signals=tuple(map(set, (split := line.split('|'))[0].split())),
                digits=tuple(map(set, split[1].split()))
            )
            for line in self.input_text_lines
        ]

    def solve(self):
        data = self.parse_input()
        counts = Counter()
        for item in data:
            for signal in item.signals:
                if match := LENGTH_TO_DIGIT.get(len(signal)):
                    counts[match] += item.digits.count(signal)

        # In the output values, how many times do digits 1, 4, 7, or 8 appear?
        self.print_answer(sum(map(counts.__getitem__, '1478')))


"""
*** Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. ***

* signals which control the segments have been mixed up on each display 
* submarine is trying to display numbers by signalling wires A-G
    those wires are connected to segments randomly. 
* the wire/segment connections are mixed up separately for each four-digit display
* All of the digits within a display use the same connections
"""
