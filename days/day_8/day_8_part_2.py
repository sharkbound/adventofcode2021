from typing import NamedTuple

from icecream import ic

import utils
from day import Day


class Entry(NamedTuple):
    signals: tuple[frozenset]
    digits: tuple[frozenset]


class Day8Part2(Day):
    day = 8
    part = 2

    def get_sample_input(self):
        # return 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
        return ('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n'
                'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n'
                'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n'
                'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n'
                'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n'
                'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n'
                'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n'
                'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n'
                'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n'
                'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce')

    def parse_input(self) -> list[Entry]:
        return [
            Entry(
                signals=tuple(map(frozenset, (split := line.split('|'))[0].split())),
                digits=tuple(map(frozenset, split[1].split())),
            )
            for line in self.input_text_lines
        ]

    def solve(self):
        data = self.parse_input()
        total = 0
        for entry in data:
            known = {
                utils.first_where(entry.signals, utils.pred.eq_len(2)): '1',
                (seven_pattern := utils.first_where(entry.signals, utils.pred.eq_len(3))): '7',
                (four_pattern := utils.first_where(entry.signals, utils.pred.eq_len(4))): '4',
                utils.first_where(entry.signals, utils.pred.eq_len(7)): '8', utils.first_where(
                    entry.signals,
                    utils.pred.combine(
                        utils.pred.eq_len(6),
                        utils.pred.contains_eq_count(*seven_pattern, count=3),
                        utils.pred.contains_eq_count(*four_pattern, count=4),

                    )
                ): '9',
                utils.first_where(
                    entry.signals,
                    utils.pred.combine(
                        utils.pred.eq_len(6),
                        utils.pred.contains_eq_count(*seven_pattern, count=2),
                        utils.pred.contains_eq_count(*four_pattern, count=3),
                    )
                ): '6',
                utils.first_where(
                    entry.signals,
                    utils.pred.combine(
                        utils.pred.eq_len(5),
                        utils.pred.contains_eq_count(*four_pattern, count=2),
                    )
                ): '2',
                utils.first_where(
                    entry.signals,
                    utils.pred.combine(
                        utils.pred.eq_len(5),
                        utils.pred.contains_eq_count(*four_pattern, count=3),
                        utils.pred.contains_eq_count(*seven_pattern, count=3),
                    )
                ): '3',
                utils.first_where(
                    entry.signals,
                    utils.pred.combine(
                        utils.pred.eq_len(5),
                        utils.pred.contains_eq_count(*four_pattern, count=3),
                        utils.pred.contains_eq_count(*seven_pattern, count=2),
                    )
                ): '5',
            }
            known[utils.first_where_not(entry.signals, known.__contains__)] = '0'

            total += int(''.join(map(known.__getitem__, entry.digits)))

        self.print_answer(total)


"""
8 for first example line: 

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

a c e d g f b   scrambled mapping
| | | | | | |
c g b a e d f   actual mapping          

seems my issues in B getting bounds differently between 8 and 4 in the example



correct mapping for the above line                                           
               dddd                       ddd        aaa                                 
              e    a                     |   a      b   c                                
              e    a                     |   a      b   c                                
               ffff                        -         ddd                                 
              g    b                     |   b      e   f                                
              g    b                     |   b      e   f                                                                     
               cccc                       ---        ggg                                               
                                                 

*** Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. ***

* signals which control the segments have been mixed up on each display 
* submarine is trying to display numbers by signalling wires A-G
    those wires are connected to segments randomly. 
* the wire/segment connections are mixed up separately for each four-digit display
* All of the digits within a display use the same connections

              0:      1:      2:      3:      4:      5:      6:      7:      8:      9:
             aaaa    ....    aaaa    aaaa    ....    aaaa    aaaa    aaaa    aaaa    aaaa
            b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
            b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
             ....    ....    dddd    dddd    dddd    dddd    dddd    ....    dddd    dddd
            e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
            e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
             gggg    ....    gggg    gggg    ....    gggg    gggg    ....    gggg    gggg
             
             
So, the unique signal patterns would correspond to the following digits:

    acedgfb: 8
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    dab: 7
    cefabd: 9
    cdfgeb: 6
    eafb: 4
    cagedb: 0
    ab: 1


"""
