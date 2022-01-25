from icecream import ic

from day import Day
import re
import numpy as np
import utils


class Day10Part1(Day):
    day = 10
    part = 1

    OPEN_TO_CLOSE = utils.build_mapping_from_iter('()[]{}<>')
    CLOSE_TO_OPEN = utils.reverse_mapping(OPEN_TO_CLOSE)
    SCORES = {
        ')': 3,
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
        return self.input_text_lines

    def solve(self):
        data = self.parse_input()
        score = 0
        for line in data:
            buffer = []
            for char in line:
                if char in self.OPEN_TO_CLOSE:
                    buffer.append(char)
                elif char in self.CLOSE_TO_OPEN and self.OPEN_TO_CLOSE[buffer.pop()] != char:
                    score += self.SCORES[char]
                    break
        self.print_answer(score)
