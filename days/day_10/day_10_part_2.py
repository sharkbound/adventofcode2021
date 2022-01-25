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
        ']': 2,
        '}': 3,
        '>': 4,
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
        scores = []
        buffer = []
        for line in data:
            buffer.clear()
            for char in line:
                if char in self.OPEN_TO_CLOSE:
                    buffer.append(char)
                elif char in self.CLOSE_TO_OPEN and self.OPEN_TO_CLOSE[buffer.pop()] != char:
                    break
            else:  # no break
                score = 0
                for char in map(self.OPEN_TO_CLOSE.__getitem__, reversed(buffer)):
                    score = score * 5 + self.SCORES[char]
                scores.append(score)

        self.print_answer(int(np.median(scores)))
