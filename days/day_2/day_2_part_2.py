from collections import namedtuple

from day import Day

Instruction = namedtuple('Instruction', 'command units')


class Day2Part1(Day):
    day = 2
    part = 2

    def get_sample_input(self):
        return ('forward 5\n'
                'down 5\n'
                'forward 8\n'
                'up 3\n'
                'down 8\n'
                'forward 2')

    def parse_input(self) -> list[Instruction]:
        return [
            Instruction(command=command, units=int(unit))
            for command, unit in map(str.split, self.input_text_lines)
        ]

    def solve(self):
        data = self.parse_input()
        x = 0
        y = 0
        aim = 0

        for instr in data:
            match instr:
                case Instruction('up', units):
                    aim -= units
                case Instruction('down', units):
                    aim += units
                case Instruction('forward', units):
                    x += units
                    y += aim * units
                case Instruction('back', units):
                    x -= units
                    y -= aim * units

        print(f'day 2 part 2 answer: {x * y}')
