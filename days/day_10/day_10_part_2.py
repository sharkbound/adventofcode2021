from icecream import ic

from day import Day
import re
import numpy as np
import utils


class Day10Part2(Day):
    day = 10
    part = 2

    OPEN_TO_CLOSE = utils.build_mapping_from_iter('()[]{}<>')
    CLOSE_TO_OPEN = utils.reverse_mapping(OPEN_TO_CLOSE)
    SCORES = {
        ')': 1,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    def get_sample_input(self):
        return ('[({(<(())[]>[[{[]{<()<>>\n'
                '[(()[<>])]({[<{<<[]>>(\n'
                '{([(<{}[<>[]}>{[]{[(<()>\n'
                '(((({<>}<{<{<>}{[]{[]{}\n'
                '[[<[([]))<([[{}[[()]]]\n'
                '[{[{({}]{}}([{[{{{}}([]\n'
                '{<[[]]>}<{[{[{[]{()[[[]\n'
                '[<(<(<(<{}))><([]([]()\n'
                '<{([([[(<>()){}]>(<<{{\n'
                '<{([{{}}[<[[[<>{}]]]>[]]')

    def parse_input(self):
        return self.input_sample_lines

    def solve(self):
        data = self.parse_input()
        score = 0
        valid_lines = []
        buffer = []
        for line in data:
            buffer.clear()
            for char in line:
                if char in self.OPEN_TO_CLOSE:
                    buffer.append(char)
                elif char in self.CLOSE_TO_OPEN and self.OPEN_TO_CLOSE[buffer.pop()] != char:
                    score += self.SCORES[char]
                    break
            else:  # no break
                valid_lines.append(line)
        self.print_answer(valid_lines)
